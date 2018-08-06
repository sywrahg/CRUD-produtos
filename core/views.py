from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from core.models import Product, Category
from .forms import ProductForm, CategorytForm

class ProductCreateView(generic.CreateView):	
	form_class = ProductForm
	template_name = 'products/create_products.html'	

	def get_success_url(self):
		return reverse_lazy('core:products_all')


class CategoryCreateView(generic.CreateView):
	model = Category
	form_class = CategorytForm
	template_name = 'core/create_category.html'

	def get_success_url(self):
		return reverse_lazy('core:home')


class ProductCategoryListView(generic.CreateView):

	def get(self, request, *args, **kwargs):
		category_id = self.kwargs['category_id']
		category = Category.objects.get(id = category_id)
		products = Product.objects.filter(category_id = category_id)

		return render(request, "products/product_category_list.html", {'products':products, 'category': category})


class ProductListView(generic.CreateView):
	def get(self, request):		
		products = Product.objects.all()

		return render(request, "products/product_list.html", {'products':products})


class ProductUpdateView(generic.UpdateView):
	model = Product
	form_class = ProductForm
	template_name = 'products/create_products.html'
	
	def get_object(self, queryset=None):
		pk = self.kwargs['pk']
		return Product.objects.get(pk=pk)

	def get_success_url(self):
		return reverse_lazy('core:products_all')

class ProductDeleteView(generic.UpdateView):
	model = Product		
	
	def get(self, request, *args, **kwargs):
		pk = kwargs['pk']
		product = Product.objects.get(pk=pk)
		product.delete()		
		products = Product.objects.all()

		return render(request, "products/product_list.html", {'products':products})

	def get_success_url(self):
		return reverse_lazy('core:products_all')

class CategoryListView(generic.CreateView):
	def get(self, request):
		categories = Category.objects.all()

		return render(request, "core/home.html", {'categories':categories})
				