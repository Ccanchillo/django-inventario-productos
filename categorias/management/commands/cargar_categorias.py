from django.core.management.base import BaseCommand
from categorias.models import Categoria

class Command(BaseCommand):
    help = 'Carga categorías por defecto en la base de datos'
    
    def handle(self, *args, **options):
        categorias = [
            {'nombre': 'Lácteos', 'descripcion': 'Productos derivados de la leche'},
            {'nombre': 'Aceites', 'descripcion': 'Aceites vegetales y comestibles'},
            {'nombre': 'Bebidas', 'descripcion': 'Bebidas alcoholicas y no alcoholicas'},
            {'nombre': 'Legumbres', 'descripcion': 'Legumbres y granos'},
            {'nombre': 'Dulces', 'descripcion': 'Productos dulces y confitería'},
        ]
        
        for cat_data in categorias:
            categoria, created = Categoria.objects.get_or_create(
                nombre=cat_data['nombre'],
                defaults={'descripcion': cat_data['descripcion']}
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Categoría creada: {cat_data["nombre"]}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Categoría ya existe: {cat_data["nombre"]}')
                )