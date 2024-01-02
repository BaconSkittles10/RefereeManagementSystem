from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=1000)
    location = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

    @property
    def officials(self):
        return [o for o in Official.objects.all() for org in o.organizations if org == self]

class Club(models.Model):
    name = models.CharField(max_length=1000)
    location = models.CharField(max_length=5000)

    def __str__(self):
        return self.name

class OrganizationUserPermissions(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    name = models.CharField(max_length=1000)

    can_read_posts = models.BooleanField(default=True)
    can_make_posts = models.BooleanField(default=True)
    can_moderate_posts = models.BooleanField()

    can_assign_all_games = models.BooleanField()
    can_update_all_assignments = models.BooleanField()

    can_create_games = models.BooleanField()
    can_create_teams = models.BooleanField()

    def __str__(self):
        return self.organization.name + " - " + self.name


OFFICIAL_POSITIONS = [
    ("Center Referee", "Center Referee"),
    ("Assistant Referee 1", "Assistant Referee 1"),
    ("Assistant Referee 2", "Assistant Referee 2"),
    ("Fourth Official", "Fourth Official"),
    ("Shadow Referee", "Shadow Referee"),
    ("Assessor", "Assessor"),
    ("Additional Official", "Additional Official")
]
class Assignment(models.Model):
    game = models.ForeignKey("officials.Game", on_delete=models.CASCADE)
    official = models.ForeignKey("officials.Official", on_delete=models.CASCADE)
    position = models.CharField(max_length=1000, choices=OFFICIAL_POSITIONS)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.game} - {self.official} ({self.position})"

class Official(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    organizations_permissions = models.ManyToManyField(OrganizationUserPermissions, blank=True)

    level = models.CharField(max_length=1000)
    experience = models.CharField(max_length=1000, help_text="E.g. Amount of years or seasons you have been an official")

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.user.get_full_name()

    @property
    def organizations(self):
        return [o.organization for o in self.organizations_permissions.all()]

class Assignor(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)

    organizations_permissions = models.ManyToManyField(OrganizationUserPermissions, blank=True, help_text="Make sure that the user has assigning permissions.")
    
    def __str__(self):
        return self.user.get_full_name()

    @property
    def organizations(self):
        return [o.organization for o in self.organizations_permissions.all()]

class AgeDivision(models.Model):
    name = models.CharField(max_length=1000)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=1000)
    age_division = models.ForeignKey(AgeDivision, on_delete=models.SET_NULL, null=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.club} {self.name} ({self.age_division})"

class Game(models.Model):
    game_number = models.CharField(max_length=100)
    hosting_organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    age_division = models.ForeignKey(AgeDivision, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=5000)

    starting = models.DateTimeField()

    home_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="home")
    away_team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="away")

    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True) 

    def __str__(self):
        return self.game_number
