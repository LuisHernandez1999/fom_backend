from django.db import models
from django.core.exceptions import ValidationError


class Pillow(models.Model):
    TYPES_CATEGORY = [
        ('kids', 'Kids'),
        ('elders', 'Elders'),
        ('baby', 'Baby'),
        ('travels', 'Travels'),
        ('outlet', 'Outlet'),
    ]
    name= models.CharField(max_length=51,null=False,
        blank=False,default='Travisseiro de pluma')
    pillow_code = models.CharField(max_length=14, unique=True)
    aquisition_date = models.DateField()
    category = models.CharField(max_length=20, choices=TYPES_CATEGORY)
    quantity = models.CharField(max_length=4)
    outlet = models.BooleanField(default=False)
    value = models.CharField(max_length=10)
    promotion_value = models.CharField(max_length=10, blank=True, null=True)
    dealer = models.CharField(max_length=20)

    def clean(self):
        if self.category.lower() == 'outlet' and not self.promotion_value:
            raise ValidationError("travesseiros da categoria Outlet devem ter um valor promocional,ze.")

    def save(self, *args, **kwargs):
        self.full_clean()  
        self.outlet = (self.category.lower() == 'Outlet') 
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.pillow_code} - {self.category}"
