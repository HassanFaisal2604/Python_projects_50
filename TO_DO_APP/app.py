import streamlit as st
import functions 
todos=functions.read_tasks()
print(todos)
st.title("Welcome to the To-Do App!")
st.subheader("This is a To-do app") 
def add_todo():
    todo=st.session_state["new_todo"]
    functions.add_task(todo)
    
for todo in todos:
    st.checkbox(todo)
    
  
input_user=st.text_input(label="",placeholder="add new todo",on_change=add_todo,key='new_todo')
st.session_state