from flask import Flask

app = Flask(__name__)

@app.route('/index/n')
def sum():
    while(n!=0):
        a=n%10
        b=b+a
        n=n//10
    return 'sum of integer'
if __name__ =='__main__':
    app.run(debug=True)
