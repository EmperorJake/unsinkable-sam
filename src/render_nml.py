#!/usr/bin/env python

print("[RENDER NML] render_nml.py")

import codecs # used for writing files - more unicode friendly than standard open() module

import sys
import os
currentdir = os.curdir

import unsinkable_sam
import utils
import global_constants
from rosters import registered_rosters

# get args passed by makefile
repo_vars = utils.get_repo_vars(sys)

from chameleon import PageTemplateLoader # chameleon used in most template cases
# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, 'src', 'templates'))

def render_header_item_nml(header_item, consists):
    template = templates[header_item + '.pynml']
    return utils.unescape_chameleon_output(template(consists=consists,
                                                    global_constants=global_constants,
                                                    utils=utils,
                                                    registered_rosters=registered_rosters,
                                                    repo_vars=repo_vars))

def render_consist_nml(consist):
    result = utils.unescape_chameleon_output(consist.render())
    # write the nml per vehicle to disk, it aids debugging
    consist_nml = codecs.open(os.path.join('generated', 'nml', consist.id + '.nml'),'w','utf8')
    consist_nml.write(result)
    consist_nml.close()
    # also return the nml directly for writing to the concatenated nml, don't faff around opening the generated nml files from disk
    return result

def main():
    generated_nml_path = os.path.join(unsinkable_sam.generated_files_path, 'nml')
    if not os.path.exists(generated_nml_path):
        os.mkdir(generated_nml_path) # reminder to self: inside main() to avoid modifying filesystem simply by importing module
    grf_nml = codecs.open(os.path.join('unsinkable-sam.nml'),'w','utf8')

    # 'consists' not 'ships', it makes it easier to cross-maintain this script with scripts in IH and RH
    consists = unsinkable_sam.get_ships_in_buy_menu_order()

    header_items = ['header', 'cargo_table', 'disable_default_vehicles']
    for header_item in header_items:
        grf_nml.write(render_header_item_nml(header_item, consists))

    # multiprocessing was tried here and removed as it was empirically slower in testing (due to overhead of starting extra pythons probably)
    for consist in consists:
        grf_nml.write(render_consist_nml(consist))

    grf_nml.close()

if __name__ == '__main__':
    main()
