# Generated by Django 5.0.7 on 2025-06-23 09:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('report_type', models.CharField(choices=[('sales', 'Sales Report'), ('inventory', 'Inventory Report'), ('user_activity', 'User Activity Report'), ('vendor_performance', 'Vendor Performance Report'), ('transaction', 'Transaction Report')], max_length=20)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('filters', models.JSONField(blank=True, help_text='Additional filters applied to the report', null=True)),
                ('file_path', models.FileField(blank=True, null=True, upload_to='reports/')),
                ('is_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('generated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generated_reports', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserActivityLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('login', 'Login'), ('logout', 'Logout'), ('product_view', 'Product View'), ('product_create', 'Product Create'), ('product_update', 'Product Update'), ('product_delete', 'Product Delete'), ('order_create', 'Order Create'), ('order_update', 'Order Update'), ('cart_add', 'Cart Add'), ('cart_remove', 'Cart Remove'), ('profile_update', 'Profile Update')], max_length=20)),
                ('resource_type', models.CharField(blank=True, max_length=50, null=True)),
                ('resource_id', models.CharField(blank=True, max_length=50, null=True)),
                ('details', models.JSONField(blank=True, null=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
                'indexes': [models.Index(fields=['user', 'action'], name='reports_use_user_id_fd11fd_idx'), models.Index(fields=['created_at'], name='reports_use_created_31a3b0_idx')],
            },
        ),
    ]
