from django.db import models

# Category model


class Category(models.Model):
    """
    Model for categories. Each instance is a category.
    """

    name = models.CharField(max_length=20)


class Post(models.Model):
    """
    Model for all posts. Each instance is a post with title, body, and dates
    of creation and modification. Also has a many to many relation to
    Categories.
    """

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")


class Comment(models.Model):
    """
    Model for all comments. Each instance is a comment with author, body,
    created_on, and the post it is related to is a ForeignKey.
    """

    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
