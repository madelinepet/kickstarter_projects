from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.paginator import Paginator
from .models import Kickstarter


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def kickstarter_list_view(request):
    """ This is the function defining the list view of all kickstarters in a
    paginated way with 20 items per page.
    """
    kickstarters_query = get_list_or_404(Kickstarter)

    paginator = Paginator(kickstarters_query, 20)

    page = request.GET.get('page')
    kickstarters = paginator.get_page(page)

    # import pdb; pdb.set_trace()

    context = {
        'kickstarters': kickstarters
    }
    return render(request, 'reviews/kickstarter_list.html', context)


def kickstarter_detail_view(request, pk=None):
    """ This is the function defining the detail view for each kickstarter
    """
    context = {
        'kickstarter': get_object_or_404(Kickstarter, id=pk)
    }
    return render(request, 'reviews/kickstarter_detail.html', context)
