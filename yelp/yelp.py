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

	# default for count of user_useful is the mean
	np_user_useful = np.array(user_useful)
	mean_user_useful = np.mean(np_user_useful)
	print "\nmean user Useful ", mean_user_useful

	#default for count of user_
	np_user_review_count = np.array(user_reviewCount)
	#print "\n user review array \n", user_reviewCount
	mean_user_review_count = np.mean(np_user_review_count)
	print "\nmean user review count ", mean_user_review_count

	x = 0
	for review in review_coll.find() :
		#stars = review['stars']
		text = review['text']

		review_useful_count[x] = review['votes']['useful']

		# date on on Mongo is of the form 2011-01-30 
		datestring = review['date']
		dateArray[x] = datetime.strptime(datestring, '%Y-%m-%d')
		tdelta = base_date - dateArray[x]
		dateDeltaArray[x] = tdelta.total_seconds()
		
		textArray[x] = len(text)
		starsArray[x] = review['stars']

		review_userId[x] = review['user_id']
		review_bizId[x] = review['business_id']

		review_user_useful[x] = user_useful_dict.get(review_userId[x], mean_user_useful)
		review_user_review_count[x] = user_review_count_dict.get(review_userId[x], mean_user_review_count)


		x = x + 1
		if x == review_total :
			break


def get_UserData() :

	print "\ntotal number of users: ", user_count
	print "\ntotal used for now: ", user_total

	printSeparator()

	x = 0
	for user in user_coll.find() :
		user_userId[x] = user['user_id']
		user_avgStars[x] = user['average_stars']
		user_reviewCount[x] = user['review_count']
		
		user_useful[x] = user['votes']['useful']

		user_useful_dict[user_userId[x]] = user_useful[x]
		user_review_count_dict[user_userId[x]] = user_reviewCount[x]


		x = x + 1
		if x == user_total :
			break



def get_BizData() :

	print "\ntotal number of biz: ", biz_count
	print "\ntotal biz used for now ", biz_total

	printSeparator()

	x = 0
	for biz in biz_coll.find() :
		biz_bizId[x] = biz['business_id']
		biz_reviewCount[x] = biz['review_count']
		biz_stars[x] = biz['stars']

		x = x + 1
		if x == biz_total :
			break


############################################################################

#global data

# I assume that the db is already loaded into Mongo
db = MongoClient().test

review_coll = db['review']
review_count = review_coll.count()
review_total = review_count

textArray = [None] * review_total
starsArray = [None] * review_total
review_useful_count = [None] * review_total
dateArray = [None] * review_total
dateDeltaArray = [None] * review_total
review_userId = [None] * review_total
review_bizId = [None] * review_total 
review_user_useful = [None] * review_total
review_user_review_count = [None] * review_total

user_coll = db['user']
user_count = user_coll.count()
user_total = user_count

user_userId = [None] * user_total
user_avgStars = [None] * user_total
user_reviewCount = [None] * user_total
user_useful = [None] * user_total
user_useful_dict = dict()
user_review_count_dict = dict()

biz_coll = db['business']
biz_count = biz_coll.count()
biz_total = biz_count

biz_bizId = [None] * biz_total
biz_reviewCount = [None] * biz_total
biz_stars = [None] * biz_total 


get_UserData()
get_BizData()
get_ReviewData()


# converts the lists into numpy Arrays 
ta = np.array(textArray)
sa = np.array(starsArray)
ua = np.array(review_useful_count)

#dateArray.sort()
#dateDeltaArray.sort()
da = np.array(dateDeltaArray)

#print "\nreview length mean: ", np.mean(ta)
#print "\nstar review mean: ", np.mean(sa)

#ua = np.array(review_useful_count)
#print "\nreview_useful_count mean: ", np.mean(ua)

# graphic
# scatter(sa, ta, marker ='^', c='r')
# show()
#
###########
# printSeparator()

# print "coefficient based on only one variable"

# #print "\npredictors:\n", predictors
# regr = linear_model.LinearRegression()

# # the slicing below needs to be done because 
# # linear regression needs a 2d array
# regr.fit (ta[:, np.newaxis], ua)
# print "\n text length coeff: \n", regr.coef_

# # not use matplotlib scatter
# #scatter(ta, ua, marker ='^', c='r')
# #show()

# regr.fit (sa[:, np.newaxis], ua)
# print "\n stars coeff: \n", regr.coef_
# #scatter(sa, ua, marker ='o', c='r')
# #show()


# regr.fit (da[:, np.newaxis], ua)
# print "\n date delta coeff: \n", regr.coef_
# #scatter(da, ua, marker ='+', c='r')
# #show()

# printSeparator()

# print "coefficient based on two variables"
# print "text length & stars"

# # use OLS this time
# predictor = np.column_stack((ta, sa))

# #, 'useful', ['text length', 'stars'])
# model = ols(ua, predictor, 'useful', ['length', 'stars']) 
# print "coefficient p-values ", model.p
# print model.summary()



# printSeparator()

print "coefficient based on five variables"


# use OLS this time
ruu = np.array(review_user_useful)
rurc = np.array(review_user_review_count)



predictor = np.column_stack((ta, sa, da, rurc, ruu))

#, 'useful', ['text length', 'stars'])
model = ols(ua, predictor, 'useful', ['length', 'stars', 'age', 'user_reviews', 'user_useful']) 
print "coefficient p-values ", model.p
print model.summary()


#pl.scatter(textArray, starsArray, color='black')
#pl.plot(textArray, regr.predict(textArray), color='blue', linewidth=3)


#pl.xticks(())
#pl.yticks(())

#pl.show()


