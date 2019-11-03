from django.db import models


class Field(models.Model):
    big_int = models.BigIntegerField(max_length=512)
    binary = models.BinaryField(max_length=512)
    boolean = models.BooleanField
    char = models.CharField(max_length=512)
    date = models.DateField(max_length=512)
    date_time = models.DateTimeField(max_length=512)
    decimal = models.DecimalField(max_digits=9, decimal_places=2)
    duration = models.DurationField(max_length=512)
    email = models.EmailField(max_length=512)
    file = models.FileField()
    file_path = models.FilePathField(path='C:/Users/dLnnnnnn/Desktop', match='1.')
    float_field = models.FloatField(max_length=512)
    image = models.ImageField()
    integer = models.IntegerField(max_length=512)
    generic_ip = models.GenericIPAddressField()
    null = models.NullBooleanField()
    positive_integer = models.PositiveIntegerField(max_length=512)
    positive_small_integer = models.PositiveSmallIntegerField(max_length=512)
    slug = models.SlugField(max_length=512)
    small_integer = models.SmallIntegerField(max_length=512)
    text = models.TextField(max_length=1024)
    time = models.TextField(max_length=512)
    URL = models.URLField(max_length=256)
    UUID = models.UUIDField(max_length=512)
