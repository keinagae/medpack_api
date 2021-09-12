from django.core.management.base import BaseCommand

from medpack.users.models import UserProfile, User


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        users=User.objects.all()
        for user in users:
            try:
                user.profile
            except Exception:
                UserProfile.objects.create(user=user)
