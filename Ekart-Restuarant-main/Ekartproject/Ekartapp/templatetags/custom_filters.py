from django import template
import math

register = template.Library()

@register.filter(name='star_rating')
def star_rating(rating):
    if not isinstance(rating, int):
        rating = round(rating)  # Round the rating to the nearest integer
    filled_stars = '★' * rating
    empty_stars = '☆' * (5 - rating)
    return filled_stars + empty_stars
