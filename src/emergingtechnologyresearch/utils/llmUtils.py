# import os
# from crewai.llm import BaseLLM, LLM
# from typing import (
#     Any,
#     Union,
# )
# from pydantic import InstanceOf

# def getVerbose() -> bool:
#     return True if os.getenv("VERBOSE_OUTPUT") == "TRUE" else False

# def getLlm()->Union[str, InstanceOf[BaseLLM], Any]:
#     if os.getenv('OPENAI_API_KEY'):
#         return LLM(
#             model='openai/gpt-4.1',
#             api_key=os.getenv('OPENAI_API_KEY')
#         )
#     else:
#         return LLM('bedrock/us.amazon.nova-pro-v1:0')

import os
from crewai.llm import BaseLLM, LLM
from typing import (
    Any,
    Union,
)
from pydantic import InstanceOf

def getVerbose() -> bool:
    return True if os.getenv("VERBOSE_OUTPUT") == "TRUE" else False

def getLlm() -> Union[str, InstanceOf[BaseLLM], Any]:
    if os.getenv('OPENAI_API_KEY'):
        return LLM(
            model='openai/gpt-4.1',
            api_key=os.getenv('OPENAI_API_KEY')
        )
    elif os.getenv('OPENROUTER_API_KEY'):
        return LLM(
            model='openrouter/anthropic/claude-sonnet-4',
            api_key=os.getenv('OPENROUTER_API_KEY'),
            base_url='https://openrouter.ai/api/v1',
            max_tokens=2000  # cap it to fit your free credits
        )
    else:
        return LLM('bedrock/us.amazon.nova-pro-v1:0')