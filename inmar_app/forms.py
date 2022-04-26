from django import forms

from inmar_app.models import Store


class StoreForms(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'