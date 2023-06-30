from model.fragment import Fragment

# Parser: TextParser

f0 = Fragment(uuid='TEST-00',
         path='README.txt',
         lineno=1,
         depth=1,
         type='documentation',
         name='',
         text='Test project\n============\n')

f1 = Fragment(uuid='TEST-01', path='README.txt', lineno=3, depth=1, type='documentation', name='', text='\n= Rationale =\n')

f2 = Fragment(uuid='TEST-02',
         path='README.txt',
         lineno=5,
         depth=1,
         type='documentation',
         name='',
         text='\nThis is a project used by the unit tests of the **AskYourCode** _ChatGPT_ plugin.\n')

f3 = Fragment(uuid='TEST-03',
         path='README.txt',
         lineno=7,
         depth=1,
         type='documentation',
         name='',
         text='\nWe need a standard set of source code files to validate the unit tests results with.\n')

f4 = Fragment(uuid='TEST-04',
         path='README.txt',
         lineno=9,
         depth=1,
         type='documentation',
         name='',
         text='\n== Doc types and languages ==\n')

f5 = Fragment(uuid='TEST-05',
         path='README.txt',
         lineno=11,
         depth=1,
         type='documentation',
         name='',
         text='\nSupported **document types** and **programming languages**:\n')

f6 = Fragment(uuid='TEST-06',
         path='README.txt',
         lineno=13,
         depth=1,
         type='documentation',
         name='',
         text='\n'
              '- Text\n'
              '- Markdown\n'
              '- Python\n'
              '- Shell\n'
              '- C#\n'
              '- C\n'
              '- C++\n'
              '- Rust\n'
              '- Zig\n'
              '- Java\n'
              '- JavaScript\n'
              '- SQL\n'
              '- CSS\n'
              '- HTML\n')

f7 = Fragment(uuid='TEST-07',
         path='README.txt',
         lineno=28,
         depth=1,
         type='documentation',
         name='',
         text='\n== Some long section ==\n')

f8 = Fragment(uuid='TEST-08',
         path='README.txt',
         lineno=30,
         depth=1,
         type='documentation',
         name='',
         text='\n'
              'Einstein eventually identified the property of spacetime\n'
              'which is responsible for gravity as its curvature. Space\n'
              "and time in Einstein's universe are no longer flat\n"
              '(as implicitly assumed by Newton) but can pushed and pulled,\n'
              'stretched and warped by matter.\n')

f9 = Fragment(uuid='TEST-09', path='README.txt', lineno=36, depth=1, type='documentation', name='', text='\n== Summary ==\n')

f10 = Fragment(uuid='TEST-10',
         path='README.txt',
         lineno=38,
         depth=1,
         type='documentation',
         name='',
         text='\nThis has been a test document for the Markdown parser.\n')

f11 = Fragment(uuid='TEST-11',
         path='README.txt',
         lineno=40,
         depth=1,
         type='documentation',
         name='',
         text='\nEnd of test doc.')

f12 = Fragment(uuid='TEST-12', path='README.txt', lineno=1, depth=0, type='summary', name='', text='File: README.txt\n')

