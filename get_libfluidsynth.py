import requests
import zipfile
import io
import argh

from os.path import join as opjoin


def download_fluidsynth(venv_path = 'venv'):
    url = r'https://github.com/FluidSynth/fluidsynth/releases/download/v2.2.0/fluidsynth-2.2.0-win10-x64.zip'

    zfolder = 'bin/'
    export_folder = f'./{venv_path}/Scripts'

    filelist = [
        "libfluidsynth-3.dll",
        "libgcc_s_seh-1.dll",
        "libglib-2.0-0.dll",
        "libgobject-2.0-0.dll",
        "libgomp-1.dll",
        "libgthread-2.0-0.dll",
        "libinstpatch-2.dll",
        "libintl-8.dll",
        "libsndfile-1.dll",
        "libstdc++-6.dll",
        "libwinpthread-1.dll",
    ]

    def naming_rule(x: str) -> str:
        if x == "libfluidsynth-3.dll":
            return "libfluidsynth.dll"
        return x

    print("Downloading Fluidsynth")
    r = requests.get(url=url)

    print("Extracting fluidsynth")
    try:
        with zipfile.ZipFile(io.BytesIO(r.content)) as z:
            for file in filelist:
                path = opjoin(zfolder,file)
                with z.open(path,'r') as zfile:
                    with open(opjoin(export_folder,naming_rule(file)),'wb') as out:
                        out.write(zfile.read())


    except Exception as e:
        print("Error extracting",e)      


if __name__ == '__main__':
    argh.dispatch_command(download_fluidsynth)