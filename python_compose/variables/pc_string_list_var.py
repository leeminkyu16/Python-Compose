import typing

from python_compose.variables.pc_string_var import PcStringVar


class PcStringListVar:
	def __init__(
		self,
		default_value: str = "",
	):
		# A dict is used instead of a list to allow for sparse indexing
		self._value: typing.Dict[int, PcStringVar] = {}
		self.default_value: str = default_value
		self.next_available_index = 0

	def get(self, index: int) -> str:
		return self._value[index].get()

	def generate_var(self, default_value: typing.Optional[str] = None) -> int:
		current_index = self.next_available_index
		self.next_available_index += 1

		self._value[current_index] = PcStringVar(
			default_string=default_value if default_value is not None else self.default_value,
		)

		return current_index

	def remove(self, index: int):
		self._value.pop(index)

	def get_string_vars(self) -> typing.List[PcStringVar]:
		return list(
			map(
				lambda x: x[1],
				sorted(
					self._value.items(), key=lambda x: x[0]
				)
			)
		)

	def get_key_string_var_pairs(self) -> typing.List[typing.Tuple[int, PcStringVar]]:
		return list(
			sorted(
				self._value.items(), key=lambda x: x[0]
			)
		)

	def get_strings(self) -> typing.List[str]:
		return list(
			map(
				lambda x: x[1].get(),
				sorted(
					self._value.items(), key=lambda x: x[0]
				)
			)
		)
