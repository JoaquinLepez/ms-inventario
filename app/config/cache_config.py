from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class CacheConfig():
    CACHE_TYPE= 'RedisCache' 
    CACHE_DEFAULT_TIMEOUT= 300 
    CACHE_KEY_PREFIX= 'flask_' 

class DevelopmentCacheConfig(CacheConfig):
    CACHE_REDIS_HOST = os.environ.get('DEV_REDIS_HOST')
    CACHE_REDIS_PORT = os.environ.get('DEV_REDIS_PORT') 
    CACHE_REDIS_DB = os.environ.get('DEV_REDIS_DB') 
    CACHE_REDIS_PASSWORD = os.environ.get('DEV_REDIS_PASSWORD')


class ProductionCacheConfig(CacheConfig):
        CACHE_REDIS_HOST = os.environ.get('REDIS_HOST')
        CACHE_REDIS_PORT = os.environ.get('REDIS_PORT') 
        CACHE_REDIS_DB = os.environ.get('REDIS_DB')
        CACHE_REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

def class_to_dict(cls):
        return {
            attr: getattr(cls, attr)
            for attr in dir(cls)
            if not attr.startswith('__') and not callable(getattr(cls, attr))
        }

cache_config = {
    'development': class_to_dict(DevelopmentCacheConfig),
    'production': class_to_dict(ProductionCacheConfig),
    'default': class_to_dict(DevelopmentCacheConfig)
}

# redis_client = redis.StrictRedis(
#     host=os.environ.get('REDIS_HOST'),
#     port=int(os.environ.get('REDIS_PORT')),
#     db=int(os.environ.get('REDIS_DB')),
#     password=os.environ.get('REDIS_PASSWORD'),
#     decode_responses=True
# )
