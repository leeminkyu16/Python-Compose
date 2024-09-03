import typing

import customtkinter

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.variables.pc_boolean_var import PcBooleanVar
from python_compose.variables.pc_string_var import PcStringVar
from python_compose.pc_style_bundle import PcStyleBundle


def pc_button(
	style_bundle: PcStyleBundle,
	parent: typing.Any,
	string_var: typing.Optional[PcStringVar] = None,
	command: typing.Union[typing.Callable[[], typing.Any], None] = None,
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

		return customtkinter.CTkButton(
			master=parent,
			command=command,
			textvariable=string_var.value,
			width=128 if style_bundle.width is None else style_bundle.width,
			height=32 if style_bundle.height is None else style_bundle.height,
			corner_radius=style_bundle.corner_radius,
			border_width=style_bundle.border_width,
			border_spacing=style_bundle.border_spacing,
			fg_color=style_bundle.fg_color,
			hover_color=style_bundle.hover_color,
			border_color=style_bundle.border_color,
			text_color=style_bundle.text_color,
			text_color_disabled=style_bundle.text_color_disabled,
			font=style_bundle.font,
		)

	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
	)
