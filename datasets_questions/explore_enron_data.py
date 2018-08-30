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

#print(len(enron_data["SKILLING JEFFREY K"]))
features = enron_data["SKILLING JEFFREY K"].keys()

#num_of_poi = 0

# for person in enron_data:
# 	if (enron_data[person]["poi"] == 1):
# 		num_of_poi += 1

# print(num_of_poi)
#print(enron_data["PRENTICE JAMES"]["total_stock_value"])

#print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])

# print(enron_data['SKILLING JEFFREY K']['total_payments'])
# print(enron_data['LAY KENNETH L']['total_payments'])
# print(enron_data['FASTOW ANDREW S']['total_payments'])

num_of_salaries = 0
num_of_emails = 0
num_nan_total_payments = 0
poi_with_no_pay = 0
num_of_poi = 0


for person in enron_data:
	if (enron_data[person]["poi"] == True):
		num_of_poi += 1
	
	if isinstance(enron_data[person]['salary'], int):
		num_of_salaries += 1

	if enron_data[person]['email_address'] != 'NaN':
		num_of_emails += 1

	if enron_data[person]['total_payments'] == 'NaN':
		num_nan_total_payments += 1
		if enron_data[person]['poi'] == True:
			poi_with_no_pay += 1

print(num_of_salaries)
print(num_of_emails)
print "NAN Total payments", num_nan_total_payments
print "POI with no pay", poi_with_no_pay
print "POIs: ", num_of_poi

num_people = len(enron_data)
print("Num of People: ", num_people)
