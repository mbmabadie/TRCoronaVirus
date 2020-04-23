import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['İstanbul', 'İzmir ', 'Ankara ', 'Konya', 'Kocaeli','Sakarya', 'Isparta','Bursa','Adana', 'Zonguldak',
'Samsun', 'Kayseri','Tekirdağ ', 'Eskişehir', 'Balıkesir', 'Antalya', 'Rize','Manisa ', 'Edirne', 'Tokat',
'Ordu', 'Trabzon','Denizli ', 'Şırnak', 'Erzurum', 'Giresun', 'Malatya','Yalova ', 'Mardin', 'Gaziantep',
'Kırklareli', 'Osmaniye ','Diyarbakır ', 'Muğla', 'Siirt', 'Uşak', 'Amasya','Sinop ', 'Çorum', 'Adıyaman',
'Düzce', 'Hatay','Ağrı ', 'Çanakkale', 'Kahramanmaraş', 'Nevşehir', 'Iğdır','Kastamonu ', 'Çankırı', 'Van',
'Bayburt', 'Kırıkkale','Bitlis ', 'Artvin', 'Aydın', 'Karabük', 'Bolu','Afyonkarahisar ', 'Kars', 'Şanlıurfa',
'Kilis', 'Mersin','Bilecik ', 'Erzincan', 'Yozgat', 'Karaman', 'Muş','Elazığ ', 'Gümüşhane', 'Niğde',
'Bingöl', 'Bartın','Batman ', 'Sivas', 'Kırşehir', 'Tunceli', 'Aksaray','Ardahan ', 'Kütahya', 'Burdur',
'Hakkari']

Vaka_sayisi = [1223.1 ,110.5 ,86.0 ,60.1 ,50.0 ,33.7 ,28.9 ,25.9 ,24.1 ,19.7 ,
16.7 ,13.0 ,12.1 ,11.8 ,10.6 ,10.2 ,10.1 ,10.0 ,9.1 ,9.0 ,
8.8 ,8.7 ,8.6 ,8.0 ,7.8 ,7.3 ,6.6 ,6.4 ,5.1 ,4.9 ,
4.9 ,4.7 ,4.6 ,4.6 ,4.4 ,4.0 ,3.8 ,3.5 ,3.5 ,3.2 ,
3.2 ,3.2 ,3.1 ,3.0 ,2.8 ,2.7 ,2.6 ,2.6 ,2.5 ,2.4 ,
2.3 ,2.3 ,2.2 ,2.0 ,2.0 ,2.0 ,1.9 ,1.8 ,1.8 ,1.8 ,
1.7 ,1.7 ,1.6 ,1.5 ,1.5 ,1.4 ,1.4 ,1.2 ,1.2 ,1.2 ,
1.0 ,.9 ,.9 ,.9 ,.7 ,.6 ,.5 ,.5 ,.5 ,.3 ,
.2 ]

Vefat_sayisi = [117 ,18 ,7 ,7 ,8 ,3 ,1 ,2 ,3 ,5 ,
1 ,1 ,0 ,1 ,5 ,2 ,3 ,1 ,2 ,3 ,
0 ,5 ,2 ,1 ,0 ,1 ,1 ,0 ,0 ,1 ,
0 ,1 ,2 ,1 ,0 ,1 ,1 ,1 ,1 ,0,
0 ,0 ,0 ,2 ,1 ,0 ,0 ,0 ,0 ,0 ,
0 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,
0 ,0 ,0 ,1 ,2 ,0 ,0 ,1 ,0 ,0 ,
0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0,
0 ]

x = np.arange(len(labels))  # the label locations
width = 0.35               # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, Vaka_sayisi, width, label='Vaka (in tens)')
rects2 = ax.bar(x + width/2, Vefat_sayisi, width, label='Vefat (Normal)')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Türkiye Koronavirüs')
ax.set_title('Türkiye Koronavirüs (illere göre Vaka - Vefat sayıları)')
ax.set_xticks(x)
plt.xticks(rotation=90)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()