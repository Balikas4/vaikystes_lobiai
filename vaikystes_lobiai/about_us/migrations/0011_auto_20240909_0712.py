from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0010_alter_dailyroutine_options_remove_dailyroutine_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyroutine',
            name='activities',
        ),
    ]
