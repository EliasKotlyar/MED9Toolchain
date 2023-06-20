# Med9Toolchain

The Med9Toolchain is a command-line application that allows you to apply patches to a binary file. 
Its basically a Toolset for your MED9.X ECU, which is able to "patch" functionality in.
It provides a set of functionalities to write patches in C language, and then apply them automatically to any binary provided.

## How does this tool work?

Refer please to FAQ.md


## Installation on Windows

1. Install Python 3.X for Windows

   ```bash
   https://www.python.org/downloads/windows/
   ```
2. Install PowerPC GCC compiler for Windows

   ```bash
   https://gnutoolchains.com/powerpc-eabi/
   ```
   
3. Clone the repository:

   ```bash
   git clone <repository-url>
   ```


4. Navigate to the project directory:

```bash
   cd med9toolchain
   ```


5. Install the required dependencies:

    
```bash
   pip install -r requirements.txt
   ```

## Usage


```bash
python med9toolchain.py [-h] [-o OUTPUTFILE] inputfile [patches [patches ...]]
   ```


Arguments

    inputfile: Path to the input file. This is the file to which the patches will be applied.
    patches: List of patches to apply. Choose from the available patches.

Options

    -h, --help: Show the help message and exit.
    -o OUTPUTFILE, --outputfile OUTPUTFILE: Path to the output file. If not provided, the output file will be named inputfile_MOD.bin.

Example

To apply the sample "mapswitch" to an input file, run the following command:


```bash
python med9toolchain.py testfile.bin mapswitch_ldrxn
   ```

This command applies mapswitch to the input.bin file. The output file input.bin_MOD.bin will be generated with the applied patches.

Note: Make sure the input file exists in the specified path, and the patches are valid.



# License

This project is licensed under the MIT License.
