from django.db import models

# Create your models here.
class TblCandidates(models.Model):
    candidate_id = models.BigAutoField(db_column='CANDIDATE_ID', primary_key=True)  # Field name made lowercase.
    voter_id = models.BigIntegerField(db_column='VOTER_ID', blank=True, null=True)  # Field name made lowercase.
    position_id = models.BigIntegerField(db_column='POSITION_ID', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='REMARKS', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'TBL_CANDIDATES'


class TblElectCandidates(models.Model):
    elect_number = models.BigAutoField(db_column='ELECT_NUMBER', primary_key=True)  # Field name made lowercase.
    position_id = models.BigIntegerField(db_column='POSITION_ID', blank=True, null=True)  # Field name made lowercase.
    number_elect = models.IntegerField(db_column='NUMBER_ELECT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_ELECT_CANDIDATES'


class TblPosition(models.Model):
    position_id = models.BigAutoField(db_column='POSITION_ID', primary_key=True)  # Field name made lowercase.
    position_description = models.TextField(db_column='POSITION_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_POSITION'


class TblVoter(models.Model):
    voter_id = models.BigAutoField(db_column='VOTER_ID', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FIRSTNAME', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LASTNAME', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    area = models.TextField(db_column='AREA', blank=True, null=True)  # Field name made lowercase.
    access_code = models.TextField(db_column='ACCESS_CODE', blank=True, null=True)  # Field name made lowercase.
    image = models.BinaryField(db_column='IMAGE', blank=True, null=True)  # Field name made lowercase.
    registration_status = models.TextField(db_column='REGISTRATION_STATUS', blank=True, null=True)  # Field name made lowercase.
    registration_date = models.TextField(db_column='REGISTRATION_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_VOTER'


class TblVotes(models.Model):
    vote_id = models.BigAutoField(db_column='VOTE_ID', primary_key=True)  # Field name made lowercase.
    ballot_number = models.BigIntegerField(db_column='BALLOT_NUMBER', blank=True, null=True)  # Field name made lowercase.
    voter_id = models.BigIntegerField(db_column='VOTER_ID', blank=True, null=True)  # Field name made lowercase.
    candidate_id = models.BigIntegerField(db_column='CANDIDATE_ID', blank=True, null=True)  # Field name made lowercase.
    date_time = models.DateTimeField(db_column='DATE_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TBL_VOTES'

class WinnersList(models.Model):
    access_code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
