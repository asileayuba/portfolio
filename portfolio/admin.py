from django.contrib import admin
from .models import ContactMessage, Project, Skill, Experience, Education, Profile, Home

# Define the admin model
class HomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_image')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'profile_image', 'resume')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'progress')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'created_at')
    list_filter = ('technologies', 'created_at')
    search_fields = ('title', 'technologies')
    ordering = ('-created_at',)

# Register the model with the custom admin class
admin.site.register(Home, HomeAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ContactMessage)
