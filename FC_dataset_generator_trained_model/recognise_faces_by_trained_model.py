####################################################
# Modified by Nazmi Asri                           #
# Original code: http://thecodacus.com/            #
# All right reserved to the respective owner       #
####################################################

# Import OpenCV2 for image processing
import cv2
import glob
# Import numpy for matrices calculations
import numpy as np

import os 

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


def getNames_Ids(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #create empth face list
    names=[]
    #create empty ID list
    Ids=[]
    
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        #pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        #imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        #Id=int(os.path.split(imagePath)[-1].split(".")[0])
        Id = int(imagePath.split('.')[1])
        # get the name
        name = str(os.path.basename(imagePath).split('.')[0])
        # extract the face from the training image sample
        #faces=detector.detectMultiScale(imageNp)
        #If a face is there then append that in the list as well as Id of it
        Ids.append(Id)
        names.append(name)
        
    return names,Ids


# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("models/")

# Load the trained mode
recognizer.read('models/trained_model.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# get names for  Ids
names, Ids = getNames_Ids('dataSet')

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

# Loop
while True:
    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)
    
    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)
         
        # Recognize the face belongs to which ID
        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
        # get Name
        name = names[Ids.index(Id)]
        
        # Check the ID if exist 
        text = str(name + "  {0:.2f}%").format(round(100 - confidence, 2))

        # Put text describe who is in the picture
        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, text,  (x,y-40), font, 1, (255,255,255), 3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('Capture',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Stop the camera
cam.release()
# Close all windows
cv2.destroyAllWindows()
