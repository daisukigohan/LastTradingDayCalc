import datetime
import jpholiday

def get_weekday():
    #日本時間での現在の日付データ取得
    #念のためUTCの時間を取得してから時差分を足してる
    jstTime = datetime.datetime.utcnow() + datetime.timedelta(hours=9)
    day = jstTime.day

    #曜日を漢字で取得したかった
    #.weekday()ではint型の数が取得でき、0が月曜日で6が日曜日なのでリストと組み合わせた
    wd = ["月","火","水","木","金","土","日"]
    weekday = wd[jstTime.weekday()]

    #1週間前の日付が同月かどうか調べる -> 1日より前か後かで判別
    #dayが1日以降(同月)なら出現回数+1してdayに1週間前の日付を代入(-7する)、1日より前(前の月の日付)なら処理終了
    weeks = 0
    while day > 0:
        weeks += 1
        day -= 7

    """
    例：今日が2017/11/13の場合、day = 13
    1ループ目・・・ day(=13) > 0 なので出現回数+1(weeks += 1)、1週間前の日付代入(day -= 7)
    2ループ目・・・ day(=6) > 0 なので出現回数+1(weeks += 1)、1週間前の日付代入(day -= 7)
    3ループ目・・・ day(=-1)は day > 0 を満たさないのでループを抜ける
    """

    print('今日は、今月の第' + str(weeks) + weekday + '曜日です。')
    #例：今日は、今月の第2月曜日です。

    return

get_weekday()