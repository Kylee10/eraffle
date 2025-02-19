from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from math import ceil
import random
from .models import TblCandidates,TblElectCandidates,TblPosition,TblVoter,TblVotes, WinnersList

# Create your views here.
def index(request, spins):
    voters = TblVoter.objects.filter(registration_status = 'Registered')
    winners = WinnersList.objects.all()
    if len(winners) != 0:
        new_voters = [i for i in voters if not any(k.access_code == i.access_code for k in winners)]
    else:
        new_voters = voters
    list = []
    masterlist = []
    for a in new_voters:
        dict = {"access_code": a.access_code, "name_code": a.lastname + ", " + a.firstname}
        list.append(dict)
    if(int(spins) <= 0):
        return HttpResponseRedirect(reverse('eraffle:index', args=str(6)))
    counter = ceil(len(list)/int(spins))
    random.shuffle(list)
    sublist = []
    count = 1

    if list != []:
        for index in list:
            sublist.append(index)
            if count == counter:
                masterlist.append(sublist)
                sublist = []
                count = 1
            else:
                count+=1
            if index == list[len(list) - 1] and count < counter and sublist != []:
                masterlist.append(sublist)
        if int(spins) < 6:
            for x in range(6 - int(spins)):
                sublist = []
                masterlist.append(sublist)
        
        if int(spins) > 6:
            return HttpResponseRedirect(reverse('eraffle:index', args=str(6)))
        else:
            return render(request, "app/index.html",{"content1": masterlist[0], "content2": masterlist[1], "content3": masterlist[2], "content4": masterlist[3], "content5": masterlist[4], "content6": masterlist[5]})
    else:
        return render(request, "app/index.html",{"content1": [], "content2": [], "content3": [], "content4": [], "content5": [], "content6": []})
def attendance(request):
    voters = TblVoter.objects.filter(registration_status = 'Registered')
    new_voters_list = []
    for index in voters:
        new_voters_list.append(index.lastname + ", " + index.firstname)
    return render(request, "app/attendance.html", {"attendance": new_voters_list})

def winners(request):
    winners = WinnersList.objects.all()
    return render(request, "app/winners.html", {'winners': winners })

def getWinners(request):
    btn = 'saveWinners' in request.POST
    viewBtn = 'viewWinners' in request.POST
    attendanceBtn = 'checkAttendance' in request.POST
    resetBtn = 'resetList' in request.POST

    if btn == True:
        list = []
        r1 = request.POST['result1']
        r11 = r1.split("_")
        r2 = request.POST['result2']
        r21 = r2.split("_")
        r3 = request.POST['result3']
        r31 = r3.split("_")
        r4 = request.POST['result4']
        r41 = r4.split("_")
        r5 = request.POST['result5']
        r51 = r5.split("_")
        r6 = request.POST['result6']
        r61 = r6.split("_")
        list = [r11, r21, r31, r41, r51, r61]
        for index in list:
            if index != ['']:
                winners = WinnersList(access_code=index[0], name=index[1])
                winners.save()
        winners = WinnersList.objects.all()
        return HttpResponseRedirect(reverse('eraffle:index', args=[6]))
    elif viewBtn == True:
        return HttpResponseRedirect(reverse('eraffle:winners'))
    elif attendanceBtn == True:
        return HttpResponseRedirect(reverse('eraffle:attendance'))
    elif resetBtn == True:
        return HttpResponseRedirect(reverse('eraffle:index', args=[6]))

def setSpins(request):
    spins = request.POST["spins"]
    return HttpResponseRedirect(reverse('eraffle:index', args=[spins]))

def backToHomeOrAttendance(request):
    homeBtn = 'home' in request.POST
    attendanceBtn = 'checkAttendance' in request.POST
    viewBtn = 'viewWinners' in request.POST

    if homeBtn == True:
        return HttpResponseRedirect(reverse('eraffle:index', args=[6]))
    elif attendanceBtn == True:
        return HttpResponseRedirect(reverse('eraffle:attendance'))
    elif viewBtn == True:
        return HttpResponseRedirect(reverse('eraffle:winners'))
    