#!/bin/bash

echo "enter filename"
read filename

git add $filename
git commit -m "create $filename"
git push

