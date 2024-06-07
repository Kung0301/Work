import csv

# กำหนดชื่อไฟล์ CSV ที่ต้องการสร้าง
filename = 'example.csv'

# ข้อมูลที่ต้องการจะเขียนลงไฟล์ CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '24', 'New York'],
    ['Bob', '19', 'San Francisco'],
    ['Charlie', '35', 'Los Angeles']
]

# เปิดไฟล์ (หรือสร้างไฟล์ถ้ายังไม่มี) เพื่อเขียนข้อมูล
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

    # เขียนข้อมูลจากตัวแปร data ไปยังไฟล์ CSV
    for row in data:
        writer.writerow(row)

print(f'ไฟล์ {filename} ถูกสร้างเรียบร้อยแล้ว')