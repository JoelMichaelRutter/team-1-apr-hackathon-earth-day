from .models import Recycle, Reuse, Reduce

def actions_context(request):
    """
    Make action objects count available across app
    """
    recycle_objects = Recycle.objects.all()
    reuse_objects = Reuse.objects.all()
    reduce_objects = Reduce.objects.all()

    return {
        'recycle_actions': recycle_objects,
        'reuse_actions': reuse_objects,
        'reduce_actions': reduce_objects,
    }
