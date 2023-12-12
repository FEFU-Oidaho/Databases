"""_summary_

Returns:
    _type_: _description_
"""

import flet as ft


class InspectorContent(ft.UserControl):
    """_summary_

    Args:
        ContentField (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.id = "Инспектор"

    def build(self):
        return ft.Text(value=self.id)
