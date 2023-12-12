"""_summary_

Returns:
    _type_: _description_
"""

from .content_field import ContentField


class DriverContent(ContentField):
    """_summary_

    Args:
        ContentField (_type_): _description_
    """

    def __init__(self, need_login: bool = True):
        super().__init__()
        self.id = "Водитель"
        self.id_label = "Водительское удостоверение"

        self.need_login = need_login
