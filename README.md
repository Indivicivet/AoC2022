# AoC2022

this year I am going to try to have fun. :)

## Calendar

[reverse lookup](#reverse-lookup) (by language / method)

[Day 1](#day-1)
| [Day 2](#day-2)
| [Day 3](#day-3)
| [Day 4](#day-4)
| [Day 5](#day-5)

[Day 6](#day-6)
| [Day 7](#day-7)
| [Day 8](#day-8)
| [Day 9](#day-9)
| [Day 10](#day-10)

[Day 11](#day-11)
| [Day 12](#day-12)
| [Day 13](#day-13)
| [Day 14](#day-14)
| [Day 15](#day-15)

[Day 16](#day-16)
| [Day 17](#day-17)
| [Day 18](#day-18)
| [Day 19](#day-19)
| [Day 20](#day-20)

[Day 21](#day-21)
| [Day 22](#day-22)
| [Day 23](#day-23)
| [Day 24](#day-24)
| [Day 25](#day-25)

# Solutions

## Day 1

python with some arithmetic in brainfuck

[python code](/day01.py)

[brainfuck "sum chunks" for part 1](/day01_part1_sum_chunks.b)

[brainfuck "add 3 numbers"...](/day01_part2_sum3.b)

## Day 2

by hand in google docs/calculator

![part 1 ctrl-f for X, Y, Z, A X etc](/day02_part1.png)
![part 2 ctrl-f for A X, A Y, etc](/day02_part2.png)

## Day 3

### 3-1

in godot: pass the left half and right half of the background through each other, increasing the score whenever a collision happens. make a big explosion upon collision to remove duplicates

[godot project](/day03_part1/)

![part 1: lots of black boxes with letters, long orange rectangles and a score counter](/day03_part1_screenshot.png)

### 3-2

in python, code golfed to 95 bytes (loads a file called "3" in the same directory; there's a setup batch script to copy that from the inputs folder)

[python file](/day03_part2/day03_part2_95bytes.py)

## Day 4

### 4-1

work in progress: python + brainfuck

## Day 5

todo

## Day 6

by hand with pen + paper

![part 1: dots under the first many letters, column count and calculations on the side](/day06_part1.jpg)

![part 2: messy lines under letters in the middle, incorrect + correct calculations on the side](/day06_part2.jpg)

## Day 7

python (writing to/querying the filesystem, of course; only tested on windows)

[python code](/day07.py)

## Day 8

wip...

## Day 9

in (the rather nice, I think?) [noulith](https://github.com/betaveros/noulith) language by betaveros, the Advent of Code (current) #1 ranked user. [their webpage](https://beta.vero.site/) / [their github](https://github.com/betaveros/)

[part 1](/day09_part1.noul)

[part 2](/day09_part2.noul) which does act as a generalization of part 1, but also has slightly less clean code

## Day 10

in python and very boring, although at least I define sensible classes? [python code](/day10.py)

## Day 12

by hand with pen + paper

![day 12: areas to avoid blocked off, path highlighted, various tickmarks for counting the path length](/day12.jpg)

the right/finish section is navigating up a spiral of all letters, and I did this first, to get to d/e -- there is only one d/e area you can get to. I did this first, and it tells you where you have to aim for. the left/start section is just navagating a sea of c's; you can never drop into an a-hole because there are no b's to get back out. the route is super simple once you block off all the a's (ignore the part where I made a mistake...).

I had an off-by-two error which I fixed by going via z at the end, although the problem statement says that's the same elevation as the end point... I'm not sure how else I managed to create a shorter route :/

the second part is very easy. you only have to pick the optimal starting "a" point from the far left column, since there are no b's other than in the second column. you can then read off how many vertical steps you skipped by comparing to the start point and subtract that from the part 1 answer.

## Day 13

just plain python. trying to make it look easy since python *almost* solves this question out of the box, just not quite... [python code](/day13.py)

## Day 16

by hand on pen + paper, using a spreadsheet for the actual value calculations

### 16-1

first draw out all of the valves and tunnels...

![messy page with many two-letter valve names and connecting lines](/day16/day16_part1_1.jpg)

then find the links between the valves you actually care about (ones with flow rate > 0; the majority of valves are flow rate 0 and just act as intermediate points)...

![the same page but with nonzero flow rate valves circled in green, and connected to each other in orange](/day16/day16_part1_2.jpg)

redraw just the nonzero flow rate valves (and distances) on a new page, highlight the 20+ and 10+ flow rate valves, scribble some candidate paths...

![a neater page showing a graph with fewer links, where high-value nodes are highlighted](/day16/day16_part1_4.jpg)

at this point there were three obvious candidate paths: two ways of rushing straight to a long chain of high values, and another way which gets a couple of very high values quickly but requires doubling back on yourself. I calculated the resulting score for these three paths with [a spreadsheet](/day16/day16_part1_calculations/.ods):

![spreadsheet calculating the score from magnitudes and times, with a section for each candidate path](/day16/day16_part1_calculations_screenshot.ods)

# Reverse Lookup

days by language / method / etc

## godot

- [day 3 part 1](#3-1)

## python + brainfuck

- [day 1](#day-1)
- [day 4 part 1](#4-1)

## python (gode colfed)

- [day 3 part 2](#3-2) 95 bytes

## just python...

- [day 7](#day-7) (+ filesystem!)
- [day 10](#day-10)
- [day 13](#day-13)

## noulith

this is the language [noulith](https://github.com/betaveros/noulith) written by betaveros, the Advent of Code (current) #1 ranked user. [their webpage](https://beta.vero.site/) / [their github](https://github.com/betaveros/)

- [day 9](#day-9)

## google docs

- [day 2](#day-2) in google docs (+google calculator)

## pen + paper

- [day 6](#day-6) by hand with pen + paper
- [day 12](#day-12) by hand with pen + paper (+ highlighter)
- [day 16](#day-16) pen + paper, plus a spreadsheet for actual value calculations
