import csv
import io

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from rest_framework import generics
from tablib import Dataset

from .forms import UploadCSVForm
from .models import Employee, Roster, Shift, Upload
from .serializers import EmployeeSerializer, RosterSerializer, ShiftSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the shiftmanger index.")


class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ShiftListCreate(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer


class RosterListCreate(generics.ListCreateAPIView):
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer


def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            filename = request.FILES['upload'].name
            if filename.find('employees') > -1:
                parse_csv(request.FILES['upload'], 'employees')
            elif filename.find('shifts') > -1:
                parse_csv(request.FILES['upload'], 'shifts')

            return HttpResponse(f"Succesfully uploaded {filename}")
    else:
        form = UploadCSVForm()
    return render(request, 'upload_csv.html', {'form': form})


def parse_csv(data, upload_type):
    data.seek(0)
    decoded_file = data.read().decode('utf-8')
    io_string = io.StringIO(decoded_file)
    reader = csv.reader(io_string, delimiter=',', quotechar='"')

    # Skip header
    next(reader)

    if upload_type == 'employees':
        for row in reader:
            try:
                Employee.objects.get(first_name=row[0], last_name=row[1])
            except Employee.DoesNotExist as e:
                Employee(first_name=row[0], last_name=row[1]).save()

    if upload_type == 'shifts':
        for row in reader:
            try:
                Shift.objects.get(
                    date=row[0],
                    start_time=row[1],
                    end_time=row[2],
                    break_length=row[3],
                )
            except Shift.DoesNotExist as e:
                Shift(
                    date=row[0],
                    start_time=row[1],
                    end_time=row[2],
                    break_length=row[3],
                ).save()
