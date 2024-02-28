import openai
from decouple import config

from functions.database import get_recent_messages

# Get Environment Vars
openai.organization = config("OPEN_AI_ORG", default="org-C0W6EHmQZOFhOLs7cG0zhcR6")
openai.api_key = config("OPEN_AI_KEY", default="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")

# Open AI - Whisper
# Convert audio to text
def convert_audio_to_text(audio_file):
  try:
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    message_text = transcript["text"]
    print("=================USER TRANSCRIPTED PROMPT====================")
    print("Users input: ", message_text)
    return message_text
  except Exception as e:
    print("Error in converting audio to text: ", e)
    return

# Open AI - Chat GPT
# Convert audio to text
def get_chat_response(message_input):

  messages = get_recent_messages()
  user_message = {"role": "user", "content": message_input }
  messages.append(user_message)
  try:
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )
    message_text = response["choices"][0]["message"]["content"]
    print("=================RESPONSE====================")
    print("Output Text response : ", message_text)
    print("=================RESPONSE till here====================")
    return message_text
  except Exception as e:
    print("Error in getting chat response: ", e)
    return
