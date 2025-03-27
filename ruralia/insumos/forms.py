from django import forms
from .models import Remito, RemitoInsumo, Insumo

class RemitoForm(forms.ModelForm):
    insumos = forms.ModelMultipleChoiceField(
        queryset=Insumo.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Insumos"
    )
    
    class Meta:
        model = Remito
        fields = ['numero_remito', 'proveedor', 'fecha', 'insumos']

class RemitoInsumoForm(forms.ModelForm):
    insumo = forms.ModelChoiceField(queryset=Insumo.objects.all(), label='Insumo')
    cantidad = forms.IntegerField(min_value=1, label='Cantidad')

    class Meta:
        model = RemitoInsumo
        fields = ['insumo', 'cantidad']

#INSUMO 

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['nombre', 'descripcion', 'precio', 'unidad']  # Asegúrate de que estos campos existan en el modelo