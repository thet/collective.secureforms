# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.secureforms


class CollectiveSecureformsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=collective.secureforms)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.secureforms:default')


COLLECTIVE_SECUREFORMS_FIXTURE = CollectiveSecureformsLayer()


COLLECTIVE_SECUREFORMS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_SECUREFORMS_FIXTURE,),
    name='CollectiveSecureformsLayer:IntegrationTesting',
)


COLLECTIVE_SECUREFORMS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_SECUREFORMS_FIXTURE,),
    name='CollectiveSecureformsLayer:FunctionalTesting',
)


COLLECTIVE_SECUREFORMS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_SECUREFORMS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveSecureformsLayer:AcceptanceTesting',
)
