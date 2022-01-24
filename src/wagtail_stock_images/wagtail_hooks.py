from django.templatetags.static import static
from django.urls import include, path, re_path, reverse
from django.utils.html import format_html, format_html_join
from django.utils.translation import gettext as _
from wagtail.admin.menu import Menu, MenuItem, SubmenuMenuItem
from wagtail.core import hooks

from wagtail_stock_images import settings as wagtail_stock_images_settings
from wagtail_stock_images import views

wagtail_stock_images_menu = Menu(
    register_hook_name="register_wagtail_stock_images_menu_item",
    construct_hook_name="construct_wagtail_stock_images_menu",
)


class WagtailStockImagesMenuItem(MenuItem):
    def is_shown(self, request):
        return True


@hooks.register("register_admin_urls")
def register_urls():
    return [
        path(
            "%s/<str:id>/" % wagtail_stock_images_settings.PATH_PREFIX,
            views.SaveStockImagesView.as_view(),
            name="wagtail-stock-images-save",
        ),
        path(
            "%s/" % wagtail_stock_images_settings.PATH_PREFIX,
            views.SearchStockImagesView.as_view(),
            name="wagtail-stock-images-search",
        ),
    ]


@hooks.register("register_admin_menu_item")
def register_menu():
    return SubmenuMenuItem(
        wagtail_stock_images_settings.MENU_LABEL,
        wagtail_stock_images_menu,
        classnames="icon icon-image",
        order=wagtail_stock_images_settings.MENU_ORDER,
    )


@hooks.register("register_wagtail_stock_images_menu_item")
def register_menu_item():
    return WagtailStockImagesMenuItem(
        _("Search"),
        reverse("wagtail-stock-images-search"),
        classnames="icon icon-search",
        order=0,
    )
