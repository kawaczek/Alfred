#update i upgrade
while true; do
    read -p "czy zrobic update i upgrade?"  tn
    case $tn in
        [Tt]* )   a="true"; break ;;
        [Nn]* )   a="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac
done
#apt-get install pliki
while true; do
    read -p "czy zainstalowac potrzebne pliki?" tn
    case $tn in
        [Tt]* )   b="true"; break ;;
        [Nn]* )   b="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac

done
#rdate
while true; do
    read -p "Czy ustawić czas?" tn
    case $tn in
        [Tt]* )   c="true"; break ;;
        [Nn]* )   c="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac

done
# sciagniecie i instalacja realvnc
while true; do
    read -p "Instalujemy RealVNC ? (musimy posiadac licence ona jest za free)" tn
    case $tn in
        [Tt]* )   d="true"; break ;;
        [Nn]* )   d="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac
done
if $d ;then
read -p "poprosze o licencje RealVNC" reallic
fi

#mega
while true; do
    read -p "Czy mamy konto na mega.nz (darmowy backup)" tn
    case $tn in
        [Tt]* )   e="true"; break ;;
        [Nn]* )   e="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac
done

if $d ;then
 while true; do
    read -p "Czy zainstalować klienta mega.nz ?" tn
    case $tn in
        [Tt]* )   f="true"; break ;;
        [Nn]* )   f="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac
 done

    read -p "prosze o podanie loginu(mail)" megalogin
    read -p "prosze o podanie hasla" megapass

fi

#aktualizacja pip'a
while true; do
    read -p "Aktulizujemy pip?" tn
    case $tn in
        [Tt]* )   g="true"; break ;;
        [Nn]* )   g="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac

done

#instalacja zaleznosci do alfreda
while true; do
    read -p "instalujemy twittera?" tn
    case $tn in
        [Tt]* )   g1="true"; break ;;
        [Nn]* )   g1="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac

done

#instalacja wit
while true; do
    read -p "instalujemy wita?" tn
    case $tn in
        [Tt]* )   h="true"; break ;;
        [Nn]* )   h="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac

done



#beutiful soap
while true; do
    read -p "czy instalujemy beutiful soap ?" tn
    case $tn in
        [Tt]* )   i="true"; break ;;
        [Nn]* )   i="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac

done


#apt-get pywanna
while true; do
    read -p "czy zainstalowac pyvona (syntezator mowy)?" tn
    case $tn in
        [Tt]* )   j="true"; break ;;
        [Nn]* )   j="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac

done


#apt-get samba
while true; do
    read -p "instalujemy sambe (dysk sieciowy)" tn
    case $tn in
        [Tt]* )   k="true"; break ;;
        [Nn]* )   k="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac

done

#apt-get samba
while true; do
    read -p "instalujemy soft od bluetootha" tn
    case $tn in
        [Tt]* )   l="true"; break ;;
        [Nn]* )   l="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac

done
#Zet
while true; do
    read -p "zrobić magie ?" tn
    case $tn in
        [Tt]* )   z="true"; break ;;
        [Nn]* )   z="false" ; break;;
        * ) echo "wybieramy t/n.";;
    esac

done






if $a ; then

 sudo apt-get update && sudo apt-get upgrade -y

fi
if $b ; then

 sudo apt-get -y install python-dev python-pip libsox-dev libffi-dev rdate build-essential libglib2.0-dev libssl-dev libcurl4-openssl-dev libgirepository1.0-dev screen

fi

if $c ; then

sudo rdate -s ntp.task.gda.pl

fi

if $d ; then

curl -L -o VNC.tar.gz https://www.realvnc.com/download/binary/latest/debian/arm/ 
tar xvf VNC.tar.gz 
sudo dpkg -i *.deb
rm *.tar.gz
rm *.deb
sudo vnclicense -add $reallic
fi


if $e ; then

sudo rdate -s ntp.task.gda.pl

fi

if $f ; then

wget http://megatools.megous.com/builds/megatools-1.9.95.tar.gz 
tar -zxf megatools-1.9.95.tar.gz 
cd megatools-1.9.95 
./configure --disable-shared 
make
sudo make install
fi 


if $g ; then

sudo pip install --upgrade pip
sudo pip install 'requests[security]'
fi

if $g1 ; then
sudo pip install tweepy
fi
if $h ; then
sudo pip install wit requests
fi

if $i ; then
sudo pip install beautifulsoup4
fi

if $j ; then
sudo pip install  pyvona
fi

if $k ; then
sudo apt-get  install  samba samba-common-bin
fi

if $l ; then
sudo apt-get install bluetooth bluez blueman pulseaudio-module-bluetooth
fi

echo "[Login]" > ~/.megarc
echo "Username = " $megalogin >> ~/.megarc
echo "Password = " $megapass >> ~/.megarc


if $z ; then
cd
megaget /Root/AlfredBckp/current.tar.gz
tar -zxf current.tar.gz
sudo mv ~/Alfred/wpa_supplicant.conf /etc/wpa_supplicant/
sudo mv ~/Alfred/hostname /etc/hostname
sudo mv ~/Alfred/.conf ~/
pacmd set-default-sink 1
pacmd set-default-source 1
sudo head -n -9 /usr/local/lib/python2.7/dist-packages/pyvona.py > pyvona.tmp
curl http://kawak.pl/ivopl >> pyvona.tmp
sudo mv pyvona.tmp /usr/local/lib/python2.7/dist-packages/pyvona.py
mv ~/Alfred/.conf ~/.conf
fi
