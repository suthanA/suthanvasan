from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    a=55
    b=33
    
    c=a+b
    
    d=a-b
    
    e=a*b
    f=a//b
    return render_template('mathcal.html',**locals())
if __name__ =='__main__':
    app.run(debug=True)
    