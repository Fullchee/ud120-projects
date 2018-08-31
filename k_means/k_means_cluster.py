#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.preprocessing import MinMaxScaler




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

# find the range of exercised_stock_options
lowest_stock_option = 1e10
highest_stock_option = 0
lowest_salary = 1e10
highest_salary = 0

for person in data_dict:
    stock_options = data_dict[person]['exercised_stock_options']

    if stock_options != 'NaN':
        if stock_options > highest_stock_option:
            highest_stock_option = stock_options

        if stock_options < lowest_stock_option:
            lowest_stock_option = stock_options

for person in data_dict:
    salary = data_dict[person]['salary']

    if salary != 'NaN':
        if salary > highest_salary:
            highest_salary = salary

        if salary < lowest_salary:
            lowest_salary = salary

print "highest_stock_option: ", highest_stock_option
print "lowest_stock_option: ", lowest_stock_option
print "highest salary: ", highest_stock_option
print "lowest_ salary: ", lowest_stock_option

### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2)
kmeans.fit(finance_features)
pred = kmeans.predict(finance_features)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"

# Feature Scaling
scaler = MinMaxScaler()
print "Rescaled $200 000: ", scaler.fit_transform([[float(lowest_salary)], [200000], [float(highest_salary)]]) # 0.17962407 (holy cow, a $200 000 salary is on the low end), I guess that makes sense compared to a million that Skillings had

print "Rescaled $1 000 000: ", scaler.fit_transform([[float(lowest_stock_option)], [1000000], [float(highest_stock_option)]]) # holy sh*t, 0.02902059, a million dollars is 2% of what someone else got