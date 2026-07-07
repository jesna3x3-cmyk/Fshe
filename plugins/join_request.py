from pyrogram import Client
from pyrogram.types import ChatJoinRequest
from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4, LOGGER

# All configured force-sub channel ids (ignores the ones left as 0/unset)
FORCE_SUB_CHANNELS = [
    c for c in (FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4) if c
]


@Client.on_chat_join_request()
async def approve_force_sub_join_request(client: Client, chat_join_request: ChatJoinRequest):
   
    chat_id = chat_join_request.chat.id
    user_id = chat_join_request.from_user.id

    if chat_id not in FORCE_SUB_CHANNELS:
        return

    try:
        await client.approve_chat_join_request(chat_id=chat_id, user_id=user_id)
    except Exception as e:
        LOGGER(__name__).warning(f"Couldn't approve join request for {user_id} in {chat_id}: {e}")


# Jishu Developer
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
