import sqlite3 



conn = sqlite3.connect('repices.db')
cur= conn.cursor()


#tablo oluşturma

cur.execute("""CREATE TABLE IF NOT EXISTS yemek_listesi(
            isim TEXT NOT NULL,
            tarif TEXT NOT NULL

            )
            """)

Yemek_listesi=[
    ("Menemen", "Tam kıvamında bir menemen yapmak için önce biberleri yağda kavurup ardından domatesleri suyunu çekene kadar pişirmeniz ve en son yumurtaları ekleyerek hafif sulu kalacak şekilde karıştırmanız gerekir. Hazırlaması ortalama 10 dakika süren bu klasik lezzet, 15 dakika içinde servise hazır hale gelir.",),

    ("Döner", "Evde döner yapmak için en pratik ve lezzetli yöntem, marine edilmiş eti veya baharatlı kıymayı rulo şeklinde dondurup ince yapraklar halinde keserek tavada pişirmektir. Dışarıda yediğiniz döner kıvamını yakalamak için etin dondurulup donukken kesilmesi en kritik püf noktasıdır.",),   

    ("Mantı", "Ev yapımı klasik mantı, sert kıvamlı bir hamurun açılıp kıymalı iç harçla bohça şeklinde kapatılması ve kaynar suda haşlanmasıyla yapılır.",),
]

cur.executemany("INSERT INTO yemek_listesi VALUES (?, ?)", Yemek_listesi)
conn.commit()


cur.execute("DELETE FROM yemek_listesi  WHERE isim='Mantı'")
conn.commit()

cur.execute("UPDATE yemek_listesi SET tarif='Tam kıvamında bir menemen yapmak için önce biberleri yağda kavurup ardından domatesleri suyunu çekene kadar pişirmeniz ve en son yumurtaları ekleyerek hafif sulu kalacak şekilde karıştırmanız gerekir. Hazırlaması ortalama 10 dakika süren bu klasik lezzet, 15 dakika içinde servise hazır hale gelir,isterseniz Menemenin içine sucuk ekleyerek farklı bir lezzet elde edebilirsiniz. Sucukları dilimleyip menemenin içine ekleyip pişirmeniz yeterlidir.' WHERE isim='Menemen'")

conn.commit()