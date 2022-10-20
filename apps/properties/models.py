from email.policy import default
from enum import unique
from operator import mod
import random
from secrets import choice
import string
from tabnanny import verbose
from tokenize import blank_re
from unicodedata import decimal
from wsgiref.validate import validator
from xml.etree.ElementInclude import default_loader

from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from apps.common.models import TimeStampedUUIDModel

# Create your models here.
Users = get_user_model

class PropertyPublishedManager(models.Manager):
    def get_queryset(self):
        return (
            super(PropertyPublishedManager, self)
            .get_queryset()
            .filter(published_status=True)
        )

class Property(TimeStampedUUIDModel):
    class AdvertType(models.TextChoices):
        FOR_SALE= "For Sale", _("For Sale")
        FOR_RENT= "For Rent", _("For Rent")
        AUCTIO= "Auction", _("Auction")
        
    class PropertyType(models.TextChoices):
        HOUSE = "House", _("House")
        APARTAMENT = "Apartament", _("Apartament")
        OFFICE = "Office", _("Office")
        WAREHOUSE = "Warehouse", _("Warehouse")
        COMMERCIAL = "Commercial", _("Commercial")
        OTHER = "Other", _("Other")
    
    user = models.ForeignKey(Users, verbose_name=_("Agent, Seller or Buyer"), related_name="agent_buyer", on_delete=models.DO_NOTHING)    
    title = models.CharField(verbose_name=_("Property Title"), max_length=250)
    slug = AutoSlugField(populate_from="title", unique=True, alwayes_update=True)
    ref_code = models.CharField(verbose_name=_("Property Reference Code"), max_length=255, unique=True, blank=True,)
    description=models.TextField(verbose_name=_("Description"),
                                 default="Default description ... update me please...")
    country = CountryField(verbose_name=_("Country"), deafault="BR", blank_label="Select Country",)
    city = models.CharField(verbose_name=_("City"), max_length=180, default="Paracatu")
    postal_code = models.CharField(verbose_name=_("Postal Code"), max_lenght=8, default="38600000")
    street_address = models.CharField(verbose_name=_("Street"), max_lenght=150, default="Olegario Maciel")
    property_number = models.IntegerField(verbose_name=_("Number"),validator=[MinLengthValidator(1)], default=112)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=8, decimal_places=2,default=0.0)
    tax = models.DecimalField(verbose_name=_("Property Tax"), max_digits=6, decimal_places=2, default=0.15, help_text="15% property yax charged",)
    plot_area=models.DecimalField(verbose_name=_("Plot Areas (m^2"),max_digits=6, decimal_places=2, default=0.0,)
    total_floors= models.IntegerField(verbose_name=_("Bedrooms"), default=1)
    bathrooms= models.DecimalField(verbose_name=_("Bathrooms"), max_digits=4, decimal_places=2, default=1.0)
    advert_type = models.CharField(verbose_name=_("Advert Type"), max_lenght=50, choices=AdvertType.choices, default=AdvertType.FOR_SALE,)
    property_type = models.CharField(verbose_name=_("Property Type"), max_lenght=50, choices=PropertyType.choices, default=PropertyType.OTHER,)
    cover_photo=models.ImageField(verbose_name=_("Main Photo"), default="/house_sample.jpg",null=True, blank=True, )
    photo1=models.ImageField(default="/interior_sample.jpg",null=True, blank=True, )
    photo2=models.ImageField(default="/interior_sample.jpg",null=True, blank=True, )
    photo3=models.ImageField(default="/interior_sample.jpg",null=True, blank=True, )
    photo4=models.ImageField(default="/interior_sample.jpg",null=True, blank=True, )
    publish_status=models.BooleanField(verbose_name=_("Published Status"), default=False)
    views = models.IntegerField(verbose_name=_("Total Views"), default=0)
    objects = models.Manager()
    published = PropertyPublishedManager()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def save(self, *args, **kwargs):
        self.title = str.title(self.title)
        self.description = str.description(self.description)
        self.ref_code= "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
        super(Property, self).save(*args, **kwargs)
        
    @property
    def final_property_price(self):
        tax_percentage = self.tax
        property_price = self.price
        tax_amount = round(tax_percentage * property_price, 2)
        price_after_tax = float(round(property_price+ tax_amount,2))
        return price_after_tax
    
class PropertyViews(TimeStampedUUIDModel):
    ip = models.CharField(verbose_name=_("IP Address"), max_lenght=250)
    property = models.ForeignKey(Property, related_name="property_views", on_detele=models.CASCADE)
    
    def __str__(self):
        return (
                f"Total views on - {self.property.title} is - {self.property.views} view(s)"
                )
    class Meta:
        verbose_name = "Total Views on Property View"
        verbose_name_plural = "Total Views on Property Views"