from langchain.agents import create_react_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from tools import create_folder_tool, update_file_tool, create_file_tool
from prompts import react_prompt
from llm_models import llm

from dotenv import load_dotenv
import os
load_dotenv(override=True)

import langchain
langchain.debug = os.getenv("DEBUG")

# Define the tools
tools = [
    create_file_tool,
    create_folder_tool,
    update_file_tool
]
conversational_memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True,
)

agent = create_react_agent( # ConversationalAgent
    llm=llm,
    tools=tools,
    prompt=react_prompt,
)
agent_executor = AgentExecutor(agent=agent,
                               tools=tools,
                               memory=conversational_memory,
                               verbose=True,
                               handle_parsing_errors=True)


# Example function to handle user queries
def handle_query(query: str):
    return agent_executor.invoke({"input": query})

# Example usage
if __name__ == "__main__":
    user_query = "Create a project called MyApp with a folder src and a file main.py containing a Python function that prints 'Hello, World!'"
    # user_query = "Create a folder named TestFolder"
    response = handle_query(user_query)
    print("Final Response")
    print(response)
