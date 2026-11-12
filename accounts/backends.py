from django.contrib.auth.backends import BaseBackend

from accounts.models import User

class EmailBackend(BaseBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):

        try:

            user_obj=User.objects.get(email=username)

            if user_obj.check_password(password):

                return user_obj

            else:

                return None

        except:

            return None

