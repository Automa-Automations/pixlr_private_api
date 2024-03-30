import unittest
from pixlr_private_api.main import PixlrApi


class TestPixlrApi(unittest.TestCase):
    def test_register(self):
        api = PixlrApi()
        assert api.register() is True

    def test_verify(self):
        api = PixlrApi()
        assert api.register() is True
        assert api.verify_email() is True
        assert api.bearer_token is not None

    def test_delete(self):
        api = PixlrApi()
        assert api.register() is True
        assert api.verify_email() is True
        assert api.delete_account() is True

    def test_generate_image(self):
        api = PixlrApi()
        assert api.register() is True
        assert api.verify_email() is True
        assert len(api.generate_image(1024, 1024, 1, "An Image of a cute Cat!")) > 0
        assert len(api.generate_image(1344, 768, 1, "An Image of a cute Dog!")) > 0
        assert len(api.generate_image(768, 1344, 1, "An Image of a cute Bird!")) > 0
        api.delete_account()


if __name__ == "__main__":
    unittest.main()
