from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import JobApplication
from .forms import RegisterForm, LoginForm
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages


# ---------- AUTH ----------

def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')

    return render(request, 'jobs/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username or password")

        else:
            messages.error(request, "Please fill in all fields correctly")

    else:
        form = LoginForm()

    return render(request, "jobs/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')


# ---------- JOB CRUD (manual HTML) ----------

@login_required
def dashboard(request):
    query = request.GET.get('q')
    jobs = JobApplication.objects.filter(user=request.user)
    if query:
        jobs = jobs.filter(
            Q(company__icontains=query) |
            Q(role__icontains=query)
        )
    applied_count = jobs.filter(status="Applied").count()
    interview_count = jobs.filter(status="Interview").count()
    offer_count = jobs.filter(status="Offer").count()
    rejected_count = jobs.filter(status="Rejected").count()

    return render(request, "jobs/dashboard.html", {
        'jobs': jobs,
        'applied_count': applied_count,
        'interview_count': interview_count,
        'offer_count': offer_count,
        'rejected_count': rejected_count,
    })


@login_required
def add_job(request):
    if request.method == "POST":
        JobApplication.objects.create(
            user=request.user,
            company=request.POST.get("company"),
            role=request.POST.get("role"),
            status=request.POST.get("status"),
            date_applied=request.POST.get("date_applied"),
            notes=request.POST.get("notes"),
        )
        return redirect("dashboard")

    return render(request, "jobs/add_job.html")


@login_required
def edit_job(request, id):
    job = get_object_or_404(JobApplication, id=id, user=request.user)

    if request.method == "POST":
        job.company = request.POST.get("company")
        job.role = request.POST.get("role")
        job.status = request.POST.get("status")
        job.date_applied = request.POST.get("date_applied")
        job.notes = request.POST.get("notes")
        job.save()
        return redirect("dashboard")

    return render(request, "jobs/edit_job.html", {"job": job})


@login_required
def delete_job(request, id):
    job = get_object_or_404(JobApplication, id=id, user=request.user)
    job.delete()
    return redirect("dashboard")
