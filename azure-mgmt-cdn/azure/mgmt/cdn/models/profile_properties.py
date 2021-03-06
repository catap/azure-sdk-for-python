# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ProfileProperties(Model):
    """ProfileProperties

    :param Sku sku: Profile sku
    :param str resource_state: Resource status of the profile. Possible
     values include: 'Creating', 'Active', 'Deleting', 'Disabled'
    :param str provisioning_state: Provisioning status of the profile.
     Possible values include: 'Creating', 'Succeeded', 'Failed'
    """ 

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'resource_state': {'key': 'resourceState', 'type': 'ProfileResourceState'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'ProvisioningState'},
    }

    def __init__(self, sku=None, resource_state=None, provisioning_state=None, **kwargs):
        self.sku = sku
        self.resource_state = resource_state
        self.provisioning_state = provisioning_state
