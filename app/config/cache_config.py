from dotenv import load_dotenv
from pathlib import Path
import os
import redis

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

# redis_client = redis.StrictRedis(
#     host=os.environ.get('REDIS_HOST'),
#     port=int(os.environ.get('REDIS_PORT')),
#     db=int(os.environ.get('REDIS_DB')),
#     password=os.environ.get('REDIS_PASSWORD'),
#     decode_responses=True
# )

cache_config={
    'CACHE_TYPE': 'RedisCache', 
    'CACHE_DEFAULT_TIMEOUT': 300, 
    'CACHE_REDIS_HOST': os.environ.get('REDIS_HOST'), 
    'CACHE_REDIS_PORT': os.environ.get('REDIS_PORT'), 
    'CACHE_REDIS_DB': os.environ.get('REDIS_DB'), 
    'CACHE_REDIS_PASSWORD': os.environ.get('REDIS_PASSWORD'), 
    'CACHE_KEY_PREFIX': 'flask_' 
}