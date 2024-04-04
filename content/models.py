from django.db import models

# Create your models here.


class Todo(models.Model):

    Title = models.CharField(max_length=225)

    completed = models.BooleanField(default=False)

    Date = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.Title
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
