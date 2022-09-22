import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def paginate(request, data, count_per_page):
    page = request.GET.get('page', 1)

    paginator = Paginator(data, count_per_page)
    try:
        paged_data = paginator.page(page)
    except PageNotAnInteger:
        paged_data = paginator.page(1)
    except EmptyPage:
        paged_data = paginator.page(paginator.num_pages)
    return paged_data

# Converts time to most appropriate unit
def date_formatter(data):
    data['time'] = (int(datetime.datetime.now().strftime('%s')) - int(data['time']))

    if int(data['time']) > (60 * 60 * 24):
        data['time'] = str(int(data['time'] / (60 * 60 * 24))) + " days"
    elif int(data['time']) > (60 * 60):
        data['time'] = str(int(data['time'] / (60 * 60))) + " hours"
    elif int(data['time']) > 60:
        data['time'] = str(int(data['time'] / 60)) + " mins"
    else:
        data['time'] = str(int(data['time'])) + " secs"
    
    return data