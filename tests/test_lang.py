import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / "main"))
import unittest
from unittest.mock import Mock,patch
from main.lang import Language
#py -m unittest tests.test_lang
class TestLanguage(unittest.TestCase):
    lang = Language()
    abnormal_params = [
        #異常系
        ('nihongo','引数の言語が正しくありません。'),
        ('jp','引数の言語が正しくありません。'),
        ('English','引数の言語が正しくありません。')
    ]
    def test_to_lang_name(self):
        params = [
            ('ja','日本語'),
            ('en','英語'),
            #異常系
            ('日本語','日本語')
        ]
        params += self.abnormal_params
        self.run_subtest(params,'to_lang_name')
    def test_to_lang_code(self):
        params = [
            ('日本語','ja'),
            ('英語','en'),
            #異常系
            ('ja','ja')
        ]
        params += self.abnormal_params
        self.run_subtest(params,'to_lang_code')
    def run_subtest(self,params,method_name):
        for source,result in params:
            with self.subTest(source = source, result = result):
                actual = ''
                if method_name == 'to_lang_name':
                    actual = self.lang.to_lang_name(source)
                elif method_name == 'to_lang_code':
                    actual = self.lang.to_lang_code(source)
                print(actual)
                self.assertEqual(actual,result)