import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train_data = pd.read_csv("Titanic_Dataset/train.csv")
train_data['Age'].replace('', np.nan, inplace=True) 
train_data = train_data.drop(['PassengerId','Name','Ticket','Cabin','Embarked'], axis=1)#delete useless column
train_data.dropna(subset=['Age'], inplace=True) #remove noise from empty Age
train_data.replace(to_replace =["male", "female"], value =[1,0],inplace=True)#give simplest value
train_data.reset_index(inplace=True, drop=True)#replace index
ROWS = len(train_data)
df_num = train_data[['Age','SibSp','Parch','Fare']]
df_cat = train_data[['Survived','Pclass','Sex']]


def detailsSex():

    women = train_data.loc[train_data.Sex == 0]["Survived"]
    rate_women = sum(women)/len(women)*100
    men = train_data.loc[train_data.Sex == 1]["Survived"]
    rate_men = sum(men)/len(men)*100

    print("Sex info :")
    print("% of women who survived :", rate_women)
    print("% of men who survived :", rate_men)

#============================================================================================================================
def detailsPclass():
    class3 = train_data.loc[train_data.Pclass == 3]["Survived"]
    rate_c3 = sum(class3)/len(class3)*100
    class2 = train_data.loc[train_data.Pclass == 2]["Survived"]
    rate_c2 = sum(class2)/len(class2)*100
    class1 = train_data.loc[train_data.Pclass == 1]["Survived"]
    rate_c1 = sum(class1)/len(class1)*100
    
    print("\nClass info :")
    print("% of 3rd class who survived :", rate_c3)
    print("% of 2nd class who survived :", rate_c2)
    print("% of 1st class who survived :", rate_c1)

#============================================================================================================================
def detailsAge(): #3 group (young, adult, old)
    bins = [0,10,20,30,40,50,60,70,80]
    labels = ["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80"]
    ages = pd.cut(train_data.loc[train_data.Survived == 1]['Age'], bins = bins, labels = labels, include_lowest = True)
    ages = ages.value_counts(sort=False)
    
    #print(ages)

    rate_a00_20 = sum(ages[0:1])/ROWS*100
    rate_a20_40 = sum(ages[2:3])/ROWS*100
    rate_a50_80 = sum(ages[4:7])/ROWS*100

    print("\nAge info /TT passengers:")
    print("% of from 0-20 years who survived :", rate_a00_20)
    print("% of from 20-40 years who survived :", rate_a20_40)
    print("% of from 40-80 years who survived :", rate_a50_80)

    #----------------------------------------------------------------------------------------------------------------------------

    ages = pd.cut(train_data.loc[train_data.Survived == 1][train_data.Sex == 1]['Age'], bins = bins, labels = labels, include_lowest = True)
    rows = len(train_data.loc[train_data.Sex == 1]['Sex']) #male
    ages = ages.value_counts(sort=False)
    
    #print(ages)

    rate_a00_20 = sum(ages[0:1])/rows*100
    rate_a20_40 = sum(ages[2:3])/rows*100
    rate_a50_80 = sum(ages[4:7])/rows*100

    print("\nAge info / Men:")
    print("% of from 0-20 years who survived :", rate_a00_20)
    print("% of from 20-40 years who survived :", rate_a20_40)
    print("% of from 40-80 years who survived :", rate_a50_80)

    ages = pd.cut(train_data.loc[train_data.Survived == 1][train_data.Sex == 0]['Age'], bins = bins, labels = labels, include_lowest = True)
    rows = len(train_data.loc[train_data.Sex == 0]['Sex']) #Women
    ages = ages.value_counts(sort=False)
    
    #print(ages)

    rate_a00_20 = sum(ages[0:1])/rows*100
    rate_a20_40 = sum(ages[2:3])/rows*100
    rate_a50_80 = sum(ages[4:7])/rows*100

    print("\nAge info / Women:")
    print("% of from 0-20 years who survived :", rate_a00_20)
    print("% of from 20-40 years who survived :", rate_a20_40)
    print("% of from 40-80 years who survived :", rate_a50_80)


#============================================================================================================================
def detailsSibsp(): #not used
    sibsp = pd.cut(train_data.loc[train_data.Survived == 1]['SibSp'], bins = 5, labels = [0,1,2,3,4], include_lowest = True)
    sibsp = sibsp.value_counts(sort=False)

    #print(sibsp)

    rate_s0 = sibsp[0]/ROWS*100
    rate_s1 = sibsp[1]/ROWS*100
    rate_s2 = sibsp[2]/ROWS*100
    rate_s3 = sibsp[3]/ROWS*100
    rate_s4 = sibsp[4]/ROWS*100

    print("\nSiblings / Spouses info :")
    print("% of people with 0 sibsp :", rate_s0)
    print("% of people with 1 sibsp :", rate_s1)
    print("% of people with 2 sibsp :", rate_s2)
    print("% of people with 3 sibsp :", rate_s3)
    print("% of people with 4+ sibsp :", rate_s4)

#============================================================================================================================
def detailsParch():
    parch = pd.cut(train_data.loc[train_data.Survived == 1]['Parch'],bins=6, include_lowest = True)
    parch = parch.value_counts(sort=False)

    #print(parch)

    rate_p0 = parch[0]/ROWS*100
    rate_p1 = sum(parch[1:5])/ROWS*100

    print("\nParents / Childrens info :")
    print("% of people with 0 Parch :", rate_p0)
    print("% of people with 1+ Parch :", rate_p1)

 #-------------------------------------------------------------------------------------------------------------------------------

    parch = pd.cut(train_data.loc[train_data.Survived == 1][train_data.Sex == 1]['Parch'],bins=6, include_lowest = True)
    rows = len(train_data.loc[train_data.Sex == 1]['Sex'])#Men
    parch = parch.value_counts(sort=False)

    #print(parch)

    rate_p0 = parch[0]/rows*100
    rate_p1 = sum(parch[1:5])/rows*100

    print("\nParents / Childrens Men info :")
    print("% of people with 0 Parch :", rate_p0)
    print("% of people with 1+ Parch :", rate_p1)

    #-------------------------------------------------------------------------------------------------------------------------------

    parch = pd.cut(train_data.loc[train_data.Survived == 1][train_data.Sex == 0]['Parch'],bins=6, include_lowest = True)
    rows = len(train_data.loc[train_data.Sex == 0]['Sex'])#Women
    parch = parch.value_counts(sort=False)

    #print(parch)

    rate_p0 = parch[0]/rows*100
    rate_p1 = sum(parch[1:5])/rows*100

    print("\nParents / Childrens Women info :")
    print("% of people with 0 Parch :", rate_p0)
    print("% of people with 1+ Parch :", rate_p1)

#============================================================================================================================
def detailsFare():

    normalizingFare() #values are too close without 

    fare = pd.cut(train_data.loc[train_data.Survived == 1]['Fare_norm'],bins=30, include_lowest = True)
    fare = fare.value_counts(sort=False)
    #print(fare)

    rate_f0 = sum(fare[0:9])/ROWS*100
    rate_f1 = sum(fare[10:19])/ROWS*100
    rate_f2 = sum(fare[20:29])/ROWS*100

    print("\nFare info :")
    print("% of Low Fare :", rate_f0)
    print("% of Average Fare :", rate_f1)
    print("% of High Fare :", rate_f2)

 #-------------------------------------------------------------------------------------------------------------------------------

    fare = pd.cut(train_data.loc[train_data.Survived == 1][train_data.Pclass == 1]['Fare_norm'],bins=30, include_lowest = True)
    rows = len(train_data.loc[train_data.Pclass == 1]['Fare_norm'])
    fare = fare.value_counts(sort=False)

    # print(fare)

    rate_f0 = sum(fare[0:7])/rows*100
    rate_f1 = sum(fare[8:29])/rows*100

    print("\nFare info Class1:")
    print("% of Average Fare :", rate_f0)
    print("% of High Fare :", rate_f1)

 #-------------------------------------------------------------------------------------------------------------------------------

    fare = pd.cut(train_data.loc[train_data.Survived == 1][train_data.Pclass > 1]['Fare_norm'],bins=30, include_lowest = True)
    rows = len(train_data.loc[train_data.Pclass > 1]['Fare_norm'])
    fare = fare.value_counts(sort=False)

    #print(fare)

    rate_f0 = sum(fare[0:14])/rows*100
    rate_f1 = sum(fare[15:29])/rows*100

    print("\nFare info Class 2 & 3:")
    print("% of Low Fare :", rate_f0)
    print("% of Average Fare :", rate_f1)

#================================================================================================================================
#plot all the data to have a better visualisation
def overallCharts():
    for i in df_num.columns:
        plt.hist(df_num[i])
        plt.title(i)
        plt.show()

    for i in df_cat.columns:
        sns.barplot(df_cat[i].value_counts().index,df_cat[i].value_counts()).set_title(i)
        plt.show()

    # sns.heatmap(df_num.corr())
    # plt.show()

    # sns.heatmap(df_cat.corr())
    # plt.show()

#================================================================================================================================
def statData3():
    #compare the survival rate
    print(pd.pivot_table(train_data, index= 'Survived', values=df_num))

    #get a surviving ratio Pclass
    print('\n')
    print(pd.pivot_table(train_data, index='Survived', columns='Pclass',values='Age' ,aggfunc='count'))
    detailsPclass()

    #get a surviving ratio Sex
    print('\n')
    print(pd.pivot_table(train_data, index='Survived', columns='Sex',values='Age' ,aggfunc='count'))
    detailsSex()

#================================================================================================================================
def normalizingSibSp():
    train_data['SibSp_norm'] = np.log(train_data.SibSp+1)
    train_data['SibSp_norm'].hist()
    plt.title('SibSp_normalized')
    plt.show()

    train_data[train_data.Survived == 1]['SibSp_norm'].hist()
    plt.title('Survived_SibSp_normalized')
    plt.show()

#================================================================================================================================
def normalizingParch():
    train_data['Parch_norm'] = np.log(train_data.Parch+1)
    train_data['Parch_norm'].hist()
    plt.title('Parch_normalized')
    plt.show()

    train_data[train_data.Survived == 1]['Parch_norm'].hist()
    plt.title('Survived_Parch_normalized')
    plt.show()

#================================================================================================================================
def normalizingFare():
    train_data['Fare_norm'] = np.log(train_data.Fare+1)
    # train_data['Fare_norm'].hist()
    # plt.title('Fare_normalized')
    # plt.show()

    # train_data[train_data.Survived == 1]['Fare_norm'].hist()
    # plt.title('Survived_Fare_normalized')
    # plt.show()

overallCharts()