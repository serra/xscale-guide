import pypandoc
# now all rst files are located in _generated, with .md extension
# convert them using pypandoc and our custom filters

filters = ['all_relative_links_to_wiki_filter.py']
filename = './source/_generated/Leadership as a Service.md'
output = pypandoc.convert_file(filename, 'rst', filters=filters)
print(output)
