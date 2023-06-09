# Generated by Django 4.2 on 2023-06-04 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('all_for_sale', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.SmallIntegerField(choices=[(1, 'Like'), (-1, 'Dislike')])),
                ('afs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_dislike', to='all_for_sale.afs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_dislike', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('afs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_AFS', to='all_for_sale.afs')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_AFS', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
