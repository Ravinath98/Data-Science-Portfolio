from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)


#@app.route('/<string:name>')
@app.route('/')
#def hello_world(name:str):  # put application's code here
def home():
    #return '<h1>Hello World!</h1>' #HTML response
    #return jsonify(data=name) #json response
    return  render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['name']
        country=request.form['country']
        return redirect(url_for('user',usr=user,ctr=country))
    else:
        return render_template('login.html')

@app.route('/<usr>/<ctr>')
def user(usr,ctr):
    #return f"<h1>{usr}</h1>"
    return render_template('user.html',user=str(usr),country=str(ctr))


if __name__ == '__main__':
    app.run()
