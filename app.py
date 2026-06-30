import streamlit as st
import asyncio
import edge_tts

st.set_page_config(
    page_title="EGSA Afaan Oromoo AI Voice",
    page_icon="🎙️"
)

st.title("🎙️ EGSA Afaan Oromoo AI Voice Generator")

text = st.text_area(
    "Barreeffama Afaan Oromoo galchi:",
    """
Baga nagaan gara Dhaabbata Economic Growth Solution Association EGSA dhuftan.

Mee waa'ee EGSA, kaayyoo isaa fi hojii isaa waliin haa barannu.
"""
)

voice = st.selectbox(
    "Filadhu:",
    [
        "om-ET-MekdesNeural"
    ]
)


async def generate_audio():
    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(
        "EGSA_audio.mp3"
    )


if st.button("Generate Audio 🎧"):

    asyncio.run(generate_audio())

    st.success(
        "Audio created successfully!"
    )

    audio_file = open(
        "EGSA_audio.mp3",
        "rb"
    )

    st.audio(
        audio_file.read(),
        format="audio/mp3"
    )