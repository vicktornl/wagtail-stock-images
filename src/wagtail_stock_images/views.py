from urllib.request import urlretrieve

from django.core.files import File
from django.core.files.images import get_image_dimensions
from django.http import Http404, HttpResponseRedirect, response
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import FormView, TemplateView
from wagtail.admin import messages
from wagtail.admin.forms.search import SearchForm
from wagtail.images import get_image_model

from wagtail_stock_images.forms import SaveImageForm
from wagtail_stock_images.utils import get_search_engine

WagtailImage = get_image_model()


class SaveStockImagesView(FormView):
    template_name = "wagtail_stock_images/save.html"
    form_class = SaveImageForm

    def get_image(self, id):
        search_engine = get_search_engine()
        try:
            image = search_engine.get_image(id)
        except Exception as err:
            raise Http404
        return image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"image": self.image})
        return context

    def get_initial(self):
        return {
            "title": self.image.title[:255],
        }

    def form_valid(self, form):
        remote_image = urlretrieve(self.image.url)
        with open(remote_image[0], "rb") as image_file:
            width, height = get_image_dimensions(image_file)
            wagtail_image = WagtailImage.objects.create(
                title=form.cleaned_data["title"],
                file=File(image_file),
                collection=form.cleaned_data["collection"],
                width=width,
                height=height,
            )
        messages.success(
            self.request, _("Stock image '{0}' saved.").format(self.image.id)
        )
        return HttpResponseRedirect(
            reverse("wagtailimages:edit", args=[wagtail_image.id])
        )

    def post(self, request, id, *args, **kwargs):
        self.image = self.get_image(id)
        return super().post(request, *args, **kwargs)

    def get(self, request, id, *args, **kwargs):
        self.image = self.get_image(id)
        return super().get(request, *args, **kwargs)


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
