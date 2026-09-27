import streamlit as st

st.set_page_config(page_title="AI Study Assistant", page_icon="📚")

st.title("📚 AI Study Assistant")
st.write("Create a personalized study-plan prompt to use with ChatGPT or Gemini.")

subject = st.text_input("What subject are you studying?")
topic = st.text_input("Which topic do you want to learn?")
hours = st.number_input("How many hours can you study?", min_value=1, max_value=12, value=2)
level = st.selectbox("Your current level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Create my study prompt"):
    if subject.strip() and topic.strip():
        prompt = f"""
Act as a friendly study tutor. Create a practical study plan for me.

Subject: {subject}
Topic: {topic}
Available study time: {hours} hour(s)
My current level: {level}

Include:
1. A simple explanation of the topic.
2. A time-based study schedule.
3. Important points to remember.
4. Three practice questions with answers.
5. A short revision checklist.

Use clear, beginner-friendly language.
"""
        st.subheader("Your study prompt")
        st.code(prompt, language="text")
        st.info("Copy this prompt and paste it into ChatGPT or Gemini to get your study plan.")
    else:
        st.warning("Please enter both a subject and a topic.")
