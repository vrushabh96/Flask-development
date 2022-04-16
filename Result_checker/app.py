from flask import Flask,redirect,url_for
app=Flask(__name__)


@app.route("/")
def welcome():
    return '<html><body><h1>Welcome to Result checker system!</h1></body></html>'

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and result is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and result is "+ str(score)

@app.route('/results/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))
    

if __name__=="__main__":
    app.run(debug=True)