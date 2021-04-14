from labeler import Labeler
from midi import MidiParser
from pipeline import Pipeline
from pstep_base import SymmetryAdapter
from synth import Synth
from synthesia import SynthesiaMetaDataParser
from accord_grouper import GroupAccords


def main():
    driver = Pipeline([
        [
            MidiParser('../Silent Night (Easy).mid'),
            SynthesiaMetaDataParser('../Silent Night (Easy).synthesia')
        ],
        [
            SymmetryAdapter(GroupAccords(), GroupAccords())
        ],
        [
            SymmetryAdapter(Synth('left\\out'), Synth('right\\out')),
            SymmetryAdapter(Labeler('left\\out'), Labeler('right\\out'))
        ]
    ])

    driver.run()


if __name__ == '__main__':
    main()
