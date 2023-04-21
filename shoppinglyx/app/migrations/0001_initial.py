# Generated by Django 4.2 on 2023-04-19 11:51

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
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("locality", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=200)),
                ("zipcode", models.IntegerField()),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Maharashtra", "Maharashtra"),
                            ("Bihar", "Bihar"),
                            ("Uttar Pradesh", "Uttar Pradesh"),
                            ("Telangana", "Telangana"),
                            ("Karnataka", "Karnataka"),
                            ("Kerala", "Kerala"),
                            ("Madhya Pradesh", "Madhya Pradesh"),
                            ("Orissa", "Orissa"),
                            ("Gujrat", "Gujrat"),
                            ("Rajasthan", "Rajasthan"),
                            ("Haryana", "Haryana"),
                            ("Punjab", "Punjab"),
                            ("Himachal Pradesh", "Himachal Pradesh"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("selling_price", models.FloatField()),
                ("discounted_price", models.FloatField()),
                ("description", models.TextField()),
                ("brand", models.CharField(max_length=100)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("M", "Mobile"),
                            ("L", "Laptop"),
                            ("TW", "Top Wear"),
                            ("BW", "Bottom Wear"),
                        ],
                        max_length=2,
                    ),
                ),
                ("product_image", models.ImageField(upload_to="product_img")),
            ],
        ),
        migrations.CreateModel(
            name="Order_Placed",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.DateTimeField(auto_now_add=True)),
                ("ordered_date", models.CharField(max_length=50)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Maharashtra", "Maharashtra"),
                            ("Bihar", "Bihar"),
                            ("Uttar Pradesh", "Uttar Pradesh"),
                            ("Telangana", "Telangana"),
                            ("Karnataka", "Karnataka"),
                            ("Kerala", "Kerala"),
                            ("Madhya Pradesh", "Madhya Pradesh"),
                            ("Orissa", "Orissa"),
                            ("Gujrat", "Gujrat"),
                            ("Rajasthan", "Rajasthan"),
                            ("Haryana", "Haryana"),
                            ("Punjab", "Punjab"),
                            ("Himachal Pradesh", "Himachal Pradesh"),
                        ],
                        default="Pending",
                        max_length=50,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.customer"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
