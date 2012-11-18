from django.core.management.base import BaseCommand, CommandError

from aggregator import feed_updater

class Command(BaseCommand):
    help = 'Update all feeds'

    def handle(self, *args, **options):
        try:
            feed_updater.update_all()
        except Exception as e:
            raise CommandError("Something went wrong during update all: %s", e)

        self.stdout.write('Finished updating all feeds.')
