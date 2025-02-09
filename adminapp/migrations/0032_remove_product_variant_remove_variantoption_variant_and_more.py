# Generated by Django 5.1.1 on 2024-11-05 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0031_alter_orderitem_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='variant',
        ),
        migrations.RemoveField(
            model_name='variantoption',
            name='variant',
        ),
        migrations.RemoveField(
            model_name='product',
            name='variant_option',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='image',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='adminapp.product')),
            ],
        ),
        migrations.AddField(
            model_name='cartitem',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.productvariant'),
        ),
        migrations.AddField(
            model_name='image',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='adminapp.productvariant'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.productvariant'),
        ),
        migrations.AddField(
            model_name='review',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='adminapp.productvariant'),
        ),
        migrations.DeleteModel(
            name='Variant',
        ),
        migrations.DeleteModel(
            name='VariantOption',
        ),
    ]
