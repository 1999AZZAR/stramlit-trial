# Prompt Sanctuary (streamlit)

Welcome to Prompt Sanctuary, a versatile tool for generating prompts for both text and image inputs. This README provides detailed instructions on how to set up and run the application.

## Table of Contents

- [Prompt Sanctuary (streamlit)](#prompt-sanctuary-streamlit)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [Structure of the Code](#structure-of-the-code)
  - [Credits](#credits)
  - [See on streamlit](#see-on-streamlit)

## Introduction

Prompt Sanctuary is a Streamlit-based application that leverages AI-powered generative models to create prompts based on user input. It offers two main functionalities: generating text prompts and generating image prompts. Users can either input their custom text or upload an image to generate prompts tailored to their needs. Additionally, there's an option to generate random prompts for both text and image inputs, adding an element of surprise and creativity.

## Installation

To set up Prompt Sanctuary on your local machine, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/1999AZZAR/streamlit_promptgen
   ```

2. Navigate to the project directory:

   ```bash
   cd streamlit_promptgen
   ```

3. Create a virtual env (optional)

    ```bash
    python -m venv myenv
    ```

4. Activate the virtual env (if u use one)

   ```bash
   source myenv/bin/activate
    ```

5. Navigate to the actual code directory:

   ```bash
   cd code
   ```

6. Install the required dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

After completing the installation steps, you can run the application locally. Execute the following command from the project directory:

```bash
streamlit run app.py
```

This command will start a local server, and the application will be accessible through your web browser at `http://localhost:8501`.

## Structure of the Code

The codebase for Prompt Sanctuary is organized as follows:

```text
streamlit/
└── code/
    ├── img/
    │   ├── favicon.ico
    │   └── logo.png
    ├── instruction/
    │   ├── examples1.txt
    │   ├── examples2.txt
    │   └── image_styles.txt
    ├── app.py
    └── generator.py
```

- `img/`: Directory containing the application's favicon and logo images.
- `instruction/`: Directory containing text files with instructions or examples.
- `app.py`: The main Python script containing the Streamlit application code.
- `generator.py`: Python module implementing the GenerativeModel class for generating prompts.

## Credits

Prompt Sanctuary is powered by Streamlit and leverages AI models for prompt generation. Special thanks to the developers of Streamlit and the underlying generative models for enabling this project.

## See on streamlit

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://prompt-sanctuary.streamlit.app/)
