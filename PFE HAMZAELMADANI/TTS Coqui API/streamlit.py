import streamlit as st
import requests
import json
import time


flask_url = "http://localhost:5000/addtext"

# Custom CSS to enhance the appearance with updated colors
st.markdown(
    """
    <style>
    .main {
        background-color: #ffffff;  /* White background */
    }
    .title {
        font-family: 'Arial', sans-serif;
        font-size: 36px;
        color: #4CAF50;  /* Keep the title green */
        text-align: center;
        margin-top: 20px;
    }
    .description {
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        color: #000000;  /* Black text */
        text-align: center;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        font-family: 'Arial', sans-serif;
        margin-top: 50px;
        color: #000000;  /* Black text */
    }
    .stTextInput>div>div>input {
        color: #000000 !important;  /* Black text */
    }
    .stTextArea>div>div>textarea {
        color: #000000 !important;  /* Black text */
    }
    .stButton>button {
        background-color: #4CAF50;  /* Green background */
        color: white;  /* White text */
        margin: 0 auto; /* Center align */
        display: block; /* Display as block element */
    }
    .logo-container {
        display: flex;
        justify-content: center;
        margin-bottom: 20px; /* Add margin bottom for spacing */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# State management
if "step" not in st.session_state:
    st.session_state.step = 1

# Function to display a spinner during processing
def show_spinner():
    with st.spinner('Generating audio...'):
        time.sleep(0)  # Adjusted to a realistic delay

# Display the logo in the sidebar with a width of 120
st.sidebar.image("static/images/logo.png", width=120)

# Set the title and description of the Streamlit app
st.markdown('<div class="title">Text-to-Speech Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Follow the steps to generate speech from text.</div>', unsafe_allow_html=True)

# Combined Step: User enters the text and selects the audio file
st.markdown("### Enter Text and Select Audio Input")
text = st.text_area("Enter text", height=200)
audio_input = st.selectbox("Select an audio input", options=["audio1.mp3", "audio2.mp3", "audio3.mp3", "audio4.mp3"])

if st.button("Submit"):
    if text.strip() == "":
        st.error("Please enter some text.")
    else:
        st.session_state.text = text
        st.session_state.audio_input = audio_input
        
        # Show a spinner while waiting for the response
        show_spinner()
        
        # Send a POST request with the text and audio input as JSON data
        try:
            response = requests.post(flask_url, json={"text": st.session_state.text, "audio_file": st.session_state.audio_input.replace('.mp3', '')})

            # If the request was successful, display the audio URL and the transformed text
            if response.status_code == 200:
                data = response.json()
                audio_url = data["audio_url"]
                transformed_text = data["transformed_text"]
                
                st.success("Audio generated successfully!")
                st.write(f"### Transformed Text\n{transformed_text}")
                
                # Display the audio player
                st.audio(audio_url)
            else:
                st.error(f"An error occurred: {response.json().get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred while connecting to the server: {e}")

# Add a footer
st.markdown("""
<div class="footer">
    Made with love by <a href="https://lematin.ma/" target="_blank">GLM SI Digital</a>
</div>
""", unsafe_allow_html=True)