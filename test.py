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

    def test_generate_phosus_token(self):
        api = PixlrApi()
        assert api._generate_phosus_auth_token() is not None

    def test_remove_background(self):
        api = PixlrApi()
        image = api.remove_background("./dummy.jpg")
        print("test_remove_background IMAGE PATH: ", image)
        assert image is not None

    def test_auto_fix(self):
        api = PixlrApi()
        image = api.auto_fix("./dummy.jpg")
        print("test_auto_fix IMAGE PATH: ", image)
        assert image is not None


if __name__ == "__main__":
    # Ask which tests to run.
    # Get all method names in the class
    print("0. Run all tests")
    tests = [i for i in dir(TestPixlrApi) if i.startswith("test_")]
    for test in tests:
        print(f"{tests.index(test) + 1}. {test}")

    choice = int(input("Enter the test number to run: "))
    if choice == 0:
        unittest.main()
    else:
        test_name = tests[choice - 1]
        suite = unittest.TestSuite()
        suite.addTest(TestPixlrApi(test_name))
        unittest.TextTestRunner().run(suite)
