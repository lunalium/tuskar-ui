# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django import http
from django.core.urlresolvers import reverse

from mox import IsA

from openstack_dashboard import api
from openstack_dashboard.test import helpers as test


class ResourceManagementTests(test.BaseAdminViewTests):
    def setUp(self):
        super(ResourceManagementTests, self).setUp()

    def test_index(self):
        #flavors = self.flavors.list()
        #self.mox.StubOutWithMock(api.management, 'flavor_list')

        #api.management.flavor_list(IsA(http.HttpRequest)).AndReturn(flavors)

        self.mox.ReplayAll()

        url = reverse('horizon:infrastructure:resource_management:index')
        res = self.client.get(url)

        self.assertTemplateUsed(
            res, 'infrastructure/resource_management/index.html')
        #self.assertItemsEqual(res.context['flavors_table'].data, flavors)