from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.





class User(AbstractUser):
    
    user_image  = models.ImageField(upload_to='posts/img/'
                              , blank=True, null=True)
    description = models.TextField(null=True)
    location    = models.TextField()



class Domains(models.Model):
    domainid  = models.AutoField(primary_key=True)
    domain_name = models.CharField(max_length=250)
    

    def __str__(self):
        return str(self.domain_name)


class Notebook(models.Model):
    notebookid   = models.AutoField(primary_key=True)
    notebookname = models.CharField(max_length=250, unique=True)
    userid       = models.ForeignKey(User, on_delete=models.CASCADE)
    domainid     = models.ForeignKey(Domains, on_delete=models.CASCADE)
    totaluservisited_all_chapters  = models.IntegerField(default=0)
    total_rating = models.IntegerField(default=0)
    added_date   = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)



    def __str__(self) -> str:
        return str(self.notebookname)

    # def get_absolute_url(self):
    #     return reverse("notebook:gp-detail", kwargs={"pk": self.pk})
    

class Notebookchapters(models.Model):
    notebookchaptersid         = models.AutoField(primary_key=True)
    notebookid                 = models.ForeignKey(Notebook, on_delete=models.CASCADE)
    chapter_name               = models.CharField(max_length=250)
    chapter_content            = models.TextField()
    totaluservisited_chapters  = models.IntegerField(default=0)
    total_rating               = models.IntegerField(default=0)
    added_date                 = models.DateTimeField(auto_now_add=True)
    updated_date               = models.DateTimeField(null=True)



    def __str__(self) -> str:
        return str(self.chapter_name)


class Usercomment(models.Model):
    usercommentid              = models.AutoField(primary_key=True)
    notebookid                 = models.ForeignKey(Notebook, on_delete=models.CASCADE)
    notebookchaptersid         = models.ForeignKey(Notebookchapters, on_delete=models.CASCADE)
    userid                     = models.ForeignKey(User, on_delete=models.CASCADE)
    comment                    = models.TextField()
    added_date                 = models.DateTimeField(auto_now_add=True)
    



    def __str__(self) -> str:
        return str(self.usercommentid)
