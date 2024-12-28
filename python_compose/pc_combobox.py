import typing

import customtkinter

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_observable_bool import PcObservableBool
from python_compose.variables.pc_string_var import PcStringVar


def pc_combobox(
	style_bundle: PcStyleBundle,
	parent: typing.Any,
	values: typing.List[str],
	active: typing.Optional[PcObservableBool] = None,
	string_var: typing.Optional[PcStringVar] = None,
) -> PcBaseClassWrapper:
	if active is None:
		active = PcObservableBool(value=True)

	if string_var is None:
		string_var = PcStringVar()

	def create_widget():
		if not active.get():
			return None
		string_var.set_parent(parent=parent)

		return customtkinter.CTkComboBox(
			master=parent,
			values=values,
			width=128 if style_bundle.width is None else style_bundle.width,
			height=32 if style_bundle.height is None else style_bundle.height,
			corner_radius=style_bundle.corner_radius,
			bg_color=style_bundle.bg_color,
			fg_color=style_bundle.fg_color,
			border_color=style_bundle.border_color,
			text_color=style_bundle.text_color,
			font=style_bundle.font,
			variable=string_var.value,
		)

	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
		active=active,
	)
