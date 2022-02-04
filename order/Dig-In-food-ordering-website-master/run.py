from app import app

# Adding Secret Key to our App
app.secret_key = 'make this hard to guess!'

app.run(debug=True)
