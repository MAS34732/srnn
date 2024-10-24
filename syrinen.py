import random
from time import sleep

je_taime_langues = [
    "Je t'aime", "I love you", "Te quiero", "Ti amo", "Ich liebe dich", 
    "Eu te amo", "Te iubesc", "Я тебя люблю", "Seni seviyorum", "愛してる",
    "사랑해", "Te volim", "Ég elska þig", "Ik hou van jou", "Volim te", 
    "Nakupenda", "Saya cinta padamu", "Kocham cię", "Aš tave myliu",
    "Mahal kita", "Jeg elsker deg", "Minä rakastan sinua", "Te dua", "Εγώ σε αγαπώ",
    "Kuv hlub koj", "Je t'aime beaucoup", "T'estimo", "O iubesc", "Ti voglio bene",
    "Es gribētu tevi", "Kimi o aishiteru", "Jeg elskar deg", "Jetaime", 
    "Mi amas vin", "Aloha wau ia’oe", "Main tumhe pyar karti hoon", "Ani ohevet otach",
    "Amo-te", "Ek het jou lief", "Ich lieb' dich", "Szeretlek", "Volim te",
    "Me t’aime", "Mina rakastan sinua", "Ik hou van jou"
]

compliments = [
    "mon amour éternel", "ma princesse", "ma reine", "mon cœur", "mon trésor", 
    "mon ange", "ma beauté", "ma perle rare", "ma vie", "ma lumière", 
    "mon étoile", "ma douce", "ma merveille", "mon souffle", "mon bonheur", 
    "ma lune", "mon soleil", "ma raison de vivre", "ma chérie", "ma douce moitié",
    "ma muse", "mon univers", "ma raison d'être", "mon bijou", "ma passion",
    "ma tendresse", "mon éclat", "mon joyau", "ma fleur", "mon trésor caché",
    "mon paradis", "ma déesse", "mon rêve", "mon petit ange", "mon rayon de soleil",
    "ma princesse de rêve", "mon trésor infini", "ma perle précieuse", "mon unique",
    "ma chérie d'amour", "ma belle étoile", "mon doux trésor", "mon idylle", 
    "ma rose", "ma sirène", "mon étoile filante", "ma tendre moitié", 
    "ma petite fée", "ma sirène des mers", "mon arc-en-ciel", "ma lune d'argent", 
    "mon élue", "ma lumière divine", "mon âme sœur", "mon éclat de bonheur", "ma syrine"
]

acssi_syrine1 = r"""
   ,-,--.                           .=-.-..-._           ,----.  
 ,-.'-  _\ ,--.-.  .-,--.-.,.---.  /==/_ /==/ \  .-._ ,-.--` , \ 
/==/_ ,_.'/==/- / /=/_ /==/  `   \|==|, ||==|, \/ /, /==|-  _.-` 
\==\  \   \==\, \/=/. /==|-, .=., |==|  ||==|-  \|  ||==|   `.-. 
 \==\ -\   \==\  \/ -/|==|   '='  /==|- ||==| ,  | -/==/_ ,    / 
 _\==\ ,\   |==|  ,_/ |==|- ,   .'|==| ,||==| -   _ |==|    .-'  
/==/\/ _ |  \==\-, /  |==|_  . ,'.|==|- ||==|  /\ , |==|_  ,`-._ 
\==\ - , /  /==/._/   /==/  /\ ,  )==/. //==/, | |- /==/ ,     / 
 `--`---'   `--`-`    `--`-`--`--'`--`-` `--`./  `--`--`-----``  

"""
acssi_syrine2 = r"""                                                             
  ____      __   __   ____                 _   _   U _____ u 
 / __"| u   \ \ / /U |  _"\ u     ___     | \ |"|  \| ___"|/ 
<\___ \/     \ V /  \| |_) |/    |_"_|   <|  \| |>  |  _|"   
 u___) |    U_|"|_u  |  _ <       | |    U| |\  |u  | |___   
 |____/>>     |_|    |_| \_\    U/| |\u   |_| \_|   |_____|  
  )(  (__).-,//|(_   //   \\_.-,_|___|_,-.||   \\,-.<<   >>  
 (__)      \_) (__) (__)  (__)\_)-' '-(_/ (_")  (_/(__) (__) 

"""

acssi_syrine3 = r"""                                                                                                                                                                          
   SSSSSSSSSSSSSSS                                         iiii                                       
 SS:::::::::::::::S                                       i::::i                                      
S:::::SSSSSS::::::S                                        iiii                                       
S:::::S     SSSSSSS                                                                                   
S:::::S      yyyyyyy           yyyyyyyrrrrr   rrrrrrrrr  iiiiiiinnnn  nnnnnnnn        eeeeeeeeeeee    
S:::::S       y:::::y         y:::::y r::::rrr:::::::::r i:::::in:::nn::::::::nn    ee::::::::::::ee  
 S::::SSSS     y:::::y       y:::::y  r:::::::::::::::::r i::::in::::::::::::::nn  e::::::eeeee:::::ee
  SS::::::SSSSS y:::::y     y:::::y   rr::::::rrrrr::::::ri::::inn:::::::::::::::ne::::::e     e:::::e
    SSS::::::::SSy:::::y   y:::::y     r:::::r     r:::::ri::::i  n:::::nnnn:::::ne:::::::eeeee::::::e
       SSSSSS::::Sy:::::y y:::::y      r:::::r     rrrrrrri::::i  n::::n    n::::ne:::::::::::::::::e 
            S:::::Sy:::::y:::::y       r:::::r            i::::i  n::::n    n::::ne::::::eeeeeeeeeee  
            S:::::S y:::::::::y        r:::::r            i::::i  n::::n    n::::ne:::::::e           
SSSSSSS     S:::::S  y:::::::y         r:::::r           i::::::i n::::n    n::::ne::::::::e          
S::::::SSSSSS:::::S   y:::::y          r:::::r           i::::::i n::::n    n::::n e::::::::eeeeeeee  
S:::::::::::::::SS   y:::::y           r:::::r           i::::::i n::::n    n::::n  ee:::::::::::::e  
 SSSSSSSSSSSSSSS    y:::::y            rrrrrrr           iiiiiiii nnnnnn    nnnnnn    eeeeeeeeeeeeee  
                   y:::::y                                                                            
                  y:::::y                                                                             
                 y:::::y                                                                              
                y:::::y                                                                               
               yyyyyyy                                                                                
"""

acssi_syrine4 = r"""

   .-'''-.    ____     __ .-------.   .-./`) ,---.   .--.    .-''-.   
  / _     \   \   \   /  /|  _ _   \  \ .-.')|    \  |  |  .'_ _   \  
 (`' )/`--'    \  _. /  ' | ( ' )  |  / `-' \|  ,  \ |  | / ( ` )   ' 
(_ o _).        _( )_ .'  |(_ o _) /   `-'`"`|  |\_ \|  |. (_ o _)  | 
 (_,_). '.  ___(_ o _)'   | (_,_).' __ .---. |  _( )_\  ||  (_,_)___| 
.---.  \  :|   |(_,_)'    |  |\ \  |  ||   | | (_ o _)  |'  \   .---. 
\    `-'  ||   `-'  /     |  | \ `'   /|   | |  (_,_)\  | \  `-'    / 
 \       /  \      /      |  |  \    / |   | |  |    |  |  \       /  
  `-...-'    `-..-'       ''-'   `'-'  '---' '--'    '--'   `'-..-'   
"""

def ligne():
    print("=========================================================================================================")

def random_acssi():
    sccii_list = [acssi_syrine1,acssi_syrine2,acssi_syrine3,acssi_syrine4]
    
    choiced = random.choice(sccii_list)
    
    print(choiced)

print("De Amine pour ça bien aimer.")
ligne()
print("Pour nos 1 ans : ")
print(" ")
print("Syrine + Amine = Pour la vie")
ligne()
sleep(2)
random_acssi()
ligne()
sleep(2)

while True:
    rslt = random.randint(0,20)
    
    if rslt <= 1:
        ligne()
        random_acssi()
        ligne()
        sleep(0.5)
    else: 
        phrase_je_taime = random.choice(je_taime_langues)
        compliment = random.choice(compliments)
        
        print(f"{phrase_je_taime}, {compliment}")
