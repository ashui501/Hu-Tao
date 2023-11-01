#MIT License
#Copyright (c) 2023, ©NovaNetworks

import sys
from logging import getLogger

LOGGER = getLogger(__name__)

# Required ENV
try:
    BOT_TOKEN = "6463388462:AAFUfHtXrFxvCTftyS0-qc1yvl34GxSp7BQ" # BOT TOKEN
    API_ID =  "21410165"  # API ID
    API_HASH = "1d762542d9e3d13edb4e68e86994d376" # API HASH
except Exception as e:
    LOGGER.error(f"Looks Like Something Is Missing!! Please Check Variables\n{e}")
    sys.exit(1)


TIMEZONE = "Asia/Kolkata" # YOUR TIME ZONE

COMMAND_HANDLER = ". /".split() # COMMAND HANDLER

SUDO = list({int(x)for x in ("").split()})

SUPPORT_CHAT = "uchiha_clanu" # SUPPORT GROUP (ID OR USERNAME)

LOG_CHANNEL_ID = -1001880512435 #LOG GROUP ID FOR YOUR BOT

OWNER = list({int(x)for x in ("5829077962").split()}) #OWNER ID

DB_URL = "mongodb+srv://DarkLightning2008:Darkdeebu2008@cluster1.ut0l8mm.mongodb.net/?retryWrites=true&w=majority" # MONGO DB URL

SQL_URL = "postgres://mlckhdzh:***@tiny.db.elephantsql.com/mlckhdzh" # ELEPHANT SQL URL
