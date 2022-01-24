from django.http import Http404
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from wagtail.admin.forms.search import SearchForm

from wagtail_stock_images.utils import get_search_engine


class SaveStockImagesView(TemplateView):
    template_name = "wagtail_stock_images/save.html"

    def get(self, request, id, *args, **kwargs):
        search_engine = get_search_engine()

        try:
            image = search_engine.get_image(id)
        except Exception as err:
            raise Http404

        context = self.get_context_data(**kwargs)
        context.update(
            {
                "image": image,
            }
        )
        return self.render_to_response(context)


class SearchStockImagesView(TemplateView):
    template_name = "wagtail_stock_images/search.html"

    def get(self, request, *args, **kwargs):
        images = []
        query_string = None

        if "q" in request.GET:
            form = SearchForm(request.GET, placeholder=_("Search images"))
            if form.is_valid():
                query_string = form.cleaned_data["q"]
                search_engine = get_search_engine()
                images = search_engine.search_images(query_string)
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
