from django.db import models

class About(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=100)
    address = models.TextField() 
    phone = models.IntegerField()
    email = models.EmailField()
    resume = models.FileField(upload_to='resume/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Education(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()  
    start_time = models.DateField()
    end_time = models.DateField()
    descriptions = models.TextField()
    
    def __str__(self):
        return f'{self.name}' 

class Experience(models.Model):        
    name = models.CharField(max_length=100)
    address = models.TextField()  
    start_time = models.DateField()
    end_time = models.DateField()
    descriptions = models.TextField()
    
    def __str__(self):
        return f'{self.name}' 

class Skill(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=100)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title}'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'
    
class Links(models.Model):
     key = models.CharField(max_length=100)
     Value = models.TextField()
     create_at = models.DateTimeField(auto_now_add=True)
        
     
     def __str__(self):
         return f'{self.key}'       
        
        