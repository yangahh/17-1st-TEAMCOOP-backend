# Generated by Django 3.1.6 on 2021-02-16 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'activity_levels',
            },
        ),
        migrations.CreateModel(
            name='AgeLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'age_levels',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='DietaryHabit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'dietary_habits',
            },
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'diseases',
            },
        ),
        migrations.CreateModel(
            name='GenderCode',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'gender_codes',
            },
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('icon', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'goals',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('sub_name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=3000)),
                ('image_url', models.CharField(max_length=2000)),
                ('nutrition_url', models.CharField(max_length=2000)),
                ('is_default', models.BooleanField(default=False)),
                ('care_smoker', models.BooleanField(default=False)),
                ('care_drinker', models.BooleanField(default=False)),
                ('activity_level', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.activitylevel')),
                ('age_level', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.agelevel')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='VeganLevel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'vegan_levels',
            },
        ),
        migrations.CreateModel(
            name='RelatedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard_product', to='product.product')),
                ('standard_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_product', to='product.product')),
            ],
            options={
                'db_table': 'related_products',
            },
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=20, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'product_stocks',
            },
        ),
        migrations.CreateModel(
            name='ProductGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.goal')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'product_goals',
            },
        ),
        migrations.CreateModel(
            name='ProductDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.disease')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'product_diseases',
            },
        ),
        migrations.CreateModel(
            name='ProductDietaryHabit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dietary_habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.dietaryhabit')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'product_dietary_habits',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='dietary_habit',
            field=models.ManyToManyField(through='product.ProductDietaryHabit', to='product.DietaryHabit'),
        ),
        migrations.AddField(
            model_name='product',
            name='disease',
            field=models.ManyToManyField(through='product.ProductDisease', to='product.Disease'),
        ),
        migrations.AddField(
            model_name='product',
            name='gender_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.gendercode'),
        ),
        migrations.AddField(
            model_name='product',
            name='goal',
            field=models.ManyToManyField(through='product.ProductGoal', to='product.Goal'),
        ),
        migrations.AddField(
            model_name='product',
            name='vegan_level',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.veganlevel'),
        ),
        migrations.AddField(
            model_name='category',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.menu'),
        ),
    ]
