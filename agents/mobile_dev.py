import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def create_mobile_developer():
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    name = "Mobile App Developer"
    instructions = """
    You are an expert mobile app developer. Based on the Manager's input, 
    provide app development ideas, UI suggestions, or code in Flutter, React Native, or Kotlin/Java (if specified).
    Focus on practical mobile solutions.
    """

    return {
        "name": name,
        "instructions": instructions,
        "model": model
    }
