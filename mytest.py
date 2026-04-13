from testcase import TestCase
from testresult import TestResult
from testcasetest import TestCaseTest
from testsuite import TestSuite
from testsuitetest import TestSuiteTest

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


result = TestResult()
suite = TestSuite()

suite.add_test(TestCaseTest('test_result_success_run'))
suite.add_test(TestCaseTest('test_result_failure_run'))
suite.add_test(TestCaseTest('test_result_error_run'))
suite.add_test(TestCaseTest('test_result_multiple_run'))
suite.add_test(TestCaseTest('test_was_set_up'))
suite.add_test(TestCaseTest('test_was_run'))
suite.add_test(TestCaseTest('test_was_tear_down'))
suite.add_test(TestCaseTest('test_template_method'))

suite.add_test(TestSuiteTest('test_suite_size'))
suite.add_test(TestSuiteTest('test_suite_success_run'))
suite.add_test(TestSuiteTest('test_suite_multiple_run'))

suite.run(result)
print(result.summary())

# a classe MyTest está herdando os métodos da template class TestCase,
# definindo o set_up específico da classe(implementando da classe pai que permite sua implementação),
# definindo os casos de teste específicos da classe. (test_a, test_b, test_c)
# depois para cada teste que é feito ele instancia uma classe dessa e roda o run(que é da classe pai e faz a rotina de teste)
# dessa vez para cada caso do stub
# estamos aqui testando os casos de teste agora
