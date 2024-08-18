# s1tolua v1.2b
# Python script that automates the process of importing Sonic 1 Level information into Roblox using the the Sonic 1 disassembly.
# made by tedbasher3000
import os
import sys

VERSION = 'v1.2b'

def readbyte(byte):
    # reads integer byte (for chunk data)
    string = str(byte).lower().strip()
    hexonly = '0' + str(byte)[3:len(str(byte))-1]
    if len(string) > 6:
        # is a non-string hex
        return int(hexonly, 16)
    else:
        # is a character
        if len(string) == 4:
            # character
            return int(hex(ord(string[3])), 16)
        else:
            # has a \ for whatever reason (ngl it prolly gets split into 2 chars so this is wrong but help)
            return int(hex(ord(string[4])), 16)

def readbyte_bits(byte):
    # returns a byte in binary format
    scale = 16 ## equals to hexadecimal
    num_of_bits = 8
    return bin(readbyte(byte))[2:].zfill(num_of_bits)

def numbool(string):
    # converts a 0 or 1 to a lua bool (for flags)
    if string == '0':
        return 'false'
    else:
        return 'true'

def getsolidity(string):
    # gets solidity based on string (sorry if this and numbool look like yanderedev code)
    if string == '01':
        return 'Top'
    elif string == '10':
        return 'LRB'
    elif string == '11':
        return 'All'
    else:
        return 'Off'


if len(sys.argv) < 3:
    print('Usage: s1tolua.py -[l/c] <file> <output>\nMode: -l for Level Layout, -c for Chunks (Kosinski decompressed) \nfile: File to parse\noutput: File to output to')
else:
    table = '{'
    width = 0
    height = 0
    
    index = 0
    if sys.argv[1] == '-l':
        with open(sys.argv[2], "rb") as f:
            while (byte := f.read(1)):
                index = index + 1

                # parse header
                if index == 1:
                    width = readbyte(byte) + 1
                elif index == 2:
                    height = readbyte(byte) + 1
                elif index > 2:
                    # header done, parse level
                    if index == 3:
                        table = table + str(readbyte(byte))
                    else:
                        table = table + ', ' + str(readbyte(byte))

            table = table + '}'
            level = f"""--[[
    File from s1tolua {VERSION}
    Generated from: {sys.argv[2]}
    Type: Level data
    ! CAUTION ! s1tolua is *STILL* experimental!
    This file may as well be complete garbage data.
    by tedbasher3000
]]--
return {{
    Name = '{sys.argv[2]}';
    Act = 1;
    Width = {str(width)};
    Height = {str(height)};
    Chunks = {table}
}}"""
        with open(sys.argv[3], "wt") as f:
            f.write(level)
            print(f"Converted {sys.argv[2]} to {sys.argv[3]}!")

    elif sys.argv[1] == '-c':
        # parse chunk data
        chunks = '{'
        tiles = '{'
        cindex = 0
        double = True
        firstpart = None
        with open(sys.argv[2], "rb") as f:
            while (byte := f.read(1)):
                comma = ', '
                ccomma = ';'
                index = index + 1
                cindex = cindex + 1
                double = not double
                # every 512 bytes starts a new chunk
                if cindex == 513:
                    cindex = 1
                    if index == 513:
                        ccomma = ''
                    chunks = chunks + ccomma + "\n       " + tiles + "}"
                    tiles = '{'
                    
                if double == True:
                    # we are on a second byte
                    mix = firstpart + readbyte_bits(byte)
                    # parse the chunk data
                    solidity = getsolidity(mix[1:3])
                    flipy = numbool(mix[3])
                    flipx = numbool(mix[4])
                    tile = int(mix[5:16], 2)

                    # add to tiles
                    if cindex == 2:
                        comma = ''
                    tiles = tiles + comma + f"{{Solidity=\"{solidity}\",FlipY={flipy},FlipX={flipx},Tile={str(tile)}}}"
                else:
                    # we are on the first byte
                    firstpart = readbyte_bits(byte)
            chunks = chunks + '\n   }'
            chunkdata = f"""--[[
    File from s1tolua {VERSION}
    Generated from: {sys.argv[2]}
    Type: Chunk data
    ! CAUTION ! s1tolua is *STILL* experimental!
    This file may as well be complete garbage data.
    by tedbasher3000
]]--
return {{
    Name = '{sys.argv[2]}';
    Chunks = {chunks}
}}"""
        with open(sys.argv[3], "wt") as f:
            f.write(chunkdata)
            print(f"Converted {sys.argv[2]} to {sys.argv[3]}!")
                
    else:
        print("Unrecognized mode")
