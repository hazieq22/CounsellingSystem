# Generated by Django 4.2.6 on 2023-10-18 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_remove_tracking_status_tracking_details_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=100, null=True)),
                ('followup', models.TextField(default='No', max_length=10)),
                ('sessionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.session')),
                ('studentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.student')),
            ],
        ),
    ]
