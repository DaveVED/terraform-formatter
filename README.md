# terraform-formatter
Python CLI provding terraform file manipulation (formating) functionality. Allowing you to format and write valid terraform files using `python`. Something that is typically only achievable in `go`. 

If you just just want to use the code to format and write a terraform file without the cli, you can check out the `./tf/terraform/writter.tf` file. 

* currently only supports, `*.tf` files with only variable blocks.
## Functionality
This CLI allows your to.
- [x] Pass in a argument defining what type of file manipulation you would like. 
    - [x] `./tfw/main.py sort` - Sort a file in alphabetical (or reverse) order
- [x] Read in one ore more files and store them in a python readable `TerraformFile` object.
    - [x] `./tfw/main.py sort -file file1 file2` - User provided files
- [x] Validates all files passed in for formatting are valid `*.tf` files.

## Usage.

```
    # Sort user provided files.
    ./tf/main.py sort -file test/files/easy-files/easy1.tf test/files/easy-files/easy2.tf

```
