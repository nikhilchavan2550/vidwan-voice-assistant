from gtts import gTTS
import random


def text_to_audio(text, output_file=f'output{random.randint(1,1000)}.mp3', lang='en'):
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_file)
    print("output saved to ", output_file)
    print("=================DONE==================")
    return tts, output_file
    # os.system('start ' + output_file)  # Opens the audio file with the default program













### Eleven Labs: Convert text to speech
# import requests
# from decouple import config

# ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY", default="") #shubham api key

# # Eleven Labs
# # Convert text to speech
# def convert_text_to_speech(message):
#   body = {
#     "text": message,
#     "voice_settings": {
#         "stability": 0,
#         "similarity_boost": 0
#     }
#   }

#   voice_shaun = "mTSvIrm2hmcnOvb21nW2"
#   voice_rachel = "21m00Tcm4TlvDq8ikWAM"
#   voice_antoni = "ErXwobaYiN019PkySvjV"

#   # Construct request headers and url
#   headers = { "xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "accept": "audio/mpeg" }
#   endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_antoni}"

#   try:
#     print("----------Now eleven labs things are below-------")
#     print("endpoint is: ", endpoint)
#     print("body is: ", body)
#     print("headers are: ", headers)
#     print("----------Now eleven labs things are above-------")

#     response = requests.post(endpoint, json=body, headers=headers)
#     print(response)
#     print(response.content) 
#   except Exception as e:
#     print("Error in converting text to speech of output response: ", e)
#     return




#   if response.status_code == 200:
#       print("audio response and status code is 200 and there should be outputfileofresponse.wav in the backend folder")
#       # with open("outputfileofresponse.wav", "wb") as f:
#       #     f.write(audio_data)
#       print("audio response and status code is 200 and above is response from eleven labs", response.content)
#       return response.content
#   else:
#     return
