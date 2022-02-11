from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Select, SelectMultiple

from apps.properties.models import Property, Owner


class PropertyForm(ModelForm):

    def clean_cadastral_id(self):
        cadastral_id = self.cleaned_data['cadastral_id']
        cadastral_len = len(cadastral_id)
        if cadastral_len not in [20, 30]:
            raise ValidationError('La longitud debe ser igual a 20 o 30')
        return cadastral_id

    def clean(self):
        clean_data = super().clean()
        user = None
        if clean_data.get('type') == 1 and not clean_data.get('address'):
            raise ValidationError('La dirección es requerida')
        elif clean_data.get('type') == 2 and not clean_data.get('name'):
            raise ValidationError('El nombre es requerido')
        return clean_data

    class Meta:
        model = Property
        fields = [
            'registration_number',
            'cadastral_id',
            'address',
            'name',
            'type',
            'owners'
        ]

        widgets = {
            'registration_number': TextInput(attrs={'class': 'form-control'}),
            'cadastral_id': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-select'}),
            'owners': SelectMultiple(attrs={'class': 'basic-multiple', 'multiple': 'multiple'}),
        }


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = [
            'name',
            'identification',
            'type'
        ]

        widgets = {
            'identification': TextInput(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'type': Select(attrs={'class': 'form-select'}),
        }
