# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.secureforms.testing import COLLECTIVE_SECUREFORMS_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.secureforms is properly installed."""

    layer = COLLECTIVE_SECUREFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.secureforms is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.secureforms'))

    def test_browserlayer(self):
        """Test that ICollectiveSecureformsLayer is registered."""
        from collective.secureforms.interfaces import (
            ICollectiveSecureformsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveSecureformsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_SECUREFORMS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.secureforms'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.secureforms is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.secureforms'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveSecureformsLayer is removed."""
        from collective.secureforms.interfaces import \
            ICollectiveSecureformsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveSecureformsLayer,
            utils.registered_layers())
