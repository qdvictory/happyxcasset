# Happyxcasset
`Happyxcasset` is a python script that easily imports resource files into xcassets in Xcode.   
It is easy and efficient.
No longer appear annoying `-1 -2 -3`   
It will not appear to replace the resources to wait for several minutes of embarrassment.   
Then let's use it.   
In advance is your machine installed python (2 | 3), very pleased that mac os comes with python.   
### Shell   
`python xcodexcassets.py -i <inputfile> -o <outputfile>`   
`-i` The resource's input directory can contain subfolders   
`-o` The output directory of the resource, which is the directory of the .xcasset in Xcode   
`-h` Help

If you do not want to enter long long python command every time, then simply set it up:
### Open file   
`vi ~ / .bash_profile`   
### Add line    
`alisa happyxcasset = "python /Users/<pathto>/xcodexcassets.py"` 
### Save
`source ~ / .bash_profile`     
### Use   
`happyxcasset -h`   