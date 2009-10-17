from schedule_box.tests import *

class TestEditController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='edit', action='index'))
        # Test response...
