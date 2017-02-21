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

from sklearn.ensemble import RandomForestClassifier

# n = 10 --> 0.924
# n = 20 --> 0.928
# n = 20, min split = 3 --> 0.912
# n = 20, min split = 2 --> 0.92
# n = 20, min split =4 --> 0.932
# n = 30 --> 0.916

clf = RandomForestClassifier(n_estimators=25, min_samples_split=2, min_samples_leaf=3)

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
