import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()  # Load environment variables from .env file

def create_manager():
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")  # Use API key from env
    )

    name = "Manager"

    instructions = """You are the project manager of a smart AI team. Your job is to:

1. Analyze the user's request.
2. Decide which agent should handle it.
   - Choose one: 'web', 'mobile', or 'marketing'
3. Return your decision in the following format:
   
   Agent: <agent name>
   Task: <task to be done>

4. If the request doesn't match any category, respond with:
   Agent: none
   Task: Sorry, we don’t have an agent for this task.

Be short, clear, and only include the 'Agent' and 'Task' fields in your response.
"""

    return {
        "name": name,
        "instructions": instructions,
        "model": model
    }
