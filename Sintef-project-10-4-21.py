import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import rcParams
import streamlit as st
import datetime as dt
from datetime import timedelta
import plotly.express as px
# from PIL import Image
from datetime import date, time, datetime
# image3 = Image.open('sintef-logo-centered-negative.jpg')
# image1 = Image.open('enviotlogo.jpg')
col1, col2, col3 = st.beta_columns([1,3,1])
col1.subheader('EnvIot')
col3.subheader('SINTEF')
col2.title('SINTEF Sensor Data')
option2 = st.sidebar.radio("Plasma/NotPlasma", ('Plasma', 'NotPlasma'))
option = st.sidebar.selectbox("1St Plot", ('VOC', 'pid', 'TEMP', 'HUM', 'PM1_0', 'PM2_5', 'PM10', 'PM1_0E',
                                                   'PM2_5E', 'PM10E','P0_3', 'P0_5', 'P1_0', 'P2_5', 'P5_0', 'P10'))
option1 = st.sidebar.selectbox("2nd Plot", ('VOC', 'pid', 'TEMP', 'HUM', 'PM1_0', 'PM2_5', 'PM10', 'PM1_0E',
                                                   'PM2_5E', 'PM10E','P0_3', 'P0_5', 'P1_0', 'P2_5', 'P5_0', 'P10'))
# option = st.sidebar.checkbox("Which Dashboard?", ('VOC', 'pid', 'TEMP', 'HUM', 'PM1_0', 'PM2_5', 'PM10', 'PM1_0E',
#                                                    'PM2_5E', 'PM10E','P0_3', 'P0_5', 'P1_0', 'P2_5', 'P5_0', 'P10'))


#@st.cache
def parameters(file, time_now):
    st.write('Sensor Data on '+ str(time_now))
    t = []
    VOC, pid, TEMP, HUM, PM1_0, PM2_5, PM10, PM1_0E, PM2_5E, PM10E, P0_3, P0_5, P1_0, P2_5, P5_0, P10 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    for line in file:
        splitline = line.split(':')
        if splitline[0] == 'VOC':
            VOC.append(int(splitline[1]))
        elif splitline[0] == 'pid':
            pid.append(int(splitline[1]))
        elif splitline[0] == 'TEMP':
            TEMP.append(float(splitline[1]))
        elif splitline[0] == 'HUM':
            HUM.append(float(splitline[1]))
        elif splitline[0] == 'PM1.0':
            PM1_0.append(int(splitline[1]))
        elif splitline[0] == 'PM2.5':
            PM2_5.append(int(splitline[1]))
        elif splitline[0] == 'PM10':
            PM10.append(int(splitline[1]))
        elif splitline[0] == 'PM1.0_E':
            PM1_0E.append(int(splitline[1]))
        elif splitline[0] == 'PM2.5_E':
            PM2_5E.append(int(splitline[1]))
        elif splitline[0] == 'PM10_E':
            PM10E.append(int(splitline[1]))
        elif splitline[0] == 'P>0.3um_0.1L_air':
            P0_3.append(int(splitline[1]))
        elif splitline[0] == 'P>0.5um_0.1L_air':
            P0_5.append(int(splitline[1]))
        elif splitline[0] == 'P>1.0um_0.1L_air':
            P1_0.append(int(splitline[1]))
        elif splitline[0] == 'P>2.5um_0.1L_air':
            P2_5.append(int(splitline[1]))
        elif splitline[0] == 'P>5.0um_0.1L_air':
            P5_0.append(int(splitline[1]))
        elif splitline[0] == 'P>10.0um_0.1L_air':
            P10.append(int(splitline[1]))
            delta = timedelta(seconds=1)
            cur_time = time_now + delta
            t.append(cur_time)
            time_now = cur_time
    # MAKING THE DATA FRAME FROM SERIES OF ALL THE SENSOR PARAMETERS
    t = pd.Series(t)
    VOC = pd.Series(VOC)
    pid = pd.Series(pid)
    TEMP = pd.Series(TEMP)
    HUM = pd.Series(HUM)
    PM1_0 = pd.Series(PM1_0)
    PM2_5 = pd.Series(PM2_5)
    PM10 = pd.Series(PM10)
    PM1_0E = pd.Series(PM1_0E)
    PM2_5E = pd.Series(PM2_5E)
    PM10E = pd.Series(PM10E)
    # --
    P0_3 = pd.Series(P0_3)
    P0_5 = pd.Series(P0_5)
    P1_0 = pd.Series(P1_0)
    P2_5 = pd.Series(P2_5)
    P5_0 = pd.Series(P5_0)
    P10 = pd.Series(P10)

    df = pd.concat(
        [t, VOC, pid, TEMP, HUM, PM1_0, PM2_5, PM10, PM1_0E, PM2_5E, PM10E, P0_3, P0_5, P1_0, P2_5, P5_0, P10], axis=1)
    df.columns = ['t', 'VOC', 'pid', 'TEMP', 'HUM', 'PM1_0', 'PM2_5', 'PM10', 'PM1_0E', 'PM2_5E', 'PM10E',
                  'P0_3', 'P0_5', 'P1_0', 'P2_5', 'P5_0', 'P10']
    headers = ['t', 'VOC', 'pid', 'TEMP', 'HUM', 'PM1_0', 'PM2_5', 'PM10', 'PM1_0E', 'PM2_5E', 'PM10E',
               'P0_3', 'P0_5', 'P1_0', 'P2_5', 'P5_0', 'P10']
    dtypes = [dt.datetime, int, int, float, float, float, float, float, float, float, float, float, float, float,
              float, float, float]
    #df = df.set_index('t')
    ### WRITING THE SENSOR DATA INTO CSV FILE
    df.to_csv('D:/EnvIOT/Sensor for SINTEF/dataFile_notPlasma.csv', date_format='%H:%M:%S')
    # df = df.reindex(columns=['t', 'VOC', 'pid', 'TEMP', 'HUM', 'PM1_0', 'PM2_5', 'PM10', 'PM1_0E', 'PM2_5E', 'PM10E',
    #                          'P0_3', 'P0_5', 'P1_0', 'P2_5', 'P5_0', 'P10'])
    st.subheader('Sensor Paramaters')
    df['t'] = df["t"].dt.strftime('%H:%M:%S')
    if st.checkbox('Data Frame'):
        st.write(df)
    st.subheader('Data Frame description')
    if st.checkbox('Des'):
        st.write(df.describe())
    st.subheader('NaN Values in each parameter')
    if st.checkbox('Missing Data'):
        st.write(df.isna().sum())
    #df5=df[['t', 'VOC']]
    #st.write(df5)
    # all_columns = df.columns.to_list()
    # selected_columns = st.multiselect("option", all_columns)
#***********************
# PLOTTING THE SENSOR DATA   START
# ***********************
    if option == 'VOC' or option1 == 'VOC':
        #st.header(option)
        st.subheader('VOC graph')
        fig = px.line(df, x="t", y="VOC", title='VOC')
        st.plotly_chart(fig)
        #st.line_chart(df.VOC)
    if option == 'pid' or option1 == 'pid':
        st.subheader('pid graph')
        fig = px.line(df, x="t", y="pid", title='pid')
        st.plotly_chart(fig)
        #st.line_chart(df.pid)
    if option == 'TEMP' or option1 == 'TEMP':
        st.subheader('Temperature graph')
        fig = px.line(df, x="t", y="TEMP", title='Temperature')
        st.plotly_chart(fig)
        #st.line_chart(df.TEMP)
    if option == 'HUM' or option1 == 'HUM':
        st.subheader('Humidity graph')
        fig = px.line(df, x="t", y="HUM", title='Humidity')
        st.plotly_chart(fig)
        #st.line_chart(df.HUM)
    if option == 'PM1_0' or option1 == 'PM1_0':
        st.subheader('PM1_0 graph')
        fig = px.line(df, x="t", y="PM1_0", title='PM1_0')
        st.plotly_chart(fig)
    if option == 'PM2_5' or option1 == 'PM2_5':
        st.subheader('PM2_5 graph')
        fig = px.line(df, x="t", y="PM2_5", title='PM2_5')
        st.plotly_chart(fig)
    if option == 'PM10' or option1 == 'PM10':
        st.subheader('PM10 graph')
        fig = px.line(df, x="t", y="PM10", title='PM10')
        st.plotly_chart(fig)
    if option == 'PM1_0E' or option1 == 'PM1_0E':
        st.subheader('PM1_0E graph')
        fig = px.line(df, x="t", y="PM1_0E", title='PM1_0E')
        st.plotly_chart(fig)
    if option == 'PM2_5E' or option1 == 'PM2_5E':
        st.subheader('PM2_5E graph')
        fig = px.line(df, x="t", y="PM2_5E", title='PM2_5E')
        st.plotly_chart(fig)
    if option == 'PM10E' or option1 == 'PM10E':
        st.subheader('PM10E graph')
        fig = px.line(df, x="t", y="PM10E", title='PM10E')
        st.plotly_chart(fig)
    if option == 'P0_3' or option1 == 'P0_3':
        st.subheader('P0_3 graph')
        fig = px.line(df, x="t", y="P0_3", title='P0_3')
        st.plotly_chart(fig)
    if option == 'P0_5' or option1 == 'P0_5':
        st.subheader('P0_5 graph')
        fig = px.line(df, x="t", y="P0_5", title='P0_5')
        st.plotly_chart(fig)
    if option == 'P1_0' or option1 == 'P1_0':
        st.subheader('P1_0 graph')
        fig = px.line(df, x="t", y="P1_0", title='P1_0')
        st.plotly_chart(fig)
    if option == 'P2_5' or option1 == 'P2_5':
        st.subheader('P2_5 graph')
        fig = px.line(df, x="t", y="P2_5", title='P2_5')
        st.plotly_chart(fig)
    if option == 'P5_0' or option1 == 'P5_0':
        st.subheader('P5_0 graph')
        fig = px.line(df, x="t", y="P5_0", title='P5_0')
        st.plotly_chart(fig)
    if option == 'P10' or option1 == 'P10':
        st.subheader('P10 graph')
        fig = px.line(df, x="t", y="P10", title='P10')
        st.plotly_chart(fig)
    # #### PLOTTING THE SENSOR DATA  END      'P0_3', 'P0_5', 'P1_0', 'P2_5', 'P5_0', 'P10'
    return df

def main(file):
    ## Data file in the root folder (where this python file is stored)
    #file = open('notPlasma_1.txt', 'r')
    for line in file:
        splitline = line.split(' ')
        # Extracting starting Date and time of the sensor data read
        if splitline[1] == 'PuTTY':
            time_1 = splitline[4]
            date_1 = splitline[3]
            date_1 = dt.datetime.strptime(date_1, "%Y.%m.%d")
            date_1 = date_1.strftime("%d-%m-%y")
            date_1 = dt.datetime.strptime(date_1, "%d-%m-%y")
            time_1 = dt.datetime.strptime(time_1, "%H:%M:%S").time()
            time_now = dt.datetime.combine(date_1, time_1)
            break
    print(parameters(file, time_now))


if __name__ == '__main__':
    if option2 == 'Plasma':
        file = open('pahPlasma_1.txt', 'r')
        main(file)
    if option2 == 'NotPlasma':
        file = open('notPlasma_1.txt', 'r')
        main(file)

