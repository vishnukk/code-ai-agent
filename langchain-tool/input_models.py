from pydantic import BaseModel, Field


class CreateFolder(BaseModel):
    folder_path: str = Field(..., description="Name of the folder path to be created")

class CreateFile(BaseModel):
    file_path: str = Field(..., description="Name of the file path to be created")

class UpdateFile(BaseModel):
    file_path: str = Field(..., description="Name of the file path to be updated")
    content: str = Field(..., description="Content of the file to be updated")
