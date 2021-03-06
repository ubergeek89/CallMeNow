from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

#For namespacing the urls in this app.
app_name = 'mainapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign-up/$', views.sign_up, name='sign_up'),
    url(r'^emailconfirm/(?P<uuid>[-\w]+)/$', views.email_confirm, name='email_confirm'),
    url(r'^logout/$', views.logoutpage,  name='logout'),
    url(r'^forgotpassword/$', views.forgotpassword, name='forgotpassword'),
    url(r'^forgot_password_confirm/(?P<uuid>[-\w]+)/$', views.forgot_password_confirm, name='forgot_password_confirm'),
    url(r'^changepassword/$', views.changepassword, name='changepassword'),
    url(r'^gettingstarted/$', views.gettingstarted, name='gettingstarted'),
    url(r'^home/$', views.home, name='home'),
    url(r'^team/$', views.team, name='team'),
    url(r'^team/create-new/$', views.team_create_new, name='team_create_new'),
    url(r'^team/toggleavailability/(?P<user_id>[-\w]+)/(?P<value>[-\w]+)/$', views.toggleavailability, name='toggleavailability'),
    url(r'^team/edit/(?P<user_id>[0-9]+)/$', views.team_edit, name='team_edit'),
    url(r'^widgets/$', views.widgets, name='widgets'),
    url(r'^widgets/create-new/', views.widgets_create_new, name='widgets_create_new'),
    url(r'^widgets/edit/(?P<widget_id>[0-9]+)/$', views.widget_edit, name='widget_edit'),
    url(r'^widgets/editappearance/(?P<widget_id>[0-9]+)/$', views.editappearance, name='editappearance'),
    url(r'^directcall/(?P<widget_id>[0-9]+)/$', views.directcall, name='directcall'),
    url(r'^ajax/widgets/agents/(?P<widget_id>[0-9]+)/$', views.ajax_widget_agents, name='ajax_widget_agents'),
    url(r'^leads/$', views.leads, name='leads'),
    url(r'^leads/detail/(?P<lead_id>[0-9]+)/$', views.lead_detail, name='lead_detail'),
    url(r'^leads/detail/add_new_note/(?P<lead_id>[0-9]+)/$', views.add_new_note, name='add_new_note'),
    url(r'^leads/call_from_admin/(?P<lead_id>[0-9]+)/$', views.call_from_admin, name='call_from_admin'),
    url(r'^leads/ajax_edit_lead/(?P<lead_id>[0-9]+)/$', views.ajax_edit_lead, name='ajax_edit_lead'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^referral/$', views.referral, name='referral'),

    url(r'^billing/$', views.billing, name='billing'),
    url(r'^billing_success/$', views.billing_success, name='billing_success'),
    url(r'^paddle_webhook/', views.paddle_webhook, name='paddle_webhook'),

    url(r'^widgetapi/available/(?P<widget_id>[0-9]+)/$', views.available, name='available'),
    url(r'^widgetapi/newlead/(?P<widget_id>[0-9]+)/$', views.new_lead, name='new_lead'),
    url(r'^widgetapi/newcall/(?P<widget_id>[0-9]+)/$', views.new_call, name='new_call'),
    url(r'^widgetapi/callstatus/(?P<uuid>[-\w]+)/$', views.call_status, name='call_status'),

    url(r'^plivo/plivo_clientfirst_answer_url/(?P<uuid>[-\w]+)/', views.plivo_clientfirst_answer_url, name='plivo_clientfirst_answer_url'),
    url(r'^plivo/plivo_clientfirst_dial_url/(?P<uuid>[-\w]+)/', views.plivo_clientfirst_dial_url, name='plivo_clientfirst_dial_url'),
    url(r'^plivo/plivo_clientfirst_callback_url/(?P<uuid>[-\w]+)/', views.plivo_clientfirst_callback_url, name='plivo_clientfirst_callback_url'),
    url(r'^plivo/plivo_clientfirst_recording_callback_url/(?P<uuid>[-\w]+)/', views.plivo_clientfirst_recording_callback_url, name='plivo_clientfirst_recording_callback_url'),

    url(r'^plivo/plivo_agentfirst_answer_url/(?P<uuid>[-\w]+)/', views.plivo_agentfirst_answer_url, name='plivo_agentfirst_answer_url'),
    url(r'^plivo/plivo_agentfirst_dial_url/(?P<uuid>[-\w]+)/', views.plivo_agentfirst_dial_url, name='plivo_agentfirst_dial_url'),
    url(r'^plivo/plivo_agentfirst_callback_url/(?P<uuid>[-\w]+)/', views.plivo_agentfirst_callback_url, name='plivo_agentfirst_callback_url'),
    url(r'^plivo/plivo_agentfirst_recording_callback_url/(?P<uuid>[-\w]+)/', views.plivo_agentfirst_recording_callback_url, name='plivo_agentfirst_recording_callback_url'),

]