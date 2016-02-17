#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
workspace_dir = "C:/Users/dm1-3266/PycharmProjects/ud120-projects/"
sys.path.append(workspace_dir+"tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
### timing the training ###
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0,3), "s"
### timing the prediction ###
t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1,3), "s"

### now print the accuracy ###
from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)


#########################################################


