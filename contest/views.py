from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContestForm
from .models import Contest


def proposal(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Contest, pk=pk)
    else:
        instance = None

    form = ContestForm(request.POST or None, instance=instance)
    context = {'form': form}

    if form.is_valid():
        if '/delete/' in request.path:
            instance.delete()
            return redirect('contest:list')
        else:
            contest = form.save()
            context['contest_id'] = contest.id

    return render(request, 'contest/form.html', context)


def proposal_list(request):
    contests = Contest.objects.order_by('id')
    context = {'contests': contests}
    return render(request, 'contest/list.html', context)