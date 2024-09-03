import typing

import customtkinter
from customtkinter import CTkTextbox

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.variables.pc_boolean_var import PcBooleanVar
from python_compose.variables.pc_string_var import PcStringVar
from python_compose.pc_style_bundle import PcStyleBundle


def pc_textbox(
	style_bundle: PcStyleBundle,
	parent: typing.Any,
	string_var: typing.Optional[PcStringVar] = None,
	active: typing.Optional[PcBooleanVar] = None,
) -> PcBaseClassWrapper:
	if active is None:
		active = PcBooleanVar(default_bool=True)
	if string_var is None:
		string_var = PcStringVar()

	def create_widget() -> typing.Optional[customtkinter.CTkTextbox]:
		if not active.get():
			return None
		active.set_parent(parent=parent)
		string_var.set_parent(parent=parent)

		textbox: CTkTextbox = customtkinter.CTkTextbox(
			master=parent,
			width=256 if style_bundle.width is None else style_bundle.width,
			height=256 if style_bundle.height is None else style_bundle.height,
			corner_radius=style_bundle.corner_radius,
			border_width=style_bundle.border_width,
			border_spacing=style_bundle.border_spacing,
			bg_color=style_bundle.bg_color,
			fg_color=style_bundle.fg_color,
			text_color=style_bundle.text_color,
			border_color=style_bundle.border_color,
			font=style_bundle.font,
		)

		def on_string_var_change(var_name, var_index, mode):
			textbox.delete("0.0", "end")
			textbox.insert("0.0", string_var.get())

		string_var.value.trace_add("write", on_string_var_change)
		textbox.get("0.0", "end")

		return textbox

	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
	)
