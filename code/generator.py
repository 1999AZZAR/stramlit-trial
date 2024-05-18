# generative_model.py
import google.generativeai as genai
import random
import streamlit as st

class GenerativeModel:
    def __init__(self):

        # Read the API key from the text file
        with open('api_key.txt', 'r') as file:
            text_key = file.read()

        # Configure the model
        self.generation_config = {
            "temperature": 0.75,        # Controls the randomness of generated responses
            "top_p": 0.65,              # Top-p (nucleus) sampling parameter
            "top_k": 35,                # Top-k filtering parameter for token sampling
            "max_output_tokens": 2048,  # Maximum number of tokens in the generated response
            'stop_sequences': [],       # Sequences to stop generation at
        }

        # Safety settings
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
        ]

        # Initialize the model with the retrieved API key
        genai.configure(api_key=text_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            generation_config=self.generation_config,
            safety_settings=self.safety_settings,
        )

    def read_prompt_parts_from_file(self, file_path, user_input_text=''):
        with open(file_path, 'r') as file:
            prompt_parts = file.read()
        if user_input_text:
            prompt_parts = prompt_parts.replace('{user_input_text}', user_input_text)
        return prompt_parts

    def generate_response(self, user_input_text):
        # self.configure_api_key()
        prompt_parts = self.read_prompt_parts_from_file('/mount/src/streamlit_promptgen/code/instruction/examples1.txt', user_input_text)
        response = self.model.generate_content(prompt_parts)
        return response.text

    def generate_random(self):
        # self.configure_api_key()
        prompt_parts = self.read_prompt_parts_from_file('/mount/src/streamlit_promptgen/code/instruction/examples2.txt')
        response = self.model.generate_content(prompt_parts)
        return response.text

    def generate_imgdescription(self, user_input_image):
        # self.configure_api_key()
        with open('/mount/src/streamlit_promptgen/code/instruction/image_styles.txt', 'r') as file:
            image_styles = [line.strip() for line in file.readlines()]

        chosen_styles = random.sample(image_styles, k=3)
        prompt_parts = [
            " ",
            f"Input: Use the following styles ({', '.join(chosen_styles)}) to create a compelling image description about {user_input_image}. if possible Incorporate elements all of those styles into your description. Your narrative should be between 200 to 400 characters, evoking a vivid and imaginative scene. Start your description with the word 'imagine,' e.g., 'imagine a hyperrealistic portrait in a dreamlike landscape...'",
            "Output: ",
        ]
        response = self.model.generate_content(prompt_parts)
        return response.text

    def generate_vrandom(self):
        # self.configure_api_key()
        with open('/mount/src/streamlit_promptgen/code/instruction/image_styles.txt', 'r') as file:
            image_styles = [line.strip() for line in file.readlines()]

        chosen_styles = random.sample(image_styles, k=3)
        prompt_parts = [
            " ",
            f"Input: Use the following styles ({', '.join(chosen_styles)}) to create a compelling image description. if possible Incorporate elements all of those styles into your description. Your narrative should be between 200 to 1000 characters, evoking a vivid and imaginative scene. Start your description with the word 'imagine,' e.g., 'imagine a hyperrealistic portrait in a dreamlike landscape...'",
            "Output: ",
        ]
        response = self.model.generate_content(prompt_parts)
        return response.text

    def generate_content(self, prompt_parts):
        response = self.model.generate_content(prompt_parts)
        return response.text

    def reverse_image(self, image_data):
        try:
            with open('/mount/src/streamlit_promptgen/code/instruction/image_styles.txt', 'r') as file:
                image_styles = [line.strip() for line in file.readlines()]

            prompt_parts = [
                "\nPlease provide a detailed description, written in proper English, to recreate this image in 250 to 500 words. Include information about the style, mood, lighting, and other important details. Ensure your sentences are complete and free from spelling and grammar errors:",
                {"mime_type": "image/jpeg", "data": image_data},
                f"\nPlease select and use up to four different artistic styles from the following list: \n{', '.join(image_styles)}\nYou can choose the same style multiple times if desired.",
                "Try to make your description as similar as possible to the original image, just like an audio describer would. Remember to begin your description with the word 'imagine.' For example, 'imagine a red-hooded woman in the forest...'",
            ]

            response_text = self.generate_content(prompt_parts)
            return response_text

        except Exception as e:
            return f"Error: {str(e)}"
