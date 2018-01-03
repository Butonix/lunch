from django.db import models


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
        Returning name as string rep.
        """
        return self.name


class Article(AbstractTimeStamp):

    """
    An entry is like a blog post but 'post' sounds shit. Is related to :model:`publications.Category`
    and to :model:`users.User`.
    """

    STATUS_CHOICES = (
        ("published", "Published"),
        ("draft", "Draft")
    )

    cover = models.ImageField()
    title = models.CharField(max_length=140)
    subtitle = models.CharField(max_length=140)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft")
    keywords = models.CharField(max_length=140)
    body = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="articles")
    is_featured = models.BooleanField(default=False)
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        """
        Returning title and status as string rep.
        """
        return f'{self.title} {self.status}'


class Magazine(AbstractTimeStamp):

    """
    A magazine is a compilation of Articles, usually with a topic.
    Is related to :model:`publications.Article` and :model:`publications.Category`
    """

    cover = models.ImageField()
    name = models.CharField(max_length=140)
    info = models.TextField()
    articles = models.ManyToManyField(Article)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        """
        Returning the name as string rep.
        """
        return self.name
