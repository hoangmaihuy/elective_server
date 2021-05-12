from django.core.cache import cache
from functools import wraps
from common.utils import from_json

def cache_func(prefix, timeout):

	def outer(func):
		@wraps(func)
		def inner(*args, **kwargs):
			cache_key = prefix + "_" + from_json(args)
			print(cache_key)
			cache_value = cache.get(cache_key)
			if cache_value is None:
				cache_value = func(*args, **kwargs)
				cache.set(cache_key, cache_value, timeout)
			return cache_value

		return inner

	return outer
