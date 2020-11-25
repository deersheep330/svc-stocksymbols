import re

def remove_common_words_from_corp_name(corp_name):
    return re.sub(r'公司|集團|企業|科技|Corp|Inc|Ltd|CORP|INC|LTD|★', '', corp_name).strip()

def remove_non_han_from_corp_name(corp_name):
    return re.sub(r'[^\u4e00-\u9fff]+', '', corp_name)
