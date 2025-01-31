from langchain_ollama import OllamaLLM
import os

llm = OllamaLLM(model=os.getenv("MODEL"),
                temperature=0,
                # stop=[ "\n    Observation" ]
                )
