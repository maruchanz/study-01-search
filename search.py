### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    source=[]
    ### ここに検索ロジックを書く
    with open("kimetsu.csv", encoding = "utf-8") as f:
        for s in f.readlines():
            source.append(s.rstrip())
        print(source)
    f.close()


    if word in source:    
        print("{}が見つかりした".format(word))
        
    else:
        print("{}が見つかりませんでした".format(word))
        source.append(word)
        with open("kimetsu.csv","a",encoding = "utf-8") as f:
            f.write(word)


        
if __name__ == "__main__":
    search()