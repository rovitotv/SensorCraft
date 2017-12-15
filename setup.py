from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='sensorcraft',
    version='1.8.0',
    long_description=readme(),
    description='Programming exercises to inspire kids to learn to program in a Minecraft type environment',
    url='https://github.com/rovitotv/sensorcraft',
    author='Todd Rovito, Adam Mitchell, and Eli Rovito',
    author_email='rovitotv@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Education :: Computer Aided Instruction (CAI)',
    ],
    keywords='education minecraft python sensor afrl',
    packages=['sensorcraft', 'docs'],
    include_package_data=True,
        package_data={
            'sensorcraft':
                ['composite_textures.png',
                'composite_world.pkl',
                'ipython.html',
                'mob_textures.png',
                'nmusaf_textures.png',
                'nmusaf.pkl',
                'numbered_textures.png',
                'rocket.pkl',
                'texture.png'
                ],
            'images':
                ['images/BlockSelectionInLabel.png',
                'images/building_automatically_great_wall.png',
                'images/building_automatically_pyramid.png',
                'images/canopy_attribute_error.jpg',
                'images/canopy_change_directory.jpg',
                'images/canopy_edit_main,jpg',
                'images/canopy_editor_tab_error.jpg',
                'images/canopy_kernel_restart_menu.jpg',
                'images/canopy_pyglet_install.jpg',
                'images/canopy_pyglet_upgrade.jpg',
                'images/canopy_pyglet_version,jpg',
                'images/canopy_welcome.jpg',
                'images/CanopyExpress1.7.jpg',
                'images/CanopyExpress2.jpg',
                'images/CanopyExpressDownload.jpg',
                'images/fps_and_coords_text,jpg',
                'images/NMUSAF.png',
                'images/Rocket.png',
                'images/sensorcraft_lab_coat_small,jpg',
                'images/sensorcraft_lab_coat_smallest.jpg',
                'images/sensorcraft_lab_coat.bmp',
                'images/sensorcraft_lab_coat.jpg',
                'images/sensorcraft_lab_coat.png',
                'images/sensorcraft.bmp',
                'images/sensorcraft.jpg',
                'images/sensorcraft.pdf',
                'images/Mob.png'
                ],
},
    install_requires=[
        'pyglet',
    ],
    zip_safe=False)