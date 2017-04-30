#!/bin/bash
set -e
maxpage=13

for ((i=0; i<maxpage; i++))
do
	curl "https://www.kaggle.com/competitions.json?sortBy=deadline&group=all&segment=allCategories&page=${i}" -o "file-${i}.json"
done

jq '.competitions[]' file-* | jq -s . > competitions.json

for ((i=0; i<maxpage; i++))
do
	rm "./file-${i}.json"
done
