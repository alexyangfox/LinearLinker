# coding: utf-8
# Proof of concept only..
from os import listdir
from os.path import isfile
import re

# Path with all the markdown files.
# TODO: scan recursively
md_dir_path = 'example_docs/'


# add trailing slash
if md_dir_path[-1] != '/':
    md_dir_path = md_dir_path + '/'


md_files = [f for f in listdir(md_dir_path) if isfile(md_dir_path +f)]

md_dag_map = dict()

# regular expression for links
# but not to match images
link_pattern = re.compile('(?<!!)\[([^]]+)]\(([^)]+)\)')

for f in md_files:
    with open(md_dir_path+f) as fp:
        file_content = ''
        for line in fp:
            file_content = file_content + line
        # FIXME: workaround for muliple lines case.
        md_dag_map[f]=set([file_name for (description,file_name) in link_pattern.findall(file_content)])

md_dag_dot_file_string = 'digraph dag{\n'

for k,v in md_dag_map.iteritems():
    for vv in v:
        md_dag_dot_file_string += '"'+vv + '" -> "' + k + '";\n'

md_dag_dot_file_string += '}'

print md_dag_dot_file_string    
