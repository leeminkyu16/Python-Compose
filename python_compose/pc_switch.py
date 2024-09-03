import tkinter
import typing

import customtkinter

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.variables.pc_boolean_var import PcBooleanVar
from python_compose.pc_style_bundle import PcStyleBundle


def pc_switch(
	style_bundle: PcStyleBundle,
	parent: typing.Any,
	text_variable: typing.Union[tkinter.Variable, None] = None,
	variable: typing.Union[tkinter.Variable, None] = None,
	active: typing.Optional[PcBooleanVar] = None,
) -> PcBaseClassWrapper:
	if active is None:
		active = PcBooleanVar(default_bool=True)

	def create_widget():
		if not active.get():
			return None
		active.set_parent(parent=parent)
		switch = customtkinter.CTkSwitch(
			master=parent,
			width=128 if style_bundle.width is None else style_bundle.width,
			height=32 if style_bundle.height is None else style_bundle.height,
			corner_radius=style_bundle.corner_radius,
			border_width=style_bundle.border_width,
			bg_color=style_bundle.bg_color,
			fg_color=style_bundle.fg_color,
			border_color=style_bundle.border_color,
			text_color=style_bundle.text_color,
			text_color_disabled=style_bundle.text_color_disabled,
			font=style_bundle.font,
			textvariable=text_variable,
			variable=variable
		)
		return switch

	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
	)
