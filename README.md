![GitHub](https://img.shields.io/github/license/hunar4321/life_code)

# Play Colored ASCII Videos in your Terminal
A program that takes a video file and outputs colored ASCII real-time video inside a terminal (with audio).\
Now works with YouTube videos in real time as well thanks to [Roman](https://github.com/zeromero-dev)!\
Only works if your terminal uses ANSI codes. \
The windows terminal does not recognize color by default. It's an option on win10+.\
Also the font needs to be monospace or the output will look funny. The font used in all demos is Iosevka Nerd Font.

Made a [Youtube Video](https://www.youtube.com/watch?v=s4weLmlOc0s&t=4s&ab_channel=HistidineDwarf)

Do what you want with the code, but credit would be much appreciated.

How to use
-------------
1. Install python3
2. Run `pip install -r requirements.txt`
3. Run `python3 bapple.py`
4. Follow displayed instructions\

**Note**: `ascii_scheme` controls whether bigger characters are used on brighter or darker pixels. Some video looks **terrible** with the wrong scheme. Same goes for the display mode. Mess around with options till it works, but Inverse scheme + max size usually works.

Change the font size of your terminal for lower/higher resolution.<br>
**If you make the font too small audio will desync because it takes too long to think per frame!**

Run the `bapple.py` script to start it. \
**Fun fact**: it's called that because the project was initially another bad apple recreation.

Examples
---------
The size limit on github is miserably low. Follow the the streamable links for full video

- ![fighter](https://user-images.githubusercontent.com/96934612/202935752-28bbe7c7-34e9-475e-8e94-73be04358da9.gif)
- [Full ASCII Colored Video](https://streamable.com/vbuxni)
- [Source video](https://www.youtube.com/watch?v=6QAiq536yWE&ab_channel=ichimaru)

For the Bad Apple demo, I messed with the settings of the program and it created a cool border effect I like.
- ![bapple](https://user-images.githubusercontent.com/96934612/202935774-eb57d621-dc68-4917-94f9-1b1fe77a54be.gif)
- [Full ASCII Colored Video](https://streamable.com/qyrrm3)
- [Source video](https://www.youtube.com/watch?v=FtutLA63Cp8)

- ![gamer](https://user-images.githubusercontent.com/96934612/202935903-ff8285fa-95af-41b6-9614-d499234711e8.gif)
- [Full ASCII Colored Video](https://streamable.com/kn4793)
- [Source video](https://www.youtube.com/watch?v=quSI1wm5WQg&ab_channel=quagmiretoiletgaming)
