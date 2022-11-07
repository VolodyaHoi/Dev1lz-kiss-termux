#! /bin/bash

clear

echo -e "\033[31m
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╯╰╮╱╱╱╱╱╱╱╱╱╱╱┃┃╱
╱╭━━┳╮╭┳━━╮╱╱╱╭━━┳━┻╮╭╋━━┳━╮╭━━┳━━┫┃╱
╱┃╭╮┃╰╯┃┃━┫╱╱╱┃━━┫╭╮┃┃┃╭╮┃╭╮┫╭╮┃━━╋╯╱
╱┃╭╮┣╮╭┫┃━┫╱╱╱┣━━┃╭╮┃╰┫╭╮┃┃┃┃╭╮┣━━┣╮╱
╱╰╯╰╯╰╯╰━━╯╱╱╱╰━━┻╯╰┻━┻╯╰┻╯╰┻╯╰┻━━┻╯╱
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱
\033[0m"

if type -P python3 >/dev/null 2>&1; then
	echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mPython3 already installed!"
else 
	echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mChoose your environment.."
	echo -e "\033[32m[\033[31mINFO\033[32m] \033[36m1. Ubuntu Terminal"
	echo -e "\033[32m[\033[31mINFO\033[32m] \033[36m2. Termux"
	echo -e -n "\033[32m[\033[36mDK\033[32m] \033[0m>>> "
	read shell
	while [ $shell -ne 1 && $shell -ne 2 ]
	do
		echo -e "\033[32m[\033[31mERROR\033[32m] \033[36mYou entered wrong number!"
		echo -e -n "\033[32m[\033[36mDK\033[32m] \033[0m>>> "
		read shell
	done
	if [ $shell -eq 1 ]; then
		echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mInstalling python3.."
		sudo apt install python3
		echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mPython3 succefully installed!"
	elif [ $shell -eq 2 ]; then
		echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mInstalling python3.."
		pkg install python
		echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mPython3 succefully installed!"
		
		echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mInstalling openssl.."
		pkg install openssl
		echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mOpenssl succefully installed!"
	fi
fi  

echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mDownloading requarements..."

echo -e "\033[35m=================================\033[32m"

python3 test.py

echo -e "\033[35m================================="

echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mRequarements installed!"

echo -e "\033[32m[\033[31mINFO\033[32m] \033[36mScript ready to start..wait 5 seconds.."

sleep 5

clear

echo -e '
\033[31m╭━━━┳━━━┳━━━╮ \033[36m+   \033[32m[\033[93mDev1lz-kiss\033[32m]\033[35m 0.1.0              
\033[31m┃╭━━┫╭━━┫╭━━╯ \033[36m+ \033[93mAuthor: \033[35mAt0m		            	 
\033[31m┃╰━━┫╰━━┫╰━━╮ \033[36m+ \033[93mTelegram: \033[35m@atomthreatsup	   
\033[31m┃╭━╮┃╭━╮┃╭━╮┃ \033[36m+ \033[93mTeam: \033[35mAtomic Threat             
\033[31m┃╰━╯┃╰━╯┃╰━╯┃ \033[36m+ \033[31mThe God you worship can be you..
\033[31m╰━━━┻━━━┻━━━╯ \033[36m+         \033[31m(c)"Satanic bible ⸸"\033[0m'
echo " "
echo -e "\033[32m[\033[35mx\033[32m] \033[0mEnter <help> to get info"
echo -e "\033[32m[\033[35mx\033[32m] \033[0mPress Ctrl + Z to exit.."
echo " "
while :
do
	echo -e -n "\033[32m[\033[36mDK\033[32m] \033[0m>>> "
	read cmdN
	echo " "
	if [ "$cmdN" = "ip" ]; then # completed
		python3 test2.py
		echo " "
	elif [ "$cmdN" = "pn" ]; then # completed
		python3 test3.py
		echo " "
	elif [ "$cmdN" = "cProxy" ]; then # comming soon
		python3 test4.py
		echo " "
	elif [ "$cmdN" = "wfScan" ]; then
		python3 test5.py
		echo " "
	elif [ "$cmdN" = "spam" ]; then
		python3 test6.py
		echo " "
	elif [ "$cmdN" = "openCfg" ]; then # completed
		nano config.cfg
		echo " "
	elif [ "$cmdN" = "help" ]; then # completed
		echo -e "\033[32m[\033[35mx\033[32m] \033[0mHelp:"
		echo -e "\033[32m[\033[35mx\033[32m] \033[0m<ip> get IP address info"
		echo -e "\033[32m[\033[35mx\033[32m] \033[0m<pn> get info about phone number"
		echo -e "\033[32m[\033[35mx\033[32m] \033[0m<cProxy> change proxy [Cooming soon]"
		echo -e "\033[32m[\033[35mx\033[32m] \033[0m<wfScan> scanning your wi-fi connection [Cooming soon]"
		echo -e "\033[32m[\033[35mx\033[32m] \033[0m<spam> spam attack [Cooming soon]"
		echo -e "\033[32m[\033[35mx\033[32m] \033[0m<openCfg> edit config.cfg"
		echo " "
	else 
		echo -e "\033[32m[\033[31mERROR\033[32m] \033[36mUnknown command!"
		echo " "
	fi
done

