# s1tolua
Python script that automates the process of importing Sonic 1 Level information into Roblox using the the Sonic 1 disassembly.

# How to use
As of v1.2b, no third party libraries are required. <br>
You'll need the [Sonic 1 disassembly](https://github.com/sonicretro/s1disasm), and Python 3 installed (Tested with 3.12.5 only as of now) <br>
There's two modes as of v1.2b:
- Level Layout ripper (-l) (v1.0b)
  1. Place a file from the `levels` folder of the Sonic 1 Disassembly in the same folder (or subfolders)
  2. Open a Command Prompt or Terminal
  3. Run `python3 s1tolua.py -l <filename> <outputfilename>`
- Chunk Data ripper (-c) (v1.2b)
  1. Place a file from the `map256` folder of the Sonic 1 Disassembly in the same folder (or subfolders)
  2. Uncompress it using a Kosinski Compressor (the one I use is `koscmp.exe` from [mdcomp](https://github.com/flamewing/mdcomp))
  3. Open a Command Prompt or Terminal
  4. Run `python3 s1tolua.py -c <filename> <outputfilename>`

# Notes
- I'm not very good at Python, and I'm pretty sure it's a bit wrong, but yeah, still a work in progress <br>
- It's intended for use in a Roblox Classic Sonic Framework.
- This is still a WIP and I don't really know what I'm doing, for all I know this is completely wrong, but yeah.
