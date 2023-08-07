import streamlit
import pandas

streamlit.title("My First Streamlit Application")

streamlit.header("Breakfast Menu")

streamlit.text("Masala Dosa")
streamlit.text("Chole Bhature")
streamlit.text("Idly")

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
