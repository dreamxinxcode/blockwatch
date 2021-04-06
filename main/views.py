from django.shortcuts import render


def homepage_view(request):
    context = {

    }
    return render(request=request, template_name='main/index.html', context=context)
