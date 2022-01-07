# References:
# https://docs.python.org/3.6/library/index.html
# https://docs.python.org/3/tutorial/controlflow.html
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago', 'new york city', 'washington']
        city= input("\n Would you like to see data for Chicago, New York City or Washington? \n").lower()
        if city in cities:
            break
        else:
            print("\n please enter a valid city name")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months= ['all','january','february','march','april','may','june']
        month = input("\n Which month would you like to see data for? (January, February, March, April, May, June or type 'all' if you do not have any preference)\n").lower()
        if month in months:
            break
        else:
            print("\n Please enter a valid month") 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days= ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = input("\n Which day of the week would you like to see data for? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type 'all' if you do not have any preference)\n").lower()         
        if day in days:
            break
        else:
            print("\n Please enter a valid day") 

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is:" ,common_month)
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day is:" ,common_day)
        
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:' ,common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:' ,common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+" "+"to"+" "+ df['End Station']
    common_combination = df['combination'].mode()[0]
    print('The most frequent combination of start and end station is:' ,common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:' ,total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=round(df['Trip Duration'].mean())
    print('The mean travel time is:' ,mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The count of user types is:\n',user_types)

     # Display counts of gender
    if 'Gender' not in df:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    else:
        print('The count of gender types is:\n',df['Gender'].value_counts())
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')
    else:
        print('The oldest user is born in the year:',int(df['Birth Year'].min()))
        print('The youngest user is born in the year:',int(df['Birth Year'].max()))
        print('Most users are born in the year:',int(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
    Ask user wheteher he/she wants to see 5 rows of data.
    Displays data based on location.
    """
    view_data = input('\Would you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    keep_asking = True
    while (keep_asking):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input('Do you wish to continue?: ').lower()               
        if view_display.lower() == 'no':
           keep_asking = False

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
