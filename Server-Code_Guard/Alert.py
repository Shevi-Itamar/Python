from CodeAnalysis import CodeAnalysis


class Alert:
    def __init__(self, file):
        self.code_str = file.read().decode('utf-8')

    def get_alerts(self):
        alerts = list()
        result = self.__length_of_file()
        if result:
            alerts.append(result)
        result = self.__len_of_func()
        if result:
            alerts.append(result)
        result = self.__functions_without_docstrings()
        if result:
            alerts.append(result)
        result = self.__unused_variables()
        if result:
            alerts.append(result)
        return alerts

    def __length_of_file(self):
        number_of_lines = CodeAnalysis.number_of_lines(self.code_str)
        if number_of_lines > 200:
            return "The file is too long"
        return None

    def __len_of_func(self):
        alert = "The file has functions that are too long: "
        is_empty = True
        func_len_dict = CodeAnalysis.get_functions_lengths(self.code_str)
        for key, value in func_len_dict.items():
            if value > 20:
                alert += key+":"+str(value)+", "
                is_empty = False
        if is_empty:
            return None
        return alert

    def __functions_without_docstrings(self):
        result = "The following functions do not have docstrings: "
        functions_without_docstrings = CodeAnalysis.get_functions_without_docstrings(self.code_str)
        if len(functions_without_docstrings) > 0:
            for function in functions_without_docstrings:
                result += function+", "
                return result
        return None

    def __unused_variables(self):
        list_of_unused_variables = CodeAnalysis.get_unused_variables(self.code_str)
        if len(list_of_unused_variables) > 0:
            result = "The following variables are not used: "
            for var in list_of_unused_variables:
                result += var+", "
            return result
        else:
            return None