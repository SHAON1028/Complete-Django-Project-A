# Generated by Django 3.1.1 on 2020-09-16 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CourseManagement', '0001_initial'),
        ('StudentManagement', '0005_auto_20200916_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CourseManagement.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudentManagement.student')),
            ],
        ),
    ]
