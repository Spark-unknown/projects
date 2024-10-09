import streamlit as st
from datetime import datetime

# File path where tasks will be stored
TASK_FILE = 'tasks.txt'

# Function to read tasks from the file
def read_tasks():
    tasks = []
    try:
        with open(TASK_FILE, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                task = line.split(' | ')
                if len(task) < 4:
                    st.warning(f"Skipping malformed line: {line}")
                    continue
                tasks.append({
                    "title": task[0],
                    "description": task[1],
                    "due_date": task[2],
                    "status": task[3]
                })
    except FileNotFoundError:
        pass
    return tasks

# Function to add a task to the file
def add_task(title, description, due_date):
    with open(TASK_FILE, 'a') as file:
        file.write(f"{title} | {description} | {due_date} | active\n")

# Function to remove a task from the file
def remove_task(title):
    tasks = read_tasks()
    tasks = [task for task in tasks if task['title'] != title]
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task['title']} | {task['description']} | {task['due_date']} | {task['status']}\n")

# Initialize session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = read_tasks()

# Streamlit UI
st.title("Task Management System")

# Form to add a new task
with st.form(key='task_form'):
    task_title = st.text_input("Task Title", value=st.session_state.get('task_title', ''))
    task_description = st.text_area("Task Description", value=st.session_state.get('task_description', ''))
    task_due_date = st.date_input("Due Date", value=st.session_state.get('task_due_date', datetime.today()))
    submit_button = st.form_submit_button("Add Task")
    
    if submit_button:
        add_task(task_title, task_description, task_due_date.strftime('%Y-%m-%d'))
        st.success("Task added successfully!")

        # Clear the input fields by resetting session state
        st.session_state.task_title = ""
        st.session_state.task_description = ""
        st.session_state.task_due_date = datetime.today()
        st.session_state.tasks = read_tasks()  # Refresh task list

# Display existing tasks in a card format
st.subheader("Existing Tasks")
if st.session_state.tasks:
    for task in st.session_state.tasks:
        # Display each task in a card-like format
        col1, col2 = st.columns([8, 2])  # Create two columns for task display and button
        with col1:
            st.markdown(
                f"""
                <div style="border: 1px solid #ccc; padding: 10px; margin-bottom: 10px; border-radius: 5px;">
                    <h4>{task['title']}</h4>
                    <p><strong>Description:</strong> {task['description']}</p>
                    <p><strong>Due Date:</strong> {task['due_date']}</p>
                    <p><strong>Status:</strong> {task['status']}</p>
                </div>
                """, unsafe_allow_html=True
            )
        with col2:
            if st.button("Remove", key=task['title']):  # Use a unique key for each button
                remove_task(task['title'])
                st.success(f"Task '{task['title']}' removed successfully!")
                st.session_state.tasks = read_tasks()  # Refresh task list immediately
else:
    st.write("No tasks available.")
