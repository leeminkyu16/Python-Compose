import typing

from python_compose.variables.pc_string_list_var import PcStringListVar
from python_compose.variables.pc_observable import PcObservable
from python_compose.variables.pc_string_var import PcStringVar


class PcObservableStringListVar(PcStringListVar, PcObservable[typing.List[PcStringVar]]):
	def __init__(
		self,
		default_value: str = "",
	):
		PcStringListVar.__init__(self, default_value=default_value)
		PcObservable.__init__(self)

	def generate_var(self, default_value: typing.Optional[str] = None) -> int:
		index = PcStringListVar.generate_var(self, default_value=default_value)
		for func in self.on_change.copy():
			func(self.get_string_vars())

		return index

	def remove(self, index: int):
		PcStringListVar.remove(self, index)
		for func in self.on_change.copy():
			func(self.get_string_vars())

	def set(self, new_value: typing.List[PcStringVar]) -> None:
		self._value.clear()
		for index, string_var in enumerate(new_value):
			self._value[index] = string_var

	def get(self, index: int):
		PcStringListVar.get(self, index)
