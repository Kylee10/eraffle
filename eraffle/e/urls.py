from django.urls import path

from . import views

app_name = "eraffle"
urlpatterns = [
    path("<spins>/start-raffle", views.index, name="index"),
    path("attendance/", views.attendance, name="attendance"),
    path("winners/", views.winners, name="winners"),
    path("getWinners/", views.getWinners, name="getWinners"),
    path("setSpins/", views.setSpins, name="setSpins"),
    path("backToHomeOrAttendance", views.backToHomeOrAttendance, name="backToHomeOrAttendance")
]