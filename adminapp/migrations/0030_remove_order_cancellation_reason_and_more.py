# Generated by Django 5.1.1 on 2024-11-02 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0029_alter_review_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cancellation_reason',
        ),
        migrations.RemoveField(
            model_name='order',
            name='return_reason',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='cancellation_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='return_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('order_recieved', 'Order Recieved'), ('packed', 'Packed'), ('shipped', 'Shipped'), ('in_transit', 'In Transit'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='order_recieved', max_length=20),
        ),
    ]
