import tkinter
import typing

import customtkinter

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_observable_bool import PcObservableBool


def pc_progress_bar(
	style_bundle: PcStyleBundle,
	parent: typing.Any,
	variable: typing.Union[tkinter.Variable, None] = None,
	active: typing.Optional[PcObservableBool] = None,
	orientation: str = "horizontal",
	mode: typing.Literal["determinate", "indeterminate"] = "determinate",
) -> PcBaseClassWrapper:
	if active is None:
		active = PcObservableBool(value=True)
	if variable is None:
		variable = tkinter.Variable()

	def create_widget():
		if not active.get():
			return None
		return customtkinter.CTkProgressBar(
			master=parent,
			width=style_bundle.width,
			height=style_bundle.height,
			corner_radius=style_bundle.corner_radius,
			border_width=style_bundle.border_width,
			bg_color=style_bundle.bg_color,
			fg_color=style_bundle.fg_color,
			border_color=style_bundle.border_color,
			progress_color=style_bundle.fg_color,
			variable=variable,
			orientation=orientation,
			mode=mode
		)

	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
		active=active,
	)
