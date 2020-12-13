from django.db import models

# Create your models here.


class Page(models.Model):
    work_img1 = models.FileField(null=True, blank=True)
    work_img2 = models.FileField(null=True, blank=True)
    my_img = models.FileField(null=True, blank=True)
    icon = models.FileField(null=True, blank=True)
    icon2 = models.FileField(null=True, blank=True)
    my_name = models.CharField(max_length=256, null=True, blank=True)
    my_info = models.TextField(null=True, blank=True)
    icon_info = models.CharField(null=True, blank=True, max_length=256)
    icon2_info = models.CharField(null=True, blank=True, max_length=256)
    f_name = models.CharField(null=True, blank=True, max_length=256)
    l_name = models.CharField(null=True, blank=True, max_length=256)
    email = models.CharField(null=True, blank=True, max_length=256)
    message = models.TextField(null=True, blank=True)
    btn = models.CharField(null=True, blank=True, max_length=256)
    ins_icon = models.FileField(null=True, blank=True)
    ins = models.CharField(null=True, blank=True, max_length=256)
    tg_icon = models.FileField(null=True, blank=True)
    tg = models.CharField(null=True, blank=True, max_length=256)
    gmail_icon = models.FileField(null=True, blank=True)
    gmail = models.CharField(null=True, blank=True, max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.my_name

    class Meta:
        verbose_name = "Page Item"
        verbose_name_plural = "Pages Items"


class Menu(models.Model):
    menu_name = models.CharField(null=True, blank=True, max_length=256)
    link = models.CharField(null=True, blank=True, max_length=256)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.menu_name

    class Meta:
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"


class Client(models.Model):
    first_name = models.CharField(null=True, blank=True, max_length=256)
    last_name = models.CharField(null=True, blank=True, max_length=256)
    client_email = models.EmailField(null=True, blank=True)
    topic = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Client Info"
        verbose_name_plural = "Client Infos"