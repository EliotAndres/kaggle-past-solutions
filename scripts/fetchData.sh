#!/bin/bash
set -e
maxpage=6

for i in {1..$maxpage}
do
	curl "https://www.kaggle.com/competitions.json?sortBy=deadline&group=all&segment=featured&page=${i}" -o "file-${i}.json"
done

jq '.competitions[]' file-* | jq -s . > competitions.json

for i in {1..$maxpage}
do
	rm "./file-${i}.json"
done
