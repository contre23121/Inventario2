from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    # Obtener la URL a la que redirigir después de iniciar sesión (usualmente viene en "next")
    next_url = request.GET.get('next', '')  # Redirige por defecto a 'vista_jefe' si no hay "next"
    
    # Cuando el formulario es enviado
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Autenticar el usuario utilizando el backend personalizado
            user = authenticate(request, username=usuario, password=password)
            if user is not None:
                # Iniciar sesión
                login(request, user, backend='gestion_usuarios.backends.UsuariosBackend')
                
                # Redireccionar según el rol
                if user.rolid == 1:  # Jefe
                    return redirect(next_url if next_url else 'vista_jefe')
                elif user.rolid == 2:  # Despachador
                    return redirect(next_url if next_url else 'vista_despachador')
            else:
                # Si la autenticación falla
                form.add_error(None, "Usuario o contraseña incorrectos")
    else:
        # Si el formulario no se ha enviado todavía
        form = CustomAuthenticationForm()
    
    # Renderizar la plantilla de login con el formulario
    return render(request, 'gestion_usuarios/login.html', {'form': form})

@login_required(login_url='login')  # Redirige a login si no está autenticado
def vista_jefe(request):
    return render(request, 'gestion_usuarios/vista_jefe.html')

@login_required(login_url='login')  # Redirige a login si no está autenticado
def vista_despachador(request):
    return render(request, 'gestion_usuarios/vista_despachador.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige al login después de cerrar sesión
