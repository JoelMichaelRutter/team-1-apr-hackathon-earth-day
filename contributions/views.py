from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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


@login_required
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
            # set custom toast/message level
            recycle_lvl = 50
            messages.add_message(
                request,
                recycle_lvl,
                f'Hail EaRRRth hero, your {recycle} -> {recycle.recycle_action} action has been saved'  # noqa ES501
            )
            return redirect(reverse('profile'))
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


@login_required
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
            # set custom toast/message level
            reduce_lvl = 60
            messages.add_message(
                request,
                reduce_lvl,
                f'Hail EaRRRth hero, your {reduce} -> {reduce.reduce_action} action has been saved'  # noqa ES501
            )
            return redirect(reverse('profile'))
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


@login_required
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
            # set custom toast/message level
            reuse_lvl = 70
            messages.add_message(
                request,
                reuse_lvl,
                f'Hail EaRRRth hero, your {reuse} -> {reuse.reuse_action} action has been saved'  # noqa ES501
            )
            return redirect(reverse('profile'))
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
