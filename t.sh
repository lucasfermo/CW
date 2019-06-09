#!/bin/sh

p=$2
c=0
s=0
while [ $s -lt $1 ]; do
	$s = $(($s+($2-($p*$3))))
	p=$p*$3
	c=$c+1
done

echo $c

	