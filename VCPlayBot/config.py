import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAIms0cw8rIbhZKJtlTYVJ_D-pSylWTEcB1vmZwl_oT-wWNAo9iESGogamoZhOMfMmPQM2153YZ-pA3Vq0k2CqjLliMhrAV97IlKx1Wym4n6TyE7HsFotKJ5F6n3z1U44T6ooSFSTvP9O61xDqwjGePr8i11ICyZM4qEjMHyPn2_EFQxONte_0VN01gRreHmXlFMNTgz46xT0c2piIQ5oZ5VrEljFyELrNz97wf-39GH2L3YXIsMYULDksbpK3V-9mhiDl52YrM_UlK3g_mXQYQbVxFJ4Me1qI66AjAjXTKa8FtMdnj4maRuXAvBxlNT963bfTxFwovFkL9l8kZPSF6AAAAAT2ZUI8A")
BOT_TOKEN = getenv("BOT_TOKEN", "5763437916:AAFCtywbrYAETLnoYJte5XCRqzKtASZ2erw")
BOT_NAME = getenv("BOT_NAME", "test")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LaylaBots")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("API_ID", "11054750"))
API_HASH = getenv("API_HASH", "f094d72a20b21659cc0531f7e901f698")
BOT_USERNAME = getenv("BOT_USERNAME", "testmasccbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Dead0XD")
OWNER_NAME = getenv("OWNER_NAME", "HEROGAMERS1")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AwesomeSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/kittybotmah/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "700"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "CTXWJS-WLXBXX-IWPXPC-MHIDWF-ARQ")
PMPERMIT = getenv("PMPERMIT", "EANABLE")
LOG_GRP = getenv("LOG_GRP", "-1001380393446")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5328425103").split()))
