import typing

import customtkinter

from python_compose.variables.pc_observable_bool import PcObservableBool
from python_compose.pc_style_bundle import PcStyleBundle


class PcBaseClassWrapper:
	widget: customtkinter.CTkBaseClass
	style_bundle: PcStyleBundle

	def __init__(
		self,
		widget: customtkinter.CTkBaseClass,
		style_bundle: PcStyleBundle,
		create_widget: typing.Callable[[], customtkinter.CTkBaseClass],
		active: typing.Optional[PcObservableBool] = None,
	):
		self.widget = widget
		self.style_bundle = style_bundle

		if active is None:
			self.active: PcObservableBool = PcObservableBool(value=True)
		else:
			self.active: PcObservableBool = active

		self.create_widget = create_widget

	def get_width(self) -> int:
		width = self.widget.winfo_reqwidth()

		pad_x = self.style_bundle.pad_x
		if isinstance(pad_x, tuple):
			width += pad_x[0] + pad_x[1]
		elif isinstance(pad_x, int):
			width += pad_x * 2
		return width

	def get_height(self) -> int:
		height = self.widget.winfo_reqheight()

		pad_y = self.style_bundle.pad_y
		if isinstance(pad_y, tuple):
			height += pad_y[0] + pad_y[1]
		elif isinstance(pad_y, int):
			height += pad_y * 2
		return height
