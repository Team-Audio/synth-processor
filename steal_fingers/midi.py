import sys

import mido

from pstep_base import PipelineStepBase


class MidiParser(PipelineStepBase):
    def __init__(self, filename: str):
        print("Ingesting midi", file=sys.stderr)
        midi = mido.MidiFile(filename)

        def do_i_want_this(x: mido.Message):
            return 'velocity' in x.dict() and x.dict()['velocity'] > 0

        self.left = list(filter(do_i_want_this, midi.tracks[1]))
        self.right = list(filter(do_i_want_this, midi.tracks[0]))

    def has_left(self) -> bool:
        return len(self.left) > 0

    def has_right(self) -> bool:
        return len(self.right) > 0

    def pop_left(self):
        return self.left.pop(0)

    def pop_right(self):
        return self.right.pop(0)
