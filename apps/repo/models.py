from django.contrib.auth.models import User
from django.db import models


class Folder(models.Model):
    name = models.CharField('Name', max_length=255)
    parent = models.ForeignKey(
        'Folder', on_delete=models.CASCADE,
        null=True, blank=True
    )
    description = models.TextField('Description', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class DocumentVersion(models.Model):
    version = models.CharField('Version', max_length=11)
    content_file = models.FileField(
        'Content File', upload_to='content/%Y/%m/%d/'
    )
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'Document', on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.parent.name}:{self.version}'


class Document(models.Model):
    name = models.CharField('Name', max_length=255)
    parent = models.ForeignKey(
        'Folder', on_delete=models.CASCADE
    )
    description = models.TextField('Description', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    versions = models.ManyToManyField(
        DocumentVersion, blank=True
    )

    def __str__(self):
        return self.name
