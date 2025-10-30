from core.logging import setup_logging
from llm.agent import assistant
from ui.chanilit_ui import run_chainlit_ui


# setup_logging()

run_chainlit_ui(assistant)
