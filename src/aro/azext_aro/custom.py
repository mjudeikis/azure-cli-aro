# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_aro(cmd, client, resource_group_name, resource_name, location=None, tags=None):
    raise CLIError('TODO: Implement `aro create`')


def list_aro(cmd, client, resource_group_name=None):
    raise CLIError('TODO: Implement `aro list`')


def update_aro(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance