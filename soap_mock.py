import re
import os.path
import time

class SoapMock:

    extension = 'xml'
    responses_dir = 'responses'
    separator ='/'
    default_response = '__default__.xml'
    response_time = 0

    def __init__(self, route, variable_xpath, directory=None, response_time=0):
        self.route = route
        self.enabled = True
        self.variable_xpath = variable_xpath
        self.directory = directory or route
        self.response_time = response_time

    def handle(self, request):
        print('Handles "%s" mock' % self.route)
        if self.enabled == False:
            abort(404, "disabled service")

        data = request.get_data().decode("utf-8") 
        variable_value = self.get_variable_value(data)
        print('Variable value="%s"' % variable_value)

        if self.response_time > 0:
            print('Waiting for %s s' % self.response_time)
            time.sleep(self.response_time)

        response_file_name = variable_value + '.' + self.extension
        response_file_path = self.generate_file_path(response_file_name)

        if os.path.exists(response_file_path) == False:
            response_file_path = self.generate_file_path(self.default_response)
        print('Returned file: %s' % response_file_path)

        response = ''
        with open(response_file_path) as fp:
            for line in fp:
                response += line

        return 200, response

    def generate_file_path(self, filename):
        return self.responses_dir + self.separator + self.directory + self.separator + filename

    def get_route(self):
        return self.route

    def get_variable_value(self, data):
        variable_regex = "%s>(.+?)<" % self.variable_xpath
        variable_pattern = re.compile(variable_regex)
        values = re.findall(variable_pattern, data)
        if len(values) > 0:
            return values[0]
        return ''

    def get_response_files(self):
        files = os.listdir(self.responses_dir + self.separator + self.directory)
        return files
