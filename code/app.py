import streamlit as st
import pyperclip
from generator import GenerativeModel  # Import the GenerativeModel class

# Set the page configuration
st.set_page_config(page_title="Prompt Sanctuary", page_icon="./img/favicon.ico")

# Create an instance of the GenerativeModel class
gen_model = GenerativeModel()

def main():
    st.sidebar.image("./img/logo.png", use_column_width=False, width=200)
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Text Prompt", "Image Prompt"))

    with st.sidebar:
        gemini_api_key = st.sidebar.text_input("Gemini API Key", key="chatbot_api_key", type="password")
        if gemini_api_key:
            gen_model.set_api_key(gemini_api_key)
        else:
            st.sidebar.info("Please enter your Gemini API key to continue.")
        st.markdown("[Get a gemini API key](https://aistudio.google.com/app/apikey)")
        st.markdown("[View the source code](https://github.com/1999AZZAR/streamlit_promptgen)")
        st.markdown("powered by :")
        st.markdown("[![gemini](https://www.gstatic.com/aistudio/ai_studio_favicon_32x32.svg)](https://aistudio.google.com)")

    if page == "Text Prompt":
        display_txt()
    elif page == "Image Prompt":
        display_img()

def display_txt():
    st.title("Prompt generator (text)")
    generated_prompt = None   # Initialize generated_prompt
    prompt_generated = False  # Initialize prompt_generated flag

    st.markdown(
        """
        <div style="text-align: justify">
        Here, you have the flexibility to create a customized prompt tailored to your specific requirements. 
        Alternatively, you can opt to use the random feature, which will generate a prompt for you—ensuring not 
        only variety but also an element of surprise and enjoyment in the process. Whether you have a specific 
        idea in mind or are seeking inspiration, the Prompt Generator is designed to accommodate both your 
        structured and spontaneous prompt needs.
        </div>
        """,
        unsafe_allow_html=True  # Allow HTML tags to style the markdown
    )
    st.subheader("Generate Text Prompt")
    user_input_text = st.text_input("Input:", "write a python code")
    
    # Use columns layout to display buttons side by side
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Generate", key=hash(user_input_text)):
            if not st.session_state.get("chatbot_api_key"):
                st.info("Please add your Gemini API key to continue.")
                st.stop()
            generated_prompt = gen_model.generate_response(user_input_text)
            prompt_generated = True
    
    with col2:
        if st.button("Random", key=hash(f"random")):
            if not st.session_state.get("chatbot_api_key"):
                st.info("Please add your Gemini API key to continue.")
                st.stop()
            generated_prompt = gen_model.generate_random()
            prompt_generated = True
        
    if generated_prompt is not None:
        st.write(f"{generated_prompt}")
        if prompt_generated and st.button("Copy Prompt"):
            pyperclip.copy(generated_prompt)
            st.success("Prompt copied to clipboard!")

def display_img():
    st.title("Prompt generator (img)")
    generated_prompt = None  # Initialize generated_prompt
    prompt_generated = False  # Initialize prompt_generated flag
    txt = False
    img = False
    rdm = False

    st.markdown(
        """
        <div style="text-align: justify">
        Here, you have the flexibility to create a customized prompt tailored to your specific requirements. 
        Alternatively, you can opt to use the random feature, which will generate a prompt for you—ensuring not 
        only variety but also an element of surprise and enjoyment in the process. Whether you have a specific 
        idea in mind or are seeking inspiration, the Prompt Generator is designed to accommodate both your 
        structured and spontaneous prompt needs.
        </div>
        """,
        unsafe_allow_html=True  # Allow HTML tags to style the markdown
    )
    st.subheader("Generate Image Prompt")
    prompt_option = st.radio("Generate from option:", ("Text", "File", "Random"))
    if prompt_option == "Text":
        txt = True
        img = False
        rdm = False
        user_input_image = st.text_input("Input:", "whale on the desert")
    elif prompt_option == "File":
        txt = False
        img = True
        rdm = False
        image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
    elif prompt_option == "Random":
        txt = False
        img = False
        rdm = True
    
    if txt:
        if st.button("Generate", key=hash(user_input_image)):
            if not st.session_state.get("chatbot_api_key"):
                st.info("Please add your Gemini API key to continue.")
                st.stop()
            generated_prompt = gen_model.generate_imgdescription(user_input_image)
    elif img:
        if st.button("Generate", key=hash(str(image_file))):
            if not st.session_state.get("chatbot_api_key"):
                st.info("Please add your Gemini API key to continue.")
                st.stop()
            generated_prompt = gen_model.reverse_image(image_file)
    elif rdm:
        if st.button("Generate", key=hash(f"vrandom")):
            if not st.session_state.get("chatbot_api_key"):
                st.info("Please add your Gemini API key to continue.")
                st.stop()
            generated_prompt = gen_model.generate_vrandom()

    if generated_prompt is not None:
        st.write(f"{generated_prompt}")
        if prompt_generated and st.button("Copy Prompt"):
            pyperclip.copy(generated_prompt)
            st.success("Prompt copied to clipboard!")

if __name__ == "__main__":
    main()
