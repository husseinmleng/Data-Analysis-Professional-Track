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
    city = ''
    while city not in CITY_DATA.keys():
        print("\nWhich city you want to explore ?")
        print("\n 1.Chicgo 2.New York 3.Washington")
        city = input().lower()
        if city not in CITY_DATA.keys():
            print("\nplease enter a valid city")
    print(f"\nYou have choosen {city.title()} as your city")
    # TO DO: get user input for month (all, january, february, ... , june)
    month_data = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in month_data.keys():
        print("\nPlease enter a month between January to june ")
        print("\nType all or All or ALL if you want all months ")
        month = input().lower()
        if month not in month_data.keys():
            print("Please enter a valid month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in day_list :
        print("Please Enter the day of the weak you want to explore\n")
        print("Enter all or All or ALL if you want all days\n")
        day = input().lower()
        if day not in day_list:
            print("please enter a valid day\n")

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
        df - pandas DataFrame containing city data filtered by month and day
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
        df = df[df['day_of_week']==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(f"Most Popular Month : {popular_month}\n")

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f"Most Popular Day : {popular_day}\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"Most Popular hour : {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f"Most Commonly Station is : {popular_start_station}\n")

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"Most Commonly Ens Station is : {popular_end_station}\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start to End'] = df['Start Station'].str.cat(df['End Station'], sep = ' to ') 
    comb = df['Start to End'].mode()[0]
    print(f"Most frequent Combination of trip is : {comb}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    # find the total duration time in  mintues and seconds
    minute, second = divmod(total_duration,60)
    #find the total duration time in  hours and mintues
    hour, minute = divmod(minute,60)
    print(f"The total trip is {hour} hours, {minute} mintues and {second} seconds.")
    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    mintue , second = divmod(average_duration,60)
    if minute > 60:
        hour, mintue = divmod(minute,60)
        print(f"\nThe average duration is {hour} hours, {minute} mintues and {second}")
    else:
        print(f"\nThe average Duration is {minute} mintues and {second} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print(f"The types of users ar : {user_type}")

    # TO DO: Display counts of gender
    try:
        gender = df["Gender"].value_counts()
        print(f"\nThe types of users gender are : {gender}")
    except:
        print("\nThere is no Gender column in this file")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}")
        print(f"\n\nThe most recent year of birth: {recent}")
        print(f"\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data? Yes or No")
        rdata = input().lower()
        #the raw data from the df is displayed if user opts for it
        if rdata == "yes":
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while rdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

    print('-'*80)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
