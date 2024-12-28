import customtkinter

from python_compose.pc_button import pc_button
from python_compose.pc_scrollable_frame import pc_scrollable_frame
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.pc_tk import pc_tk
from python_compose.variables.pc_observable_bool import PcObservableBool
from python_compose.variables.pc_string_var import PcStringVar
from tests.example.page_1 import page_1
from tests.example.page_2 import page_2


def example_ui():
	page_1_active = PcObservableBool(value=True)
	page_2_active = PcObservableBool(value=False)
	page_3_active = PcObservableBool(value=False)

	def switch_to_page_func_factory(input_variable: PcObservableBool):
		def output_function():
			for iter_variable in [
				page_1_active,
				page_2_active,
				page_3_active,
			]:
				if iter_variable == input_variable:
					iter_variable.set(True)
				else:
					iter_variable.set(False)

		return output_function

	pc_tk(
		style_bundle=PcStyleBundle()
		.set_width(512)
		.set_height(512),
		title="Example",
		child_factories=[
			lambda p: pc_scrollable_frame(
				style_bundle=PcStyleBundle()
				.set_fill(customtkinter.X),
				parent=p,
				orientation="horizontal",
				child_factories=[
					lambda p: pc_button(
						style_bundle=PcStyleBundle()
						.set_corner_radius(0)
						.set_fg_color("transparent"),
						parent=p,
						string_var=PcStringVar(
							default_string="Page 1",
						),
						command=switch_to_page_func_factory(page_1_active),
					),
					lambda p: pc_button(
						style_bundle=PcStyleBundle()
						.set_corner_radius(0)
						.set_fg_color("transparent"),
						parent=p,
						string_var=PcStringVar(
							default_string="Page 2",
						),
						command=switch_to_page_func_factory(page_2_active),
					),
					lambda p: pc_button(
						style_bundle=PcStyleBundle()
						.set_corner_radius(0)
						.set_fg_color("transparent"),
						parent=p,
						string_var=PcStringVar(
							default_string="Page 3",
						),
						command=switch_to_page_func_factory(page_3_active),
					),
				],
			),
			lambda p: page_1(
				parent=p,
				active=page_1_active,
			),
			lambda p: page_2(
				parent=p,
				active=page_2_active,
			),
		]
	).widget.mainloop()


if __name__ == "__main__":
	example_ui()
