Readme:

in order to run the code you need to:

Download the data from kaggle: https://www.kaggle.com/c/yelp-recruiting/data. Please download both the test and training sets. 

Install MongoDB

Insert the yelp dataset into the MongoDB

	 This can be done with the following commands, note the name of the databases which are hardcoded in the python code. 

	 	mongoimport --collection training_review --file yelp_training_set_review.json
	 	mongoimport --collection test_review --file yelp_test_set_review.json

		mongoimport --collection training_user --file yelp_training_set_user.json
	 	mongoimport --collection test_user--file yelp_test_set_user.json

		mongoimport --collection training_checkin --file yelp_training_set_checkin.json
	 	mongoimport --collection test_checkin --file yelp_test_set_checkin.json

		mongoimport --collection training_business --file yelp_training_set_business.json
	 	mongoimport --collection test_business--file yelp_test_set_business.json


Make sure all the data is in the MongoDb. 


Run Yelp.py:

	python yelp.py. 

	Note: the file will spit out a lot of output including a plot, at some point it will take a while while computing the Random forest. Don't worry, time ot have a cofee, it's about 6 mins, and it will tell you what it's doing. 
	When it's done it will spit out the RMSLE. 


cheers
Gustavo 