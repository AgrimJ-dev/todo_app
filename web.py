import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_task = st.session_state["new_task"] + "\n"
    todos.append(new_task)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("Use this app to increase your productivity!")

st.text("Start the day with accountability and discipline!")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="ADD TASK",placeholder="Add a new task",
              on_change=add_todo, label_visibility="hidden", key="new_task")

