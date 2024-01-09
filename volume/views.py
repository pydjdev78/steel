from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Article, Reporter

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year = year)
    context = {"year": year, "article_list": a_list}
    return render(request, "volume/year_archive.html", context)

def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__month = month)
    context = {"month": month, "article_list": a_list}
    return render(request, "volume/month_archive.html", context)

def article_details(request, year, month, pk):
    a_list = Article.objects.filter(pub_date__year = year)
    context = {"pk": pk, "article_list": a_list}
    return render(request, "volume/article_details.html", context)



    # django site deployment platforms
    # vercel
    # railway
    # pythonanywhere
    # openshift