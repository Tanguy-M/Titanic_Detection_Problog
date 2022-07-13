import string
import numpy as np
import pandas as pd
from problog.logic import Var, Term

#================================================================================================================================
#PRE-PROCESSING
train_data = pd.read_csv("Titanic_Dataset/train.csv")
train_data['Age'].replace('', np.nan, inplace=True) 
train_data = train_data.drop(['PassengerId','Name','Ticket','Cabin','Embarked'], axis=1)#delete useless column
train_data.dropna(subset=['Age'], inplace=True) #remove noise from empty Age
train_data.replace(to_replace =["male", "female"], value =[1,0],inplace=True)#give simplest value
train_data['Fare_norm'] = np.log(train_data.Fare+1)#normalize Fare
train_data.reset_index(inplace=True, drop=True)#replace index

#================================================================================================================================
#define constants
ROWS = len(train_data)
TRAIN = round(ROWS*0.9)
TRESH_ADULT = 20
TRESH_OLD = 40
TRESH_AVERAGE = 2
TRESH_HIGH = 4
TRESH_PARCH = 1
TRESH_CLASS = 1
TRESH_MAN = 1

#================================================================================================================================
#define Vars in Prolog
X = Var('X')
Y = Var('Y')

#================================================================================================================================
#define Terms in Prolog
survived = Term('survived')

sex = Term('sex')

classs = Term('classs')

#Parents/childrens
parch = Term('parch')

#Age
young = Term('young')
adult = Term('adult')
old = Term('old')

#Fare
low = Term('low')
average = Term('average')
high = Term('high')

#================================================================================================================================
def getExample(): #process the evidences for the LFI
    example = []
    for elm in range(0,TRAIN):
        results = []

        #add Survived
        if (train_data.loc[elm, 'Survived'] == 1):
            results.append((survived, True))
        else:
            results.append((survived, False))
        
        #add Sex
        if (train_data.loc[elm, 'Sex'] == 1):
            results.append((sex, True))#male
        else:
            results.append((sex, False))#female
        
        #add Class
        if (train_data.loc[elm, 'Pclass'] == 1):
            results.append((classs, True))#1 class
        else:
            results.append((classs, False))#2 or 3 class

        #add Parch
        if (train_data.loc[elm, 'Parch'] <= TRESH_PARCH):
            results.append((parch, True))# 0-1 Parent / Children
        else:
            results.append((parch, False))# >1 Parent / Children
        
        #add Age
        if (train_data.loc[elm, 'Age'] <= TRESH_ADULT):
            results.append((young, True))
        elif(train_data.loc[elm, 'Age'] <= TRESH_OLD and TRESH_ADULT < train_data.loc[elm, 'Age']):
            results.append((adult, True))
        else:
            results.append((old, True))

        #add Fare
        if (train_data.loc[elm, 'Fare_norm'] <= TRESH_AVERAGE):
            results.append((low, True))
        elif(train_data.loc[elm, 'Fare_norm'] > TRESH_AVERAGE and train_data.loc[elm, 'Fare_norm'] <= TRESH_HIGH):
            results.append((average, True))
        else:
            results.append((high, True))

        example.append(results)
        
    return example

#================================================================================================================================
def getEvidencesTest(elm): #return the evidences from 1 row for the evaluation

    person_info = ""

    #add Sex
    if (train_data.loc[elm, 'Sex'] == 1):
        person_info += "evidence(sex,true)."#male
    else:
        person_info += "evidence(sex,false)."#female

    #add Class
    if (train_data.loc[elm, 'Pclass'] == 1):
        person_info += "\nevidence(classs,true)."#1 class
    else:
        person_info += "\nevidence(classs,false)."#2 or 3 class

    #add Parch
    if (train_data.loc[elm, 'Parch'] <= TRESH_PARCH):
        person_info += "\nevidence(parch,true)."
    else:
        person_info += "\nevidence(parch,false)."
        
    #add Age
    if (train_data.loc[elm, 'Age'] <= TRESH_ADULT):
        person_info += "\nevidence(young,true)."
    elif(train_data.loc[elm, 'Age'] <= TRESH_OLD and TRESH_ADULT < train_data.loc[elm, 'Age']):
        person_info += "\nevidence(adult,true)."
    else:
        person_info += "\nevidence(old,true)."

    #add Fare
    if (train_data.loc[elm, 'Fare_norm'] <= TRESH_AVERAGE):
        person_info += "\nevidence(low,true)."
    elif(train_data.loc[elm, 'Fare_norm'] > TRESH_AVERAGE and train_data.loc[elm, 'Fare_norm'] <= TRESH_HIGH):
        person_info += "\nevidence(average,true)."
    else:
        person_info += "\nevidence(high,true)."

    person_info += "\n\nquery(survived)."

    return person_info

#================================================================================================================================
def printRow(row): #print a specific row from the dataset
    print(train_data.iloc[[row]])