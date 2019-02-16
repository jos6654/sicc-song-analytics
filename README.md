# sicc-song-analytics

## What is this?

Sicc Song Analytics (SSA) is a lyric analytical engine built in Python using the Genius API. This was made as a project during RIT's annual hackathon: BrickHack 2019. This is a collaboration effort by Max Cohn, Joe Schull, and Ryan Weiss (aka 'Boys with a Z').

## How does it work?

SSA consists of two main parts, a front end built on Flask, and a backend.

### The Front End

Users can enter an artist who's lyrics they want analyzed. Requests are handled on the backen.

### The Back End

Once a request is recieved, the artist requested is checked to see if they have already had analytics generated for them. If so, those analytics are returned to the front end, if not, the lyrics of all songs in the artist's discography are analyzed, stored in the database, and then pushed to the front end.