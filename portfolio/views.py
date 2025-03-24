from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.html import strip_tags
from portfolio.models import ContactMessage, Project, Skill, Experience, Education, Home, Profile
import os


def home(request):
    home = Home.objects.first()
    profile = Profile.objects.first()
    return render(request, 'portfolio/home.html', {"profile": profile,
                                                   'home': home})

def about(request):
    profile = Profile.objects.first()  # Assuming only one profile exists
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    return render(request, 'portfolio/about.html', {'skills': skills, 
                                                    'experiences': experiences, 
                                                    'education': education,
                                                    'profile': profile})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        
        # Check if this message has already been submitted
        if ContactMessage.objects.filter(email=email, subject=subject,message=message).exists():
            messages.warning(request, "You have already submitted this message.")
            return redirect("contact")  # Redirect to prevent resubmission
        
        # Save the message to the database
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
        
        # Format message
        full_message = f"Name: {name}\nEmail: {email}\n\n{message}"
        
        # Send message to me
        send_mail(
            subject,
            full_message,
            email,  # Sender email
            [os.getenv("EMAIL_HOST_USER")], # Send to my email
        )
        
        # Send acknowledgement email to the sender
        acknowledgement_subject = "Thank you for Contacting Me"
        acknowledgement_message = f"Hello {name},\n\nThank you for reaching out! I have received your message and will get back to you as soon as possible.\nIf it's urgent, you can also connect with me via LinkedIn or 𝕏(Twitter).\n\nBest Regards,\nAsile Ayuba"
        
        send_mail(
            acknowledgement_subject,
            acknowledgement_message,
            "no-reply@asileayuba.com",  # Use a no-reply email 
            [email],  # Send to the user
        )
        
        messages.success(request, "Your message has been sent! I'll get back to you soon.")
        return redirect("contact")
        
    return render(request, 'portfolio/contact.html')