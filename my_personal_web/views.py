from django.shortcuts import render, redirect
# from .forms import ContactForm
from .models import Contact
from django.conf import  settings
import os
from django.http import FileResponse


def my_porfolio(request):
    return render(request, 'index.html')



def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        product = request.POST.get('product')

        # ✅ Create and save the contact message
        contact_message = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            product=product
        )

        # No need to call save() again, .create() already saves the object
        # contact_message.save()  ← remove this

        # ✅ redirect() takes only a URL or route name, not request + template
        return render(request, 'index.html', {
            'success': True,
            'name': name,
        })

    # ✅ For GET requests
    return render(request, 'index.html')




def download_cv(request):
    file_pathh = os.path.join(settings.BASE_DIR, 'static', 'assets', 'files', 'Ofem_Patrick_CV.pdf')
    return FileResponse(open(file_pathh, 'rb'), as_attachment=True, filename='CV.pdf')