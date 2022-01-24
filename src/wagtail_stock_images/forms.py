from django import forms
from django.utils.translation import gettext as _
from wagtail.core.models import Collection


class SaveImageForm(forms.Form):
    title = forms.CharField(max_length=255, label=_("Title"))
    collection = forms.ModelChoiceField(
        queryset=Collection.objects.all().prefetch_related("group_permissions"),
        label=_("Collection"),
    )
