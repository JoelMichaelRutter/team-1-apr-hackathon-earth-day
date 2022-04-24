from django.shortcuts import render
from contributions.models import Reuse, Reduce, Recycle
# Create your views here.

def profile(request):
    """ A view to return index page """
    user_reuse_contributions = Reuse.objects.filter(profile=request.user)
    user_reduce_contributions = Reduce.objects.all()
    user_recycle_contributions = Recycle.objects.all()
    template = 'profiles/profile.html'
    context = {
        'user_reuse_contributions': user_reuse_contributions,
        'user_reduce_contributions': user_reduce_contributions,
        'user_recycle_contributions': user_recycle_contributions,
    }



    return render(request, template, context)