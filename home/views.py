from django.shortcuts import render

"""Renders the first/home page that allows users to select
different options
"""


def home(request):
    return render(request, 'home/index.html', {"home":home}, )
