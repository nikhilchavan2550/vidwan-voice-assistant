# Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai


# Custom function imports
from functions.text_to_speech import  text_to_audio
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages

# Get Environment Vars
openai.organization = config("OPEN_AI_ORG", default="org-C0W6EHmQZOFhOLs7cG0zhcR6")
openai.api_key = config("OPEN_AI_KEY", default="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")

# Initiate App
app = FastAPI()


# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:3000",
]


# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Check health
@app.get("/health")
async def check_health():
    return {"response": "healthy"}


# Reset Conversation
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"response": "conversation reset"}


# Post bot response
# Note: Not playing back in browser when using post request.
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
    # Convert audio to text - production
    # Save the file temporarily
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())


    audio_input = open(file.filename, "rb")

    message_decoded = convert_audio_to_text(audio_input)


    # Guard: Ensure output
    if not message_decoded:
        print("Failed to decode audio ")
        raise HTTPException(status_code=400, detail="Failed to decode audio")

    # Get chat response
    chat_response = get_chat_response(message_decoded)

    # Store messages
    store_messages(message_decoded, chat_response)

    # Guard: Ensure output
    if not chat_response:
        print("chat response not available")
        raise HTTPException(status_code=400, detail="Failed chat response")

    # Convert chat response to audio
    audio_output, file_name = text_to_audio(chat_response)


    # Guard: Ensure output
    if not audio_output:
        print("Failed audio output, i mean the audio output is not availble")
        raise HTTPException(status_code=400, detail="Failed audio output")

    def iterfile():
        with open(f"./{file_name}", 'rb') as f:
            yield from f

    return StreamingResponse(iterfile(), media_type="audio/mpeg")
