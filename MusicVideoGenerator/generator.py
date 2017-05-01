from __future__ import division

from os import listdir
from os.path import isfile, join
from random import shuffle

import configparser

from moviepy.editor import *

import audio_helpers

import sys

if len(sys.argv)!=2:
    print('Incorrect number of arguments!')
    sys.exit(0)

class ConfigLoader(object):
    DEFAULT_PATH = sys.argv[1]
    config_loader = None

    @classmethod
    def getDefaultValueFor(cls, key):
        if not cls.config_loader:
            cls.config_loader = configparser.ConfigParser()
            cls.config_loader.read(cls.DEFAULT_PATH)

        if not ('CONFIG' in cls.config_loader) or not (key in cls.config_loader['CONFIG']):
            return None

        return cls.config_loader['CONFIG'][key]


def getFilesFromDirectory(dir):
    return [f for f in listdir(dir) if isfile(join(dir, f))]


def linspace(start, stop, n):
    if n == 1:
        yield stop
        return
    h = (stop - start) / (n - 1)
    for i in range(n):
        yield start + h * i


def intervalFromTempo(tempo):
    return 60/tempo


def howManyRangesNeeded(duration, interval):
    return int(duration/interval) + 1


def getVideoLength(video_path):
    print('Obtaining video length for {}...'.format(video_path))
    clip = VideoFileClip(video_path)
    return clip.duration


def generateAndMerge(audio_path, video_path, ranges):
    audio_clip = AudioFileClip(audio_path)

    clip = VideoFileClip(video_path)

    miniclips = []

    for index, cl_range in enumerate(ranges):
        miniclips.append(clip.subclip(*cl_range))

    if ConfigLoader.getDefaultValueFor('SHUFFLE') == 'True':
        shuffle(miniclips)

    print('Merging clips...')
    final_clip = concatenate_videoclips(miniclips).set_audio(audio_clip)
    final_clip.write_videofile(ConfigLoader.getDefaultValueFor('OUTPUT_PATH'))

def main():
    inp_audio = ConfigLoader.getDefaultValueFor('INPUT_AUDIO')
    inp_vid = ConfigLoader.getDefaultValueFor('INPUT_VIDEO')

    start_offset = int(ConfigLoader.getDefaultValueFor('START_OFFSET'))
    end_offset = int(ConfigLoader.getDefaultValueFor('END_OFFSET'))

    interval_multiplier = int(ConfigLoader.getDefaultValueFor('INTERVAL_MULTIPLIER'))

    vid_len = getVideoLength(inp_vid)
    audio_len = audio_helpers.getDuration(inp_audio)
    audio_tempo = audio_helpers.estimateTempo(inp_audio)
    interval = interval_multiplier*intervalFromTempo(audio_tempo)
    ranges_needed = howManyRangesNeeded(audio_len, interval)

    linear_space = linspace(start_offset, int(vid_len)-end_offset, ranges_needed)
    ranges = [(x, x+interval) for x in linear_space]
    ranges_clean = ranges[:ranges_needed]
    generateAndMerge(inp_audio, inp_vid, ranges_clean)

main()

