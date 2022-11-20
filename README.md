![GitHub](https://img.shields.io/github/license/hunar4321/life_code)

# Colored-ASCII-Video
A program that takes a video file and outputs colored ASCII real-time video inside a terminal. Only works if your terminal works with ANSI codes. The windows terminal does not recognize color by default.

How to use
-------------
Put the path to your ethically sourced video in the `path` variable. 

`ascii_scheme` controls whether bigger characters are used on brighter or darker pixels. Some video looks terrible with the wrong scheme.

`mode` can be 1 or 2. 1 tries to keep the aspect ratio and 2 tries to fill up your terminal. Basically just try the other one if video breaks.

Change the font size of your terminal for lower/higher resolution. If you make the font too small audio will desync because it takes too long to think per frame

Run the `bapple.py` script to start it. it's called that because the project was initially another bad apple recreation.
