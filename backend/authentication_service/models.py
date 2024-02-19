from django.db import models

# Create your models here.


class Lawyer(models.Model):
    """
    Lawyer table
    """
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    image_url = models.CharField(max_length=100)
    specific_focus_ares = models.CharField(max_length=50)
    lawyer_resume = models.CharField(max_length=100)
    lawyer_bio = models.TextField()
    password_hash = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    lawyer_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lawyer'
        verbose_name_plural = 'Lawyers'


class Client(models.Model):
    """
    Client table
    """
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    image_url = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    client_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
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
        verbose_name = 'Lawyer Practice Area'
        verbose_name_plural = 'Lawyer Practice Areas'


class Reviews(models.Model):
    """
    Reviews table
    """
    lawyer_id = models.CharField(max_length=100)
    client_id = models.CharField(max_length=100)
    review = models.TextField()
    review_id = models.AutoField(primary_key=True)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lawyer_id

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
