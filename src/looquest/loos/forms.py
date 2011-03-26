from django.forms import ModelForm
from models import LooSpot

class LooSpotForm(ModelForm):
    
    class Meta:
        model = LooSpot