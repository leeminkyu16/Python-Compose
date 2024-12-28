import tkinter
import typing

import customtkinter

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_observable_bool import PcObservableBool


def pc_slider(
	style_bundle: PcStyleBundle,
	parent: typing.Any,
	variable: typing.Union[tkinter.Variable, None] = None,
	from_: int = 0,
	to: int = 1,
	command: typing.Union[typing.Callable[[float], None], None] = None,
	active: typing.Optional[PcObservableBool] = None,
	orientation: str = "horizontal",
) -> PcBaseClassWrapper:
	if active is None:
		active = PcObservableBool(value=True)

	def create_widget():
		if not active.get():
			return None
		return customtkinter.CTkSlider(
			master=parent,
			width=style_bundle.width,
			height=style_bundle.height,
			corner_radius=style_bundle.corner_radius,
			border_width=style_bundle.border_width,
			bg_color=style_bundle.bg_color,
			fg_color=style_bundle.fg_color,
			border_color=style_bundle.border_color,
			progress_color=style_bundle.fg_color,
			button_color=style_bundle.fg_color,
			button_hover_color=style_bundle.hover_color,
			from_=from_,
			to=to,
			variable=variable,
			command=command,
			orientation=orientation
		)

	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
		active=active,
	)
