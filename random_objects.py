import random as rand
from mathutils import Matrix

import bpy
from bpy_extras.object_utils import world_to_camera_view

from extract_vertices import extract_vertices

# Output resolution (Stereoscopic images & depthmap)
bpy.context.scene.render.resolution_x = 450
bpy.context.scene.render.resolution_y = 400

# Total number of set of stereoscopic images and depth maps
total_scene_number = 1

def CreateCube(CubeName, MatName, magn):
    bpy.ops.mesh.primitive_cube_add(location=(
        (0.3 - rand.random()) * magn, (0.3 - rand.random()) * magn, (0.3 - rand.random()) * magn))
    bpy.ops.transform.rotate(value=rand.random() * 3.14,
                             axis=(rand.random(), rand.random(), rand.random()),
                             constraint_axis=(False, False, False), constraint_orientation='GLOBAL',
                             mirror=False, proportional='DISABLED',
                             proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.material.new()
    mat1 = bpy.data.materials[MatName]
    mat1.diffuse_color = (rand.random(), rand.random(), rand.random())

    bpy.data.objects[CubeName].data.materials.append(mat1)


def CreateCone(ConeName, MatName, magn):
    bpy.ops.mesh.primitive_cone_add(location=(
        (0.5 - rand.random()) * magn, (0.4 - rand.random()) * magn, (0.6 - rand.random()) * magn))
    bpy.ops.transform.rotate(value=rand.random() * 3.14,
                             axis=(rand.random(), rand.random(), rand.random()),
                             constraint_axis=(False, False, False), constraint_orientation='GLOBAL',
                             mirror=False, proportional='DISABLED',
                             proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.material.new()
    mat1 = bpy.data.materials[MatName]
    mat1.diffuse_color = (rand.random(), rand.random(), rand.random())

    bpy.data.objects[ConeName].data.materials.append(mat1)


def CreateTorus(TorusName, MatName, magn):
    bpy.ops.mesh.primitive_torus_add(location=(
        (0.35 - rand.random()) * magn, (0.55 - rand.random()) * magn, (0.45 - rand.random()) * magn))
    bpy.ops.transform.rotate(value=rand.random() * 3.14,
                             axis=(rand.random(), rand.random(), rand.random()),
                             constraint_axis=(False, False, False), constraint_orientation='GLOBAL',
                             mirror=False, proportional='DISABLED',
                             proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.material.new()
    mat1 = bpy.data.materials[MatName]
    mat1.diffuse_color = (rand.random(), rand.random(), rand.random())

    bpy.data.objects[TorusName].data.materials.append(mat1)


def CreateSphere(SphereName, MatName, magn):
    bpy.ops.mesh.primitive_uv_sphere_add(location=(
        (0.5 - rand.random()) * magn, (0.5 - rand.random()) * magn, (0.5 - rand.random()) * magn))
    bpy.ops.transform.rotate(value=rand.random() * 3.14,
                             axis=(rand.random(), rand.random(), rand.random()),
                             constraint_axis=(False, False, False), constraint_orientation='GLOBAL',
                             mirror=False, proportional='DISABLED',
                             proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.material.new()
    mat1 = bpy.data.materials[MatName]
    mat1.diffuse_color = (rand.random(), rand.random(), rand.random())

    bpy.data.objects[SphereName].data.materials.append(mat1)


def create_camera():
    # setup camera:
    camera = bpy.data.objects['Camera']
    # camera.select = True
    # Cam_x = 10
    # Cam_y = -3
    # Cam_z = 3
    # camera.location = (Cam_x, Cam_y, Cam_z)
    # camera.data.stereo.convergence_distance = 10000
    # camera.data.lens = 15  # (focal length)
    # camera.data.stereo.interocular_distance = 0.3
    # camera.select = False
    return camera


def create_walls():
    bpy.ops.mesh.primitive_plane_add(radius=1, enter_editmode=False, location=(7, 8, -1), rotation=(0, 0, 0), layers=(
    True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
    False, False, False, False))
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False),
                             constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED',
                             proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True),
                             constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED',
                             proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.transform.resize(value=(30, 30, 30), constraint_axis=(False, False, False), constraint_orientation='GLOBAL',
                             mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH',
                             proportional_size=1)

    bpy.ops.mesh.primitive_plane_add(radius=1, enter_editmode=False, location=(-3, -2, -1), rotation=(0, 0, 0), layers=(
    True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
    False, False, False, False))
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 1, 0), constraint_axis=(False, True, False),
                             constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED',
                             proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=3.14, axis=(0, 0, 1), constraint_axis=(False, False, True),
                             constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED',
                             proportional_edit_falloff='SMOOTH', proportional_size=1)

    bpy.ops.transform.resize(value=(30, 30, 30), constraint_axis=(False, False, False), constraint_orientation='GLOBAL',
                             mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH',
                             proportional_size=1)

    bpy.ops.mesh.primitive_plane_add(location=(3.5, 0, -5), rotation=(0, 0, 0))
    bpy.ops.transform.resize(value=(30, 30, 30), constraint_axis=(False, False, False), constraint_orientation='GLOBAL',
                             mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH',
                             proportional_size=1)

    bpy.ops.mesh.primitive_plane_add(location=(3.5, 0, 9), rotation=(0, 0, 0))
    bpy.ops.transform.resize(value=(30, 30, 30), constraint_axis=(False, False, False), constraint_orientation='GLOBAL',
                             mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH',
                             proportional_size=1)


def create_scene():
    # setup
    bpy.context.scene.use_nodes = True
    tree = bpy.context.scene.node_tree
    links = tree.links

    # setup lighting:
    light = bpy.data.objects['Lamp']
    # light.data.shadow_method = 'RAY_SHADOW'
    light.data.use_shadow = False
    light.data.energy = 5.0
    light.select = False

    camera = create_camera()

    ##################
    # Create new scene:
    ##################

    scene = bpy.context.scene
    scene.render.use_multiview = True
    # scene.render.views_format = 'STEREO_3D'
    scene.render.views_format = 'MULTIVIEW'
    rl = tree.nodes.new(type="CompositorNodeRLayers")
    composite = tree.nodes.new(type="CompositorNodeComposite")
    composite.location = 200, 0

    scene = bpy.context.scene

    # setup the depthmap calculation using blender's mist function:
    scene.render.layers['RenderLayer'].use_pass_mist = True
    # the depthmap can be calculated as the distance between objects and camera ('LINEAR'), or square/inverse square of the distance ('QUADRATIC'/'INVERSEQUADRATIC'):
    scene.world.mist_settings.falloff = 'LINEAR'
    # minimum depth:
    scene.world.mist_settings.intensity = 0.0
    # maximum depth (can be changed depending on the scene geometry to normalize the depth map whatever the camera orientation and position is):
    dist = ((camera.location[0] - (-3.22)) ** (2) + (camera.location[1] - (8.0)) ** (2) + (
                camera.location[2] - (-5.425)) ** (2)) ** (1 / 2)
    scene.world.mist_settings.depth = dist
    print(dist)

    # magnitude of the random variation of object placements:
    magn = 10

    # create objects with random location, orientation and color

    CreateCube('Cube', 'Material', magn)

    # CreateCube('Cube.001','Material.001')

    CreateCone('Cone', 'Material.001', magn)

    CreateTorus('Torus', 'Material.002', magn)

    CreateSphere('Sphere', 'Material.003', magn)

    # create walls

    return camera, links, composite, scene, rl


def render():
    camera, links, composite, scene, rl = create_scene()
    ii = 0
    Cam_x, Cam_y, Cam_z = camera.location

    while ii < 1:
        ii += 1
        Cam_y += 0.2
        # camera.location = (Cam_x, Cam_y, Cam_z)
        #################
        # Render the scene
        #################

        # ouput the depthmap:
        links.new(rl.outputs['Mist'], composite.inputs['Image'])

        scene.render.use_multiview = False

        scene.render.filepath = '/tmp/blender/Depth_map/DepthMap_' + str(ii) + '.png'
        bpy.ops.render.render(write_still=True)
        # time.sleep(0.2)
        # output the stereoscopic images:
        links.new(rl.outputs['Image'], composite.inputs['Image'])

        scene.render.use_multiview = True

        scene.render.filepath = '/tmp/blender/StereoImages/Stereoscopic_' + str(ii) + '.png'
        bpy.ops.render.render(write_still=True)
        print(list(extract_vertices(bpy.data.objects['Cube'], bpy.data.objects['Camera'])))
        print(list(extract_vertices(bpy.data.objects['Cone'], bpy.data.objects['Camera'])))
        print(list(extract_vertices(bpy.data.objects['Torus'], bpy.data.objects['Camera'])))
        print(list(extract_vertices(bpy.data.objects['Sphere'], bpy.data.objects['Camera'])))

if __name__ == '__main__':
    render()
