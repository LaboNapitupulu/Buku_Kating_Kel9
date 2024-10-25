import streamlit as st
import random

# Daftar kutipan dalam bahasa Inggris
kutipan = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "You miss 100% of the shots you don’t take. - Wayne Gretzky",
    "The secret of getting ahead is getting started. - Mark Twain",
    "Do not watch the clock; do what it does. Keep going. - Sam Levenson",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "It is never too late to be what you might have been. - George Eliot",
    "You must be the change you wish to see in the world. - Mahatma Gandhi",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Don’t let yesterday take up too much of today. - Will Rogers",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Strive not to be a success, but rather to be of value. - Albert Einstein",
    "The only impossible journey is the one you never begin. - Tony Robbins",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Opportunities don’t happen, you create them. - Chris Grosser",
    "Don’t be afraid to give up the good to go for the great. - John D. Rockefeller",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "Don’t wait for opportunity. Create it. - George Bernard Shaw",
    "Try not to become a person of success, but rather try to become a person of value. - Albert Einstein",
    "Great things never come from comfort zones. - Anonymous",
    "Dream big and dare to fail. - Norman Vaughan",
    "He who has a why to live can bear almost any how. - Friedrich Nietzsche",
    "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis",
    "A winner is a dreamer who never gives up. - Nelson Mandela",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "Happiness is not something ready-made. It comes from your own actions. - Dalai Lama",
    "Challenges are what make life interesting. Overcoming them is what makes life meaningful. - Joshua J. Marine",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "To succeed in life, you need two things: ignorance and confidence. - Mark Twain",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis"
]

# Judul aplikasi dalam bahasa Indonesia
st.title("Penghasil Kutipan Acak")

# Menyimpan state dari kutipan yang dihasilkan
if 'kutipan_terpilih' not in st.session_state:
    st.session_state.kutipan_terpilih = random.choice(kutipan)

# Tombol untuk menghasilkan kutipan baru
if st.button("Tampilkan Kutipan Baru"):
    st.session_state.kutipan_terpilih = random.choice(kutipan)

# Tampilkan kutipan dengan tulisan besar dan font yang unik
st.markdown(
    f"""
    <div style="text-align: center; font-size: 30px; font-family: 'Courier New', Courier, monospace;">
        {st.session_state.kutipan_terpilih}
    </div>
    """,
    unsafe_allow_html=True
)
