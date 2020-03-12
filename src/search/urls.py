from django.conf.urls import url

from .views import (    http_example,
        fexample, CExample,
        book_list, BookList,
        BookDetail,
        read_arg, read_kwarg, ReadArg, ReadKwarg,
        SearchBooks,
    )

# f in the link name, is used for function based view, otherwise class based view

urlpatterns = [
    [...]

    url(r'^searchfromurl/(?P<urlsearch>[\w-]+)/$', SearchBooks.as_view(),
            name="searchfromurl"), # search item received from url
]