class NamespaceManager:
    def __init__(self):
        self.namespace = {}

    def set_variable(self, name, value):
        self.namespace[name] = value
        return self.namespace

    def get_variable(self, name):
        try:
            return self.namespace[name]
        except KeyError:
            print('The variable does not exist')

    def delete_variable(self, name):
        try:
            self.namespace.pop(name)
        except KeyError:
            print('The variable does not exist')

    def list_variables(self):
        var_list = []
        for key, value in self.namespace:
            var_list.append(key)

        return var_list


    def execute_function(self, code):
        executed_statement = exec(code, self.namespace)
        return executed_statement