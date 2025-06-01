import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def create_web_developer():
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    name = "Web Developer"
    instructions = """
    You are a highly skilled web developer. Based on the Manager's task, 
    provide website-related code (HTML, CSS, JavaScript), framework suggestions (React, Next.js), 
    or UI/UX improvements.
    """

    return {
        "name": name,
        "instructions": instructions,
        "model": model
    }
