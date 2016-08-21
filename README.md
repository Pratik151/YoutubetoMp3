# YoutubetoMp3
**Command line tool to download youtube video as mp3 file**

#Installation

##Using pip

`pip install YoutubetoMp3`

##Get the latest version from the Source

* Clone the repo `git clone https://github.com/Pratik151/YoutubetoMp3.git`
* Run `python setup.py install`

##Dependencies
* Beautifulsoup - `pip install beautifulsoup4`

##How to run
`YoutubetoMp3 URL [path] [filename]`
* There is one required argument URL which is the URL of the youtube video
* Second argument is path where the file has to be downloaded, it is optional and default is /home/Music
* Third argument is name of the file, it is optional and default is name of the video

##Examples
* `YoutubetoMp3 https://www.youtube.com/watch?v=450p7goxZqg`
* `YoutubetoMp3 https://www.youtube.com/watch?v=450p7goxZqg /home/Documents/`
* `YoutubetoMp3 https://www.youtube.com/watch?v=450p7goxZqg /home/Documents/ Song.mp3`

##Upcoming Features
* Download Mp3 file by name of the video
* and more

##Contribute
* If you find any bugs feel free to open Issue and if you want to add new features/fix any bug then send a Pull Request *
