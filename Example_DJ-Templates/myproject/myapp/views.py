from django.shortcuts import render

def my_view(request):
    context = {'user': request.user}
    return render(request, 'mytemplate.html', context)


