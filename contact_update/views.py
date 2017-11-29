from django.shortcuts import render
from django.http import HttpResponse

from .forms import SearchForm
from apps.api.models import User


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year'].strftime("%Y")
            username = form.cleaned_data['username']
            realname = form.cleaned_data['realname']

            try:
                user = User.objects.get(
                        id=username,
                        ent_year=year,
                        name=realname)
            except User.DoesNotExist:
                return render(request, 'contact_update/search.html',
                        {'form': form, 'error': 'notfound'})

            return render(request, 'contact_update/result.html', {'user': user})
        else:
            return render(request, 'contact_update/search.html', {'form': form})
    else:
        form = SearchForm()

    return render(request, 'contact_update/search.html', {'form': form})
