import re
# Precompile the patterns
regexes = [re.compile(p)
           for p in ['this', 'that']
           ]
text = "Does this text match the pattern?"
print ('Text: %r\n' % repr(text) )


for regex in regexes:
    print ('Seeking "%s"->' % regex.pattern)

    if regex.search(text):
        print ('match!' )
    else:
        print ('no match')


