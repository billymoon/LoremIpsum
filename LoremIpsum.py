import sublime
import sublime_plugin
import random
import re


class LoremIpsumCommand(sublime_plugin.TextCommand):

    def run(self, edit, qty=10):

        selections = self.view.sel()
        for selection in selections:

            # always start with Lorem ipsum for first outpur lorem
            para = "Lorem ipsum "

            # words from the original Lorum ipsum text
            words = "dolor sit amet consectetur adipisicing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum".split()

            lastchars = self.view.substr(sublime.Region(selection.begin()-20, selection.end()))
            last = re.search("(|(\d+)(\.\d+)*)$", lastchars).group(0)
            if re.search("\d", last):
                print "will repeat " + last + " times"
                # + len(last)
                selection = sublime.Region(selection.begin() - len(str(last)), selection.end())
            else:
                last = 1

            m = str(last).split(".")
            paras = int(m[0])

            if len(m) > 1:
                qty = int(m[1])

            for i in range(0, paras):
                from random import choice
                para += choice(words).capitalize() + " "
                for x in range(random.randint((qty - qty/3)-2, (qty + qty/3)-2)):
                    para += choice(words) + " "
                para += choice(words) + "."
                if i != paras and paras > 1:
                    para += "\n\n"
                editor = self.view.begin_edit()

            print len(str(last))

            # erase region
            self.view.erase(editor, selection)

            last = self.view.substr(sublime.Region(selection.begin()-1, selection.end()))
            if last == ".":
                para = " " + para

            # insert para before current cursor position
            self.view.insert(editor, selection.begin(), para)

            # insert para over the top of selection, but remaining selected (not behavior we want)
            # self.view.replace(editor, self.view.sel()[0], para)

            self.view.end_edit(editor)
