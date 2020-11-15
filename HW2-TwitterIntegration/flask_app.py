from flask import Flask
from app import app

@app.route('/')
def display():
    return "Looks like it works!"

if __name__=='__main__':
    app.run()