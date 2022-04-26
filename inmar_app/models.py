from django.db import models


class Common(models.Model):
    """
    Common to use date creation
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)


class Location(Common):
    location = models.CharField(max_length=120)

    def __str__(self):
        return self.location


class Department(Common):
    department = models.CharField(max_length=120)

    def __str__(self):
        return self.department


class Category(Common):
    category = models.CharField(max_length=120)

    def __str__(self):
        return self.category


class SubCategory(Common):
    subcategory = models.CharField(max_length=120)

    def __str__(self):
        return self.subcategory


class Store(Common):
    sku = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)


