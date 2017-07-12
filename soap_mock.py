from lxml import etree
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
    
        parser = etree.XMLParser(ns_clean=True)
        data = request.get_data()
        tree = etree.fromstring(data, parser)
 
        variable_value = ''
        for item in get_element_by_tag(tree, self.variable_xpath):
            variable_value = item.text
        print('Variable value="%s"' % variable_value)

        if self.response_time > 0:
            print('Waiting for %s s' % self.response_time)
            time.sleep(self.response_time)

        response_file_name = variable_value + '.' + self.extension
        response_file_path = self.responses_dir + self.separator + self.directory + self.separator + response_file_name
        response = ''

        if os.path.exists(response_file_path) == False:
            response_file_path = self.responses_dir + self.separator + self.directory + self.separator + self.default_response
        print('Returned file: %s' % response_file_path)

        #TODO sale!
        with open(response_file_path) as fp:
            for line in fp:
                response += line
        
        return response, 200

            
    def get_route(self):
        return self.route



def get_element_by_tag(element, tag):
    if element.tag.endswith(tag):
        yield element
    for child in element:
        for g in get_element_by_tag(child, tag):
            yield g
        