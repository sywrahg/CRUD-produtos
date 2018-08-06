from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length = 80, verbose_name = 'Nome do Produto')
	price = models.DecimalField(max_digits = 30, decimal_places = 2, default = 0, verbose_name = 'Preço')
	quantity = models.IntegerField(default = 0, verbose_name = 'Quantidade')
	category = models.ForeignKey('Category', related_name = 'products', null = True, on_delete = models.SET_NULL)
	

class Category(models.Model):
	name = models.CharField(max_length = 80, verbose_name = 'Nome da Categoria')	

	def __str__(self): 
		return self.name
