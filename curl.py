# -*- coding: utf-8 -*-

import urllib2
import sublime_plugin


class CurlCommand(sublime_plugin.WindowCommand):

    def finish(self, url):
        url = normalize_url(url)
        filename = get_filename_from_url(url)
        data = get_data_from_url(url)
        output = self.window.new_file()
        output.set_name(filename)
        output.set_scratch(True)
        edit = output.begin_edit()
        output.insert(edit, 0, data)
        output.end_edit(edit)

    def run(self):
        self.window.show_input_panel('curl>', '', self.finish, None, None)


def get_data_from_url(url):
    try:
        response = urllib2.urlopen(url)
        return response.read()
    except Exception as e:
        return "Couldnt get file! Here's why:\n%s" % repr(e)


def get_filename_from_url(url):
    try:
        return url.split('/')[-1]
    except KeyError:
        return None


def normalize_url(url):
    if url[0:4] != 'http':
        url = 'http://%s' % url
    return url
