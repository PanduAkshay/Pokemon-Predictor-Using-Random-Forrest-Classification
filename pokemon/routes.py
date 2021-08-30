from pokemon import app
from pokemon.forms import PokeForm
from flask import render_template, request, redirect, url_for, session
import numpy as np
import pandas as pd
import json
import pickle
import os

#function to get the name of the image to fetch...
def change_names(name):
    name = name.replace('.png',"")
    name = name.lower()
    name = name.replace('mega ','')
    temp = ''
    for i in range(len(name)):
        if (name[i].isalnum()):
            temp += name[i]
    
    return temp + '.png'


#Random Forest Classifier...
def run_rf(features):
    features = [features]
    location = os.path.join('pokemon', 'pokemon_model')
    fp_classifier = open(os.path.join(location,'classifier.pkl'),'rb')
    fp_label = open(os.path.join(location,'labelEnc.pkl'),'rb')
    fp_onehot = open(os.path.join(location,'onehot.pkl'),'rb')

    classifier = pickle.load(fp_classifier)
    labelE = pickle.load(fp_label)
    onehot = pickle.load(fp_onehot)

    fp_classifier.close()
    fp_label.close()
    fp_onehot.close()

    features = np.array(onehot.transform(features))
    y_pred = classifier.predict(features)
    y_pred = labelE.inverse_transform(y_pred)

    return y_pred[0]

#To fetch the actual details of a pokemon from the csv file...
def get_actual_details(name):
    location = os.path.join('pokemon', 'pokemon_model')
    df = pd.read_csv(os.path.join(location, 'pokemon.csv'))
    pokemon_row = df.loc[ df['Name']==name, ["Type 1", "Type 2", "Attack", "Defense", "Speed"]]
    fp_minmax = open(os.path.join(location,'min_max.pkl'),'rb')
    minmax = pickle.load(fp_minmax)
    pokemon_row.iloc[:,2:] = minmax.transform(pokemon_row.iloc[:,2:])
    pokemon_row.iloc[:,2:] = pokemon_row.iloc[:,2:].applymap(lambda x:x*100)
    fp_minmax.close()
    pokemon_row = pokemon_row.values
    data = dict()
    data['ptype'] = pokemon_row[0][0]
    data['stype'] = 'No Secondary Type' if pd.isnull(pokemon_row[0][1]) else pokemon_row[0][1]
    data['attack'] = round(pokemon_row[0][2],2)
    data['defense'] = round(pokemon_row[0][3],2)
    data['speed'] = round(pokemon_row[0][4],2)
    return data

#The page containing the form...
@app.route("/", methods = ['GET','POST'])
def mainpage():
    form = PokeForm(stype = "No Secondary Type" )
    if request.method == 'POST':
        data = dict()
        data['attack'] = str(form.attack.data)
        data['defense'] = str(form.defense.data)
        data['speed'] = str(form.speed.data)
        data['ptype'] = form.ptype.data
        data['stype'] = form.stype.data
        session['data'] = json.dumps(data)
        return redirect(url_for('result')) 
    return render_template('mainpage.html', form = form)

#The results are displayed in this page...
@app.route('/Results')
def result():
    if 'data' in session:     
        pData = json.loads(session['data'])
        session.pop('data')
        features = [pData['ptype'], pData['stype'], pData['attack'],
        pData['defense'], pData['speed']]
        name = run_rf(features)
        pic = url_for('static', filename = f"Poke_Images/{change_names(name)}")
        if not os.path.isfile(os.path.join('pokemon', 'static','Poke_Images',change_names(name))):
            pic = url_for('static', filename = f"Poke_Images/default.png")
        actual_data = get_actual_details(name)
        return render_template('results.html', pData=pData, name=name, pic = pic , actual_data= actual_data)
    else:
        return redirect(url_for('mainpage'))

