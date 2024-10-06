import unittest, os
from app import create_app, db
from app.models import Stock
class StockTestCase(unittest.TestCase):
    
    def setUp(self):
        # User
        self.IDPRODUCTO_PRUEBA = 1
        self.FECHATRANSACCION_PRUEBA = "2020-01-01:00:00"
        self.CANTIDAD_PRUEBA = 6
        self.ENTRADASALIDA_PRUEBA = 1
    
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_stock(self):
        stock = self.__get_stock()

        self.assertEqual(stock.producto_id, self.IDPRODUCTO_PRUEBA)
        self.assertEqual(stock.fecha_transaccion, self.FECHATRANSACCION_PRUEBA)
        self.assertEqual(stock.cantidad, self.CANTIDAD_PRUEBA)
        self.assertEqual(stock.entrada_salida, self.ENTRADASALIDA_PRUEBA)

    def __get_stock(self):
        stock = Stock()
        stock.producto_id = self.IDPRODUCTO_PRUEBA
        stock.fecha_transaccion = self.FECHATRANSACCION_PRUEBA
        stock.cantidad = self.CANTIDAD_PRUEBA
        stock.entrada_salida = self.ENTRADASALIDA_PRUEBA

        return stock
    
if __name__ == '__main__':
    unittest.main()