# Generated by Plain 0.21.4 on 2025-02-11 18:03

import plain.models.functions.text
import plain.passwords.models
import plain.passwords.validators
from plain import models
from plain.models import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.PrimaryKeyField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "password",
                    plain.passwords.models.PasswordField(
                        validators=[
                            plain.passwords.validators.MinimumLengthValidator(),
                            plain.passwords.validators.CommonPasswordValidator(),
                            plain.passwords.validators.NumericPasswordValidator(),
                        ]
                    ),
                ),
                ("is_admin", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                plain.models.functions.text.Lower("email"), name="unique_lower_email"
            ),
        ),
    ]
