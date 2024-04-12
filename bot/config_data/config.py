import os

from environs import Env

env = Env()
env.read_env()
api_token = env('BOT_TOKEN')
