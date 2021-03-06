from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class RenderSlot(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Render slot name'''
        return str()