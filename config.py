import json

class Config:
    token: str = ""
    application_id: int = 0
class Gemini:
    api_key: str = ""

jsonConfig = open('./config.json')
jsonFile = jsonConfig.read()
jsonFile = json.loads(jsonFile)
config = Config()
gemini = Gemini()

config.token = jsonFile["discord_config"]['bot_token']
config.application_id = jsonFile["discord_config"]["application_id"]
gemini.api_key = jsonFile["gemini"]["api_key"]

TOKEN = config.token
APPLICATION_ID = config.application_id
GENAI_APIKEY = gemini.api_key