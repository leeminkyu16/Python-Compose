import typing
import weakref

from python_compose.pc_base_class_wrapper import PcBaseClassWrapper
from python_compose.variables.pc_observable import PcObservable


def clear_list_of_finalize(list_of_finalize: typing.List[weakref.finalize]) -> None:
	for finalizer in list_of_finalize:
		if finalizer.alive:
			finalizer_detach_output = finalizer.detach()
			func = finalizer_detach_output[1]
			if isinstance(func, typing.Callable):
				func()
	list_of_finalize.clear()


def setup_child_creation(
	parent: typing.Any,
	children: typing.Set[PcBaseClassWrapper],
	create_children: typing.Callable[[], None],
	observed_vars: typing.List[PcObservable],
	list_of_finalize: typing.List[weakref.finalize],
):
	clear_list_of_finalize(list_of_finalize)

	def on_change(_: typing.Any):
		for child in children:
			child.destroy()
		children.clear()
		create_children()

	for observed_var in observed_vars:
		on_change_unsubscribe = observed_var.add_on_change(on_change=on_change)
		list_of_finalize.append(weakref.finalize(parent, on_change_unsubscribe))
