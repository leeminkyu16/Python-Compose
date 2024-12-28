import typing

import customtkinter

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.pc_entry_type import PcEntryType
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_observable_bool import PcObservableBool
from python_compose.variables.pc_string_var import PcStringVar


def validate_int(candidate) -> bool:
	return str.isdigit(candidate) or candidate == ""


def pc_entry(
	style_bundle: PcStyleBundle,
	parent: customtkinter.CTkBaseClass,
	string_var: typing.Optional[PcStringVar] = None,
	active: typing.Optional[PcObservableBool] = None,
	placeholder_text: str = "",
	input_type: PcEntryType = PcEntryType.STRING,
) -> PcBaseClassWrapper:
	if active is None:
		active = PcObservableBool(value=True)

	if string_var is None:
		string_var = PcStringVar()

	def create_widget():
		if not active.get():
			return None
		string_var.set_parent(parent=parent)

		new_entry = customtkinter.CTkEntry(
			master=parent,
			width=128 if style_bundle.width is None else style_bundle.width,
			height=32 if style_bundle.height is None else style_bundle.height,
			textvariable=string_var.value,
			placeholder_text=placeholder_text,
			text_color=style_bundle.text_color,
			border_color=style_bundle.border_color,
			fg_color=style_bundle.fg_color,
			bg_color=style_bundle.bg_color,
			placeholder_text_color=style_bundle.placeholder_text_color,
			validate="all" if input_type == PcEntryType.INT else "none",
			validatecommand=(parent.register(validate_int), '%P') if input_type == PcEntryType.INT else (),
		)

		return new_entry

	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
		active=active,
	)


