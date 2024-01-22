from typing import Union
import json
from bson import ObjectId
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from app.models.database_models import OID
from app.models.blog_models import Blog_Post_Category_Data, Blog_Post_Data
from app.services.database_manager import DatabaseManagerInterface, get_database

menu_router = APIRouter(prefix='/menu_items')
collection_name = 'skills'

#--------#
# Menus #
#--------#

# # CREATE

# # READ
@menu_router.get("/all")
async def all(database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Blog_Post_Category_Data]:
    menu = await database_manager_service.all('menu_items')
    return menu

@menu_router.get("/of_category/{id_category}")
async def all_skills_of_category(id_category: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)): #list[Blog_Post_Category_Data]:
    menu = await database_manager_service.all('menu_items', id_category)
    return menu

@menu_router.get('/read/{id_menu_item}')
async def one(id_menu_item: str, database_manager_service: DatabaseManagerInterface = Depends(get_database)):
    menu_item = await database_manager_service.one_item(id_menu_item, 'menu_items')
    return menu_item

# # UPDATE

# # DELETE