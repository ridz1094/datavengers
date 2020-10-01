from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
    
# Defining the home page of our website
@app.route("/") 
def home():
    return "Hello! this is Twitter! <h1>Hi</h1>" 

def user(name):
    return f"Hi there {name}!"

if __name__== "__main__":
    app.run()
