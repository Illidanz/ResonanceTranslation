# Resonance Translation
## Setup
Create a "data" folder and copy the PSP image as "resonance.iso" in it, and the PS2 image as "resonance_ps2.iso".  
## Run from binary
Download the latest [release](https://github.com/Illidanz/ResonanceTranslation/releases) outside the data folder.  
Run `tool extract` to extract everything and `tool repack` to repack after editing.  
Run `tool extract --help` or `tool repack --help` for more info.  
## Run from source
Install [Python 3.8](https://www.python.org/downloads/) and pipenv.  
Download [armips.exe](https://github.com/Kingcom/armips/releases).  
Download xdelta.exe.  
Run `pipenv install`.  
Run the tool with `pipenv run tool.py` or build with `pipenv run pyinstaller tool.spec`.  
## Text Editing
Rename the \*\_output.txt files to \*\_input.txt (smd_output.txt to smd_input.txt, etc) and add translations for each line after the "=" sign.  
To blank out a line, use a single "!". If just left empty, the line will be left untranslated.  
Comments can be added at the end of lines by using #  
## Image Editing
Rename the out\_\* folders to work\_\* (out_IMG to work_IMG, etc).  
If an image doesn't require repacking, it should be deleted from the work folder.  
