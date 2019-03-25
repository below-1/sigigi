from environs import Env

env = Env()
env.read_env()

DEBUG = env.bool("DEBUG", default=False)
APP_SECRET = env.str("APP_SECRET")
DATABASE_URI = env.str("DATABASE_URI")