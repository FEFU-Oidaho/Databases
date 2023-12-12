"""_summary_

Returns:
    _type_: _description_
"""

from .content_field import ContentField

class InspectorContent(ContentField):
    """_summary_

    Args:
        ContentField (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.id = "Инспектор"
        self.id_label = "Удостоверение инспектора"

