from urllib import response
from newz.models import LatestNewsModel
import requests


API_ENDPOINT = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'

# returns specific post endpoint
def item_api_endpoint(id):
    ITEM_API_ENDPOINT = f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty'
    return ITEM_API_ENDPOINT

# Returns time as integer
def get_time(post):
    return int(post['time'])

# Maps post id list to corresponding post details from specific post endpoint
def get_post(post_list, post_id_list):
    for id in post_id_list:
        try:
            post_response = requests.get(item_api_endpoint(id)).json()
            post_list.append(post_response)
        except:
            print(f'Could not get post {id}')

    # sort post_list by time of post
    post_list.sort(key=get_time, reverse=True)

# Gets first 100 latest posts from hacker news API
def get_news():
    response = requests.get(API_ENDPOINT)
    print("latest post ids gotten")

    try:
        response.raise_for_status()
        post_id_list = response.json()
        post_id_list = post_id_list[:100] if len(post_id_list) > 100 else post_id_list

        post_id_list.sort(reverse=True)
        return post_id_list

    except:
        print(f'An error occured while requesting the API {API_ENDPOINT}')
        return None

# Updates db with new post data
def update_news():

    # Request stories
    # Make DB query to return the last entry
    # Check if last entry's ID is in stories response
    # If present get corresponding ID and split stories response by [0: ID]
    # Save the resulting sliced list
    # Else save the entire response

    response = get_news()

    try:
        last_entry = LatestNewsModel.objects.latest('pub_date')
        if (response is not None) and last_entry and (last_entry.id in response):
            id = response.index(last_entry.id)
            print(f'part of response is in db at {id}')

            response = response[:id]
    except:
        print("There are no items in the db")
    
    # Loop through post_id_list and create another array container corresponding posts
    latest_news = []
    if response:
        get_post(latest_news, response)

    if len(latest_news) > 0:

        for post in latest_news:

            model = LatestNewsModel()
            model.id=post['id']
            model.post_data=post
            model.pub_date=post['time']
            model.custom_post=False
            model.save()
