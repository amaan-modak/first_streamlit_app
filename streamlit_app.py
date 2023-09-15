import streamlit

streamlit.title('My Parents\' New Healthy Diner')

streamlit.header('🥑Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach Smoothie')
streamlit.text('🐔Hard-boiled Egg')


streamlit.header('Build your own first smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
