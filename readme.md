# Visual Studio Github Copilot Chat to Markdown convertor

## Usage

**Convert exported json file to markdown**

```
vschat2md your-chat.json your-chat-output.md

```

**Convert all files from the directory**

```
vschat2mdd dir_path
```

## Installation

**Step 1**:- Clone this repository.

```
git clone https://github.com/seekersingh/vschat2md
```

**Step 2**:- Navigate to cloned directory.

```
cd vschat2md
```

**Step 3**:- Make the files executable.

```
 chmod +x vschat2md.py
 chmod +x vschat2mdd.py
```

**Step 4**:- Optional. Try Converting your exported chat file.

```
./vschat2md.py your-chat.json your-chat-output.md

```

**Step 5**:- Move it to `/usr/local/bin` (or your execution path) to access from anywhere.

```
sudo cp vschat2mdd.py /usr/local/bin/vschat2md
sudo cp vschat2mdd.py /usr/local/bin/vschat2md
```

Now you can run

```
vschat2md chat.json chat.md
```

for converting single chat json file to markdown.
Or you can convert all the chat json files from the directory using

```
vschat2mdd dir_path
```

Enjoy!
