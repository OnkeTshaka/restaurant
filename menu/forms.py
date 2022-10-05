from tkinter import Widget
from django.forms import ModelForm
from menu.models import Restaurant


class RestaurantForm(ModelForm):
    class Meta: 
        model=Restaurant
        fields="__all__"
        widget ={
            
        }