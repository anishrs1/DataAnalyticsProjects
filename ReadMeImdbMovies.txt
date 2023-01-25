This project is based on a dataset that contains information about all movies on Imdb from 2006 to 2016. The purpose
of this project is to find out and identify which exact categories from the dataset have the most influence
on the overall popularity of a movie. First, we imported the dataset using the read_csv function. Then, we cleaned
the dataset to remove blank fields, incorrect datatypes, irrelevant values and unnecessary columns from the
table. Afterwards, we used the xgbclassifier package to predict the values of all the variables within the dataset.
Then, we used the pyplot package from matplotlib libary to display the model that illustrates the variables that
have the biggest influence on a movie's popularity. From the results, the variables that have the most influence
on a movie's popularity are number of votes, director and revenue of a particular movie.