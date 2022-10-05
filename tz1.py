class Contact:
    def __init__(self,last_name,first_name,middle_name,number,email):
        self.first_name=first_name
        self.last_name=last_name
        self.middle_name=middle_name
        self.number=number
        self.email=email
    def inf(self):
        return f'{self.last_name} {self.first_name} {self.middle_name} {self.number} {self.email}'
def find(*data):
    for i in range(len(ar)):
        global id
        k=0
        for x in data:
            if len(data)==1:
                if x in ar[i].inf().split():
                    print(ar[i].inf())
                    id =i
            if len(data)==2:
                if x in ar[i].inf().split():
                    k+=1
                    if k==2:
                        print(ar[i].inf())
                        id =i
            if len(data)==3:
                if x in ar[i].inf().split():
                    k+=1
                    if k==3:
                        print(ar[i].inf())
                        id =i
            if len(data)==4:
                if x in ar[i].inf().split():
                    k+=1
                    if k==4:
                        print(ar[i].inf())
                        id =i
            if len(data)==5:
                if x in ar[i].inf().split():
                    k+=1
                    if k==5:
                        print(ar[i].inf())
                        id =i
ar=[]
while True:
    Op=int(input('Варианты действий:\n 1-Добавить файл контактов \n 2-Закончить програму \n 3-Найти нужней вам контакт(По одному из его элементоа) \n 4-Изменить один из элементов контакта \n '))
    if Op==1:
        g=input('Введите название файла: ')
        with open(g, encoding='utf-8') as f:
            for line in f:
                p=str(line)
                t=p.replace(',', "")
                r=t.split()
                print(r)
                k=0
                fn='-'
                mn='-'
                nb='-'
                em='-'
                for i in r:
                    if k==4:
                        em=r[4]
                    elif k==3:
                        if '+' in i:
                            nb=r[3]
                        elif '@' in i:
                            em=r[3]
                    elif k==2:
                        if '+' in i:
                            nb=r[2]
                        elif '@' in i:
                            em=r[2]
                        else:
                            mn=r[2]
                    elif k==1:
                        if '+' in i:
                            nb=r[1]
                        elif '@' in i:
                            em=r[1]
                        else:
                            fn=r[1]
                    else:
                        ln=r[0]
                    k+=1
                c=Contact(ln,fn,mn,nb,em)
                ar.append(c)
        print('Файл загружен')
        continue

    elif Op==2:
        break
    elif Op==3 or Op==4:
        s=input('Введите элемент контакта (Если нужны контакты, в которых не хватает данных введите "-"): \n')
        sr=s.split()
        if len(sr)==1:
            res=find(sr[0])
        if len(sr)==2:
            res=find(sr[0],sr[1])
        if len(sr)==3:
            res=find(sr[0],sr[1],sr[2])
        if len(sr)==4:
            res=find(sr[0],sr[1],sr[2],sr[3])
        if len(sr)==5:
            res=find(sr[0],sr[1],sr[2],sr[3],sr[4])
        if Op==4:
            v=int(input('Что хотите изменить:\n 1-Фамилию\n 2-Имя\n 3-Отчество\n 4-Номер\n 5-Почту\n '))
            if v==1:
                ar[id].last_name=input('Введите фамилию накоторую хотите поменять: ')
            elif v==2:
                ar[id].first_name=input("Введите имя на которое хотите поменять: ")
            elif v==3:
                ar[id].middle_name=input("Введите отчество на которое хотите поменять: ")
            elif v==4:
                ar[id].number=input("Введите номер на который хотите поменять: ")
            elif v==5:
                ar[id].email=input("Введите почту на которую хотите поменять: ")


