from testcase import TestCase
from testresult import TestResult
from testcasetest import TestCaseTest
from testsuite import TestSuite
from testsuitetest import TestSuiteTest
from testloader import TestLoader
from testloadertest import TestLoaderTest
from testrunner import TestRunner

class MyTest(TestCase):

    def set_up(self):
        print("set_up")  # sobescrita de método

    # definção dos casos de teste
    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

    def test_c(self):
        print("test_c")

    # sobescrita de método
    def tear_down(self):
        print("tear_down")




