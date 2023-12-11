"""
Main body componets file
"""
import flet as ft
from config import (
    ELEMENT_COLOR,
    ACCENT_COLOR
)


class Body(ft.UserControl):
    """_summary_

    Args:
        ft (_type_): _description_
    """

    def build(self):
        controls = [
            RoleSelecter(self.page),
        ]

        content = ft.Column(
            controls=controls,
        )

        container = ft.Container(
            content=content,
            bgcolor=ELEMENT_COLOR,
            border_radius=10,
            border=ft.border.all(1, "black"),
            height=655,
            width=1260,
            padding=5,
            margin=5,
        )

        return container


class RoleSelecter(ft.UserControl):
    """_summary_

    Args:
        ft (_type_): _description_
    """

    def change(self, e):
        pass

    def build(self):
        tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            on_change=self.change,
            tabs=[
                ft.Tab(
                    icon=ft.icons.PERSON,
                    text="Водитель",
                ),
                ft.Tab(
                    icon=ft.icons.PERSON_2,
                    text="Инспектор"
                ),
                ft.Tab(
                    icon=ft.icons.PERSON_3,
                    text="Оператор"
                ),
            ],
            expand=1,
            indicator_color=ACCENT_COLOR,
            label_color=ACCENT_COLOR,
        )

        return tabs
