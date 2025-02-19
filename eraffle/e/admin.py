from django.contrib import admin
from .models import TblCandidates,TblElectCandidates,TblPosition,TblVoter,TblVotes

# Register your models here.
admin.site.register(TblCandidates)
admin.site.register(TblElectCandidates)
admin.site.register(TblPosition)
admin.site.register(TblVoter)
admin.site.register(TblVotes)