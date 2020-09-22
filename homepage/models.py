from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class File(MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    options = [('FILE', 'file'), ('FOLDER', 'folder')]
    option = models.CharField(max_length=6, choices=options, default='FILE')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name