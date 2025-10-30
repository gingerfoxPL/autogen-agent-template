import os
import chainlit as cl
from autogen_agentchat.base import Response
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import ModelClientStreamingChunkEvent, ToolCallRequestEvent, ToolCallExecutionEvent, TextMessage
from autogen_core import CancellationToken

from services.app_monitor import create_record
from core.constants import EXPORTS_FOLDER_PATH

def run_chainlit_ui(assistant: AssistantAgent): 

    @cl.on_chat_start
    async def start_chat() -> None:
        cl.user_session.set("prompt_history","")
        cl.user_session.set("agent",assistant)
        await cl.Message(content="🤖 Hi! How can I help you today? 🚀").send()

    @cl.on_message
    async def chat(message: cl.Message) -> None:
        agent = cl.user_session.get("agent")
        response = cl.Message(content="")
        async for msg in agent.on_messages_stream(
            messages=[TextMessage(content=message.content, source="user")],
            cancellation_token=CancellationToken()
        ):
            if isinstance(msg, ModelClientStreamingChunkEvent):
                await response.stream_token(msg.content)

            elif isinstance(msg, Response):
                await response.send()

            elif isinstance(msg, ToolCallRequestEvent):
                tool_name = msg.content[0].name
                await response.stream_token(f"Wait for the result of {tool_name} function.\n")
                
            elif isinstance(msg, ToolCallExecutionEvent):
                try:
                    respones = create_record(project_id=1)
                except Exception as e:
                    logging.error(msg=f"App Monitor server not available: {e}")
                tool_name, tool_result = msg.content[0].name, msg.content[0].content
                if tool_result != "None" and tool_result in os.listdir(EXPORTS_FOLDER_PATH):
                    file_name = tool_result.split(" ")[1]
                    file_path = f"{EXPORTS_FOLDER_PATH}/{tool_result}"
                    element = cl.File(
                        name=file_name,
                        path=file_path,
                        display="inline"
                    )
                    tool_response = cl.Message(content="Result:", elements=[element])
                    await tool_response.send()

