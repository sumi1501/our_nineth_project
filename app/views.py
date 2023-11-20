from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='this is our project'
    d={'project':data}
    return render (request,'data_render.html',context=d)