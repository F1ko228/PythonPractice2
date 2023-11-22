from django.db import models
#from formatChecker import ContentTypeRestrictedFileField

from users.models import User
# Create your models here.

class ApplicationCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = 'Application Categories'

    def __str__(self):
        return self.name

class ApplicationStatus(models.Model):
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = 'Application Statuses'

    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=125)
    imageofapp = models.ImageField(upload_to='applications_image')
    description = models.TextField(max_length=256)
    category = models.ForeignKey(ApplicationCategory, on_delete=models.CASCADE)
    status = models.ForeignKey(ApplicationStatus, on_delete=models.CASCADE, default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name} | {self.category.name}'




# class UsersApplications(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     application = models.ForeignKey(Application, on_delete=models.CASCADE)
#     status = models.ForeignKey(ApplicationStatus, on_delete=models.CASCADE, default=1)
#
#     def __str__(self):
#         return f'Заявки пользователя {self.user.username} | Заявка {self.application.name}'



