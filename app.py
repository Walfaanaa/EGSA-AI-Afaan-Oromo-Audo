import streamlit as st
import edge_tts
import asyncio
import os

st.set_page_config(
    page_title="EGSA Afaan Oromoo AI Audio",
    page_icon="🎙️"
)

st.title("🎙️ EGSA Afaan Oromoo AI Voice Generator")

text = st.text_area(
    "Barreeffama Afaan Oromoo galchi:",
    value="""
Baga nagaan gara Dhaabbata Economic Growth Solution Association EGSA dhuftan.

Mee waa'ee EGSA, kaayyoo isaa fi hojii isaa waliin haa barannu.
"""
)


async def get_oromo_voice():

    voices = await edge_tts.list_voices()

    # Search Oromo voice
    for voice in voices:
        if voice["Locale"] == "om-ET":
            return voice["ShortName"]

    # fallback female voice
    return "en-US-JennyNeural"



async def generate():

    voice = await get_oromo_voice()

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice
    )

    await communicate.save(
        "EGSA_audio.mp3"
    )

    return voice



if st.button("Generate 🎧"):

    try:

        voice_used = asyncio.run(generate())

        st.success(
            f"Generated using: {voice_used}"
        )

        if os.path.exists("EGSA_audio.mp3"):

            with open(
                "EGSA_audio.mp3",
                "rb"
            ) as f:

                st.audio(
                    f.read(),
                    format="audio/mp3"
                )

    except Exception as e:

        st.error(
            "Audio generation failed"
        )

        st.write(e)
