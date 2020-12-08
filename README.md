# cgi-Python-Xampp

### Requirements
  1. install Python3
  2. get Path of executable by typing `where python` in CMD (Win10)

### Instruction for Xampp configuration
  1. #### Add .py extention
      - find the line `AddHandler cgi-script .cgi .pl .asp` by searching for `.asp`
      - add `.py`  
      - finished line: `AddHandler cgi-script .cgi .pl .asp .py`
  2. #### Place files
      - copy echo.py to the `cgi-bin` directory and **update python path in the first line of the file**  
      - copy .html .css files to `htdocs` directory
  3. #### Start Apache
