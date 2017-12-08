# FontAwesome 3 to 4
**A small Python tool to migrate from FontAwesome 3 to 4**

FontAwesome 3 to 4 is brought to you by Giovdi by Pixelstyle.it.

A FontAwesome 4 to 5 version is also available at [https://github.com/giovdi/fontawesome-4-to-5](https://github.com/giovdi/fontawesome-4-to-5)

## How to use it
In `main.py` you can define the file or the folders you want to check.  
Use `pathCheck` to check every file into a folder or `fileCheck` to check a single file.

For example:
```
# For Windows users
FontAwesome3To4.pathCheck("C:/path/to/folder", True)
FontAwesome3To4.fileCheck("C:/path/to/file.php", True)
# For Unix users
FontAwesome3To4.pathCheck("/path/to/folder", True)
FontAwesome3To4.fileCheck("/path/to/file.php", True)
```

The first parameter is a folder or a file to convert, the second one, if True, creates a .bak file for each file analyzed.

To quickly use this tool, feel free to change `main.py` with your paths and files.  
You can also use `from fontawesome3to4 import FontAwesome3To4` to use this library in your projects.

## Eclipse integration
You can import this project into your Eclipse workspace to easly use the library standalone.

## Requirements
The script uses Python 2.7 to work