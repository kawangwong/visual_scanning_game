# visual_scanning_game
This is a simple terminal text-based visual scanning game that was created for practice with individuals to scan on their keyboard to improve visual attention, perception and scanning abilities.

The module used is [art](https://pypi.org/project/art/), which is a pip module that can convert user input text into an ASCII art, with many different options of style and output.

Currently, the program will prompt the user for the number of rounds they wish to participate in. It will also print out a score in the end.
It will also create a text file post round for saved user data by default, which can be changed through modifying the functionfile.py file from True to False. A custom file name function can be utilized by adding a single space name after the command to run the program. Purpose of save function for scoring in case this was used as a metric assessment or repeated assessment. That can be implemented as an optional function.

This is simply a project designed for learning and perhaps one day be used in the therapy space for teachers or therapists working with individuals with cognitive or visual processing disorder difficulties.

This is not a medical tool by any means, but a therapeutic tool for practice.

<h3>Anticipated feature</h3>
I am looking to build this application into a package or perhaps a web app that can either be run locally or hosted on a low cost server. Currently explorying options of either doing a Flask implementation or py installer or utilizing Ajax. It's unclear as these are some of less explored areas in programming and development. For now. This will be considered V1.
Second feature will be a auto response without user return key input, to reduce lag time between question and answer as well as a way to set the program for use with specific letters only and change in font for sample output as I have noticed that the default font outrputs letter like U and V very similarly.

<h3>Visual Scanning</h3>
Visual scanning is a skill involving cognitive motoric abilities to look for objects in space. The ability itself can be recognition of a pattern, an object, of even seeking relevant visual information. In the context of this game, most health individuals should be able to recognize the ASCII art as a respective letter shape and then visually scan for it on the keyboard to identify and press with no issue.

For individuals with difficulties, this isn't an assessment tool for a be all end all as more assessments will be required to make a more definitive judgement on difficulties with visual skills.

Once again, This is not a medical tool by any means, but a therapeutic tool for practice.

<h2>Instructions</h2>
<h3>For Terminal use</h3>
Download Python 3.x and install.

Wget, fork, or [download source files](https://www.alphr.com/download-files-github/).

Pip install requirements.txt command ``pip install -r requirements.txt`` This will install the art module.

Check python is installed using ``python --version`` or ``python3 --version``

Optional: Create a [virtual environment](https://docs.python.org/3/library/venv.html). 

After you installed python and pip, run ``pip install -r requirements.txt``

Run function.py script. with python or python3 or python3.exe or python3

If you want to save results to a custom text file, simply add a single word after the function.py command such as ``python function.py yourname``, otherwise, a default one will be saved for you in results.txt. This can be disabled by changing the flag from True to false in the function python file on line.

<h3>For Standalone Package Use</h3>
A friend of mine told me that the pip module [pyinstaller](https://pypi.org/project/pyinstaller/) would be able to solve this. This program would compile the intepreted language code into one that can be almost all in one, where the program can be run as long as the folder is shared amongst like hardware systems(Same OS version and same CPU architecture). I have decided not to compile and upload a complete program, but one can be built with these instructions. The only limitation here is that the program will not create a custom result file name, instead defaulting to only the base results.txt.
<h4>Steps</h4>

Run the command ``pip install pyinstaller``

``pyinstaller functionfile.py``

Two folders will be created with two sub folders. Open dist -->functionfile-->functionfile.exe or whichever file it is on a mac or Linux. I have only tested this on Windows 10. 


![image](https://github.com/kawangwong/visual_scanning_game/blob/main/Screenshot.jpg?raw=true)
