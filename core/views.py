from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from django.utils import timezone

from .models import Profile, Skill, Request, Transaction

def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'auth/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')   # VERY IMPORTANT
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home_view(request):
    profile = request.user.profile
    return render(request, 'home.html', {'profile': profile})

@login_required
def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'skills/list.html', {'skills': skills})

@login_required
def add_skill(request):
    if request.method == "POST":
        Skill.objects.create(
            owner=request.user,
            name=request.POST['name'],
            level=request.POST['level'],
            description=request.POST['description']
        )
        return redirect('skills')

    return render(request, 'skills/add.html')


@login_required
def send_request(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)

    Request.objects.create(
        sender=request.user,
        receiver=skill.owner,
        skill=skill
    )

    return redirect('skills')


@login_required
def request_list(request):
    received = Request.objects.filter(receiver=request.user)
    sent = Request.objects.filter(sender=request.user)

    return render(request, 'requests/list.html', {
        'received': received,
        'sent': sent
    })
    
    
@login_required
def accept_request(request, request_id):
    req = get_object_or_404(Request, id=request_id)

    req.status = 'accepted'
    req.save()

    return redirect('requests')

@login_required
def schedule_session(request, request_id):
    req = get_object_or_404(Request, id=request_id)

    if request.method == "POST":
       req.scheduled_date = request.POST['date']
       req.scheduled_time = request.POST['time']
       req.meeting_link = request.POST['link']
       req.status = 'scheduled'
       req.save()

       return redirect('requests')

    return render(request, 'requests/schedule.html', {'req': req})




@login_required
def add_meeting_link(request, request_id):
    req = get_object_or_404(Request, id=request_id)

    if request.method == "POST":
        req.meeting_link = request.POST['link']
        req.save()

        return redirect('session', request_id=req.id)

    return render(request, 'requests/detail.html', {'req': req})




@login_required
def session_view(request, request_id):
    req = get_object_or_404(Request, id=request_id)

    return render(request, 'session/session.html', {'req': req})


@login_required
def complete_session(request, request_id):
    req = get_object_or_404(Request, id=request_id)

    # logic will be added later
    req.status = 'completed'
    req.save()

    return redirect('home')

@login_required
def leaderboard_view(request):
    profiles = Profile.objects.all().order_by('-sessions_taught', '-sessions_learned', '-streak')

    return render(request, 'leaderboard/leaderboard.html', {'profiles': profiles})




@login_required
def buy_credits(request):
    if request.method == "POST":
        credits = int(request.POST['credits'])

        # price mapping
        price_map = {
            10: 50,
            25: 100,
            50: 180
        }

        amount = price_map.get(credits, 0)

        # update profile
        profile = request.user.profile
        profile.credits += credits
        profile.save()

        # save transaction
        Transaction.objects.create(
            user=request.user,
            credits_added=credits,
            amount=amount
        )

        return redirect('home')

    return render(request, 'payments/buy_credits.html')

@login_required
def complete_session(request, request_id):
    req = get_object_or_404(Request, id=request_id)

    # Only allow sender or receiver
    if request.user != req.sender and request.user != req.receiver:
        return redirect('home')

    # Prevent duplicate completion
    if req.status == 'completed':
        return redirect('home')

    # =========================
    # CREDIT LOGIC (based on level)
    # =========================
    CREDIT_MAP = {
        "Beginner": 1,
        "Intermediate": 2,
        "Advanced": 3
    }

    credits = CREDIT_MAP[req.skill.level]

    learner_profile = req.sender.profile
    teacher_profile = req.receiver.profile

    # Deduct from learner
    learner_profile.credits -= credits

    # Add to teacher
    teacher_profile.credits += credits

    # =========================
    # SESSION COUNT
    # =========================
    learner_profile.sessions_learned += 1
    teacher_profile.sessions_taught += 1

    # =========================
    # STREAK LOGIC (for learner)
    # =========================
    today = date.today()
    last = learner_profile.last_active_date

    if last == today:
        pass
    elif last == today - timedelta(days=1):
        learner_profile.streak += 1
    else:
        learner_profile.streak = 1

    learner_profile.last_active_date = today

    # =========================
    # SAVE EVERYTHING
    # =========================
    learner_profile.save()
    teacher_profile.save()

    # Update request
    req.status = 'completed'
    req.completed_at = timezone.now()
    req.save()

    return redirect('home')


def leaderboard(request):
    users = User.objects.all()

    users = sorted(
        users,
        key=lambda u: getattr(u.profile, 'streak', 0),
        reverse=True
    )

    return render(request, 'leaderboard.html', {'users': users})