# Naive Bayes
import numpy as np 
import pandas as pd
import math
import matplotlib.pyplot as plt
#6880 HW2 XINYU LIU
#import data
import warnings
warnings.filterwarnings("ignore")
data=pd.read_excel(r'DATA1.xlsx')
data.head()
data=pd.DataFrame(data)
cols=['Employment Status','Credit Rating','Available Credit','Age']
x=data[cols]
x=pd.DataFrame(x)
y=data['Approve Application ?']
x1=data[['Employment Status','Approve Application ?']]
x2=data[['Credit Rating','Approve Application ?']]
x3=data[['Available Credit','Approve Application ?']]
x4=data[['Age','Approve Application ?']]
#Naive Bayes without sklearn
p_yes=11/19 
p_no=8/19 
#Calculate employment status
#print(x1.value_counts())
p_unemyes=4/9
#Credit rating
#print(x2.value_counts())
p_exyes=7/9
#avaiable credit
p_hiyes=3/5
#print(x3.value_counts())
#Age
#print(x4.value_counts())
p_senyes=3/7
#Calculate predict case
p_preyes=p_unemyes*p_exyes*p_hiyes*p_senyes*p_yes
print(p_preyes)
p_preno=(1-p_unemyes)*(1-p_exyes)*(1-p_hiyes)*(1-p_senyes)*p_no
print(p_preno)










