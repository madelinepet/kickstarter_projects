from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator

from .models import Kickstarter


def kickstarter_list_view(request):
    kickstarters_query = get_list_or_404(Kickstarter)

    paginator = Paginator(kickstarters_query, 20)

    page = request.GET.get('page')
    kickstarters = paginator.get_page(page)

    context = {
        'kickstarters': kickstarters
    }
    return render(request, 'reviews/kickstarter.html', context=context)


def kickstarter_detail_view(request, pk=None):
    context = {
        'kickstarter': get_object_or_404(Kickstarter, id=pk)
    }
    return render(request, 'reviews/kickstarter_detail.html', context=context)
