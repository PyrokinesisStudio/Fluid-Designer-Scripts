from . nodetree import NodeTree
from . texture import Texture
from . imagepreview import ImagePreview
from . id import ID
from . struct import Struct
from . cycleslampsettings import CyclesLampSettings
from . library import Library
from . animdata import AnimData
from . lamptextureslots import LampTextureSlots
from . bpy_struct import bpy_struct
import mathutils

class Lamp(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String) Unique datablock ID name'''
        return str()
    @property
    def users(self):
        '''(Integer) Number of times this datablock is referenced'''
        return int()
    @property
    def use_fake_user(self):
        '''(Boolean) Save this datablock even if it has no users'''
        return bool()
    @property
    def tag(self):
        '''(Boolean) Tools can use this to tag data for their own purposes
        (initial state is undefined)'''
        return bool()
    @property
    def is_updated(self):
        '''(Boolean) Datablock is tagged for recalculation'''
        return bool()
    @property
    def is_updated_data(self):
        '''(Boolean) Datablock data is tagged for recalculation'''
        return bool()
    @property
    def is_library_indirect(self):
        '''(Boolean) Is this ID block linked indirectly'''
        return bool()
    @property
    def library(self):
        '''(Library) Library file the datablock is linked from'''
        return Library()
    @property
    def preview(self):
        '''(ImagePreview) Preview image and icon of this datablock (None if not
        supported for this type of data)'''
        return ImagePreview()
    @property
    def type(self):
        '''(Enum) Type of Lamp
        
        [POINT, SUN, SPOT, HEMI, AREA]'''
        return str()
    @property
    def distance(self):
        '''(Float) Falloff distance - the light is at half the original intensity
        at this point'''
        return float()
    @property
    def energy(self):
        '''(Float) Amount of light that the lamp emits'''
        return float()
    @property
    def color(self):
        '''(Vector 3D) Light color'''
        return mathutils.Vector()
    @property
    def use_own_layer(self):
        '''(Boolean) Illuminate objects only on the same layers the lamp is on'''
        return bool()
    @property
    def use_negative(self):
        '''(Boolean) Cast negative light'''
        return bool()
    @property
    def use_specular(self):
        '''(Boolean) Create specular highlights'''
        return bool()
    @property
    def use_diffuse(self):
        '''(Boolean) Do diffuse shading'''
        return bool()
    @property
    def node_tree(self):
        '''(NodeTree) Node tree for node based lamps'''
        return NodeTree()
    @property
    def use_nodes(self):
        '''(Boolean) Use shader nodes to render the lamp'''
        return bool()
    @property
    def animation_data(self):
        '''(AnimData) Animation data for this datablock'''
        return AnimData()
    @property
    def texture_slots(self):
        '''(Sequence of LampTextureSlot) Texture slots defining the mapping and
        influence of textures'''
        return LampTextureSlots()
    @property
    def active_texture(self):
        '''(Texture) Active texture slot being displayed'''
        return Texture()
    @property
    def active_texture_index(self):
        '''(Integer) Index of active texture slot'''
        return int()
    @property
    def cycles(self):
        '''(CyclesLampSettings) Cycles lamp settings'''
        return CyclesLampSettings()
    def copy(self):
        '''Create a copy of this datablock (not supported for all datablocks)
        
        Returns:
          id: (ID) New copy of the ID'''
        return ID()
    def user_clear(self):
        '''Clear the user count of a datablock so its not saved, on reload the
        data will be removed'''
        return 
    def animation_data_create(self):
        '''Create animation data to this ID, note that not all ID types support
        this
        
        Returns:
          anim_data: (AnimData) New animation data or NULL'''
        return AnimData()
    def animation_data_clear(self):
        '''Clear animation on this this ID'''
        return 
    def update_tag(self, refresh):
        '''Tag the ID to update its display data, e.g. when calling
        :class:`bpy.types.Scene.update`
        
        Parameter:
          refresh: (Enum) Type of updates to perform'''
        return 