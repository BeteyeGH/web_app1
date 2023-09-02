import streamlit as st #importing the streamlit third party module for web app designing
import functions

todos=functions.file_open()

def todos_add(): #this is the function we defined which will be called thru the on_change argument of the text input - this will be called first when text input changes, then the whole script will be called from top to bototm
    todo_new=st.session_state["new_todo"] + '\n' #here we get the new todo extracted from the session_state dictionary with also the backslash n for proper spacing of list items
    if todo_new not in todos: # the append process will only be made if the todo_new is not already in the todos list - adding this function to prevent the DuplicateWidget error - when a check is made the app re-runs so it was taking what was placed in the inbox bar into the txt file again
        todos.append(todo_new) #here we append the new taken todo to todos list
        functions.file_write(todos) #then we write the new todos list into the text file for updating

st.title("My To-Do App")
st.subheader("This is my to-do app.")
st.write("This app is for increasing your productivity.")

for index, todo in enumerate(todos): #for iteration on every single element of todos
    checkbox=st.checkbox(todo, key=todo) #write it as checkbox element
    if checkbox: #other way of saying if checkbox == true - if the item's checkbox is checked it shows true as the variable
        todos.pop(index) #then remove the item from the todos list - based on its index
        functions.file_write(todos) #writing the new updated list into txt file
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a to-do:", placeholder="Please enter a to-do...", on_change=todos_add, key="new_todo")


