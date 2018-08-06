from django import forms
from django.forms import inlineformset_factory
from core.models import Product, Category


class ProductForm(forms.ModelForm):			
	def __init__(self, *args, **kwargs):
		super(ProductForm, self).__init__(*args, **kwargs)
		self.fields['category'].required = False

	class Meta:
		model = Product		
		fields = '__all__'


class CategorytForm(forms.ModelForm):		

	class Meta:
		model = Category	
		fields = '__all__'

