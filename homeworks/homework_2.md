## Homework
Data Science III, General Assembly
Gustavo Sandoval


#Journal Review:
"Word Usage mirrors community structure in Twitter"
Authors: 
John Bryden, Sebastian Funk and Vincent AA Jansen


# Objective/Abstract: 
Word analysis  provides the ability to automate de classification of communities in social networks and identify emerging social groups.
There are numerous applications of these classification including:
social group identification, 
customizing online experience, 
targeted marketing, and
crowd-source characterization

# Hypothesis: 
Word usage should closely match the community structure of a social network 

# Methods: 
189 thousand users were sampled, along with 75 million tweets and calculated a global clustering coefficient of 0.084. 

## Network Sampling
The sample network was formed using a process called snowball-sampling. This means that that for each user sampled:
1. all the conversational tweets were recorded. (DMs)
2. new users referenced  where added to the list of users to be picked next
3.  Retweets where ignored


## Ranking words within a community
Compared the fraction of users that use each word within a community with the fraction of users that used the word globally


## Comparing communities using a bootstrap
For each word used by a community, they calculated its relative word usage frequency. 
This means the proportion of the total word instances what were a certain word. 



## Predicting communities of individual users
To predict the communities of individual users they compared the individual word usage with community word usage to select the best matching community. 



# Conclusions: 

I think that this paper was for the most part well written. I learned a lot from it and enjoyed reading it.  I knew from the beginning and throughout what the authors wanted to show. However, one problem I see is that from the beginning there isn't a shadow of a doubt that the hyphotesis will hold true. 

It was also interesting for me to realize that during the results discussion a lot of terms I didn't know were used such as bootstrap, maximum modularity, etc . However once we got to the methods section most of those were explained. Since this is my first foray into reading these kind of papers, I don't know if this is the way a lot of these academic papers are written. 

Even after reading the paper, it was a little hard to follow the technical explanation of some of the methodologies.   For example, comparing communities using bootstrap, I"m not sure how that works. 


##Glossary:

* Clustering coefficient - In graph theory, a clustering coefficient is a measure of degree to which nodes in a graph tend to cluster together. http://en.wikipedia.org/wiki/Clustering_coefficient

* Modularity is one measure of the structure of networks or graphs. Designed to 


