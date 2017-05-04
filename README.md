# Music Video Generator

**Summary** 

Extremly simple music clips generator targeted for those in hurry  

## Overview

This tools works in the following way:

1. It measures tempo of specified music track 
2. It calculates interval for changing view based on tempo
3. It cuts specified video  to clips of length 'interval'
4. Shuffles them (optionally)
5. Merges clips all together

## Requirements

- Python 3.X
- GTK+ (version 3) (for GUI)
- librosa
- moviepy

## Installation

```
$ git clone https://github.com/szymonsadowski3/Simple-Music-Video-Generator.git
```

## Basic use (see also: [Pictures](#pictures))

1. Firstly, you must define your config file (via GUI or by writing it yourself)
2. After this step you are ready to generate your music video
3. Run from your command line generator: ```python3.5 generator.py <path_to_config_file>```
4. Wait for your results :D

## Pictures

1. ![1st step](http://i.imgur.com/vbH2OnS.png)
2. ![2ndstep](http://i.imgur.com/2eJqUlV.png)
3. ![3rd step](http://imgur.com/IfkCh3Pl.png)
