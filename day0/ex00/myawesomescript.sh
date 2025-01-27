#!/bin/sh

curl -sS $1 | grep -o 'href="[^"]*"' | cut -d '"' -f 2
 