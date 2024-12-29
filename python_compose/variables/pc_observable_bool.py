import typing

from python_compose.variables.pc_observable import PcObservable


class PcObservableBool(PcObservable[bool]):
	def __init__(self, value: bool):
		super().__init__()
		self.value: bool = value

	def get(self) -> bool:
		return self.value

	def set(self, new_value: bool) -> None:
		self.value = new_value
		for func in self.on_change.copy():
			func(new_value)

	def clear_on_change(self) -> None:
		super().clear_on_change()

	def add_on_change(self, on_change: typing.Callable[[bool], None]):
		super().add_on_change(on_change)
