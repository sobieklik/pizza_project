# Generated by Django 2.2.12 on 2020-05-12 21:45

from django.db import migrations, models
import django.db.models.deletion
import pizza.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Dodatkowy składnik')),
            ],
            options={
                'verbose_name': 'Dodatkowy składnik',
                'verbose_name_plural': 'Dodatkowe składniki',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nazwa')),
            ],
            options={
                'verbose_name': 'Napój',
                'verbose_name_plural': 'Napoje',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nazwa')),
                ('category', models.CharField(choices=[('CASSEROLES', 'Zapiekanki'), ('PASTAS', 'Makarony'), ('DINNERS', 'Dania obiadowe'), ('PANCAKES', 'Naleśniki'), ('SOUPS', 'Zupy'), ('SALADS', 'Sałatki'), ('SNACKS', 'Przekąski'), ('KEBAB', 'Kebab'), ('FASTFOODS', 'Fast food')], default='MEAL.CASSEROLES', max_length=20, verbose_name='Kategoria')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Opis')),
                ('change_meat', models.BooleanField(default=False, verbose_name='Wybór mięsa')),
                ('change_chips', models.BooleanField(default=False, verbose_name='Wybór frytek')),
            ],
            options={
                'verbose_name': 'Potrawa',
                'verbose_name_plural': 'Potrawy',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=pizza.models.Pizza.get_number, unique=True, verbose_name='Numer')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nazwa')),
                ('description', models.CharField(max_length=200, verbose_name='Opis')),
            ],
            options={
                'verbose_name_plural': 'Pizze',
            },
        ),
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, unique=True, verbose_name='Cena')),
            ],
            options={
                'verbose_name': 'Sos',
                'verbose_name_plural': 'Sosy',
            },
        ),
        migrations.CreateModel(
            name='UUID',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sauce_SIZE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nazwa')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sauce_product', to='pizza.Sauce')),
            ],
            options={
                'verbose_name': 'Sos',
                'verbose_name_plural': 'Sosy',
            },
        ),
        migrations.CreateModel(
            name='Pizza_SIZE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cena')),
                ('size', models.CharField(choices=[('GIGA', 'Gigant'), ('MEGA', 'Mega'), ('BIG', 'Duża'), ('SMALL', 'Mała')], default='SIZES.GIGA', max_length=20, verbose_name='Rozmiar')),
                ('sauce', models.IntegerField(default=1, verbose_name='Ilość sosów')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_product', to='pizza.Pizza')),
                ('uuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='uuid_Pizza', to='pizza.UUID')),
            ],
            options={
                'verbose_name': 'Rozmiar i cena',
                'verbose_name_plural': 'Rozmiar i cena',
                'unique_together': {('model', 'size')},
            },
        ),
        migrations.CreateModel(
            name='Food_SIZE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cena')),
                ('size', models.CharField(choices=[('BIG', 'Duża'), ('SMALL', 'Mała')], default='SIZES.BIG', max_length=20, verbose_name='Porcja')),
                ('sauce', models.IntegerField(default=0, verbose_name='Ilość sosów')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_product', to='pizza.Food')),
                ('uuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='uuid_Food', to='pizza.UUID')),
            ],
            options={
                'verbose_name': 'Rozmiar i cena',
                'verbose_name_plural': 'Rozmiar i cena',
                'unique_together': {('model', 'size')},
            },
        ),
        migrations.CreateModel(
            name='Drink_SIZE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cena')),
                ('capacity', models.CharField(default='500', max_length=5, verbose_name='Pojemność [ ml ]')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drink_product', to='pizza.Drink')),
                ('uuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='uuid_Drink', to='pizza.UUID')),
            ],
            options={
                'verbose_name': 'Pojemność i cena',
                'verbose_name_plural': 'Pojemność i cena',
                'unique_together': {('capacity', 'model')},
            },
        ),
        migrations.CreateModel(
            name='Additives_SIZE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('GIGA', 'Gigant'), ('MEGA', 'Mega'), ('BIG', 'Duża'), ('SMALL', 'Mała')], default='SIZES.GIGA', max_length=20, verbose_name='Dodatek do porcji')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cena')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additives_product', to='pizza.Additives')),
                ('uuid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='uuid_additives', to='pizza.UUID')),
            ],
            options={
                'verbose_name': 'Rozmiar i cena',
                'verbose_name_plural': 'Rozmiar i cena',
                'unique_together': {('model', 'size')},
            },
        ),
    ]