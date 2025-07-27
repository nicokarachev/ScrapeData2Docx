from telethon.sync import TelegramClient

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'
client = TelegramClient('session_name', api_id, api_hash)

with client:
    for dialog in client.iter_dialogs():
        print(f"{dialog.name} — ID: {dialog.id}")