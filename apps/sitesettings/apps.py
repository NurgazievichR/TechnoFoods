from django.apps import AppConfig


class SitesettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sitesettings'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .models import SiteSettings

        def create_default_settings(sender, **kwargs):
            if not SiteSettings.objects.exists():
                SiteSettings.objects.create()

        post_migrate.connect(create_default_settings, sender=self)
