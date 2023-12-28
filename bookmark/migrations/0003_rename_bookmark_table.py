from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_auto_20190611_1204'),
    ]

    operations = [
        migrations.RenameModel('bookmark', 'bookmark_item')
    ]