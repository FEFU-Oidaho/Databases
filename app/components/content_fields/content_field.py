"""_summary_

Returns:
    _type_: _description_
"""

import flet as ft
from config import (
    ACCENT_COLOR,
    BACKGROUND_COLOR
)


class ContentField(ft.UserControl):
    """_summary_

    Args:
        ContentField (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.id = None
        self.id_label = None

        self.input_field = None

        self.need_login = None

    def build(self):
        self.input_field = InputField(
            self.id_label,
            id_given_func=self.id_given,
        )
        self.input_field.visible = self.need_login

        controls = [
            self.input_field,
        ]

        content = ft.Column(
            controls=controls,
            alignment=ft.MainAxisAlignment.CENTER
        )

        container = ft.Container(
            content=content,
            bgcolor=BACKGROUND_COLOR,
            alignment=ft.alignment.center,
            border_radius=10,
            border=ft.border.all(1, "black"),
            width=1260,
            height=585,
        )

        return container

    def id_given(self, status):
        """_summary_

        Args:
            status (_type_): _description_
        """


class InputField(ft.UserControl):
    """_summary_

    Args:
        ft (_type_): _description_
    """

    def __init__(self, id_label, id_given_func):
        super().__init__()
        self.id_label = id_label
        self.id_given_func = id_given_func

        self.text_input = None
        self.button_input = None

    def build(self):
        self.text_input = ft.TextField(
            label=self.id_label,
            border_color="white",
        )
        self.button_input = ft.IconButton(
            icon=ft.icons.CHECK,
            icon_size=40,
            on_click=self.on_click,
            bgcolor=ACCENT_COLOR
        )

        controls = [
            self.text_input,
            self.button_input
        ]

        content = ft.Row(
            controls=controls,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        return content

    def on_click(self, e):  # pylint: disable=unused-argument
        """_summary_
        """
        if not self.text_input.value:
            return

        value = self.text_input.value
        self.text_input.value = ""
        super().update()

        # TODO: database request

        self.id_given_func(value)
