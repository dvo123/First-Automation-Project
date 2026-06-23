import pytest
from utils.config_reader import ConfigReader
from utils.api_helper import APIHelper

class TestDummyJsonProductAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_helper = APIHelper(base_url=ConfigReader.get_base_api_url())
        yield
        self.api_helper.close_session()

    @pytest.mark.get
    def test_get_product_by_id(self):
        product_id = 1
        # DummyJSON uses the plural 'products' path
        response = self.api_helper.get(f"products/{product_id}")

        assert response.status_code == 200
        product = response.json()
        assert product['id'] == product_id
        assert product["title"] == 'Essence Mascara Lash Princess'