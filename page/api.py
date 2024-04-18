from ninja import NinjaAPI

import page.models
from page.models import Page

api = NinjaAPI()


def to_dict(list_: list) -> dict:
    """
    Recursively creates a tree structure of pages

    list_ - List[QuerySet(Page)]
    """
    obj, *residual = list_
    if residual:
        return {"name": obj.name,
                "slug": obj.slug,
                "url": obj.url,
                "children": to_dict(residual)
                }
    else:
        return {"name": obj.name,
                "slug": obj.slug,
                "url": obj.url,
                "children": []
                }


@api.get("/pages/")
def get_structure_page(request, url: str):
    try:
        parents = Page.objects.get(url=url).get_ancestors(ascending=False, include_self=True)
    except page.models.Page.DoesNotExist:
        return {"message": "Sorry, url not correct("}

    return to_dict(parents)
