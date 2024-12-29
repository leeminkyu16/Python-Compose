import typing
import weakref

import customtkinter

from python_compose.helpers.create_child_helper import create_child_helper
from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_observable import PcObservable


def pc_tk(
	style_bundle: PcStyleBundle,
	title: str,
	child_factories: typing.List[typing.Callable[[customtkinter.CTk], PcBaseClassWrapper]],
	observed_vars: typing.Optional[typing.List[PcObservable]] = None,
):
	if observed_vars is None:
		observed_vars = []

	def create_widget():
		c_tk = customtkinter.CTk(
			fg_color=style_bundle.fg_color,
		)

		c_tk.title(title)

		children: typing.Set[PcBaseClassWrapper] = set()
		list_of_finalize: typing.List[weakref.finalize] = []

		initial_render: bool = True

		def create_children():
			total_height = 0
			max_width = 0
			for child_factory in child_factories:
				# noinspection PyTypeChecker
				new_child = create_child_helper(
					parent=c_tk,
					child_factory=child_factory,
					children=children,
					list_of_finalize=list_of_finalize,
					create_children=create_children,
					observed_vars=observed_vars,
				)

				if new_child is None or new_child.widget is None:
					continue

				children.add(new_child)
				total_height += new_child.get_height()
				max_width = max(max_width, new_child.get_width())

				new_child.widget.pack(
					side=customtkinter.TOP,
					padx=new_child.style_bundle.pad_x,
					pady=new_child.style_bundle.pad_y,
					ipadx=new_child.style_bundle.ipad_x,
					ipady=new_child.style_bundle.ipad_y,
					expand=new_child.style_bundle.expand,
					fill=new_child.style_bundle.fill,
					anchor=new_child.style_bundle.anchor,
				)

			screen_width = c_tk.winfo_screenwidth()
			screen_height = c_tk.winfo_screenheight()

			set_width = max_width if style_bundle.width is None else style_bundle.width
			set_height = total_height if style_bundle.height is None else style_bundle.height

			if initial_render:
				c_tk.geometry(
					"".join(
						(
							str(set_width),
							"x",
							str(set_height),
							"+",
							str(
								int(
									(screen_width / 2) - (set_width / 2)
								)
							),
							"+",
							str(
								int(
									(screen_height / 2) - (set_height / 2)
								)
							),
						)
					)
				)
				c_tk.focus()
			else:
				c_tk.geometry(
					"".join(
						(
							str(set_width),
							"x",
							str(set_height),
						)
					)
				)

		create_children()

		initial_render = False

		return c_tk

	# noinspection PyTypeChecker
	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
	)
