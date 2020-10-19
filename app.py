from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import MinMaxScaler
app = Flask(__name__,template_folder='templates')
with open('loan_classifier.pkl','rb') as f:
    model=pickle.load(f)

standard_to = MinMaxScaler()
@app.route("/", methods=['GET','POST'])
def main():
    #Fuel_Type_Diesel=0
    if request.method == 'POST':
        applicant_income=request.form.get('applicant_income')
        co_applicant_income=request.form.get('co_income')
        amount=request.form.get('amount')
        term=request.form.get('term')
        credit_history=request.form.get('credit_history')
        marital_status=request.form.get('marital_status')
        graduate=request.form.get('graduate')
        self_employed=request.form.get('self_emp')
        property_area=request.form.get('property_area')
        if credit_history=='Yes':
           c_history=1
        else:
           c_history=0
        if(marital_status=='Married'):
            m_status=1
        else:
            m_status=0	
        if(graduate=='Yes'):
            grad=0
        else:
            grad=1
        if self_employed=='Yes':
           selfemp=1
        else:
           selfemp=0
        if property_area=='Rural':
           property_area_semiurban=0
           property_area_urban=0
        if property_area=='Urban':
           property_area_semiurban=0
           property_area_urban=1
        if property_area=='Semi-Urban':
           property_area_semiurban=1
           property_area_urban=0
        #arr=[np.array([applicant_income,co_applicant_income,amount,term,c_history,m_status,grad,selfemp,property_area_semiurban,property_area_urban])]
        #a=np.nan_to_num(arr)
        prediction=model.predict([[applicant_income,co_applicant_income,amount,term,c_history,m_status,grad,selfemp,property_area_semiurban,property_area_urban]])
        print(prediction)
        #output=round(prediction[0],2)
        if prediction==0:
            return render_template('main.html',result="your loan can be approved")
        else:
            return render_template('main.html',result="your loan cannot be approved")
        
    else:
        return render_template('main.html')

if __name__=="__main__":
    app.run(debug=True)
