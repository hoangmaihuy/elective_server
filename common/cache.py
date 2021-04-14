from django.core.cache import cache
from functools import wraps

def cache_func(prefix, timeout):

	def outer(func):
		@wraps(func)
		def inner(*args, **kwargs):
			cache_key = prefix + "_" + "_".join(args) + "_" + "_".join(kwargs.keys())
			cache_value = cache.get(cache_key)
			if cache_value is None:
				cache_value = func(*args, **kwargs)
				cache.set(cache_key, cache_value, timeout)
			print("cache_func|", cache_key, cache_value)
			return cache_value

		return inner

	return outer
