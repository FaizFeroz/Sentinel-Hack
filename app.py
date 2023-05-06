import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    # form_features = [int(x) for x in request.form.values()] #getting the form features
    form_values=[request.form.values()]

    # values_list = []
    # values_list.append(list(request.form.values())[0])
    #l=[]
    # print(values_list)

    # for i in request.form.items():
    #     print(i)
    #     l.append()

    l=[]
    form_values = []
    for key, value in request.form.items():
        form_values.append(value)
    for i in form_values:
        print(i)

    for i in range(len(form_values)):
        if(i==2 or i==5 or i==6 or i==7 or i==8 or i==10):
            l.append(int(form_values[i]))
        else:
            if(i==0):
                if(form_values[i]=='Male'):
                    l.append(1)
                else:
                    l.append(0)
            if(i==1):
                if(form_values[i]=='Yes'):
                    l.append(1)
                else:
                    l.append(0)
            if(i==3):
                if(form_values[i]=='Graduate'):
                    l.append(1)
                else:
                    l.append(0)
            if(i==4):
                if(form_values[i]=='Yes'):
                    l.append(1)
                else:
                    l.append(0)
            if(i==9):
                if(form_values[i]=='Urban'):
                    l.append(0)
                if(form_values[i]=='Rural'):
                    l.append(1)
                if(form_values[i]=='Semiurban'):
                    l.append(2)
    print(l)        

    features=[np.array(l)]
    prediction=model.predict(features)
    ans=prediction[0]
    if(ans==0):
        ans="Not approved"
    if(ans==1):
        ans="Approved"
    return render_template("index.html",prediction_text=f"The loan can be {ans}")        
            
      

    




#array reshaping for model
    # features = [np.array(form_features)]
    # prediction = model.predict(features)
    # return render_template("index.html", prediction_text = f"The loan can be {prediction}")

if __name__ == "__main__":
    flask_app.run(debug=True)