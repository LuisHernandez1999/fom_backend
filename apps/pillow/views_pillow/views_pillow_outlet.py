from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.pillow.service_pillow.service_pillow_outlet.outlet_pillow_service import get_outlet_fields

@csrf_exempt
def get_outlet_pillows_view(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'metodo nao permitido'}, status=405)

    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except ValueError:
        return JsonResponse({'error': 'numero de pagina invalido ou nao existe man '}, status=400)

    outlet_pillows = get_outlet_fields(page=page)
    return JsonResponse({'data': outlet_pillows}, safe=False, status=200)