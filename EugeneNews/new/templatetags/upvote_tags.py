from django import template

register = template.Library()


@register.simple_tag
def has_upvote(user, post):
    return user.id in list(post.upvote_set.all().value_list(user, flat=True))