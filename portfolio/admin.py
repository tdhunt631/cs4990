from django.contrib import admin
from portfolio.models import CaseStudy

class CaseStudyAdmin(admin.ModelAdmin):
	list_display = ('title', 'description',)	

admin.site.register(CaseStudy, CaseStudyAdmin)
