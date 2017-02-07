#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
from sklearn.svm import SVC
classifier = SVC(kernel="linear")

t0 = time()
classifier.fit(features_train, labels_train)
print "SVM training time", round(time() - t0, 3), "s"

t0 = time()
score = classifier.score(features_test, labels_test)
print "SVM testing time", round(time() - t0, 3), "s"

print "SVM accuracy =", score
#########################################################


