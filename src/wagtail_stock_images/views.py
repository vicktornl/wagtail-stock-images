from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from unsplash.api import Api
from unsplash.auth import Auth
from wagtail.admin.forms.search import SearchForm

from wagtail_stock_images import settings


def get_unsplash_images(query_string):
    auth = Auth(
        settings.UNSPLASH_CLIENT_ID,
        settings.UNSPLASH_CLIENT_SECRET,
        settings.UNSPLASH_REDIRECT_URI,
    )
    api = Api(auth)
    images = api.search.photos(query_string, page=1, per_page=25)
    return images["results"]


class SearchStockImagesView(TemplateView):
    template_name = "wagtail_stock_images/search.html"

    def get(self, request, *args, **kwargs):
        images = []
        query_string = None
        if "q" in request.GET:
            form = SearchForm(request.GET, placeholder=_("Search images"))
            if form.is_valid():
                query_string = form.cleaned_data["q"]
                # TODO: Import string search engine (e.g. UnsplashSearchEngine)
                images = get_unsplash_images(query_string)
        else:
            form = SearchForm(placeholder=_("Search images"))

        context = self.get_context_data(**kwargs)
        context.update(
            {
                "images": images,
                "search_form": form,
                "query_string": query_string,
                "is_searching": bool(query_string),
            }
        )

        return self.render_to_response(context)
