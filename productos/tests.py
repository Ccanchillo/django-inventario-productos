from django.test import TestCase
from django.urls import reverse
from .models import Producto
from categorias.models import Categoria

class ProductoTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Electrónicos")
        self.producto = Producto.objects.create(
            nombre="Laptop",
            precio=1500.00,
            stock=10,
            categoria=self.categoria
        )

    def test_creacion_producto(self):
        self.assertEqual(self.producto.nombre, "Laptop")
        self.assertEqual(self.producto.precio, 1500.00)

    def test_lista_productos(self):
        response = self.client.get(reverse('lista_productos'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Laptop")