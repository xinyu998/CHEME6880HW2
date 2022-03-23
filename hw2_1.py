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
x1=data[['Employment Status','Approve Application ?']]
x2=data[['Credit Rating','Approve Application ?']]
x3=data[['Available Credit','Approve Application ?']]
x4=data[['Age','Approve Application ?']]
approve=data['Approve Application ?']
cols=['Employment Status','Credit Rating','Available Credit','Age']
x=data[cols]
x=pd.DataFrame(x)
y=data['Approve Application ?']
#Decision tree without software package
print(y.value_counts())
#total outcomes
p=11
n=8
H=(-p/(p+n))*math.log2(p/(p+n))-(n/(p+n))*math.log2(n/(p+n))
print(H)
#define Information gain function
def infogain(p0,n0,p1,n1,p2,n2):
	H0=(-p0/(p0+n0))*math.log2(p0/(p0+n0))-(n0/(p0+n0))*math.log2(n0/(p0+n0))
	if n1!=0:
		H1=(-p1/(p1+n1))*math.log2(p1/(p1+n1))-(n1/(p1+n1))*math.log2(n1/(p1+n1))
	else:
		H1=0
	H2=(-p2/(p2+n2))*math.log2(p2/(p2+n2))-(n2/(p2+n2))*math.log2(n2/(p2+n2))
	if p2==100:
		EH=((p0+n0)/(p+n))*H0+((p1+n1)/(p+n))*H1
	else:
		EH=((p0+n0)/(p+n))*H0+((p1+n1)/(p+n))*H1+((p2+n2)/(p+n))*H2
	IG=H-EH
	print(f'Information gain is {IG}')

#print(x1.value_counts())
infogain(4,5,7,3,100,10)
#print(x2.value_counts())
infogain(4,6,7,2,100,10)
#print(x3.value_counts())
infogain(3,2,5,4,3,2)
#print(x4.value_counts())
infogain(2,4,6,0,3,4)

#Focus on age, test diff values to find the root
senior_data=data.loc[data['Age']==2]
x1=senior_data[['Employment Status','Approve Application ?']]
x2=senior_data[['Credit Rating','Approve Application ?']]
x3=senior_data[['Available Credit','Approve Application ?']]
approve=data['Approve Application ?']
print(x1.value_counts())
infogain(1,1,2,3,100,10)
print(x2.value_counts())
infogain(1,2,1,2,100,10)
print(x3.value_counts())
infogain(1,1,1,1,100,2)
#Focus on avabile credit
credit_data=senior_data.loc[senior_data['Available Credit']==0]
print(credit_data)
x1=credit_data[['Employment Status','Approve Application ?']]
x2=credit_data[['Credit Rating','Approve Application ?']]
print(x1.value_counts())
#infogain(0,1,1,2,100,10)
print(x2.value_counts()) #zero

# focus on employment
em_data=credit_data.loc[credit_data['Employment Status']==0]
x1=credit_data[['Credit Rating','Approve Application ?']]
print(x1.value_counts())







