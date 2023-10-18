with open("input.txt", encoding="utf-8") as file:
    text=file.read()
    alf="АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    decodtexts=dict()
    for i in range(33):
        decodtext=''
        chasdecodtext=dict()
        for j in range(len(text)):
            bukva=text[j]
            if bukva in alf:
                ind=alf.find(bukva)
                bukva=alf[(ind+i)%33]
            decodtext+=bukva
        decodtexts[i] = decodtext
        #print(decodtext)
    Chas={'А':7.96, 'Б':1.67, 'В':4.71, 'Г':1.87, 'Д':3.07, 'Е':8.90, 'Ё':0.11, 'Ж':1.18, 'З':1.74, 'И':6.38, 'Й':0.98,'К':3.25,
         'Л':4.64, 'М':3.13, 'Н':6.70, 'О':11.26, 'П':2.71,'Р':3.90, 'С':5.32, 'Т':6.31, 'У':2.63, 'Ф':0.18, 'Х':0.73, 'Ц':0.29,
        'Ч':1.91, 'Ш':0.82, 'Щ':0.29, 'Ъ':0.03,'Ы':1.73,'Ь':2.25,'Э':0.36,'Ю':0.60,'Я':2.39}
    ans=dict()
    for i in range(len(decodtexts)):
        ch=dict()
        text=decodtexts[i]
        l=len(set(text))
        for j in range(len(text)):
            a=text[j]
            if a in alf:
                ch[a]=(ch.setdefault(a,0)*l+1)/l
        X=0
        for j in range(len(text)):
            a=text[j]
            if a in alf:
                X=X+ch[a]*Chas[a]
        ans[X]=text
    print(ans[max(ans)])