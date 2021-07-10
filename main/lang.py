import unicodedata
class LangData:
    langs ={
        '日本語':'ja' ,
        '英語':'en' ,
        '中国語(簡体)':'zh-CN' ,
        '中国語(繁体)':'zh-TW' ,
        'スペイン語':'es' ,
        'ジャワ語':'jv' ,
        'ヒンディー語':'hi' ,
        'アラビア語':'ar' ,
        'ベンガル語':'bn' ,
        'ポルトガル語':'pt' ,
        '韓国語・朝鮮語':'ko' ,
        'ロシア語':'ru' ,
        'フランス語':'fr' ,
        'ドイツ語':'de' ,
        'イタリア語':'it' 
    }
class Language:
    langs = LangData().langs
    def to_lang_code(self,source:str):
        #異常入力をキャッチする
        if source in self.langs.values():
            return source
        elif  not source in self.langs.keys():
            return '引数の言語が正しくありません。'
        return self.langs[source]
    def to_lang_name(self,source:str):
        #異常入力をキャッチする
        if source in self.langs.keys():
            return source
        if not source in self.langs.values():
            return '引数の言語が正しくありません。'
        return [k for k,v in self.langs.items() if v == source][0]
    def langstr_convert(self):
        #一番長い言語名を取得する
        max_len_langname = max(self.langs.keys(),key=len)
        #言語コードを左寄せにする
        digit = len(max_len_langname)*3
        result = '```cs\n#【言語名】'+' '*(digit-12)+'【言語コード】\n'
        for k,v in self.langs.items():
            digit = len(max_len_langname)*3
            for i in k:
                if unicodedata.east_asian_width(i) in ('F','W','A'):
                    digit -= 2
                else:digit -= 1
            k2 = k + ' ' * digit
            result += f'{k2}{v}\n'
        result += '```'
        return result