### Date created
17th March 2019

### Project Title
Bikeshare

### Description
This project explores randomly selected bike sharing data of Chicago, New York City, and Washington within the time period of Jan-Jun 2017. The original data has been provided by [Motivate], a bike share system provider for many major cities in the United States. For the purpose of this project the data has been prepared and reduced in size and scope in advance. Bikeshare allows to gather descriptive statistics as well as data excerpts within an interactive terminal session. The data can be filtered as follows: 

| Filter | Options |
| ------ | ------ |
| CHOOSE CITY | Chicago, New York City, Washington |
| CHOOSE MONTH | number of the month or zero for all months available |
| CHOOSE DAY | number of the day (Monday=1, Sunday=7) or zero for the entire week |

Descriptive statistics are provided for the following attributes:
* Travel start times
* Poular stations and trips
* Travel duration
* User age, type and gender (if available)

### Files used
The following files are used within Bikeshare:
* chicago.csv
* new_york_city.csv
* washington.csv

### Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

```sh
Start Time (e.g., 2017-01-01 00:07:57)
End Time (e.g., 2017-01-01 00:20:53)
Trip Duration (seconds - e.g., 776)
Start Station (e.g., Broadway & Barry Ave)
End Station (e.g., Sedgwick St & North Ave)
User Type (Subscriber or Customer)
```
The Chicago and New York City files also have the following two columns:
```sh
Gender
Birth Year
```

### Credits
The links and blogposts below were consulted during this project:
https://stackoverflow.com/questions/4048651/python-function-to-convert-seconds-into-minutes-hours-and-days/4048773
https://dzone.com/articles/pandas-find-rows-where-columnfield-is-null
https://stackoverflow.com/questions/20461165/how-to-convert-index-of-a-pandas-dataframe-into-a-column
https://stackoverflow.com/questions/27673231/why-should-i-make-a-copy-of-a-data-frame-in-pandas
https://erikrood.com/Python_References/add_new_col_df_default_value_final.html
https://jakevdp.github.io/PythonDataScienceHandbook/03.05-hierarchical-indexing.html
https://stackoverflow.com/questions/3371269/call-int-function-on-every-list-element
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.sort_values.html
https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.astype.html
https://docs.scipy.org/doc/numpy/reference/generated/numpy.percentile.html
https://www.codementor.io/sheena/how-to-write-python-custom-exceptions-du107ufv9

[Motivate]: <https://www.motivateco.com/>

