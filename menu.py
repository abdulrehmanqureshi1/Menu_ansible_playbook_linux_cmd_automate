import os
import getpass

os.system("tput setaf 3")
print("\t\t\t Welcome to my Menu !!")
os.system("tput setaf 7")
print("\t\t\t----------------------")

passwd = getpass.getpass("Enter Your Password: ")

if passwd != "redhat":
    print("password incorrect ...")
    exit()

option = input("Where You Want to Run (local/remote) : ")

while True:
    print("start")

    os.system("clear")
    print("""
    \n
    Press 1  : Run Date
    Press 2  : Run Calculator
    Press 3  : Reboot
    Press 4  : Set Up Samba Server
    Press 5  : Set Up Web Server
    Press 6  : Set Up Docker
    Press 7  : Install Centos Image In Docker
    Press 8  : Create webserver Docker Image
    Press 9  : Run Docker webserver container
    Press 10 : User Create
    Press 11 : Exit
    """)

    ch = input("Enter Your Choice : ")
    print(ch)

    if option == "local":

        if int(ch) ==1:
            os.system("date")

        elif int(ch) ==2:
            os.system("cal")

        elif int(ch) ==3:
            os.system("reboot")

        elif int(ch) ==4:
            os.system("ansible-playbook samba_playbook.yml")
        
        elif int(ch) ==5:
            os.system("ansible-playbook webrole.yml")

        elif int(ch) ==6:
            os.system("ansible-playbook docker_role.yml --tags install_docker")

        elif int(ch) ==7:
            os.system("ansible-playbook docker_role.yml --tags pull_image_centos")

        elif int(ch) ==8:
            os.system("ansible-playbook docker_role.yml --tags build_image_apche")

        elif int(ch) ==9:
            os.system("ansible-playbook docker_role.yml --tags run_apache_container")


        elif int(ch) ==10:
            username = input("Please type username")
            os.system("useradd {}".format(username))

        elif int(ch) ==11:
            exit()

    elif option == "remote":

        ip = input("Enter remote ip address")


        if int(ch) ==1:
            os.system("ssh {} date".format(ip))

        elif int(ch) ==2:
            os.system("ssh {} cal".format(ip))

        elif int(ch) ==3:
            os.system("ssh {} reboot".format(ip))

        elif int(ch) ==6:
            username = input("Please type username")
            os.system("ssh {0} useradd {1}".format(ip,username))
           
        elif int(ch) ==7:
            exit()
   

    else:
        print("Not Supported Login")

    input("\nPlease Enter To Rerun ")



