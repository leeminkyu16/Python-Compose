import typing

import customtkinter

from python_compose.pc_column import pc_column
from python_compose.pc_label import pc_label
from python_compose.pc_scrollable_frame import pc_scrollable_frame
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_observable_bool import PcObservableBool
from python_compose.variables.pc_string_var import PcStringVar


def page_1(
	parent: typing.Any,
	active: PcObservableBool,
):
	# noinspection PyShadowingNames
	return pc_column(
		style_bundle=PcStyleBundle()
		.set_pad_y((0, 8)),
		parent=parent,
		active=active,
		child_factories=[
			lambda p: pc_label(
				style_bundle=PcStyleBundle()
				.set_width(128)
				.set_anchor(customtkinter.W),
				parent=p,
				string_var=PcStringVar(default_string="Page 1")
			),
			lambda p: pc_scrollable_frame(
				style_bundle=PcStyleBundle()
				.set_height(128)
				.set_expand(True)
				.set_fill(customtkinter.BOTH),
				parent=p,
				child_factories=[
					lambda p: pc_label(
						style_bundle=PcStyleBundle()
						.set_justify(customtkinter.LEFT),
						parent=p,
						string_var=PcStringVar(default_string="Page 1 Content")
					),
				],
			),
		],
	)
