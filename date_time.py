# Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import date, datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day, month, year, minute,hour, timestamp)
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
t = now.strftime("%m/%d/%Y, %H:%M:%S")
t1 = now.strftime("%A, %d/%b/%Y, Month of %B..")
print(t)
print(t1)
# Today is 5 December, 2019. Change this time string to time.
string_to_change = "Today is 5 December, 2019."
date_part = string_to_change.replace("Today is ", "").strip().replace(".", "")

t2 = datetime.strptime(date_part, "%d %B, %Y")
print(t2)
# Calculate the time difference between now and new year.
today = date(year = 2025, month=7, day=24)
new_year = date(year=2026, month=1, day=1)
time_to_new_year = new_year - today
print(f"Time to the new year {time_to_new_year}")
#Calculate the time difference between 1 January 1970 and now
today = date(year = 2025, month=7, day=24)
timestamp = date(1970,1,1)
t3 = (timestamp - today).total_seconds()
print(t3)
"""
    Think, what can you use the datetime module for? Examples:
    > Time series analysis
    Getting the difference betwwen some datagetting the now date
    and the las date
    > To get a timestamp of any activities in an application
    Getting the date of the user usage of the app
    > Adding posts on a blog
    Getting the date of the publishing 

"""
"""
The `datetime` module in Python is a powerful tool for working with dates and times.

Here are some common use cases:

1. Time Series Analysis:
   > Analyze trends over time by working with date-based data.
   > Example: Calculate the difference between two dates to find the number of days, weeks, or months.
   > Example: Filter records from a database that fall within a specific date range.

2. Logging and Timestamps:
   > Automatically add timestamps to user activity or events in an application.
   > Example: Store the exact time a user logs in or performs a specific action.

3. Blog or Content Management Systems:
   > Track when a blog post or article was published.
   > Example: Sort posts by publish date or show "published X days ago".

4. Scheduling and Notifications:
   > Set up tasks to run at specific times or intervals.
   > Example: Send reminders 24 hours before an event.

5. Formatting and Display:
   > Convert datetime objects to human-readable formats.
   > Example: Show current date as "24 July, 2025" or "Thursday, 24/07/2025".

6. Timezone Handling:
   > Convert between different timezones (with the help of additional modules like `pytz` or `zoneinfo` in Python 3.9+).

7. Performance Monitoring:
   > Measure the execution time of operations.
   > Example: Capture start and end time, then compute the elapsed time.

In short, `datetime` is essential when your application or analysis involves **anything related to time**.
"""
