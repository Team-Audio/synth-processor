from labeler import Labeler
from midi import MidiParser
from pipeline import Pipeline
from pstep_base import SymmetryAdapter
from synth import Synth
from synthesia import SynthesiaMetaDataParser
from accord_grouper import GroupAccords
import argh

@argh.arg('--output_left','-l')
@argh.arg('--output_right','-r')
@argh.arg('--soundfont','-f')

def main(midi_file, synthesia_file, output_left='left', output_right='right',soundfont=r'C:\soundfonts\default.sf2'):
    driver = Pipeline([[
        MidiParser(midi_file),
        SynthesiaMetaDataParser(synthesia_file)
    ], [
        SymmetryAdapter(GroupAccords(), GroupAccords())
    ], [
        SymmetryAdapter(Synth(f'{output_left}\\out',soundfont), Synth(f'{output_right}\\out',soundfont)),
        SymmetryAdapter(Labeler(f'{output_left}\\out'), Labeler(f'{output_right}\\out'))
    ]])

    print(driver.run())


if __name__ == '__main__':
    argh.dispatch_command(main)
