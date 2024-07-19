# Generated by Django 4.2.14 on 2024-07-19 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="users/usuario_defeco.jpg",
                        upload_to="users/",
                        verbose_name="Imagen de perfil",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="dirección"
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="localidad"
                    ),
                ),
                (
                    "telephone",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Teléfono"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuario",
                    ),
                ),
            ],
            options={
                "verbose_name": "Perfil",
                "verbose_name_plural": "Perfiles",
                "ordering": ["-id"],
            },
        ),
    ]