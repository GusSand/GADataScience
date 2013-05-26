## The german Credit data set contains 25 columns. 
## columns 1 - 20 are actual data features
## columns 21 - 24 are indicator columns
## column 25 is the classificator column

 
## Read in the data set. 
# apparently only works if we put sep=""
df <- read.csv('homework_1.txt', header=FALSE, sep="")

## quick summary of all data
head(df)
summary(df)


## quick look to see the classification of all 100
## give some rownames
#x <- (1:1000)
#qqplot (x, df$V25)

## the above graph showed tha somewhere between 600 - 800
## of the people in the study had  good credit = 1, 
## whereas the rest have bad = 2. 
## Find out the real number with the table function
## which gives us that it's 
## 700 -> 1
## 300 -> 2
#class <- table(df$V25)
#class

# let's use a regular linear model first, and plot it against our data set
fit <- lm(V25 ~ ., data=df)
summary(fit)

# remove all the indicator columns ? 
## TODO: does this make sense ? 
fit2 <- update(fit, .~. -V24 -V23 -V22 -V21)

# remove the one with lowest t score
fit3 <- update(fit2, .~. -V8)
summary(fit3)

fit4 <- update(fit3, .~. -V13)
summary(fit4)

fit5 <- update(fit4, .~. -V10)
summary(fit5)

plot(resid(fit5))		# want to see absence of structure in resid scatterplot ("gaussian white noise")
## not good yet, let's remove more. 

fit6 <- update(fit5, .~. -V4)
summary(fit6)

fit7 <- update(fit6, .~. -V14)
summary(fit7)

## it's looking kind of good
plot(resid(fit7))
qqnorm(resid(fit7))


# let's use a regular linear model first, and plot it against our data set
fit <- lm(pairs ~ ped, df)
plot(pairs ~ ped, df)
abline(fit, col="red")

# What's going on here? Do we think this is a good fit of the model?
# probably not.

# Let's try polynomial regression at various levels and compare each performance

# fit with two values
fit2 <- lm(pairs ~ poly(ped, 2), df)
points(df$ped, predict(fit2), col="blue", type="l")

# fit with three values
fit3 <- lm(pairs ~ poly(ped, 3), df)
points(df$ped, predict(fit3), col="orange", type="l")

# fit with four values
fit4 <- lm(pairs ~ poly(ped, 4), df)
points(df$ped, predict(fit4), col="green", type="l")



# which data set performed the best? Why do you think so?

# check the analysis of variance between each fit. which fit has the best p value?
anova(fit, fit2, fit3, fit4)