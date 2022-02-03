import os

class Config(object):
	API_HASH = os.getenv('API_HASH','cd2fb4cdc795334aee3fbbc83da463ce')
	BOT_TOKEN = os.getenv('BOT_TOKEN','5039125485:AAE8MLRVUp2pnqFDQmBihNe2M4mJpsDC4JA')
	API_ID = int(os.getenv('API_ID','2791256'))
	OWNER = int(os.environ.get('OWNER','1916694742'))
	OWNER_USERNAME = os.getenv('OWNER_USERNAME','Rdyry')
	PASSWORD = os.getenv('PASSWORD','Videomergedbott')
	DATABASE_URL=os.environ.get("DATABASE_URL","mongodb+srv://erichdaniken:erichdaniken@cluster0.c13qk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
	FLAG = int(os.getenv('FLAG',1))		# Dont Change this(unfinished feature!!) or else bot will stop working
