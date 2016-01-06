from django.contrib import admin
from flashnews.models import Category, Participant, Emergency, News

class ParticipantInline(admin.TabularInline):
    model = Participant

class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ParticipantInline,
    ]

admin.site.register(Category, CategoryAdmin)

class EmergencyInline(admin.TabularInline):
    model = Emergency

class NewsInline(admin.TabularInline):
    model = News

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('org_name', 'slug',)
    list_editable = ('slug',)
    prepopulated_fields = {'slug': ('org_name',)}
    inlines = [
        EmergencyInline,
        NewsInline,
    ]

admin.site.register(Participant, ParticipantAdmin)

class EmergencyAdmin(admin.ModelAdmin):
    list_display = ('participant', 'the_parent_category', '__unicode__', 'school_related', 'testing', 'updated',)
    list_filter = ['school_related', 'testing', ]

admin.site.register(Emergency, EmergencyAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('participant', 'the_parent_category', '__unicode__', 'school_related', 'testing', 'updated',)
    list_filter = ['school_related', 'testing',]

admin.site.register(News, NewsAdmin)
