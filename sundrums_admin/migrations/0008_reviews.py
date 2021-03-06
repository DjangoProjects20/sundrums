# Generated by Django 2.1 on 2018-08-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sundrums_admin', '0007_teacher_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='None', max_length=64, null=True, verbose_name=' фио кто оставил отзыв')),
                ('image', models.ImageField(blank=True, help_text='фото', upload_to='static/media/reviews_images/', verbose_name='фото оставившего отзыв')),
                ('text_review', models.CharField(blank=True, default='None', max_length=2054, null=True, verbose_name='текст отзыва ')),
                ('prof_reviewrs', models.CharField(blank=True, default='None', max_length=64, null=True, verbose_name='профессия того кто оставил отзыв ')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'отзывы',
            },
        ),
    ]
