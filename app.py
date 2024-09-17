import streamlit as st
from DBhelper import DB
import plotly.express as px
db = DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu',['Select one','Check Flights','Analytics'])

if user_option =='Check Flights':
    st.title ('Check Flights')
    col1,col2 = st.columns(2)
    db.__int__()
    data=db.fetch_city_names()
    with col1:
        source = st.selectbox('Source',data)
    with col2:
        destination = st.selectbox('Destination',data)
    if st.button('Search'):
        result = db.fetch_flight_data(source,destination)
        st.dataframe(result)
elif user_option =='Analytics':
    db.__int__()
    st.title('Analytics')

    airline, freq = db.piechart_data()
    fig = px.pie(values=freq,names=airline, title="Piechart")
    st.plotly_chart(fig, theme=None)

    city,num = db.busy_aiport()
    fig = px.bar(x=city,y=num)
    st.plotly_chart(fig,theme='streamlit',use_container_width=True)

    date, num2 = db.doj()
    fig = px.line(x=date,y=num2)
    st.plotly_chart(fig,theme='streamlit',use_container_width=True)



else:
    st.title('Tell about the project')

