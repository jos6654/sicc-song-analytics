# sicc-song-analytics

## What is this?

Sicc Song Analytics (SSA) is a lyric analytical engine built in Python using the Genius API. This was made as a project during RIT's annual hackathon: BrickHack 2019. This is a collaboration effort by Max Cohn, Joe Schull, and Ryan Weiss (aka 'Boys with a Z').

## How does it work?

SSA consists of two main parts, a front end to send requests to a Flask server, and a backend written in Python.

### The Front End

Users can enter an artist who's lyrics they want analyzed. Requests are handled on the backen.

### The Back End

Once a request is recieved, the artist requested is checked to see if they have already had analytics generated for them. If so, those analytics are returned to the front end, if not, the lyrics of all songs in the artist's discography are analyzed, stored in the database, and then pushed to the front end.

## What technologies are we using?

We're using a Flask server to handle requests, MySQL to store the analytics after they're computed, and Python for all the code behind the scenes.

## What's the inpiration?

I (Max) was walking to class listening to 'Slaughter Beach, Dog' and I realised how much they mentioned coffee in their lyrics. I figured I'd write a little Python script to figure it out, but then I thought about all the other statistics we could track per artist. I held in my excitement and told my teammates (Joe and Ryan) and then we patiently waited til BrickHack, and here we are!

## What problems did we encounter?

Our main problem was the Genius API. We feel that there is much to be improved, particularly the addition of the ability to request a song's lyrics would be helpful.

Another odd issue with their API was that 'blink-182's artist name is stored with 2 zero width space characters (\u200b) preceding their name. **WHY?** There is no reason at all, and blink-182 is the **ONLY** artist where this is the case. It's especially unfortunate because blink-182 is Ryan's favorite band.

Another issue we ran into was that on Genius, anyone can add a song for an artist. This didn't affect small artists, but for an artist like Drake, this resulted in us getting a lot of garbage data that we didn't care about. We couldn't find a way to prevent this either. This was kind of unavoidable as we see it, due to Genius being a community driven service, there are bound to be some user faults.

## What did we learn?

### Joe

Previously I only had experience in Python from taking CS I, but to do this project I learned a bunch about using different libraries to accomplish tasks more easily. I also learned how to do some object-oriented programming in Python which was useful.

We also realized toward the middle of our project that our choice of using Genius API was poor because in order to get the actual song lyrics, we needed to take the url and scrape the lyrics which made our program take an ungodly amount of time to run.

So evaluate your tools before you're in too deep

### Ryan

### Max

First off, I love regular expressions, but wow did I learn to love them even more. We were able to use them for so many quick modifications to the text.

Piggybacking off of what Joe said, I learned the valuable lesson of learning how to use your tools before attempting to use them. We should have seen that the Genius API was lacking in the services we needed, but at least we know now!

I also learned how to write code that interacts with a database, which is definitely a skill I'll be using the future.

## What would we change?

If it wasn't apparent by now, we should've looked into other song lyric APIs, as Genius wasn't as good for our purposes as we had hoped. We would've looked more into other lyric APIs.

Other changes would be more modern web page design, but that wasn't a priority for us. We just wanted to make sure the data was received. We focused on function instead of asthetic, mostly because this isn't a project we will try to market, but test of our abilities.

## General points

* Is this project perfect? No.
* Is this project going to get worked on after BrickHack 5? Probably not.
* Is the code the most beautiful thing ever? We'd like to think so, but it has its short comings.

But all of this is OK! This is a learning experience for us and it's been a ton of fun!

## Side notes

Running this project takes a bit of work, as you need to modify the database login in `database.py`, and modify the access token for the Genius API in `song_retrieval.py`. Once that's going, it's a standard Flask app to be ran.