from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=200)

    def __str__(self):
        return self.tag_name


class Game(models.Model):
    game_name = models.CharField(max_length=200)
    game_image_height = models.PositiveIntegerField()
    game_image_width = models.PositiveIntegerField()
    game_image = models.ImageField(upload_to='media/', height_field='game_image_height', width_field='game_image_width')
    game_url = models.CharField(max_length=200)
    game_added_date = models.DateField(default=timezone.now)
    game_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.game_name

    class Meta:
        ordering = ('game_added_date',)
