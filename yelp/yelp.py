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


def get_ReviewData():

	base_date = datetime(2013, 01, 01)

	print "\nabout the review data:"
	print "\ntotal number of reviews: %d" % review_count
	print "\ntotal used for now: %d" % review_total

	printSeparator()

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

		review_userId = review['user_id']
		review_bizId = review['business_id']


		x = x + 1
		if x == review_total :
			break


def get_UserData() :

	print "\ntotal number of users: ", user_count
	print "\ntotal used for now: ", user_total

	printSeparator()

	x = 0
	for user in user_coll.find() :
		user_userId = user['user_id']
		user_avgStars = user['average_stars']
		user_reviewCount = user['review_count']
		user_useful = user['votes']['useful']

		x = x + 1
		if x == user_total :
			break



def get_BizData() :

	print "\ntotal number of biz: ", biz_count
	print "\ntotal biz used for now ", biz_total

	printSeparator()

	x = 0
	for biz in biz_coll.find() :
		biz_bizId = biz['business_id']
		biz_reviewCount = biz['review_count']
		biz_stars = biz['stars']

		x = x + 1
		if x == biz_total :
			break


############################################################################

#global data

# I assume that the db is already loaded into Mongo
db = MongoClient().test

review_coll = db['review']
review_count = review_coll.count()
review_total = 500 #review_count

textArray = [None] * review_total
starsArray = [None] * review_total
usefulArray = [None] * review_total
dateArray = [None] * review_total
dateDeltaArray = [None] * review_total
review_userId = [None] * review_total
review_bizId = [None] * review_total 

user_coll = db['user']
user_count = user_coll.count()
user_total = 50 # user_count

user_userId = [None] * user_total
user_avgStars = [None] * user_total
user_reviewCount = [None] * user_total
user_useful = [None] * user_total

biz_coll = db['business']
biz_count = biz_coll.count()
biz_total = 50 # biz_count

biz_bizId = [None] * biz_total
biz_reviewCount = [None] * biz_total
biz_stars = [None] * biz_total 



get_ReviewData()

get_UserData()

get_BizData()


# converts the lists into numpy Arrays 
ta = np.array(textArray)
sa = np.array(starsArray)
ua = np.array(usefulArray)

#dateArray.sort()
#dateDeltaArray.sort()
da = np.array(dateDeltaArray)

#print "\nreview length mean: ", np.mean(ta)
#print "\nstar review mean: ", np.mean(sa)

#ua = np.array(usefulArray)
#print "\nusefulArray mean: ", np.mean(ua)

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

# not use matplotlib scatter
#scatter(ta, ua, marker ='^', c='r')
#show()

regr.fit (sa[:, np.newaxis], ua)
print "\n stars coeff: \n", regr.coef_
#scatter(sa, ua, marker ='o', c='r')
#show()


regr.fit (da[:, np.newaxis], ua)
print "\n date delta coeff: \n", regr.coef_
#scatter(da, ua, marker ='+', c='r')
#show()

printSeparator()

print "coefficient based on two variables"
print "text length & stars"

# use OLS this time
predictor = np.column_stack((ta, sa))

#, 'useful', ['text length', 'stars'])
model = ols(ua, predictor, 'useful', ['length', 'stars']) 
print "coefficient p-values ", model.p
print model.summary()



printSeparator()

print "coefficient based on three variables"


# use OLS this time
predictor = np.column_stack((ta, sa, da))

#, 'useful', ['text length', 'stars'])
model = ols(ua, predictor, 'useful', ['length', 'stars', 'age']) 
print "coefficient p-values ", model.p
print model.summary()


#pl.scatter(textArray, starsArray, color='black')
#pl.plot(textArray, regr.predict(textArray), color='blue', linewidth=3)


#pl.xticks(())
#pl.yticks(())

#pl.show()


