# Generated by Django 3.0.7 on 2020-08-30 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'get_latest_by': 'id', 'ordering': ['-article_order', '-pub_time'], 'verbose_name': 'article', 'verbose_name_plural': 'article'},
        ),
        migrations.AlterModelOptions(
            name='blogsettings',
            options={'verbose_name': 'Website configuration', 'verbose_name_plural': 'Website configuration'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'classification', 'verbose_name_plural': 'classification'},
        ),
        migrations.AlterModelOptions(
            name='links',
            options={'ordering': ['sequence'], 'verbose_name': 'Links', 'verbose_name_plural': 'Links'},
        ),
        migrations.AlterModelOptions(
            name='sidebar',
            options={'ordering': ['sequence'], 'verbose_name': 'Sidebar', 'verbose_name_plural': 'Sidebar'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'label', 'verbose_name_plural': 'label'},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_order',
            field=models.IntegerField(default=0, verbose_name='Sort, the higher the number, the higher the front'),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=mdeditor.fields.MDTextField(verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='classification'),
        ),
        migrations.AlterField(
            model_name='article',
            name='comment_status',
            field=models.CharField(choices=[('o', 'turn on'), ('c', 'shut down')], default='o', max_length=1, verbose_name='Comment status'),
        ),
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation time'),
        ),
        migrations.AlterField(
            model_name='article',
            name='last_mod_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified time'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='release time'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'draft'), ('p', 'publish')], default='p', max_length=1, verbose_name='Article status'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='Label collection'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.CharField(choices=[('a', 'article'), ('p', 'page')], default='a', max_length=1, verbose_name='Types of'),
        ),
        migrations.AlterField(
            model_name='article',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='Pageviews'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='analyticscode',
            field=models.TextField(default='', max_length=1000, verbose_name='Website Statistics Code'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='article_sub_length',
            field=models.IntegerField(default=300, verbose_name='Article summary length'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='beiancode',
            field=models.CharField(blank=True, default='', max_length=2000, null=True, verbose_name='case number'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='gongan_beiancode',
            field=models.TextField(blank=True, default='', max_length=2000, null=True, verbose_name='Public Security Record Number'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='google_adsense_codes',
            field=models.TextField(blank=True, default='', max_length=2000, null=True, verbose_name='Advertising content'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='open_site_comment',
            field=models.BooleanField(default=True, verbose_name='Whether to open website comment function'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='resource_path',
            field=models.CharField(default='/var/www/resource/', max_length=300, verbose_name='Static file storage address'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='show_gongan_code',
            field=models.BooleanField(default=False, verbose_name='Whether to display the public security record number'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='show_google_adsense',
            field=models.BooleanField(default=False, verbose_name='Whether to show Google ads'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='sidebar_article_count',
            field=models.IntegerField(default=10, verbose_name='Number of sidebar articles'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='sidebar_comment_count',
            field=models.IntegerField(default=5, verbose_name='Number of sidebar comments'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='site_description',
            field=models.TextField(default='', max_length=1000, verbose_name='Site description'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='site_keywords',
            field=models.TextField(default='', max_length=1000, verbose_name='Site keywords'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='site_seo_description',
            field=models.TextField(default='', max_length=1000, verbose_name='Website SEO description'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='sitename',
            field=models.CharField(default='', max_length=200, verbose_name='Site name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation time'),
        ),
        migrations.AlterField(
            model_name='category',
            name='last_mod_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified time'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Category name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Parent category'),
        ),
        migrations.AlterField(
            model_name='links',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation time'),
        ),
        migrations.AlterField(
            model_name='links',
            name='is_enable',
            field=models.BooleanField(default=True, verbose_name='Whether to show'),
        ),
        migrations.AlterField(
            model_name='links',
            name='last_mod_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified time'),
        ),
        migrations.AlterField(
            model_name='links',
            name='link',
            field=models.URLField(verbose_name='link address'),
        ),
        migrations.AlterField(
            model_name='links',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Link name'),
        ),
        migrations.AlterField(
            model_name='links',
            name='sequence',
            field=models.IntegerField(unique=True, verbose_name='Sort'),
        ),
        migrations.AlterField(
            model_name='links',
            name='show_type',
            field=models.CharField(choices=[('i', 'Home'), ('l', 'List'), ('p', 'Article page'), ('a', 'Full Site'), ('s', 'Friendship link page')], default='i', max_length=1, verbose_name='Display type'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation time'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='is_enable',
            field=models.BooleanField(default=True, verbose_name='Whether to enable'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='last_mod_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified time'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='name',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='sidebar',
            name='sequence',
            field=models.IntegerField(unique=True, verbose_name='Sort'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='created_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation time'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='last_mod_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Modified time'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='Label name'),
        ),
    ]
