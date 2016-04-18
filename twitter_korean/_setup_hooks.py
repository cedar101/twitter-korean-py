from __future__ import print_function

import os.path

from distutils import log
import setuptools
from zipfile import ZipFile

#from maven.requestor import RequestException
from maven.artifact import Artifact
from maven.downloader import Downloader

from twitter_korean import JAR_DIR

artifact = Artifact(group_id='com.twitter.penguin', artifact_id='korean-text',
                    version='4.4')

def download_jar(cmdobj):
    filename = os.path.join(__name__.split('.')[0], JAR_DIR,
                            artifact.get_filename())
    dl = Downloader()
    dl.download(artifact, filename) # may raise RequestException
    with ZipFile(os.path.join(filename)) as jar:
        text_files = (filename for filename in jar.namelist()
                        if filename.endswith('.txt'))
        jar.extractall(JAR_DIR, text_files)

class DownloadJarCommand(setuptools.Command):
    __doc__ = '''Download twitter-korean-text jar file'''
    description = __doc__
    command_name = 'download_jar'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self, *args, **kwargs):
        log.info('[pbr] Downloading twitter-korean-text jar file')
        download_jar(self)
        #return setuptools.Command.run(self)


class TestCommand(setuptools.Command):
    __doc__ = 'run tests using [mamba](http://nestorsalceda.github.io/mamba/)'
    description = __doc__
    command_name = 'test'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        sys.exit(os.system('mamba -f documentation spec/*.py'))
