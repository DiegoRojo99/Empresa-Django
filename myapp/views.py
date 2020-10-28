from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Departamento, Habilidad, Empleado
from .forms import MyForm, LoginForm

#devuelve el listado de empresas
def index(request):
	departamentos = get_list_or_404(Departamento.objects.order_by('nombre'))
	context = {'lista_departamentos': departamentos }
	return render(request, 'index.html', context)

#devuelve los datos de un departamento
def detail(request, departamento_id):
	departamento = get_object_or_404(Departamento, pk=departamento_id)
	context = {'departamento': departamento }
	return render(request, 'detail.html', context)

#devuelve los empelados de un departamento
def empleados(request, departamento_id):
	departamento = get_object_or_404(Departamento, pk=departamento_id)
	empleados =  departamento.empleado_set.all()
	context = {'departamento': departamento, 'empleados' : empleados }
	return render(request, 'empleados.html', context)

#devuelve los detalles de un empleado
def empleado(request, empleado_id):
	empleado = get_object_or_404(Empleado, pk=empleado_id)
	habilidades =  empleado.habilidades.all()
	context = {'empleados': empleados, 'habilidades':habilidades}
	return render(request, 'empleado.html', context)

# Devuelve los detalles de una habilidad
def habilidad(request, habilidad_id):
    habilidad = get_object_or_404(Habilidad, pk=habilidad_id)
    empleados =  habilidad.empleado_set.all()
    context = { 'empleados': empleados, 'habilidad' : habilidad }
    return render(request, 'habilidad.html', context)

# Formulario
def loginform(request):
	form = MyForm()
	return render(request, 'login.html', {'form':form})

def get_name(request):
	if request.method == 'POST':
	# Crear una instancia del formulario y asociar los datos recibidos:
	form = LoginForm(request.POST)
	# Validar los datos:
	if form.is_valid():
	# Procesar los datos mediante form.cleaned_data
	# ...
	# redireccionar a una nueva URL:
	return HttpResponseRedirect('/dashboard/')
	# Si el metodo es GET (o cualquier otro) crear un formulario vacío
	else:
	form = NameForm()
	# Renderizar la plantilla con el formulario (con los datos anteriores o vacío)
	return render(request, 'name.html', {'form': form})