kakeibo={}
try:
  with open("/Users/chai/kakeibo_cn.txt","r",encoding="utf-8")as f:
    lines=f.readlines()
  for line in lines:
    parts=line.strip().split(",")
    kakeibo[parts[0]]=int(parts[1])
except FileNotFoundError:
  print("第一次使用，没有找到资料")
def input_number(program):
  while True:
    try:
      text=input(program)
      number=int(text)
      return number
    except:
      print("这个输入不太对哦，请再试一次（要数字哦）")
def add_item(data):
  print("您选择了添加")
  item=input("您今天买了什么：")
  money=input_number("价格：")
  data[item]=money
def get_total(data):
  return sum(data.values())
def show_items(data):
  print("您选择了显示")
  print("您今天买了：")
  if not data:
    print("目前没有任何记录哦")
  else:
    for key,value in data.items():
      print(key,value)
def delete_item(data):
  print("您选择了删除")
  delete_name=input("请输入您想删除的商品：")
  if delete_name in data:
    del data[delete_name]
    print("删除成功")
  else:
    print("没有这个商品")
def edit_item(data):
  print("您选择了修改")
  edit_name=input("请输入您想修改的商品:")
  if edit_name in data:
    money=input_number("请输入新价格：")
    data[edit_name]=money
    print("修改成功")
  else:
    print("没有这个商品")
def show_menu():
  print("=======记账本=======")
  print("1.添加")
  print("2.删除")
  print("3.显示")
  print("4.修改")
  print("5.退出")
  choice=input("请选择并输入对应数字：")
  return choice
budget=input_number("请输入您的今日预算：")
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
  elif choice=="5":
    break
with open("/Users/chai/kakeibo_cn.txt","w",encoding="utf-8")as f:
  for key in kakeibo:
    f.write(f"{key},{kakeibo[key]}\n")
print("您今天买了：")
for key,value in kakeibo.items():
  print(key,value)
print("共计：",get_total(kakeibo),"元")
total=get_total(kakeibo)
if total>budget:
  print("超预算了！！！")
elif total<budget:
  remaining=budget-total
  print("真棒您今天节省了：",remaining,"元")
else:
  print("预算控制得非常精准！")
print("感谢您的使用！祝您有美好的一天")