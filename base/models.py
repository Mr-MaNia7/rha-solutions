from django.db import models

# Create your models here.

BS_CHOICES = {
    ('fas fa-headset', 'headset icon'),
    ('fas fa-briefcase', 'briefcase icon'),
}

class Header(models.Model):
    big_text = models.TextField(default="RHA Solutions PLC.")
    small_text =models.TextField(default="One of the few technology hubs in Ethiopia.")

    def __str__(self):
        return f"Service: {self.big_text}"

class Project(models.Model):
    title = models.TextField(default="Call Center")
    description = models.TextField(default="A full-fledged call center with the use of latest technologies")
    num = models.IntegerField(default=9)
    bs_icon = models.CharField(default="fas fa-headset", choices=BS_CHOICES, max_length=30)
    img = models.ImageField(default = "da-img-1.jpg",upload_to="project-img")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-created', '-updated']

    def __str__(self):
        return f"Project: {self.title}"

class Service(models.Model):
    title = models.TextField(default="Software Development")
    description = models.TextField(default="Long years of experience with technology and software development makes us deliver undeniably fruitfull projects")
    bs_icon = models.TextField(default="fas fa-briefcase")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Service: {self.title}"

class Feature(models.Model):
    title = models.TextField(default="Agile")
    description = models.TextField(default="We work on our projects in an agile environment.")
    bs_icon = models.TextField(default="fas fa-briefcase")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Feauture: {self.title}"

class Sender(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30)
    message = models.TextField

    def __str__(self):
        return f"Sender: {self.first_name}"
