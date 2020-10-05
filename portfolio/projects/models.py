from django.db import models

# Projects model


class Projects(models.Model):
    """
    Projects model class for the projects app.

    Each instance describes a Project, with it's own distictive title, it's
    description, techonlogy used, and image of it working.
    """

    title = models.CharField(max_length=100)
    description = models.TextField()
    techonlogy = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")
