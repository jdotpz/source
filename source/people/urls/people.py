from django.conf import settings
from django.conf.urls.defaults import *
from django.views.decorators.cache import cache_page

from source.people.views import PersonList, PersonDetail

STANDARD_CACHE_TIME = getattr(settings, 'CACHE_MIDDLEWARE_SECONDS', 60*2)

urlpatterns = patterns('',
    url(
        regex = '^$',
        view = cache_page(PersonList.as_view(), STANDARD_CACHE_TIME),
        kwargs = {},
        name = 'person_list',
    ),
    url(
        regex = '^(?P<slug>[-\w]+)/$',
        view = cache_page(PersonDetail.as_view(), STANDARD_CACHE_TIME),
        kwargs = {},
        name = 'person_detail',
    ),
)
