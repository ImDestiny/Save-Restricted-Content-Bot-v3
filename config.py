# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "27866551")
API_HASH = os.getenv("API_HASH", "76057a79a74262e29d6de1e9f41aab0d")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7109878113:AAH_w4p2Kdk95dgrutucTdyKJsJxaQSrC54")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://justsagara:HO51oF0IOvrZV8NB@cluster0.iy1cv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "5437233066").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002693852663")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
