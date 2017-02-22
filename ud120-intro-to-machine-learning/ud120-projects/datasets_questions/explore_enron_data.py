#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

people = list(enron_data)
print "# people:", len(people)
print "people = ", people
firstPerson = people[0]
print "features per person:", len(enron_data[firstPerson])

poi = 0
for person, features in enron_data.iteritems():
    poi += features["poi"]

print "poi:", poi

print "James Prentice's stock = ", enron_data["PRENTICE JAMES"]["total_stock_value"]

v1 = "LAY", enron_data["LAY KENNETH L"]["total_payments"]
v2 = "SKILLING", enron_data["SKILLING JEFFREY K"]["total_payments"]
v3 = "FASTOW", enron_data["FASTOW ANDREW S"]["total_payments"]

winner = max([v1, v2, v3], key=lambda item: item[1])
print "Winner = ", winner

withSalary = 0
for person in list(enron_data):
    if "salary" in enron_data[person] and enron_data[person]["salary"] != "NaN":
        withSalary += 1

print "With salary:", withSalary

withEmail = 0
for person in list(enron_data):
    if "email_address" in enron_data[person] and enron_data[person]["email_address"] != "NaN":
        withEmail += 1

print "With email:", withEmail

withTotalPayment = 0
for person in list(enron_data):
    if "total_payments" in enron_data[person] and enron_data[person]["total_payments"] != "NaN":
        withTotalPayment += 1

print "With total payment:", withTotalPayment

nanPoi = 0
for person in list(enron_data):
    if enron_data[person]["poi"] and enron_data[person]["total_payments"] == "NaN":
        nanPoi += 1

print "POI w/ NaN for payments:", nanPoi

