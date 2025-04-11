import base64
from io import BytesIO
from PIL import Image
import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

from graph import invoke_our_graph
from st_callable_util_improved import get_streamlit_cb  # Utility function to get a Streamlit callback handler with context



# Set up OpenAI API key from environment variable
openai_api_key = st.secrets["OPENAI_API_KEY"]
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")





# Set the title of the Streamlit app
st.set_page_config(layout="wide")#, page_title="Llama 3 Model Document Q&A"
st.title("LangGraph LLM Chatbot")



# Creating a Session State array to store and show a copy of the conversation to the user.
if "messages" not in st.session_state:
    st.session_state["messages"] = []  # Initialize the messages list in session state

# Initialize images list in session state
if "images" not in st.session_state:
    st.session_state["images"] = []

# Create the Sidebar
sidebar = st.sidebar

# Create the reset button for the chats
clear_chat = sidebar.button("Clear Chat")
if clear_chat:
    st.session_state["messages"] = []
    st.session_state["images"] = []
    st.toast('Conversation Deleted', icon='⚙️')


# Function to encode image to base64
def encode_image(image_file):
    if image_file is None:
        return None
    
    img = Image.open(image_file)
    
    # Convert RGBA to RGB if necessary
    if img.mode == 'RGBA':
        # Create a white background image
        background = Image.new('RGB', img.size, (255, 255, 255))
        # Paste the image on the background using the alpha channel as mask
        background.paste(img, mask=img.split()[3])  # 3 is the alpha channel
        img = background
    
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str


question = st.chat_input(placeholder="Ask Anything.", key=1, accept_file=True, file_type=[".png", ".jpg", ".jpeg"])

if question:

    for message in st.session_state.messages:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.write(message.content)

        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)


    # Add the user question to the session state messages
    st.session_state["messages"].append(HumanMessage(content=question.text))

    # Update the image processing section in your code:
    with st.chat_message("Human"):
        st.write(question.text)
        
        # Process and display uploaded images
        uploaded_images = []
        if question and question.files:
            for file in question.files:
                st.image(file)
                encoded_image = encode_image(file)
                if encoded_image:
                    uploaded_images.append(encoded_image)

    # Invoke the graph with the user question, images, and the callback handler
    with st.chat_message("AI"):
        st_callback = get_streamlit_cb(st.container())
        response = invoke_our_graph(
            st_messages=st.session_state.messages,
            images=uploaded_images if uploaded_images else None,
            callables=[st_callback]
        )
        st.session_state.messages.append(AIMessage(content=response["messages"][-1].content))