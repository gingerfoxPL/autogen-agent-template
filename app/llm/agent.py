from autogen_agentchat.agents import AssistantAgent
from llm.client import model_client
# from utils.tools import *
from utils.prompts import SYSTEM_PROMPT


assistant = AssistantAgent(
    name="assistant",
    model_client=model_client,
    system_message=SYSTEM_PROMPT,
    # tools=[],
    model_client_stream=True,  
    reflect_on_tool_use=True, 
)