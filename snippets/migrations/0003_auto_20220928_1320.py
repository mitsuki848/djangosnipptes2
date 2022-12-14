# Generated by Django 3.2 on 2022-09-28 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_alter_comment_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
        migrations.AlterModelTable(
            name='snippet',
            table='snippets',
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='タグ名')),
                ('snippets', models.ManyToManyField(related_name='tags', related_query_name='tag', to='snippets.Snippet')),
            ],
            options={
                'db_table': 'tags',
            },
        ),
    ]
