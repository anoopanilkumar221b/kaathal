from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import random

def home(request):
    result = None  # Initialize result variable
    if request.method == "POST":
        name1 = request.POST.get('your_name')  # Get 'your_name' from the form
        name2 = request.POST.get('crush_name')  # Get 'crush_name' from the form

        # Generate a random love percentage between 70 and 100
        result = random.randint(70, 100)

        # Prepare the email content
        subject = "Love Calculator Result"
        message = f"Names entered:\nYour Name: {name1}\nCrush's Name: {name2}\n\nLove Compatibility: {result}% 💘"
        recipient_email = "your-email@gmail.com"  # Replace with your email address

        # Send the email
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient_email])

    # Render the template and pass the result to the template context
    return render(request, 'calculator/index.html', {'result': result})
