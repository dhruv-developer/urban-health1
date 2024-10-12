import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define function to generate image from text prompt
def generate_image(prompt, n=1, size="1024x1024"):
    try:
        # Call the OpenAI API for DALL-E
        response = openai.Image.create(
            prompt=prompt,
            n=n,  # Number of images
            size=size  # Image size
        )
        return response['data']
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

# Define prompts for Urban Health solutions
prompts = [
    "Create an eco-friendly urban park where nature, healthcare technology, and community blend seamlessly—featuring greenery, healthcare kiosks, clean energy, and futuristic buildings.",
    "Design a futuristic city with zero pollution, wide public spaces for exercise, and areas optimized for mental well-being, surrounded by clean air and green spaces.",
    "Visualize a smart city where drones deliver medical supplies, green rooftops reduce pollution, and digital healthcare kiosks provide instant diagnosis for citizens.",
    "Create a public space designed for mental health, featuring quiet zones, nature therapy areas, and communal gardens, all within an urban environment.",
    "Imagine an urban street where self-driving electric ambulances, AI-controlled traffic systems, and health-monitoring streetlights work together to ensure a healthy environment.",
    "Depict a future city where all buildings are covered with vertical gardens, and air-purifying towers monitor pollution levels to maintain clean air for everyone.",
    "Showcase a futuristic subway station where biometric scanners check vital signs, and interactive walls provide real-time health data, guiding passengers to the nearest healthcare facility if needed.",
    "Design a healthcare-focused marketplace where urban citizens access local organic food, on-site health checks, and eco-friendly products, all within a vibrant, tech-driven environment.",
    "Illustrate a community of eco-friendly homes where solar-powered healthcare centers, smart fitness trackers, and AI doctors provide continuous health care to residents.",
    "Generate an image of a futuristic urban playground with smart exercise stations, health monitoring wearables for children, and green zones designed to boost physical and mental well-being.",
    "Depict a clean, futuristic hospital in the heart of a bustling city, with robot nurses, automated patient care, and AI-assisted surgeries taking place in an eco-friendly, tech-driven environment.",
    "Imagine a futuristic bike-sharing system where bikes are equipped with air quality sensors, health tracking devices, and personalized fitness recommendations for riders."
]

# Generate images from the prompts
for i, prompt in enumerate(prompts):
    print(f"Generating image for prompt {i+1}: {prompt}")
    images = generate_image(prompt)

    if images:
        for img in images:
            print(f"Image URL for prompt {i+1}: {img['url']}")
