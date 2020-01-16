#!/bin/bash
string1=$1
string2=$2
string3="awesome"

if [ ${string1} == ${string2} ]; then
    echo "string 1, string2 is same"
elif [ ${string1} == ${string3} ]; then
    echo "string 1 is awesome"
else
    echo "else condition"
fi
