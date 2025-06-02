from apps.pillow.models import Pillow
from django.core.paginator import Paginator, EmptyPage

def get_outlet_fields(page=1):
    max_pages = 10000 * 100
    outlet_pillows = Pillow.objects.filter(category='Outlet').values('pillow_code', 'promotion_value')[:max_pages]
    paginator = Paginator(outlet_pillows, 100)
    try:
        page_data_outlet= paginator.page(page)
    except EmptyPage:
        return []
    return list(page_data_outlet)
