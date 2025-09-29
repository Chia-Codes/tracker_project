from django.db import migrations
from django.db.models import Count


def dedupe_cyclelog(apps, schema_editor):
    CycleLog = apps.get_model('tracker', 'CycleLog')
    dups = (CycleLog.objects
            .values('user_id','date')
            .annotate(c=Count('id'))
            .filter(c__gt=1))

    for row in dups:
        logs = list(CycleLog.objects
                    .filter(user_id=row['user_id'], date=row['date'])
                    .order_by('-id')) 
        keep, extras = logs[0], logs[1:]
        for extra in extras:
            if (not keep.notes) and extra.notes:
                keep.notes = extra.notes
            if (not keep.symptom) and extra.symptom:
                keep.symptom = extra.symptom
            extra.delete()
        keep.save()


class Migration(migrations.Migration):
    dependencies = [
        ('tracker', '0002_usersheet'),
    ]
    operations = [
        migrations.RunPython(dedupe_cyclelog, migrations.RunPython.noop),
    ]
