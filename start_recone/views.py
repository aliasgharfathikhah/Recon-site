
from django.shortcuts import render
from .forms import UrlForm
from utils.recon import Find_Links
from utils.find_port import Find_Port
from utils.whois import get_whois
from utils.re import ReP, ReE

def get_links(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            links = Find_Links(url)
            port = Find_Port(url)
            whois = get_whois(url)
            phones = ReP(url)
            emails = ReE(url)
            return render(request, 'file/link.html', {
                'links': links,
                'ports': port,
                'whois': whois,
                'phones': phones,
                'emails': emails,
            })

    else:
        form = UrlForm()

    return render(request, 'file/index.html', {'form': form})
