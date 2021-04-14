import fluidsynth
import numpy as np

import wave

from tqdm import tqdm

from pstep_base import SymmetricPipelineStepBase


class Synth(SymmetricPipelineStepBase):
    def __init__(self, outname='out', sfont='C:\\soundfonts\\default.sf2'):
        self.sfont = sfont
        self.outname = outname
        self.fnames = []

    def take_pipeline(self, value):
        for i, ((accords, _),) in enumerate(tqdm(value, desc='Synthesizing Audio')):

            fl = fluidsynth.Synth()

            sfid = fl.sfload(self.sfont)
            fl.program_select(0, sfid, 0, 0)

            s = np.array([])

            for (note, _) in accords:
                fl.noteon(0, note, 80)

            s = np.append(s, fl.get_samples(44100))

            for (note, _) in accords:
                fl.noteoff(0, note)

            s = fluidsynth.raw_audio_string(np.append(s, fl.get_samples(44100)))

            with wave.open(f"{self.outname}{i}.wav", 'w') as obj:
                obj.setnchannels(1)
                obj.setsampwidth(2)
                obj.setframerate(44100)

                obj.writeframesraw(s)
                self.fnames += [f"{self.outname}{i}.wav"]

    def has_value(self) -> bool:
        return len(self.fnames) > 0

    def pop(self):
        self.fnames.pop(0)
