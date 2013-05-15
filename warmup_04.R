#load required libraries
install.packages('DMwR')
library(DMwR)

#preprocessing/load data
data(algae)
summary(algae)

hist(algae$mxPH, prob = T)	# histogram

plot(algae$NH4, xlab = '')	# generic plot
abline(h = mean(algae$NH4, na.rm = T), lty = 1)  #abline line type = 1 (straight)
abline(h = mean(algae$NH4, na.rm = T) + sd(algae$NH4, na.rm = T), lty = 2) #abline line type = dots
abline(h = median(algae$NH4, na.rm = T), lty = 3)  #same as first except line type = ??

lm(PO4 ~ oPO4, data = algae) #linear model of PO4 
clean.algae <- knnImputation(algae, k = 10) ##Fill in the unknown nearest neighbors

lm.a1 <- lm(a1 ~ ., data = clean.algae[, 1:12]) # linear model
summary(lm.a1)
anova(lm.a1) 	## analysis of variance

lm2.a1 <- update(lm.a1, . ~ . - season)
summary(lm2.a1)		##
anova(lm.a1, lm2.a1)	## analysis of variance

final.lm <- step(lm.a1)	## Choose a model by AIC in a Stepwise Algorithm
