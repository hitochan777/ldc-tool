import unicodedata
# import mojimoji

# def containHankaku(s):
    # return mojimoji.zen_to_han(s) == s and mojimoji.han_to_zen(s) != s

def containChineseCharacter(s):
    for c in s:
        if unicodedata.name(c).startswith("CJK UNIFIED IDEOGRAPH"):
            return True     

    return False

