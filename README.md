# GlobalAIProject

* CSV yazma
        import csv

        with open('names.csv', 'w', newline='') as csvfile:
            fieldnames = ['first_name', 'last_name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
            writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
            writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

* CSV okuma

        import csv

        with open('some.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)         


* Pandas ile CSV okuma

        import pandas as pd

        data = pd.read_csv("dosya.csv")


* Excel işlemleri
    
        pip install openpyxl

        from openpyxl import Workbook,load_workbook

        wb = Workbook()

        ws = wb.active
        ws.title = "İlk Çalışma Alanı"
        ws = wb.create_sheet("Posta Kodları")
        ws = wb.create_sheet("Ülkeler")
        wb.save("dosyaAdi.xlsx")


*Pandas ile csv okuyup excele çevirme işlemleri

        import pandas as pd

        read_file = pd.read_csv (r'Path where the CSV file is stored\File name.csv')
        read_file.to_excel (r'Path to store the Excel file\File name.xlsx', index = None, header=True)
