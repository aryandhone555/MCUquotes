import streamlit as st
import random
import quotes  # Import the quotes from quotes.py

def get_random_quote():
    character = random.choice(list(quotes.mcu_quotes.keys()))
    quote = random.choice(quotes.mcu_quotes[character])
    return character, quote

# Page configuration
st.set_page_config(page_title="MCU Quote Generator", page_icon=":rocket:", layout="wide")

# Set the background image using a URL
bg_image_url = "https://wallpapercave.com/wp/wp2436369.jpg"

# Add custom CSS for background image and styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url({bg_image_url}) no-repeat center center fixed;
        background-size: cover;
        height: 100vh;
        width: 100vw;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }}
    .title {{
        font-family: 'Bungee', monospace;
        font-size: 3em;
        color: #FFFFFF;
        text-shadow: 2px 2px #000000;
        text-align: center;
    }}
    .welcome {{
        font-family: 'Orbitron', monospace;
        font-size: 1.5em;
        color: #FFFFFF;
        text-shadow: 1px 1px #000000;
        text-align: center;
    }}
    .quote-box {{
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 15px;
        margin: 20px auto;
        max-width: 600px;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }}
    .footer {{
        text-align: center;
        margin-top: 50px;
        color: #4A148C;
    }}
    .footer a {{
        color: #6A1B9A;
        text-decoration: none;
        font-weight: bold;
    }}
    .footer a:hover {{
        color: #4A148C;
        text-decoration: underline;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title and welcome message with increased font size
st.markdown('<div class="title">Quotes From MARVEL CINEMATIC UNIVERSE</div>', unsafe_allow_html=True)
st.markdown('<div class="welcome">Welcome! Refresh the page to see a new quote.</div>', unsafe_allow_html=True)

# Get and display a random quote
character, quote = get_random_quote()
st.markdown(f'<div class="quote-box"><blockquote>&ldquo;{quote}&rdquo;<br> &mdash; {character}</blockquote></div>', unsafe_allow_html=True)

# Footer with designer information
st.markdown("---")
st.markdown(
    """
    <div class="footer">
        Designed by <a href="https://linktr.ee/aryandhone555">Aryan</a> 
        <br>
        <a href="mailto:er.aryandhone@gmail.com">er.aryandhone@gmail.com</a> |
        <a href="https://linkedin.com/in/aryandhone555">LinkedIn</a>
    </div>
    """, unsafe_allow_html=True
)
