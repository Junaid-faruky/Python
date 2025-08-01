# 20. Speech to text (OpenAI Whisper)
import openai
audio_file= open("speech.mp3","rb")
transcript = openai.Audio.transcriptions.create(model="whisper-1", file=audio_file)
print(transcript.text)
