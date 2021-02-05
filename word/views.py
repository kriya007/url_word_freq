from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from word.models import Frequency
from word.models import Store
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from bs4 import BeautifulSoup
import requests
import urllib.request
import urllib.parse
import re




common = requests.get("https://www.textfixer.com/tutorials/common-english-words-with-contractions.txt")
words = common.content
soup2 = BeautifulSoup(words, 'lxml')
arr2 = ((soup2.get_text()))
a2 = arr2.split(',')
fi = []
fi = a2
fi.append("The")
fi.append("[")
fi.append("~")
fi.append("]")
fi.append("^")
fi.append(".")
fi.append("(")
fi.append(")")
fi.append("}")
fi.append("{")
fi.append("-")
fi.append("_")

#print(fi)
# Create your views here.
@csrf_exempt
def index(request):
    if request.method == "POST":
        url = request.POST.get('url')
        if Store.objects.filter(url= url).exists():
            site = Store.objects.filter(url = url)[:10]
            content = {'variable': " This site was accessed before"}
            return render(request, "result.html", {'site' : site})
        else:
            result = requests.get(url)
            src= result.content
            soup =BeautifulSoup(src, 'lxml')
            target = ((soup.get_text()))
            tar = target.split()
        #print(tar)
            di = []
            di = tar
            length= len(di)
            i=0
            freq = dict()
            while  i!= length:
                if di[i] not in fi:
                    if di[i] >= '64' and di[i] !='92':
                        k= di.count(di[i])
                        freq[di[i]] = k
                        store = Store(url = url, count = k, streengs = di[i])
                        store.save()
                        site = Store.objects.filter(url = url)[:10]
                i= i+1
            content = {'variable': " "}
        return render(request, "result.html", {'site' : site})
    return render(request, "index.html")

    