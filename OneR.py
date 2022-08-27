#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Import pandas and numpy packages
import pandas as pd
import numpy as np


# Load test set, training set
# python script and csv files must be in the same folder (directory)
train = pd.read_csv('C:/Users/augus/Documents/MATH 6380/Homeworks/HW-6_Team16/titanic_traning.csv', decimal =',') 
test = pd.read_csv('C:/Users/augus/Documents/MATH 6380/Homeworks/HW-6_Team16/titanic_test.csv', decimal = ',')

# Extract features from training set
ids = train.ID
pclass = train.pclass
gender = train.gender
age = train.age
sibsp = train.sibsp
parch = train.parch
fare = train.fare
embarked = train.embarked
survived = train.survived

# Extract features from test set
ids_t = test.ID
pclass_t = test.pclass
gender_t = test.gender
sibsp_t = test.sibsp
parch_t = test.parch
embarked_t = test.embarked

# Define decision rule for each categorical feature
pclass_d = pd.crosstab(pclass, survived) # class 1
gender_d = pd.crosstab(gender, survived) # female
sibsp_d = pd.crosstab(sibsp, survived) # 1
parch_d = pd.crosstab(parch, survived) #1,2,3
embarked_d = pd.crosstab(embarked, survived) #C
# The decisions rules are as follows: 
# For pclass = class 1
# For gender = Female
# For sibsp = 1
# For parch = 1,2, and 3
# For embarked = C (Cherbourg)

# Create parch_t categories because decision rule applies to three different subcategories
# where the survival rate is highest, the subcategories are chosen as follows:
# 0 = no, 1 = yes, 2 = yes, 3 = yes, 4 = no, 5 = no, 6 = no, 9 = no 
def process_parch(df,cut_points,label_names):
    df['parch_cat'] = pd.cut(df['parch'],cut_points,labels=label_names)
    return df

cut_points = [-1,0.99,3.1,9]
label_names = ['no0','yes','no']
test = process_parch(test,cut_points,label_names)
parch_t = test.parch_cat

pclass_r = pclass_d[0]<pclass_d[1] #
plc_r2 = pclass_d[1]/pclass_d[0] #rate

## ML general model based on OneR Classifier
def oneR(feature,rule):  #rule is determined on by categories of the features
    for i in feature:
        if i == rule: 
            pred1 = 1
            pred.append(pred1)
            continue
        else:
            pred0 = 0
            pred.append(pred0)
            
# Run ML for each feature and obtain the predicted class (survived = 1 and notsurvived = 0)
# For pclass 
pred = []               
oneR(pclass_t,1)  #more survived in first class than other classes
pred_pclass = pred

# For gender
pred = []               
oneR(gender_t,'female') #female is the condition since more women survived
pred_gender = pred

# For sibsp
pred = []               
oneR(sibsp_t,1)     # passengers with one sibling or their spouse survived 
pred_sibsp = pred   # than those with more than one or non accompanyng them

# For parch
pred = []               
oneR(parch_t,'yes') # those with mother, father, child, or some other children 
pred_parch = pred   # were more likely to survive on that disaster 

# For embarked 
pred = []               
oneR(embarked_t,'C') # Those who embarked at Cherbourg were more likely
pred_embarked = pred # to survive as well

# Store pssanger ID's and Predicted class labels based in each feature into the 
# 'titanic_test_prediction.csv' file.

# Load the 'titanic_test_prediction.csv' file as 'test_pred'
header_names = ['ID','truth','prediction']
test_pred = pd.read_csv('C:/Users/augus/Documents/MATH 6380/Homeworks/HW-6_Team16/titanic_test_prediction.csv',
                        header = 0, names = header_names, decimal = ',')

# Extract passanger 'ID' and 'truth' from the test_pred dataset 
ids_pred = test_pred.ID
truth_pred = test_pred.truth

# Create a dataframe including: ids_pred, truth_pred, pred_pclass, pred_gender,
# pred_sibsp, pred_parch, and pred_embarked
df = pd.DataFrame({'ID': ids_pred,                          ##################
                   'Ground truth': truth_pred,              #                #
                   'Gender_Based_Prediction': pred_gender,  #                #
                   'Class_Based_Prediction': pred_pclass,   # Names assigned #
                   'SibSp_Based_Prediction': pred_sibsp,    # to predictors  #
                   'ParCh_Based_Prediction': pred_parch,    # to be saved    #
                   'Port_Based_Prediction': pred_embarked}) ##################

# Save as a .xlsx file named 'titanic_test_prediction.xlsx'
df.to_excel('titanic_test_prediction.xlsx', index = False,
            sheet_name = 'Predictions') 

# Compute success rates for each feature in test set
# For pclass
pclass_pred = pd.Series(pred_pclass, dtype = int) 
pclass_table = pd.crosstab(truth_pred, pclass_pred, margins = True)
pclass_rate = (pclass_table.loc[0,0]+pclass_table.loc[1,1])/len(truth_pred)

# For gender
gender_pred = pd.Series(pred_gender, dtype = int) 
gender_table = pd.crosstab(truth_pred, gender_pred, margins = True)
gender_rate = (gender_table.loc[0,0]+gender_table.loc[1,1])/len(truth_pred)

# For sibsp
sibsp_pred = pd.Series(pred_sibsp, dtype = int) 
sibsp_table = pd.crosstab(truth_pred, sibsp_pred, margins = True)
sibsp_rate = (sibsp_table.loc[0,0]+sibsp_table.loc[1,1])/len(truth_pred)

# For parch
parch_pred = pd.Series(pred_parch, dtype = int) 
parch_table = pd.crosstab(truth_pred, parch_pred, margins = True)
parch_rate = (parch_table.loc[0,0]+parch_table.loc[1,1])/len(truth_pred)

# For embarked
embarked_pred = pd.Series(pred_embarked, dtype = int) 
embarked_table = pd.crosstab(truth_pred, embarked_pred, margins = True)
embarked_rate = (embarked_table.loc[0,0]+embarked_table.loc[1,1])/len(truth_pred)

# Save success rates on a different .xlsx file 'titanic_test_prediction_success_rate.xlsx'
# Create dataframe for success rate 
features_pred = ['Gender','Class','SibSp','ParCh','Port']
S_rate = [gender_rate, pclass_rate, sibsp_rate, parch_rate, embarked_rate]
df2 = pd.DataFrame({'Feature_Based_Prediction': features_pred,
                   'Success_Rate': S_rate})
# Save success rates on .xlsx file
df2.to_excel('titanic_test_prediction_success_rate.xlsx', index = False,
             sheet_name='Success_Rate')





