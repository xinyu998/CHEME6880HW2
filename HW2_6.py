import pandas as pd
import numpy as np 
import warnings
warnings.filterwarnings("ignore")
#import data
data=pd.read_excel(r'DATA2.xlsx')
data.head()
data=pd.DataFrame(data)
cols=['X1','X2','X3']
X=data[cols]
X=pd.DataFrame(X)
y=data['Y']
Xtest=[[1.5,1.5,1.5]]
#polynomial SVM using sklearn
from sklearn.svm import SVC
svcpoly=SVC(kernel='poly',degree=2)
svcpoly.fit(X,y)
yprepoly=svcpoly.predict(Xtest)
print(yprepoly)
#Gaussian SVM using sklearn
svcgau=SVC(kernel='rbf')
svcgau.fit(X,y)
ypregau=svcgau.predict(Xtest)
print(ypregau)
