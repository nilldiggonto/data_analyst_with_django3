from django.shortcuts import render
from .models import Product,Purchase

import pandas as pd


# Create your views here.
def home(request):
    template_name = 'products/main.html'
    return render(request,template_name)

def chart_page(request):
    template_name = 'products/chart.html'
    queryset = Product.objects.all()
    qs1 = Product.objects.all().values()
    qs2 = Product.objects.all().values_list()

    purchase = Purchase.objects.all()
    # print(qs1)
    # print(qs2)

    product_df = pd.DataFrame(qs1)
    purchase_df = pd.DataFrame(purchase.values())
    # print(product_df)

    #merging df
    product_df['product_id'] = product_df['id']
    df = pd.merge(purchase_df,product_df,on='product_id').drop(['id_y','created_y'],axis=1).rename({'id_x':'id','created_x':'date'},axis=1)
    context = {
        'queryset':queryset,
        'product_df':product_df.to_html(),
        'purchase_df':purchase_df.to_html(),
        'df':df.to_html(),
    }
    return render(request,template_name,context)