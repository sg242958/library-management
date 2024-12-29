from django.db import models

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(null=False)
    author = models.TextField(null=False)
    published_date = models.DateField(null=False)
    category = models.TextField(null=False)
    available_copies = models.IntegerField(null=False)

class Members(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(null=False)
    email = models.TextField(unique=True, null=False)
    membership_date = models.DateField(null=False)
    MEMBERSHIP_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    membership_status = models.CharField(
        max_length=10,
        choices=MEMBERSHIP_STATUS_CHOICES,
        default='Active',
    )

class BorrowRecords(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    borrow_date = models.DateField(null=False)
    return_date = models.DateField(null=True, blank=True)