from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm
from categorias.models import Categoria

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def crear_producto(request):
    # Verificar que existan categorías, si no, crear algunas por defecto
    if not Categoria.objects.exists():
        categorias_por_defecto = [
            Categoria(nombre='Lácteos', descripcion='Productos lácteos'),
            Categoria(nombre='Aceites', descripcion='Aceites comestibles'),
            Categoria(nombre='Bebidas', descripcion='Bebidas varias'),
            Categoria(nombre='Legumbres', descripcion='Legumbres y granos'),
            Categoria(nombre='Dulces', descripcion='Productos dulces'),
        ]
        Categoria.objects.bulk_create(categorias_por_defecto)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente!')
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    
    # Obtener todas las categorías para el dropdown
    categorias = Categoria.objects.all()
    
    return render(request, 'productos/crear_producto.html', {
        'form': form,
        'categorias': categorias
    })

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente!')
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    
    # Obtener todas las categorías para el dropdown
    categorias = Categoria.objects.all()
    
    return render(request, 'productos/editar_producto.html', {
        'form': form, 
        'producto': producto,
        'categorias': categorias
    })

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente!')
        return redirect('lista_productos')
    
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})