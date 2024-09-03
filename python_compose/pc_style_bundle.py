import typing
import customtkinter


class PcStyleBundle:
	def __init__(self):
		self.pad_x: typing.Union[int, typing.Tuple[int, int]] = 0
		self.pad_y: typing.Union[int, typing.Tuple[int, int]] = 0
		self.ipad_x: typing.Union[int, typing.Tuple[int, int]] = 0
		self.ipad_y: typing.Union[int, typing.Tuple[int, int]] = 0
		self.expand: bool = False
		self.fill: typing.Literal["none", "x", "y", "both"] = customtkinter.NONE
		self.width: typing.Optional[int] = None
		self.height: typing.Optional[int] = None
		self.corner_radius: typing.Optional[int] = None
		self.border_width: typing.Optional[int] = None
		self.border_spacing: int = 2
		self.fg_color: typing.Optional[typing.Union[str, typing.Tuple[str, str]]] = None
		self.bg_color: typing.Union[str, typing.Tuple[str, str]] = "transparent"
		self.hover_color: typing.Optional[typing.Union[str, typing.Tuple[str, str]]] = None
		self.border_color: typing.Optional[typing.Union[str, typing.Tuple[str, str]]] = None
		self.text_color: typing.Optional[typing.Union[str, typing.Tuple[str, str]]] = None
		self.placeholder_text_color: typing.Optional[typing.Union[str, typing.Tuple[str, str]]] = None
		self.text_color_disabled: typing.Optional[typing.Union[str, typing.Tuple[str, str]]] = None
		self.font: typing.Optional[typing.Union[typing.Tuple, customtkinter.CTkFont]] = None
		self.anchor: typing.Literal[
			"n", "s", "w", "e", "nw", "sw", "ne", "se", "ns", "ew", "nsew", "center",
		] = customtkinter.CENTER
		self.justify: typing.Literal["left", "center", "right"] = customtkinter.CENTER

	def set_pad_x(self, pad_x: typing.Union[int, typing.Tuple[int, int]]) -> typing.Self:
		self.pad_x = pad_x
		return self

	def set_pad_y(self, pad_y: typing.Union[int, typing.Tuple[int, int]]) -> typing.Self:
		self.pad_y = pad_y
		return self

	def set_ipad_x(self, ipad_x: typing.Union[int, typing.Tuple[int, int]]) -> typing.Self:
		self.ipad_x = ipad_x
		return self

	def set_ipad_y(self, ipad_y: typing.Union[int, typing.Tuple[int, int]]) -> typing.Self:
		self.ipad_y = ipad_y
		return self

	def set_expand(self, expand: bool) -> typing.Self:
		self.expand = expand
		return self

	def set_fill(self, fill: typing.Literal["none", "x", "y", "both"]) -> typing.Self:
		self.fill = fill
		return self

	def set_width(self, width: int) -> typing.Self:
		self.width = width
		return self

	def set_height(self, height: int) -> typing.Self:
		self.height = height
		return self

	def set_corner_radius(self, corner_radius: typing.Optional[int]) -> typing.Self:
		self.corner_radius = corner_radius
		return self

	def set_border_width(self, border_width: typing.Optional[int]) -> typing.Self:
		self.border_width = border_width
		return self

	def set_border_spacing(self, border_spacing: typing.Optional[int]) -> typing.Self:
		self.border_spacing = 2 if border_spacing is None else border_spacing
		return self

	def set_fg_color(self, fg_color: typing.Optional[typing.Union[str, tuple[str, str]]]) -> typing.Self:
		self.fg_color = fg_color
		return self

	def set_bg_color(self, bg_color: typing.Union[str, tuple[str, str]]) -> typing.Self:
		self.bg_color = bg_color
		return self

	def set_hover_color(self, hover_color: typing.Optional[typing.Union[str, tuple[str, str]]]) -> typing.Self:
		self.hover_color = hover_color
		return self

	def set_border_color(self, border_color: typing.Optional[typing.Union[str, tuple[str, str]]]) -> typing.Self:
		self.border_color = border_color
		return self

	def set_text_color(self, text_color: typing.Optional[typing.Union[str, tuple[str, str]]]) -> typing.Self:
		self.text_color = text_color
		return self

	def set_placeholder_text_color(
		self,
		placeholder_text_color: typing.Optional[typing.Union[str, tuple[str, str]]],
	) -> typing.Self:
		self.placeholder_text_color = placeholder_text_color
		return self

	def set_text_color_disabled(
		self,
		text_color_disabled: typing.Optional[typing.Union[str, tuple[str, str]]],
	) -> typing.Self:
		self.text_color_disabled = text_color_disabled
		return self

	def set_font(self, font: typing.Optional[typing.Union[tuple, customtkinter.CTkFont]]) -> typing.Self:
		self.font = font
		return self

	def set_anchor(
		self,
		anchor: typing.Literal["n", "s", "w", "e", "nw", "sw", "ne", "se", "ns", "ew", "nsew", "center",],
	) -> typing.Self:
		self.anchor = anchor
		return self

	def set_justify(
		self,
		justify: typing.Literal["left", "center", "right"],
	) -> typing.Self:
		self.justify = justify
		return self
