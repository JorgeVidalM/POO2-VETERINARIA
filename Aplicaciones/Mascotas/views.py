from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Dueno, Mascota, Especie
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError


def menu_principal(request):
    return render(request, "menu.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/menu/')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('/login/')

def gestion_mascota(request):
    mascotas = Mascota.objects.all()
    duenos = Dueno.objects.all()
    especies = Especie.objects.all()
    return render(request, 'gestionMascota.html', {
        'mascotas': mascotas,
        'duenos': duenos,
        'especies': especies
    })


def registrarMascota(request):
    if request.method == 'POST':
        nombre = request.POST.get('txtNombre')
        fecha_nacimiento = request.POST.get('fechaNacimiento')
        sexo = request.POST.get('sexo')
        dueno_rut = request.POST.get('dueno')
        especie_id = request.POST.get('especie')

        if not (nombre and fecha_nacimiento and sexo and dueno_rut and especie_id):
            messages.error(request, "Faltan campos obligatorios.")
            return redirect('gestion_mascota')

        try:
            dueno = Dueno.objects.get(rut=dueno_rut)
            especie = Especie.objects.get(id=especie_id)

            Mascota.objects.create(
                nombre=nombre,
                fecha_nacimiento=fecha_nacimiento,
                sexo=sexo,
                dueno=dueno,
                especie=especie
            )
            messages.success(request, "Mascota registrada con éxito.")
        except Dueno.DoesNotExist:
            messages.error(request, "El dueño seleccionado no existe.")
        except Especie.DoesNotExist:
            messages.error(request, "La especie seleccionada no existe.")
        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")
        except Exception as e:
            messages.error(request, f"Error inesperado: {str(e)}")
            print("Error al registrar:", e)

    return redirect('gestion_mascota')


def edicionMascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    duenos = Dueno.objects.all()
    especies = Especie.objects.all()
    
    return render(request, "edicionMascota.html", {
        "mascota": mascota,
        "duenos": duenos,
        "especies": especies
    })


def editarMascota(request):
    if request.method == "POST":
        id_mascota = request.POST['idMascota']
        mascota = get_object_or_404(Mascota, id=id_mascota)

        mascota.nombre = request.POST['txtNombre']
        mascota.fecha_nacimiento = request.POST['fechaNacimiento']
        mascota.sexo = request.POST['sexo']
        mascota.dueno = get_object_or_404(Dueno, rut=request.POST['RutDueno'])
        mascota.especie = get_object_or_404(Especie, id=request.POST['IdEspecie'])
        mascota.save()

        messages.success(request, '¡Mascota actualizada!')
    
    return redirect('/mascotas/')


def eliminarMascota(request, id):
    mascota = get_object_or_404(Mascota, id=id)
    mascota.delete()
    messages.success(request, '¡Mascota eliminada!')
    return redirect('/mascotas/')




def gestion_dueno(request):
    duenos = Dueno.objects.all()
    return render(request, "gestionDueno.html", {"duenos": duenos})


def registrarDueno(request):
    if request.method == "POST":
        rut = request.POST['txtRut']
        nombre = request.POST['txtNombre']
        direccion = request.POST['txtDireccion']
        telefono = request.POST['txtTelefono']
        correo = request.POST['txtCorreo']

        if Dueno.objects.filter(rut=rut).exists():
            messages.warning(request, "El RUT ya está registrado.")
        else:
            Dueno.objects.create(
                rut=rut,
                nombre_completo=nombre,
                direccion=direccion,
                telefono=telefono,
                correo=correo
            )
            messages.success(request, '¡Dueño registrado!')
    return redirect('/duenos/')


def edicionDueno(request, rut):
    dueno = get_object_or_404(Dueno, rut=rut)
    return render(request, "edicionDueno.html", {"dueno": dueno})


def editarDueno(request):
    if request.method == "POST":
        rut = request.POST['txtRut']
        dueno = get_object_or_404(Dueno, rut=rut)

        dueno.nombre_completo = request.POST['txtNombre']
        dueno.direccion = request.POST['txtDireccion']
        dueno.telefono = request.POST['txtTelefono']
        dueno.correo = request.POST['txtCorreo']
        dueno.save()

        messages.success(request, '¡Dueño actualizado!')
    return redirect('/duenos/')


def eliminarDueno(request, rut):
    dueno = get_object_or_404(Dueno, rut=rut)
    dueno.delete()
    messages.success(request, '¡Dueño eliminado!')
    return redirect('/duenos/')


def detalle_dueno(request, rut):
    dueno = get_object_or_404(Dueno, rut=rut)
    mascotas = Mascota.objects.filter(dueno=dueno)

    return render(request, "detalleDueno.html", {
        "dueno": dueno,
        "mascotas": mascotas
    })



def gestion_especie(request):
    especie = Especie.objects.all()
    return render(request, "gestionEspecie.html", {"especie": especie})

def registrarEspecie(request):
    if request.method == "POST":
        nombre = request.POST['txtNombre']
        if Especie.objects.filter(nombre__iexact=nombre).exists():
            messages.warning(request, "Esa especie ya existe.")
        else:
            Especie.objects.create(nombre=nombre)
            messages.success(request, '¡Especie registrada!')
    return redirect('/especie/')

def edicionEspecie(request, id):
    especie = get_object_or_404(Especie, id=id)
    return render(request, "edicionEspecie.html", {"especie": especie})

def editarEspecie(request):
    if request.method == "POST":
        id = request.POST['idEspecie']
        especie = get_object_or_404(Especie, id=id)
        especie.nombre = request.POST['txtNombre']
        especie.save()
        messages.success(request, '¡Especie actualizada!')
    return redirect('/especie/')

def eliminarEspecie(request, id):
    especie = get_object_or_404(Especie, id=id)
    try:
        especie.delete()
        messages.success(request, '¡Especie eliminada!')
    except ProtectedError:
        messages.error(request, 'No se puede eliminar: hay mascotas asociadas a esta especie.')
    return redirect('/especie/')
