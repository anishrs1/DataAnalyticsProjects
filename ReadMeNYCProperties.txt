The goal of this project is to find out the variables that most influence the selling price of real 
estate properties in New York City. First, I imported the dataset containing information about the 
83,000 properties in New York City. Then, I cleaned the data by removing duplicate entries and null
values in the dataset. Upon realizing the potential inaccuracies outliers could cause, I removed 
the outliers in selling price in order to normalize my data. Afterwards, I paired every single variable
with the sale price and then ran the randomforest regressor for every set of variables and computed the
root-mean square error. I found that this value, the root-mean square error was the lowest for the two 
variables borough location and sale price. Moreover, the root-mean square error was 0.58, which is between
0.2 and 0.6 and thus is a huge indication that the borough location is a reasonably good predictive variable 
for the sale price of a property in New York City.