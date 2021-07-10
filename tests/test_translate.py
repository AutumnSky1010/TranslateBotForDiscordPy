import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent / "main"))
import unittest
from unittest.mock import Mock,patch
from main.translate import Translate
class TestTranslate(unittest.TestCase):
    #py -m unittest tests.test_translate
    @patch('requests.get')
    def test_get_result(self,mock:Mock):
        jsonresults = (
            '{"code":200,"text":"こんにちは"}',
            '{"code":200,"text":"Bonjour"}',
            '{"code":400,"text":"Bad Request"}',
            'Exception'#四番目のケース以降はAPIに全て例外を返される
        )
        tr = Translate()
        params = [
            #正常入力
            ('hello','ja','en','こんにちは'),
            ('こんにちは','fr','','Bonjour'),
            #異常入力
            ('','ja','en','翻訳する対象がありません。'),
            ('hello','','en','翻訳後の言語が指定されていません。'),
            ('hello','日本語','en','引数の言語が正しくありません。'),
            ('hello','ja','英語','引数の言語が正しくありません。'),
            ('hello','nihongo','en','引数の言語が正しくありません。'),
            ('hello','ja','eigo','引数の言語が正しくありません。')
        ]
        for i,(sentence,target_language,source,result) in enumerate(params):
            if i > 3:i=3
            mock().text = jsonresults[i]
            with self.subTest(sentence=sentence,target_language = target_language,source=source,result=result):
                actual = tr.get_result(sentence,target_language,source)
                self.assertEqual(result,actual)
