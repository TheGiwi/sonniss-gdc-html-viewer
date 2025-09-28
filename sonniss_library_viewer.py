import os
from textwrap import dedent

path = r"F:\ place-in-your-own-sonniss-library-parent folder-path"

counter = 0
counter2 = 0
counter6s = 0
counter6s_row = 1
Searchwav = ".wav"
SearchWAV = ".WAV"
SearchWav = ".Wav"
FileFullLog = "source/file_full_log.txt"


def extract_folder_name(input):
    parts = input.split('\\')
    if len(parts) >= 2:
        return parts[3]
    else:
        return None

def extract_file_name(input):
    parts = input.split('\\')
    if len(parts) >= 2:
        return parts[4]
    else:
        return None
    
    
def extract_file_path_rel(input):
    parts = input.split('\\')

    # Check if there are enough parts
    if len(parts) < 4:
        return ""  # Not enough parts to extract TEXT2 and TEXT3

    # Extract TEXT2 and TEXT3, and rejoin with forward slashes
    result = '/'.join(parts[2:4]) + '/'

    return result

def extract_file_path_abs(input):
    parts = input.split('\\')

    # Check if there are enough parts
    if len(parts) < 4:
        return ""  # Not enough parts to extract TEXT2 and TEXT3

    # Extract TEXT2 and TEXT3, and rejoin with forward slashes
    result = '/'.join(parts[0:4]) + '/'

    return result




HTML_file = "source/index.html"
html_code_b = dedent(f"""
                   
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Sonniss Viewer</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <div class="wrap">
    <h1>Sonniss GDC Audio Library Viewer</h1>
    <p class="hint">You can download the entire GDC library from Sonniss <a href="https://sonniss.com/gameaudiogdc/" style="text-decoration: none;font-weight: bold; color: #00ffdd;" target="_blank">here</a></p>

    <div class="toolbar">
      <button id="playAll" type="button">Play All (sequential)</button>
      <button id="pauseAll" type="button">Pause All</button>
      <button id="stopAll" type="button">Stop & Reset</button>
    </div>

    <section class="grid" id="grid">
""")



def input_variables (row, track_name, url, file_path, file_name):
    html_code_m1 = dedent(f"""

      <!-- Item {row} -->
      <figure class="tile">
        <figcaption class="title">
          <span class="track">{track_name}</span>
          <span class="filename"><a href="{url}" class="copy-link">{file_name}</a></span>
        </figcaption>
        <audio controls preload="metadata" src="{file_path}"></audio>
      </figure>

""")
    return html_code_m1

html_code_e = dedent(f"""

    </section>
    </div>

    <script src="app.js"></script>
    </body>
    </html>


""")

with open(FileFullLog, 'w', encoding='utf-8') as FileFullLogHandler, open(HTML_file, 'a', encoding='utf-8') as HTMLFileHandler :
    print ("Log files created!")
    HTMLFileHandler.write(f"{html_code_b}\n")

    for root, dirs, files in os.walk(path):

        for file in files:
            if Searchwav in file:
                counter += 1
                counter6s + 6
                HTMLFileHandler.write(input_variables(str(counter), extract_folder_name(f"{os.path.join(root, file)}"), extract_file_path_abs(f"{os.path.join(root, file)}"), extract_file_path_rel(f"{os.path.join(root, file)}") + extract_file_name(f"{os.path.join(root, file)}"),extract_file_name(f"{os.path.join(root, file)}")))
                FileFullLogHandler.write(f"{os.path.join(root, file)}\n")
            if SearchWav in file:
                counter += 1
                HTMLFileHandler.write(input_variables(str(counter), extract_folder_name(f"{os.path.join(root, file)}"), extract_file_path_abs(f"{os.path.join(root, file)}"), extract_file_path_rel(f"{os.path.join(root, file)}") + extract_file_name(f"{os.path.join(root, file)}"),extract_file_name(f"{os.path.join(root, file)}")))
                FileFullLogHandler.write(f"{os.path.join(root, file)}\n")
            if SearchWAV in file:
                counter += 1
                HTMLFileHandler.write(input_variables(str(counter), extract_folder_name(f"{os.path.join(root, file)}"), extract_file_path_abs(f"{os.path.join(root, file)}"), extract_file_path_rel(f"{os.path.join(root, file)}") + extract_file_name(f"{os.path.join(root, file)}"),extract_file_name(f"{os.path.join(root, file)}")))
                FileFullLogHandler.write(f"{os.path.join(root, file)}\n")


    HTMLFileHandler.write(f"{html_code_e}\n")

