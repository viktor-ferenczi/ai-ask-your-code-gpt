from model.fragment import Fragment

# Parser: MarkdownParser

f0 = Fragment(uuid='TEST-00',
         path='README.md',
         lineno=1,
         depth=1,
         type='documentation',
         name='',
         text='# Test project\n'
              '\n'
              '## Rationale\n'
              '\n'
              'This is a project used by the unit tests of the **AskYourCode** _ChatGPT_ plugin.\n'
              '\n'
              'We need a standard set of source code files to validate the unit tests results with.\n'
              '\n'
              '### Doc types and languages\n'
              '\n'
              'Supported **document types** and **programming languages**:\n'
              '\n'
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
              '- HTML\n'
              '\n')

f1 = Fragment(uuid='TEST-01',
         path='README.md',
         lineno=28,
         depth=2,
         type='documentation',
         name='',
         text='### Some long section\n'
              '\n'
              'Einstein eventually identified the property of spacetime\n'
              'which is responsible for gravity as its curvature. Space\n'
              "and time in Einstein's universe are no longer flat\n"
              '(as implicitly assumed by Newton) but can pushed and pulled,\n'
              'stretched and warped by matter.\n'
              '\n')

f2 = Fragment(uuid='TEST-02',
         path='README.md',
         lineno=36,
         depth=1,
         type='documentation',
         name='',
         text='## Summary\n\nThis has been a test document for the Markdown parser.\n\nEnd of test doc.')

f3 = Fragment(uuid='TEST-03',
         path='README.md',
         lineno=1,
         depth=0,
         type='summary',
         name='',
         text='# Test project\n## Rationale\n### Doc types and languages\n### Some long section\n## Summary\n')

