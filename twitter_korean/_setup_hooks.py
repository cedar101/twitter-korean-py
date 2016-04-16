from __future__ import print_function

import os.path

from distutils import log
#from distutils.command import build_py
import setuptools

from twitter_korean import JAR_DIR

VERSION = '4.4'

def download_jar(cmdobj):
    from maven.requestor import RequestException
    from maven.artifact import Artifact
    from maven.downloader import Downloader

    artifact = Artifact('com.twitter.penguin', 'korean-text', VERSION)
    filename = os.path.join(__name__.split('.')[0], JAR_DIR,
                            artifact.get_filename())
    dl = Downloader()
    try:
        dl.download(artifact, filename)
    except RequestException as e:
        print(e.msg)


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
