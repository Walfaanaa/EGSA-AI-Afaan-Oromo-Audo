import streamlit as st
import edge_tts
import asyncio
import os

st.set_page_config(
    page_title="EGSA Afaan Oromoo Voice",
    page_icon="🎙️"
)

st.title("🎙️ EGSA Afaan Oromoo AI Voice Generator")

text = st.text_area(
    "Barreeffama Afaan Oromoo galchi:",
    value="""
Baga nagaan gara Dhaabbata Economic Growth Solution Association EGSA dhuftan.

Tokkummaan keenya humna keenya.
"""
)

# Use stable female voice
VOICE = "en-US-JennyNeural"


async def generate_audio():

    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )

    await communicate.save("EGSA_audio.mp3")


if st.button("Generate 🎧"):

    try:
        asyncio.run(generate_audio())

        st.success("Audio generated successfully!")

        with open("EGSA_audio.mp3", "rb") as f:
            st.audio(f.read(), format="audio/mp3")

    except Exception as e:
        st.error("Error generating audio")
        st.write(e)
