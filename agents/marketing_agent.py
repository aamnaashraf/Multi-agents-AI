import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def create_marketing_agent():
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    name = "Marketing Agent"
    instructions = """
    You are a creative and strategic marketing expert. Based on the Manager's input, 
    provide marketing plans, social media strategies, ad campaign ideas, and ways to promote the product or service.
    Make sure your responses are clear, actionable, and aligned with modern digital marketing trends.
    """

    return {
        "name": name,
        "instructions": instructions,
        "model": model
    }
