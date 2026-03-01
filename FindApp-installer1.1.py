import subprocess
import distro

print(r"""
 _       __     __                             __      
| |     / /__  / /________  ____ ___  ___     / /_____ 
| | /| / / _ \/ / ___/ __ \/ __ `__ \/ _ \   / __/ __ \
| |/ |/ /  __/ / /__/ /_/ / / / / / /  __/  / /_/ /_/ /
|__/|__/\___/_/\___/\____/_/ /_/ /_/\___/   \__/\____/   
                                                                                                   
                
 ________  _                 __       _                         _____                  _          __   __                 
|_   __  |(_)               |  ]     / \                       |_   _|                / |_       [  | [  |                
  | |_ \_|__   _ .--.   .--.| |     / _ \    _ .--.   _ .--.     | |   _ .--.   .--. `| |-',--.   | |  | | .---.  _ .--.  
  |  _|  [  | [ `.-. |/ /'`\' |    / ___ \  [ '/'`\ \[ '/'`\ \   | |  [ `.-. | ( (`\] | | `'_\ :  | |  | |/ /__\\[ `/'`\] 
 _| |_    | |  | | | || \__/  |  _/ /   \ \_ | \__/ | | \__/ |  _| |_  | | | |  `'.'. | |,// | |, | |  | || \__., | |     
|_____|  [___][___||__]'.__.;__]|____| |____|| ;.__/  | ;.__/  |_____|[___||__][\__) )\__/\'-;__/[___][___]'.__.'[___]    
                                            [__|     [__|                      [_____)
       ____     ____ 
___  _/_   |   /_   |
\  \/ /|   |    |   |
 \   / |   |  _ |   |
  \_/  |___| (_)|___|   

  ____________
 (            )
 (            )             
 (            )                                                           )             
 (            )
 (            )             
 (____________)                                                       
    ///
   ///
  ///
 ///
///
""")

distro = distro.like()
package_number = input("How many packages you want to install;(This tool supports 3 MAX!): ")
if package_number == "1":
      pkg_name = input("Please input the name of the application you want to install! (With lowercase characters only): ")
elif package_number == "2":
        pkg_name = input("Please input the name of the application you want to install! (With lowercase characters only): ")
        pkg_name_2 = input("Please input the name of the second application you want to install! (With lowercase characters only): ")
else :
    if package_number == "3":
         pkg_name = input("Please input the name of the application you want to install! (With lowercase characters only): ")
         pkg_name_2 = input("Please input the name of the second application you want to install! (With lowercase characters only): ")
         pkg_name_3 = input("Please input the name of the third application you want to install! (With lowercase characters only): ")
continue_ = input("please enter yes to continue or no if you dont! ")

def continue_or_not():
 if continue_ == "no":
     print("Exiting...")
     subprocess.run("exit")
 else:    
     print("ok")


continue_or_not()

def distro_check():
    if distro == "ubuntu debian" or distro == "debian":
        print("ok continuing succesfully with the installation")
    else:
        print("Temporarly this tool does not support any other linux distros except debian or ubuntu based please go to this link and install your app from here: https://flathub.org")

if package_number == "1":
  search_result = subprocess.run(
    f"apt list  {pkg_name}",
            shell=True,
            capture_output=True,
            text=True
        )
elif package_number == "2":
 search_result = subprocess.run(
            f"apt list  {pkg_name} {pkg_name_2}",
            shell=True,
            capture_output=True,
            text=True

        )
else:
 if package_number == "3":
  search_result = subprocess.run(
            f"apt list  {pkg_name} {pkg_name_2} {pkg_name_3}",
            shell=True,
            capture_output=True,
            text=True

        )

distro_check()


def app_installation():
    if "Listing..." in search_result.stdout and pkg_name not in search_result.stdout:
        print("❌ Package not found, please go to https://flathub.org and install your app from there!")
    else:
        print("package has been found✅")
        print(search_result.stdout)

app_installation()

confirmation = input("please input the package/packages you want to install as it is beeing shown above to confirm you want to install it!(ignore any notes execpt from the app!)if they are more than one please put spaces between each of them: ")

install_process = subprocess.Popen(
    f"sudo apt install -y {confirmation}",
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

for line in install_process.stdout:
    print(line, end="")  

install_process.wait()
print("App installed close the terminal window and enjoy!")