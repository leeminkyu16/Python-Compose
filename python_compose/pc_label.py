import typing

import customtkinter

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.variables.pc_boolean_var import PcBooleanVar
from python_compose.variables.pc_string_var import PcStringVar
from python_compose.pc_style_bundle import PcStyleBundle


def pc_label(
	style_bundle: PcStyleBundle,
	parent: typing.Any,
	string_var: typing.Optional[PcStringVar] = None,
	active: typing.Optional[PcBooleanVar] = None,
) -> PcBaseClassWrapper:
	if active is None:
		active = PcBooleanVar(default_bool=True)
	if string_var is None:
		string_var = PcStringVar()

	def create_widget():
		if not active.get():
			return None
		active.set_parent(parent=parent)
		string_var.set_parent(parent=parent)

		return customtkinter.CTkLabel(
			master=parent,
			width=0 if style_bundle.width is None else style_bundle.width,
			height=32 if style_bundle.height is None else style_bundle.height,
			corner_radius=style_bundle.corner_radius,
			bg_color=style_bundle.bg_color,
			text_color=style_bundle.text_color,
			textvariable=string_var.value,
			font=style_bundle.font,
			anchor=style_bundle.anchor,
			justify=style_bundle.justify,
		)

	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
	)
