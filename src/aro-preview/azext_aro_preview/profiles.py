# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core.profiles import CustomResourceType

CUSTOM_ARO_PREVIEW = CustomResourceType('azext_saro_preview.vendored_sdks',
                                         'AzureRedHatOpenShiftClient')
