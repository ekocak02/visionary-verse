# app/main.py

from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
from .ai_core import get_image_caption, generate_story_from_caption

app = FastAPI(
    title="Visionary Verse API",
    description="An AI service that generates fantasy stories inspired by an image."
)

@app.get("/")
def read_root():
    """A simple root endpoint to check if the API is running."""
    return {"message": "Welcome to the Visionary Verse API! Go to /docs to test."}

@app.post("/generate")
async def generate_text_from_image(file: UploadFile = File(...)):
    """
    Generates a story from an uploaded image file.
    - **file**: The image file to upload (e.g., jpg, png).
    """
    contents = await file.read()
    try:
        uploaded_image = Image.open(io.BytesIO(contents)).convert("RGB")
    except Exception:
        return {"error": "Invalid image file. Please upload a file in jpg or png format."}

    image_caption = get_image_caption(uploaded_image)
    if "Could not generate" in image_caption:
        return {"error": "Could not understand the content of the image."}
    
    generated_story = generate_story_from_caption(image_caption)

    return {
        "input_image_filename": file.filename,
        "generated_caption": image_caption,
        "generated_story": generated_story
    }