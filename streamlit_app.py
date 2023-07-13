import streamlit

streamlit.title('My Mom\'s New Healthy Diner')
streamlit.header('BreakFast Favorites')
streamlit.text('🥣 Omega3 & Blueberry Oat meal')
streamlit.text('🥑🍞 PanCake & Egg Omlette')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
