class TestCase:  # Classe Base Abstrata (ou Template Class)

    def __init__(self, test_method_name):
        self.test_method_name = test_method_name

    def run(self, result): #essa classe agora receber como parâmetro o resultado do teste
        result.test_started() #this.testresult.run_count += 1
        self.set_up() #this.set_up
        try:
            test_method = getattr(self, self.test_method_name) #extração do nome do método de
            test_method() #chamando o método com o nome que o getattr extraiu
        except AssertionError as e:
            result.add_failure(self.test_method_name)
        except Exception as e:
            result.add_error(self.test_method_name)
        self.tear_down()

    def set_up(self):  # método sobescrevível
        pass

    def tear_down(self):  # método sobescrevível
        pass
    

    
    
       