import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.pillow.service_pillow.service_crud_pillow.crud_service_pillow  import create_pillow  
from django.core.exceptions import ValidationError


@csrf_exempt 
def create_pillow_view(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'metodo nao permitido'}, status=405)

    try:
        data = json.loads(request.body)

        pillow = create_pillow(
            pillow_code=data.get('pillow_code'),
            aquisition_date=data.get('aquisition_date'),
            category=data.get('category'),
            quantity=data.get('quantity'),
            value=data.get('value'),
            promotion_value=data.get('promotion_value'),
            dealer=data.get('dealer'),
        )
        return JsonResponse({
            'message': f'travesseiro criado com sucesso: {pillow.id}',
            'pillow_id': pillow.id
        }, status=201)
    except ValidationError as e:
        return JsonResponse({'error': str(e)}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'json invalido'}, status=400)
    except Exception:
        return JsonResponse({'error': 'erro interno do servidor'}, status=500)
