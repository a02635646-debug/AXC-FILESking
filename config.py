import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "8201560790:AAE_WeAmFXMdaS74lywKwbSBT3LdG7rjFew")
API_ID = int(os.environ.get("API_ID", "20232047"))
API_HASH = os.environ.get("API_HASH", "ec4fab92f1d53f4b62db607225d994ad")


OWNER_ID = int(os.environ.get("OWNER_ID", "58973445314"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Hemanthxforyou:9550399779htr@cluster0.e50ndwr.mongodb.net/")
DB_NAME = os.environ.get("DB_NAME", "hemanthxforyou")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID","-1002982919681")

FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1003166051388")

FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "0"))

FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "0"))

FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "0"))

START_PIC = os.environ.get("START_PIC", "https://files.catbox.moe/ufzpkn.jpg")
F_PIC = os.environ.get("FORCE_PIC", "https://files.catbox.moe/ufzpkn.jpg")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


PORT = os.environ.get("PORT", "8050")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[58973445314]
    for x in (os.environ.get("ADMINS", "58973445314").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Sry You can't Able to Message me !\n\n» My Owner 👉 "

START_MSG = os.environ.get("START_MESSAGE", "<b>Hi {first} Friend I am a Advance File Store bot 😈 \n\n I was created by 👉@alonekingstar7 </b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} You must join the given channels ..\n\n 𝐒𝐨 please join and  “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")




ADMINS.append(58973445314)
ADMINS.append(58973445314)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

class Txt(object):
    about = f"""<b>😈 My Name :</b> <a href=''>[AW] File store bot 😈 </a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/tech_freak_tamil'>TFT BOTS</a>
<b>🛡️ :</b> <a href='https://t.me/+NITVxLchQhYzNGZl'>TFT Developer</a>
    
<b>😈 Bot Made By :</b> @ANIMETELUGUDUALTYPE"""


# Tech freak 
# Don't Remove Credit!!!
# Telegram Channel @ANIMETELUGUDUALTYPE
# Developer @ALONEKINGSTAR7
