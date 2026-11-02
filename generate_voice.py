import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

text = """
Dzień dobry! Witam w podcaście Świat w 20 minut.
Przed nami najważniejsze wiadomości ze świata.
Polityka, gospodarka, biznes i technologia.
Przedstawimy fakty, kontekst i konsekwencje.
Zaczynamy!
"""

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="cedar",
    input=text,
    instructions=(
        "Speak fluent, natural Polish in the style of "
        "a dynamic, professional radio news journalist. "
        "Use expressive but credible intonation, "
        "natural pauses, and confident pacing. "
        "Avoid robotic delivery."
    ),
) as response:
    response.stream_to_file(Path("probka_glosu.mp3"))

print("Gotowe: probka_glosu.mp3")
