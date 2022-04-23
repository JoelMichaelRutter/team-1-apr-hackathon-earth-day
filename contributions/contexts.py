from .models import Recycle, Reuse, Reduce

def actions_context(request):
    """
    Make action objects count available across app
    """
    recycle_objects = list(Recycle.objects.all())
    reuse_objects = list(Reuse.objects.all())
    reduce_objects = list(Reduce.objects.all())

    recycle_count = len(recycle_objects)
    reuse_count = len(reuse_objects)
    reduce_count = len(reduce_objects)

    return {
        'recycle_actions': recycle_objects,
        'reuse_actions': reuse_objects,
        'reduce_actions': reduce_objects,
        'recycle_count': recycle_count,
        'reduce_count': reduce_count,
        'reuse_count': reuse_count,
    }
