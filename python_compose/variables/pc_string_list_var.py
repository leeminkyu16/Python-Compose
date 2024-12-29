import typing

from python_compose.variables.pc_string_var import PcStringVar


class PcStringListVar:
	def __init__(
		self,
		default_value: str = "",
	):
		self._value: typing.Dict[int, PcStringVar] = {}
		self.default_value: str = default_value

	def get(self, index: int) -> str:
		return self._value[index].get()

	def generate_var(self, default_value: typing.Optional[str] = None) -> int:
		index = len(self._value)

		self._value[index] = PcStringVar(
			default_string=default_value if default_value is not None else self.default_value,
		)

		return index

	def remove(self, index: int):
		self._value.pop(index)

	def get_all_string_vars(self) -> typing.List[PcStringVar]:
		return list(
			map(
				lambda x: x[1],
				sorted(
					self._value.items(), key=lambda x: x[0]
				)
			)
		)

	def get_all_strings(self) -> typing.List[str]:
		return list(
			map(
				lambda x: x[1].get(),
				sorted(
					self._value.items(), key=lambda x: x[0]
				)
			)
		)
