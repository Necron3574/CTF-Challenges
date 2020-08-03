# Arch Enemy
## Description
```
John likes Arch Linux. What is he hiding?
Link to image -
https://ctf.csivit.com/files/0f0746bf806a1e956f7a384c5dd22260/arched.png?token=eyJ1c2VyX2lkIjoxMTczLCJ0ZWFtX2lkIjozMzAsImZpbGVfaWQiOjQ4NDd9.Xxbmpw.fkSB2EiJvjhJDIwsHhrUQaFv944
```
## Solution
* Okay so we have a png image.
* Hoping that it was an image of the flag I opened it but wait *drumrolls* It didnt open.
* So I went on my terminal and used the `file` command and it says that the image is jpeg format.
* After changing the extension of the file from `.png` to `.jpg` I was able to open the image.
* But its just a black arch linux wallpaper.
* So I started using steg tools.
* Exiftool and Binwalk didnt give me anything useful.
* Then suddenly it hit me that I was supposed to use Steghide.
* My reasoning was that since png is unsupported by steghide the image must have been changed to that.
* So I quickly tried to extract files with steghide with an empty password.(Command given below)
  `steghide extract -sf arched.jpg`
* And bingo I got a zip file called flag.zip.
* I tried to open it but alas it was password protected.
* But wait lets take a look at the question again, it says `John` like arch linux.
* Hence I got my friend to run a password bruteforce for an hour using `John The Ripper`.
* The password was `kathmandu`.
* So I entered the password and found an image which had the flag inside it.
