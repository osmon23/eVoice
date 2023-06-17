# Generated by Django 4.2.2 on 2023-06-17 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('election', '0003_alter_election_election_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('age', models.PositiveIntegerField(verbose_name='age')),
                ('party', models.CharField(max_length=100, verbose_name='party')),
                ('experience', models.CharField(max_length=255, verbose_name='experience')),
                ('biography', models.TextField(max_length=500, verbose_name='biography')),
                ('photo', models.ImageField(upload_to='candidate_photos/', verbose_name='photo')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='election_candidates', to='election.election', verbose_name='Election')),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
        ),
    ]
