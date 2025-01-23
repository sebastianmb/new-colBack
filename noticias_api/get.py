from django.contrib.auth.models import User

superusers = User.objects.filter(is_superuser=True)
for user in superusers:
    print(user.username)
