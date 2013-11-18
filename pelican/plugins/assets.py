# -*- coding: utf-8 -*-
"""
Asset management plugin for Pelican
===================================

This plugin is a fork of the assets pelican plugin:

https://github.com/getpelican/pelican-plugins/tree/master/assets

I have modified it so that asset bundles are now defined here using the
webassets api directly instead of defining them in the pelicanconf file.
I have also added code to process font files which I could not get
webassets to process presumable because they are not referenced directly
in the HTML templates. Additionally, I have moved away from using webassets to
gzip since it produces a new file hash each time.

"""
from __future__ import unicode_literals

import os
import gzip
import shutil
import logging

from pelican import signals
logger = logging.getLogger(__name__)

try:
    import webassets
    from webassets import Environment
    from webassets import Bundle
    from webassets.filter import get_filter
    from webassets.ext.jinja2 import AssetsExtension
except ImportError:
    webassets = None


def add_jinja2_ext(pelican):
    """Add Webassets to Jinja2 extensions in Pelican settings."""

    pelican.settings['JINJA_EXTENSIONS'].append(AssetsExtension)

def register_bundles(env):
    """Registers asset bundels"""

    style_css = Bundle(
        # Bootstrap
        Bundle('components/bootstrap/less/bootstrap.less',
            'components/bootstrap/less/responsive.less',
            filters='less',
            output='webassets-external/less-%(version)s.css'),
        # Fontawesome
        Bundle('components/font-awesome/css/font-awesome.css',
            'components/font-awesome/css/font-awesome-ie7.css',),
        # Custom css
        Bundle('css/custom.css', 'css/sticky-footer.css'),
        filters='cssmin',
        output='css/style-%(version)s.css')
    env.register('style_css', style_css)

    epicloops_logo_png = Bundle(
        'png/epicloops-logo.png',
        output='png/epicloops-logo-%(version)s.png')
    env.register('epicloops_logo_png', epicloops_logo_png)

    favicon_png = Bundle(
        'ico/favicon.png',
        output='ico/favicon-%(version)s.png')
    env.register('favicon_png', favicon_png)

    icon_114_precomposed_png = Bundle(
        'ico/apple-touch-icon-114-precomposed.png',
        output='ico/apple-touch-icon-114-precomposed-%(version)s.png')
    env.register('icon_114_precomposed_png',
        icon_114_precomposed_png)

    icon_144_precomposed_png = Bundle(
        'ico/apple-touch-icon-144-precomposed.png',
        output='ico/apple-touch-icon-144-precomposed-%(version)s.png')
    env.register('icon_144_precomposed_png',
        icon_144_precomposed_png)

    icon_57_precomposed_png = Bundle(
        'ico/apple-touch-icon-57-precomposed.png',
        output='ico/apple-touch-icon-57-precomposed-%(version)s.png')
    env.register('icon_57_precomposed_png',
        icon_57_precomposed_png)

    icon_72_precomposed_png = Bundle(
        'ico/apple-touch-icon-72-precomposed.png',
        output='ico/apple-touch-icon-72-precomposed-%(version)s.png')
    env.register('icon_72_precomposed_png',
        icon_72_precomposed_png)

def process_webassets(generator):
    """Define the assets environment and pass it to the generator."""

    generator.env.assets_environment = Environment()

    assets_url = 'static/'
    generator.env.assets_environment.url = assets_url
    generator.env.assets_environment.directory = \
        os.path.join(generator.output_path, assets_url)

    assets_src = os.path.join(generator.theme, 'static')
    generator.env.assets_environment.load_path = [assets_src]

    generator.env.assets_environment.versions = 'hash:32'

    if logging.getLevelName(logger.getEffectiveLevel()) == "DEBUG":
        generator.env.assets_environment.debug = True

    register_bundles(generator.env.assets_environment)

def rm_src_files(pelican):
    """Remove the source files that get copied over. We are only interested in
    the optimized output."""
    shutil.rmtree('output/static/src')

def copy_fonts(pelican):
    """Copy font files to output dir since they are not processed by webassets.

    Webassets is not processing font files presumably because they
    are not referenced in the HTML templates"""

    font_dirs = [
        'theme/static/components/font-awesome/font',
    ]

    font_filepaths = []
    for path in font_dirs:
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                font_filepaths.append(filepath)

    for in_filepath in font_filepaths:
        basename = os.path.basename(in_filepath)
        out_filepath = os.path.join('output/static/font', basename)

        if not os.path.exists(os.path.dirname(out_filepath)):
            os.makedirs(os.path.dirname(out_filepath))

        shutil.copyfile(in_filepath, out_filepath)

def copy_jpgs(pelican):
    """Copy jpgs to output dir since they are not processed by webassets.

    Webassets is not processing jpgs that are only referenced in css presumably
    because they are not referenced in the HTML templates"""

    jpg_dirs = [
        'theme/static/jpg',
    ]

    jpg_filepaths = []
    for path in jpg_dirs:
        for dirpath, _, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                jpg_filepaths.append(filepath)

    for in_filepath in jpg_filepaths:
        basename = os.path.basename(in_filepath)
        out_filepath = os.path.join('output/static/jpg', basename)

        if not os.path.exists(os.path.dirname(out_filepath)):
            os.makedirs(os.path.dirname(out_filepath))

        shutil.copyfile(in_filepath, out_filepath)

def gzip_files(pelican):
    """Gzip files.

    We are not using webassets to gzip because webassets hashes the file after
    gzip. This produces a new hash each time and makes it look like the file
    has changed when it has not."""
    if logging.getLevelName(logger.getEffectiveLevel()) == "DEBUG":
        return
    gzip_extensions = [
        '.css',
        '.js',
        '.html',
        '.xml',
        '.eot',
        '.svg',
        '.ttf',
        '.woff',
        '.otf',
    ]
    for dirpath, _, filenames in os.walk(pelican.settings['OUTPUT_PATH']):
        for filename in filenames:
            if os.path.splitext(filename)[1] not in gzip_extensions:
                continue
            else:
                filepath = os.path.join(dirpath, filename)
                compressed_path = filepath + '.gz'
                with open(filepath, 'rb') as uncompressed:
                    try:
                        logger.debug('Compressing: %s' % filepath)
                        compressed = gzip.open(compressed_path, 'wb', 9)
                        compressed.writelines(uncompressed)
                    except Exception as ex:
                        logger.critical('Gzip compression failed: %s' % ex)
                    finally:
                        compressed.close()
                os.remove(filepath)
                os.rename(compressed_path, filepath)

def register():
    """Plugin registration."""
    if webassets:
        signals.initialized.connect(add_jinja2_ext)
        signals.generator_init.connect(process_webassets)
        signals.finalized.connect(rm_src_files)
        signals.finalized.connect(copy_fonts)
        signals.finalized.connect(copy_jpgs)
        signals.finalized.connect(gzip_files)
    else:
        logger.warning('`assets` failed to load dependency `webassets`.'
                       '`assets` plugin not loaded.')
