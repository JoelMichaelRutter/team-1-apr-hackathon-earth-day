from django.shortcuts import render
from .models import Recycle, Reduce, Reuse
from .forms import RecycleForm

# Create your views here.
def testAction(request):
    recyle_contribs = list(Recycle.objects.all())
    reuse_contribs = list(Reuse.objects.all())
    reduce_contribs = list(Reduce.objects.all())
    recycle_form = RecycleForm()

    context = {
        'recycle': recyle_contribs,
        'reuse': reuse_contribs,
        'reduce': reduce_contribs,
        'recyle_form': recycle_form,
    }
    print(recyle_contribs)
    return render(request, 'contributions/contributions.html', context)
