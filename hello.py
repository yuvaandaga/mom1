import streamlit as st
import random

# Title and Introduction
st.title("Thanks for Everything You Have Done for Me 💖")
st.write("Here are some reasons that make you the best mom ever:")

# List of reasons
reasons = [
    "You always try to lead me to the right path!",
    "You always want my wellbeing!",
    "You make the best aamras!",
    "You are the best!",
    "You always want us to have fun!",
    "You always think of us before yourself!",
    "Sanjeev Kapoor is no match for your cooking!"
]

# When the button is clicked
if st.button("Show me a reason 💌"):
    reason = random.choice(reasons)
    st.success(reason)

    # Play the Bulleya song after the button is clicked
    audio_file = open("Bulleya-Sultan.mp3", "rb")  # Ensure the song is in the same folder as this script
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")


