from django import forms

from contact_manager.models import Country


#class CountryForm(forms.Form):
#    name = forms.CharField(max_length=10)
#    capital = forms.CharField(max_length=24)
 #   population = forms.IntegerField()
  #  sea = forms.BooleanField()
   # currency = forms.CharField(max_length=3)


class CountryModelForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
