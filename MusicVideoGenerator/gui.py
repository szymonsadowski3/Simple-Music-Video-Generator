import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def createConfig(a_in, v_in, st_off, end_off, mul, v_out, shuffle, cfg_out):
    pattern = """[CONFIG]
INPUT_AUDIO = {}
INPUT_VIDEO = {}
START_OFFSET = {}
END_OFFSET = {}
INTERVAL_MULTIPLIER = {}
OUTPUT_PATH = {}
SHUFFLE = {}""".format(a_in, v_in, st_off, end_off, mul, v_out, shuffle)

    with open(cfg_out, 'w+') as out:
        out.write(pattern)

builder = Gtk.Builder()
builder.add_from_file("gui.glade")

class Handler:
    def onDeleteWindow(self, *args):
        print('Quitting main window')
        Gtk.main_quit(*args)

    def onExport(self, button):
        #WIDGETS
        fchooser_audio_in = builder.get_object('fchooser_audio_in')
        fchooser_video_in = builder.get_object('fchooser_video_in')

        entry_video_out = builder.get_object('entry_video_out')
        entry_cfg_out = builder.get_object('entry_cfg_out')

        spin_st_offset = builder.get_object('spin_st_offset')
        spin_end_offset = builder.get_object('spin_end_offset')
        spin_interval_mul = builder.get_object('spin_interval_mul')
        combo_shuffle = builder.get_object('combo_shuffle')

        #VALUES
        audio_in = fchooser_audio_in.get_file().get_path()
        video_in = fchooser_video_in.get_file().get_path()

        st_offset = spin_st_offset.get_value_as_int()
        end_offset = spin_end_offset.get_value_as_int()

        interval_mul = spin_interval_mul.get_value_as_int()

        video_out = entry_video_out.get_text()

        shuffle = combo_shuffle.get_text()

        cfg_out = entry_cfg_out.get_text()

        print('Exporting cfg file...')
        createConfig(audio_in, video_in, st_offset, end_offset, interval_mul, video_out, shuffle, cfg_out)
        print('Done')


builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

Gtk.main()