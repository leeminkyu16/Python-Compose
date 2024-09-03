import tkinter
import typing


class PcBooleanVar:
	def __init__(
		self,
		default_bool: bool = False,
	):
		self.value: typing.Optional[tkinter.BooleanVar] = None
		self.default_bool: bool = default_bool

	def set_parent(self, parent: typing.Any):
		boolean_val = self.get()

		self.value = tkinter.BooleanVar(
			master=parent,
			value=boolean_val,
		)

	def add_on_change(self, on_change: typing.Callable[[str, str, str], object]):
		self.value.trace_add(mode="write", callback=on_change)

	def get(self) -> bool:
		if self.value is None:
			return self.default_bool
		return self.value.get()

	def set(self, new_value: bool):
		if self.value is not None:
			self.value.set(value=new_value)
