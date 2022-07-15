# Generated by Django 3.2.2 on 2021-05-12 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_name', models.CharField(blank=True, max_length=100)),
                ('body', models.TextField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lesson_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='curriculam.lesson')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='WorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_days', to='curriculam.standard')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_time_slots', to='curriculam.standard')),
            ],
        ),
        migrations.CreateModel(
            name='SlotSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots_days', to='curriculam.workingdays')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots_time', to='curriculam.timeslots')),
                ('slot_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots_subject', to='curriculam.subject')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_slots', to='curriculam.standard')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply_body', models.TextField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='curriculam.comment')),
            ],
        ),
    ]
