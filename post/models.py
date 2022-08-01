from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=False)
    content = models.TextField()

    def __str__(self):
        return self.title
