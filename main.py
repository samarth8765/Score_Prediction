import numpy as np
import model_predict

from flask import Flask,render_template, redirect, url_for,request
app = Flask(__name__,static_folder="images")

@app.route('/')
def hello_world():
    return render_template('index.html')


def which_ground(set_1):
    if set_1 == '0':
        return [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif set_1 == '1':
        return [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif set_1 == '2':
        return [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
    elif set_1 == '3':
        return [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif set_1 == '4':
        return [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]    
    elif set_1 == '5':
        return [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]    
    elif set_1 == '6':
        return [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]    
    elif set_1 == '7':
        return [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]    
    elif set_1 == '8':
        return [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    elif set_1 == '9':
        return [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0] 
    elif set_1 == '10':
        return [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0] 
    elif set_1 == '11':
        return [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0] 
    elif set_1 == '12':
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0] 
    elif set_1 == '13':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0] 
    elif set_1 == '14':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0] 
    elif set_1 == '15':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0] 
    elif set_1 == '16':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0] 
    elif set_1 == '17':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] 

def which_battingbowling(set_2):
    if set_2 == '0':
        return [1,0,0,0,0,0,0,0]
    elif set_2 == '1':
        return [0,1,0,0,0,0,0,0]
    elif set_2 == '2':
        return [0,0,1,0,0,0,0,0]
    elif set_2 == '3':
        return [0,0,0,1,0,0,0,0]
    elif set_2 == '4':
        return [0,0,0,0,1,0,0,0]
    elif set_2 =='5':
        return [0,0,0,0,0,1,0,0]
    elif set_2 == '6':
        return [0,0,0,0,0,0,1,0]
    elif set_2 == '7':
        return [0,0,0,0,0,0,0,1]

@app.route('/form',methods=['GET','POST'])
def return_answer():
    if request.method=="POST":
        temp=[]

        test_wickets=int(request.form.get("app_wickets"))
        test_wickets_last=int(request.form.get("app_wicketslast"))

        if test_wickets < test_wickets_last:
            return render_template("index.html",content="Total Wickets are less than wickets fell in last 5 overs")

        test_batting=request.form.get("app_batting")
        test_bowling=request.form.get("app_bowling")

        
        if test_batting==test_bowling:
            return render_template("index.html",content="Batting and Bowling Teams Cannot be Same")
            
        

        
        test_ground=request.form.get("app_ground")
        temp=temp+which_ground(test_ground)
        
        temp=temp+which_battingbowling(test_batting)

        temp=temp+which_battingbowling(test_bowling)

        test_runs=int(request.form.get("app_runs"))
        test_overs=float(request.form.get("app_overs"))
        test_runs_last=int(request.form.get("app_runslast"))

        temp=temp+[test_runs,test_wickets,test_overs,test_runs_last,test_wickets_last]

        # test_data=[temp]
        test_data=np.array([temp])
        # model=model_predict.score_predictor()
        prediction_forest=int(model_predict.model1.predict(test_data))
        prediction_linear=int(model_predict.model2.predict(test_data))

        lower_forest=prediction_forest-5
        upper_forest=prediction_forest+5

        # prediction_linear=0
    

        lower_linear=prediction_linear-5
        upper_linear=prediction_linear+5

        return render_template(
            "index.html",content="Score will be between "+str(lower_forest)+" to "+str(upper_forest)+" Runs using Random Forest Regression"+"<br>"
            "Score will be between "+str(lower_linear)+" to "+str(upper_linear)+" Runs using Linear Regression"+"<br><br>"+
            "R^2 Score:<br>"+"Random Forest Regressor: "+str(model_predict.m1s)+"<br>"+
            "Linear model: "+str(model_predict.m2s))
    
if __name__ == '__main__':
    app.run(debug=True)
