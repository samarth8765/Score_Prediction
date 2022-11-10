import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression


def score_predictor():
    df_encode = pickle.load(open('data.pickle','rb'))
    
    y = df_encode.total
    X = df_encode.drop('total',axis=1)
    
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25)
    
    model1 = RandomForestRegressor(n_estimators=50)
    model1.fit(X_train,y_train)
    m1s=model1.score(X_test,y_test)

    model2=LinearRegression()
    model2.fit(X_train,y_train)
    m2s=model2.score(X_test,y_test)
    
    return (model1,m1s,model2,m2s)

model1,m1s,model2,m2s = score_predictor()