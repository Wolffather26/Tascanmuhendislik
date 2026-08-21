from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.i18n import set_language
from xml.sax.saxutils import escape

from .models import ContactMessage, Project, Service, SiteSettings


def site_settings():
    return SiteSettings.objects.first() or SiteSettings()


def home(request):
    context = {
        "site": site_settings(),
        "services": Service.objects.filter(is_active=True)[:4],
        "projects": Project.objects.filter(is_featured=True)[:3],
    }
    template = "website/en/home.html" if request.LANGUAGE_CODE == "en" else "website/home.html"
    return render(request, template, context)


def project_list(request):
    template = "website/en/projects.html" if request.LANGUAGE_CODE == "en" else "website/projects.html"
    return render(
        request,
        template,
        {"site": site_settings(), "projects": Project.objects.all()},
    )


def project_detail(request, slug):
    template = "website/en/project_detail.html" if request.LANGUAGE_CODE == "en" else "website/project_detail.html"
    return render(
        request,
        template,
        {"site": site_settings(), "project": get_object_or_404(Project, slug=slug)},
    )


def contact(request):
    site = site_settings()
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            phone=request.POST.get("phone", "").strip(),
            subject=request.POST.get("subject", "").strip(),
            message=request.POST.get("message", "").strip(),
        )
        message = (
            "Your message has been received. We will get back to you shortly."
            if request.LANGUAGE_CODE == "en"
            else "Mesajınız alındı. En kısa sürede sizinle iletişime geçeceğiz."
        )
        messages.success(request, message)
        return redirect("contact")
    template = "website/en/contact.html" if request.LANGUAGE_CODE == "en" else "website/contact.html"
    return render(request, template, {"site": site})


def robots_txt(request):
    sitemap = request.build_absolute_uri("/sitemap.xml")
    return HttpResponse(
        f"User-agent: *\nAllow: /\nDisallow: /admin/\nDisallow: /i18n/\nSitemap: {sitemap}\n",
        content_type="text/plain",
    )


def sitemap_xml(request):
    base = request.build_absolute_uri("/").rstrip("/")
    urls = ["/", "/projeler/", "/iletisim/"]
    urls += [project.get_absolute_url() for project in Project.objects.all()]
    entries = "".join(f"<url><loc>{escape(base + path)}</loc></url>" for path in urls)
    xml = f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{entries}</urlset>'
    return HttpResponse(xml, content_type="application/xml")
