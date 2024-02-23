# type: ignore
from django.db import models

# Create your models here.


class Lawyer(models.Model):
    """
    Lawyer table
    """
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    phone = models.CharField(max_length=10, null=False)
    address = models.TextField(default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    zip_code = models.CharField(max_length=10, default='')
    # Will be a url for a file saved in aws cloud
    image_url = models.CharField(max_length=200, default='')
    specific_focus_areas = models.CharField(max_length=50, default='')
    # will be a file saved in aws cloud
    lawyer_resume = models.CharField(max_length=100, default='')
    lawyer_bio = models.TextField(default='')
    password_hash = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True,)
    lawyer_id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Lawyer'
        verbose_name = 'Lawyer'
        verbose_name_plural = 'Lawyers'


class Client(models.Model):
    """
    Client table
    """
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=False)

    phone = models.CharField(max_length=10, default='')
    address = models.TextField(default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    zip_code = models.CharField(max_length=10, default='')
    # Will be a url for a file saved in aws cloud
    image_url = models.CharField(max_length=100, default='')
    password_hash = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    client_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class Roles(models.Model):
    """
    Practice Areas
    """
    practice_area_id = models.AutoField(primary_key=True)
    practice_area_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'Roles'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class Lawyer_practice_areas(models.Model):
    """
    Lawyer Practice Areas table
    """
    lawyer_id = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    practice_area_id = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return self.lawyer_id

    class Meta:
        db_table = 'Lawyer_practice_areas'
        verbose_name = 'Lawyer Practice Area'
        verbose_name_plural = 'Lawyer Practice Areas'


class Reviews(models.Model):
    """
    Reviews table
    """
    lawyer_id = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    review = models.TextField()
    review_id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lawyer_id

    class Meta:
        db_table = 'Reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
