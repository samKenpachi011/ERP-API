# Generated by Django 3.2.20 on 2023-07-25 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('hired_date', models.DateField(blank=True, null=True)),
                ('identity_type', models.CharField(blank=True, choices=[('country_id', 'Country ID number'), ('passport', 'Passport'), ('birth_certificate', 'Birth Certificate'), ('OTHER', 'Other')], max_length=50)),
                ('highest_qualification', models.CharField(blank=True, choices=[('None', 'None'), ('primary', 'Primary'), ('junior_secondary', 'Junior Secondary'), ('senior_Secondary', 'Senior Secondary'), ('diploma', 'Diploma'), ('graduate_certificate', 'Graduate certificate'), ('associates_degree', 'Associates degree'), ('graduate_diploma', 'Graduate diploma'), ('tertiary', 'Tertiary'), ('bachelor_degree', 'Bachelor degree'), ('masters_degree', 'Masters degree'), ('doctoral_degree', 'Doctoral degree'), ('phd', 'PhD'), ('postdoctoral', 'Postdoctoral')], max_length=50)),
                ('postal_address', models.CharField(blank=True, max_length=200)),
                ('emp_code', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.department')),
            ],
        ),
    ]