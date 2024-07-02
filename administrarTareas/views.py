from django.shortcuts import render, redirect, get_object_or_404
from .models import Tareas
from .Formulario import FormularioTarea

# Create your views here.
def crearTareas(request):
    
    tareasObtenidas = Tareas.objects.all()
    
    if request.method == "POST":
        tituloTarea = request.POST.get("txtnombreTarea")
        descripcion = request.POST.get("areaDescripcion")
        

        if  tituloTarea == "" or descripcion == "":
            
            return render(request, "CrearTareas.html", {"error": "Debe llenar ambos campos", "tareas": tareasObtenidas})
    
        tarea = Tareas(nombreTarea=tituloTarea, descripcionTarea=descripcion)
        tarea.save()
        
        return redirect('CrearTarea')

    return render(request, "CrearTareas.html", {"tareas": tareasObtenidas})


def eliminarTarea(request, idTarea):
    
    try:
        tarea = get_object_or_404(Tareas, pk=idTarea)
        tarea.delete()
    
        return redirect('CrearTarea')
    except:
        
        print("ocurrio un error")

def editarTarea(request, id_Tarea):
    tarea = Tareas.objects.get(pk=id_Tarea)
    if request.method == "POST":

        formulario = FormularioTarea(request.POST,instance=tarea)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('CrearTarea')
        else:
            print("Error al registrar")
    
    else:
        
        formulario = FormularioTarea(instance=tarea)
    
    context = {"Formulario": formulario, "tarea": tarea}
    
    return render(request, "EdicionTarea.html", context)
    
    
    
    
    