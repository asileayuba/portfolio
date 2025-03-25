from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.html import strip_tags
from portfolio.models import ContactMessage, Project, Skill, Experience, Education, Home, Profile
from .forms import ProfileForm
import os


def home(request):
    home = Home.objects.first()
    profile = Profile.objects.first()
    return render(request, 'portfolio/home.html', {
        "profile": profile,
        "home": home
    })


def about(request):
    profile = Profile.objects.first()  # Assuming only one profile exists
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    return render(request, 'portfolio/about.html', {
        "skills": skills,
        "experiences": experiences,
        "education": education,
        "profile": profile
    })


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {"projects": projects})


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        # Prevent duplicate messages
        if ContactMessage.objects.filter(email=email, subject=subject, message=message).exists():
            messages.warning(request, "You have already submitted this message.")
            return redirect("contact")

        # Save message in DB
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)

        # Email to Admin (You)
        full_message = f"Name: {name}\nEmail: {email}\n\n{message}"
        send_mail(
            subject,
            full_message,
            email,
            [os.getenv("EMAIL_HOST_USER")],  # Your email from environment variable
        )

        # Acknowledgement Email to Sender
        acknowledgement_subject = "Thank you for Contacting Me"
        acknowledgement_message = f"""
        Hello {name},

        Thank you for reaching out! I have received your message and will get back to you as soon as possible.
        If it's urgent, you can also connect with me via LinkedIn or 𝕏(Twitter).

        Best Regards,
        Asile Ayuba
        """

        send_mail(
            acknowledgement_subject,
            strip_tags(acknowledgement_message),
            "no-reply@asileayuba.com",  # No-reply email
            [email],
        )

        messages.success(request, "Your message has been sent! I'll get back to you soon.")
        return redirect("contact")

    return render(request, 'portfolio/contact.html')


def upload_profile(request):
    profile = None
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save()
    else:
        form = ProfileForm()

    return render(request, {"form": form, "profile": profile})
