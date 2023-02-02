#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Import the csv file for Fitbase data

daily_activity = pd.read_csv("C:/Courses/Data_Analytics/Case_Study/CaseStudy-2/Fitabase Data 4.12.16-5.12.16/working_database/dailyActivity_merged.csv",parse_dates = True)

hourly_calories = pd.read_csv("C:/Courses/Data_Analytics/Case_Study/CaseStudy-2/Fitabase Data 4.12.16-5.12.16/working_database/hourlyCalories_merged.csv",parse_dates = True)

hourly_steps = pd.read_csv("C:/Courses/Data_Analytics/Case_Study/CaseStudy-2/Fitabase Data 4.12.16-5.12.16/working_database/hourlySteps_merged.csv",parse_dates = True)

sleep_day = pd.read_csv("C:/Courses/Data_Analytics/Case_Study/CaseStudy-2/Fitabase Data 4.12.16-5.12.16/working_database/sleepDay_merged.csv",parse_dates = True)

weight_log = pd.read_csv("C:/Courses/Data_Analytics/Case_Study/CaseStudy-2/Fitabase Data 4.12.16-5.12.16/working_database/weightLogInfo_merged.csv",parse_dates = True)


# In[3]:


#Data Exploration

#Getting an overview of the data


# In[4]:


daily_activity.head()


# In[5]:


hourly_calories.head()


# In[6]:


hourly_steps.head()


# In[7]:


sleep_day.head()


# In[8]:


weight_log.head()


# In[9]:


#Checking the info in each dataset


# In[10]:


daily_activity.info()


# In[11]:


hourly_calories.info()


# In[12]:


hourly_steps.info()


# In[13]:


sleep_day.info()


# In[14]:


weight_log.info()


# In[15]:


#Summary Statistics


# In[16]:


daily_activity.Id.nunique()


# In[17]:


hourly_calories.Id.nunique()


# In[18]:


hourly_steps.Id.nunique()


# In[19]:


sleep_day.Id.nunique()


# In[20]:


weight_log.Id.nunique()


# In[21]:


#cleaning the data


# In[22]:


#checking for empty cells


# In[23]:


daily_activity.isna().sum()


# In[24]:


hourly_calories.isna().sum()


# In[25]:


hourly_steps.isna().sum()


# In[26]:


sleep_day.isna().sum()


# In[27]:


weight_log.isna().sum()


# In[28]:


#checking for duplicate


# In[29]:


daily_activity.duplicated().sum()


# In[30]:


hourly_calories.duplicated().sum()


# In[31]:


hourly_steps.duplicated().sum()


# In[32]:


sleep_day.duplicated().sum()


# In[33]:


sleep_day.drop_duplicates(inplace = True)


# In[34]:


sleep_day


# In[35]:


weight_log.duplicated().sum()


# In[36]:


#Data Transformation


# In[37]:


#renaming the column

daily_activity = daily_activity.rename(columns = {'ActivityDate' : 'Date'})


# In[38]:


hourly_calories = hourly_calories.rename(columns = {'ActivityHour' : 'Time'})


# In[39]:


hourly_steps = hourly_steps.rename(columns = {'ActivityHour' : 'Time'})


# In[40]:


sleep_day = sleep_day.rename(columns = {'SleepDay' : 'Date'})


# In[41]:


#changing the data type 


# In[42]:


daily_activity['Date'] = pd.to_datetime(daily_activity['Date'])

hourly_calories['Time'] = pd.to_datetime(hourly_calories['Time'])

hourly_steps['Time'] = pd.to_datetime(hourly_steps['Time'])

sleep_day['Date'] = pd.to_datetime(sleep_day['Date'])


# In[43]:


#Creating a day of the week column


# In[44]:


daily_activity['day_of_week'] = daily_activity['Date'].dt.day_name()

sleep_day['day_of_week'] = sleep_day['Date'].dt.day_name()


# In[45]:


sns.set_style('darkgrid')


# In[46]:


# Different categories of Total Steps and Calories

daily_activity.agg(
                   {'TotalSteps' : ['min','max','mean'],
                    'Calories'   : ['min','max','mean']
                   }
)


# In[47]:


# Relationship between the total number of steps and calories

sns.scatterplot (data=daily_activity,
                x = 'TotalSteps',
                y = 'Calories',
                alpha = 0.8,
             )
plt.xlabel('Total Steps',size = 10)
plt.xlabel('Total Calories',size = 10)
plt.show()


# In[48]:


# Average of Total Steps by Day of the Week

daily_activity.groupby(daily_activity["day_of_week"])[["TotalSteps"]].mean()


# In[49]:


plot_1 = daily_activity.groupby(daily_activity["day_of_week"],as_index = False).mean()

sns.barplot(data = plot_1,
            x = 'day_of_week',
            y = 'TotalSteps',
           )
plt.xlabel('Weekdays',size = 10)
plt.ylabel('Total Steps',size = 10)
plt.xticks(rotation = 30)
plt.show()


# In[50]:


# Average of Total Steps by hour of the day 
hourly_steps.groupby(hourly_steps["Time"].dt.hour)[["StepTotal"]].mean()


# In[51]:


hourly_steps['hour'] = hourly_steps['Time'].dt.hour
plot_2 = hourly_steps.groupby(hourly_steps["hour"],as_index = False).mean()

sns.barplot (data = plot_2,
             x = 'hour',
             y = 'StepTotal')
plt.xlabel('hour of the day',size = 10)
plt.ylabel('Total Steps',size = 10)
plt.show()


# In[52]:


# Average of Total Calories by hour of the day

hourly_calories.groupby(hourly_calories["Time"].dt.hour)[["Calories"]].mean()


# In[53]:


hourly_calories['hour'] = hourly_calories["Time"].dt.hour
plot_3 = hourly_calories.groupby(hourly_calories["hour"],as_index = False).mean()

sns.barplot(data = plot_3,
            x = 'hour',
            y = 'Calories')
plt.xlabel('hour of the day',size = 10)
plt.ylabel('Calories',size = 10)
plt.show()


# In[54]:


# Average of Total Tracker Distance by Day of the Week

daily_activity.groupby(daily_activity["day_of_week"])[["TrackerDistance"]].mean()


# In[55]:


plot_4 = daily_activity.groupby(daily_activity["day_of_week"],as_index = False).mean()

sns.barplot(data = plot_4,
            x = 'day_of_week',
            y = 'TrackerDistance')
plt.xlabel('Weekdays',size = 10)
plt.ylabel('Total Distance in km',size = 10)
plt.show()


# In[56]:


# Different categories of Activities

daily_activity.agg({'SedentaryMinutes': ['min','max','mean'] ,
                    'LightlyActiveMinutes' : ['min','max','mean'],
                    'FairlyActiveMinutes' : ['min','max','mean'],
                    'VeryActiveMinutes' : ['min','max','mean']
                   }
)


# In[57]:


plot_5 = daily_activity.agg({'SedentaryMinutes': 'mean' ,
                    'LightlyActiveMinutes' : 'mean',
                    'FairlyActiveMinutes' : 'mean',
                    'VeryActiveMinutes' : 'mean'
                   }
)
keys = ['SedentaryMinutes','LightlyActiveMinutes','FairlyActiveMinutes','VeryActiveMinutes']
explode = [0.1, 0.0, 0.0 ,0.0]

plt.pie(plot_5 , labels = keys, autopct='%.0f%%',explode = explode )
plt.show()


# In[58]:


# Average minutes of activities in a weekday

daily_activity.groupby(daily_activity["day_of_week"])[['SedentaryMinutes','LightlyActiveMinutes','FairlyActiveMinutes','VeryActiveMinutes']].mean()


# In[59]:


weekday = daily_activity.groupby(daily_activity['day_of_week']).mean()
Activities = weekday[['SedentaryMinutes','LightlyActiveMinutes','FairlyActiveMinutes','VeryActiveMinutes']]
Activities.plot.bar(xlabel = 'weekdays',ylabel = 'Average Active Minutes',rot=0, figsize=(8,5))


# In[60]:


# Average different minutes of sleep time 

sleep_day.agg({ 'TotalTimeInBed' : ['min','max','mean'] ,
                'TotalMinutesAsleep' : ['min','max','mean']
              }
)


# In[61]:


# Relationship between the TotalTimeInBed and TotalMinutesAsleep

plot_10 = sns.scatterplot(data =sleep_day, x = 'TotalTimeInBed', y ='TotalMinutesAsleep',alpha = 0.7)
plt.show()


# In[62]:


# Average different categories of minutes by day of week
sleep_day['AwakeTimeInBed'] = sleep_day['TotalTimeInBed'] - sleep_day['TotalMinutesAsleep']

sleep_day.groupby(['day_of_week'])[['TotalTimeInBed','TotalMinutesAsleep','AwakeTimeInBed']].mean()


# In[63]:


# Average categories of sleep percentage

plot_11 = sleep_day.agg({'TotalTimeInBed': 'mean' ,
                    'TotalMinutesAsleep' : 'mean',
                    'AwakeTimeInBed' : 'mean'
                   }
)

keys = ['TotalTimeInBed','TotalMinutesAsleep','AwakeTimeInBed']

plt.pie(plot_11, labels = keys,autopct='%.0f%%')
plt.show()


# In[64]:


# Average of minutes

weekday = sleep_day.groupby(sleep_day["day_of_week"]).mean()
time_bed = weekday[['TotalMinutesAsleep','TotalTimeInBed','AwakeTimeInBed']]

time_bed.plot.bar(xlabel='Day of the Week', ylabel='Average of Minutes', rot=0, figsize=(8,5))
plt.show()

