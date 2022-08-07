bl_info = {
    "name": "canvas flipping and rotation simulation",
    "author": "Alexander Mehler (Ulf3000)",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "operators",
    "description": "Adds a few Operators to simulate canvas flipping and rotation from painting programs with blenders camera view",
    "warning": "the script uses the delta transforms of the camera as a hack, so if you are using the delta transforms for your camera rig or any other reason this addon os not the right solution for you",
    "doc_url": "https://github.com/Ulf3000/Blender-Timing-Tools",
    "category": "global",
}

import bpy 

class Rotate_camera_delta_clockwise(bpy.types.Operator):
    bl_idname = "camera.rotate_right"
    bl_label = "rotate camera 15° clockwise"
    
    def execute(self, context):

        bpy.context.scene.camera.delta_rotation_euler[1] = bpy.context.scene.camera.delta_rotation_euler[1] - 0.262 # 0.262 = 15°

        if bpy.context.scene.camera.delta_rotation_euler[1] <= -6.2831854820251465:
            bpy.context.scene.camera.delta_rotation_euler[1] = 0
        return {'FINISHED'}
            
class Rotate_camera_delta_counterclockwise(bpy.types.Operator):
    bl_idname = "camera.rotate_left"
    bl_label = "rotate camera 15° counterclockwise"
    
    
    def execute(self, context):

        bpy.context.scene.camera.delta_rotation_euler[1] = bpy.context.scene.camera.delta_rotation_euler[1] + 0.262 # 0.262 = 15°

        if bpy.context.scene.camera.delta_rotation_euler[1] >= 6.2831854820251465: # = 360°
            bpy.context.scene.camera.delta_rotation_euler[1] = 0
        return {'FINISHED'}

class Reset_camera_delta_rotation(bpy.types.Operator):
    bl_idname = "camera.reset_camera_delta_rotation"
    bl_label = "Flip camera view"
    
    def execute(self, context):
        bpy.context.scene.camera.delta_rotation_euler[1] = 0   
        return {'FINISHED'}

class Flip_camera_delta_Y(bpy.types.Operator):
    bl_idname = "camera.flip_camera"
    bl_label = "Flip camera view"
    
    def execute(self, context):
        bpy.context.scene.camera.delta_scale[0] = bpy.context.scene.camera.delta_scale[0] * (-1)    
        return {'FINISHED'}

def register():
    bpy.utils.register_class(Rotate_camera_delta_clockwise)
    bpy.utils.register_class(Rotate_camera_delta_counterclockwise)
    bpy.utils.register_class(Reset_camera_delta_rotation)
    bpy.utils.register_class(Flip_camera_delta_Y)
    
def unregister():
    bpy.utils.unregister_class(Rotate_camera_clockwise)
    
if __name__ == "__main__":
    register()