# visual_scanning_game
This is a simple terminal text-based visual scanning game that was created as a practice game for individuals to visually scan on their keyboard to improve visual attention, perception and scanning abilities.

The module used is [art](https://pypi.org/project/art/), which is a pip module that can convert user input text into an ASCII art, with many different options of style and output.

<h3>Features</h3>

<h4>Assessment Data Logs</h4>
Currently, the program will prompt the user for the number of rounds they wish to participate in. It will also print out a score in the end. It can also log data.
The can do the following:
Enable or disable a save file.
If enabled, make it a custom name or a name that is customized.
Save the results of the data when used with a custom list. If it is not custom, there is no additional output on the file.txt

<h4>Standalone packaging</h4>

The program can be made into a standalone package, but has not been done so for this git since it would be more efficient for the end-user to create that package using [pyinstaller](https://www.pyinstaller.org/).


<h4>Custom list</h4>
There is a function built in to allow for custom letters or even words used.

This is simply a project designed for learning and perhaps one day be used in the therapy space for teachers or therapists working with individuals with cognitive or visual processing disorder difficulties.

This is not a medical tool by any means, but a therapeutic tool for practice.

<h4>Custom fonts</h4>

[Fonts](https://github.com/sepandhaghighi/art#font-modes) for sample output as I have noticed that the default font outrputs letter like U and V very similarly. This can be achieved by modifying the user editable setting, so less tinkering is necessary by the user.

<h4>Anticipated feature</h4>
I am looking to build this to web app that can either be run locally or hosted on a low cost server. Currently exploring options of either doing a Flask implementation or utilizing Ajax. It's unclear as these are some of less explored areas in programming and development. For now. This will be considered V1. 

Second feature is to allow a randomization of fonts. This can be achieved by using a list import of user preferred fonts. I also need to set up a default if this is the case.

<h3>Visual Scanning</h3>
Visual scanning is a skill involving cognitive motoric abilities to look for objects in space. The ability itself can be recognition of a pattern, an object, of even seeking relevant visual information. In the context of this game, most health individuals should be able to recognize the ASCII art as a respective letter shape and then visually scan for it on the keyboard to identify and press with no issue.

For individuals with difficulties, this isn't an assessment tool for a be all end all as more assessments will be required to make a more definitive judgement on difficulties with visual skills.

Once again, This is not a medical tool by any means, but a therapeutic tool for practice.

<h2>Instructions</h2>
<h3>For Terminal use</h3>
Download Python 3.x and install.

Wget, fork, or [download source files](https://www.alphr.com/download-files-github/).

Check python is installed using ``python --version`` or ``python3 --version``

Optional: Create a [virtual environment](https://docs.python.org/3/library/venv.html). 

Pip install requirements.txt command ``pip install -r requirements.txt`` This will install the art module.

Run function.py script. with python or python3 or python.exe or python3.exe

If you want to save results to a custom text file, simply add a single word after the function.py command such as ``python function.py yourname``, otherwise, a default one will be saved for you in results.txt. This can be disabled by changing the flag from True to false in the useroption.py file.

The useroption.py file has two user features that can be set. One is a save option for options to save data to file. One is the ability to use a custom list, and the other is to use all the alphabets in the list. Interesting thing about this option is that it will also take in words if you choose to add words into the list. At least that has been tested by me so far.

<h3>For Standalone Package use</h3>

A friend of mine told me that the pip module [pyinstaller](https://pypi.org/project/pyinstaller) would be able to solve this. This program would compile the intepreted language code into one that can be almost all in one, where the program can be run as long as the folder is shared amongst like hardware systems(Same OS version and same CPU architecture). I have decided not to compile and upload a complete program, but one can be built with these instructions. The only limitation here is that the program will not create a custom result file name, instead defaulting to only the base results.txt.

<h4>Steps</h4>

Run the command ``pip install pyinstaller``

``pyinstaller functionfile.py``

Two folders will be created with two sub folders. Open dist -->functionfile-->functionfile.exe or whichever file it is on a mac or Linux. I have only tested this on Windows 10. 


![image](https://github.com/kawangwong/visual_scanning_game/blob/main/Screenshot.jpg?raw=true)
