## greetings from the stabby stabbot :hocho:

### What is this?
I was stuck at home during a typhoon and was bored. I also happen to be one of the mods for a discord server for a [community](https://www1.flightrising.com/forums/forga/3208161/1) that plays forum mafia / werewolf on Flight Rising (FR), a dragon breeding site, meaning that I could probably abuse my mod powers and have the server be the testing grounds for my bot-creating shenangians. 

Hence, the stabby stabbot :tm: was created with a feature absolutely nobody needed or asked for: to "randomly" generate a (possibly very unbalanced) mafia rolecard given a dragon.

This bot is created for said server, but if you would like to add the bot to your server [here is the link!](https://discord.com/api/oauth2/authorize?client_id=1147007001621168128&permissions=2048&scope=applications.commands%20bot)

### Available Commands

`/rolecard [link to FR dragon]`: randomly generates a rolecard for a dragon of your choice.

(more cursed commands to come, maybe)

### How does it work?

The /rolecard function is *supposed* to take in a link to the dragon, but it doesn't actually go to the link or access the site, as that would violate FR's TOS. The only thing that it extracts is the dragon ID, a 1-8 digit number, at the end of the link.

...and then I butcher the dragon id and get its SHA-1 hash and do some "magic" with the hash. Which means I look at different digits of the hash, and assign things to the rolecard based on the value of that character. 

For example, the alignment is determined by the first digit of the hash: if the first digit is from 0-2, you're a third party. If it's 3-6, you're mafia. If it's 7 to f (=15 in hexadecimal), you're town. (you can see this from `ALIGNMENT_MAPPING` in `rolecard_mappings.py`.)

#### What is SHA-1 and why are you using it?
First things first. SHA-1 is a *cryptographic hash function*, which is mostly being used for cryptography stuff to protect the integrity of stuff (i.e. digital signatures). SHA-1 is no longer considered to be secure, but I'm not using it for security purposes.

Such functions have several properties that are beneficial for my use case:

- They **turn a string of *any* length into a fixed-length string.** In SHA-1's case it turns its input into a string of 40 hexadecimal (each character can have 16 possible values) characters. This means that no matter how many digits the dragon id has, I will know how many digits its hash has and can do things like "if the xth digit of the hash is a certain value, do something to the rolecard".
- They are **one-way functions** (i.e. it is hard to guess the input by looking at the output). Part of this means that the input-to-output conversion is hard to predict and seemingly random--changing the input slightly will give you an entirely different hash (you can see what I mean for yourself with literally any online tool such as [this one](https://emn178.github.io/online-tools/sha1.html))! This mean that I can also have seemingly random rolecards generated (i.e. you won't see all dragons with id ending in '1' be mafia-aligned.)
- They will **always return the same value given the same input**. Even though I want the rolecard to be "randomly" generated, calling `/rolecard` on the same dragon should always give the same results. 

...40 characters is too much though for my use case, so I subsequently yeeted all of the digits after the first eight.

So! For demonstration purposes, here are the first 8 digits of the SHA-1 hashes of different dragon IDs:
```pycon
>>> import hashlib
>>> hashlib.sha1('10'.encode('utf-8')).hexdigest()[:8]
'b1d57811'
>>> hashlib.sha1('11'.encode('utf-8')).hexdigest()[:8]
'17ba0791'
>>> hashlib.sha1('83221441'.encode('utf-8')).hexdigest()[:8]
'720d5517'
``` 