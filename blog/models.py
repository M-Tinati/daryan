from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="نام خبر")
    content = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="blog/", verbose_name="تصویر خبر")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
