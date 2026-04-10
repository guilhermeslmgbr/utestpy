class TestCase:  # Classe Base Abstrata (ou Template Class)

    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self):
        self.set_up()  # chama método de setup
        test_method = getattr(self, self.test_method_name)
        # Dado uma string com o nome de um método, getattr nos permite executar esse método
        # por exemplo, getattr(x, 'test_foo') é equivalente a x.test_foo
        test_method()  # chama método de teste
        self.tear_down()  # chama método de teardown

    def set_up(self):  # método sobescrevível
        pass

    def tear_down(self):  # método sobescrevível
        pass
