import streamlit as st
from datetime import datetime
from src import task_manager, scheduler
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI()

st.set_page_config(page_title="Student Personal Assistant", page_icon="🎓")

st.title("🎓 Student Personal Assistant")
st.write("Manage tasks, reminders, and ask academic questions easily.")

# --- Task Manager ---
st.header("📝 Task Manager")

tasks = task_manager.load_tasks()
new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task:
        tasks.append(new_task)
        task_manager.save_tasks(tasks)
        st.success(f"Task '{new_task}' added.")
    else:
        st.warning("Please enter a task before adding.")

if st.button("View Tasks"):
    if tasks:
        st.write("### Your Tasks:")
        for idx, task in enumerate(tasks, 1):
            st.write(f"{idx}. {task}")
    else:
        st.info("No tasks available.")

# --- Reminder Scheduler ---
st.header("⏰ Reminder Scheduler")

reminders = scheduler.load_reminders()
note = st.text_input("Reminder Note:")
reminder_datetime = st.text_input("Date & Time (YYYY-MM-DD HH:MM):")

if st.button("Add Reminder"):
    if note and reminder_datetime:
        try:
            dt = datetime.strptime(reminder_datetime, "%Y-%m-%d %H:%M")
            reminders.append({"note": note, "datetime": dt.strftime("%Y-%m-%d %H:%M")})
            scheduler.save_reminders(reminders)
            st.success(f"Reminder '{note}' added for {dt}.")
        except ValueError:
            st.error("Invalid date format. Use YYYY-MM-DD HH:MM.")
    else:
        st.warning("Please enter both note and date/time.")

if st.button("View Reminders"):
    if reminders:
        st.write("### Your Reminders:")
        for idx, reminder in enumerate(reminders, 1):
            st.write(f"{idx}. {reminder['note']} at {reminder['datetime']}")
    else:
        st.info("No reminders available.")

# --- Academic Q&A ---
st.header("🤖 Academic Q&A (GPT-powered)")

question = st.text_input("Ask your academic question:")
if st.button("Ask"):
    if question:
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-preview",
                    messages=[
                        {"role": "system", "content": "You are a helpful academic assistant for students."},
                        {"role": "user", "content": question}
                    ]
                )
                st.write("### Answer:")
                st.write(response.choices[0].message.content.strip())
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question before submitting.")
