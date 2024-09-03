import tkinter
import typing


class PcStringVar:
	def __init__(
		self,
		default_string: str = "",
	):
		self.value: typing.Optional[tkinter.StringVar] = None
		self.default_string: str = default_string

	def set_parent(self, parent: typing.Any):
		string_val = self.get()

		self.value = tkinter.StringVar(
			master=parent,
			value=string_val,
		)

	def get(self) -> str:
		if self.value is None:
			return self.default_string
		return self.value.get()

	def set(self, new_value: str):
		if self.value is not None:
			self.value.set(value=new_value)
