from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle

#create the flask app.....
app = Flask(__name__)

#load pickle model
model=pickle.load(open('model_concrete.pkl','rb')) #rb->read the pickle file



@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/predict',methods=['POST']) #post becase receive the independent variable values..
def predict():
    float_features=[float(x) for x in request.form.values()] #convert input variables to float values
    features=[np.array(float_features)] #convert to numpy array
    prediction=model.predict(features)

    return render_template('index.html',prediction_text='The strength is {}'.format(prediction))
if __name__ == '__main__':
    app.run()
