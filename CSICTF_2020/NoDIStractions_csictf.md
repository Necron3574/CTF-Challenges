# No DIStractions
## Description
```
I see all, I read all, but I shall not speak until I am 'commanded' to do so.
Ask me, and thou shall recieve.
```
## Solution
This is a typical discord bot challenge.
The question tells us that the bot won't give us the flag unless its commanded to do so.
So on dming the bot with `.list` gives us a list of commands (The flag command is obviously missing).
Now we know we can initiate a command with a dot.
Hence I tried `.flag` and voila I got the flag.
