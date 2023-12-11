"""
Main body componets file
"""
import flet as ft
from config import (
    ELEMENT_COLOR,
    ACCENT_COLOR
)


# ------------------------------------------------------------------------------------App body class
class Body(ft.UserControl):
    """_summary_

    Args:
        ft (_type_): _description_
    """

    def __init__(self):
        super().__init__()

        self.role_selector = RoleSelector(
            on_change=self.on_role_changed
        )

        self.driver_content = DriverContent()
        self.inspector_cointent = InspectorContent()
        self.operator_content = OperatorContent()

        self.driver_content.visible = True
        self.inspector_cointent.visible = False
        self.operator_content.visible = False

        self.content_fields = [
            self.driver_content,
            self.inspector_cointent,
            self.operator_content
        ]

    def build(self):
        controls = [
            self.role_selector,
            self.driver_content,
            self.inspector_cointent,
            self.operator_content
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

    def on_role_changed(self):
        """_summary_
        """
        selection = self.role_selector.selection

        for content_field in self.content_fields:
            if content_field.id == selection:
                content_field.visible = True
            else:
                content_field.visible = False

        super().update()


# -------------------------------------------------------------------------------Role selector class
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
                    icon=ft.icons.PERSON_3,
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


# ---------------------------------------------------------------------------Content Field baseclass
class ContentField(ft.UserControl):
    """_summary_

    Args:
        ft (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.id = None


# ---------------------------------------------------------Content Field targetclasses
class DriverContent(ContentField):
    """_summary_

    Args:
        ContentField (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.id = "Водитель"

    def build(self):
        return ft.Text(value=self.id)


class InspectorContent(ContentField):
    """_summary_

    Args:
        ContentField (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.id = "Инспектор"

    def build(self):
        return ft.Text(value=self.id)


class OperatorContent(ContentField):
    """_summary_

    Args:
        ContentField (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.id = "Оператор"

    def build(self):
        return ft.Text(value=self.id)
