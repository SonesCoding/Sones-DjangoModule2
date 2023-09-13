from django import forms
from . import models

star_list = models.Star.objects.all()

class Shop(forms.Form):
    chosen_star= forms.CharField(label='You may choose 1 Star',
                                    widget=forms.RadioSelect(choices= star_list))