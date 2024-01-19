from typing import Optional
from bson import ObjectId
from pydantic.main import BaseModel

from app.models.database import OID, BaseDBModel

class Projects_Data(BaseDBModel):
    id: Optional[OID]
    project_url: str
    img_src: str
    title: str
    content: str

class Projects_Category_Data(BaseDBModel):
    id: Optional[OID]
    name: str