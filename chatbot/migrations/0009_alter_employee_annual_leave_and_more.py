# Generated by Django 5.1.3 on 2024-12-10 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0008_alter_employee_bereavement_leave_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='annual_leave',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='bereavement_leave',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='maternity_leave',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='paternity_leave',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sick_leave',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='toil',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
