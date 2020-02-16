# 戻り値の形式(errorcode <str>,hash <str,すべて小文字>,checker <bool>,errormsg)
# 渡されるパラーメーターの形式(filePath <str, 絶対パスで指定>,currentHash <str>,algorithm <int>)

# errorcode一覧
errorMsgs = {"00": "#00 正常終了(ハッシュ合致)",
             "01": "#01 正常終了(ハッシュ不合致)",
             "50": "#50 エラー(typeが不正)",
             "51": "#51 エラー(hashが不正)",
             "52": "#52 エラー(ファイルが存在しません)"}

def mainCalc(filePath, currentHash, algorithm):
    import hashlib
    algorithmNames = ["md5", "sha256", "sha512"]
    selectedAlgorithm = algorithmNames[int(algorithm)]
    # ハッシュアルゴリズムを決めます
    algo = selectedAlgorithm

    # ハッシュオブジェクトを作ります
    h = hashlib.new(algo)

    # 分割する長さをブロックサイズの整数倍に決めます
    Length = hashlib.new(algo).block_size * 0x800

    # 大きなバイナリデータを用意します
    with open(filePath, 'rb') as f:
        BinaryData = f.read(Length)

        # データがなくなるまでループします
        while BinaryData:
            # ハッシュオブジェクトに追加して計算します。
            h.update(BinaryData)

            # データの続きを読み込む
            BinaryData = f.read(Length)

        calculatedHash = str(h.hexdigest())

    if str.upper(calculatedHash) == str.upper(currentHash):
        errorcode = "00"
        checker = True
    else:
        errorcode = "01"
        checker = False

    print(errorcode)
    print(calculatedHash)
    print(checker)
    print(errorMsgs[errorcode])

    return errorcode, calculatedHash, checker, errorMsgs[errorcode]
