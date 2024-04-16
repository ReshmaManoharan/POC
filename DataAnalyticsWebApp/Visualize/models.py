from django.db import models

class CountryQuery(models.Manager):
    
    def get_queryset(self, **kwargs):
        return super(CountryQuery, self).get_queryset().filter(**kwargs)

class Country(models.Model):
    name = models.CharField(max_length=255)

    #override the default manager model of usings Organization.Objects.all()
    #objects = QueryManager()
    objects = CountryQuery()

    class Meta:
        verbose_name = "country"

    def __str__(self):
        return self.name
    
class IndustryQuery(models.Manager):
    
    def get_queryset(self, **kwargs):
        return super(IndustryQuery, self).get_queryset().filter(**kwargs)
    
class Industry(models.Model):
    name = models.CharField(max_length=255)

    objects = IndustryQuery()
    
    class Meta:
        verbose_name = "industry"

    def __str__(self):
        return self.name

class Organization(models.Model):
    organization_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    website = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name="indus")
    founded = models.IntegerField()
    no_of_employees = models.IntegerField()
 
    class Meta:
        verbose_name = "organization"

    def __str__(self):
        return self.name


# #overrides manager api which a way of interaction between models and db.
# class QueryManager(models.Manager):
#     #overrides the default queryset from manager class
#     def get_queryset(self):
#         return super(QueryManager, self).get_queryset().filter(country="")
