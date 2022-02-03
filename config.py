import os

class Config(object):
	API_HASH = os.getenv('API_HASH','')
	BOT_TOKEN = os.getenv('BOT_TOKEN','')
	API_ID = int(os.getenv('API_ID',''))
	OWNER = int(os.environ.get('OWNER','1940030638'))
	OWNER_USERNAME = os.getenv('OWNER_USERNAME','Dcbotsa')
	PASSWORD = os.getenv('PASSWORD','Videomergedbot')
	DATABASE_URL=os.environ.get("DATABASE_URL","")
	FLAG = int(os.getenv('FLAG',1))		# Dont Change this(unfinished feature!!) or else bot will stop working
