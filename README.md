# cgi-Python-Xampp

### Requirements
  1. install Python3
  2. get Path of executable by typing `where python3` in CMD (Win10) or `which python3` in terminal(MAC/Linux)

### Instruction for Xampp configuration
  1. #### Add .py extention
      - find the line `AddHandler cgi-script .cgi .pl .asp` by searching for `.asp`
      - add `.py`  
      - finished line: `AddHandler cgi-script .cgi .pl .asp .py`
      - save and close
  2. #### Place files
      - copy echo.py to the `cgi-bin` directory and **update python path in the first line of the file**  
      - copy .html .css files to `htdocs` directory
  3. #### Start Apache
  
  
### for different directories
  1. search:  
        <Directory "/xampp/htdocs">  
          ...  
          Options Indexes FollowSymLinks Includes ExecCGI  
          ...  
        </Directory>
  2. make sure `ExecCGI` is there
