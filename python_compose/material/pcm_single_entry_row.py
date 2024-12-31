import typing

import customtkinter

from python_compose.pc_entry import pc_entry
from python_compose.pc_label import pc_label
from python_compose.pc_row import pc_row
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_string_var import PcStringVar


def pcm_single_entry_row(
	parent: typing.Any,
	label_string_var: PcStringVar,
	entry_string_var: PcStringVar,
	style_bundle: typing.Optional[PcStyleBundle] = None,
):
	if style_bundle is None:
		style_bundle = PcStyleBundle().set_pad_y((0, 8))

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
			lambda p: pc_entry(
				style_bundle=PcStyleBundle()
				.set_width(256),
				parent=p,
				string_var=entry_string_var,
			),
		]
	)
