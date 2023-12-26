import sys
import sqlite3 as sq 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout , QLineEdit,QRadioButton
import time
from base1 import base1
sotryd=25
gosti=5




local = time.ctime(time.time())

with sq.connect("base.db") as base:
            
            cur = base.cursor()
            cur.execute('DROP TABLE IF EXISTS rabotniki')
            cur.execute("""CREATE TABLE IF NOT EXISTS rabotniki(
                        famil TEXT,
                        name TEXT,
                        otch TEXT,
                        date TEXT,
                        dol TEXT,
                        nomer TEXT,
                        pochta TEXT,
                        time_ek TEXT ,
                        time_ex TEXT 
                        );
                        """)
            cur.executemany("INSERT INTO rabotniki VALUES(?, ? , ?, ?, ? , ?, ? , ?,?)",base1)
            base.commit()
with sq.connect("gosti.db") as base2:
            
            cur2 = base2.cursor()
            cur2.execute('DROP TABLE IF EXISTS gosti')
            cur2.execute("""CREATE TABLE IF NOT EXISTS gosti(
                        famil TEXT,
                        name TEXT,
                        otch TEXT,
                        date TEXT,
                        cel TEXT,
                        nomer TEXT,
                        pochta TEXT,
                        time_ek INT ,
                        time_ex INT 
                        );
                        """)
            base2.commit()


class PassControlApp(QWidget):
    def __init__(self):
        super().__init__()
        global cur
        global base
        global sotryd
        global gosti
        self.cur = 0
        self.car = 0

        
        
        self.RadioButton=QRadioButton("Наличие машины")

        self.issue_pass_button2 = QPushButton('Добавить временный пропуск')
        self.issue_pass_button = QPushButton('Вход')
        self.issue_pass_button3 = QPushButton('Выход')
      
        self.issue_pass_button.clicked.connect(self.eks)
        self.issue_pass_button3.clicked.connect(self.exit)
        self.issue_pass_button2.clicked.connect(self.vremPROP)
        
        self.RadioButton.toggled.connect(self.update)


        self.name = QLineEdit(self,placeholderText="Введите почту сотрудника...")
        
        self.passv = QLineEdit(self,placeholderText="Введите имя...")

        self.fam = QLineEdit(self,placeholderText="Введите фамилию...")

        self.fath = QLineEdit(self,placeholderText="Введите отчество...")

        self.num = QLineEdit(self,placeholderText="Введите номер телефона...")

        

        layout = QVBoxLayout()
    

        
        layout.addWidget(self.name)
        layout.addWidget(self.passv)
        layout.addWidget(self.fam)
        layout.addWidget(self.fath)
        layout.addWidget(self.num)
        layout.addWidget(self.RadioButton)
        layout.addWidget(self.issue_pass_button2)
        layout.addWidget(self.issue_pass_button)
        layout.addWidget(self.issue_pass_button3)
        

        self.setLayout(layout)
        self.setWindowTitle('Пропускной пункт')
        
    
    
    def vremPROP(self):
        pass1.show()
        
    

    def eks(self):
       global gosti
       global sotryd
       self.dog=self.name.text().find("@")
       self.poch = self.name.text()
       
       
       self.local_time = time.ctime(time.time())
       if self.car == 1 :
            if sotryd!=0:
              if sotryd<5 and gosti>0:
                   sotryd=sotryd-1
                   gosti=gosti-1
              else:
                   sotryd=sotryd-1
              cur.execute(f"""UPDATE rabotniki SET time_ek = ? where pochta=?""",[self.local_time,self.poch])
              
              cur.execute('SELECT pochta FROM rabotniki')
              self.rows = cur.fetchall()
              if self.rows.count((self.name.text(),)) :
                  print("Сотрудник",self.poch,"Вошёл")
              else:
                    print("Такой почты нет в базе данных")
              base.commit()
              
            else:
              print("Извините мест нет")
       elif self.car == 0 :
            
          cur.execute(f"""UPDATE rabotniki SET time_ek = ? where pochta=?""",[self.local_time,self.poch])
          base.commit()
          cur.execute('SELECT pochta FROM rabotniki')
          self.rows = cur.fetchall()
          if self.rows.count((self.name.text(),)) :
                  print("Сотрудник",self.poch,"Вошёл")
          else:
               print("Такой почты нет в базе данных")
          

       
       

    def exit(self):
       global gosti
       global sotryd
       self.poch = self.name.text()
       if self.car == 1:
            if sotryd<5 and gosti<5 :
                   sotryd=sotryd+1
                   gosti=gosti+1
            sotryd=sotryd+1
            
       
       self.local_time = time.ctime(time.time())
       cur.execute(f"""UPDATE rabotniki SET time_ex = ? where pochta=? AND time_ek!='NULL' """,[self.local_time,self.poch])

       cur.execute('SELECT pochta FROM rabotniki')
       self.rows = cur.fetchall()
       if self.rows.count((self.name.text(),)) :
                  print("Сотрудник",self.poch,"Вышел")
       else:
                    print("Такой почты нет в базе данных")
       base.commit()




       base.commit()

    def update(self):
         if self.car == 0:
              self.car = 1
         else:
              self.car = 0

         print(self.car)













class App(QWidget):
    def __init__(self):

        super().__init__()
        self.car = 0
        global cur2
        global base2
        global sotryd
        global gosti
        
        self.pass_label = QLabel('Пропускные документы: 0')

        self.issue_pass_button2 = QPushButton('Выдать пропуск на выход')
        self.issue_pass_button = QPushButton('Выдать пропуск')
        self.RadioButton=QRadioButton("Наличие машины")


        self.issue_pass_button.clicked.connect(self.issue_pass)
        self.issue_pass_button2.clicked.connect(self.vremPROP)
        self.RadioButton.toggled.connect(self.update)
        
      
        self.exit= QLineEdit(self,placeholderText="Введите контактную почту для выхода...")
        

        self.famil= QLineEdit(self,placeholderText="Введите фамилию ...")
        self.name= QLineEdit(self,placeholderText="Введите имя...")
        self.otch = QLineEdit(self,placeholderText="Введите отчество...")
        self.date= QLineEdit(self,placeholderText="Введите дату рождения...")
        self.cel= QLineEdit(self,placeholderText="Введите цель визита...")
        self.nomer = QLineEdit(self,placeholderText="Введите номер телефона...")
        self.pochta = QLineEdit(self,placeholderText="Введите контактную почту...")

        layout = QVBoxLayout()

        layout.addWidget(self.pass_label)


        layout.addWidget(self.famil)
        layout.addWidget(self.name)
        layout.addWidget(self.otch)
        layout.addWidget(self.date)
        layout.addWidget(self.cel)
        layout.addWidget(self.nomer)
        layout.addWidget(self.pochta)
        

        layout.addWidget(self.RadioButton)
        layout.addWidget(self.issue_pass_button)
        layout.addWidget(self.exit)
        layout.addWidget(self.issue_pass_button2)

        self.setLayout(layout)
        self.setWindowTitle('Пропускной пункт для гостей')
    def update(self):
         if self.car == 0:
              self.car = 1
         else:
              self.car = 0
         
         if gosti ==0:
                print("Парковочных мест нет! Приезжайте позже!")    
    
    def vremPROP(self):
       global gosti
       global sotryd
       if self.car == 1:
            sotryd=sotryd+1
            gosti=gosti+1
       self.exi = self.exit.text()
       self.time = time.time() 
      
       self.local_time = time.ctime(time.time())
       cur2.execute(f"""UPDATE gosti SET time_ex = ? where pochta=? """,[self.time,self.exi])
       cur2.execute('SELECT pochta FROM gosti')
       self.rows = cur2.fetchall()
       if self.rows.count((self.exit.text(),)) :
               print("Гость",self.exi,"Вышел")
               cur2.execute('SELECT time_ek,time_ex FROM gosti WHERE pochta=?',self.pochtat)
               self.rows2 = cur2.fetchall()
               self.tkk = self.rows2[0]
               self.tk,self.tx = self.tkk
               
               if self.tx-self.tk>10:
                     print(f"Гость {self.exi} - привысил время посещения на {(self.tx)-(self.tk)-10} сек, 'ОБРАТИТЕСЬ К НАЧАЛЬНИКУ ОХРАНЫ'")
               if self.tx-self.tk<10:
                     print(f"Гость {self.exi} пробыл внутри {(self.tx)-(self.tk)} сек")
       else:
               print("Такой почты нет в базе данных")
       
       
    
  
    def issue_pass(self):
        global gosti
        global sotryd
        if self.car == 1:
             if gosti ==0:
                  print("Парковочных мест нет! Приезжайте позже!")
             else:
                    sotryd=sotryd-1
                    gosti=gosti-1
                    self.time = time.time() 
                    self.familt=self.famil.text()
                    self.namet=self.name.text()
                    self.otcht=self.otch.text()
                    self.datet=self.date.text()
                    self.celt=self.cel.text()
                    self.nomert=self.nomer.text()
                    self.pochtat=self.pochta.text()
                    self.CORT=[(self.familt,self.namet,self.otcht,self.datet,self.celt,self.nomert,self.pochtat,self.time,"NULL")]
                    
                    cur2.execute('SELECT pochta FROM gosti')
                    self.rows = cur2.fetchall()
                    if self.rows.count((self.pochta.text(),)) :
                            print("Такая почта уже есть")
                    else:
                            print("Гость",self.pochtat,"Вошёл")
                            cur2.executemany("INSERT INTO gosti VALUES(?, ? , ?, ?, ? , ?, ? , ?,?)",self.CORT)
                            base2.commit()
                    


        else:
                    self.time = time.time() 
                    self.familt=self.famil.text()
                    self.namet=self.name.text()
                    self.otcht=self.otch.text()
                    self.datet=self.date.text()
                    self.celt=self.cel.text()
                    self.nomert=self.nomer.text()
                    self.pochtat=self.pochta.text()
                    self.CORT=[(self.familt,self.namet,self.otcht,self.datet,self.celt,self.nomert,self.pochtat,self.time,0)]
                    cur2.execute('SELECT pochta FROM gosti')
                    self.rows = cur2.fetchall()
                    if self.rows.count((self.pochta.text(),)) :
                            print("Такая почта уже есть")
                    else:
                            print("Гость",self.pochtat,"Вошёл")

                            cur2.executemany("INSERT INTO gosti VALUES(?, ? , ?, ?, ? , ?, ? , ?,?)",self.CORT)
                            base2.commit()
                    cur2.execute('SELECT time_ek,time_ex FROM gosti WHERE pochta=?',self.pochtat)
                    self.rows2 = cur2.fetchall()
                    self.tkk = self.rows2[0]
                    self.tk = self.tkk
                    

                    
                   







if __name__ == '__main__':
    app = QApplication(sys.argv)
    pass_control = PassControlApp()
    pass1 = App()
    pass_control.show()
    sys.exit(app.exec())