import bpy
from bpy_extras.object_utils import world_to_camera_view


def extract_vertices(obj, cam):
    """Extract vertices oj an object in camera space."""
    scene = bpy.context.scene
    render = scene.render
    res_x = render.resolution_x
    res_y = render.resolution_y

    verts = (obj.matrix_world * vert.co for vert in obj.data.vertices)
    coords_2d = [world_to_camera_view(scene, cam, coord) for coord in verts]

    rnd = lambda i: round(i)
    return ((rnd(res_x*x), rnd(res_y*y), distance_to_lens) for x, y, distance_to_lens in coords_2d)
