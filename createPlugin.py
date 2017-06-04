#!/usr/bin/env python3
"""This plugin creates a template plugin for RPGMakerMV style."""

import os
import sys
import textwrap

def create_file(flename):
    "Creates a file from scratch with a specified name"
    return


def write_template(flename):
    "Creates a template for a plugin"
    template = """
    //=============================================================================
    // %s.js
    //=============================================================================

    /*:
    * @author Kino
    * @plugindesc description
    *
    *
    * @help
    *
    //=============================================================================
    //  Contact Information
    //=============================================================================
    *
    * Contact me via twitter: EISKino, or on the rpg maker forums.
    * Username on forums: Kino.
    *
    * Forum Link: http://forums.rpgmakerweb.com/index.php?/profile/75879-kino/
    * Website Link: http://endlessillusoft.com/
    * Twitter Link: https://twitter.com/EISKino
    * Patreon Link: https://www.patreon.com/EISKino
    *
    * Hope this plugin helps, and enjoy!
    * --Kino
    */

    (function(){
      function setup() {

      }

      setup();
    })();
    """ % (flename)
    template = textwrap.dedent(template)
    fle = open(flename+".js", "w")
    fle.write(template)
    fle.close()
    return

for element in sys.argv:
    write_template(element)

