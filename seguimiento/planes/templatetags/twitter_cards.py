from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('twitter_cards/summary_card.html')
def summary_card(*args, **kwargs):
    card = {'card': 'summary',
            'site': kwargs.get('site', getattr(settings, 'TWITTER_CARD_SITE', None)),
            'title': kwargs.get('title', None),
            'description': kwargs.get('description', None)}

    return card
