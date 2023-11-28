from django.shortcuts import render,redirect
from django.views.generic import View


def dashboardView(request):
    dashboard_link="https://codepen.io/aybukeceylan/pen/OJRNbZp"
    return render(request,"dashboard.html",{'dashboard_link':dashboard_link})