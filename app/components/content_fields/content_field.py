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

    def build(self):
        controls = [
            InputField(self.id_label),
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


class InputField(ft.UserControl):
    """_summary_

    Args:
        ft (_type_): _description_
    """
    def __init__(self, id_label):
        super().__init__()
        self.id_label = id_label

    def build(self):
        controls = [
            ft.TextField(
                label=self.id_label
            ),
            ft.IconButton(
                icon=ft.icons.CHECK,
                icon_size=40,
                on_click=None,
                bgcolor=ACCENT_COLOR
            )
        ]

        content = ft.Row(
            controls=controls,
            alignment=ft.MainAxisAlignment.CENTER,
        )

        return content
