from django.shortcuts import render
from .models import Item 
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login')
def main(request):
	if request.user.is_authenticated():
		items = Item.objects.all().order_by('-updated')

		paginator = Paginator(items, 4)

		try: page = int(request.GET.get("page", '1'))
		except ValueError: page = 1

		try:
 			page_images = paginator.page(page)
    		except (InvalidPage, EmptyPage):
        		page_images = paginator.page(paginator.num_pages)

		context = {
			"items" : page_images[:4],
			"media_url" : settings.MEDIA_URL,
			"page_images" : page_images,
		}

		return render(request, "stockManagement.html", context)


