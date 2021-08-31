# Pokemon-Predictor-Using-Random-Forrest-Classifier
## Based on the input given by the user this web=application predicts the pokemon.

## Intructions to run the web-application

1) Install python 3.6 or above on your device
2) Setup a python virtual environment and activate it.(optional)
3) Install Flask, Flask-WTF, scikit-learn, pandas, numpy.
4) Download the Zip file of the repository and unzip it.
5) Open the project directory and navigate to ./pokemon/pokemon_model/ directory on command line.
6) Run model.py with python.
7) This will create four .pkl files(classifier.pkl, onehot.pkl, min_max.pkl, labelEnc.pkl) in the 'pokemon_model' directory. 
8) Note: If you don't run model.py with 'pokemon_model' as you working directory, the .pkl files will be saved in some other directory. Please run the model.py script with 'pokemon_model' as your working directory.
9) Now run main.py in the project directory which will start the server.
10) Open http://localhost:5000 on your browser with the server running.

## Datasets used
1) For data: https://www.kaggle.com/abcsds/pokemon?select=Pokemon.csv
2) For Images: https://www.kaggle.com/arenagrenade/the-complete-pokemon-images-data-set
Note: some changes were made to the csv files and also to the filenames and quality of the images to fit the needs of the application. 