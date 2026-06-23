import logging
from typing import Dict, Any, Optional
import requests
from utils.config_reader import ConfigReader
# logger = logging.getLogger(__name__)

class APIHelper:
    def __init__(self, base_url: str, timeout: float = 10.0, headers: Optional[Dict[str, str]] = None):
        """Initialize API helper.

        base_url: full base URL like 'https://dummyjson.com'
        """
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(headers or {"Accept": "application/json"})

    def request(self, method, endpoint, param = None, json_data = None, headers = None, timeout = None):
        # Tao URL day du
        endpoint = endpoint.lstrip('/')
        url = self.base_url + "/" + endpoint

        # Gui request
        response = self.session.request(
            method=method,
            url=url,
            params=param,
            json=json_data,
            headers=headers,
            timeout=timeout or self.timeout
        )

        # 3. Ghi log status code tra ve
        # simple logging for debug
        print(f"Response status code: {response.status_code}")

        # 4. Ghi log status code tra
        return response

    # This is the main method that all other HTTP methods will call
    def get(self, endpoint, params=None):
        response = self.request(
            method="GET",
            endpoint=endpoint,
            param=params
        )
        return response

    def post(self, endpoint, data=None):
        response = self.request(
            method="POST",
            endpoint=endpoint,
            json_data=data
        )
        return response
    def close(self):
        self.session.close()

    # Kept for compatibility with existing code
    close_session = close