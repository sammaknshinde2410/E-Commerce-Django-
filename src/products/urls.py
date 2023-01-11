from django.urls import path

from products.views import (ProductListView, 
                            product_list_view,
                            ProductDetailView, 
                            product_detail_view, 
                            ProductFeaturedListView, 
                            ProductFeaturedDetailView, 
                            ProductDetailsslugView
                            )

app_name= 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug>/',ProductDetailsslugView.as_view(), name="detail"),
]


