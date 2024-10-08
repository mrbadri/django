# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Home Page!")


from django.shortcuts import render
from .forms import ContactForm


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
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            
            # پردازش داده‌ها
            print(f"Name: {name}, Message: {message}")
            
            return render(request, 'thanks.html', {'name': name})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


