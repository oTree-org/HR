# Generated by Django 3.1.7 on 2021-03-16 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hr', '0003_auto_20210316_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('config_json', models.TextField(default='')),
                ('session_wide_url', models.CharField(max_length=255)),
                ('admin_url', models.CharField(max_length=255)),
                ('num_participants', models.IntegerField()),
                ('study_id', models.CharField(max_length=255, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='hr.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prolific_pid', models.CharField(max_length=255)),
                ('study_id', models.CharField(max_length=255)),
                ('prolific_sid', models.CharField(max_length=255, unique=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prolific.session')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]