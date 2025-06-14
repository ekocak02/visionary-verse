# app/ai_core.py

import warnings
from transformers import pipeline, AutoProcessor
from PIL import Image
import torch

# Ignore the specific warning about the slow processor, as it's informational.
warnings.filterwarnings(
    "ignore", 
    message="Using a slow image processor as `use_fast` is unset*"
)

# Determine the device to use (GPU if available, otherwise CPU)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {DEVICE}")


# --- Load Models ---
# Models are loaded once when the script starts to improve performance
# and avoid reloading on every request.
print("Loading image-to-text model (GIT)...")
git_processor = AutoProcessor.from_pretrained("microsoft/git-large-coco")
captioner = pipeline(
    "image-to-text", 
    model="microsoft/git-large-coco",
    processor=git_processor,
    device=DEVICE
)
print("Image-to-text model loaded.")

print("Loading text-generation model (GPT-2)...")
text_generator = pipeline(
    "text-generation", 
    model="gpt2",
    device=DEVICE
)
print("Text-generation model loaded.")


# --- Core Functions ---
def get_image_caption(image: Image.Image) -> str:
    """Generates a text caption from a given PIL Image object."""
    try:
        result = captioner(image)
        caption = result[0]['generated_text']
        print(f"Generated Caption: {caption}")
        return caption
    except Exception as e:
        print(f"Error in get_image_caption: {e}")
        return "Could not generate image caption."

def generate_story_from_caption(caption: str) -> str:
    """Generates a story based on a given caption."""
    prompt = f"A fantasy adventure set in a land that once was {caption}:"
    try:
        result = text_generator(
            prompt, 
            max_new_tokens=150,
            num_return_sequences=1,
            temperature=0.9,
            repetition_penalty=1.2,
            truncation=True,
            pad_token_id=text_generator.tokenizer.eos_token_id
        )
        generated_text = result[0]['generated_text']
        print("\n--- Generated Story ---")
        print(generated_text)
        print("-----------------------\n")
        return generated_text
    except Exception as e:
        print(f"Error in generate_story_from_caption: {e}")
        return "Could not generate story."

# --- Direct Test Block ---
# This block runs only when the script is executed directly (e.g., python app/ai_core.py)
# It's useful for testing the AI logic without running the full API.
if __name__ == "__main__":
    test_image_file = "test_image.jpeg"
    print(f"Starting test with '{test_image_file}'...")
    try:
        image_obj = Image.open(test_image_file).convert("RGB")
        image_caption = get_image_caption(image_obj)
    
        if "Could not generate" not in image_caption:
            generate_story_from_caption(image_caption)
        else:
            print("Story could not be generated because caption creation failed.")
    except FileNotFoundError:
        print(f"Error: Test file '{test_image_file}' not found. Please add an image to the project's root directory.")