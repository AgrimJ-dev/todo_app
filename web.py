import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("Use this app to increase your productivity!")

st.text("Start the day with accountability and discipline!")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",placeholder="Add a new task")