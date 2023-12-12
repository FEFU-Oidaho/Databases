"""
Main body componets file
"""
import flet as ft
from config import ELEMENT_COLOR
from .role_selector import RoleSelector
from .content_fields import (
    DriverContent,
    InspectorContent,
    OperatorContent
)


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
        ]
        controls.extend(self.content_fields)

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
