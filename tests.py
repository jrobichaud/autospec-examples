import unittest
from unittest import mock

import module_to_test
import test_utils


class SignatureTestCase(unittest.TestCase):
    def test_signature_problem(self):
        with mock.patch("my_module.MyClass.some_method") as mock_some_method:
            module_to_test.signature_problem()
        mock_some_method.assert_called_once_with("Bar", "Buzz")
        self.skipTest(
            "When the signature of a function changes we want the tests to fail..."
        )

    def test_auto_spec_to_the_rescue(self):
        with mock.patch(
            "my_module.MyClass.some_method", autospec=True
        ), self.assertRaises(TypeError) as ex:
            module_to_test.signature_problem()
        self.assertEqual("too many positional arguments", str(ex.exception))


class ClassAutoSpecTestCase(unittest.TestCase):
    def test_full_auto_spec(self):
        with mock.patch("my_module.MyClass", autospec=True), self.assertRaises(
            AttributeError
        ) as ex:
            module_to_test.my_method_to_test()

        self.assertEqual("Mock object has no attribute 'name'", str(ex.exception))

    def test_appropriate_auto_spec(self):
        with mock.patch("my_module.MyClass", autospec=True) as mock_my_class:
            mock_instance = mock_my_class.return_value
            mock_instance.name = "ZZZ"

            result = module_to_test.my_method_to_test()

        mock_my_class.assert_called_once_with("Foo")
        """validates if constructor was called"""

        mock_instance.some_method.assert_called_once_with("Bar")

        self.assertEqual("ZZZ", result, "The mock works properly")


class ImportTestCase(unittest.TestCase):
    def test_incorrect_import(self):
        with mock.patch("my_module.MyClass") as mock_my_class:
            mock_instance = mock_my_class.return_value
            mock_instance.name = "ZZZ"
            mock_instance.some_method.assert_not_called()
            result = module_to_test.incorrect_import()
        self.assertEqual("Foo", result, "The mock does not work properly")

    def test_correct_import(self):
        with mock.patch("my_module.MyClass") as mock_my_class:
            mock_instance = mock_my_class.return_value
            mock_instance.name = "ZZZ"
            result = module_to_test.my_method_to_test()
        self.assertEqual("ZZZ", result, "The mock works properly")
        mock_instance.some_method.assert_called_once_with("Bar")


class AutoSpecStaticMethod(unittest.TestCase):
    def test_auto_spec_for_all_python_versions(self):
        with mock.patch(
            "my_module.MyClass.some_static_method",
            autospec=test_utils.STATIC_METHOD_AUTO_SPEC,
        ):
            pass

        self.assertTrue("autospec of static methods only works only with python 3.7.4+")
