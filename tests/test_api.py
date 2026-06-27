import pytest
from utils.config_reader import ConfigReader
from utils.api_helper import APIHelper

class TestDummyJsonProductAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_helper = APIHelper(base_url=ConfigReader.get_base_api_url())
        yield
        self.api_helper.close_session()

    def test_get_product_by_id(self):
        product_id = 1
        # DummyJSON uses the plural 'products' path
        response = self.api_helper.get(f"products/{product_id}")

        assert response.status_code == 200
        product = response.json()
        assert product['id'] == product_id
        assert product["title"] == 'Essence Mascara Lash Princess'

    def test_create_product(self):
        new_product_data = {
            "title": "Test Product",
            "price": 99.99,
            "brand": "Test Brand",
            "category": "test-category"
        }
        response = self.api_helper.post("products/add", data=new_product_data)

        assert response.status_code == 201
        created_product = response.json()
        assert created_product["title"] == new_product_data["title"]
        assert created_product["price"] == new_product_data["price"]
        assert created_product["brand"] == new_product_data["brand"]
        assert created_product["category"] == new_product_data["category"]

    def test_update_product(self):
        updated_product = {
            "title": "Updated Product",
            "price": 199.99
        }

        response = self.api_helper.put(
            "products/1",
            data=updated_product
        )

        assert response.status_code == 200

        product = response.json()

        assert product["id"] == 1
        assert product["title"] == "Updated Product"
        assert product["price"] == 199.99

    def test_delete_product(self):
        response = self.api_helper.delete("products/1")

        assert response.status_code == 200

        deleted_product = response.json()

        assert deleted_product["id"] == 1
        assert deleted_product["isDeleted"] is True