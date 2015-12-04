from django.shortcuts import render
from .forms import ContactForm, SignUpForm
# Create your views here.
def home(request):
	title = 'Welcome'
	# if request.user.is_authenticated():
	# 	title = "My Title %s" %(request.user)


	#add a form


	# if request.method == "POST":
	# 	print request.POST
	form = SignUpForm(request.POST or None)


	context = {
			"title" : title,
			"form" : form,
	}

	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print instance
		print instance.timestamp

		context = {
			"title" : "Thank you",
		}


	return render(request, "home.html", context)

def contact(request):

	form = ContactForm(request.POST or None)

	if form.is_valid():
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")
		print email, message, full_name

	context = {
		"form": form,
	}
	return render(request, "form.html", context)