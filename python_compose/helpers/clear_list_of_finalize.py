import typing
import weakref


def clear_list_of_finalize(list_of_finalize: typing.List[weakref.finalize]) -> None:
	for finalizer in list_of_finalize:
		if finalizer.alive:
			finalizer_detach_output = finalizer.detach()
			func = finalizer_detach_output[1]
			if isinstance(func, typing.Callable):
				func()
	list_of_finalize.clear()
