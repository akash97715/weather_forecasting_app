from logging import exception
import streamlit as st
import pandas as pd
import requests
import re
from datetime import datetime
#select module
st.title("USA Weather forecating app", anchor=None)
uploaded_file = st.sidebar.selectbox(" ", ["Single location","List of locations"])
if uploaded_file=='Single location':
    try:
        latitude = st.text_input("Enter Latitude with direction","38.2527° N")
        longitude = st.text_input("Enter Longitude with direction","85.7585° W")
        if st.button("Click me for forecast"):
            def lat_builder(obj):
                g=obj
                if g[-1]=='S':
                    g=-float(g[:-3])
                else:
                    g=float(g[:-3])
                return g
            def lon_builder(obj):
                try:
                    g=obj
                    if g[-1]=='W':
                        g=-float(g[:-3])
                    else:
                        g=float(g[:-3])
                except ValueError:
                    st.write("please enter correct Longitude with direction")
                return g
            pre=lat_builder(latitude)
            pre1=lon_builder(longitude)
            url =f"https://api.weather.gov/points/{pre},{pre1}"
            response1 = requests.get(url)
            full_data = response1.json()
            response2 = requests.get(full_data['properties']['forecast'])
            full_data2 = response2.json()
            check=False
            try:
                temp=next(item for item in full_data2['properties']['periods'] if item["name"] == "Wednesday Night")
                check=True
            except StopIteration:
                st.write("Today is Wednesday")
            if check==False:
                try:
                    temp=next(item for item in full_data2['properties']['periods'] if item["name"] == "Overnight")
                    check=True
                except StopIteration:
                    st.write("Wait!!")
            if check==False:
                try:
                    temp=next(item for item in full_data2['properties']['periods'] if item["name"] == "Tonight")
                except StopIteration:
                    st.write("Please contact to app devloper akash97715@gmail.com immediately")
            dfr=temp['startTime']
            res=dfr.split("T")[0]
            date_time_obj = datetime.strptime(res, '%Y-%m-%d')
            showof=date_time_obj.strftime("%b,%d %Y")   
            dfshow=temp['name']+"("+str(showof)+")"
            st.header(dfshow, anchor=None)
            image=temp['icon']
            st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
            no6=temp['windDirection']
            if no6=='E'or no6=='EW'or no6=='EN'or no6=='ES':
                no6='East specific'
            if no6=='W'or no6=='WS'or no6=='WE'or no6=='WN':
                no6='West specific'
            if no6=='N'or no6=='NS'or no6=='NE'or no6=='NW':
                no6='North specific'
            if no6=='S'or no6=='SE'or no6=='SW'or no6=='SN':
                no6='South specific'
            col1, col2, col3 = st.columns(3)
            col1.metric(label="Temperature", value=str(temp['temperature'])+" °"+temp['temperatureUnit'])
            col2.metric("Wind speed", temp['windSpeed'])
            col3.metric("Wind direction", no6)
            no2=temp['shortForecast']
            new_title1 = f'Short Forecast :- '
            no3=re.sub('\s+','',no2).lower()
            if no3.find("clear")!=-1:
                st.markdown(f"### {new_title1+no2}🌞!!")
            if no3.find("rain")!=-1:
                st.write(f"### {new_title1+no2}☔!!")
            if no3.find("fog")!=-1:
                st.write(f"### {new_title1+no2}🌁!!")
            if no3.find("storm")!=-1:
                st.write(f"### {new_title1+no2}⛈️!!")
            if no3.find("snow")!=-1:
                st.write(f"### {new_title1+no2}T❄️!!")
            if no3.find("cloud")!=-1:
                st.write(f"### {new_title1+no2}⛅")
            no9=temp['detailedForecast']
            original_title = f'Detailed Forecast :- '
            new_title = f'### {original_title+no9}'
            st.markdown(new_title, unsafe_allow_html=True)
    except Exception as e:
        st.write("Please enter correct Latitude and longitude value for USA, For detail refer Google Map")
elif uploaded_file=='List of locations':
    @st.cache(allow_output_mutation=True)
    def get_data():
        return []
    latitude = st.text_input("Enter Latitude with direction","38.2527° N")
    longitude = st.text_input("Enter Longitude with direction","85.7585° W")
    if st.button("Add Location to the system"):
        get_data().append({"Latitude": latitude, "Longitude": longitude})
    submit = st.button('Done Inserting')
    try:
        if submit:
            g1=pd.DataFrame(get_data())
            lenc=len(g1)
            #st.write(f"There are {lenc} Location Records in the System")
            st.write(g1.head(lenc))
        reqt = st.text_input("Enter Latitude to be searched ","38.2527° N")
        reqt1 = st.text_input("Enter Longitude to be searched ","85.7585° W")
        submit1 = st.button('Generate Forecast')
        if submit1:
            g1=pd.DataFrame(get_data())
            for index, row in g1.iterrows():
                
                if row['Latitude']==reqt and row['Longitude']==reqt1:
                    print(row)
                    latitude = reqt
                    longitude = reqt1
                    def lat_builder(obj):
                        g=obj
                        if g[-1]=='S':
                            g=-float(g[:-3])
                        else:
                            g=float(g[:-3])
                        return g
                    def lon_builder(obj):
                        try:
                            g=obj
                            if g[-1]=='W':
                                g=-float(g[:-3])
                            else:
                                g=float(g[:-3])
                        except ValueError:
                            st.write("please enter correct Longitude with direction")
                        return g
                    pre=lat_builder(latitude)
                    pre1=lon_builder(longitude)
                    url =f"https://api.weather.gov/points/{pre},{pre1}"
                    response1 = requests.get(url)
                    full_data = response1.json()
                    response2 = requests.get(full_data['properties']['forecast'])
                    full_data2 = response2.json()
                    check=False
                    try:
                        temp1=next(item for item in full_data2['properties']['periods'] if item["name"] == "Wednesday Night")
                        check=True
                    except StopIteration:
                        st.write("Today is Wednesday")
                    if check==False:
                        try:
                            temp1=next(item for item in full_data2['properties']['periods'] if item["name"] == "Overnight")
                            check=True
                        except StopIteration:
                            st.write("Wait!!")
                    if check==False:
                        try:
                            temp1=next(item for item in full_data2['properties']['periods'] if item["name"] == "Tonight")
                        except StopIteration:
                            st.write("Please contact to app devloper akash97715@gmail.com immediately")
                            st.stop()
                    dfr=temp1['startTime']
                    res=dfr.split("T")[0]
                    date_time_obj = datetime.strptime(res, '%Y-%m-%d')
                    showof=date_time_obj.strftime("%b,%d %Y")   
                    dfshow=temp1['name']+"("+str(showof)+")"
                    st.header(dfshow, anchor=None)
                    image=temp1['icon']
                    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    no6=temp1['windDirection']
                    if no6=='E'or no6=='EW'or no6=='EN'or no6=='ES':
                        no6='East specific'
                    if no6=='W'or no6=='WS'or no6=='WE'or no6=='WN':
                        no6='West specific'
                    if no6=='N'or no6=='NS'or no6=='NE'or no6=='NW':
                        no6='North specific'
                    if no6=='S'or no6=='SE'or no6=='SW'or no6=='SN':
                        no6='South specific'
                    col1, col2, col3 = st.columns(3)
                    col1.metric(label="Temperature", value=str(temp1['temperature'])+" °"+temp1['temperatureUnit'])
                    col2.metric("Wind speed", temp1['windSpeed'])
                    col3.metric("Wind direction", no6)
                    no2=temp1['shortForecast']
                    new_title1 = f'Short Forecast :- '
                    no3=re.sub('\s+','',no2).lower()
                    if no3.find("clear")!=-1:
                        st.markdown(f"### {new_title1+no2}🌞!!")
                    if no3.find("rain")!=-1:
                        st.write(f"### {new_title1+no2}☔!!")
                    if no3.find("fog")!=-1:
                        st.write(f"### {new_title1+no2}🌁!!")
                    if no3.find("storm")!=-1:
                        st.write(f"### {new_title1+no2}⛈️!!")
                    if no3.find("snow")!=-1:
                        st.write(f"### {new_title1+no2}T❄️!!")
                    if no3.find("cloud")!=-1:
                        st.write(f"### {new_title1+no2}⛅")
                    no9=temp1['detailedForecast']
                    original_title = f'Detailed Forecast :- '
                    new_title = f'### {original_title+no9}'
                    st.markdown(new_title, unsafe_allow_html=True)
                    break
            st.write("Please make sure you enter the Latitude and Longitude that already Insterted in the System")

    except Exception as e:
        st.write("Please enter correct Latitude and longitude value for USA, For detail refer Google Map") 

        