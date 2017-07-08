# Happyxcasset
`Happyxcasset` is a python script that easily imports resource files into xcassets in Xcode.   
It is easy and efficient.
No longer appear annoying `-1 -2 -3`   
It will not appear to replace the resources to wait for several minutes of embarrassment.   
Then let's use it.   
In advance is your machine installed python (2 | 3), very pleased that mac os comes with python.   
### Shell   
`python xcodexcassets.py -i <inputdir> -o <outputdir>`   
`-i` The resource's input directory can contain subfolders   
`-o` The output directory of the resource, which is the directory of the .xcasset in Xcode   
`-h` Help

old xcassets:   
>Image.xcassets/a.imageset/a.png   
Image.xcassets/a.imageset/Contents.json   
Image.xcassets/b.imageset/b.png   
Image.xcassets/b.imageset/Contents.json  
Image.xcassets/c.imageset/c.png   
Image.xcassets/c.imageset/Contents.json   

input dir:   
>resources/home/a.png     
resources/profile/c.pdf   
resources/squre/d.png   
resources/squre/e@1x.png   
resources/squre/e@2x.png   
resources/squre/e@3x.png   

output xcassets:
>Image.xcassets/a.imageset/a.png   `#update`   
Image.xcassets/a.imageset/Contents.json   `#settings before`   
Image.xcassets/b.imageset/b.png    `#old again`   
Image.xcassets/b.imageset/Contents.json   `#old again`   
~~Image.xcassets/c.imageset/c.png~~    `#delete`   
Image.xcassets/c.imageset/c.pdf    `#new insert`   
Image.xcassets/c.imageset/Contents.json   `#settings before`   
Image.xcassets/d.imageset/d.png    `#new insert`   
Image.xcassets/d.imageset/Contents.json   `#new insert`   
Image.xcassets/e.imageset/e@1x.png    `#new insert`   
Image.xcassets/e.imageset/e@2x.png    `#new insert`   
Image.xcassets/e.imageset/e@3x.png    `#new insert`   
Image.xcassets/e.imageset/Contents.json    `#new insert`   

If you do not want to enter long long python command every time, then simply set it up:
### Open file   
`vi ~ / .bash_profile`   
### Add line    
`alisa happyxcasset = "python /Users/<pathto>/xcodexcassets.py"` 
### Save
`source ~ / .bash_profile`     
### Use   
`happyxcasset -h`   