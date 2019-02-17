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

## What did we learn?

### Joe

### Ryan

### Max

First off, I love regular expressions, but wow did I learn to love them even more.

## General points

* Is this project perfect? No.
* Is this project going to get worked on after BrickHack 5? Probably not
* Is the code the most beautiful thing ever? We'd like to think so, but it has its short comings.

But all of this is OK! This is a learning experience for us and it's been a ton of fun!