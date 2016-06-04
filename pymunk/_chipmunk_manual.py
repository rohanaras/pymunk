from collections import namedtuple

class ShapeFilter(namedtuple("ShapeFilter", ['group', 'categories', 'mask'])):
    """
    
    Chipmunk has two primary means of ignoring collisions: groups and 
    category masks.

    Groups are used to ignore collisions between parts on a complex object. A 
    ragdoll is a good example. When jointing an arm onto the torso, you'll 
    want them to allow them to overlap. Groups allow you to do exactly that. 
    Shapes that have the same group don't generate collisions. So by placing 
    all of the shapes in a ragdoll in the same group, you'll prevent it from 
    colliding against other parts of itself. Category masks allow you to mark 
    which categories an object belongs to and which categories it collidies 
    with.

    For example, a game has four collision categories: player (0), enemy (1), 
    player bullet (2), and enemy bullet (3). Neither players nor enemies 
    should not collide with their own bullets, and bullets should not collide 
    with other bullets. However, players collide with enemy bullets, and 
    enemies collide with player bullets.

    ============= =============== =============
    Object        Object Category Category Mask
    ============= =============== =============
    Player        1               4, 5       
    Enemy         2               2, 3, 4
    Player Bullet 3               1, 5
    Enemy Bullet  4               2, 5
    Walls         5               1, 2, 3, 4
    ============= =============== =============
    
    Note that everything in this example collides with walls. Additionally, 
    the enemies collide with eachother.

    By default, objects exist in every category and collide with every category.

    Objects can fall into multiple categories. For instance, you might have a 
    category for a red team, and have a red player bullet. In the above 
    example, each object only has one category. If you make use of multiple 
    categories on an object, you may also wish to consider replacing the 
    ShapeFilter class and the cpShapeFilterReject() function in 
    chipmunk_private.h to customize it to better suit your game's needs.

    The default type of categories and mask in ShapeFilter is unsigned int 
    which has a resolution of 32 bits on most systems. You can redefine 
    cpBitmask in chipmunk_types.h if you need more bits to work with.

    There is one last way of filtering collisions using collision handlers. 
    See the section on callbacks for more information. Collision handlers can 
    be more flexible, but can be slower. Fast collision filtering rejects 
    collisions before running the expensive collision detection code, so 
    using groups or category masks is preferred.

    """
    __slots__ = ()    

    def __new__(cls, group = 0, categories = 0xffffffff, mask = 0xffffffff):
        self = super(ShapeFilter, cls).__new__(cls, group, categories, mask)
        return self

from . import _chipmunk_cffi
cp = _chipmunk_cffi.lib
ffi = _chipmunk_cffi.ffi
from .vec2d import Vec2d


class Transform(namedtuple('Transform', ['a','b','c','d','tx','ty'])):
    """Type used for 2x3 affine transforms.
    
    See wikipedia for details: 
    http://en.wikipedia.org/wiki/Affine_transformation
    
    The properties map to the matrix in this way: 
    
    = = ==
    = = ==
    a c tx
    b d ty
    = = ==
        
    An instance can be created in this way::
        >>> Transform(1,2,3,4,5,6)
        Transform(a=1, b=2, c=3, d=4, tx=5, ty=6)
    Or using the default identity in this way::
        >>> Transform.identity()
        Transform(a=1, b=0, c=0, d=1, tx=0, ty=0)
    Or overriding only some of the values (on a identity matrix):
        >>> Transform(b=3,ty=5)
        Transform(a=1, b=3, c=0, d=1, tx=0, ty=5)
    
        
    """
    __slots__ = ()
    
    def __new__(cls, a=1, b=0, c=0, d=1, tx=0, ty=0):
        self = super(Transform, cls).__new__(cls, a, b, c, d, tx, ty)
        return self
    
    @staticmethod
    def identity():
        """The identity transform"""
        return Transform(1,0,0,1,0,0)
