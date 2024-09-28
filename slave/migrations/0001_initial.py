# Generated by Django 4.0.6 on 2023-10-01 13:31

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
            name='file',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=100)),
                ('p_id', models.ForeignKey(blank=True, db_column='p_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='slave.file')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isf', models.BooleanField()),
                ('isc', models.BooleanField()),
                ('fid', models.IntegerField()),
                ('u_id', models.ForeignKey(db_column='u_id', on_delete=django.db.models.deletion.CASCADE, to='slave.users')),
            ],
        ),
        migrations.CreateModel(
            name='link_list',
            fields=[
                ('l_id', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('remark', models.CharField(default='none', max_length=100)),
                ('p_id', models.ForeignKey(db_column='p_id', on_delete=django.db.models.deletion.CASCADE, to='slave.file')),
                ('u_id', models.ForeignKey(db_column='u_id', on_delete=django.db.models.deletion.CASCADE, to='slave.users')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='u_id',
            field=models.ForeignKey(blank=True, db_column='u_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='slave.users'),
        ),
    ]
