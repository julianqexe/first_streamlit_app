import streamlit
import pandas
streamlit.title('My parents new healthy Diner')
streamlit.header('Breakfast menu')
streamlit.text('Omega 3 and blueberry muffin 🥣')
streamlit.text('Kale, spinach and rocket smoothie 🥗')
streamlit.text('Hardboiled free range eggs 🐔')
streamlit.text('Avocado toast 🥑🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

