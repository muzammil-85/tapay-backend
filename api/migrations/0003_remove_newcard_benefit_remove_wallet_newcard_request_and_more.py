# Generated by Django 4.1.1 on 2022-12-17 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_bus_canteen_cart_events_fee_type_fees_igoal_library_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newcard',
            name='benefit',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='newcard_request',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='total_history',
        ),
        migrations.AddField(
            model_name='events',
            name='event_logo',
            field=models.ImageField(default='', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='others',
            name='company_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bus',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.total_history'),
        ),
        migrations.AlterField(
            model_name='canteen',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.total_history'),
        ),
        migrations.AlterField(
            model_name='canteen',
            name='notification',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='cart',
            name='available_card',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cart',
            name='book_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='cart',
            name='book_no',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='events',
            name='events_details',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='fee_type',
            name='admission_fee',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='fee_type',
            name='tution_spfee',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='fee_type',
            name='waiver_scheme',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='fees',
            name='fees_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fee_type'),
        ),
        migrations.AlterField(
            model_name='fees',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.total_history'),
        ),
        migrations.AlterField(
            model_name='library',
            name='book',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='library',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cart'),
        ),
        migrations.AlterField(
            model_name='library',
            name='date',
            field=models.DateField(max_length=150),
        ),
        migrations.AlterField(
            model_name='library',
            name='fine',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='library',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.total_history'),
        ),
        migrations.AlterField(
            model_name='library',
            name='time',
            field=models.TimeField(max_length=150),
        ),
        migrations.AlterField(
            model_name='newcard',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='newcard',
            name='card_image',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='newcard',
            name='charge',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='others',
            name='company_profile',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='others',
            name='igoal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.igoal'),
        ),
        migrations.AlterField(
            model_name='paylater',
            name='limit',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='paylater',
            name='spend',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id_card',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='store',
            name='date',
            field=models.DateField(max_length=15),
        ),
        migrations.AlterField(
            model_name='store',
            name='history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.total_history'),
        ),
        migrations.AlterField(
            model_name='store',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='store',
            name='time',
            field=models.TimeField(max_length=15),
        ),
        migrations.AlterField(
            model_name='total_history',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='total_history',
            name='merchant',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='total_history',
            name='trans_mode',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='cashback',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='is_activate',
            field=models.BooleanField(max_length=15),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='limit_transaction',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='reward_point',
            field=models.IntegerField(),
        ),
    ]