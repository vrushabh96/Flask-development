from flask import Flask,redirect,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Web Development using FLASK!!!"

if __name__=='__manin__':
    app.run(debug=True)