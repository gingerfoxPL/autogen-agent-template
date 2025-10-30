from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()

class LlmConfig(BaseSettings):
    azure_deployment: str = "azure_deployment_name"
    model: str = "gpt-4.1-mini-2025-04-14"

llm_config = LlmConfig()
