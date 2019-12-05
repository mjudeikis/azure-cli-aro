# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.operations import Operations
from .operations.open_shift_clusters_operations import OpenShiftClustersOperations
from . import models


class AzureRedHatOpenShiftClientConfiguration(Configuration):
    """Configuration for AzureRedHatOpenShiftClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, credentials, base_url=None):

        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(AzureRedHatOpenShiftClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azureredhatopenshiftclient/{}'.format(VERSION))

        self.subscription_id = subscription_id
        self.credentials = credentials


class AzureRedHatOpenShiftClient(object):
    """Rest API for Azure Red Hat OpenShift

    :ivar config: Configuration for client.
    :vartype config: AzureRedHatOpenShiftClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: redhatopenshift.operations.Operations
    :ivar open_shift_clusters: OpenShiftClusters operations
    :vartype open_shift_clusters: redhatopenshift.operations.OpenShiftClustersOperations

    :param subscription_id: Subscription credentials which uniquely identify
     Microsoft Azure subscription. The subscription ID forms part of the URI
     for every service call.
    :type subscription_id: str
    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    :param str base_url: Service URL
    """

    def __init__(
            self, subscription_id, credentials, base_url=None):

        self.config = AzureRedHatOpenShiftClientConfiguration(subscription_id, credentials, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-12-31-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.open_shift_clusters = OpenShiftClustersOperations(
            self._client, self.config, self._serialize, self._deserialize)
