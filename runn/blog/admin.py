from django.contrib import admin
from .models import Blog
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
class BlogAdminForm(forms.ModelForm):
    Content=forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model=Blog
        fields='__all__'
class BlogAdmin(admin.ModelAdmin):
    form=BlogAdminForm
    
# Register your models here.
admin.site.register(Blog,BlogAdmin)
