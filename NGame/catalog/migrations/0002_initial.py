# Generated by Django 5.0.6 on 2024-07-08 21:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.cart'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.game'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.game'),
        ),
        migrations.AddField(
            model_name='like',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.game'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'game')},
        ),
    ]
