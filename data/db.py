from config import DB_URL
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from typing import Dict, List, Union

_mongo_async_ = _mongo_client_(DB_URL)
mongodb = _mongo_async_.BorzTagger

chatsdb = mongodb.chats
usersdb = mongodb.users
cagirmadb = mongodb.cagirma

# Users

async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_served_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})


# Served Chats

async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def get_served_chats() -> list:
    chats_list = []
    async for chat in chatsdb.find({"chat_id": {"$gt": 0}}):
        chats_list.append(chat)
    return chats_list


async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})
# Axtaris

async def get_cagirma() -> int:
    chat_id = 98324
    mode = await cagirmadb.find_one({"chat_id": chat_id})
    if not mode:
        return 0
    return mode["mode"]


async def set_cagirma(mode: int):
    chat_id = 98324
    cagirma = await cagirmadb.find_one({"chat_id": chat_id})
    if cagirma:
        mode = cagirma["mode"] + mode
    return await cagirmadb.update_one(
        {"chat_id": chat_id}, {"$set": {"mode": mode}}, upsert=True
    )
