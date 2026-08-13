from django.db import models
from django.urls import reverse


class SiteSettings(models.Model):
    company_name = models.CharField("Firma adı", max_length=120, default="Taşcan Mühendislik")
    tagline = models.CharField("Kısa slogan", max_length=180, default="Geleceği sağlam temellerle inşa ediyoruz.")
    phone = models.CharField("Telefon", max_length=40, default="+90 312 000 00 00")
    email = models.EmailField("E-posta", default="info@tascanmuhendislik.com")
    address = models.CharField("Adres", max_length=240, default="Çankaya, Ankara")
    about_text = models.TextField(
        "Hakkımızda metni",
        default=(
            "Taşcan Mühendislik; güvenli, verimli ve sürdürülebilir yapılar için "
            "mühendisliği tasarımla buluşturan çözüm ortağınızdır."
        ),
    )
    updated_at = models.DateTimeField("Güncellenme tarihi", auto_now=True)

    class Meta:
        verbose_name = "Site ayarları"
        verbose_name_plural = "Site ayarları"

    def __str__(self):
        return self.company_name


class Service(models.Model):
    title = models.CharField("Başlık", max_length=120)
    slug = models.SlugField("URL adı", max_length=140, unique=True)
    short_description = models.CharField("Kısa açıklama", max_length=220)
    description = models.TextField("Açıklama", blank=True)
    icon = models.CharField("İkon harfi", max_length=3, default="01", help_text="Kartta görünecek kısa işaret")
    order = models.PositiveIntegerField("Sıra", default=0)
    is_active = models.BooleanField("Yayında", default=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetler"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField("Proje adı", max_length=140)
    slug = models.SlugField("URL adı", max_length=160, unique=True)
    category = models.CharField("Kategori", max_length=80, default="Mühendislik")
    summary = models.CharField("Kısa özet", max_length=220)
    details = models.TextField("Proje detayları", blank=True)
    location = models.CharField("Lokasyon", max_length=100, default="Ankara")
    year = models.PositiveIntegerField("Yıl", default=2025)
    accent = models.CharField("Vurgu rengi", max_length=20, default="#f26a3d", help_text="Örn: #f26a3d")
    is_featured = models.BooleanField("Ana sayfada göster", default=True)
    order = models.PositiveIntegerField("Sıra", default=0)

    class Meta:
        ordering = ["order", "-year"]
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})


class ContactMessage(models.Model):
    name = models.CharField("Ad soyad", max_length=120)
    email = models.EmailField("E-posta")
    phone = models.CharField("Telefon", max_length=40, blank=True)
    subject = models.CharField("Konu", max_length=160, blank=True)
    message = models.TextField("Mesaj")
    is_read = models.BooleanField("Okundu", default=False)
    created_at = models.DateTimeField("Gönderim tarihi", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "İletişim mesajı"
        verbose_name_plural = "İletişim mesajları"

    def __str__(self):
        return f"{self.name} — {self.subject or 'Yeni mesaj'}"
