from django import forms
from g2p.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['docfile']