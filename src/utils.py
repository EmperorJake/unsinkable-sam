import os.path
import codecs # used for writing files - more unicode friendly than standard open() module

def get_makefile_args(sys):
    # get args passed by makefile
    if len(sys.argv) > 1:
        makefile_args = {'repo_revision': sys.argv[1], 'repo_version': sys.argv[2],
                    'num_pool_workers': int(sys.argv[3]), 'roster': sys.argv[4]}
    else: # provide some defaults so templates don't explode when testing python script without command line args
        makefile_args = {'repo_revision': 0, 'repo_version': 0}
    return makefile_args

def unescape_chameleon_output(escaped_nml):
    # chameleon html-escapes some characters; that's sane and secure for chameleon's intended web use, but not wanted for nml
    # there is probably a standard module for unescaping html entities, but this will do for now
    escaped_nml = '>'.join(escaped_nml.split('&gt;'))
    escaped_nml = '<'.join(escaped_nml.split('&lt;'))
    escaped_nml = '&'.join(escaped_nml.split('&amp;'))
    return escaped_nml

def parse_base_lang():
    # expose base lang strings to python - for reuse in docs
    base_lang_file = codecs.open(os.path.join('src', 'lang', 'english.lng'), 'r','utf8')
    text = base_lang_file.readlines()
    # this is fragile, playing one line python is silly :)
    strings = dict((line.split(':',1)[0].strip(), line.split(':',1)[1].strip()) for line in text if ':' in line)
    return strings

def echo_message(message):
    # use to raise messages from templates to standard out (can't print directly from template render)
    # magically wraps these messages in ANSI colour to make them visible - they are only intended for noticeable messages, not general output
    print('\033[33m' + message + '\033[0m')