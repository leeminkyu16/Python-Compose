import tkinter
import typing

import customtkinter

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_observable_bool import PcObservableBool


def pc_segmented_button(
	style_bundle: PcStyleBundle,
	parent: typing.Any,
	values: typing.List[str],
	variable: typing.Union[tkinter.Variable, None] = None,
	command: typing.Union[typing.Callable[[str], None], None] = None,
	active: typing.Optional[PcObservableBool] = None,
) -> PcBaseClassWrapper:
	if active is None:
		active = PcObservableBool(value=True)

	def create_widget():
		if not active.get():
			return None

		return customtkinter.CTkSegmentedButton(
			master=parent,
			width=128 if style_bundle.width is None else style_bundle.width,
			height=32 if style_bundle.height is None else style_bundle.height,
			corner_radius=style_bundle.corner_radius,
			border_width=style_bundle.border_width,
			bg_color=style_bundle.bg_color,
			fg_color=style_bundle.fg_color,
			selected_color=style_bundle.fg_color,
			selected_hover_color=style_bundle.hover_color,
			unselected_color=style_bundle.bg_color,
			unselected_hover_color=style_bundle.hover_color,
			text_color=style_bundle.text_color,
			text_color_disabled=style_bundle.text_color_disabled,
			font=style_bundle.font,
			values=values,
			variable=variable,
			command=command
		)

	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
		active=active,
	)
