from django import forms
from .models import Producto
from categorias.models import Categoria

class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personalizar el campo categoría
        self.fields['categoria'].queryset = Categoria.objects.all()
        self.fields['categoria'].empty_label = "Seleccione una categoría"
        self.fields['categoria'].widget.attrs.update({'class': 'form-control'})
        
        # Agregar clases a todos los campos
        for field_name, field in self.fields.items():
            if field_name != 'imagen':  # No agregar clase al file input
                field.widget.attrs.update({'class': 'form-control'})
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'precio': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'nombre': 'Nombre del Producto *',
            'precio': 'Precio *',
            'stock': 'Stock *',
            'categoria': 'Categoría *',
        }