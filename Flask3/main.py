# Intergrate HTML with Flask
#HTTP verb GET and POST


#Jinja2 template 

'''{%....%} for statements'''
'''{{  }} for expressions to print out'''
'''{#  #} this is for comments'''
from flask import Flask,render_template,redirect,url_for,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index2.html')

@app.route('/members')
def members():
    return "Hello there !! My name is Vrushabh Jinde and this is members function."

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>50:
        res="Pass"
    else:
        res="Fail"
    exp={'score':score,'res':res}
    return render_template('result2.html',result=score)

@app.route('/fail/<int:score>')
def fail(score):
    return "<html><body><h1>The student has faild!!!</h1></body></html>"

@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result="Fail"
    else:
        result="Pass"
    return redirect(url_for(result,score=marks))

#Result checker html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        ds=float(request.form['ds'])
        dbms=float(request.form['dbms'])
        total_score=(science+maths+ds+dbms)/4
    res=""
    if total_score>=50:
        res="success"
    else:
        res="fail"
    print(res)
    return redirect(url_for(res,score=total_score))    



if __name__=='__main__':
    app.run(debug=True)