import typing
import weakref


class PcObservableBool:
	def __init__(self, value: bool):
		self.value: bool = value
		self.on_change: typing.Set[typing.Callable[[bool], None]] = set()

	def get(self) -> bool:
		return self.value

	def set(self, new_value: bool) -> None:
		self.value = new_value
		for func in self.on_change.copy():
			func(new_value)

	def clear_on_change(self) -> None:
		self.on_change.clear()

	def add_on_change(self, on_change: typing.Callable[[bool], None]):
		self.on_change.add(on_change)

		weak_self_ref = weakref.ref(self)
		weak_new_on_change_ref = weakref.ref(self)

		def unsubscribe():
			weak_self: typing.Optional[typing.Self] = weak_self_ref()
			weak_new_on_change: typing.Optional[typing.Callable[[bool], None]] = weak_new_on_change_ref()
			if weak_self is not None and weak_new_on_change in weak_self.on_change:
				weak_self.on_change.remove(weak_new_on_change)

		return unsubscribe
