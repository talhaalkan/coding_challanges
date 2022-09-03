s = "((({{{}}}[][])))"
def isValid(s) :
    while "()" in s or "[]" in s or "{}" in s :  # bunlardan herhangi biri olduğu sürece döngü devam eder.
        s = s.replace("()", "").replace("[]", "").replace("{}", "") #döngü devam eder, bulduklarını siler. parantez yoksa silmez
                 # silecek uygun parantez bulamazsa aynısını döndürür. Üstte stringimizi kendisine eşitlemiş olduk.                                                
    return s == ""  # str boş ise true döndür, boş str değilse false döndür.
isValid(s)