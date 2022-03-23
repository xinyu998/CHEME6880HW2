# use sklearn
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
#import data
data=pd.read_excel(r'DATA1.xlsx')
data.head()
data=pd.DataFrame(data)
cols=['Employment Status','Credit Rating','Available Credit','Age']
x=data[cols]
x=pd.DataFrame(x)
y=data['Approve Application ?']
Xtest=[[0,1,2,2]]
# Predict test function
# define a function to run the test data, Xtest, and print out the results
def predict_test(Xtest, classifier, model_name):

    # make predictionson the test data
    predictions = classifier.predict(Xtest)

    # check if the probability estimates are available
    if hasattr(classifier, "predict_proba"):
        predictions_proba = classifier.predict_proba(Xtest)
        prob_estimate = True 
    else:
        prob_estimate = False    

    # print out the results  
    for i in range(len(Xtest)):       
        print("\nThe test data point {} is classified to Category {} by {}.".format(Xtest[i], predictions[i], model_name))      
        if prob_estimate == True:
            print("Below is the probability estimates for each category:")    
            for j in range(len(predictions_proba[i])):       
                print("Category {}: {:5.4f}".format(j, predictions_proba[i,j]))
    
    return

#Decision tree
# from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
# dt_model = DecisionTreeClassifier(max_depth = 5).fit(x, y)
# plt.figure(figsize=(9,9))  # set plot size (denoted in inches)
# tree.plot_tree(dt_model)
# plt.show()
# Xtest = [[0,1,2,2]]
# model_name = "decision tree"
# predict_test(Xtest, dt_model, model_name)
# print(predict_test)

#Naive bayes
from sklearn.naive_bayes import GaussianNB
nb_model = GaussianNB().fit(x, y)

predictions = nb_model.predict(Xtest)
predictions_proba = nb_model.predict_proba(Xtest)
for i in range(len(Xtest)):       
    print("\nThe test data point {} is classified to Category {} by Naive Bayes.".format(Xtest[i], predictions[i]))      
    print("Below is the probability estimates for each category:")    
    for j in range(len(predictions_proba[i])):       
        print("Category {}: {:5.4f}".format(j, predictions_proba[i,j]))

# k-nearest
# import KNN classifier
from sklearn.neighbors import KNeighborsClassifier

# n_neighborsint is for number of neighbors
# p is the power parameter for the Minkowski metric
knn_model1 = KNeighborsClassifier(n_neighbors=1, p=2).fit(x, y)
knn_model3 = KNeighborsClassifier(n_neighbors=3, p=2).fit(x, y)
knn_model5 = KNeighborsClassifier(n_neighbors=5, p=2).fit(x, y)
# call the predict_test function to predict the test data
model_name1 = "KNN,k=1"
model_name3 = "KNN,k=3"
model_name5 = "KNN,k=5"
predict_test(Xtest, knn_model1, model_name1)
predict_test(Xtest, knn_model3, model_name3)
predict_test(Xtest, knn_model5, model_name5)

#Support vector machine
# import SVM package
from sklearn.svm import SVC
# choose the linear kernel for linear SVM
lsvm_model = SVC(kernel='linear').fit(x, y)
# call the predict_test function to predict the test data
model_name = "Linear SVM"
predict_test(Xtest, lsvm_model, model_name) 





