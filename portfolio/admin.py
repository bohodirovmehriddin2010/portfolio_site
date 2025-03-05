from django.contrib import admin
from .models import About, Education, Experience, Blog, Links, Skill, Contact
from unfold.admin import ModelAdmin


@admin.register(About)
class AboutAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'date_of_birth', 'country', 'address', 'phone', 'email', 'resume')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('country',)


@admin.register(Education)
class EducationAdmin(ModelAdmin):
    list_display = ('id', 'name', 'address', 'start_time', 'end_time', 'descriptions')
    search_fields = ('name',)
    list_filter = ('start_time', 'end_time')


@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    list_display = ('id', 'name', 'address', 'start_time', 'end_time', 'descriptions')
    search_fields = ('name',)
    list_filter = ('start_time', 'end_time')


@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ('id', 'name', 'value')
    search_fields = ('name',)
    list_filter = ('value',)


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('id', 'image', 'title', 'body', 'create_at')
    search_fields = ('title',)
    list_filter = ('create_at',)


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ('id',)
