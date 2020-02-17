# 渡されるパラーメーターの形式(filePatt,algorithm)
# 戻り値の形式(errorcode,hash,errormsg)
# パラメーター、戻り値はすべてstr型、パスは絶対パス、ハッシュは小文字


import hashlib


errorMsgs = {"00": "#00 Hash is calculated successfully!",
             "50": "#50 ERROR OCCURRED! There's something wrong in the selected file!"}


def calculate_hash (filePath, algorithm):

    fileError = False

    # 第2引数で指定されたアルゴリズムでハッシュオブジェクトを生成
    hashObject = hashlib.new(algorithm)

    # ブロックサイズの整数倍の長さ、ファイルが大きいときの対策
    blockLength = hashObject.block_size * 0x800


    # 第1引数で指定されたバイナリデータを開けるか検証する
    # 開けなかった場合、ファイルハッシュの計算を行わない
    try:
        with open(filePath, "rb") as f:
            pass
    except:
        errcode = "50"
        fileError = True

    if not fileError:
        with open(filePath, "rb") as f:
            currentData = f.read(blockLength)

            # データの大きさだけループ
            while currentData:
                # 播種オブジェクトに追加して計算
                hashObject.update(currentData)

                # 続きを読む
                currentData = f.read(blockLength)

        errcode = "00"
        return (errcode, str.lower(str(hashObject.hexdigest())), errorMsgs[errcode])

    return (errcode, "", errorMsgs[errcode])