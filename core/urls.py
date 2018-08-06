from django.urls import path, include
from core.views import ProductCreateView, ProductListView, CategoryListView, CategoryCreateView,ProductDeleteView, ProductUpdateView, ProductCategoryListView

app_name = 'core'

urlpatterns = [
	path('', CategoryListView.as_view(),name='home'),
	path('product/create/', ProductCreateView.as_view(), name='new_product'),	
	path('category/create/', CategoryCreateView.as_view(), name='new_category'),
	path('list_products/<int:category_id>', ProductCategoryListView.as_view(), name='products'),	
	path('list_products/all', ProductListView.as_view(), name='products_all'),
	path('delete_product/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
	path('update_product/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
 
]