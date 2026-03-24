from django.db import migrations


def ensure_ticketbooking_table(apps, schema_editor):
    TicketBooking = apps.get_model("main", "TicketBooking")
    table_names = schema_editor.connection.introspection.table_names()
    if TicketBooking._meta.db_table not in table_names:
        schema_editor.create_model(TicketBooking)


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(ensure_ticketbooking_table, reverse_code=noop_reverse),
    ]
