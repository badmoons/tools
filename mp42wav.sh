#!/bin/sh

set +xe
echo "Convert .mp4 files to .wav easy."
printf "Usage:\n\tINPUT=<path/to/input/file> OUTPUT=<path/to/output/file> ./mp42wav\n\n"

ffmpeg -hide_banner -i $INPUT -ar 16000 -ac 1 -c:a pcm_s16le $OUTPUT
