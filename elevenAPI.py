from dotenv import load_dotenv
from io import BytesIO
#import requests
import os
from elevenlabs.client import ElevenLabs
#from pydub import AudioSegment

load_dotenv()

client = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY")
)

file_path = r"C:\Users\chris\Downloads\JRE-56.mp4"

with open(file_path, "rb") as f:
    file_data = f.read()

    audio_data = BytesIO(file_data)

    transcription = client.speech_to_text.convert(
    file=audio_data,
    model_id="scribe_v1",
    diarize=True,
    enable_logging=True)

    print(transcription)
