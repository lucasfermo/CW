#!/bin/sh


m=$1

declare -A dict

dict=( ["A"]="T" ["C"]="G" ["T"]="A" ["G"]="C")

temp=""


for (( i=0; i<${#m}; i++ ));do
	
	old=${m:$i:1}
	
	new=${dict[$old]}
	temp="$temp$new"
done

echo $temp

	