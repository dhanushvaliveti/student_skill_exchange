from django.urls import path
from . import views

urlpatterns = [

    # =====================
    # AUTH
    # =====================
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # =====================
    # HOME
    # =====================
    path('', views.home_view, name='home'),

    # =====================
    # SKILLS
    # =====================
    path('skills/', views.skill_list, name='skills'),
    path('skills/add/', views.add_skill, name='add_skill'),

    # =====================
    # REQUESTS
    # =====================
    path('send-request/<int:skill_id>/', views.send_request, name='send_request'),
    path('requests/', views.request_list, name='requests'),
    path('accept-request/<int:request_id>/', views.accept_request, name='accept_request'),

    # =====================
    # SCHEDULING
    # =====================
    path('schedule/<int:request_id>/', views.schedule_session, name='schedule'),

    # =====================
    # MEETING LINK
    # =====================
    path('add-link/<int:request_id>/', views.add_meeting_link, name='add_link'),

    # =====================
    # SESSION
    # =====================
    path('session/<int:request_id>/', views.session_view, name='session'),

    # =====================
    # COMPLETE SESSION
    # =====================
    path('complete/<int:request_id>/', views.complete_session, name='complete_session'),

    # =====================
    # LEADERBOARD
    # =====================
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),

    # =====================
    # BUY CREDITS
    # =====================
    path('buy-credits/', views.buy_credits, name='buy_credits'),
]