# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Operation(Model):
    """Operation represents an operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that describes the operation.
    :type display: ~redhatopenshift.models.Display
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'Display'},
    }

    def __init__(self, name=None, display=None):
        super(Operation, self).__init__()
        self.name = name
        self.display = display
