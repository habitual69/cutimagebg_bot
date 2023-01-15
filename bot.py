import pyrogram
import os
from rembg import remove
import io
from hide import *
from PIL import Image


# Create a new client
app = pyrogram.Client("cutimagebg_bot", api_id=YOUR_API_ID, api_hash=YOUR_API_HASH, bot_token=BOT_TOKEN)


@app.on_message(pyrogram.filters.command("start"))
async def start(app,message):
   await message.reply_text("""
Hi! I am a <b>Background 🖼️ Remover</b> can remove the background from images. 
Just send an image and let the <b>AI</b> do its magic.""")


@app.on_message()
async def handle_messages(app, message):
    if message.photo:
        # Download the image
        image_file = message.photo.file_id
        image_path = await app.download_media(image_file)
        #open the image file
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
            new_image = remove(image_bytes)
        #save the file as valid image and send it
        image = Image.open(io.BytesIO(new_image))
        with io.BytesIO() as f:
            image.save(f, format='png')
            f.seek(0)
            await message.reply_photo(f)
        # remove the image after it has been processed and sent
        os.remove(image_path)

# Start the bot
app.run()
