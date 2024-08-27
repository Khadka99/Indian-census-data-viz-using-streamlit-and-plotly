import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv("India.csv")
list_of_state = df['State'].unique().tolist()
list_of_state.insert(0,'Overall India')


st.sidebar.title("India Data Viz")

selected_state = st.sidebar.selectbox("Select a State",list_of_state)
primary = st.sidebar.selectbox("Select Primary Parameter",sorted(df.columns[5:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter",sorted(df.columns[5:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size Represents Primary Parameter")
    st.text("Color Represents Secondary Parameter")
    if selected_state == 'Overall India':
        #plot all india viz
        fig = px.scatter_mapbox(df, lat='Latitude', lon='Longitude', zoom=4,
                                size= primary,color=secondary,size_max=35,
                                width=1200,height=700,hover_name='District',
                                color_continuous_scale=px.colors.cyclical.IceFire,
                                mapbox_style='carto-positron')
        st.plotly_chart(fig,use_container_width=True)
    else:
        #plot state wise viz
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=6,
                                size=primary,color=secondary, size_max=35,
                                width=1200, height=700, hover_name='District',
                                color_continuous_scale=px.colors.cyclical.IceFire,
                                mapbox_style='carto-positron')
        st.plotly_chart(fig, use_container_width=True)
