from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from .models import Recycle, Reduce, Reuse
from .forms import RecycleForm, ReduceForm, ReuseForm
from profiles.models import UserProfile


def contributions(request):
    """ A view to show contributions form """
    recycle_form = RecycleForm()
    reuse_form = ReuseForm()
    reduce_form = ReduceForm()

    context = {
        'recycle_form': recycle_form,
        'reuse_form': reuse_form,
        'reduce_form': reduce_form,
    }
    return render(request, 'contributions/contributions.html', context)


def add_recycle(request):
    """
    View to handle User creating Recycle Action
    """

    if request.method == 'POST':
        form = RecycleForm(request.POST)
        if form.is_valid():
            recycle = form.save(commit=False)
            recycle.profile = request.user
            recycle.save()
            return redirect(reverse('home'))
    recycle_form = RecycleForm()
    reuse_form = ReuseForm()
    reduce_form = ReduceForm()

    template = 'contributions/contributions.html'
    context = {
        'recycle_form': recycle_form,
        'reuse_form': reuse_form,
        'reduce_form': reduce_form,
    }

    return render(request, template, context)


def add_reduce(request):
    """
    View to handle User creating Recycle Action
    """

    if request.method == 'POST':
        form = ReduceForm(request.POST)
        if form.is_valid():
            reduce = form.save(commit=False)
            reduce.profile = request.user
            reduce.save()
            return redirect(reverse('home'))
    recycle_form = RecycleForm()
    reuse_form = ReuseForm()
    reduce_form = ReduceForm()

    template = 'contributions/contributions.html'
    context = {
        'recycle_form': recycle_form,
        'reuse_form': reuse_form,
        'reduce_form': reduce_form,
    }

    return render(request, template, context)


def add_reuse(request):
    """
    View to handle User creating Recycle Action
    """

    if request.method == 'POST':
        form = ReuseForm(request.POST)
        if form.is_valid():
            reuse = form.save(commit=False)
            reuse.profile = request.user
            reuse.save()
            return redirect(reverse('home'))
    recycle_form = RecycleForm()
    reuse_form = ReuseForm()
    reduce_form = ReduceForm()

    template = 'contributions/contributions.html'
    context = {
        'recycle_form': recycle_form,
        'reuse_form': reuse_form,
        'reduce_form': reduce_form,
    }

    return render(request, template, context)
