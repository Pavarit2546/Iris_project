from django import forms
from .models import IrisFlower

class IrisFlowerForm(forms.ModelForm):
    class Meta:
        model = IrisFlower
        fields = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        widgets = {
            'SepalLengthCm': forms.NumberInput(attrs={'placeholder': 'Sepal Length in cm'}),
            'SepalWidthCm': forms.NumberInput(attrs={'placeholder': 'Sepal Width in cm'}),
            'PetalLengthCm': forms.NumberInput(attrs={'placeholder': 'Petal Length in cm'}),
            'PetalWidthCm': forms.NumberInput(attrs={'placeholder': 'Petal Width in cm'}),
        }