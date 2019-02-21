library(survival)
library(survminer)
library(cgdsr)
library(sparklyr)
library(dplyr)
library(shiny)
library(miniUI)

#cgds <- cgdsr::CGDS("http://www.cbioportal.org/public-portal/")
#Studies<- cgdsr::getCancerStudies(cgds)
#clinicalData <- cgdsr::getClinicalData(cgds, "gbm_tcga_pub_all")

sc <- spark_connect(master = "local", version = "2.4.0")

clinicalData_tbl <- dplyr::copy_to(sc, clinicalData, overwrite = TRUE)

iris_tbl <- copy_to(sc, iris, "iris", overwrite = TRUE)

# Create the gadget user interface
ui <- miniPage(
  gadgetTitleBar("ggplot Data after spark transformation"),
  
  miniTabstripPanel(
    miniTabPanel("Plot", icon = icon("area-chart"),
                 miniContentPanel(
                   plotOutput("clinicalDataPlot")
                 )
    ),
    miniTabPanel("ML", icon = icon("table"),
                 miniContentPanel(
                   plotOutput("iris_model_plot")
                 )
    )
    
  )
)
# Create the shiny gadget functions
server <- function(input, output){
  
  ## import data from spark to R
  clinicalData_tbl <- spark_read_table(sc, 'clinicaldata')
  iris_tbl <- spark_read_table(sc, 'iris')
  
  start_time <- Sys.time()
  spark_clinicalData_trans <- reactive({
    clinicalData_tbl %>%
      mutate(OS_STATUS = regexp_replace(OS_STATUS, "LIVING", "0")) %>%
      mutate(OS_STATUS = regexp_replace(OS_STATUS, "DECEASED", "1")) %>%
      mutate(DFS_STATUS = regexp_replace(DFS_STATUS, "^$|^ $", "DiseaseFree")) %>%
      filter(!is.na(OS_STATUS)) %>%
      mutate(OS_STATUS = as.numeric(OS_STATUS)) %>%
      arrange(is.na(OS_MONTHS), OS_MONTHS) %>%  ## OUFFF put Nan at the end of the column
      mutate(DiseaseFree = ifelse(DFS_STATUS == "DiseaseFree", 1, 0)) %>% 
      as.data.frame() %>%
      mutate( n_DiseaseFree = cumsum(as.numeric(DiseaseFree == 1 ))) %>%
      mutate( n_Recurred = cumsum(as.numeric(DiseaseFree == 0 ))) %>%
      collect()
    
  })
  
  # DOES NOT WORK
  # spark_iris_model <- reactive({
  #    iris_tbl %>%
  #     select(Petal_Width, Petal_Length) %>%
  #     ml_linear_regression(Petal_Length ~ Petal_Width) %>%
  #     collect()
  #   
  # }) 
  
  spark_iris_data <- reactive({
    iris_tbl %>%
      select(Petal_Width, Petal_Length)
  })
  
  
  output$clinicalDataPlot <- renderPlot({
    ggplot(spark_clinicalData_trans(), 
           aes(x = OS_MONTHS, y = value, color = variable)) +
      geom_point(aes(y = n_DiseaseFree, col = "n_DiseaseFree")) +
      geom_point(aes(y = n_Recurred, col = "n_Recurred"))  +
      labs(title = paste("Running Time = ", Sys.time() - start_time, " s"))
  })
  
  output$iris_model_plot <- renderPlot({
    
    #ml_model <-  spark_iris_model() DOES NOT WORK
    
    ## Predict linear model
    ml_model <-  iris_tbl %>%
      select(Petal_Width, Petal_Length) %>%
      ml_linear_regression(Petal_Length ~ Petal_Width)
    
    # get ggplot
      ggplot(spark_iris_data(), ## select data
             aes(Petal_Length, Petal_Width)) +
      geom_point(aes(Petal_Width, Petal_Length), size = 2, alpha = 0.5) +
      geom_abline(aes(slope = ml_model$coefficients[2],
                     intercept = ml_model$coefficients[1]),
                color = "red") +
      labs(
        x = "Petal Width",
        y = "Petal Length",
        title = "Linear Regression: Petal Length ~ Petal Width",
        subtitle = "Use Spark.ML linear regression to predict petal length as a function of petal width."
      )
  })
  
  observeEvent(input$done, {
    stopApp(TRUE)
  })
}
# Run the gadget
runGadget(ui, server)
