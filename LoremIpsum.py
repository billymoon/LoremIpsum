import sublime
import sublime_plugin
import random
import re
from random import choice

class LoremIpsumCommand(sublime_plugin.TextCommand):

    def run(self, edit, qty=15):

        selections = self.view.sel()
        for selection in selections:

            # always start with Lorem ipsum for first output lorem
            para = ""

            # start with lorem ipsum 20% of the time
            if random.randint(0, 5) == 0:
                para = "lorem ipsum "

            # words from the original Lorum ipsum text
            words = "dolor sit amet consectetur adipisicing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum".split()

            for x in list(range(random.randint(int(qty - qty/3)-2, int(qty + qty/3)-2))):
                para += choice(words) + " "

            para += choice(words)

            para = para.capitalize() + "."

            # erase region
            self.view.erase(edit, selection)

            last = self.view.substr(sublime.Region(selection.begin()-1, selection.end()))
            if last == ".":
                para = " " + para

            # insert para before current cursor position
            self.view.insert(edit, selection.begin(), para)

        self.view.end_edit(edit)
