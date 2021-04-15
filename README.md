# Convert Synthesia Finger Data to wav's and labels

## Setup 
- `python -mvenv venv`
- `pip install -r requirements.txt`
- `python get_libfluidsynth.py`  
   Note that for this step to work you need to have a virutal env installed in `venv`  
   if that is not the case specify your venv path with `-v VENV_PATH`


## Compatability
- Python3 
- Windows only (requires relativley easy modification to get_fluidsynth to get it working on linux)

## Usage
```
Usage:
  python resynth.py <midi_file> <synthesia_file> --output-left LFOLDER --output-right RFOLDER

Options:
  --output-left   the folder to put the samples and labels into for the left hand,
                  note that they will be named out<i>.wav & out<i>.labels.npy respectively
                  (where i indicates the accord)
  --output-right  the folder to put the samples and lables into for the right hand,
                  note that the same rules apply as to the left hand

Output Format:
    The Wav files will be pressed for one second and have a one second decay, making them
    2 seconds long, they are sampled at 44100kHz

    The labels are stored in npy binary format and have the following structure:
    [(<first note>,<finger>),(<second note>,<finger>)...]
```