import random #randomは擬似乱数の生成

player, computer = '',''
coordinate=[i for i in range(9)]  #以下必要な座標の定義
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) #勝利のパターン
tab=range(1,10)
        
def answear_method():
    ox =('O','X')
    if random.randint(0,1) == 0: #ランダムな整数を返す(返される変数nは0<=n<=1となる)
        return ox[::-1]       #O,X
    return ox

def table(): #〇✖ゲームのテーブル(3×3)
    print( coordinate[0], "|", coordinate[1], "|", coordinate[2])
    print("---------")
    print( coordinate[3], "|", coordinate[4], "|", coordinate[5])
    print("---------")
    print( coordinate[6], "|", coordinate[7], "|", coordinate[8])

#def 
"""
間違いがあった箇所
"""


def game_method():
    return coordinate.count('X') + coordinate.count('O') != 9

def main():
    player, computer = answear_method()
    welcome = """
    ゲームを開始します。このゲームは２人でプレイしてください
    1Pと2Pを決めてください。
    """
    print(welcome)
    print('1Pが「%s」 で、2Pは「%s」です' % (player, computer))
    print("1Pが先攻です")
    while game_method():
        table()
        print('１～９の座標を入力してください : ')
        move = int(input())
        
        if not #間違いがあった箇所
            print('!エラー!：空いている１～９の座標を入力してください')
            continue
        if won:
            result='あなたの勝ちです'
            break
        elif :
            result='あなたの負けです'
            break;
    table()
    print('%% ゲーム終了です %%')

if __name__ == "__main__":
    main()