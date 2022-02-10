
from typing import Optional

from pydantic import BaseModel


class FileModel(BaseModel):
    gid: str
    filename: str
    separator: Optional[str] = None
    type_file: str = 'csv'


class WSModel(BaseModel):
    gid: str
    url: str
    status_code: Optional[int] = None


class SQLModel(BaseModel):
    gid: str
    user: str
    password: str
    db: str
    host: str
    port: Optional[int] = None
    driver: str
    resource: str

