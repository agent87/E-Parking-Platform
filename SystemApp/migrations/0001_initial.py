# Generated by Django 4.0 on 2022-02-10 12:30

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.SmallAutoField(db_column='CustomerId', editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(db_column='CompanyName', max_length=50)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=50, null=True)),
                ('enrollment_date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name_plural': 'Customers',
                'db_table': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Gates',
            fields=[
                ('gate_id', models.AutoField(db_column='GateId', editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='Name', max_length=50)),
                ('status', models.CharField(db_column='Status', max_length=50)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=50, null=True)),
                ('camera_id', models.CharField(blank=True, db_column='CameraId', max_length=50, null=True)),
                ('cashiers', models.JSONField(blank=True, db_column='Cashiers', null=True)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemApp.customers')),
            ],
            options={
                'verbose_name_plural': 'Gates',
                'db_table': 'Gates',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.SmallAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('phonenum', models.CharField(blank=True, db_column='PhoneNum', max_length=30, null=True)),
                ('role', models.CharField(blank=True, max_length=50, null=True)),
                ('mail_verified', models.CharField(max_length=50)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemApp.customers')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'db_table': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Tarrif',
            fields=[
                ('tarrif_id', models.AutoField(db_column='TarrifId', primary_key=True, serialize=False)),
                ('from_time', models.BigIntegerField(db_column='FromTime')),
                ('to_time', models.BigIntegerField(db_column='ToTime')),
                ('cost', models.FloatField(blank=True, db_column='Cost', null=True)),
                ('datetime', models.DateTimeField(db_column='Date', default=django.utils.timezone.now)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemApp.customers')),
            ],
            options={
                'verbose_name_plural': 'Tarrifs',
                'db_table': 'Tarrif',
                'ordering': ('from_time', 'to_time'),
            },
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('date', models.DateField(db_column='Date', default=datetime.datetime(2022, 2, 10, 12, 30, 43, 915363, tzinfo=utc))),
                ('subscription_id', models.BigAutoField(db_column='SubscriptionId', primary_key=True, serialize=False)),
                ('plate_number', models.CharField(db_column='PlateNumber', max_length=50)),
                ('start_date', models.DateField(db_column='start')),
                ('end_date', models.DateField(db_column='end')),
                ('amount', models.FloatField(db_column='SubscriptionAmount')),
                ('name', models.CharField(blank=True, db_column='Name', max_length=50, null=True)),
                ('phone_number', models.CharField(db_column='ContactNumber', max_length=50)),
                ('comments', models.TextField(blank=True, db_column='Comments', max_length=100, null=True)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemApp.customers')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemApp.users')),
            ],
            options={
                'verbose_name_plural': 'Subscription',
                'db_table': 'Subscriptions',
            },
        ),
        migrations.CreateModel(
            name='Parkinglog',
            fields=[
                ('ticket_id', models.BigAutoField(db_column='TicketId', primary_key=True, serialize=False)),
                ('date', models.DateField(db_column='Date', default=datetime.datetime(2022, 2, 10, 12, 30, 43, 917364, tzinfo=utc))),
                ('plate_number', models.CharField(db_column='PlateNum', max_length=50)),
                ('checkin_method', models.CharField(db_column='CheckInMethod', default='Manual', max_length=10)),
                ('checkin_time', models.BigIntegerField(db_column='CheckinTime')),
                ('checkout_time', models.BigIntegerField(blank=True, db_column='CheckoutTime', null=True)),
                ('parked', models.BooleanField(blank=True, db_column='Parked', null=True)),
                ('duration', models.BigIntegerField(blank=True, db_column='Duration', null=True)),
                ('cost', models.BigIntegerField(blank=True, db_column='Cost', null=True)),
                ('amount_payed', models.BigIntegerField(blank=True, db_column='AmountPayed', null=True)),
                ('checkout_method', models.CharField(blank=True, db_column='CheckoutMethod', max_length=10, null=True)),
                ('payment_method', models.CharField(blank=True, db_column='PaymentMethod', max_length=50, null=True)),
                ('checkin_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkin_user', to='SystemApp.users')),
                ('checkout_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkout_user', to='SystemApp.users')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SystemApp.customers')),
                ('entry_gate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_gate', to='SystemApp.gates')),
                ('exit_gate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exit_gate', to='SystemApp.gates')),
                ('subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SystemApp.subscriptions')),
            ],
            options={
                'verbose_name_plural': 'Parking logs',
                'db_table': 'ParkingLog',
                'ordering': ('-checkin_time',),
            },
        ),
    ]
