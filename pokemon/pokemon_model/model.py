import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
import random
import math
import pickle

#function for creating fake data...
def temp_func(x):
    opt = random.choice([0,1,2,3])
    if opt == 0:
        #floor operation
        x = math.floor(x)
    elif opt == 1:
        #ceil operation
        x = math.ceil(x)
    elif opt == 2:
        #add some value
        x = x + random.choice([1,2,3,4,5,6,7])
    else:
        #subtract some value
        x = x - random.choice([1,2,3,4,5,6,7])
    return x


#importing dataset
pokemon_data = pd.read_csv("pokemon.csv")

df = pd.DataFrame()
df[["Type 1", "Type 2", "Attack", "Defense", "Speed", "Name"]] = \
    pokemon_data.loc[:, ["Type 1", "Type 2", "Attack", "Defense", "Speed", "Name"]]

#replacing np.nan with 'No Secondary Type'
df["Type 2"] = df["Type 2"].replace(np.nan, "No Secondary Type")

#Scaling Attack, Defense, Speed
min_max_scaler = MinMaxScaler()
df.iloc[:, 2:-1] = min_max_scaler.fit_transform(df.iloc[:, 2:-1])
df.iloc[:,2:-1] = df.iloc[:,2:-1].applymap(lambda x:x*100)

#creating fake data using temp_func...
temp_df = df.copy()
temp_df.iloc[:,2:-1] = temp_df.iloc[:,2:-1].applymap(temp_func)

temp_df2 = df.copy()
temp_df2.iloc[:,2:-1] = temp_df2.iloc[:,2:-1].applymap(temp_func)

temp_df3 = df.copy()
temp_df3.iloc[:,2:-1] = temp_df3.iloc[:,2:-1].applymap(temp_func)

#concatenating the dataframes...
df = pd.concat([df, temp_df, temp_df2, temp_df3])



#X -> Independent variables
#y -> Dependent variable
X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values


#Encoding Categorical data: Type 1, Type 2
ct = ColumnTransformer(transformers = [('encoder1', OneHotEncoder(sparse = False ), [0,1])], remainder = "passthrough" )
X = np.array(ct.fit_transform(X))

#Encoding Categorical data: Name
le = LabelEncoder()
le.fit(y)
y = le.transform(y)

classifier = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
classifier.fit(X, y)

#creating pickles
classifier_pkl = open("classifier.pkl","wb") 
minmax_pkl = open("min_max.pkl","wb") 
onehot_pkl = open("onehot.pkl","wb") 
labelEnc_pkl = open("labelEnc.pkl","wb") 

pickle.dump(classifier, classifier_pkl)
pickle.dump(min_max_scaler, minmax_pkl)
pickle.dump(ct, onehot_pkl)
pickle.dump(le, labelEnc_pkl)

classifier_pkl.close() 
minmax_pkl.close() 
onehot_pkl.close() 
labelEnc_pkl.close() 

