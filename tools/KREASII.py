
import streamlit as st
import random

# Daftar kutipan 
kutipan = [
    {"quote": "The best way to predict the future is to create it.", "author": "Peter Drucker"},
    {"quote": "Success is not the key to happiness. Happiness is the key to success.", "author": "Albert Schweitzer"},
    {"quote": "Life is what happens when you're busy making other plans.", "author": "John Lennon"},
    {"quote": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt"},
    {"quote": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein"},
    {"quote": "You miss 100% of the shots you don’t take.", "author": "Wayne Gretzky"},
    {"quote": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
    {"quote": "Do not watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.", "author": "Winston Churchill"},
    {"quote": "It is never too late to be what you might have been.", "author": "George Eliot"},
    {"quote": "You must be the change you wish to see in the world.", "author": "Mahatma Gandhi"},
    {"quote": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"quote": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"quote": "Don’t let yesterday take up too much of today.", "author": "Will Rogers"},
    {"quote": "What lies behind us and what lies before us are tiny matters compared to what lies within us.", "author": "Ralph Waldo Emerson"},
    {"quote": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"quote": "Strive not to be a success, but rather to be of value.", "author": "Albert Einstein"},
    {"quote": "The only impossible journey is the one you never begin.", "author": "Tony Robbins"},
    {"quote": "Success usually comes to those who are too busy to be looking for it.", "author": "Henry David Thoreau"},
    {"quote": "Opportunities don’t happen, you create them.", "author": "Chris Grosser"},
    {"quote": "Don’t be afraid to give up the good to go for the great.", "author": "John D. Rockefeller"},
    {"quote": "I find that the harder I work, the more luck I seem to have.", "author": "Thomas Jefferson"},
    {"quote": "Success is walking from failure to failure with no loss of enthusiasm.", "author": "Winston Churchill"},
    {"quote": "Don’t wait for opportunity. Create it.", "author": "George Bernard Shaw"},
    {"quote": "Try not to become a person of success, but rather try to become a person of value.", "author": "Albert Einstein"},
    {"quote": "Dream big and dare to fail.", "author": "Norman Vaughan"},
    {"quote": "He who has a why to live can bear almost any how.", "author": "Friedrich Nietzsche"},
    {"quote": "Success is not how high you have climbed, but how you make a positive difference to the world.", "author": "Roy T. Bennett"},
    {"quote": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis"},
    {"quote": "A winner is a dreamer who never gives up.", "author": "Nelson Mandela"},
    {"quote": "What you get by achieving your goals is not as important as what you become by achieving your goals.", "author": "Zig Ziglar"},
    {"quote": "Happiness is not something ready-made. It comes from your own actions.", "author": "Dalai Lama"},
    {"quote": "Challenges are what make life interesting. Overcoming them is what makes life meaningful.", "author": "Joshua J. Marine"},
    {"quote": "Do what you can, with what you have, where you are.", "author": "Theodore Roosevelt"},
    {"quote": "The only person you are destined to become is the person you decide to be.", "author": "Ralph Waldo Emerson"},
    {"quote": "To succeed in life, you need two things: ignorance and confidence.", "author": "Mark Twain"},
    {"quote": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"quote": "Hardships often prepare ordinary people for an extraordinary destiny.", "author": "C.S. Lewis"},
    {"quote": "People have to go through trials and tribulations to get where they at. Do your thing - continue to rock it - because obviously, God wants you here.", "author": "Kendrick Lamar"}
]

# Judul 
st.title("Penghasil Kutipan Acak")

# Menyimpan state dari kutipan yang dihasilkan
if 'kutipan_terpilih' not in st.session_state or isinstance(st.session_state.kutipan_terpilih, str):
    st.session_state.kutipan_terpilih = random.choice(kutipan)

# Tombol 
if st.button("Tampilkan Quotes Baru"):
    st.session_state.kutipan_terpilih = random.choice(kutipan)

# Tampilkan kutipan dan penulis dengan gaya CSS 
st.markdown(
    f"""
    <div style="text-align: center; font-size: 30px; font-family: 'Courier New', Courier, monospace;">
        <b>"{st.session_state.kutipan_terpilih['quote']}"</b><br><br>
        <b style="text-align: center;">{st.session_state.kutipan_terpilih['author']}</b>
    </div>
    """,
    unsafe_allow_html=True
)
