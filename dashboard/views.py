from django.shortcuts import render, redirect
from main import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from rest_framework import viewsets
from main.models import Category
from . import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()  # Queryset for all categories
    serializer_class = CategorySerializer  # Serializer for data conversion

    def perform_create(self, serializer):
        # Optional: Customize create logic here (e.g., set defaults)
        serializer.save()










# @login_required(login_url='dashboard:log_in')
def index(request):

    return render(request, 'dashboard\index.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return render(request, 'dashboard/auth/login.html', {'error': 'Invalid credentials. Please try again.'})

    return render(request, 'dashboard/auth/login.html')



def create_category(request):
    if request.method == "POST":       
        name= request.POST['name']
        models.Category.objects.create(
            name=name,
        
        )   
    return render(request, 'dashboard/category/create.html')


def detail_category(request, id):
    category = models.Category.objects.get(id=id)
    context = {
        'category':category
    }
    return render(request, 'dashboard/category/detail.html', context)

def list_category(request):
    category = models.Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'dashboard/category/list.html', context)


def update_category(request, id):
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.save()
        return redirect('dashboard:detail_category', category.id )      
    return render(request, 'dashboard/category/update.hml', {'category':category})


def detail_category(request, id):
    category = models.Category.objects.get(id=id)
    context = {
        'category':category
    }
    return render(request, 'dashboard/category/detail.html', context)



def delete_category(request, id):
    models.Category.objects.get(id=id).delete()
    return redirect('list_category')
    


def create_post(request):
    regions = models.Region.objects.all()
    category = models.Category.objects.all()
    context = {
        'regions':regions,
        'category':category
    }
    if request.method == 'POST':
        models.Post.objects.create(
            

           
            name = request.POST['name'],
            body = request.POST['body'],
            banner_img = request.POST['banner_img'],

        )

   
    return render(request, 'dashboard/post/create.html', context)

# def product_create(request):
#     categorys = models.Category.objects.all()
#     context = {'categorys':categorys}
#     if request.method == 'POST':
#         delivery = True if request.POST.get('delivery') else False

#         models.Product.objects.create(
#             category_id = request.POST['category_id'],
#             name = request.POST['name'],
#             body = request.POST['body'],
#             price = request.POST['price'],
#             banner_img = request.FILES['banner_img'],
#             quantity = request.POST['quantity'],
#             delivery = delivery
#         )
#         return redirect('dashboard:product_list')
#     return render(request, 'dashboard/product/create.html', context)




def regions(request, id):
    regions = models.Region.objects.all()
    
    return render(request, 'dashboard/post/regions.html', {'regions': regions})












