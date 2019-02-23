from tests.all.integration.setup_database import Setup
from tests.all.integration.utils import OpenEventTestCase
from app import current_app as app
from app.models import db
from app.models.setting import Setting
from app.api.helpers.third_party_auth import GoogleOAuth, FbOAuth, TwitterOAuth, InstagramOAuth 
import unittest

class TestThirdPartyAuth(OpenEventTestCase):
    def setUp(self):
        self.app = Setup.create_app()
    
    def test_google_get_client_id(self):
