from django.shortcuts import render

# Create your views here.
def contributions(request):
    """ A view to show contributions form """

    return render(request, 'contributions/contributions.html')
