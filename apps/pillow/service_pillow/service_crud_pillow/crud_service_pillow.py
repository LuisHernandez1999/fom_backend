from apps.pillow.models import Pillow
from django.core.exceptions import ValidationError

def create_pillow(pillow_code, aquisition_date, category, quantity, value, promotion_value, dealer):
    if Pillow.objects.filter(pillow_code=pillow_code).exists():
        raise ValidationError(f"o codigo '{pillow_code}' ja esta em uso.")
    if category.lower() == 'outlet' and not promotion_value:
        raise ValidationError("itens da categoria Outlet devem ter um valor promocional definido, ze ")
    new_pillow = Pillow.objects.create(
        pillow_code=pillow_code,
        aquisition_date=aquisition_date,
        category=category,
        quantity=quantity,
        value=value,
        promotion_value=promotion_value,
        dealer=dealer,
        outlet=(category.lower() == 'outlet')  
    )

    return new_pillow
