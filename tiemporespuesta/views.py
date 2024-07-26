from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from .forms import PruebaForm
from .models import Prueba
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@login_required
def mi_puntuacion(request):
    pruebas = Prueba.objects.filter(usuario=request.user)
    puntuaciones = [prueba.tiempo_total() for prueba in pruebas]
    puntuacion_total = sum(puntuaciones)

    context = {
        'puntuacion_total': puntuacion_total,
        'pruebas': pruebas
    }
    return render(request, 'mi_puntuacion.html', context)

@csrf_exempt
@require_POST
def guardar_prueba(request):
    try:
        data = json.loads(request.body)
        prueba = Prueba(
            usuario=request.user,
            letra_1=data.get('letra_1', ''),
            tiempo_1=data.get('tiempo_1', 0),
            letra_2=data.get('letra_2', ''),
            tiempo_2=data.get('tiempo_2', 0),
            letra_3=data.get('letra_3', ''),
            tiempo_3=data.get('tiempo_3', 0),
            letra_4=data.get('letra_4', ''),
            tiempo_4=data.get('tiempo_4', 0),
            letra_5=data.get('letra_5', ''),
            tiempo_5=data.get('tiempo_5', 0)
        )
        prueba.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = PruebaForm(request.POST)
        if form.is_valid():
            prueba = form.save(commit=False)
            prueba.usuario = request.user
            prueba.save()
            return redirect('resultado')
    else:
        form = PruebaForm()

    return render(request, 'dashboard.html', {'form': form})

@login_required
def jugar(request):
    return render(request, 'jugar.html')

def ver_ranking(request):
    pruebas = Prueba.objects.all()
    pruebas_ordenadas = sorted(pruebas, key=lambda p: p.tiempo_total())
    mejores_pruebas = pruebas_ordenadas[:10]
    return render(request, 'ranking.html', {'pruebas': mejores_pruebas})


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/'
