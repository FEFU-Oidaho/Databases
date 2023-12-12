"""_summary_

Returns:
    _type_: _description_
"""

import flet as ft
from config import ACCENT_COLOR


class RoleSelector(ft.UserControl):
    """_summary_

    Args:
        ft (_type_): _description_
    """

    def __init__(self, on_change=None):
        super().__init__()
        self.tabs = None
        self.on_change_func = on_change
        self.selection = None

    def build(self):
        self.tabs = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            on_change=self.on_change_local,
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
                    icon=ft.icons.PERSON_4,
                    text="Оператор"
                ),
            ],
            expand=1,
            indicator_color=ACCENT_COLOR,
            label_color=ACCENT_COLOR,
        )

        self.selection = self.tabs.tabs[self.tabs.selected_index].text
        return self.tabs

    def on_change_local(self, e): # pylint: disable=unused-argument
        """_summary_

        Returns:
            _type_: _description_
        """
        self.selection = self.tabs.tabs[self.tabs.selected_index].text
        self.on_change_func()
