from django.forms.widgets import ClearableFileInput, MultipleFileInput

class MRIUploadForm(forms.Form):
    images = forms.FileField(widget=ClearableFileInput(attrs={'multiple': True}))
