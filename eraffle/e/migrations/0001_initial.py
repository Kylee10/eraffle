# Generated by Django 5.0.3 on 2024-03-13 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblCandidates',
            fields=[
                ('candidate_id', models.BigAutoField(db_column='CANDIDATE_ID', primary_key=True, serialize=False)),
                ('voter_id', models.BigIntegerField(blank=True, db_column='VOTER_ID', null=True)),
                ('position_id', models.BigIntegerField(blank=True, db_column='POSITION_ID', null=True)),
                ('remarks', models.TextField(blank=True, db_column='REMARKS', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblElectCandidates',
            fields=[
                ('elect_number', models.BigAutoField(db_column='ELECT_NUMBER', primary_key=True, serialize=False)),
                ('position_id', models.BigIntegerField(blank=True, db_column='POSITION_ID', null=True)),
                ('number_elect', models.IntegerField(blank=True, db_column='NUMBER_ELECT', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblPosition',
            fields=[
                ('position_id', models.BigAutoField(db_column='POSITION_ID', primary_key=True, serialize=False)),
                ('position_description', models.TextField(blank=True, db_column='POSITION_DESCRIPTION', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblVoter',
            fields=[
                ('voter_id', models.BigAutoField(db_column='VOTER_ID', primary_key=True, serialize=False)),
                ('firstname', models.TextField(blank=True, db_column='FIRSTNAME', null=True)),
                ('lastname', models.TextField(blank=True, db_column='LASTNAME', null=True)),
                ('status', models.TextField(blank=True, db_column='STATUS', null=True)),
                ('area', models.TextField(blank=True, db_column='AREA', null=True)),
                ('access_code', models.TextField(blank=True, db_column='ACCESS_CODE', null=True)),
                ('image', models.BinaryField(blank=True, db_column='IMAGE', max_length='max', null=True)),
                ('registration_status', models.TextField(blank=True, db_column='REGISTRATION_STATUS', null=True)),
                ('registration_date', models.TextField(blank=True, db_column='REGISTRATION_DATE', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TblVotes',
            fields=[
                ('vote_id', models.BigAutoField(db_column='VOTE_ID', primary_key=True, serialize=False)),
                ('ballot_number', models.BigIntegerField(blank=True, db_column='BALLOT_NUMBER', null=True)),
                ('voter_id', models.BigIntegerField(blank=True, db_column='VOTER_ID', null=True)),
                ('candidate_id', models.BigIntegerField(blank=True, db_column='CANDIDATE_ID', null=True)),
                ('date_time', models.DateTimeField(blank=True, db_column='DATE_TIME', null=True)),
            ],
        ),
    ]
