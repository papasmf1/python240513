import openpyxl
import random

# 전자제품 이름 목록
product_names = ["TV", "Refrigerator", "Washing Machine", 
    "Microwave", "Laptop", "Smartphone", "Tablet", "Camera", "Headphones", "Speaker"]

# 엑셀 워크북 생성
wb = openpyxl.Workbook()
ws = wb.active

# 헤더 추가
ws.append(["id", "name", "수량", "가격"])

# 데이터 생성 및 추가
for i in range(1, 101):
    product_id = i
    name = random.choice(product_names)
    quantity = random.randint(1, 20)
    price = random.randint(100, 2000) * 10  # 가격은 1000원에서 20000원 사이로 설정
    ws.append([product_id, name, quantity, price])

# 엑셀 파일로 저장
wb.save(r"c:\work\result.xlsx")
