from django.shortcuts import render

from newz.helper_funcs import date_formatter, paginate
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import LatestNewsModel

from scheduler.newsAPI import update_news
from scheduler.newsAPI import get_post


    

# Create your views here.

def home (request):

    latest_news_full = LatestNewsModel.objects.all()

    # Implement pagination for posts
    paged_news = paginate(request, latest_news_full, 10)
    new_list = []
    for item in paged_news:
        data = item.post_data

        data = date_formatter(data)

        new_list.append(data)
    

    ctx = {
        'latest_news': new_list,
        "paged_news": paged_news
    }
    
    return render(request, 'index.html', ctx)

def post(request, id):

    post_list = []
    post_id_list = []

    try:
        got_post = LatestNewsModel.objects.get(id=id)
        got_post = got_post.post_data
        got_post = date_formatter(got_post)

        if 'kids' in got_post:
            post_id_list = got_post['kids']

            # Implement pagination for comments
            paged_comments = paginate(request, post_id_list, 5)

            get_post(post_list, paged_comments)

            new_post_list = []
            for item in post_list:
                item = date_formatter(item)
                new_post_list.append(item)
            post_list = new_post_list
        # print(f'post formatted: {got_post["kids"]}')
    except:
        got_post = []
        print(f'There was a problem loading post {id}')

    ctx = {
        'post': got_post,
        'comments': post_list,
        'paged_news': paged_comments
    }

    return render(request, 'post_page.html', ctx)