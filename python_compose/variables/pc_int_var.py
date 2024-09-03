import tkinter
import typing


class PcIntVar:
	def __init__(
		self,
		default_int: int = 0,
	):
		self.value: typing.Optional[tkinter.IntVar] = None
		self.default_int: int = default_int

	def set_parent(self, parent: typing.Any):
		int_val = self.get()

		self.value = tkinter.IntVar(
			master=parent,
			value=int_val,
		)

	def get(self) -> int:
		if self.value is None:
			return self.default_int
		return self.value.get()

	def set(self, new_value: int):
		if self.value is not None:
			self.value.set(value=new_value)
