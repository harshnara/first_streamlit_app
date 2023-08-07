import streamlit
import pandas

streamlit.title("My First Streamlit Application")

streamlit.header("Breakfast Menu")

streamlit.text("Masala Dosa")
streamlit.text("Chole Bhature")
streamlit.text("Idly")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list_w_index = my_fruit_list.set_index('Fruit')

fruit_selected = streamlit.multiselect('Pick some fruits',list(my_fruit_list_w_index.index),['Avocado'])

fruits_to_show = my_fruit_list_w_index.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)
