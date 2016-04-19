import sys
import os.path
from zipfile import ZipFile

from distutils import log
from distutils.command.install_data import install_data
import setuptools

import six
# if six.PY3:
#     from past import autotranslate
#     autotranslate(['maven', 'maven.requestor', 'maven.downloader'])

module_name = __name__.split('.')[0]
#JAR_PATH = os.path.join(module_name, JAR_DIR)

artifact_info = {'group_id': 'com.twitter.penguin', 'artifact_id': 'korean-text',
                 'version': '4.4'}

def download_jar(cmdobj):
    '''Download and extract twitter-korean-text jar file'''
    log.info('[pbr] Downloading twitter-korean-text jar file')

    if six.PY2:
        from maven.artifact import Artifact
        from maven.downloader import Downloader

        artifact = Artifact(**artifact_info)
        dl = Downloader()
        dl.download(artifact) # may raise RequestException or IOError
        jar_path = artifact.get_filename()
    else:   # six.PY3
        # maven-artifact is not compatible with python 3
        # install and execute mvn
        os.system(
            'mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:get'
            ' -Dartifact={group_id}:{artifact_id}:{version}'.format(**artifact_info)
        )
        jar_path = os.path.join('~/.m2/repository',
                                artifact_info.group_id.replace('.', '/'),
                                artifact_info.artifact_id,
                                artifact_info.version,
                                '{artifact_id}-{version}.jar'.format(**artifact_info))

    with ZipFile(jar_path) as jar:
        text_files = (filename for filename in jar.namelist()
                        if filename.endswith('.txt'))
        jar.extractall(module_name, text_files)

class DownloadJarCommand(setuptools.Command):
    __doc__ = download_jar.__doc__
    description = __doc__
    command_name = 'download_jar'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        download_jar(self)


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
        self.run_command('download_jar')
        sys.exit(os.system('mamba -f documentation spec/*.py'))
