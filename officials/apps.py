from django.apps import AppConfig
from django.contrib.auth import get_user_model

class OfficialsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'officials'

    def ready(this):
        from django.contrib.auth.models import User 
        
        def get_name_last_first(self):
            return self.last_name + ", " + self.first_name

        UserModel = get_user_model()
        UserModel.add_to_class("get_name_last_first", get_name_last_first)
