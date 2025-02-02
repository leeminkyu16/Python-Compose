import typing
import weakref

import customtkinter

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper


def create_child_helper(
	parent: customtkinter.CTkBaseClass,
	child_factory: typing.Callable[[customtkinter.CTkBaseClass], PcBaseClassWrapper],
	children: typing.Set[PcBaseClassWrapper],
	list_of_finalize: typing.List[weakref.finalize],
	create_children: typing.Callable[[], None],
) -> PcBaseClassWrapper:
	new_child = child_factory(parent)
	new_child_weak_ref = weakref.ref(new_child)

	def on_active_change(new_value: bool):
		if new_value:
			for child in children:
				child.destroy()
			children.clear()
			create_children()
		else:
			weak_new_child = new_child_weak_ref()
			if weak_new_child is not None and weak_new_child.widget is not None:
				weak_new_child.destroy()
			if weak_new_child in children:
				children.remove(weak_new_child)

	active_on_change_unsubscribe = new_child.active.add_on_change(on_change=on_active_change)
	list_of_finalize.append(weakref.finalize(parent, active_on_change_unsubscribe))

	return new_child


