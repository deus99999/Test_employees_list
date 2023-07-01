from django.db import models
from django.utils import timezone
#from mptt.models import MPTTModel, TreeForeignKey

# class Role(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=100)
#     role_level = models.IntegerField(default=1)
#
#     def __str__(self):
#        return self.title


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    hire_date = models.DateField(default=timezone.now)
    position = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subordinates')

    def __str__(self):
        return self.name

    def get_hierarchy(self):
        if self.subordinates.all():
            name = self.name
            email = self.email
            hire_date = self.hire_date
            position = self.position
            manager = self.manager
            subordinates = []

            for subordinate in self.subordinates.all():
                subordinates.append(subordinate.get_hierarchy())


            hierarchy = {'name': name, 'email': email, 'hire_date': hire_date, 'position': position,
                         'manager': manager, 'subordinates': subordinates}

        else:
            hierarchy = {
                'name': self.name,
                'email': self.email,
                'hire_date': self.hire_date,
                'position': self.position,
                'manager': self.manager,
            }
        return hierarchy