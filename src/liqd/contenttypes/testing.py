from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class LiqdcontenttypesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import liqd.contenttypes
        xmlconfig.file(
            'configure.zcml',
            liqd.contenttypes,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'liqd.contenttypes:default')

LIQD_CONTENTTYPES_FIXTURE = LiqdcontenttypesLayer()
LIQD_CONTENTTYPES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LIQD_CONTENTTYPES_FIXTURE,),
    name="LiqdcontenttypesLayer:Integration"
)
LIQD_CONTENTTYPES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LIQD_CONTENTTYPES_FIXTURE, z2.ZSERVER_FIXTURE),
    name="LiqdcontenttypesLayer:Functional"
)
