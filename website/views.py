from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render


# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST.get('message-name')
		message_email = request.POST.get('message-email')
		subject_email = request.POST.get('subject-email')
		subject = request.POST.get('subject')

		# send an email
		send_mail( 

			subject_email , #subject
			f'You have an email from {message_name},' + subject, #message
			'aero8991@msn.com', #from email
			['daniel.rossano10@gmail.com'], #To Email
			fail_silently=False
			)
		return render(request, 'contact.html', {'message_name' : message_name})

	else:
		return render(request, 'contact.html', {})

def blog(request):
	return render(request, 'blog.html', {})

def detail(request):
	return render(request, 'detail.html', {})

def service(request):
	return render(request, 'service.html', {})

def team(request):
	return render(request, 'team.html', {})

def testimonial(request):
	return render(request, 'testimonial.html', {})

def about(request):
	return render(request, 'about.html', {})