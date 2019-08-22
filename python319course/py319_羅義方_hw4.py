
zipcode = {"台北市":{"中正區": 100, "大同區": 103, "中山區": 104, "松山區": 105,
 "大安區": 106, "萬華區": 108, "信義區": 110, "士林區": 111, "北投區": 112,
  "內湖區": 114, "南港區": 115, "文山區": 116}, "基隆市":{"仁愛區": 200, "信義區": 201, "中正區": 202,
   "中山區": 203, "安樂區": 204, "暖暖區": 205, "七堵區": 206},"新北市": {"萬里區": 207, "金山區": 208, "板橋區": 220, "汐止區": 221, "深坑區": 222, "石碇區": 223, "瑞芳區": 224, "平溪區": 226, "雙溪區": 227, "貢寮區": 228, "新店區": 231, "坪林區": 232, "烏來區": 233, "永和區": 234, "中和區": 235, "土城區": 236, "三峽區": 237, "樹林區": 238, "鶯歌區": 239, "三重區": 241, "新莊區": 242, "泰山區": 243, "林口區": 244, "蘆洲區": 247, "五股區": 248, "八里區": 249, "淡水區": 251, "三芝區": 252, "石門區": 253}}
print(zipcode)

def list_zip(city):
    p=zipcode.get(city,"無此城市")
    print(p)

def area_to_zip(area):
    s1=[]
    i = 0
    for city,areas in zipcode.items():
        for areas,code in areas.items():
            s1 = s1+[(city,areas,code)]
    while i < len(s1):
        if s1[i][1]==area:
            print(s1[i][0],s1[i][2])
        i=i+1
def zip_to_area(zcode):
    s2=[]
    j = 0
    for city,areas in zipcode.items():
        for areas,code in areas.items():
            s2 = s2+[(city,areas,code)]
    while j < len(s2):
        if s2[j][2]==zcode:
            print(s2[j][0],s2[j][1])
        j=j+1

print("請選擇查詢方式")
mode=input("1-城市郵遞區號表,2-地區郵遞區號,3-郵遞區號地區")

while mode!='1' and mode!='2' and mode != '3':
    mode=input("1-城市郵遞區號表,2-地區郵遞區號,3-郵遞區號地區")
else:
    if mode=='1':
        incity=input("請輸入城市名稱")
        list_zip(incity)

    if mode=='2':
        inarea=input("請輸入地區名稱")
        area_to_zip(inarea)
    if mode=='3':
        incode=int(input("請輸入郵遞區號"))
        zip_to_area(incode)
