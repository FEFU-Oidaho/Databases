"""
Main body componets file
"""
import flet as ft
from config import (
    ELEMENT_COLOR,
)


class Body(ft.UserControl):
    """_summary_

    Args:
        ft (_type_): _description_
    """
    def build(self):
        container = ft.Container(
            content=None,
            alignment=ft.alignment.center,
            bgcolor=ELEMENT_COLOR,
        )
           
        return container
