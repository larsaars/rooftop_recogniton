#!/bin/bash
find . -name '*.png' -execdir mogrify -resize 28x28 {} + 
