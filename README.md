
# Weather forecast basic app

This is the weather forecasting app for USA. This app allows you to enter Latitude and Longitude of a place inside USA and it will give the weather detail for that respective latitude and longitude

# App components detail

This app has 2 components

### Component 1

First Component name is "Single location" which allows user to search the weather forecast information detail just by entering the correct Latitude and Longitude of the location

### Component 2

Second Component name is "List of locations" which allows user to first enter all the locations one by one into the pandas dataframe using the Streamlit UI. Once you enter one Latitude and Longitude value press "Add location to system" button on the UI to update the entered location into app Dataframe.
If you have entered all the latitude and longitude press "Done inserting" button on the Streamlit UI. By pressing "Done inserting" you will see all the list of values entered by you on the UI.
After that enter the Latitude and Longitude for which you want to get the forecast(Make sure entered Latitude and Longitude is already inserted into system while adding location to system earlier). Now click on "Generate Forecast" button on the Streamlit UI


## Step to be followed to clone and configure the project

### Make Sure you have Anaconda installed in your system

Step 1

```bash
  git clone https://github.com/akash97715/weather_forecasting_app.git

```
Step 2 :- 
Naigate to the project path and go inside the project folder

Step 3 :- Download the required package from the requirements.txt by using below command

```bash
  pip install -r requirements.txt
```

Step 4 :- Now its time to run the app and see the forecast by using the below command

```bash
  streamlit run app.py
```
#### Component 1 Screenshot:-

[![single-location.png](https://i.postimg.cc/q7FvmWNc/single-location.png)](https://postimg.cc/R3cmhsQq)

#### Component 2 Screenshot:-

[![list-locations.png](https://i.postimg.cc/vHxpRB06/list-locations.png)](https://postimg.cc/YhkXYpKp)
[![list-location-2.png](https://i.postimg.cc/rwxGLX6J/list-location-2.png)](https://postimg.cc/DSf4qNwJ)

## App running screenshot on server

[![deplomenturl.png](https://i.postimg.cc/fRQ3hVf3/deplomenturl.png)](https://postimg.cc/bsLYxNM8)

## Forecast app screenshot (Final)

[![forecast-ss.png](https://i.postimg.cc/RZVVQwSz/forecast-ss.png)](https://postimg.cc/kBzm76Rj)


## FAQ

#### Shall we run this app using Docker?

Yes, to run this app using docker we need a dockerfile. To request for dockerfile please contact akash97715@gmail.com


#### Shall we take this app and run in production?

Yes, If the user base is very small. If the userbasr is large and global we need to be following the best deployment practices and also we need to take care of Non-performace and server test.



## Feedback

If you have any feedback, please reach out to me akash97715@gmail.com


