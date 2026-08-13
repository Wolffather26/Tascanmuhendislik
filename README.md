# Taşcan Mühendislik

Kurumsal web sitesi ve içerik yönetim paneli için ayrı Django projesi.

## Başlatma

```bash
../TuruncuPDKS/.venv/bin/python -m pip install -r requirements.txt
../TuruncuPDKS/.venv/bin/python manage.py migrate
../TuruncuPDKS/.venv/bin/python manage.py createsuperuser
../TuruncuPDKS/.venv/bin/python manage.py runserver
```

- Web sitesi: http://127.0.0.1:8000/
- Yönetim paneli: http://127.0.0.1:8000/admin/
