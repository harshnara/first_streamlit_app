import streamlit
import pandas
import requests
import snowflake.connector


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

fruit_choice = streamlit.text_input("What fruit you would like?", 'Kiwi')
streamlit.write('The user entered', fruit_choice)

response = requests.get('https://fruityvice.com/api/fruit/' + fruit_choice)

fruit_df = pandas.json_normalize(response.json())
streamlit.dataframe(fruit_df)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
