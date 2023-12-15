import requests
from datetime import datetime, timedelta
from config import togglAPIkey
import pandas

def toggl_entries_to_dataframe(toggl_entries):
    """
    Converts a list of Toggl time entries into a Pandas DataFrame.

    Parameters:
    toggl_entries (list): A list of dictionaries, where each dictionary represents a Toggl time entry.

    Returns:
    DataFrame: A Pandas DataFrame with each time entry as a row.
    """
    # Create a DataFrame from the list of time entries
    df = pandas.DataFrame(toggl_entries)

    # Optionally, you can convert timestamps to datetime objects, and perform other transformations
    # For example, converting the 'start' and 'stop' fields from string to datetime
    df['start'] = pandas.to_datetime(df['start'])
    df['stop'] = pandas.to_datetime(df['stop'])

    # You can add more transformations here as needed

    return df
def get_entries():
    # Replace 'your_api_token' with your actual Toggl API token
    api_token = togglAPIkey

    # Toggl API URL for time entries
    url = 'https://api.track.toggl.com/api/v8/time_entries'

    # Use HTTP Basic Authentication
    auth = (api_token, 'api_token')

    # Set the date range for the time entries you want to fetch
    start_date = datetime.now() - timedelta(days=7)  # last 7 days
    end_date = datetime.now()

    # Convert dates to ISO format
    params = {
        'start_date': start_date.isoformat() + 'Z',
        'end_date': end_date.isoformat() + 'Z'
    }

    # Make the request
    response = requests.get(url, auth=auth, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        time_entries = response.json()
        time_entries_df = toggl_entries_to_dataframe(time_entries)
        return time_entries_df
    else:
        print(f"Failed to fetch time entries: {response.status_code}")

test = get_entries()
x = 1