import bpy

_myName = input("Set your Name: ")
bpy.ops.mesh.primitive_cube_add(location = (0, 4, 0))
_cube = bpy.context.object
_cube.name = _myName
bpy.ops.wm.save_mainfile()
