from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, password, **kwargs):

        if not email:
            raise ValueError("email is required.")

        if not password:
            raise ValueError("password is required.")

        user = self.model(email=self.normalize_email(
            email), name=name, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password, **kwargs):

        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        return self.create_user(email, name, password, **kwargs)
