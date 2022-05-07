from django import forms
from .models import Banhmi, Size


# class BanhmiForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])

class BanhmiForm(forms.ModelForm):

    size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None)

    class Meta:
        model = Banhmi
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1': '1st Topping', 'topping2': '2nd Topping'}


class MultipleBanhmiForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)
