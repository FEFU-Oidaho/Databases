"""_summary_

Returns:
    _type_: _description_
"""

from .content_field import ContentField


class OperatorContent(ContentField):
    """_summary_

    Args:
        ContentField (_type_): _description_
    """

    def __init__(self, need_login: bool = True):
        super().__init__()
        self.id = "Оператор"
        self.id_label = "Удостоверение оператора"

        self.need_login = need_login
