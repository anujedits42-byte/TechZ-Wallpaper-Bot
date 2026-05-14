from flask import Flask
from threading import Thread
from main import app
import pyrogram, random
from pyrogram import filters, idle
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from main.wall import get_wallpapers, get_unsplash
from main.db_funcs import *

web_app = Flask(__name__)

@web_app.route('/')
def home():
    return """
    <center>
        <h1>⚜️ VIP WALLPAPER BOT ⚜️</h1>
        <p>Bot Is Running Successfully ✅</p>
    </center>
    """

def run_web():
    web_app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

START = """
╭━━━〔 ⚜️ 𝙑𝙄𝙋 𝙒𝘼𝙇𝙇𝙋𝘼𝙋𝙀𝙍 𝙃𝙐𝘽 ⚜️ 〕━━━╮

      ✦ 𝟰𝗞 • 𝗛𝗗 • 𝗔𝗠𝗢𝗟𝗘𝗗 ✦
   ⚡ 𝗙𝗮𝘀𝘁 • 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 • 𝗦𝗺𝗼𝗼𝘁𝗵 ⚡

╰━━━━━━━━━━━━━━━━━━━━━━━━╯

🌐 𝙎𝙤𝙪𝙧𝙘𝙚𝙨:
➤ https://wall.alphacoders.com
➤ https://unsplash.com

━━━━━━━━━━━━━━━━━━━━━━

🎯 𝙁𝙚𝙖𝙩𝙪𝙧𝙚𝙨:
➤ 𝗜𝗻𝘀𝘁𝗮𝗻𝘁 𝗪𝗮𝗹𝗹𝗽𝗮𝗽𝗲𝗿 𝗦𝗲𝗮𝗿𝗰𝗵
➤ 𝗨𝗹𝘁𝗿𝗮 𝗛𝗗 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝘀
➤ 𝗔𝗲𝘀𝘁𝗵𝗲𝘁𝗶𝗰 & 𝗧𝗿𝗲𝗻𝗱𝗶𝗻𝗴 𝗖𝗼𝗹𝗹𝗲𝗰𝘁𝗶𝗼𝗻𝘀
➤ 𝗠𝗼𝗯𝗶𝗹𝗲 + 𝗗𝗲𝘀𝗸𝘁𝗼𝗽 𝗦𝘂𝗽𝗽𝗼𝗿𝘁

━━━━━━━━━━━━━━━━━━━━━━

📌 𝙐𝙨𝙚 /help 𝙩𝙤 𝙫𝙞𝙚𝙬 𝙖𝙡𝙡 𝙘𝙤𝙢𝙢𝙖𝙣𝙙𝙨
💎 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 𝙑𝙄𝙋 𝙀𝙣𝙜𝙞𝙣𝙚
"""

HELP = """
╭━━━〔 ⚡ 𝙑𝙄𝙋 𝙒𝘼𝙇𝙇𝙋𝘼𝙋𝙀𝙍 𝙂𝙐𝙄𝘿𝙀 ⚡ 〕━━━╮

🖼️ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚 𝙈𝙚 ?

━━━━━━━━━━━━━━━━━━━━━━

🔍 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙 𝙃𝘿 𝙒𝙖𝙡𝙡𝙥𝙖𝙥𝙚𝙧𝙨:
➤ `/wall <search>`

🌄 𝙐𝙣𝙨𝙥𝙡𝙖𝙨𝙝 𝙒𝙖𝙡𝙡𝙥𝙖𝙥𝙚𝙧𝙨:
➤ `/unsplash <search>`

━━━━━━━━━━━━━━━━━━━━━━

♻️ 𝙀𝙭𝙖𝙢𝙥𝙡𝙚𝙨:
➤ `/wall anime`
➤ `/wall cyberpunk`
➤ `/unsplash cat`
➤ `/unsplash nature`

━━━━━━━━━━━━━━━━━━━━━━

⚡ 𝙁𝙖𝙨𝙩 • 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 • 𝙃𝘿 𝙍𝙚𝙨𝙪𝙡𝙩𝙨
💎 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 𝙑𝙄𝙋 𝙀𝙣𝙜𝙞𝙣𝙚

╰━━━━━━━━━━━━━━━━━━━━━━━━╯
"""

# Commands
@app.on_message(filters.command("start"))
async def start(bot, message: Message):
  await message.reply_photo("https://telegra.ph/file/dd62dad81f1ace73233d4.jpg",caption=START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Help", callback_data="help_menu")]]))

@app.on_message(filters.command("help"))
async def help(bot, message: Message):
  await message.reply_photo("https://telegra.ph/file/dd62dad81f1ace73233d4.jpg",caption=HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="start_menu")]]))

@app.on_message(filters.command("wall") & filters.incoming & filters.text & ~filters.forwarded & (
  filters.group | filters.private))
async def wall(bot, message: Message):
  try:
    text = message.text.replace("wall","").replace("/","").replace("@wallpaper_anuj_bot","").strip().upper()
    
    if text == "":
      return await message.reply_text(HELP)

    x = await message.reply_text("`🔍 Searching Wallpapers For You...`")  
    wall = await get_wallpapers(text)
      
    if "error" in wall:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @log_ak_bot \n\n`{wall}`")
    
    if "nonee" in wall:
      return await x.edit(f"`❌ Something Went Wrong...`\n\n`{wall}`")
    
    img = random.choice(wall)
      
    await x.edit("`🔄 Got It... Now Sending You`")
    
    id = await save_image(img)

    await message.reply_photo(img,caption="**🏞 Wallpaper By @wallpaper_anuj_bot**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"wall {id}")]]))
    
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In @anujedits76\n\n" + str(e))


@app.on_message(filters.command("unsplash") & filters.incoming & filters.text & ~filters.forwarded & (
  filters.group | filters.private))
async def unsplash(bot, message: Message):
  try:
    text = message.text.replace("unsplash","").replace("/","").replace("@wallpaper_anuj_bot","").strip().upper()
    
    if text == "":
      return await message.reply_text(HELP)

    x = await message.reply_text("`🔍 Searching Wallpapers For You...`")  
    wall = await get_unsplash(text)
      
    if "error" in wall:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @anujedits76 \n\n`{wall}`")
    
    if "nonee" in wall:
      return await x.edit(f"`❌ Something Went Wrong...`\n\n`{wall}`")
    
    wall = random.choice(wall)
      
    await x.edit("`🔄 Got It... Now Sending You`")

    id = await save_image(wall)
    
    await message.reply_photo(wall,caption="**🏞 Wallpaper By @anujedits76**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"wall {id}")]]))
    
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In @anujedits76")
    
# Callbacks
@app.on_callback_query(filters.regex("start_menu"))
async def start_menu(_,query):
  await query.answer()
  await query.message.edit(START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Help", callback_data="help_menu")]]))

@app.on_callback_query(filters.regex("help_menu"))
async def help_menu(_,query):
  await query.answer()
  await query.message.edit(HELP,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Back", callback_data="start_menu")]]))

@app.on_callback_query(filters.regex("wall"))
async def logo_doc(_,query):
  await query.answer()
  try:
    x = await query.message.reply_text("`🔄 Sending You The Wallpaper As File`")
    await query.message.edit_reply_markup(reply_markup=None)
    id = query.data.replace("wall","").strip()
    link = await get_image(id)
    await query.message.reply_document(link,caption="**🏞 Wallpaper By @log_ak_bot**")
    await del_image(id)
  except FloodWait:
    pass
  except Exception as e:
    try:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In @log_ak_bot \n\n`{str(e)}`")
    except:
      return
    
  return await x.delete()


if __name__ == "__main__":

    keep_alive()

    print("==================================")
    print("[INFO]: VIP WALLPAPER BOT STARTED")
    print("==========JOIN @log_ak_bot=========")

    app.run()
    idle()

    print("[INFO]: BOT STOPPED")
