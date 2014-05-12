import re
import urllib
from app.redismodel import redis

redis_key = 'stations'

def process_request(request):
    '''takes a request URL, chops it up, transforms the pertinent values and adds them to redis'''
    if request['pls_link'] and request['pls_nick']:
      redis.hset(redis_key, request['pls_nick'], request['pls_link'])

def delete_pls(nick):
    '''deletes redis entry by nick'''
    redis.hdel(redis_key, nick)
