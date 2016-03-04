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
workspace_dir = "C:/Users/dm1-3266/PycharmProjects/ud120-projects/"
enron_data = pickle.load(open(workspace_dir + "final_project/final_project_dataset.pkl", "r"))

# size of the Enron Datasets
print len(enron_data)

# Features in the Enron Dataset
print len(enron_data[enron_data.keys()[1]])

# POIs in the Enron Data
counter = 0
for k in enron_data.keys():
    if enron_data[k]["poi"]:
        counter += 1

print counter

# Query the Dataset 1
print enron_data["PRENTICE JAMES"]["total_stock_value"]

# Query the Dataset 2
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

# Query the Dataset 3
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Research the Enron Fraud
# Follow the Money
max(enron_data["SKILLING JEFFREY K"]["total_payments"],enron_data["LAY KENNETH L"]["total_payments"],
    enron_data["FASTOW ANDREW S"]["total_payments"])

# Dealing with Unfilled Features
counter = 0
for k in enron_data.keys():
    if type(enron_data[k]["salary"]) == int:
        counter += 1

print counter

counter = 0
for k in enron_data.keys():
    if enron_data[k]["email_address"] != "NaN":
        counter += 1

print counter





