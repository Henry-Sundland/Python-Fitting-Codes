# Python Fitting Codes
 Codes I created, in python, to fit to supplied data sets and the like. Just doing this stuff for fun and to review things important for computational physics and analysis.

Will update randomly with codes for things.

At this moment, this repository has the following python codes I made:

1.) Linear Least Squares (without uncertainty weights and stuff)

2.) Least Linear squares (with weights to fit to data that includes uncertainties)




~ code descriptions ~

1.) Linear Least Squares (without weighted uncertainty handling) - a mathematical approach used to find the best-fitting straight line through a set of data points. The goal is to minimize the sum of the squared differences (residuals) between the observed values and the values predicted by the linear model. This method is widely used in regression analysis to estimate the parameters of a linear relationship between variables. Given a supplied set of (x,y) data, the code first plots y vs x, and then (once you close out of the plot lol) applies and graphs the fit line. It displays the fit equation too and prints uncertainties in fit values. This code doesn't take into account weighted uncertainties in the data set, but I'll post a code for that in a bit


2.) Least Linear Squares (with weights to handle data with uncertainties) - performs a weighted linear least squares fit to the data. It calculates the slope and y-intercept of the best-fit line, along with their uncertainties, and computes the chi-squared value to assess the goodness of fit. The code then plots the data points with vertical error bars representing the uncertainties and overlays the fitted line on the plot. The result is a visual representation of the linear relationship between the data, along with the associated uncertainties in the measurements and fit parameters.
