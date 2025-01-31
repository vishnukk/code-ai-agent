from langchain.agents.mrkl.prompt import PREFIX, SUFFIX
from langchain_core.prompts import PromptTemplate

FORMAT_INSTRUCTIONS = """To use a tool, please use the following format:
```
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action. If the action requires **only one input argument**, provide it **as a plain string** without JSON formatting. If the action requires **multiple input arguments**, construct them as a **JSON object**.
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
```
When the requested question is completed and you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```
Thought: I now know the final answer
Final Answer: the final answer to the original input question
```"""

template = "\n\n".join([PREFIX, "{tools}", FORMAT_INSTRUCTIONS, SUFFIX])
react_prompt = PromptTemplate(template=template, input_variables=["input", "chat_history", "tools", "tool_names", "agent_scratchpad"])
print(react_prompt)
