"""
 1. Для получения GigaChat API: авторизируйтесь на сайте https://developers.sber.ru/docs/ru/gigachat/models
 и сгенерируйте свой Authorization Key
 2. Для получения BOT API: Сгенерируйте API для модели https://huggingface.co/intfloat/multilingual-e5-large
"""


BOT_API = "YOUR_BOT_API"
GigaChat_API = "YOUR_GIGACHAT_API"

RATINGS_FILE = "Data/ratings.csv" 
ADDRESSES_FILE = "Data/user_addresses.csv"

CLASSIFICATOR_NAME = "intfloat/multilingual-e5-large"
GIGACHAT_VERSION = "GigaChat-Max" # GigaChat (lite), GigaChat-Pro (pro), GigaChat-Max (max)