# this run main model 

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
import pickle
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix , ConfusionMatrixDisplay

os.makedirs('model' , exist_ok=True)
os.makedirs('result' , exist_ok=True)

# read file
 
df = pd.read_csv('data/drug200.csv')
# df.head(5)

# split features and labels

X = df.drop('Drug' , axis = 1).values
Y = df['Drug'].values


# split train and test 
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.3, random_state=125 )

# data processing and training pipeline 


cat_col = [1,2,3]
num_col = [0,4]

transform = ColumnTransformer(
    [
        ("encoder", OrdinalEncoder(), cat_col),
        ("num_imputer", SimpleImputer(strategy="median"), num_col),
        ("num_scaler", StandardScaler(), num_col),
    ]
)
pipe = Pipeline(
    steps=[
        ("preprocessing", transform),
        ("model", RandomForestClassifier(n_estimators=100, random_state=125)),
    ]
)
pipe.fit(X_train, y_train)


# save model
with open ('model/drug_classification.pkl' , mode ='wb') as file : 
    pickle.dump(pipe , file)


# evaluate metrics and save to result

# f1 score
y_predict = pipe.predict(X_test)
f1 = f1_score(y_test, y_predict , average='macro')
# print(round(f1 , 2))

with open('result/metrics.txt' , mode = 'w') as file:
    file.write(f'f1_score is {round(f1 , 2)}')

# confusion matrix
cm = confusion_matrix(y_test , y_predict , labels=pipe.classes_)
display = ConfusionMatrixDisplay(cm , display_labels = pipe.classes_)
# display.plot()
plt.savefig('result/cm.png' , dpi = 120)