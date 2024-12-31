import typing

import customtkinter

from python_compose.pc_checkbox import pc_checkbox
from python_compose.pc_label import pc_label
from python_compose.pc_row import pc_row
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_boolean_var import PcBooleanVar
from python_compose.variables.pc_string_var import PcStringVar


def pcm_checkbox_row(
	parent: typing.Any,
	label_string_var: PcStringVar,
	checkbox_variable: PcBooleanVar,
	style_bundle: typing.Optional[PcStyleBundle] = None,
):
	if style_bundle is None:
		style_bundle = PcStyleBundle().set_pad_y((0, 8)).set_fill(customtkinter.X)

	# noinspection PyShadowingNames
	return pc_row(
		style_bundle=style_bundle,
		parent=parent,
		child_factories=[
			lambda p: pc_label(
				style_bundle=PcStyleBundle()
				.set_width(128)
				.set_anchor(customtkinter.W),
				parent=p,
				string_var=label_string_var,
			),
			lambda p: pc_row(
				style_bundle=PcStyleBundle()
				.set_fg_color("transparent")
				.set_width(256)
				.set_expand(True),
				parent=p,
				child_factories=[
					lambda p: pc_checkbox(
						style_bundle=PcStyleBundle()
						.set_width(24)
						.set_height(16)
						.set_checkbox_width(24)
						.set_checkbox_height(24)
						.set_anchor(customtkinter.CENTER),
						parent=p,
						variable=checkbox_variable.value,
					),
				]
			),
		],
	)
