from DjangoRevisionHistory.functions import render_to
from django.shortcuts import redirect
from pages.models import Page
from pages.forms import NewPageForm

@render_to('pages/list.html')
def list(request):
	return {'pages': Page.objects.all().order_by('-id')}

@render_to('pages/new.html')
def new(request):
	if request.method == 'GET':
		form = NewPageForm()
	elif request.method == 'POST':
		form = NewPageForm(request.POST)
		if form.is_valid():
			page = form.save()
			return redirect(page)

	return {'form': form}

@render_to('pages/single.html')
def single(request, id):
	page = Page.objects.get(pk=id)
	return {'page': page}

@render_to('pages/new.html')
def revise(request, id):
	parent_page = Page.objects.get(pk=id)

	if request.method == 'GET':
		form = NewPageForm(instance=parent_page)
	elif request.method == 'POST':
		form = NewPageForm(request.POST)
		if form.is_valid():
			page = form.save()

			page.parent = parent_page
			page.save()

			return redirect(page)

	return {'form': form}