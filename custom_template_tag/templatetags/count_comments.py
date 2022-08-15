from django import template

register = template.Library()


@register.simple_tag(name="count_comments")
def count_comments(parent_comment, child_comment):
    """
    Counting the number of comments without sending too much queries to database
    """
    numberOfComments = int(parent_comment) + int(child_comment)
    return numberOfComments
