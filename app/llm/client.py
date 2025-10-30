from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from core.config import llm_config


model_client = AzureOpenAIChatCompletionClient(
    azure_deployment=llm_config.azure_deployment,
    model=llm_config.model
)