import abc
import typing
import weakref


class PcObservable[T](abc.ABC):

	def __init__(self):
		self.on_change: typing.Set[typing.Callable[[T], None]] = set()

	@abc.abstractmethod
	def get(self) -> T:
		raise NotImplementedError

	@abc.abstractmethod
	def set(self, new_value: T) -> None:
		raise NotImplementedError

	def clear_on_change(self) -> None:
		self.on_change.clear()

	def add_on_change(self, on_change: typing.Callable[[T], None]) -> typing.Callable[[], None]:
		self.on_change.add(on_change)

		weak_self_ref = weakref.ref(self)
		weak_new_on_change_ref = weakref.ref(on_change)

		def unsubscribe():
			weak_self: typing.Optional[typing.Self] = weak_self_ref()
			weak_new_on_change: typing.Optional[typing.Callable[[T], None]] = weak_new_on_change_ref()
			if weak_self is not None and weak_new_on_change in weak_self.on_change:
				weak_self.on_change.remove(weak_new_on_change)

		return unsubscribe
