import typing

import customtkinter

from python_compose.pc_button import pc_button
from python_compose.pc_column import pc_column
from python_compose.pc_entry import pc_entry
from python_compose.pc_label import pc_label
from python_compose.pc_row import pc_row
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_observable_string_list_var import PcObservableStringListVar
from python_compose.variables.pc_string_var import PcStringVar


def pcm_multiple_entry_row(
	parent: typing.Any,
	label_string_var: PcStringVar,
	entry_string_list_var: PcObservableStringListVar,
	style_bundle: typing.Optional[PcStyleBundle] = None,
):
	if style_bundle is None:
		style_bundle = PcStyleBundle().set_pad_y((0, 8)).set_fill(customtkinter.X)

	def on_add_element_button_clicked():
		entry_string_list_var.generate_var()

	# noinspection PyShadowingNames
	return pc_column(
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
			lambda p: pc_column(
				style_bundle=PcStyleBundle()
				.set_width(256)
				.set_expand(True)
				.set_fill(customtkinter.BOTH)
				.set_fg_color("transparent"),
				parent=p,
				child_factories=[
					(
						lambda var_key, string_var:
						lambda p: pc_row(
							style_bundle=PcStyleBundle()
							.set_pad_x((8, 8))
							.set_pad_y((0, 4))
							.set_fill(customtkinter.BOTH),
							parent=p,
							child_factories=[
								lambda p: pc_entry(
									style_bundle=PcStyleBundle()
									.set_width(256),
									parent=p,
									string_var=string_var,
								),
								lambda p: pc_button(
									style_bundle=PcStyleBundle()
									.set_width(256)
									.set_pad_x((4, 0)),
									parent=p,
									string_var=PcStringVar(default_string="Remove"),
									command=lambda: entry_string_list_var.remove(var_key),
								),
							],
						)
					)(var_key, string_var) for var_key, string_var in entry_string_list_var.get_key_string_var_pairs()
				],
			),
			lambda p: pc_button(
				style_bundle=PcStyleBundle()
				.set_width(256),
				parent=p,
				string_var=PcStringVar(default_string="Add Element"),
				command=on_add_element_button_clicked,
			),
		],
		observed_vars=[entry_string_list_var],
	)
