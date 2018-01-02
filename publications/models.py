from django.db import models

from users import models as user_models

class AbstractTimeStamp(models.Model):

    """
    An Abstract Model useful to extend from it and
    time stamp all the other models.
    """ 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(AbstractTimeStamp):

    """
    A category to be able to classify the entries
    """

    name = models.CharField(max_length=140)
    photo = models.ImageField()


    def __str__(self):
        """
        Returning name as string representation
        """
        return self.name


class Article(AbstractTimeStamp):

    """
    An entry on the website. Is related to :model:`publications.Category`
    and to :model:`users.User`.
    """

    STATUS_CHOICES = (
        ("published", "Published"),
        ("draft", "Draft")
    )

    title = models.CharField(max_length=140)
    subtitle = models.CharField(max_length=140)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default="draft")
    keywords = models.CharField(max_length=140)
    article = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="articles")
    is_featured = models.BooleanField(default=False)
    author = models.ForeignKey(
        user_models.User, on_delete=models.CASCADE, related_name='articles')

    
    def __str__(self):
        """
        Returning title and status as string representation
        """
        return f'{self.title} {self.status}'



