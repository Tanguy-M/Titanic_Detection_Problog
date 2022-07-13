from Pre_processing import *
from problog.program import PrologString
from problog import get_evaluatable
import seaborn as sns
import matplotlib.pyplot as plt

TRESH_EVALUATION = 0.5

trained_model = """
1/2::sex.
1/2::classs.
1/2::parch.
1/3::young; 1/3::adult; 1/3::old.
1/3::low; 1/3::average; 1/3::high.

0.453819322323842::status(boy) :- sex, young.
0.999999999999999::status(girl) :- \+sex, young.
0.283622156921437::status(man) :- sex, adult.
1.0::status(woman) :- \+sex, adult.
0.22033653760489::status(old_man) :- sex, old.
0.945529524423287::status(old_woman) :- \+sex, old.

1.0::wealth(very_rich) :- classs, high.
0.999999578182651::wealth(rich) :- classs, average.
0.636420427294039::wealth(middle) :- \+classs, average.
0.500048632630683::wealth(poor) :- \+classs, low.

1.0::survived :- status(X), wealth(Y), parch.
0.877753177252582::survived :- status(X), wealth(Y), \+parch.

"""

def get_evaluation1(num_passenger): #evaluate with row number
    person_info = getEvidencesTest(num_passenger)
    evaluation_model = trained_model + person_info
    result = get_evaluatable().create_from(PrologString(evaluation_model),propagate_evidence=True).evaluate()
    result = list(result.values())[0]

    if result > TRESH_EVALUATION:
        guess = 1
    else:
        guess = 0

    evaluation_model = ""
    return result, guess

def get_evaluation(person_info): #evaluate with evidences from main.py
    evaluation_model = trained_model + person_info
    result = get_evaluatable().create_from(PrologString(evaluation_model),propagate_evidence=True).evaluate()
    result = list(result.values())[0]

    if result > TRESH_EVALUATION:
        guess = 1
    else:
        guess = 0

    evaluation_model = ""
    return result, guess

def test_evaluation():

    my_file = open("Results_evalutation.csv","w+")
    txt = "Index,Survived,Prediction,Result"
    for elm in range(TRAIN,ROWS):
        [result, guess] = get_evaluation1(elm)
        txt += "\n" + str(train_data.index[elm]) + "," +str(train_data['Survived'].loc[train_data.index[elm]]) + "," + str(result) + "," + str(guess)

    my_file.write(txt)
    my_file.close()

    df = pd.read_csv("Results_evalutation.csv")
    confusion_matrix = pd.crosstab(df['Survived'], df['Result'], rownames=['Actual'], colnames=['Predicted'])
    sns.heatmap(confusion_matrix,annot=True).set_title('Confusion Matrix')

    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for i in range(0,len(df)):
        if df.loc[i,"Survived"] == df.loc[i,"Result"] and df.loc[i,"Survived"] == 1:
            TP+=1
        if df.loc[i,"Survived"] == df.loc[i,"Result"] and df.loc[i,"Survived"] == 0:
            TN+=1
        if df.loc[i,"Survived"] != df.loc[i,"Result"] and df.loc[i,"Survived"] == 1:
            FN+=1
        if df.loc[i,"Survived"] != df.loc[i,"Result"] and df.loc[i,"Survived"] == 0:
            FP+=1
    
    accuracy = (TP+TN)/(TP+TN+FN+FP)
    recall_t = TP/(TP+FP)
    precision_t = TP/(TP+FN)
    recall_f = TN/(TN+FN)
    precision_f = TN/(TN+FP)

    # print("TP : ",TP)
    # print("\nTN : ",TN)
    # print("\nFN : ",FN)
    # print("FP : ",FP)

    print("\nAccuracy : ",accuracy)
    print("Precision Survive : ",precision_t)
    print("Recall Survive: ",recall_t)
    print("Precision Dead : ",precision_f)
    print("Recall Dead: ",recall_f)
    
    plt.show()