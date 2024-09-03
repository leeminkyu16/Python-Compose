import typing
import weakref

import customtkinter

from python_compose.helpers.create_child_helper import create_child_helper
from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.pc_style_bundle import PcStyleBundle
from python_compose.variables.pc_boolean_var import PcBooleanVar


def pc_column(
	style_bundle: PcStyleBundle,
	parent: typing.Any,
	child_factories: typing.List[typing.Callable[[customtkinter.CTkBaseClass], PcBaseClassWrapper]],
	active: typing.Optional[PcBooleanVar] = None,
) -> PcBaseClassWrapper:
	if active is None:
		active = PcBooleanVar(default_bool=True)

	def create_widget():
		if not active.get():
			return None
		active.set_parent(parent=parent)
		new_column = customtkinter.CTkFrame(
			master=parent,
			width=200 if style_bundle.width is None else style_bundle.width,
			height=200 if style_bundle.height is None else style_bundle.height,
			bg_color=style_bundle.bg_color,
			fg_color=style_bundle.fg_color,
			border_color=style_bundle.border_color,
		)

		children: typing.Set[PcBaseClassWrapper] = set()
		list_of_finalize: typing.List[weakref.finalize] = []

		def create_children():
			total_height = 0
			max_width = 0
			for child_factory in child_factories:
				new_child = create_child_helper(
					parent=new_column,
					child_factory=child_factory,
					children=children,
					list_of_finalize=list_of_finalize,
					create_children=create_children,
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

			if style_bundle.width is None:
				new_column.configure(width=max_width)
			if style_bundle.height is None:
				new_column.configure(height=total_height)

		create_children()
		return new_column

	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
	)
