import typing
import weakref

import customtkinter
from customtkinter import CTkScrollableFrame

from python_compose.helpers.create_child_helper import create_child_helper
from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.variables.pc_observable_bool import PcObservableBool
from python_compose.pc_style_bundle import PcStyleBundle


def pc_scrollable_frame(
	style_bundle: PcStyleBundle,
	parent: typing.Any,
	child_factories: typing.List[typing.Callable[[customtkinter.CTkBaseClass], PcBaseClassWrapper]],
	active: typing.Optional[PcObservableBool] = None,
	orientation: typing.Literal["vertical", "horizontal"] = "vertical",
) -> typing.Optional[PcBaseClassWrapper]:
	if active is None:
		active = PcObservableBool(value=True)

	def create_widget():
		if not active.get():
			return None

		scrollable_frame: CTkScrollableFrame = customtkinter.CTkScrollableFrame(
			master=parent,
			width=(200 if style_bundle.width is None else style_bundle.width),
			height=(200 if style_bundle.height is None else style_bundle.height),
			corner_radius=style_bundle.corner_radius,
			border_width=style_bundle.border_width,
			bg_color=style_bundle.bg_color,
			fg_color=style_bundle.fg_color,
			border_color=style_bundle.border_color,
			orientation=orientation
		)

		children: typing.Set[PcBaseClassWrapper] = set()
		list_of_finalize: typing.List[weakref.finalize] = []

		def create_children():
			max_width = 0
			max_height = 0
			for child_factory in child_factories:
				# noinspection PyTypeChecker
				new_child = create_child_helper(
					parent=scrollable_frame,
					child_factory=child_factory,
					children=children,
					list_of_finalize=list_of_finalize,
					create_children=create_children,
				)

				if new_child is None or new_child.widget is None:
					continue

				children.add(new_child)
				max_width = max(max_width, new_child.get_width())
				max_height = max(max_height, new_child.get_height())

				if orientation == "vertical":
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
				elif orientation == "horizontal":
					new_child.widget.pack(
						side=customtkinter.LEFT,
						padx=new_child.style_bundle.pad_x,
						pady=new_child.style_bundle.pad_y,
						ipadx=new_child.style_bundle.ipad_x,
						ipady=new_child.style_bundle.ipad_y,
						expand=new_child.style_bundle.expand,
						fill=new_child.style_bundle.fill,
						anchor=new_child.style_bundle.anchor,
					)
				else:
					raise ValueError()

				def on_change(new_value: bool):
					if new_value:
						for child in children:
							child.widget.pack_forget()
						children.clear()
						create_children()
					else:
						new_child.widget.pack_forget()

				new_child.active.add_on_change(on_change=on_change)

			if style_bundle.width is None and orientation == "vertical":
				scrollable_frame.configure(width=max_width)
			elif style_bundle.height is None and orientation == "horizontal":
				scrollable_frame.configure(height=max_height)

		create_children()
		# To enforce set height or width
		if orientation == "vertical":
			scrollable_frame._scrollbar.configure(height=0)
		else:
			scrollable_frame._scrollbar.configure(width=0)
		return scrollable_frame

	# noinspection PyTypeChecker
	return PcBaseClassWrapper(
		widget=create_widget(),
		style_bundle=style_bundle,
		create_widget=create_widget,
		active=active,
	)
