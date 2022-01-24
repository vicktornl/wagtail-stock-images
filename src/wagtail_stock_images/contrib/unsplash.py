from typing import List

from unsplash.api import Api
from unsplash.auth import Auth

from wagtail_stock_images import settings
from wagtail_stock_images.engine import AbstractSearchEngine
from wagtail_stock_images.types import Image


class UnsplashSearchEngine(AbstractSearchEngine):
    def get_client(self):
        auth = Auth(
            settings.UNSPLASH_CLIENT_ID,
            settings.UNSPLASH_CLIENT_SECRET,
            settings.UNSPLASH_REDIRECT_URI,
        )
        api = Api(auth)
        return api

    def get_image(self, id: str) -> Image:
        res = self.get_client().photo.get(id)
        image = self._serialize_image(res)
        return image

    def search_images(self, query: str) -> List[Image]:
        res = self.get_client().search.photos(query, page=1, per_page=25)
        images = [self._serialize_image(result) for result in res["results"]]
        return images

    def _serialize_image(self, data) -> Image:
        return Image(
            id=data.id,
            title=data.description if data.description else data.id,
            url=data.urls.raw,
            thumbnail=data.urls.thumb,
            tags=[],
        )
