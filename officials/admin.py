from django.contrib import admin
from .models import Organization, Club, Official,  OrganizationUserPermissions, Assignor, Assignment, Team, Game, AgeDivision

class OrganizationPermsInLine(admin.TabularInline):
    model = OrganizationUserPermissions
    # extra = 1

class AssignmentInLine(admin.TabularInline):
    model = Assignment

class TeamInLine(admin.TabularInline):
    model = Team

class OrganizationAdmin(admin.ModelAdmin):
    inlines = (OrganizationPermsInLine,)

class GameAdmin(admin.ModelAdmin):
    inlines = (AssignmentInLine,)

class OfficialAdmin(admin.ModelAdmin):
    inlines = (AssignmentInLine,)

class ClubAdmin(admin.ModelAdmin):
    inlines = (TeamInLine,)

# Register your models here.
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Official, OfficialAdmin)
admin.site.register(Assignor)
admin.site.register(Game, GameAdmin)
admin.site.register(AgeDivision)
