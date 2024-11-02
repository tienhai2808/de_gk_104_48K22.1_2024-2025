from django import forms
from .models import BaiViet

class BaiVietForm(forms.ModelForm):
  class Meta:
    model = BaiViet
    fields = '__all__'