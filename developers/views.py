from django.shortcuts import render, redirect
from django.core.mail import send_mail


def index(request):
	return render(request, 'index.html', {})
	
def about(request):
	return render(request, 'about.html')

def services(request):
	return render(request, 'services.html')

def contact(request):
	if request.method == 'POST':
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		message_subject = request.POST['message-subject']
		your_message = request.POST['your-message']
		

		send_mail(
			message_subject, # subject
			your_message, # message	
			your_name, # from sender							
			['johnitezbean8@gmail.com'], # To Email
			)

		return render(request, 'contact2.html', {
			'your_name': your_name,
			'your_email': your_email,
			'message_subject': message_subject,
			'your_message': your_message,
			})

	else:
		return render(request, 'contact.html')