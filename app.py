import numpy as np
import pandas as pd
import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''


'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''


pickup_date = st.date_input(
    "Pickup date?",
    datetime.date(2019, 7, 6))
st.write('Pickup date:', pickup_date)

pickup_time = st.time_input('Pickup time?', datetime.time(8, 45))
st.write('Pickup time:', pickup_time)

pickup_longitude = st.number_input('Pickup longitude?', -73.950655)
st.write('Pickup longitude: ', pickup_longitude)
pickup_latitude = st.number_input('Pickup latitude?', 40.783282)
st.write('Pickup latitude: ', pickup_latitude)

dropoff_longitude = st.number_input('Dropoff longitude?', -73.984365)
st.write('Dropoff longitude: ', dropoff_longitude)
dropoff_latitude = st.number_input('Dropoff latitude?', 40.769802)
st.write('Dropoff latitude: ', dropoff_latitude)

passenger_count = st.number_input('How many passengers?', 1)
st.write('Number of passengers: ', passenger_count)


url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

pickup_datetime = datetime.datetime.combine(pickup_date, pickup_time)

X_pred = dict(
    pickup_datetime=[pickup_datetime],
    pickup_longitude=[pickup_longitude],
    pickup_latitude=[pickup_latitude],
    dropoff_longitude=[dropoff_longitude],
    dropoff_latitude=[dropoff_latitude],
    passenger_count=[int(passenger_count)],
)

if st.button('Book it!'):
    # print is visible in the server output, not in the page
    print('button clicked!')

    X_res = requests.get(url, params=X_pred)
    print(round(X_res.json()['fare'], 2))
    st.write("Your fare will be: $"+str(round(X_res.json()['fare'], 2)))
