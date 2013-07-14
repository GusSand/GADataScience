from pymongo import MongoClient
from sklearn import linear_model
from sklearn.metrics import r2_score
from pandas import *
import pylab as pl 
import pandas as pd 
import numpy as np 
#from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour
from datetime import datetime
from ols import ols


def printSeparator():
	print '=============================================================================='



#######################


# I assume that the db is already loaded into Mongo
db = MongoClient().test

review_coll = db['review']
review_count = review_coll.count()
print "\ntotal number of reviews: %d" % review_count


total = review_count
base_date = datetime(2013, 01, 01)

print "\ntotal used for now: %d" % total

textArray = [None] * total
starsArray = [None] * total
usefulArray = [None] * total
dateArray = [None] * total
dateDeltaArray = [None] * total

# get the data into two arrays

x = 0
for review in review_coll.find() :
	text = review['text']

	usefulArray[x] = review['votes']['useful']

	# date on on Mongo is of the form 2011-01-30 
	datestring = review['date']
	dateArray[x] = datetime.strptime(datestring, '%Y-%m-%d')
	tdelta = base_date - dateArray[x]
	dateDeltaArray[x] = tdelta.total_seconds()
	
	textArray[x] = len(text)
	starsArray[x] = review['stars']

	x = x + 1
	if x == total :
		break


# converts the lists into numpy Arrays 
ta = np.array(textArray)
sa = np.array(starsArray)

#dateArray.sort()
#dateDeltaArray.sort()
da = np.array(dateDeltaArray)

print "\nreview length mean: ", np.mean(ta)
print "\nstar review mean: ", np.mean(sa)

ua = np.array(usefulArray)
print "\nusefulArray mean: ", np.mean(ua)

# graphic
# scatter(sa, ta, marker ='^', c='r')
# show()

printSeparator()

print "coefficient based on only one variable"

#print "\npredictors:\n", predictors
regr = linear_model.LinearRegression()

# the slicing below needs to be done because 
# linear regression needs a 2d array
regr.fit (ta[:, np.newaxis], ua)
print "\n text length coeff: \n", regr.coef_


regr.fit (sa[:, np.newaxis], ua)
print "\n stars coeff: \n", regr.coef_


regr.fit (da[:, np.newaxis], ua)
print "\n date delta coeff: \n", regr.coef_

print "========================================================="


# use OLS this time
predictor = np.column_stack((ta, sa, da))

#, 'useful', ['text length', 'stars'])
model = ols(ua, predictor) 
print "coefficient p-values ", model.p
print model.summary()


#pl.scatter(textArray, starsArray, color='black')
#pl.plot(textArray, regr.predict(textArray), color='blue', linewidth=3)


#pl.xticks(())
#pl.yticks(())

#pl.show()


