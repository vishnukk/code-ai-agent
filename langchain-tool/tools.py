from typing import Union

from pydantic import BaseModel
import json
from langchain.agents import Tool
from input_models import CreateFolder, CreateFile, UpdateFile


def create_folder(folder_path: str) -> str:
    """
    Creates a folder at the specified path if it does not already exist.

    Args:
        folder_path (str): Name of the folder path to be created

    Returns:
         Success message if the folder is created, or a message indicating it already exists.
    """
    import os
    if os.path.exists(folder_path):
        return f"Folder {folder_path} already exists."
    else:
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder {folder_path} created successfully."

# Tool: Create File

def create_file(file_path: str) -> str:
    """
    Creates a new empty file at the specified path.

    Args:
        file_path (str): Name of the file path to be created

    Returns:
        Returns a success message if the file is created successfully.
    """
    with open(file_path, "w") as file:
        file.write("")
    return f"File {file_path} created successfully."

# Tool: Update File

def update_file(file_path: str=None, content: str=None) -> str:
    """
    Updates the specified file path with new content. Overwrites existing content.

    Args:
        file_path (str): Name of the file path to be updated
        content (str): Content of the file to be updated

    Returns:
        Returns a success message if the file is updated successfully.
    """
    if file_path is None or content is None:
        raise ValueError("Both file_path and content are required.")

    with open(file_path, "w") as file:
        file.write(content)
    return f"File {file_path} updated with new content."

def parse_tool_input(input_value: Union[str, dict], tool_schema: BaseModel):
    """Parses tool input, converting JSON strings to dicts when needed."""

    # If input is already a dict, return as is
    if isinstance(input_value, dict):
        return input_value

        # Try parsing JSON if the input is a string
    try:
        parsed_json = json.loads(input_value)
        if isinstance(parsed_json, dict):
            return parsed_json  # Return as dictionary if valid JSON
    except json.JSONDecodeError:
        pass  # Not valid JSON, treat as plain value

    # If the tool expects a single parameter, wrap it correctly
    expected_fields = list(tool_schema.__annotations__.keys())
    if len(expected_fields) == 1:
        return {expected_fields[0]: input_value}

    raise ValueError(f"Unexpected input format: {input_value}")


create_folder_tool = Tool(
    name="create_folder",
    func=lambda input: create_folder(**parse_tool_input(input, CreateFolder)),
    description="Creates a folder with the given name",
)

create_file_tool =  Tool(
    name="create_file",
    func=lambda input: create_file_tool(**parse_tool_input(input, CreateFile)),
    description="Use this tool to create a file with empty content."
)

update_file_tool = Tool(
    name="update_file",
    func= lambda input: update_file_tool(**parse_tool_input(input, UpdateFile)),
    description="Updates a file. Accepts 2 input parameters. file_path and content. "
)
