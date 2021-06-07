from django.core.cache import cache
from functools import wraps
from common.utils import from_json

def cache_func(prefix, timeout):
	"""
	force_query=True: directly query database, no save to cache
	"""
	def outer(func):
		@wraps(func)
		def inner(*args, **kwargs):
			cache_key = prefix + "_" + from_json(args)
			cache_value = None
			force_query = kwargs.get("force_query", False)
			if not force_query:
				cache_value = cache.get(cache_key)
			if cache_value is None:
				cache_value = func(*args, **kwargs)
				if not force_query:
					cache.set(cache_key, cache_value, timeout)

			return cache_value

		return inner

	return outer
