from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives, BadHeaderError
from django.template.loader import render_to_string
from django.contrib import messages
from django.utils.html import strip_tags
from portfolio.models import ContactMessage, Project, Skill, Experience, Education, Home, Profile
from .forms import ProfileForm
import os
import logging

# Logger for debugging and error tracking
logger = logging.getLogger(__name__)


def home(request):
    try:
        home = Home.objects.first()
        profile = Profile.objects.first()
    except Exception:
        logger.exception("Failed to load home data.")
        home = profile = None
    return render(request, 'portfolio/home.html', {
        "profile": profile,
        "home": home
    })


def about(request):
    try:
        profile = Profile.objects.first()
        skills = Skill.objects.all()
        experiences = Experience.objects.all()
        education = Education.objects.all()
    except Exception:
        logger.exception("Failed to load about data.")
        messages.error(request, "Something went wrong while loading the About page.")
        profile = skills = experiences = education = None
    return render(request, 'portfolio/about.html', {
        "skills": skills,
        "experiences": experiences,
        "education": education,
        "profile": profile
    })


def projects(request):
    try:
        projects = Project.objects.all()
    except Exception:
        logger.exception("Failed to load projects.")
        messages.error(request, "Could not load projects at the moment.")
        projects = []
    return render(request, 'portfolio/projects.html', {"projects": projects})


def contact(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            if not all([name, email, subject, message]):
                messages.error(request, "All fields are required.")
                return redirect("contact")

            if ContactMessage.objects.filter(email=email, subject=subject, message=message).exists():
                messages.warning(request, "You have already submitted this message.")
                return redirect("contact")

            # Save message in database
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            # === Send email to admin ===
            try:
                admin_context = {
                    'name': name,
                    'email': email,
                    'subject': subject,
                    'message': message,
                }
                admin_html = render_to_string('portfolio/emails/contact_admin_email.html', admin_context)
                admin_text = strip_tags(admin_html)

                admin_email = EmailMultiAlternatives(
                    subject=subject,
                    body=admin_text,
                    from_email=email,
                    to=[os.getenv("EMAIL_HOST_USER")]
                )
                admin_email.attach_alternative(admin_html, "text/html")
                admin_email.send()
            except BadHeaderError:
                logger.error("Invalid header found in admin email.")
                messages.error(request, "Invalid email header.")
                return redirect("contact")
            except Exception:
                logger.exception("Failed to send admin email.")
                messages.error(request, "Failed to send your message. Please try again later.")
                return redirect("contact")

            # === Send acknowledgment to user ===
            try:
                # Extract first name only
                first_name = name.strip().split()[0].title()

                user_context = {'name': first_name}
                user_html = render_to_string('portfolio/emails/contact_user_ack.html', user_context)
                user_text = strip_tags(user_html)

                user_email = EmailMultiAlternatives(
                    subject="Thank you for Contacting Me",
                    body=user_text,
                    from_email="no-reply@asileayuba.com",
                    to=[email]
                )
                user_email.attach_alternative(user_html, "text/html")
                user_email.send(fail_silently=True)
            except Exception:
                logger.warning(f"Failed to send acknowledgment to {email}")

            messages.success(request, "Your message has been sent! I'll get back to you soon.")
            return redirect("contact")

        except Exception:
            logger.exception("Unexpected error in contact view.")
            messages.error(request, "An unexpected error occurred. Please try again.")
            return redirect("contact")

    return render(request, 'portfolio/contact.html')


def upload_profile(request):
    profile = None
    try:
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save()
                messages.success(request, "Profile uploaded successfully.")
            else:
                messages.error(request, "Please correct the errors in the form.")
        else:
            form = ProfileForm()
    except Exception:
        logger.exception("Failed to upload profile.")
        messages.error(request, "There was an error uploading your profile.")
        form = ProfileForm()

    return render(request, 'portfolio/upload_profile.html', {
        "form": form,
        "profile": profile
    })
