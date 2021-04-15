from labeler import Labeler
from midi import MidiParser
from pipeline import Pipeline
from pstep_base import SymmetryAdapter
from synth import Synth
from synthesia import SynthesiaMetaDataParser
from accord_grouper import GroupAccords
import argh


def main(midi_file, synthesia_file, output_left='left', output_right='right'):
    driver = Pipeline([[
        MidiParser(midi_file),
        SynthesiaMetaDataParser(synthesia_file)
    ], [
        SymmetryAdapter(GroupAccords(), GroupAccords())
    ], [
        SymmetryAdapter(Synth(f'{output_left}\\out'), Synth(f'{output_right}\\out')),
        SymmetryAdapter(Labeler(f'{output_left}\\out'), Labeler(f'{output_right}\\out'))
    ]])

    print(driver.run())


if __name__ == '__main__':
    argh.dispatch_command(main)
