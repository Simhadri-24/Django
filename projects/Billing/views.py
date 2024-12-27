from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import market,product
from .forms import marketform, productform
def empList(request):
    emp=market.objects.all();
    return render(request,"display.html",{'emp':emp})
def addEmp(request):
    if request.method=="POST":
        form=marketform(request.POST);
        if form.is_valid():
            form.save();
            return redirect("empList")
    else:
        form=marketform();
        return render(request,"addEmp.html",{'form':form});
def delEmp(request,emp_id):
    emp=get_object_or_404(market,empnumber=emp_id)
    if request.method=="POST":
        emp.delete()
        return redirect('empList')
    return render(request,"delEmp.html",{'emp':emp})
def addProduct(request):
    if request.method=="POST":
        pro=productform(request.POST);
        if pro.is_valid():
            pro.save()
            return redirect("empList")
    else:
        pro=productform();
        return render(request,"addProduct.html",{'pro':pro})
def sold_items(request,name,pquantity):
    pro=get_object_or_404(product,pname=name)
    if pro.quantity>=pquantity:
        pro.quantity-=pquantity
        pro.save()
        return HttpResponse("product count updated successfully")
    else:
        return HttpResponse("Not enough stock")

def stock(request):
    # Get distinct categories and their products
    categories = product.objects.values('category').distinct()
    category_wise_stock = {
        category['category']: product.objects.filter(category=category['category'])
        for category in categories
    }
    return render(request, "stock.html", {'category_wise_stock': category_wise_stock})

def product_stock(request,pname):
    try:
        pro=product.objects.get(pname=pname)
        return render(request,"product.html",{'pro':pro})
    except product.DoesNotExist:
        return HttpResponse("product not found")

                
    