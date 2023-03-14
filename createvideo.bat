@echo off

ffmpeg -framerate 20 -i "output/%%04d.jpg" -i "bad apple.mp3" -c:a copy -c:v libx264 -vsync passthrough -pix_fmt yuv420p out.mp4