# test_blackbox_logger.py

from blackbox_logger.logger import HTTPLogger

logger = HTTPLogger()

fake_headers = {"User-Agent": "curl/7.0"}
fake_body = b'{"username": "admin", "password": "supersecret"}'
fake_request = type("FakeRequest", (object,), {
    "user": type("User", (object,), {"is_authenticated": True, "__str__": lambda self: "admin"})(),
    "META": {"REMOTE_ADDR": "127.0.0.1"}
})()

logger.log_request("POST", "/api/login", fake_headers, fake_body, fake_request)

fake_response_body = b'{"status": "ok"}'
logger.log_response("POST", "/api/login", fake_headers, fake_response_body, 200, fake_request)