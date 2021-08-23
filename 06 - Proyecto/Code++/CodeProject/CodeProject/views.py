from django.shortcuts import render

def dashboardventas(request):
    return render(request, 'dashboardventas.html', {
        'message': 'Mensaje desde el contexto.',
        'list': [1,2,3]
        # Context
} )
    
def dashboardproductos(request):
    return render(request, 'dashboardproductos.html', {
        # Context
} )
    
def dashboardcategorias(request):
    return render(request, 'dashboardcategorias.html', {
        # Context
} )
    
def dashboardclientes(request):
    return render(request, 'dashboardclientes.html', {
        # Context
} )

def dashboardestado(request):
    return render(request, 'dashboardestado.html', {
        # Context
} )
    
def dashboardmarcas(request):
    return render(request, 'dashboardmarcas.html', {
        # Context
} )
    
def dashboardmateriales(request):
    return render(request, 'dashboardmateriales.html', {
        # Context
} )
    
def dashboardpaisorigen(request):
    return render(request, 'dashboardpaisorigen.html', {
        # Context
} )
    
def dashboardproveedores(request):
    return render(request, 'dashboardproveedores.html', {
        # Context
} )
    
def dashboardroles(request):
    return render(request, 'dashboardroles.html', {
        # Context
} )
    
def dashboardtipodoc(request):
    return render(request, 'dashboardtipodoc.html', {
        # Context
} )
    
def dashboardusuarios(request):
    return render(request, 'dashboardusuarios.html', {
        # Context
} )
    
def index(request):
    return render(request, 'index.html', {
        # Context
} )
    
def login(request):
    return render(request, 'login.html', {
        # Context
} )