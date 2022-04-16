from flask import Flask,render_template,redirect,url_for
app=Flask(__name__)

@app.route('/')
def index():
    return "Hello there !! My name is Vrushabh Jinde and this Flask web deveoplment with Krish Naik"

@app.route('/members')
def members():
    return "Hello there !! My name is Vrushabh Jinde and this is members function."

@app.route('/pass/<int:score>')
def success(score):
    return "The person has passed and the marks"+" "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "<html><body><h1>The student has faild!</h1></body></html>"

@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result="Fail"
    else:
        result="Pass"
    return redirect(url_for(result,score=marks))

if __name__=='__main__':
    app.run(debug=True)