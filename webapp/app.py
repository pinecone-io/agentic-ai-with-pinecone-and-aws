import streamlit as st
from datetime import datetime
from rag_pipeline import RAGPipeline
from dotenv import load_dotenv

load_dotenv()
rag_pipeline = RAGPipeline()

# Page configuration
st.set_page_config(
    page_title="Chat Interface",
    page_icon="💬",
    layout="wide"
)

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# App title
st.title("💬 Chat Interface")
st.markdown("---")

# Display conversation history
if st.session_state.messages:
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
            st.caption(f"Sent at: {message['timestamp']}")

# Chat input
st.markdown("---")
st.subheader("Chat with the data")

# Use a form to automatically clear the input after submission
with st.form(key="message_form", clear_on_submit=True):
    user_input = st.text_area(
        "What questions do you have about the data?",
        key="user_input"
    )
    
    # Submit button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        submit_button = st.form_submit_button("Send Message", type="primary", use_container_width=True)
    
    # Handle message submission
    if submit_button and user_input.strip():
        # Add user message to history
        user_message = {
            "role": "user",
            "content": user_input.strip(),
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        st.session_state.messages.append(user_message)
        
        agent_message = rag_pipeline.run_agent(user_input.strip())
        st.session_state.messages.append(agent_message)
        
        # Rerun to update the display
        st.rerun()

# Sidebar with additional options
with st.sidebar:
    st.header("Chat Options")
    
    # Clear conversation button
    if st.button("Clear Conversation", type="secondary"):
        st.session_state.messages = []
        st.rerun()

# Footer
st.markdown("---")
st.markdown("*Built with 💙 at [Pinecone](https://pinecone.io)*")
