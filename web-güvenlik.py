import os

os.system("clear")

print("##############################")
print("                              ")
print("     Web Uygulama Güvenliği   ")
print("                              ")
print("##############################")
print()

print("1.Ddos")
print("2.Port Tarama")
print("3.Sqlmap")
print("4.Metasploit")

veri = input("İşlem :")

if veri =="1":
    x = input("Ddos Toolu otomatikten indirilecektir. Enter'a Basınız")
    os.system("python ddos.py")

elif veri =="2":
    x =input("Port Tarama Toolu Otomatik açılcaktır Enter'a Basınız")
    os.system("nmap")

elif veri =="3":
    x =input("Sqlmap Toolu Otomatik Açılcaktır Enter'a Basınız")
    os.system("sqlmap")

elif veri =="4":
    x =input("Metasploit açılcaktır Enter'a basınız")
    os.system("msfconsole")
