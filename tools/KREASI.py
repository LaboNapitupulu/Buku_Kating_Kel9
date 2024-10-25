import streamlit as st
import random

# List of quotes
quotes = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "The secret of getting ahead is getting started. - Mark Twain"
]

# Title of the app
st.title("Random Quote Generator")

# Display a random quote
st.write("Here is your quote of the day:")
st.write(random.choice(quotes))

# Add a button to generate a new quote
if st.button("Generate New Quote"):
    st.write(random.choice(quotes))

