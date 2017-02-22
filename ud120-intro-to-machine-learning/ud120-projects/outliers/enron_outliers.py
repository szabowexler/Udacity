#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

### read in data dictionary, convert to numpy array
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

names = list(data_dict)
maxBonusName = max(names, key=lambda name: data_dict[name]["bonus"] if data_dict[name]["bonus"] != "NaN" else 0)
data_dict.pop(maxBonusName, 0)

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

for name in list(data_dict):
    salary_ = data_dict[name]["salary"]
    if (salary_ != "NaN" and salary_ > 1000000):
        print "High salary:", name, " = ", salary_
    bonus_ = data_dict[name]["bonus"]
    if (bonus_ != "NaN" and bonus_ > 5000000):
        print "High bonus:", name, " = ", bonus_

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
