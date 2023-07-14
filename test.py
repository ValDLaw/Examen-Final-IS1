import unittest
from flask import Flask
from flask.testing import FlaskClient
from datetime import date  # Importar el módulo date
from app import app, BilleteraUTEC

class BilleteraUTECTestCase(unittest.TestCase):
    def setUp(self):
        # Crear una instancia de la aplicación Flask para realizar las pruebas
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

        # Crear una instancia de la billetera UTEC para las pruebas
        self.billetera_utec = BilleteraUTEC()

    def tearDown(self):
        self.app_context.pop()

    def test_mostrar_contactos_exitoso(self):
        # Prueba exitosa de mostrar contactos
        response = self.app.get('/billetera-utec/contactos?minumero=20210001')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'contactos': ['20210002', '20210003']})

    def test_pagar_exitoso(self):
        # Prueba exitosa de realizar un pago
        response = self.app.get('/billetera-utec/pagar?minumero=20210001&numerodestino=20210002&valor=100')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Realizado en {date}.'.format(date=date.today().strftime("%d/%m/%Y")))

    def test_mostrar_historial_exitoso(self):
        # Prueba exitosa de mostrar el historial de operaciones
        response = self.app.get('/billetera-utec/historial?minumero=20210001')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"operaciones":["Pago recibido de 400 de Maria Lopez","Pago recibido de 300 de Carlos Ramirez","2 de 3"],"saldo":200})

    def test_mostrar_contactos_error(self):
        # Prueba de error al mostrar contactos con una cuenta inexistente
        response = self.app.get('/billetera-utec/contactos?minumero=999999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'error': 'No se encontró la cuenta.'})

    def test_pagar_error(self):
        # Prueba de error al realizar un pago con una cuenta inexistente
        response = self.app.get('/billetera-utec/pagar?minumero=999999&numerodestino=20210001&valor=50')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'No se pudo realizar el pago.'})

    def test_mostrar_historial_error(self):
        # Prueba de error al mostrar el historial de operaciones con una cuenta inexistente
        response = self.app.get('/billetera-utec/historial?minumero=999999')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'error': 'No se encontró la cuenta.'})

if __name__ == '__main__':
    unittest.main()
