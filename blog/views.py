from cProfile import label
from django.shortcuts import render
from .models import Interactions
from django.db.models import Count  
from django.db.models.functions import TruncMonth
import logging
import numpy as np


def post_list(request):
    return render(request, 'blog/post_list.html', {})

def interactions(request):
    interactions = Interactions.objects.order_by('-sector_id')
    labels = []
    data = []

    queryset = Interactions.objects.values('name').annotate(count=Count('name'))
    logger = logging.getLogger("mylogger")
    logger.info(queryset)

    for interaction in queryset:
        labels.append(interaction['name'])
        data.append(interaction['count'])

    month_query = Interactions.objects.annotate(month=TruncMonth('date')).values('month').annotate(count=Count('id')).values('month', 'count')     

    labels_month = []
    data_month = []
    for month in month_query:
        labels_month.append(month['month'].strftime("%m/%Y"))
        data_month.append(month['count'])
            
    return render(request, 'blog/interactions.html', {'labels': labels, 'data': data, 'dataMonth': data_month, 'labelsMonth': labels_month, 'sum': sum(data), 'mostPopular': labels[np.argmax(data)]})
