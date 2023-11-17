from django.shortcuts import render
from home.models import Phone
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)


def example(request):
    phone = Phone.objects.all()
    paginator = Paginator(phone, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        phone = paginator.page(page)
    except PageNotAnInteger:
        phone = paginator.page(1)
    except EmptyPage:
        phone = paginator.page(paginator.num_pages)
    context = {
        'phone': phone,
    }
    return render(request, 'index.html', context)
