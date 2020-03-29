from django.shortcuts import render
import operator
from . import count


def home(request):
    return render(request, 'index.html', {'var1': '20'})


def results(request):
    article = request.GET['article']
    var_dict, word_count = count.count(article);
    return render(request, 'results.html', {'article': article, 'dist_word':  var_dict, 'word_count': word_count})
