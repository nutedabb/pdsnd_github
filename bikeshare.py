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

    while True:    
        print('Hello! Let\'s explore some US bikeshare data right now!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input('Enter the name of the City (chicago, new york city, washington) : ')

    # TO DO: get user input for month (all, january, february, ... , june)
        month = input('Enter month january to june : ')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Enter day of the week : ')
    
        print('-'*40)
        print('Your filters are :',city,month,day )
        gett = input("Are you interested in changing the filters?, Type yes to change:")
        if gett == 'yes':
            continue
        else:
            break
    return city, month, day



def load_data(city, month, day):
    try:
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
        #creating the month column
        df['months'] = df['Start Time'].dt.month
        #creating the day of th week column
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        #Applying the filter for month
        months = ['january','february','march','april','may','june','july']
        month = months.index(month) + 1
        df= df[df['months'] == month]
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day_of_week'] == day.title()]

            return df
    except:
        print('Check the data inputed is as shown in the prompt')
        
        

def show_data(df):
    # this function shows a certain amount of table
    showmore = 'yes'
    dont = 'no'
    y = 5
    try:
        lines = input('Do you want to see 5 lines of raw data, yes or no')
        
        while True:
            
            lines = lines.lower()
            if lines =='yes':
                
                hh =df.head(y)
            
                print(hh)
            x = input("\n show more lines? type : yes or no ::")
            if x.lower() == showmore:
                y = y + 5
                
                
               
                
            else:
                 x.lower() == dont
                 break
                
    except: 
        print('----please follow the prompt------')
   
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    try:
        # TO DO: display the most common month
        most_month = df['months'].mode()[0]
        print('The most common month is:  ',most_month)

        # TO DO: display the most common day of week
        most_day = df['day_of_week'].mode()[0]
        print('The most common day is:  ',most_day)

        # TO DO: display the most common start hour
        df['most_hour'] = df['Start Time'].dt.hour
        most_hour = df['most_hour'].mode()[0]
        print('The most common start hour is:  ',most_hour)
        
        

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print('Check the data inputed is as shown in the prompt')
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    try:
        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()
        print
        # TO DO: display most commonly used start station
        newdf = df
        newdf = newdf.groupby('Start Station')['Start Station'].count().to_frame('times').reset_index()
        maxy = newdf['times'].max()
    
        most = newdf.loc[newdf['times'] == maxy, 'Start Station'].iloc[0]
        print('The most commonly used start station :',most)
       
    
    
        # TO DO: display most commonly used end station
        newdf1 = df
        newdf1 = newdf1.groupby('End Station')['End Station'].count().to_frame('times').reset_index()
        maxyy = newdf1['times'].max()

    
        mostt = newdf1.loc[newdf1['times'] == maxyy, 'End Station'].iloc[0]
        print('The most commonly used End  station :',mostt)

        # TO DO: display most frequent combination of start station and end station trip
        neww = df 
    
        neww1 = neww.groupby(['Start Station','End Station']).size().idxmax()
        print('Most frequent combination of start station and end station trip is :',neww1)
        print 
    
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print('Check the data inputed is as shown in the prompt')

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    try:
        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # TO DO: display total travel time
        tdf = df
        tdf['End Time'] = pd.to_datetime(tdf['End Time'])
    
        tdf['travel time'] =  tdf['End Time'] - tdf['Start Time']
    
        sumtdf = tdf.loc[:,'travel time'].sum()
        print('Total travel time :',sumtdf)

        # TO DO: display mean travel time
        tdf = df
        tdf['End Time'] = pd.to_datetime(tdf['End Time'])
    
        tdf['travel time'] =  tdf['End Time'] - tdf['Start Time']
    
        meantdf = tdf.loc[:,'travel time'].mean()
        print('Mean travel time :',meantdf)


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print('Check the data inputed is as shown in the prompt')

def user_stats(df):
    """Displays statistics on bikeshare users."""
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        User_types = df['User Type'].value_counts()
        print('User types are :\n', User_types)
    
    
     

        # TO DO: Display counts of gender
        Gender = df['Gender'].value_counts()
        print('Counts of Gender  are ____\n', Gender)
        print('\n')
    

        # TO DO: Display earliest, most recent, and most common year of birth
        Earliest = df.loc[:,'Birth Year'].min()
        print('Earliest Birth Year :',Earliest)
        print('\n')
        Mostr = df.loc[:,'Birth Year'].max()
        print('Most recent Birth Year :',Mostr)
        print('\n')
    
        Mostc = df.loc[:,'Birth Year'].mode().iloc[0]
        print('Most Common Birth Year :', Mostc)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except:
        print('Check the data inputed is as shown in the prompt')

def main():
    while True:
        try:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            print('\n')
            show_data(df)
            station_stats(df)
            print('\n')
            trip_duration_stats(df)
            print('\n')
            user_stats(df)
            
        except:
            print('Type the prompt correctly please')
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
