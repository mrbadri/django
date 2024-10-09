from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def home(request):
    context = {
        'title': 'صفحه اصلی',
        'message': 'این یک پیام پویا است که از view ارسال شده است.'
    }
    return render(request, 'home.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # ذخیره اطلاعات فرم در پایگاه داده
             # آماده‌سازی داده‌ها برای تمپلیت
            email_subject = 'پیام جدید از طریق فرم تماس'
            email_body = render_to_string('contact_email.html', {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'message': form.cleaned_data['message'],
            })
            user_email = form.cleaned_data['email']

            # ارسال ایمیل
            send_mail(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [user_email],  # ایمیلی که پیام به آن ارسال می‌شود
                fail_silently=False,
                html_message=email_body  # اینجا پیام را به صورت HTML ارسال می‌کنیم
            )
            messages.success(request, 'پیام شما با موفقیت ارسال شد!')
            return redirect('thanks')  # هدایت به صفحه تشکر پس از ذخیره موفقیت‌آمیز
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')


# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Home Page!")



# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             message = form.cleaned_data['message']
            
#             # پردازش داده‌ها
#             print(f"Name: {name}, Message: {message}")
            
#             return render(request, 'thanks.html', {'name': name})
#     else:
#         form = ContactForm()
#     return render(request, 'contact.html', {'form': form})