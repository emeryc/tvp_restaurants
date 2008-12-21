from django.contrib.comments.signals import comment_will_be_posted

def comment_added(sender, **kwargs):
    comment = kwargs["comment"]
    if not comment.user:
        comment.is_public = False


comment_will_be_posted.connect(comment_added)