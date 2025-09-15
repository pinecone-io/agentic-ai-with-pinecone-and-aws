import chainlit as cl
from rag_pipeline import RAGPipeline
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

# Initialize the RAG pipeline
@cl.cache
def get_rag_pipeline():
    return RAGPipeline()

# Sample questions for users to select from
SAMPLE_QUESTIONS = [
    "What is the capital of France?",
    "Which company did Rod Canion cofound?",
    "What is the revenue of Compaq in 2001?",
    "What is 2001 revenue of the company Rod Canion cofound?",
    "Changes in Compaq's product offerings and their impacts on sales"
]

@cl.on_chat_start
async def start_chat():
    """Initialize the chat session and send welcome message with sample questions."""
    # Get the RAG pipeline instance
    rag_pipeline = get_rag_pipeline()
    
    # Store the pipeline in the user session
    cl.user_session.set("rag_pipeline", rag_pipeline)
    
    # Create action buttons for sample questions
    actions = [
        cl.Action(name=f"question_{i}", payload={"question": question}, label=question) 
        for i, question in enumerate(SAMPLE_QUESTIONS)
    ]
    
    # Send welcome message with sample questions
    await cl.Message(
        content="🤖 Welcome to ChatterPine 2000!\n\nYou can ask me questions about various topics, or select from the sample questions below:",
        actions=actions
    ).send()

# Create individual action callbacks for each sample question
@cl.action_callback("question_0")
@cl.action_callback("question_1")
@cl.action_callback("question_2")
@cl.action_callback("question_3")
@cl.action_callback("question_4")
async def on_action(action: cl.Action):
    """Handle when a user clicks on a sample question."""
    # Process the selected question as if it were a user message
    question = action.payload["question"]
    
    await process_user_message(question)

@cl.on_message
async def on_message(message: cl.Message):
    """Handle user messages and stream responses from the RAG pipeline."""
    await process_user_message(message.content)

async def process_user_message(user_input: str):
    """Process user input and stream the response from the RAG pipeline."""
    # Get the RAG pipeline from the user session
    rag_pipeline = cl.user_session.get("rag_pipeline")
    
    if not rag_pipeline:
        await cl.Message(content="Error: RAG pipeline not initialized. Please refresh the page.").send()
        return
    
    # Create a message placeholder for streaming
    msg = cl.Message(content="")
    await msg.send()
    
    try:
        # Get the streaming response from the RAG pipeline
        # Note: run_agent returns a generator, not an async generator
        response_stream = rag_pipeline.run_agent(user_input)
        
        # Stream each chunk of the response
        for chunk in response_stream:
            await msg.stream_token(chunk)
        
        # Update the message to finalize it
        await msg.update()
        
    except Exception as e:
        # Handle any errors that occur during processing
        error_msg = f"An error occurred while processing your request: {str(e)}"
        await msg.stream_token(error_msg)
        await msg.update()
        print(f"Error in process_user_message: {e}")

# Optional: Add a callback for when the chat ends
@cl.on_chat_end
async def on_chat_end():
    """Clean up when the chat session ends."""
    print("Chat session ended")

if __name__ == "__main__":
    # This allows running the app directly with: python chainlit_app.py
    import chainlit as cl
    cl.run()
