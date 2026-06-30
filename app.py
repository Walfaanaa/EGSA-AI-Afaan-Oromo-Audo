import streamlit as st
import asyncio
import edge_tts

st.set_page_config(
    page_title="EGSA Afaan Oromoo AI Voice",
    page_icon="🎙️"
)

st.title("🎙️ EGSA Afaan Oromoo AI Voice Generator")


text = st.text_area(
    "Afaan Oromoo barreessi:",
    """
Baga nagaan gara Dhaabbata Economic Growth Solution Association EGSA dhuftan.

Mee waa'ee EGSA, kaayyoo isaa fi hojii isaa waliin haa barannu.
"""
)


async def get_voices():
    voices = await edge_tts.list_voices()

    # Oromo voices
    oromo = [
        v["ShortName"]
        for v in voices
        if "om" in v["ShortName"].lower()
    ]

    return oromo


async def create_audio():

    voices = await get_voices()

    if len(voices) == 0:
        voice = "en-US-JennyNeural"
    else:
        voice = voices[0]


    communicate = edge_tts.Communicate(
        text,
        voice
    )

    await communicate.save(
        "EGSA_audio.mp3"
    )

    return voice



if st.button("Generate Audio 🎧"):

    try:

        voice_used = asyncio.run(create_audio())

        st.success(
            f"Audio created using {voice_used}"
        )

        with open(
            "EGSA_audio.mp3",
            "rb"
        ) as audio:

            st.audio(
                audio.read(),
                format="audio/mp3"
            )


    except Exception as e:

        st.error(
            f"Voice generation failed: {e}"
        )
