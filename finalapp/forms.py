from django.forms import ModelForm

from finalapp.models import Registerr, Branch, City


class RegisterrForms(ModelForm):
    class Meta:
        model = Registerr
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()
