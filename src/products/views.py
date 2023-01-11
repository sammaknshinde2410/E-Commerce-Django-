from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product
# Create your views here.
from carts.models import Cart

class ProductDetailsslugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"


	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailsslugView, self).get_context_data(*args, **kwargs)
		request = self.request
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		context["cart"] = cart_obj
		return context


	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		# instance = get_object_or_404(Product, slug=slug, active=True)
		try :
			instance = Product.objects.get(slug=slug, active = True)
		except Product.DoesNotExist:
			raise Http404("Not Found")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug=slug, active=True)
			instance = qs.first()
		except :
			raise Http404("Hmmmmm")
		return instance


# List view for only featured Products
class ProductFeaturedListView(ListView):
	template_name="products/featured-list.html"
	
	def get_queryset(self, *args,**kwargs):
		request = self.request
		return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
	# queryset= Product.objects.all()
	template_name="products/featured-detail.html"

	def get_queryset(self, *args,**kwargs):
		request = self.request
		return Product.objects.featured()


class ProductListView(ListView):
	queryset= Product.objects.all()
	template_name="products/list.html"

	# def get_context_data(self, *args, **kwargs):
	#	"""for printing the object list"""
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	def get_queryset(self, *args,**kwargs):
		request = self.request
		return Product.objects.all()



#defining a function for printing an object from the database.
def product_list_view(request):
	"""Queryset Var:creates a list of all objects in database."""
	queryset = Product.objects.all()
	#print(queryset)
	context = {
		'qs':queryset
	}
	return render(request, "products/featured-list.html", context)



class ProductDetailView(DetailView):
	queryset= Product.objects.all()
	template_name="products/featured-detail.html"

	def get_queryset(self, *args,**kwargs):
		request = self.request
		return Product.objects.all()


	# def get_objects(self, *args, **kwargs):
	# 	request = self.request_started
	# 	pk=self.kwargs.get('pk')
	# 	instance = Product.objects.get_by_id(pk)
	# 	# print(instance)
	# 	if instance is None:
	# 		raise Http404("Product doesn't exists")
	# 	return instance

	# def get_queryset(self, *args,**kwargs):
	# 	request = self.request
	# 	pk = self.kwargs.get('pk')
	# 	return Product.objects.filter(pk=pk)

def product_detail_view(request,pk=None, *args, **kwargs):
	#instance = Product.objects.get(pk=pk)

	#instance =get_object_or_404(Product, pk = pk)
	# queryset = Product.objects.all()
	
	# try:
	# 	instance = Product.objects.get(id=pk)
	# except Product.DoesNotExist:
	# 	print("not Product here")
	# 	raise Http404("Product Doesn't Exists")

	instance = Product.objects.get_by_id(pk)
	# print(instance)
	if instance is None:
		raise Http404("Product doesn't exists")

	qs = Product.objects.filter(id=pk)
	print(qs)#prints a single object with matching id.
	if qs.exists() and qs.count()==1:
		instance = qs.first()
	else:
		raise Http404("Product doesn't exists")


	context = {
		'object': instance
	}
	return render(request, "products/detail.html", context)