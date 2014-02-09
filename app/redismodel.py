import json
from redis import StrictRedis

class RedisModel(StrictRedis):

    '''create a singleton instance of the the RedisModel class'''

    _instance = None

    #def __new__(cls, *args, **kwargs): # know the difference btw *args and **kwargs
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(RedisModel, cls).__new__(
                cls, host='localhost', port='6379')

        return cls._instance   

    @staticmethod
    def _decode(value):
        try:
            return json.loads(value)
        except:
            pass
        return value

    @staticmethod
    def _encode(value):
        value = json.dumps(value)
        return value
        
    # OVERRIDDEN METHODS

    def set(self, name, value, **kwargs):
        value = self._encode(value)
        return super(RedisModel, self).set(name, value, **kwargs)
    
    def get(self, name):
        value = super(RedisModel, self).get(name)
        return self._decode(value)

    def delete(self, name):
        return super(RedisModel, self).delete(name)

    def hset(self, name, key, value):
        value = self._encode(value)
        return super(RedisModel, self).hset(name, key, value)

    def hget(self, name, key):
        value = super(RedisModel, self).hget(name, key)
        return self._decode(value)

    def hgetall(self, name):
        value = super(RedisModel, self).hgetall(name)
        return {key: self._decode(value[key]) for key in value}

    def hdel(self, name, key):
        return super(RedisModel, self).hdel(name, key)

    def hdelall(self, name):
        keys = super(RedisModel, self).hkeys(name) 
        for key in keys:
            self.hdel(name, key)

redis = RedisModel()
