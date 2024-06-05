import time 
import sys 
import os 

def load_animation(): 
  
    load_str = "loading ip-tracker by linuxuser-azad..."
    ls_len = len(load_str) 
  

    animation = "|/-\\"
    anicount = 0
 
    counttime = 0        
      
    i = 0                     
  
    while (counttime != 30): 
 
        time.sleep(0.075)  

        load_str_list = list(load_str)  
          
        x = ord(load_str_list[i]) 
          
        y = 0                             
  
        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
           
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
               
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
   
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
     
    if os.name =="nt": 
        os.system("cls") 
          
    
    else: 
        os.system("clear") 
  

if __name__ == '__main__':  
    load_animation() 

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 


banner = r'''                                                                                          
                                .-.
                   v 1.0       /aa \_
    accurate                 __\-  / )                 .-.
                   .-.      (__/    /   ip-tracker   _/oo \
                 _/ ..\       /     \               ( \v  /__
                ( \  u/__    /       \__             \/   ___)
                 \    \__)   \_.-._._   )  .-.       /     \
                 /     \             `-`  / ee\_    /       \_
              __/       \               __\  o/ )   \_.-.__   )
             (   _._.-._/ thelinux     (___   \/           '-'
   superfast '-'           user-        /     \
                           azad       _/       \    
                                      (   __.-._/     
                                       '-'          
'''



prCyan(banner)

from time import sleep
import sys
print("█████████████████████████████████████")
line_1 = "███  ip-tracker by mahyar azad   ████ "
for x in line_1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.1)

print("\n█████████████████████████████████████")
import sys
import os
WARNING = '\033[93m' 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 



prGreen("⮩ SELECT NO 1 TO GET DETAILS ABOUT YOUR IP  ")
prGreen("⮩ SELECT NO 2 TO TRACK AND GET DETAILS ABOUT IP  ")
prGreen("⮩ SELECT NO 3 TO OBTAINING THE IP OF THE WEBSITE  ")
prGreen("  SELECT ANY KEY TO EXIT THE SCRIPT:  ")
option = input(''' ┌─[ ip-tracker@azad ]─[~]
 └──╼ # ''')



while True:
  if option == "1":

      from requests import get
      myip = get('https://ipapi.co/json/')
      prYellow(myip.json())
      import sys
      sys.exit()
      
                
  elif option == "2" :
      from requests import get
      ip = input("enter your ip here:")
      track = get(f'https://ipapi.co/{ip}/json/')
      prYellow(track.json())
      import sys
      sys.exit()


  elif option== "3":
    print("YOU")
  

  else:
      prRed("closing....")
      prRed("thank you!")
      prRed("also make sure to add a star")
      import sys
      sys.exit()
      