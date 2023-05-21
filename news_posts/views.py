import requests
from news import settings
from django.views.generic import ListView


def get_response():
    url = settings.URL
    response = requests.get(url).json()['articles']
    return response


class NewsView(ListView):
    template_name = 'news_posts/index.html'
    paginate_by = 5
    context_object_name = 'news'

    def get_queryset(self):
        return get_response()


class SearchView(ListView):
    model = None
    template_name = 'news_posts/search.html'
    http_method_names = ['post', 'get']
    paginate_by = 5
    context_object_name = 'queryset'

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = []
            search_query = self.request.GET.get('search')
            if search_query:
                for i in get_response():
                    if search_query.lower() in i['title'].lower():
                        queryset.append(i)
                return queryset
            return get_response()
