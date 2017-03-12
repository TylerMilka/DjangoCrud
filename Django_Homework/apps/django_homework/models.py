
from django.db import models

# Create your models here.

class CodeSnippets(models.Model):
    name = models.CharField(max_length = 45)
    language = models.CharField(max_length = 45)
    code = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
