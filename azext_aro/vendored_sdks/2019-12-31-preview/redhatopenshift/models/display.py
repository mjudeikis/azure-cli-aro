# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Display(Model):
    """Display represents the display details of an operation.

    :param provider: Friendly name of the resource provider.
    :type provider: str
    :param resource: Resource type on which the operation is performed.
    :type resource: str
    :param operation: Operation type: read, write, delete, listKeys/action,
     etc.
    :type operation: str
    :param description: Friendly name of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, provider=None, resource=None, operation=None, description=None):
        super(Display, self).__init__()
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description
