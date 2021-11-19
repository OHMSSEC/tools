#!/bin/bash

#
while : ; do

resp=$(dialog --stdout  \
              --title 'OHMS MENU BASH' \
              --menu 'Oque devo fazer ?' \
              0 0 0                       \
              1 'Github'                  \
              )
[$? -ne 0 ]&& break

case "$resp" in 
    1) firefox 'https://github.com/ohmsz/tools' ;;
esac 
sair=$?
[$sair -eq 1 ]&& break

done
echo '\n[!]Saindo ...'
