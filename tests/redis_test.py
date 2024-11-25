import os
import unittest
from redis import Redis
from app import create_app, cache, db
from app.models import Stock
from app.services import StockService

service = StockService()

class RedisTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    # test connection to Redis
    def test_redis_connection(self):
        redis = Redis(
            host=self.app.config['CACHE_REDIS_HOST'],
            port=self.app.config['CACHE_REDIS_PORT'],
            db=self.app.config['CACHE_REDIS_DB'],
            password=self.app.config['CACHE_REDIS_PASSWORD']
        )
        self.assertTrue(redis.ping())
    
    def test_cache_after_adding_stock(self):
        stock = Stock(producto_id=1, fecha_transaccion='2024-09-13T15:30:00', cantidad=1, entrada_salida=1)
        stock1 = service.add(stock)
        
        cached_stock = cache.get(f'stock_{stock1.id}')
        
        
        self.assertIsNotNone(cached_stock) 
        self.assertEqual(cached_stock.id, stock1.id)
        self.assertEqual(cached_stock.producto_id, stock1.producto_id)
        self.assertEqual(cached_stock.fecha_transaccion, stock1.fecha_transaccion)
        self.assertEqual(cached_stock.cantidad, stock1.cantidad)
        self.assertEqual(cached_stock.entrada_salida, stock1.entrada_salida)
    
    def test_cache_after_deleting_stock(self):
        stock = Stock(producto_id=1, fecha_transaccion='2024-09-13T15:30:00', cantidad=1, entrada_salida=1)
        stock1 = service.add(stock)
        cached_stock = cache.get(f'stock_{stock1.id}')
        self.assertIsNotNone(cached_stock)

        service.delete(stock1.id)
        cached_stock = cache.get(f'stock_{stock1.id}')
        self.assertIsNone(cached_stock)

if __name__ == '__main__':
    unittest.main()