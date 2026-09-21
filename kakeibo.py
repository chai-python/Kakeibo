from datetime import date
kakeibo=[]
try:
    with open("kakeibo_jp.txt","r",encoding="utf-8")as f:
        lines=f.readlines()
    for line in lines:
        parts=line.strip().split(",")
        if len(parts)==2:
            record={
                "date":"不明",
                "item":parts[0],
                "money":int(parts[1])
            }
            kakeibo.append(record)
        elif len(parts)==3:
            record={
                "date":parts[0],
                "item":parts[1],
                "money":int(parts[2])
            }
            kakeibo.append(record)
except FileNotFoundError:        
    print("初めての利用のため、データが見つかりません")
def input_number(program):
    while True:
        try:
            text=input(program)
            number=int(text)
            return number
        except:
            print("入力が正しくないようです。数字でもう一度入力してください。")
def add_item(data):
    print("「追加」を選択しました")
    today=date.today()
    item=input("今日は何を買ったの？：")
    money=input_number("価格：")
    record={
        "date":today,
        "item":item,
        "money":money
    }
    data.append(record)
def get_total(data):
    return sum(record["money"] for record in data)
def show_items(data):
    print("「購入履歴」を選択しました")
    print("今日購入したもの:")
    if not data:
        print("まだデータがありません")
    else:
        for record in data:
            print(record["date"],record["item"],record["money"])
def delete_item(data):
    print("「削除」を選択しました")
    delete_name=input("削除したい商品を入力してください：")
    for i,record in enumerate(data):
        if record["item"]==delete_name:
            del data[i]
            print("商品を削除します")
            return
    print("その商品は見つかりませんでした")
def edit_item(data):
    print("「変更」を選択しました")
    edit_name=input("変更したい商品名を入力してください：")
    for record in data:
        if record["item"]==edit_name:
            record["money"]=input_number("新しい価格を入力してください：")
            print("商品を変更しました")
            return
    print("その商品は見つかりませんでした")
def search_item(data):
    print("「検索」を選択しました")
    search_name=input("検索したい商品名を入力してください：")
    found=False
    for record in data:
        if record["item"]==search_name:
            print(record["date"],record["item"],record["money"])
            found=True
    if found==False:
        print("その商品は見つかりませんでした")
def show_statistics(data):
    print("「今日の統計」を選択しました")
    today=date.today()
    total=0
    count=0
    for record in data:
        if record["date"]==today:
            total=total+record["money"]
            count=count+1
    return total,count
def show_menu():
    print("=======家計簿=======")
    print("1.追加")
    print("2.削除")
    print("3.購入履歴")
    print("4.変更")
    print("5.終了")
    print("6.検索")
    print("7.今日の統計")
    choice=input("番号を入力してください：")
    return choice
budget=input_number("今日の予算を入力してください：")
while True:
    choice=show_menu()
    if choice=="1":
        add_item(kakeibo)
    elif choice=="3":
         show_items(kakeibo)
    elif choice=="2":
        delete_item(kakeibo)
    elif choice=="4":
        edit_item(kakeibo)
    elif choice=="6":
        search_item(kakeibo)
    elif choice=="7":
        total,count=show_statistics(kakeibo)
        print("今日の購入件数：", count, "件")
        print("今日の支出合計：", total, "円")
    elif choice=="5":
        break
with open("kakeibo_jp.txt","w",encoding="utf-8")as f:
    for record in kakeibo:
        f.write(f'{record["date"]},{record["item"]},{record["money"]}\n')
print("今日購入したもの:")
for record in kakeibo:
    print(record["date"],record["item"],record["money"])
print("合計:",get_total(kakeibo),"円")
total=get_total(kakeibo)
if total>budget:
    print("予算オーバー")
elif total<budget:
    remaining=budget-total
    print("素晴らしい！今日は",remaining,"円節約できましたね！")
else:
    print("予算どおりに使えました！")
print("ご利用いただきありがとうございます！素敵な一日をお過ごしください！")