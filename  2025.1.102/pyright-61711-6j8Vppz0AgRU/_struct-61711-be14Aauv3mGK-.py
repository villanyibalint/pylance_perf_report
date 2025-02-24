# Python: 3.12.3 (main, Feb  4 2025, 14:48:35) [GCC 13.3.0]
# Library: _struct, version: unspecified
# Module: _struct, version: unspecified

"Functions to convert between Python values and C structs.\nPython bytes objects are used to hold the data representing the C struct\nand also as format strings (explained below) to describe the layout of data\nin the C struct.\n\nThe optional first format char indicates byte order, size and alignment:\n  @: native order, size & alignment (default)\n  =: native order, std. size & alignment\n  <: little-endian, std. size & alignment\n  >: big-endian, std. size & alignment\n  !: same as >\n\nThe remaining chars indicate types of args and must match exactly;\nthese can be preceded by a decimal repeat count:\n  x: pad byte (no data); c:char; b:signed byte; B:unsigned byte;\n  ?: _Bool (requires C99; if not available, char is used instead)\n  h:short; H:unsigned short; i:int; I:unsigned int;\n  l:long; L:unsigned long; f:float; d:double; e:half-float.\nSpecial cases (preceding decimal count indicates length):\n  s:string (array of char); p: pascal string (with count byte).\nSpecial cases (only available in native format):\n  n:ssize_t; N:size_t;\n  P:an integer type that is wide enough to hold a pointer.\nSpecial case (not in native mode unless 'long long' in platform C):\n  q:long long; Q:unsigned long long\nWhitespace between formats is ignored.\n\nThe variable struct.error is an exception raised on errors.\n"

import typing
import builtins as _mod_builtins
import struct as _mod_struct

class Struct(_mod_builtins.object):
    'Struct(fmt) --> compiled struct object\n\n'
    def __delattr__(self, name) -> None:
        'Implement delattr(self, name).'
        ...
    
    def __getattribute__(self, name) -> typing.Any:
        'Return getattr(self, name).'
        ...
    
    def __init__(self, fmt) -> None:
        'Struct(fmt) --> compiled struct object\n\n'
        ...
    
    @classmethod
    def __init_subclass__(cls) -> None:
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        ...
    
    __module__: str
    def __setattr__(self, name, value) -> None:
        'Implement setattr(self, name, value).'
        ...
    
    def __sizeof__(self) -> int:
        'S.__sizeof__() -> size of S in memory, in bytes'
        ...
    
    @classmethod
    def __subclasshook__(cls, subclass: typing.Any) -> bool:
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        ...
    
    @property
    def format(self) -> typing.Any:
        'struct format string'
        ...
    
    def iter_unpack(self, buffer) -> typing.Any:
        'Return an iterator yielding tuples.\n\nTuples are unpacked from the given bytes source, like a repeated\ninvocation of unpack_from().\n\nRequires that the bytes length be a multiple of the struct size.'
        ...
    
    def pack(self) -> typing.Any:
        'S.pack(v1, v2, ...) -> bytes\n\nReturn a bytes object containing values v1, v2, ... packed according\nto the format string S.format.  See help(struct) for more on format\nstrings.'
        ...
    
    def pack_into(self) -> typing.Any:
        'S.pack_into(buffer, offset, v1, v2, ...)\n\nPack the values v1, v2, ... according to the format string S.format\nand write the packed bytes into the writable buffer buf starting at\noffset.  Note that the offset is a required argument.  See\nhelp(struct) for more on format strings.'
        ...
    
    @property
    def size(self) -> typing.Any:
        'struct size in bytes'
        ...
    
    def unpack(self, buffer) -> typing.Any:
        "Return a tuple containing unpacked values.\n\nUnpack according to the format string Struct.format. The buffer's size\nin bytes must be Struct.size.\n\nSee help(struct) for more on format strings."
        ...
    
    def unpack_from(self, buffer, offset) -> typing.Any:
        "Return a tuple containing unpacked values.\n\nValues are unpacked according to the format string Struct.format.\n\nThe buffer's size in bytes, starting at position offset, must be\nat least Struct.size.\n\nSee help(struct) for more on format strings."
        ...
    
    def __getattr__(self, name) -> typing.Any:
        ...
    

__doc__: str
__name__: str
__package__: str
def _clearcache() -> typing.Any:
    'Clear the internal cache.'
    ...

def calcsize(format) -> typing.Any:
    'Return size in bytes of the struct described by the format string.'
    ...

error = _mod_struct.error
def iter_unpack(format, buffer) -> typing.Any:
    'Return an iterator yielding tuples unpacked from the given bytes.\n\nThe bytes are unpacked according to the format string, like\na repeated invocation of unpack_from().\n\nRequires that the bytes length be a multiple of the format struct size.'
    ...

def pack() -> typing.Any:
    'Return a bytes object containing the values v1, v2, ... packed according\nto the format string.  See help(struct) for more on format strings.'
    ...

def pack_into() -> typing.Any:
    'Pack the values v1, v2, ... according to the format string and write\nthe packed bytes into the writable buffer buf starting at offset.  Note\nthat the offset is a required argument.  See help(struct) for more\non format strings.'
    ...

def unpack(format, buffer) -> typing.Any:
    "Return a tuple containing values unpacked according to the format string.\n\nThe buffer's size in bytes must be calcsize(format).\n\nSee help(struct) for more on format strings."
    ...

def unpack_from(format, buffer, offset) -> typing.Any:
    "Return a tuple containing values unpacked according to the format string.\n\nThe buffer's size, minus offset, must be at least calcsize(format).\n\nSee help(struct) for more on format strings."
    ...

def __getattr__(name) -> typing.Any:
    ...

