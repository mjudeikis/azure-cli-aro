# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import time
import os

from knack.util import CLIError
from azure.cli.core.commands.client_factory import get_subscription_id
from azure.cli.core.util import sdk_no_wait
from ._client_factory import cf_resource_groups
from .vendored_sdks.models import OpenShiftCluster

from msrestazure.azure_exceptions import CloudError



def aro_preview_create(cmd, client, resource_group_name, resource_name, location=None, tags=None,
                       no_wait=False):
    subscription_id = get_subscription_id(cmd.cli_ctx)

    if location is None:
        rg_location = _get_rg_location(cmd.cli_ctx, resource_group_name)
        location = rg_location


    oc = OpenShiftCluster(
        location = location,
        tags = tags,
    )

    # TODO: implement all other configurables

    max_retry = 30
    retry_exception = Exception(None)
    for _ in range(0, max_retry):
        try:
            return sdk_no_wait(no_wait, client.create,
                resource_group_name=resource_group_name, resource_name=resource_name, parameters=oc)
        except CloudError as ex:
            retry_exception = ex
            if 'not found in Active Directory tenant' in ex.message:
                time.sleep(3)
            else:
                raise ex
    raise retry_exception


    raise CLIError('TODO: Implement `aro_preview create`')

def aro_preview_delete(cmd, client, resource_group_name, resource_name, location=None, tags=None):
    raise CLIError('TODO: Implement `aro_preview create`')


def aro_preview_list(cmd, client, resource_group_name=None, resource_name=None, location=None, tags=None):
    raise CLIError('TODO: Implement `aro_preview list`')

def aro_preview_show(cmd, client, resource_group_name, resource_name, location=None, tags=None):
    raise CLIError('TODO: Implement `aro_preview list`')

def aro_preview_get_credentials(cmd, client, resource_group_name, resource_name, location=None, tags=None):
    raise CLIError('TODO: Implement `aro_preview list`')

def aro_preview_update(cmd, client, resource_group_name, resource_name, location=None, tags=None):
   raise CLIError('TODO: Implement `aro_preview list`')


def _get_rg_location(ctx, resource_group_name, subscription_id=None):
    groups = resource_groups_client_factory(ctx, subscription_id=subscription_id)
    # Just do the get, we don't need the result, it will error out if the group doesn't exist.
    rg = groups.get(resource_group_name)
    return rg.location
