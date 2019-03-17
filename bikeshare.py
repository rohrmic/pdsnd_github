import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# a list is used to guarantee the correct order of the list items in the user prompt
CITIES = ['chicago','new york city','washington']

MONTHS = ['January','February','March','April',
          'May','June','July','August',
          'September','October','November','December']

DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def print_calc_time(start_time):
    print("\ncalculation time: %s" % (time.time() - start_time))

def convert_seconds(seconds):
    """
    Converts seconds into days, hours, minutes and remaining seconds.
    divmod takes two numbers and returns a pair of numbers (a tuple) 
    consisting of their quotient and remainder
    """
    
    days = divmod(seconds, 86400) 
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    return days[0], hours[0], minutes[0], minutes[1]

def print_without_index(df, rows=5):
    """Returns first 5 rows of dataframe without auto-index."""
    
    blankIndex=[''] * len(df)
    df.index=blankIndex
    print(df.head(rows))

def check_null_columns(df, city):
    """Lists null values per column."""
    
    start_time = time.time()
    
    print('\nNumber of null values in {} \n'.format(CITY_DATA[CITIES[city-1]]))
    
    null_columns=df.columns[df.isnull().any()]
    if null_columns.empty:
        print("There are no null values in this data set.")
    else:
        ds = df[null_columns].isnull().sum()
        for index, val in ds.iteritems():
            print("{}: {} / {}%".format(index, val, round(100*val/len(df.index), 2)))
        
    print_calc_time(start_time)
    print('-'*75)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze. For convenience to the user 
    a corresponding number can be selected for these items. before viewing the data user 
    has to confirm choice.
    Returns:
        (int) city - number of the city to analyze
        (int) month - number of the month to filter by, or "0" to apply no month filter
        (int) day - number of the day of week to filter by, or "0" to apply no day filter
    """
    
    #filters = {} # not used, filters are returned individually as three integers
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    # set flags to control the logic of the user prompt (subject to refactoring)
    city_flag = True
    month_flag = True
    day_flag = True
    confirm_flag = True
    choice_flag = True
    
    # user has to confirm choice after selecting all the filters
    while confirm_flag and choice_flag:
    
    # get user input for city, month, day of the week and confirmation
        print('\nCHOOSE CITY') 
        while city_flag:
            
            print('1) Chicago') 
            print('2) New York City') 
            print('3) Washington')
            try:
                userInput = int(input("Please enter a number for the city: "))
                if userInput in [1,2,3]:
                    city = userInput
                    city_flag = False
            except ValueError:
                print("\nPlease enter a number from the selection below.")
                
        print('\nCHOOSE MONTH', end="") 
        while month_flag:
            
            try:
                userInput = int(input("\nPlease enter the number of the month or '0' for all months available \n(January to June 2017): "))
                if userInput in range(0,7):
                    month = userInput
                    month_flag = False
            except ValueError:
                print("\nPlease enter a number for the month from 1-6 or '0' for all months available.")
            
        print('\nCHOOSE DAY', end="") 
        while day_flag:
            
            try:
                userInput = int(input("\nPlease select the number of the day (Monday=1, Sunday=7) or '0' for the \nentire week: "))
                if userInput in range(0,8):
                    day = userInput
                    day_flag = False
            except ValueError:
                print("\nPlease enter a number for the day from 1-6.")
                
        print('\nCONFIRM YOUR CHOICE', end="")
        if day == 0 and month == 0:
            print('\nYou chose data for: {} / {} through {} / {} through {}'.format(CITIES[city-1].title(), MONTHS[0], MONTHS[6-1], DAYS[0], DAYS[6]))
        elif month ==0 and day != 0:
            print('\nYou chose data for: {} / {} through {} / {}'.format(CITIES[city-1].title(), MONTHS[0], MONTHS[11], DAYS[day-1]))
        elif month !=0 and day == 0:
            print('\nYou chose data for: {} / {} / {} through {}'.format(CITIES[city-1].title(), MONTHS[month-1], DAYS[0], DAYS[6]))
        else:
            print('\nYou chose data for: {} / {} / {}'.format(CITIES[city-1].title(), MONTHS[month-1], DAYS[day-1]))
        
    # repeat filter dialog or return filter values
        while choice_flag:
            
            try:
                userInput = input("Please confirm with 'yes' or repeat selection with 'no': ")
                if userInput.lower() == 'yes':
                    confirm_flag = False
                    choice_flag = False
                elif userInput.lower() != 'no':
                    raise ValueError
                else:
                    # reset the flags to repeat the process
                    city_flag = True
                    month_flag = True
                    day_flag = True
                    #confirm_flag = True
                    #choice_flag = True
                    break
            except ValueError:
                print("\nPlease type either 'yes' or 'no'.")
    
    print('-'*75)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (int) city - number of the city to analyze
        (int) month - number of the month to filter by, or "0" to apply no month filter
        (int) day - number of the day of week to filter by, or "0" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[CITIES[city-1]])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 0:
        # filter by month to create the new dataframe (January has value of 1)
        month = month
        df = df[df.month == month]
           
    # filter by day of week if applicable
    if day != 0:
        # filter by day of week to create the new dataframe (Monday has value of 0)
        day = day - 1
        df = df[df.day_of_week == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent start times of travel."""

    start_time = time.time()
    print('\n1) Most frequent start times of travel\n')
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Month:', MONTHS[popular_month-1])

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Day:', DAYS[popular_day])

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Hour:', popular_hour)

    print_calc_time(start_time)
    print('-'*75)

def station_stats(df):
    """Displays statistics on the most popular stations and trip(s)."""

    start_time = time.time()
    
    print('\n2) Most popular stations and trip(s)\n')

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Start Station: {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('End Station: {}'.format(popular_end_station))

    cdf = df.copy()
    
    # add new coulumn with default value
    cdf['start_end_count'] = 0
    
    # count combinations of start and end stations
    routes = cdf.groupby(['Start Station','End Station']).count()
    routes = pd.DataFrame(routes['start_end_count'])
    
    # find count for most travelled route(s)
    top_combination = routes.sort_values(by=['start_end_count'], ascending=False).head(1)
    
    # convert index to column
    routes.reset_index(level=['Start Station', 'End Station'], inplace=True)
    
    # display all routes with top count
    routes = routes[routes['start_end_count'] == top_combination.start_end_count[0]]
    print("\nMost popular trip(s):")
    print_without_index(routes)
    
    print_calc_time(start_time)
    print('-'*75)

def trip_duration_stats(df):
    """Displays statistics on the number of trips and the total and average trip duration."""

    start_time = time.time()
    
    time_string = "%i days, %i hours, %i minutes, %i seconds"
    
    count = df['Trip Duration'].count()
    print('\n3) Travel time statistics for a total of %i trips\n' % (count))
    
    # display total travel time
    duration = df['Trip Duration'].sum()
    d, h, m, s = convert_seconds(duration)
    print("Total duration (%i seconds):\n" % (duration) + time_string % (d, h, m, s))
    
    # display mean travel time
    mean = df['Trip Duration'].mean()
    d, h, m, s = convert_seconds(mean)
    print("\nMean (%i seconds):\n" % (mean) + time_string % (d, h, m, s))
    
    # display median travel time
    median = df['Trip Duration'].median()
    d, h, m, s = convert_seconds(median)
    print("\nMedian (%i seconds):\n" % (median) + time_string % (d, h, m, s))

    # display min travel time
    min_duration = df['Trip Duration'].min()
    d, h, m, s = convert_seconds(min_duration)
    print("\nMin (%i seconds):\n" % (min_duration) + time_string % (d, h, m, s))

    # display max travel time
    max_duration = df['Trip Duration'].max()
    d, h, m, s = convert_seconds(max_duration)
    print("\nMax (%i seconds):\n" % (max_duration) + time_string % (d, h, m, s))

    print_calc_time(start_time)
    print('-'*75)

def user_stats(df):
    """
    Displays statistics on bikeshare users.
    Gender and Birth Year is not available for all cities.
    """

    start_time = time.time()
    print('\n4) Statistics for user type and age')

    # display counts of user types
    print("\nUser Types:")
    user_types = df['User Type'].value_counts()
    
    for index, val in user_types.iteritems():
        print("  {}: {}".format(index, val))

    # display counts of gender
    print("\nGender:")
    if 'Gender' not in df:
        print("There is no data available for Gender.")
    else:
        gender = df['Gender'].value_counts()
        for index, val in gender.iteritems():
            print("  {}: {}".format(index, val))

    # display earliest, most recent, and most common year of birth
    print("\nBirth Year:")
    if 'Birth Year' not in df:
        print("There is no data available for Birth Year.")
    else:
        print('  Earliest:', int(df['Birth Year'].min()))
        print('  Latest:', int(df['Birth Year'].max()))
        print('  Most Common:', int(df['Birth Year'].mode()[0]))
        
    print_calc_time(start_time)
    print('-'*75)

def print_drill_down_menu(city):    
    print("\nDRILL DOWN ({})".format(CITIES[city-1].title()))
    print("1) Travel start times")
    print("2) Poular stations and trips")
    print("3) Travel duration")
    print("4) User age")
    print("5) Raw data")
    print("6) Restart")
    print("7) End")          

def get_time_values(df, month):
    '''
    Calculates top five start times by month, week day and hour.

    Args:
        (int) month - number of the month
        df -  Pandas DataFrame containing city data filtered by month and day
    Returns:
        data - ndarray of hours and counts per weekday for specified month
               hours and counts are appended per day, with m=hours,counts; n=top5
               and range=days: [[nxm],[[nxm], .., [nxm]]]
        sorted list of weekdays (available in the df)
    '''
    
    # used to attach the values of the dataframe
    data = np.zeros((5,1))
    
    week_day_list = df.day_of_week.unique()
    for i in np.sort(week_day_list): 
        times = df.copy() # TODO: check if this can be done outside of the loop
        times['count'] = 0
        times = times[(times['month'] == month) & (times['day_of_week'] == i)].groupby(['day_of_week','hour']).count()
        times.reset_index(level=['day_of_week','hour'], inplace=True)
        
    # get top 5 values and day of the week
        sorted_desc_df = times.sort_values(by=['day_of_week','count'], ascending=[True, False]).head()
        day = DAYS[sorted_desc_df.iloc[0]['day_of_week']]
        
    # append ndarrays for hours and counts for each day
        data = np.append(data, sorted_desc_df[['hour','count']].values, axis=1)
        
    # remove zero vector which was used to attach the dataframe    
    data = data[:,1:]
    
    return data.astype(int), np.sort(week_day_list)
        
def show_start_time_data(df): 
    '''
    Returns top 5 start time hours per day and month.
    Calls get_time_values and constructs multi-index dataframe.
    '''
    
    print("1) Travel start times ranking (decending by count)\n")

    tdf = df.copy()
    month_list = tdf.month.unique()
    
    for i in np.sort(month_list):
        data, week_day_list = get_time_values(tdf, i)
        week_day_list = [ DAYS[int(x)] for x in week_day_list ]
    
    # create hierarchical colums
        columns = pd.MultiIndex.from_product([week_day_list, ['hour', 'count']])
        
        time_data = pd.DataFrame(data, columns=columns)
        
        print(MONTHS[i-1])
        #print(time_data)
        print_without_index(time_data)
        
    print('-'*75)
    
def show_stations_data(df):
    '''Displays the 5 most popular start/end stations and trips'''
    
    print("2) Poular stations and trips ranking (decending by count)\n")
    
    start_st = df.copy()
    
    # add new coulumn with default value
    start_st['count'] = 0
    
    # count start stations
    start_st = start_st.groupby(['Start Station']).count()
    start_st = pd.DataFrame(start_st['count'])
    
    # convert index to column
    start_st.reset_index(level=['Start Station'], inplace=True)
    sorted_desc_df_start = start_st.sort_values(by=['count'], ascending=False)
    
    # display the 5 most popular start stations
    print("start station:") 
    print_without_index(sorted_desc_df_start)
    
    end_st = df.copy()
    
    # add new coulumn with default value
    end_st['count'] = 0
    
    # count end stations
    end_st = end_st.groupby(['End Station']).count()
    end_st = pd.DataFrame(end_st['count'])
    
    # convert index to column
    end_st.reset_index(level=['End Station'], inplace=True)
    sorted_desc_df_end = end_st.sort_values(by=['count'], ascending=False)
    
    # display the 5 most popular end stations
    print("\nend station:") 
    print_without_index(sorted_desc_df_end)
    
    routes = df.copy()
    
    # add new coulumn with default value
    routes['trip_count'] = 0
    
    # count combinations of start and end stations
    routes = routes.groupby(['Start Station','End Station']).count()
    routes = pd.DataFrame(routes['trip_count'])

    # convert index to column
    routes.reset_index(level=['Start Station','End Station'], inplace=True)
    sorted_desc_df_trip = routes.sort_values(by=['trip_count'], ascending=False)
    
    # display the 5 most popular trips
    print("\ntrips:") 
    print_without_index(sorted_desc_df_trip)
    
    print('-'*75)

def get_duration_values(df, month):
    '''
    Calculates the 95th percentile for the travel duration per day and given month.

    Args:
        (int) month - number of the month
        df -  Pandas DataFrame containing city data filtered by month and day
    Returns:
        data - array of percentiles per weekday for specified month
               values are appended per day, with range=days: [p0,..,p6]]
        sorted list of weekdays (available in the df)
    '''
    
    # used to attach the values of the dataframe
    data = []
    week_day_list = df.day_of_week.unique()
    for i in np.sort(week_day_list): 
        duration = df.copy() # TODO: check if this can be done outside of the loop
        duration['count'] = 0
        duration = duration[(duration['month'] == month) & (duration['day_of_week'] == i)]
    
    # append values for 95th percentile per day
        data.append(int(round(np.percentile(duration['Trip Duration'], 95),0)))
       
    return data, np.sort(week_day_list)    
    
def show_duration_data(df):
    '''
    Returns 95th percentile for duration per day and month.
    Calls get_duration_values and constructs dataframe.
    '''
    
    print("3) 95th percentile of travel duration\n")
    
    tdf = df.copy()
    month_list = tdf.month.unique()
    
    data_values = []
    month_labels = []
    
    for i in np.sort(month_list):
        data, week_day_list = get_duration_values(tdf, i)
        week_day_list = [ DAYS[int(x)] for x in week_day_list ]
        
    # append labels and list of values for each month available in df
        month_labels.append(MONTHS[i-1])
        data_values.append(data)
        
    duration_data = pd.DataFrame(data=data_values, columns=week_day_list, index=month_labels)

    print(duration_data)
        
    print('-'*75)
    
def show_user_age_data(df):
    """
    Displays top and bottom 5 of birth years with counts
    Birth Year (and Gender) is not available for all cities.
    """
    
    print("4) User age data\n")

    birth_years = df.copy()
    birth_years['count'] = 0

    if 'Birth Year' not in df:
        print("There is no data available for Birth Year.")
    else:
        birth_years = birth_years.groupby(['Birth Year']).count()
        birth_years = pd.DataFrame(birth_years['count'])
    
    # convert index to column
        birth_years.reset_index(level=['Birth Year'], inplace=True)
        
    # convert Birth Year to int for sorting
        birth_years['Birth Year'] = birth_years['Birth Year'].astype(int)
    
        sorted_desc_df = birth_years.sort_values(by=['Birth Year'],ascending=False)
        sorted_asc_df = birth_years.sort_values(by=['Birth Year'],ascending=True)
        sorted_by_count = birth_years.sort_values(by=['count'],ascending=False)
        
        print("years ascending:")    
        print_without_index(sorted_asc_df)
    
        print("\nyears decending:") 
        print_without_index(sorted_desc_df)
        
        print("\ncount decending:")
        print_without_index(sorted_by_count)
        
    print('-'*75)

def show_raw_data(df):
    '''Display top 5 rows of filtered dataframe (raw data)'''
    
    print("5) Raw data\n")
    
    print(df.head())
    
    print('-'*75)
    


def main():
    full_start = True
    while True:
        
    # only used if program is started for the first time or restarted
        if full_start:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            check_null_columns(df, city)
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
        
        print_drill_down_menu(city)
        
        try:
            menu = int(input('\nPlease select from the menu for data excerpts or to restart or end the program.\n')) 
            
    # the program is ended with 7 and restarted with 6
            if (menu !=7):
                if menu == 1:
                    show_start_time_data(df)
                    full_start = False
                elif menu == 2:
                    show_stations_data(df)
                    full_start = False
                elif menu == 3:
                    show_duration_data(df)
                    full_start = False
                elif menu == 4:
                    show_user_age_data(df)
                    full_start = False
                elif menu == 5:
                    show_raw_data(df)
                    full_start = False
                elif (menu <= 0 or menu > 7):
                    raise ValueError
                else:
                    full_start = True
            else:
                print('Thank you for exploring US bikeshare data!')
                break
        except ValueError:
                print("\nPlease enter a number from the menu.")
                full_start = False
        

if __name__ == "__main__":
    main()
