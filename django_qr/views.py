from django.shortcuts import render

from django_qr.settings import BASE_DIR
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings


def generate_qr(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            url = form.cleaned_data['url']

            # Generate QRcode
            qr = qrcode.make(url)
            file_name = name.replace(' ', '_').lower() + '.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)
            qr_url = os.path.join(settings.MEDIA_URL, file_name)

            context = {
                'file_name': file_name,
                'name': name,
                'qr_url': qr_url
            }
            return render(request, 'view_qr.html', context)
    else:
        form = QRCodeForm()
        context = {
            'form': form
        }
        return render(request, 'generate_qr.html', context)


def home(request):
    return render(request, 'home.html')