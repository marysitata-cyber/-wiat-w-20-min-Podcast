
import asyncio
import edge_tts

TEXT = """
Dzień dobry! Witam w podcaście Świat w 20 minut.

Przed nami najważniejsze wiadomości ze świata.
Polityka, gospodarka, biznes i technologia.

Przedstawimy fakty, wyjaśnimy kontekst
i pokażemy, jakie konsekwencje mają
dzisiejsze wydarzenia.

Zaczynamy!
"""

async def main():
    speech = edge_tts.Communicate(
        text=TEXT,
        voice="pl-PL-MarekNeural",
        rate="+8%",
        pitch="-2Hz"
    )
    await speech.save("probka_glosu.mp3")

asyncio.run(main())
