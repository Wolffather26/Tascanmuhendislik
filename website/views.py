from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import ContactMessage, Project, Service, SiteSettings


def site_settings():
    return SiteSettings.objects.first() or SiteSettings()


def home(request):
    context = {
        "site": site_settings(),
        "services": Service.objects.filter(is_active=True)[:4],
        "projects": Project.objects.filter(is_featured=True)[:3],
    }
    return render(request, "website/home.html", context)


def project_list(request):
    return render(
        request,
        "website/projects.html",
        {"site": site_settings(), "projects": Project.objects.all()},
    )


def project_detail(request, slug):
    return render(
        request,
        "website/project_detail.html",
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
        messages.success(request, "Mesajınız alındı. En kısa sürede sizinle iletişime geçeceğiz.")
        return redirect("contact")
    return render(request, "website/contact.html", {"site": site})
