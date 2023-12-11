"""
App main file
"""

import flet as ft
from config import (
    VIEW_MODE,
    BACKGROUND_COLOR,
    APP_TITLE,
    APP_PORT
)
from .components import (
    Body,
)


class App:
    """_summary_
    """
    def page(self, page: ft.Page):
        """
        Defines the type of main page
        """
        # ---App Settings---
        page.title = APP_TITLE
        page.bgcolor = BACKGROUND_COLOR
        page.update()

        # -----App body-----

        body = Body()
        page.add(body)

    def run(self, view_mode: str = "web"):
        """_summary_

        Args:
            view_mode (str, optional): _description_. Defaults to "web".
        """
        ft.app(
            target=self.page,
            view=VIEW_MODE[view_mode],
            port=APP_PORT
        )
