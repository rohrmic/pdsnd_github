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
It's important to give proper credit. Add links to any repo that inspired you or blogposts you consulted.

