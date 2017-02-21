#!/usr/bin/python
from time import time

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

print "Feature count = ", len(features_train[0])
print "Training points = ", len(features_train)

from sklearn.ensemble import AdaBoostClassifier

# n = 25 --> 0.924
# n = 25, L = 2.0 --> 0.836
# n = 25, L = 0.25 --> 0.928
# n = 35, L = 0.2 --> 0.92
# n = 50 --> 0.924
# n = 50, L = 0.25 --> 0.928
# n = 100, L = 0.1 --> 0.92
# n = 100 --> 0.924
clf = AdaBoostClassifier(n_estimators=50, learning_rate=0.25)

t0 = time()
clf.fit(features_train, labels_train)
print "Training time: ", round(time() - t0, 3), "s"

t0 = time()
accuracy = clf.score(features_test, labels_test)
print "Testing time: ", round(time() - t0, 3), "s"
print "Accuracy: ", accuracy




try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
