import chainlit as cl

from agents.manager import create_manager
from agents.web_dev import create_web_developer
from agents.mobile_dev import create_mobile_developer
from agents.marketing_agent import create_marketing_agent


@cl.on_chat_start
async def start():
    # Create all agents
    manager = create_manager()
    web_dev = create_web_developer()
    mobile_dev = create_mobile_developer()
    marketing = create_marketing_agent()

    # Store agents in user session for access later
    cl.user_session.set("agents", [manager, web_dev, mobile_dev, marketing])

    await cl.Message(content="👋 Welcome! You are now chatting with a multi-agent AI team.\n\nAsk a question and let the Manager decide who should respond.").send()


@cl.on_message
async def handle_message(message: cl.Message):
    agents = cl.user_session.get("agents")

    if not agents:
        await cl.Message(content="⚠️ Agents not initialized!").send()
        return

    manager = agents[0]
    team = agents[1:]

    # Let manager decide what to do
    manager_model = manager["model"]
    manager_input = f"""{manager['instructions']}

User message: {message.content}

Decide clearly which agent should handle this (choose one: web, mobile, marketing), and what the task is."""
    
    manager_response = manager_model.invoke(manager_input)
    await cl.Message(content=f"📋 **Manager:** {manager_response.content}").send()

    # Match response to known agents
    task_instruction = manager_response.content.lower()
    matched_agent = None

    for agent in team:
        agent_name_key = agent["name"].lower().split()[0]
        if agent_name_key in task_instruction:
            matched_agent = agent
            break

    if matched_agent:
        agent_model = matched_agent["model"]
        agent_input = f"{matched_agent['instructions']}\n\nTask: {task_instruction}"
        agent_response = agent_model.invoke(agent_input)

        await cl.Message(content=f"🤖 **{matched_agent['name']}:** {agent_response.content}").send()
    else:
        await cl.Message(content="❗ *Sorry, we don’t have an agent for that task.*").send()


