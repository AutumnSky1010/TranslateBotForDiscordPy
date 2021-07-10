import requests
import json
from lang import LangData
class Translate:
    def get_result(self,sentence:str,target_language:str,source:str):
        langdata = LangData()
        #異常入力対策をする
        if sentence == '':
            return '翻訳する対象がありません。'
        elif target_language == '':
            return '翻訳後の言語が指定されていません。'
        elif source != '' and (not source in langdata.langs.values() or not target_language in langdata.langs.values()):
            return '引数の言語が正しくありません。'
        
        url = f'https://script.google.com/macros/s/AKfycbyNQblP0SZAvyVIuADvKgu5jNuXt3iPTntXt9o8u83qd6a-W0c/exec?&text={sentence}&source={source}&target={target_language}'
        jsonresult = requests.get(url).text
        result = json.loads(jsonresult)
        return result['text']