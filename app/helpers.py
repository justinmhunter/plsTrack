import re
import urllib
from app.redismodel import redis

redis_key = 'stations'

def process_request(request):
    '''takes a request URL, chops it up, transforms the pertinent values and adds them to redis'''
    if re.search('&', request):
        request_dict = {}
        request_strings = request.split('&')
        for str in request_strings:
            k,v = str.split('=')
            if re.search('csrf_token', k): 
                continue
            if (len(k) !=0) and (len(v) != 0): 
                v = urllib.unquote(v).decode('utf8')
                v = urllib.unquote_plus(v).decode('utf8')
                request_dict[k] = v 
            if len(request_dict.values()) == 2:
                pass
                redis.hset(redis_key, request_dict['pls_nick'], request_dict['pls_link'])

def delete_pls(nick):
    '''deletes redis entry by nick'''
    redis.hdel(redis_key, nick)
