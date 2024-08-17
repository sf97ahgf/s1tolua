# s1tolua
Python script that automates the process of importing Sonic 1 Level information into Roblox using the the Sonic 1 disassembly.

# How to use
As of v1.0.0, no third party libraries are required. <br>
Simply place `s1tolua.py` somewhere, and place any of the files from the `levels` folder of the [Sonic 1 disassembly](https://github.com/sonicretro/s1disasm) <br>
Then open a command prompt and type `python3 s1tolua.py <file> <output filename>` (e.g. `python3 s1tolua.py ghz1.bin ghz1.lua`)

# Notes
- I'm not very good at Lua and right now this isn't really tested for accuracy, it's still a work in progress and probably spits out garbage data right now. <br>
- It's intended for use in a Roblox Classic Sonic Framework.
- This is still a WIP and I don't really know what I'm doing, for all I know this is completely wrong, but yeah.
