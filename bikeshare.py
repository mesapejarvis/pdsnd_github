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
    cities = ['chicago', 'new york city', 'washington' ]
    
    while True:
        city = input('Enter name of city  you would like to explore. chicago, new york city, or washington? ').lower()
        if city in cities:
            break
        else:
            print('That is not a valid city, please enter one of the three cities.')
    


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input('Enter the month you would like to explore or all: ').lower()
        if month in months:
            break
        else: print('Sorry, that is not a valid entry.')



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input('Enter the day of the week you would like to explore or all: ').lower()
        if day in days:
            break
        else: print('Sorry, that is not a valid entry.')


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
    
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].value_counts().idxmax()
    print( "The most common month of travel is : {}".format(month))


    # TO DO: display the most common day of week
    day = df['day'].value_counts().idxmax()
    print("The most common day of the week is : {}".format(day))


    # TO DO: display the most common start hour
    hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is : {}".format(hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print( "The most commonly used start station is : {}".format(start_station))


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print( "The most commonly used end station is : {}".format(end_station))



    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination =  start_station + ' to ' +  end_station
    frequent_combination_back =  start_station + ' and back to ' +  end_station

    if start_station == end_station :
        print( "The most frequent combination of start station and end station trip is taken from : {}".format(frequent_combination_back))
    else :
        print( "The most frequent combination of start station and end station trip is taken from : {}".format(frequent_combination))
        


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print( "The total travel time is : {} seconds".format(total_travel_time))

    


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print( "The mean travel time is : {} seconds".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print( "The user types count is : \n {}".format(user_type_count))
   

    gender = "Gender"
    birth = "Birth Year"
    # TO DO: Display counts of gender
    
    if gender in df.columns and birth in df.columns:
            
        gender_count = df['Gender'].value_counts()
        print( "The gender count is : \n {}".format(gender_count))


        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]

        print( "The earliest year of birth is : {:.0f}".format(earliest_year))
        print( "The recent year of birth is : {:.0f}".format(most_recent_year))


        
    else :   
        print("The summary stats (Gender and Birth Year) are not avalibale for this city!!!")

    



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# added this section as per previous feedback!    
def display_data(df):    
    count = 0
    user_input = input('\nDo you want to see 5 lines of raw data? Enter yes or no.\n').lower() 
    while True :
        if user_input == 'yes':
            print(df.iloc[count : count + 5])
            count += 5
            user_input = input('\nDo you want to see more raw data? Enter yes or no.\n')
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
