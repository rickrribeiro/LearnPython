import unittest

from main import titulo as tit

class testeTit(unittest.TestCase):
    """comentario"""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = tit('ricardo', 'ribeiro')
        self.assertEqual(formatted_name, 'Ricardo Ribeiro')

unittest.main()  #roda todos os testcasep