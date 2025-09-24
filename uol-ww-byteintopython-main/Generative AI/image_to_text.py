import os

os.environ["CUDA_LAUNCH_BLOCKING"]="1" 
os.environ["TORCH_USE_CUDA_DSA"] = "1"

# import the HuggingFace transformers library for manipulating models
from transformers import AutoProcessor, AutoTokenizer, Gemma3ForConditionalGeneration
from PIL import Image
import torch

# Define the local model path
local_model_path = "C:\GenAI\models\Gemma34bit"

# Load the model, processor, and tokenizer
model = Gemma3ForConditionalGeneration.from_pretrained(local_model_path, torch_dtype=torch.bfloat16)
processor = AutoProcessor.from_pretrained(local_model_path, use_fast=True,trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(local_model_path, use_fast=True)

# Move the model to GPU if available
#model.to(torch.device('cuda'))

# Define the prompt and image path
prompt = "<start_of_image> Write a detailed description of this image"

# Replace with your image file path
image_path = "C:\GenAI\images\photo.jpg"  

# Load and process the image
try:
    image = Image.open(image_path)
except FileNotFoundError:
    print(f"Error: The image file at {image_path} was not found.")
    exit()

import time # Add this import

# Prepare inputs for the model
model_inputs = processor(text=prompt, images=image, return_tensors="pt").to(torch.device('cpu'))

# Generate a response
print("Starting GPU inference...")
start_time = time.time() # Start timer
outputs = model.generate(**model_inputs, max_new_tokens=250, disable_compile=True)
end_time = time.time() # End timer
print(f"GPU inference took: {end_time - start_time:.2f} seconds") # Print duration
 
#decoded = processor.decode(outputs[0], skip_special_tokens=True)
#print(decoded)

# Decode the response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

# Print the response
print(response)

#GPU time - 35.48 seconds
#CPU time - 162.61 seconds