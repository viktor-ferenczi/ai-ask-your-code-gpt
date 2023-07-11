[Fragment(document_cs='09f1864d6543886f5dbb695e393918c53e6291ff49af7e5d4d687a9793f0908b',
          id=1,
          lineno=1,
          tokens=89,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# Sentient Sims Mod\n'
               '\n'
               '## Description\n'
               '\n'
               'Sentient Sims is a mod for The Sims 4 that brings a new level '
               'of immersion and storytelling to the game. This mod generates '
               'dynamic and engaging stories based on the interactions and '
               'actions of your Sims. With Sentient Sims, your Sims will come '
               'to life with unique personalities, realistic dialogue, and '
               'exciting adventures.\n'
               '\n'
               '[www.sentientsimulations.com](https://www.sentientsimulations.com)\n'
               '\n'),
 Fragment(document_cs='09f1864d6543886f5dbb695e393918c53e6291ff49af7e5d4d687a9793f0908b',
          id=2,
          lineno=9,
          tokens=175,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='## Contributing\n'
               '\n'
               'Contributions to the Sentient Sims mod are welcome! If you '
               'would like to contribute, please follow these guidelines:\n'
               '\n'
               '1. **Fork the repository:** Start by forking this repository '
               'to your GitHub account.\n'
               '\n'
               '2. **Create a new branch:** Create a new branch in your forked '
               'repository to work on your changes.\n'
               '\n'
               '3. **Make your modifications:** Implement your changes, '
               "whether it's adding new sim descriptions, expanding location "
               'descriptions, or improving interactions.\n'
               '\n'
               '4. **Commit and push:** Commit your changes and push them to '
               'your forked repository.\n'
               '\n'
               '5. **Submit a pull request:** Submit a pull request from your '
               'branch to the main repository. Provide a clear and detailed '
               'description of the changes you made.\n'
               '\n'
               'Please note that all contributions are subject to review. '
               'Ensure that your modifications align with the overall vision '
               'and quality of the Sentient Sims mod.\n'
               '\n'),
 Fragment(document_cs='09f1864d6543886f5dbb695e393918c53e6291ff49af7e5d4d687a9793f0908b',
          id=3,
          lineno=25,
          tokens=241,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='## Testing Locally\n'
               '\n'
               'The sentient-sims mod must be installed as a pre-requisite.\n'
               '\n'
               'Go to '
               '[www.sentientsimulations.com](https://www.sentientsimulations.com) '
               'to install the mod.\n'
               '\n'
               'In order to test your modifications locally before submitting '
               'the changes:\n'
               '\n'
               '1. Navigate to the sentient-sims folder in the Mods folder\n'
               '1. `git clone git@github.com:guspuffygit/sentient-sims.git '
               'Scripts`\n'
               '1. Delete the file `sentient-sims-descriptions.ts4script` so '
               "that the code doesn't clash with the bundled code\n"
               '1. To hot reload changes to the code while the Sims is '
               'running, open the cheat console and run one of the following '
               'to reload your changes:\n'
               '```\n'
               're sentient_sims.interaction_descriptions\n'
               're sentient_sims.sim_descriptions\n'
               're sentient_sims.zone_descriptions\n'
               '```\n'
               '\n'
               '## Supporting Interactions from Other Mods\n'
               '\n'
               "I haven't quite worked out a method yet to support dynamically "
               'adding interactions. If you want to add interactions for your '
               'mod feel free to add them directly here to this repo, or we '
               'can work to create a way to dynamically add those interaction '
               'descriptions on the fly from your code.\n'
               '\n'),
 Fragment(document_cs='09f1864d6543886f5dbb695e393918c53e6291ff49af7e5d4d687a9793f0908b',
          id=4,
          lineno=47,
          tokens=145,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='## Opening Issues\n'
               '\n'
               'If you encounter any issues, bugs, or have suggestions for '
               'improvements, please open an issue on the GitHub repository. '
               'To open an issue, follow these steps:\n'
               '\n'
               '1. **Navigate to the Issues tab:** Go to the GitHub repository '
               'and click on the "Issues" tab.\n'
               '\n'
               '2. **Click on "New Issue":** Click on the "New Issue" button '
               'to create a new issue.\n'
               '\n'
               '3. **Provide details:** Fill out the issue template with as '
               'much detail as possible. Include steps to reproduce the issue, '
               'expected behavior, and any relevant error messages.\n'
               '\n'
               '4. **Submit the issue:** Once you have filled out the '
               'necessary information, click on "Submit new issue" to create '
               'the issue.\n'),
 Fragment(document_cs='09f1864d6543886f5dbb695e393918c53e6291ff49af7e5d4d687a9793f0908b',
          id=5,
          lineno=1,
          tokens=30,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='# Sentient Sims Mod\n'
               '## Description\n'
               '## Contributing\n'
               '## Testing Locally\n'
               '## Supporting Interactions from Other Mods\n'
               '## Opening Issues\n'),
 Fragment(document_cs='106fb93e653d217772617a063a39d8183f0b2a7e911535efbb4e5e6f4c029568',
          id=6,
          lineno=1,
          tokens=14,
          depth=1,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body='import osfrom pathlib import Pathfrom pathlib import '
               'Pathimport shutilimport string'),
 Fragment(document_cs='106fb93e653d217772617a063a39d8183f0b2a7e911535efbb4e5e6f4c029568',
          id=7,
          lineno=11,
          tokens=7,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# remove all files in this directory'),
 Fragment(document_cs='106fb93e653d217772617a063a39d8183f0b2a7e911535efbb4e5e6f4c029568',
          id=8,
          lineno=7,
          tokens=20,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='create_directory',
          body='def create_directory(path: string):\n'
               '    Path(path).mkdir(parents=True, exist_ok=True)'),
 Fragment(document_cs='106fb93e653d217772617a063a39d8183f0b2a7e911535efbb4e5e6f4c029568',
          id=9,
          lineno=12,
          tokens=25,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='clean_directory',
          body='def clean_directory(path: string):\n'
               '    if os.path.exists(path) and os.path.isdir(path):\n'
               '        shutil.rmtree(path)'),
 Fragment(document_cs='106fb93e653d217772617a063a39d8183f0b2a7e911535efbb4e5e6f4c029568',
          id=10,
          lineno=17,
          tokens=17,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='prepare_directory',
          body='def prepare_directory(path: string):\n'
               '    clean_directory(path)\n'
               '    create_directory(path)'),
 Fragment(document_cs='106fb93e653d217772617a063a39d8183f0b2a7e911535efbb4e5e6f4c029568',
          id=11,
          lineno=1,
          tokens=31,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: clean_directory create_directory '
               'prepare_directory\n'
               '  Variables and usages: Path exist_ok exists isdir mkdir '
               'parents path pathlib rmtree shutil string\n'),
 Fragment(document_cs='181314065df2f2fdaf920b1a8b5311daa216a2d6489a06ada5b49cc514d89417',
          id=12,
          lineno=1,
          tokens=2,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='build/\n'),
 Fragment(document_cs='181314065df2f2fdaf920b1a8b5311daa216a2d6489a06ada5b49cc514d89417',
          id=13,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=14,
          lineno=1,
          tokens=199,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='                    GNU GENERAL PUBLIC LICENSE\n'
               '                       Version 3, 29 June 2007\n'
               '\n'
               ' Copyright (C) 2007 Free Software Foundation, Inc. '
               '<https://fsf.org/>\n'
               ' Everyone is permitted to copy and distribute verbatim copies\n'
               ' of this license document, but changing it is not allowed.\n'
               '\n'
               '                            Preamble\n'
               '\n'
               '  The GNU General Public License is a free, copyleft license '
               'for\n'
               'software and other kinds of works.\n'
               '\n'
               '  The licenses for most software and other practical works are '
               'designed\n'
               'to take away your freedom to share and change the works.  By '
               'contrast,\n'
               'the GNU General Public License is intended to guarantee your '
               'freedom to\n'
               'share and change all versions of a program--to make sure it '
               'remains free\n'
               'software for all its users.  We, the Free Software Foundation, '
               'use the\n'
               'GNU General Public License for most of our software; it '
               'applies also to\n'
               'any other work released this way by its authors.  You can '
               'apply it to\n'
               'your programs, too.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=15,
          lineno=21,
          tokens=223,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  When we speak of free software, we are referring to freedom, '
               'not\n'
               'price.  Our General Public Licenses are designed to make sure '
               'that you\n'
               'have the freedom to distribute copies of free software (and '
               'charge for\n'
               'them if you wish), that you receive source code or can get it '
               'if you\n'
               'want it, that you can change the software or use pieces of it '
               'in new\n'
               'free programs, and that you know you can do these things.\n'
               '\n'
               '  To protect your rights, we need to prevent others from '
               'denying you\n'
               'these rights or asking you to surrender the rights.  '
               'Therefore, you have\n'
               'certain responsibilities if you distribute copies of the '
               'software, or if\n'
               'you modify it: responsibilities to respect the freedom of '
               'others.\n'
               '\n'
               '  For example, if you distribute copies of such a program, '
               'whether\n'
               'gratis or for a fee, you must pass on to the recipients the '
               'same\n'
               'freedoms that you received.  You must make sure that they, '
               'too, receive\n'
               'or can get the source code.  And you must show them these '
               'terms so they\n'
               'know their rights.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=16,
          lineno=39,
          tokens=112,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  Developers that use the GNU GPL protect your rights with two '
               'steps:\n'
               '(1) assert copyright on the software, and (2) offer you this '
               'License\n'
               'giving you legal permission to copy, distribute and/or modify '
               'it.\n'
               '\n'
               "  For the developers' and authors' protection, the GPL clearly "
               'explains\n'
               'that there is no warranty for this free software.  For both '
               "users' and\n"
               "authors' sake, the GPL requires that modified versions be "
               'marked as\n'
               'changed, so that their problems will not be attributed '
               'erroneously to\n'
               'authors of previous versions.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=17,
          lineno=49,
          tokens=245,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  Some devices are designed to deny users access to install or '
               'run\n'
               'modified versions of the software inside them, although the '
               'manufacturer\n'
               'can do so.  This is fundamentally incompatible with the aim '
               'of\n'
               "protecting users' freedom to change the software.  The "
               'systematic\n'
               'pattern of such abuse occurs in the area of products for '
               'individuals to\n'
               'use, which is precisely where it is most unacceptable.  '
               'Therefore, we\n'
               'have designed this version of the GPL to prohibit the practice '
               'for those\n'
               'products.  If such problems arise substantially in other '
               'domains, we\n'
               'stand ready to extend this provision to those domains in '
               'future versions\n'
               'of the GPL, as needed to protect the freedom of users.\n'
               '\n'
               '  Finally, every program is threatened constantly by software '
               'patents.\n'
               'States should not allow patents to restrict development and '
               'use of\n'
               'software on general-purpose computers, but in those that do, '
               'we wish to\n'
               'avoid the special danger that patents applied to a free '
               'program could\n'
               'make it effectively proprietary.  To prevent this, the GPL '
               'assures that\n'
               'patents cannot be used to render the program non-free.\n'
               '\n'
               '  The precise terms and conditions for copying, distribution '
               'and\n'
               'modification follow.\n'
               '\n'
               '                       TERMS AND CONDITIONS\n'
               '\n'
               '  0. Definitions.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=18,
          lineno=74,
          tokens=170,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  "This License" refers to version 3 of the GNU General Public '
               'License.\n'
               '\n'
               '  "Copyright" also means copyright-like laws that apply to '
               'other kinds of\n'
               'works, such as semiconductor masks.\n'
               '\n'
               '  "The Program" refers to any copyrightable work licensed '
               'under this\n'
               'License.  Each licensee is addressed as "you".  "Licensees" '
               'and\n'
               '"recipients" may be individuals or organizations.\n'
               '\n'
               '  To "modify" a work means to copy from or adapt all or part '
               'of the work\n'
               'in a fashion requiring copyright permission, other than the '
               'making of an\n'
               'exact copy.  The resulting work is called a "modified version" '
               'of the\n'
               'earlier work or a work "based on" the earlier work.\n'
               '\n'
               '  A "covered work" means either the unmodified Program or a '
               'work based\n'
               'on the Program.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=19,
          lineno=91,
          tokens=245,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  To "propagate" a work means to do anything with it that, '
               'without\n'
               'permission, would make you directly or secondarily liable for\n'
               'infringement under applicable copyright law, except executing '
               'it on a\n'
               'computer or modifying a private copy.  Propagation includes '
               'copying,\n'
               'distribution (with or without modification), making available '
               'to the\n'
               'public, and in some countries other activities as well.\n'
               '\n'
               '  To "convey" a work means any kind of propagation that '
               'enables other\n'
               'parties to make or receive copies.  Mere interaction with a '
               'user through\n'
               'a computer network, with no transfer of a copy, is not '
               'conveying.\n'
               '\n'
               '  An interactive user interface displays "Appropriate Legal '
               'Notices"\n'
               'to the extent that it includes a convenient and prominently '
               'visible\n'
               'feature that (1) displays an appropriate copyright notice, and '
               '(2)\n'
               'tells the user that there is no warranty for the work (except '
               'to the\n'
               'extent that warranties are provided), that licensees may '
               'convey the\n'
               'work under this License, and how to view a copy of this '
               'License.  If\n'
               'the interface presents a list of user commands or options, '
               'such as a\n'
               'menu, a prominent item in the list meets this criterion.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=20,
          lineno=111,
          tokens=249,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  1. Source Code.\n'
               '\n'
               '  The "source code" for a work means the preferred form of the '
               'work\n'
               'for making modifications to it.  "Object code" means any '
               'non-source\n'
               'form of a work.\n'
               '\n'
               '  A "Standard Interface" means an interface that either is an '
               'official\n'
               'standard defined by a recognized standards body, or, in the '
               'case of\n'
               'interfaces specified for a particular programming language, '
               'one that\n'
               'is widely used among developers working in that language.\n'
               '\n'
               '  The "System Libraries" of an executable work include '
               'anything, other\n'
               'than the work as a whole, that (a) is included in the normal '
               'form of\n'
               'packaging a Major Component, but which is not part of that '
               'Major\n'
               'Component, and (b) serves only to enable use of the work with '
               'that\n'
               'Major Component, or to implement a Standard Interface for '
               'which an\n'
               'implementation is available to the public in source code '
               'form.  A\n'
               '"Major Component", in this context, means a major essential '
               'component\n'
               '(kernel, window system, and so on) of the specific operating '
               'system\n'
               '(if any) on which the executable work runs, or a compiler used '
               'to\n'
               'produce the work, or an object code interpreter used to run '
               'it.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=21,
          lineno=133,
          tokens=211,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  The "Corresponding Source" for a work in object code form '
               'means all\n'
               'the source code needed to generate, install, and (for an '
               'executable\n'
               'work) run the object code and to modify the work, including '
               'scripts to\n'
               'control those activities.  However, it does not include the '
               "work's\n"
               'System Libraries, or general-purpose tools or generally '
               'available free\n'
               'programs which are used unmodified in performing those '
               'activities but\n'
               'which are not part of the work.  For example, Corresponding '
               'Source\n'
               'includes interface definition files associated with source '
               'files for\n'
               'the work, and the source code for shared libraries and '
               'dynamically\n'
               'linked subprograms that the work is specifically designed to '
               'require,\n'
               'such as by intimate data communication or control flow between '
               'those\n'
               'subprograms and other parts of the work.\n'
               '\n'
               '  The Corresponding Source need not include anything that '
               'users\n'
               'can regenerate automatically from other parts of the '
               'Corresponding\n'
               'Source.\n'
               '\n'
               '  The Corresponding Source for a work in source code form is '
               'that\n'
               'same work.\n'
               '\n'
               '  2. Basic Permissions.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=22,
          lineno=155,
          tokens=235,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  All rights granted under this License are granted for the '
               'term of\n'
               'copyright on the Program, and are irrevocable provided the '
               'stated\n'
               'conditions are met.  This License explicitly affirms your '
               'unlimited\n'
               'permission to run the unmodified Program.  The output from '
               'running a\n'
               'covered work is covered by this License only if the output, '
               'given its\n'
               'content, constitutes a covered work.  This License '
               'acknowledges your\n'
               'rights of fair use or other equivalent, as provided by '
               'copyright law.\n'
               '\n'
               '  You may make, run and propagate covered works that you do '
               'not\n'
               'convey, without conditions so long as your license otherwise '
               'remains\n'
               'in force.  You may convey covered works to others for the sole '
               'purpose\n'
               'of having them make modifications exclusively for you, or '
               'provide you\n'
               'with facilities for running those works, provided that you '
               'comply with\n'
               'the terms of this License in conveying all material for which '
               'you do\n'
               'not control copyright.  Those thus making or running the '
               'covered works\n'
               'for you must do so exclusively on your behalf, under your '
               'direction\n'
               'and control, on terms that prohibit them from making any '
               'copies of\n'
               'your copyrighted material outside their relationship with '
               'you.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=23,
          lineno=174,
          tokens=208,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  Conveying under any other circumstances is permitted solely '
               'under\n'
               'the conditions stated below.  Sublicensing is not allowed; '
               'section 10\n'
               'makes it unnecessary.\n'
               '\n'
               "  3. Protecting Users' Legal Rights From Anti-Circumvention "
               'Law.\n'
               '\n'
               '  No covered work shall be deemed part of an effective '
               'technological\n'
               'measure under any applicable law fulfilling obligations under '
               'article\n'
               '11 of the WIPO copyright treaty adopted on 20 December 1996, '
               'or\n'
               'similar laws prohibiting or restricting circumvention of such\n'
               'measures.\n'
               '\n'
               '  When you convey a covered work, you waive any legal power to '
               'forbid\n'
               'circumvention of technological measures to the extent such '
               'circumvention\n'
               'is effected by exercising rights under this License with '
               'respect to\n'
               'the covered work, and you disclaim any intention to limit '
               'operation or\n'
               'modification of the work as a means of enforcing, against the '
               "work's\n"
               "users, your or third parties' legal rights to forbid "
               'circumvention of\n'
               'technological measures.\n'
               '\n'
               '  4. Conveying Verbatim Copies.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=24,
          lineno=196,
          tokens=205,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               "  You may convey verbatim copies of the Program's source code "
               'as you\n'
               'receive it, in any medium, provided that you conspicuously '
               'and\n'
               'appropriately publish on each copy an appropriate copyright '
               'notice;\n'
               'keep intact all notices stating that this License and any\n'
               'non-permissive terms added in accord with section 7 apply to '
               'the code;\n'
               'keep intact all notices of the absence of any warranty; and '
               'give all\n'
               'recipients a copy of this License along with the Program.\n'
               '\n'
               '  You may charge any price or no price for each copy that you '
               'convey,\n'
               'and you may offer support or warranty protection for a fee.\n'
               '\n'
               '  5. Conveying Modified Source Versions.\n'
               '\n'
               '  You may convey a work based on the Program, or the '
               'modifications to\n'
               'produce it from the Program, in the form of source code under '
               'the\n'
               'terms of section 4, provided that you also meet all of these '
               'conditions:\n'
               '\n'
               '    a) The work must carry prominent notices stating that you '
               'modified\n'
               '    it, and giving a relevant date.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=25,
          lineno=216,
          tokens=204,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    b) The work must carry prominent notices stating that it '
               'is\n'
               '    released under this License and any conditions added under '
               'section\n'
               '    7.  This requirement modifies the requirement in section 4 '
               'to\n'
               '    "keep intact all notices".\n'
               '\n'
               '    c) You must license the entire work, as a whole, under '
               'this\n'
               '    License to anyone who comes into possession of a copy.  '
               'This\n'
               '    License will therefore apply, along with any applicable '
               'section 7\n'
               '    additional terms, to the whole of the work, and all its '
               'parts,\n'
               '    regardless of how they are packaged.  This License gives '
               'no\n'
               '    permission to license the work in any other way, but it '
               'does not\n'
               '    invalidate such permission if you have separately received '
               'it.\n'
               '\n'
               '    d) If the work has interactive user interfaces, each must '
               'display\n'
               '    Appropriate Legal Notices; however, if the Program has '
               'interactive\n'
               '    interfaces that do not display Appropriate Legal Notices, '
               'your\n'
               '    work need not make them do so.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=26,
          lineno=234,
          tokens=230,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  A compilation of a covered work with other separate and '
               'independent\n'
               'works, which are not by their nature extensions of the covered '
               'work,\n'
               'and which are not combined with it such as to form a larger '
               'program,\n'
               'in or on a volume of a storage or distribution medium, is '
               'called an\n'
               '"aggregate" if the compilation and its resulting copyright are '
               'not\n'
               "used to limit the access or legal rights of the compilation's "
               'users\n'
               'beyond what the individual works permit.  Inclusion of a '
               'covered work\n'
               'in an aggregate does not cause this License to apply to the '
               'other\n'
               'parts of the aggregate.\n'
               '\n'
               '  6. Conveying Non-Source Forms.\n'
               '\n'
               '  You may convey a covered work in object code form under the '
               'terms\n'
               'of sections 4 and 5, provided that you also convey the\n'
               'machine-readable Corresponding Source under the terms of this '
               'License,\n'
               'in one of these ways:\n'
               '\n'
               '    a) Convey the object code in, or embodied in, a physical '
               'product\n'
               '    (including a physical distribution medium), accompanied by '
               'the\n'
               '    Corresponding Source fixed on a durable physical medium\n'
               '    customarily used for software interchange.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=27,
          lineno=256,
          tokens=222,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    b) Convey the object code in, or embodied in, a physical '
               'product\n'
               '    (including a physical distribution medium), accompanied by '
               'a\n'
               '    written offer, valid for at least three years and valid '
               'for as\n'
               '    long as you offer spare parts or customer support for that '
               'product\n'
               '    model, to give anyone who possesses the object code either '
               '(1) a\n'
               '    copy of the Corresponding Source for all the software in '
               'the\n'
               '    product that is covered by this License, on a durable '
               'physical\n'
               '    medium customarily used for software interchange, for a '
               'price no\n'
               '    more than your reasonable cost of physically performing '
               'this\n'
               '    conveying of source, or (2) access to copy the\n'
               '    Corresponding Source from a network server at no charge.\n'
               '\n'
               '    c) Convey individual copies of the object code with a copy '
               'of the\n'
               '    written offer to provide the Corresponding Source.  This\n'
               '    alternative is allowed only occasionally and '
               'noncommercially, and\n'
               '    only if you received the object code with such an offer, '
               'in accord\n'
               '    with subsection 6b.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=28,
          lineno=274,
          tokens=225,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    d) Convey the object code by offering access from a '
               'designated\n'
               '    place (gratis or for a charge), and offer equivalent '
               'access to the\n'
               '    Corresponding Source in the same way through the same '
               'place at no\n'
               '    further charge.  You need not require recipients to copy '
               'the\n'
               '    Corresponding Source along with the object code.  If the '
               'place to\n'
               '    copy the object code is a network server, the '
               'Corresponding Source\n'
               '    may be on a different server (operated by you or a third '
               'party)\n'
               '    that supports equivalent copying facilities, provided you '
               'maintain\n'
               '    clear directions next to the object code saying where to '
               'find the\n'
               '    Corresponding Source.  Regardless of what server hosts '
               'the\n'
               '    Corresponding Source, you remain obligated to ensure that '
               'it is\n'
               '    available for as long as needed to satisfy these '
               'requirements.\n'
               '\n'
               '    e) Convey the object code using peer-to-peer transmission, '
               'provided\n'
               '    you inform other peers where the object code and '
               'Corresponding\n'
               '    Source of the work are being offered to the general public '
               'at no\n'
               '    charge under subsection 6d.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=29,
          lineno=292,
          tokens=219,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  A separable portion of the object code, whose source code is '
               'excluded\n'
               'from the Corresponding Source as a System Library, need not '
               'be\n'
               'included in conveying the object code work.\n'
               '\n'
               '  A "User Product" is either (1) a "consumer product", which '
               'means any\n'
               'tangible personal property which is normally used for '
               'personal, family,\n'
               'or household purposes, or (2) anything designed or sold for '
               'incorporation\n'
               'into a dwelling.  In determining whether a product is a '
               'consumer product,\n'
               'doubtful cases shall be resolved in favor of coverage.  For a '
               'particular\n'
               'product received by a particular user, "normally used" refers '
               'to a\n'
               'typical or common use of that class of product, regardless of '
               'the status\n'
               'of the particular user or of the way in which the particular '
               'user\n'
               'actually uses, or expects or is expected to use, the product.  '
               'A product\n'
               'is a consumer product regardless of whether the product has '
               'substantial\n'
               'commercial, industrial or non-consumer uses, unless such uses '
               'represent\n'
               'the only significant mode of use of the product.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=30,
          lineno=309,
          tokens=222,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  "Installation Information" for a User Product means any '
               'methods,\n'
               'procedures, authorization keys, or other information required '
               'to install\n'
               'and execute modified versions of a covered work in that User '
               'Product from\n'
               'a modified version of its Corresponding Source.  The '
               'information must\n'
               'suffice to ensure that the continued functioning of the '
               'modified object\n'
               'code is in no case prevented or interfered with solely '
               'because\n'
               'modification has been made.\n'
               '\n'
               '  If you convey an object code work under this section in, or '
               'with, or\n'
               'specifically for use in, a User Product, and the conveying '
               'occurs as\n'
               'part of a transaction in which the right of possession and use '
               'of the\n'
               'User Product is transferred to the recipient in perpetuity or '
               'for a\n'
               'fixed term (regardless of how the transaction is '
               'characterized), the\n'
               'Corresponding Source conveyed under this section must be '
               'accompanied\n'
               'by the Installation Information.  But this requirement does '
               'not apply\n'
               'if neither you nor any third party retains the ability to '
               'install\n'
               'modified object code on the User Product (for example, the '
               'work has\n'
               'been installed in ROM).\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=31,
          lineno=328,
          tokens=159,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  The requirement to provide Installation Information does not '
               'include a\n'
               'requirement to continue to provide support service, warranty, '
               'or updates\n'
               'for a work that has been modified or installed by the '
               'recipient, or for\n'
               'the User Product in which it has been modified or installed.  '
               'Access to a\n'
               'network may be denied when the modification itself materially '
               'and\n'
               'adversely affects the operation of the network or violates the '
               'rules and\n'
               'protocols for communication across the network.\n'
               '\n'
               '  Corresponding Source conveyed, and Installation Information '
               'provided,\n'
               'in accord with this section must be in a format that is '
               'publicly\n'
               'documented (and with an implementation available to the public '
               'in\n'
               'source code form), and must require no special password or key '
               'for\n'
               'unpacking, reading or copying.\n'
               '\n'
               '  7. Additional Terms.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=32,
          lineno=344,
          tokens=230,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  "Additional permissions" are terms that supplement the terms '
               'of this\n'
               'License by making exceptions from one or more of its '
               'conditions.\n'
               'Additional permissions that are applicable to the entire '
               'Program shall\n'
               'be treated as though they were included in this License, to '
               'the extent\n'
               'that they are valid under applicable law.  If additional '
               'permissions\n'
               'apply only to part of the Program, that part may be used '
               'separately\n'
               'under those permissions, but the entire Program remains '
               'governed by\n'
               'this License without regard to the additional permissions.\n'
               '\n'
               '  When you convey a copy of a covered work, you may at your '
               'option\n'
               'remove any additional permissions from that copy, or from any '
               'part of\n'
               'it.  (Additional permissions may be written to require their '
               'own\n'
               'removal in certain cases when you modify the work.)  You may '
               'place\n'
               'additional permissions on material, added by you to a covered '
               'work,\n'
               'for which you have or can give appropriate copyright '
               'permission.\n'
               '\n'
               '  Notwithstanding any other provision of this License, for '
               'material you\n'
               'add to a covered work, you may (if authorized by the copyright '
               'holders of\n'
               'that material) supplement the terms of this License with '
               'terms:\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=33,
          lineno=364,
          tokens=220,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    a) Disclaiming warranty or limiting liability differently '
               'from the\n'
               '    terms of sections 15 and 16 of this License; or\n'
               '\n'
               '    b) Requiring preservation of specified reasonable legal '
               'notices or\n'
               '    author attributions in that material or in the Appropriate '
               'Legal\n'
               '    Notices displayed by works containing it; or\n'
               '\n'
               '    c) Prohibiting misrepresentation of the origin of that '
               'material, or\n'
               '    requiring that modified versions of such material be '
               'marked in\n'
               '    reasonable ways as different from the original version; '
               'or\n'
               '\n'
               '    d) Limiting the use for publicity purposes of names of '
               'licensors or\n'
               '    authors of the material; or\n'
               '\n'
               '    e) Declining to grant rights under trademark law for use '
               'of some\n'
               '    trade names, trademarks, or service marks; or\n'
               '\n'
               '    f) Requiring indemnification of licensors and authors of '
               'that\n'
               '    material by anyone who conveys the material (or modified '
               'versions of\n'
               '    it) with contractual assumptions of liability to the '
               'recipient, for\n'
               '    any liability that these contractual assumptions directly '
               'impose on\n'
               '    those licensors and authors.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=34,
          lineno=387,
          tokens=221,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  All other non-permissive additional terms are considered '
               '"further\n'
               'restrictions" within the meaning of section 10.  If the '
               'Program as you\n'
               'received it, or any part of it, contains a notice stating that '
               'it is\n'
               'governed by this License along with a term that is a further\n'
               'restriction, you may remove that term.  If a license document '
               'contains\n'
               'a further restriction but permits relicensing or conveying '
               'under this\n'
               'License, you may add to a covered work material governed by '
               'the terms\n'
               'of that license document, provided that the further '
               'restriction does\n'
               'not survive such relicensing or conveying.\n'
               '\n'
               '  If you add terms to a covered work in accord with this '
               'section, you\n'
               'must place, in the relevant source files, a statement of the\n'
               'additional terms that apply to those files, or a notice '
               'indicating\n'
               'where to find the applicable terms.\n'
               '\n'
               '  Additional terms, permissive or non-permissive, may be '
               'stated in the\n'
               'form of a separately written license, or stated as '
               'exceptions;\n'
               'the above requirements apply either way.\n'
               '\n'
               '  8. Termination.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=35,
          lineno=408,
          tokens=212,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  You may not propagate or modify a covered work except as '
               'expressly\n'
               'provided under this License.  Any attempt otherwise to '
               'propagate or\n'
               'modify it is void, and will automatically terminate your '
               'rights under\n'
               'this License (including any patent licenses granted under the '
               'third\n'
               'paragraph of section 11).\n'
               '\n'
               '  However, if you cease all violation of this License, then '
               'your\n'
               'license from a particular copyright holder is reinstated (a)\n'
               'provisionally, unless and until the copyright holder '
               'explicitly and\n'
               'finally terminates your license, and (b) permanently, if the '
               'copyright\n'
               'holder fails to notify you of the violation by some reasonable '
               'means\n'
               'prior to 60 days after the cessation.\n'
               '\n'
               '  Moreover, your license from a particular copyright holder '
               'is\n'
               'reinstated permanently if the copyright holder notifies you of '
               'the\n'
               'violation by some reasonable means, this is the first time you '
               'have\n'
               'received notice of violation of this License (for any work) '
               'from that\n'
               'copyright holder, and you cure the violation prior to 30 days '
               'after\n'
               'your receipt of the notice.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=36,
          lineno=428,
          tokens=201,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  Termination of your rights under this section does not '
               'terminate the\n'
               'licenses of parties who have received copies or rights from '
               'you under\n'
               'this License.  If your rights have been terminated and not '
               'permanently\n'
               'reinstated, you do not qualify to receive new licenses for the '
               'same\n'
               'material under section 10.\n'
               '\n'
               '  9. Acceptance Not Required for Having Copies.\n'
               '\n'
               '  You are not required to accept this License in order to '
               'receive or\n'
               'run a copy of the Program.  Ancillary propagation of a covered '
               'work\n'
               'occurring solely as a consequence of using peer-to-peer '
               'transmission\n'
               'to receive a copy likewise does not require acceptance.  '
               'However,\n'
               'nothing other than this License grants you permission to '
               'propagate or\n'
               'modify any covered work.  These actions infringe copyright if '
               'you do\n'
               'not accept this License.  Therefore, by modifying or '
               'propagating a\n'
               'covered work, you indicate your acceptance of this License to '
               'do so.\n'
               '\n'
               '  10. Automatic Licensing of Downstream Recipients.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=37,
          lineno=447,
          tokens=175,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  Each time you convey a covered work, the recipient '
               'automatically\n'
               'receives a license from the original licensors, to run, modify '
               'and\n'
               'propagate that work, subject to this License.  You are not '
               'responsible\n'
               'for enforcing compliance by third parties with this License.\n'
               '\n'
               '  An "entity transaction" is a transaction transferring '
               'control of an\n'
               'organization, or substantially all assets of one, or '
               'subdividing an\n'
               'organization, or merging organizations.  If propagation of a '
               'covered\n'
               'work results from an entity transaction, each party to that\n'
               'transaction who receives a copy of the work also receives '
               'whatever\n'
               "licenses to the work the party's predecessor in interest had "
               'or could\n'
               'give under the previous paragraph, plus a right to possession '
               'of the\n'
               'Corresponding Source of the work from the predecessor in '
               'interest, if\n'
               'the predecessor has it or can get it with reasonable '
               'efforts.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=38,
          lineno=462,
          tokens=156,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  You may not impose any further restrictions on the exercise '
               'of the\n'
               'rights granted or affirmed under this License.  For example, '
               'you may\n'
               'not impose a license fee, royalty, or other charge for '
               'exercise of\n'
               'rights granted under this License, and you may not initiate '
               'litigation\n'
               '(including a cross-claim or counterclaim in a lawsuit) '
               'alleging that\n'
               'any patent claim is infringed by making, using, selling, '
               'offering for\n'
               'sale, or importing the Program or any portion of it.\n'
               '\n'
               '  11. Patents.\n'
               '\n'
               '  A "contributor" is a copyright holder who authorizes use '
               'under this\n'
               'License of the Program or a work on which the Program is '
               'based.  The\n'
               'work thus licensed is called the contributor\'s "contributor '
               'version".\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=39,
          lineno=476,
          tokens=169,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  A contributor\'s "essential patent claims" are all patent '
               'claims\n'
               'owned or controlled by the contributor, whether already '
               'acquired or\n'
               'hereafter acquired, that would be infringed by some manner, '
               'permitted\n'
               'by this License, of making, using, or selling its contributor '
               'version,\n'
               'but do not include claims that would be infringed only as a\n'
               'consequence of further modification of the contributor '
               'version.  For\n'
               'purposes of this definition, "control" includes the right to '
               'grant\n'
               'patent sublicenses in a manner consistent with the '
               'requirements of\n'
               'this License.\n'
               '\n'
               '  Each contributor grants you a non-exclusive, worldwide, '
               'royalty-free\n'
               "patent license under the contributor's essential patent "
               'claims, to\n'
               'make, use, sell, offer for sale, import and otherwise run, '
               'modify and\n'
               'propagate the contents of its contributor version.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=40,
          lineno=491,
          tokens=86,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  In the following three paragraphs, a "patent license" is any '
               'express\n'
               'agreement or commitment, however denominated, not to enforce a '
               'patent\n'
               '(such as an express permission to practice a patent or '
               'covenant not to\n'
               'sue for patent infringement).  To "grant" such a patent '
               'license to a\n'
               'party means to make such an agreement or commitment not to '
               'enforce a\n'
               'patent against the party.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=41,
          lineno=498,
          tokens=192,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  If you convey a covered work, knowingly relying on a patent '
               'license,\n'
               'and the Corresponding Source of the work is not available for '
               'anyone\n'
               'to copy, free of charge and under the terms of this License, '
               'through a\n'
               'publicly available network server or other readily accessible '
               'means,\n'
               'then you must either (1) cause the Corresponding Source to be '
               'so\n'
               'available, or (2) arrange to deprive yourself of the benefit '
               'of the\n'
               'patent license for this particular work, or (3) arrange, in a '
               'manner\n'
               'consistent with the requirements of this License, to extend '
               'the patent\n'
               'license to downstream recipients.  "Knowingly relying" means '
               'you have\n'
               'actual knowledge that, but for the patent license, your '
               'conveying the\n'
               "covered work in a country, or your recipient's use of the "
               'covered work\n'
               'in a country, would infringe one or more identifiable patents '
               'in that\n'
               'country that you have reason to believe are valid.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=42,
          lineno=512,
          tokens=95,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  If, pursuant to or in connection with a single transaction '
               'or\n'
               'arrangement, you convey, or propagate by procuring conveyance '
               'of, a\n'
               'covered work, and grant a patent license to some of the '
               'parties\n'
               'receiving the covered work authorizing them to use, propagate, '
               'modify\n'
               'or convey a specific copy of the covered work, then the patent '
               'license\n'
               'you grant is automatically extended to all recipients of the '
               'covered\n'
               'work and works based on it.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=43,
          lineno=520,
          tokens=246,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  A patent license is "discriminatory" if it does not include '
               'within\n'
               'the scope of its coverage, prohibits the exercise of, or is\n'
               'conditioned on the non-exercise of one or more of the rights '
               'that are\n'
               'specifically granted under this License.  You may not convey a '
               'covered\n'
               'work if you are a party to an arrangement with a third party '
               'that is\n'
               'in the business of distributing software, under which you make '
               'payment\n'
               'to the third party based on the extent of your activity of '
               'conveying\n'
               'the work, and under which the third party grants, to any of '
               'the\n'
               'parties who would receive the covered work from you, a '
               'discriminatory\n'
               'patent license (a) in connection with copies of the covered '
               'work\n'
               'conveyed by you (or copies made from those copies), or (b) '
               'primarily\n'
               'for and in connection with specific products or compilations '
               'that\n'
               'contain the covered work, unless you entered into that '
               'arrangement,\n'
               'or that patent license was granted, prior to 28 March 2007.\n'
               '\n'
               '  Nothing in this License shall be construed as excluding or '
               'limiting\n'
               'any implied license or other defenses to infringement that '
               'may\n'
               'otherwise be available to you under applicable patent law.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=44,
          lineno=539,
          tokens=159,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               "  12. No Surrender of Others' Freedom.\n"
               '\n'
               '  If conditions are imposed on you (whether by court order, '
               'agreement or\n'
               'otherwise) that contradict the conditions of this License, '
               'they do not\n'
               'excuse you from the conditions of this License.  If you cannot '
               'convey a\n'
               'covered work so as to satisfy simultaneously your obligations '
               'under this\n'
               'License and any other pertinent obligations, then as a '
               'consequence you may\n'
               'not convey it at all.  For example, if you agree to terms that '
               'obligate you\n'
               'to collect a royalty for further conveying from those to whom '
               'you convey\n'
               'the Program, the only way you could satisfy both those terms '
               'and this\n'
               'License would be to refrain entirely from conveying the '
               'Program.\n'
               '\n'
               '  13. Use with the GNU Affero General Public License.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=45,
          lineno=553,
          tokens=164,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  Notwithstanding any other provision of this License, you '
               'have\n'
               'permission to link or combine any covered work with a work '
               'licensed\n'
               'under version 3 of the GNU Affero General Public License into '
               'a single\n'
               'combined work, and to convey the resulting work.  The terms of '
               'this\n'
               'License will continue to apply to the part which is the '
               'covered work,\n'
               'but the special requirements of the GNU Affero General Public '
               'License,\n'
               'section 13, concerning interaction through a network will '
               'apply to the\n'
               'combination as such.\n'
               '\n'
               '  14. Revised Versions of this License.\n'
               '\n'
               '  The Free Software Foundation may publish revised and/or new '
               'versions of\n'
               'the GNU General Public License from time to time.  Such new '
               'versions will\n'
               'be similar in spirit to the present version, but may differ in '
               'detail to\n'
               'address new problems or concerns.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=46,
          lineno=569,
          tokens=198,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  Each version is given a distinguishing version number.  If '
               'the\n'
               'Program specifies that a certain numbered version of the GNU '
               'General\n'
               'Public License "or any later version" applies to it, you have '
               'the\n'
               'option of following the terms and conditions either of that '
               'numbered\n'
               'version or of any later version published by the Free '
               'Software\n'
               'Foundation.  If the Program does not specify a version number '
               'of the\n'
               'GNU General Public License, you may choose any version ever '
               'published\n'
               'by the Free Software Foundation.\n'
               '\n'
               '  If the Program specifies that a proxy can decide which '
               'future\n'
               'versions of the GNU General Public License can be used, that '
               "proxy's\n"
               'public statement of acceptance of a version permanently '
               'authorizes you\n'
               'to choose that version for the Program.\n'
               '\n'
               '  Later license versions may give you additional or different\n'
               'permissions.  However, no additional obligations are imposed '
               'on any\n'
               'author or copyright holder as a result of your choosing to '
               'follow a\n'
               'later version.\n'
               '\n'
               '  15. Disclaimer of Warranty.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=47,
          lineno=590,
          tokens=149,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT '
               'PERMITTED BY\n'
               'APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE '
               'COPYRIGHT\n'
               'HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" '
               'WITHOUT WARRANTY\n'
               'OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT '
               'LIMITED TO,\n'
               'THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A '
               'PARTICULAR\n'
               'PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF '
               'THE PROGRAM\n'
               'IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME '
               'THE COST OF\n'
               'ALL NECESSARY SERVICING, REPAIR OR CORRECTION.\n'
               '\n'
               '  16. Limitation of Liability.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=48,
          lineno=601,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO '
               'IN WRITING\n'
               'WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES '
               'AND/OR CONVEYS\n'
               'THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, '
               'INCLUDING ANY\n'
               'GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING '
               'OUT OF THE\n'
               'USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED '
               'TO LOSS OF\n'
               'DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY '
               'YOU OR THIRD\n'
               'PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER '
               'PROGRAMS),\n'
               'EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE '
               'POSSIBILITY OF\n'
               'SUCH DAMAGES.\n'
               '\n'
               '  17. Interpretation of Sections 15 and 16.\n'
               '\n'
               '  If the disclaimer of warranty and limitation of liability '
               'provided\n'
               'above cannot be given local legal effect according to their '
               'terms,\n'
               'reviewing courts shall apply local law that most closely '
               'approximates\n'
               'an absolute waiver of all civil liability in connection with '
               'the\n'
               'Program, unless a warranty or assumption of liability '
               'accompanies a\n'
               'copy of the Program in return for a fee.\n'
               '\n'
               '                     END OF TERMS AND CONDITIONS\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=49,
          lineno=622,
          tokens=211,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '            How to Apply These Terms to Your New Programs\n'
               '\n'
               '  If you develop a new program, and you want it to be of the '
               'greatest\n'
               'possible use to the public, the best way to achieve this is to '
               'make it\n'
               'free software which everyone can redistribute and change under '
               'these terms.\n'
               '\n'
               '  To do so, attach the following notices to the program.  It '
               'is safest\n'
               'to attach them to the start of each source file to most '
               'effectively\n'
               'state the exclusion of warranty; and each file should have at '
               'least\n'
               'the "copyright" line and a pointer to where the full notice is '
               'found.\n'
               '\n'
               "    <one line to give the program's name and a brief idea of "
               'what it does.>\n'
               '    Copyright (C) <year>  <name of author>\n'
               '\n'
               '    This program is free software: you can redistribute it '
               'and/or modify\n'
               '    it under the terms of the GNU General Public License as '
               'published by\n'
               '    the Free Software Foundation, either version 3 of the '
               'License, or\n'
               '    (at your option) any later version.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=50,
          lineno=641,
          tokens=236,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    This program is distributed in the hope that it will be '
               'useful,\n'
               '    but WITHOUT ANY WARRANTY; without even the implied '
               'warranty of\n'
               '    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See '
               'the\n'
               '    GNU General Public License for more details.\n'
               '\n'
               '    You should have received a copy of the GNU General Public '
               'License\n'
               '    along with this program.  If not, see '
               '<https://www.gnu.org/licenses/>.\n'
               '\n'
               'Also add information on how to contact you by electronic and '
               'paper mail.\n'
               '\n'
               '  If the program does terminal interaction, make it output a '
               'short\n'
               'notice like this when it starts in an interactive mode:\n'
               '\n'
               '    <program>  Copyright (C) <year>  <name of author>\n'
               '    This program comes with ABSOLUTELY NO WARRANTY; for '
               "details type `show w'.\n"
               '    This is free software, and you are welcome to redistribute '
               'it\n'
               "    under certain conditions; type `show c' for details.\n"
               '\n'
               "The hypothetical commands `show w' and `show c' should show "
               'the appropriate\n'
               'parts of the General Public License.  Of course, your '
               "program's commands\n"
               'might be different; for a GUI interface, you would use an '
               '"about box".\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=51,
          lineno=663,
          tokens=149,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  You should also get your employer (if you work as a '
               'programmer) or school,\n'
               'if any, to sign a "copyright disclaimer" for the program, if '
               'necessary.\n'
               'For more information on this, and how to apply and follow the '
               'GNU GPL, see\n'
               '<https://www.gnu.org/licenses/>.\n'
               '\n'
               '  The GNU General Public License does not permit incorporating '
               'your program\n'
               'into proprietary programs.  If your program is a subroutine '
               'library, you\n'
               'may consider it more useful to permit linking proprietary '
               'applications with\n'
               'the library.  If this is what you want to do, use the GNU '
               'Lesser General\n'
               'Public License instead of this License.  But first, please '
               'read\n'
               '<https://www.gnu.org/licenses/why-not-lgpl.html>.\n'),
 Fragment(document_cs='3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986',
          id=52,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=53,
          lineno=2,
          tokens=240,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='careers_Adult_Freelancer_Agency_ProgrammercareerTracks_Freelancer_ProgrammerFreelance '
               'ProgrammerWhy sit in an office filled with coworkers talking '
               'about their kids? {0.SimFirstName} just wants to focus up and '
               'get some coding done in the comfort of wherever '
               '{F0.she}{M0.he} desires. No boss is going to tell '
               '{0.SimPronounObjective} what to work on. From spreadsheets to '
               "videogames, it's all {F0.her}{M0.his} "
               'choice!sentient_sims_description{sim_name} works as a '
               'freelance programmer.career_Child_GradeSchoolGrade School F '
               "StudentLet's not sugar coat things.  You're failing.  But "
               "you've still got time to turn it around!  Do some homework - "
               'any homework - and go to '
               'school.sentient_sims_description{sim_name} is a student in '
               'grade school and currently failing classes.Grade School D '
               "StudentWhen Ds are the norm, things aren't bleak quite yet, "
               "but the teacher has called home a few times and you're right "
               'on the edge of failing out of school.sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=54,
          lineno=21,
          tokens=227,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} is a student in grade school and currently failing '
               'classes.Grade School C StudentThe middle of the pack is the '
               'most popular place to be, as evidenced by the other C students '
               "that surround you.  It's like a club!  A non-exclusive "
               'mediocre club.sentient_sims_description{sim_name} is a student '
               'in grade school and barely passing classes with Cs.Grade '
               'School B Studentsentient_sims_description{sim_name} is a '
               'student in grade school and are passing classes with Bs.Grade '
               'School A StudentIt must be hard to be an A student.  All that '
               'time studying, feeling superior, and studying some '
               'more.sentient_sims_description{sim_name} is a student in grade '
               'school and are exceeding in classes with '
               "As.career_Adult_Astronaut{0.SimFirstName}'s always had dreams "
               'about exploring the cosmos, walking among the stars, and '
               'discovering places unknown. {M0.His}{F0.Her} journey begins '
               'here, in the file room, categorizing expense '
               'reports.sentient_sims_description{sim_name} is working as an '
               'Astronaut Intern.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=55,
          lineno=48,
          tokens=238,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Little-known fact: Space is an absolutely filthy place. When '
               'the shuttles return, guess who gets to hose them down and '
               'scrub off the gunk? {0.SimFirstName} hopes the goo is just '
               'dirt and not some incurable form of Oozing Space '
               'Measles.sentient_sims_description{sim_name} is working at a '
               'space facility cleaning shuttles returning from '
               "space.{0.SimFirstName} doesn't think of "
               '{M0.himself}{F0.herself} as just a glorified mechanic. The '
               'shuttle costs billions of Simoleons, and any screw-ups would '
               "cost lives. {M0.He's}{F0.She's} more like a glorified "
               'engineer.sentient_sims_description{sim_name} is working as an '
               'astronaut technician working on space shuttles.Guiding virtual '
               'rockets into place, analyzing the movements of blinking dots '
               'on a computer screen, running simulations.... Looks like all '
               'those hours {0.SimFirstName} spent playing video games are '
               'paying off!sentient_sims_description{sim_name} is working with '
               'astronauts at the space center as a command center lead, '
               'helping guide rockets in space.Low-Orbit Specialist'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=56,
          lineno=63,
          tokens=213,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Low orbit is where the real action is-satellites, space '
               'stations, space walks, daredevils attempting to break the '
               'world record for high-altitude parachuting. If something goes '
               "wrong, it's also the closest place to breathable air, which is "
               'why {0.SimFirstName} likes '
               'it.sentient_sims_description{sim_name} is working as a '
               'low-orbit specialist, piloting planes into low-orbit and '
               'helping guide satellites.{0.SimFirstName} was hoping that if '
               '{M0.he}{F0.she} \\"accidentally\\" derailed a shuttle-board '
               '\\"simulation\\" {M0.he}{F0.she} might be able to launch the '
               'shuttle and get to space\\u00e2\\u0080\\u00a6but it turns out '
               "that actual spacecraft are pretty well-secured. That's good, "
               'because {0.SimFirstName} is still learning how to space brake '
               'and star park.sentient_sims_description{sim_name} is working '
               'as a space cadet, training to become a full blown astronaut.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=57,
          lineno=73,
          tokens=216,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='This is it: Astronaut. The best of the best. The heroic few. '
               'The job kids want to be when they grow up that they still want '
               'to be as adults. {0.SimFirstName} will now go boldly into that '
               'great beyond to explore the secrets of the universe and eat '
               'weird freeze-dried ice '
               'cream.sentient_sims_description{sim_name} is working as an '
               'astronaut, they are at the top of their field, exploring space '
               'in space '
               "shuttles.Astronaut_Track2_SpaceRanger{0.SimFirstName}'s drawn "
               "a pretty good beat. {M0.He's}{F0.She's} patrolling planet "
               'Illustria, which is scenic and upscale, with nice shops and '
               "restaurants. Luckily, {M0.he}{F0.she} didn't get the Bloodwar "
               'planet, which is also pretty scenic but has fewer '
               'restaurants.sentient_sims_description{sim_name} is working '
               'planet patrol, a job for astronauts. {sim_name} patrols the '
               'planet Illustria, which is scenic and upscale.Sheriff of the '
               'Stars'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=58,
          lineno=85,
          tokens=245,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="This here galaxy's {0.SimFirstName}'s jurisdiction now. "
               'Even-handed with the punishment and generous with the '
               "attitude, {M0.he}{F0.she} don't take no nonsense from alien "
               'punks, no matter now many tentacles or ocular cavities or rows '
               'of teeth they have. Also, {M0.he}{F0.she} gets to talk like a '
               'sheriff!sentient_sims_description{sim_name} is working as '
               'sheriff of the stars, patrolling the galaxy and securing it '
               'from alien threats.When the universe is in danger, one '
               '{M0.man}{F0.woman} gets the call: {0.SimFirstName}, Space '
               'Ranger! With {M0.his}{F0.her} stout heart, keen wits, and a '
               'phozoplasmic Warp Pack strapped to {M0.his}{F0.her} back, '
               'Ranger {0.SimFirstName} defends the known galaxies from '
               'evil!sentient_sims_description{sim_name} is working as THE '
               'space ranger, when the universe is in danger, only one person '
               'gets the call, {sim_name}, defends the known galaxies from '
               'evil.Astronaut_Track3_Smuggler'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=59,
          lineno=97,
          tokens=194,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Any ranger who's quick with a laser can make more Simoleons in "
               'private security than serving the public good. '
               '{0.SimFirstName} protects galactic warlords, exterminates '
               'cabals of tribal terrorists, and helps corrupt governments '
               'maintain plausible '
               'deniability.sentient_sims_description{sim_name} is working as '
               'a moon mercenary, {sim_name} works as private security '
               'protecting galactic warlords, exterminating cabals of tribal '
               'terrorists, and helps corrupt governments.Want the horn of an '
               'endangered zygax? How about a quilt handmade from 2,000 tiny '
               'Q505Bs? Maybe just a few Gibsonian chill-out pods for the big '
               "party next weekend? {0.SimFirstName} doesn't ask questions. "
               '{M0.He}{F0.She} just makes it '
               'happen.sentient_sims_description{sim_name} is working as an '
               'alien goods trader, buys and sells legal and illegal alien '
               'goods across the galaxy.Interstellar Smuggler'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=60,
          lineno=107,
          tokens=197,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="There's no trade route too treacherous, no cargo too "
               'controversial for {0.SimFirstName} to covertly ship across the '
               "universe and into {M0.his}{F0.her} customers' covetous hands. "
               'Capitalism is capitalism. And a 2000% markup is a 2000% '
               'markup.sentient_sims_description{sim_name} is working as an '
               'interstellar smuggler, covertly shipping illegal goods across '
               'the galaxy.{0.SimFirstName} is ready to take {M0.his}{F0.her} '
               'part in the global economy. People need to buy things to make '
               'the economy happen, and that means that people need retailers '
               'to sell them things, and THAT means that someone needs to '
               'stock a bunch of shelves. Guess what '
               '{0.SimFirstName}\\u00e2\\u0080\\u0099s part '
               'is?sentient_sims_description{sim_name} is working as a shelf '
               'stocker at a department store.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=61,
          lineno=121,
          tokens=230,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} has been promoted to Sales Floor Clerk! Now '
               '{M0.he}{F0.she} can interact directly with the customers and '
               'brush up on vital salesmanship skills! And between customers '
               '{M0.he}{F0.she} can sweep floors, scrape off gum, heft boxes '
               'and restock store displays.sentient_sims_description{sim_name} '
               'is working as a sales floor clerk at a department '
               'store.\\u00e2\\u0080\\u009cHappy customers, healthy '
               'business!\\u00e2\\u0080\\u009d At least, '
               'that\\u00e2\\u0080\\u0099s what '
               '{0.SimFirstName}\\u00e2\\u0080\\u0099s training manual says. '
               '{M0.He}{F0.She} might be earning a healthier wage, manning the '
               'support desk with a smile, but the only customers who get sent '
               '{M0.his}{F0.her} way are not happy, not at '
               'all.sentient_sims_description{sim_name} is working as a '
               'customer service representative at a department '
               'store.career_Adult_Painter'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=62,
          lineno=135,
          tokens=224,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='To create great art, one must suffer. {0.SimFirstName} is well '
               'on {M0.his}{F0.her} way to greatness, as {M0.he}{F0.she} will '
               'be asked to create floor-based installations using a '
               'water-based medium (i.e. mopping the '
               'floor).sentient_sims_description{sim_name} works at an art '
               'studio cleaning and organizing palettes used for mixing '
               'paint.Saving up for art school supplies means working at the '
               'art school library. Unfortunately, the books must be '
               're-shelved by number, and no one sees the genius in '
               '{0.SimFirstName} re-shelving them by complementary color. '
               'Visionaries are often '
               'misunderstood.sentient_sims_description{sim_name} works at an '
               'art gallery arranging and categorizing art books.Being a '
               "hungry artist isn't about literal hunger. It's about "
               "{0.SimFirstName}'s burning passion to create an artistic "
               "expression that can change people's lives! (It's also about "
               'literal hunger.)sentient_sims_description{sim_name} works for '
               'little pay as a new artist.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=63,
          lineno=150,
          tokens=215,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} is now a working artist! At least '
               "{M0.he}{F0.she}'s working a booth at a local art fair, where "
               'patrons are haggling down the price of {M0.his}{F0.her} '
               'watercolored landscapes. But the words \\"work\\" and '
               '\\"artist\\" are coming closer together. And that\'s a good '
               'sign!sentient_sims_description{sim_name} works at an art '
               'gallery arranging and categorizing art '
               'books.sentient_sims_description{sim_name} works as an '
               'independent artist, creating and selling original canvas '
               'paintings.{0.SimFirstName} has boldly painted {M0.his}{F0.her} '
               'way into a career in studio art\\u00e2\\u0080\\u0094mastering '
               'still life, figure study, interior space, and the fine art of '
               'disdain for anyone living in mainstream '
               'society.sentient_sims_description{sim_name} works as a studio '
               'artist, focusing on a variety of themes and styles in his '
               'paintings.Painter_Track2_Artist'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=64,
          lineno=166,
          tokens=243,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Winning this artist residency is a true honor! Not everyone '
               'gets to work in an unheated barn loft for free. What a great '
               'way for {0.SimFirstName} to experience a slice of life '
               '{M0.he}{F0.she} would never actually '
               'choose!sentient_sims_description{sim_name} has been honored '
               'with an artist residency, providing him an exclusive space to '
               'create and exhibit his work.Professional '
               'Painter{0.SimFirstName} just hung some work in the hottest '
               "gallery in town! And it's actually {M0.his}{F0.her} work this "
               'time! This is a wonderful achievement for any '
               'artist.sentient_sims_description{sim_name} is a professional '
               'artist whose work is exhibited in one of the hottest galleries '
               'in town.Illustrious IllustratorProfessional illustrator is a '
               'challenging role. {0.SimFirstName} controls the final visual, '
               "but does not control the subject matter. Whether it's a famous "
               'historical figure or a cartoon squirrel, {M0.he}{F0.she} is up '
               'to the task!sentient_sims_description{sim_name} works as a '
               'professional illustrator, using his artistic skills to '
               'visually represent a variety of subjects.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=65,
          lineno=181,
          tokens=195,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Students now flock to {0.SimFirstName}, hoping to glean even a '
               'bit of the technique that has made {M0.his}{F0.her} artwork so '
               'popular. Time to pass on what {M0.he}{F0.she} has learned to '
               'the next generation, or just wave {M0.his}{F0.her} paintbrush '
               'and sigh, \\"Hopeless!\\"sentient_sims_description{sim_name} '
               'is a well-respected artist and mentor, sharing his artistic '
               'knowledge and expertise with aspiring '
               'artists.Painter_Track3_Critic{0.SimFirstName} now spends equal '
               'amounts of time improving {M0.his}{F0.her} own technique and '
               'politely suggesting how other artists can improve theirs. It '
               'allows interaction with the greatest talents of this '
               'generation, even if those interactions are sometimes '
               'prickly.sentient_sims_description{sim_name} works as a critic, '
               'analyzing and giving constructive criticism on the techniques '
               'of other artists.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=66,
          lineno=193,
          tokens=247,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Beauty is in the eye of the beholder, but money is in the eye '
               'of the appraiser. {0.SimFirstName} draws on {M0.his}{F0.her} '
               'significant training to determine the value of fine art, '
               'letting others know that not every paint-covered canvas is '
               'created equal.sentient_sims_description{sim_name} is an art '
               'appraiser, using his knowledge and experience to evaluate the '
               'monetary value of fine art.sentient_sims_description{sim_name} '
               'works as a curator, managing the acquisition and display of '
               "various art collections.{0.SimFirstName}'s private collection "
               'has gained such widespread fame that {M0.he}{F0.she} now '
               'spends {M0.his}{F0.her} days negotiating with museums that '
               'want to display it. As long as they each build the '
               '\\"{0.SimFirstName} Wing\\", with a bronze plaque of '
               "{0.SimFirstName}'s face, no "
               'problem!sentient_sims_description{sim_name} has become a '
               'patron of the arts, lending his valuable art collection to '
               'museums and contributing to the promotion of art in '
               'society.career_Adult_PartTime_BaristaPartTime_Barista_Track1Coffee '
               'Stain Remover'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=67,
          lineno=211,
          tokens=221,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='This is {0.SimFirstName}\\u00e2\\u0080\\u0099s first step into '
               'the exciting world of caffeine distribution systems. But of '
               'course {M0.he}{F0.she} can\\u00e2\\u0080\\u0099t be '
               'responsible for pouring coffee until {M0.he}{F0.she} proves '
               '{M0.he}{F0.she} can handle mopping floors, setting up chairs, '
               'scrubbing mugs and keeping those frothers and foamers '
               'shiny!sentient_sims_description{sim_name} just started working '
               'at starbucks part-time and is responsible for cleaning.At '
               'last, {0.SimFirstName} can drop the dishrags and become one '
               'with the art of fine coffee! Grinding together the finest '
               'organic beans from around the globe, {0.SimFirstName} is now a '
               'master bean blender, a true mixologist whose arresting '
               'combinations of aggressively bold aromas and subtly nutty '
               'undertones please every '
               'palate.sentient_sims_description{sim_name} works at starbucks '
               'part-time and is responsible for helping prep drinks.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=68,
          lineno=221,
          tokens=243,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Bravo! {0.SimFirstName} has ascended the barista ranks and '
               'seized control of the frother. Now in charge of crafting '
               'sumptuous espresso drinks, adorned with a dollop of '
               'feather-light froth which {M0.he}{F0.she} arranges in cute '
               'patterns, {0.SimFirstName} knows '
               '{M0.he}{F0.she}\\u00e2\\u0080\\u0099s a true '
               'artiste.sentient_sims_description{sim_name} works at starbucks '
               'part-time as a '
               'barista.career_Teen_ManualLaborTeen_ManualLabor_Track1For '
               'once, being young and inexperienced will work in '
               '{0.SimFirstName}\\u00e2\\u0080\\u0099s favor! After all, '
               '{M0.he}{F0.she} is strong, energetic, and less likely to sue '
               'for hearing loss. In fact, the adults in the neighborhood will '
               'almost feel like they are doing {0.SimFirstName} a favor by '
               'letting {M0.him}{F0.her} push heavy '
               'equipment!sentient_sims_description{sim_name} works as a lawn '
               'mower, mowing peoples yards.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=69,
          lineno=235,
          tokens=245,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} is working {M0.his}{F0.her} way up the ladder '
               'in the landscaping world, flexing not just {M0.his}{F0.her} '
               'muscles, but {M0.his}{F0.her} artistry as well. Sure, '
               '{0.SimFirstName} is mostly working off other '
               'people\\u00e2\\u0080\\u0099s designs-planting, digging, '
               'raking, mowing-but every so often {M0.he}{F0.she} gets to make '
               'a fleeting mark on {M0.his}{F0.her} '
               'clients\\u00e2\\u0080\\u0099 verdant '
               'tableaux.sentient_sims_description{sim_name} works as a '
               'landscaper.Every kid goes through a digging phase, but no tiny '
               'scoop and plastic pail on the beach can ever compare to the '
               'sheer awesomeness of breaking into the earth with a backhoe! '
               'This is a big promotion to operate a big machine, and '
               '{0.SimFirstName} is hoping the big responsibility will '
               'translate into big '
               'Simoleons!sentient_sims_description{sim_name} works as a '
               'backhoe operator in construction.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=70,
          lineno=245,
          tokens=161,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='careers_Adult_Freelancer_Agency_WritercareerTracks_Freelancer_WriterClimbing '
               'the ladder in a writing firm only to be assigned boring '
               "projects just isn't for {0.SimFirstName}. Neither is working "
               'unpaid and hoping to publish something that catches on. All '
               '{F0.she}{M0.he} wants to do is put {F0.her}{M0.his} prose to '
               'the paper and be rewarded for {F0.her}{M0.his} efforts. Being '
               'able to work wherever {F0.she}{M0.he} wants is a great bonus, '
               'too.sentient_sims_description{sim_name} works as a freelance '
               'writer.career_Adult_Freelancer_ArtistcareerTracks_Freelancer_Artist'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=71,
          lineno=258,
          tokens=223,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Spec art is for starving artists; corporate art is for those '
               "who have sacrificed their creative soul. Surely there's a "
               "better way to earn a living wage without abdicating one's "
               'creative freedom? Such is the path of a freelancer, who '
               'possesses the temerity to pick and choose from those seeking '
               '{M0.his}{F0.her} artistic talents. With Digitalistic Sketchpad '
               'in hand; go forth and add beauty to the world on your own '
               'terms.sentient_sims_description{sim_name} works as a freelance '
               'artist, painting murals and art installations for '
               'hire.{0.SimFirstName} is about to learn what it means to pay '
               '{M0.his}{F0.her} dues as an assistant-assistant coffee-getter, '
               'assistant fact-looker-upper, and assistant paperwork-filer. '
               'After a while, {M0.he}{F0.she} may even get to do some '
               'writing, although {M0.his}{F0.her} boss will take the '
               'credit.sentient_sims_description{sim_name} works as writer '
               'intern, getting coffee and helping fill paperwork.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=72,
          lineno=272,
          tokens=129,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='It\\u00e2\\u0080\\u0099s more important to write fast than to '
               'write well\\u00e2\\u0080\\u00a6does {0.SimFirstName} have what '
               'it takes? Bloggers only get paid if they get clicks, so '
               '{M0.he\\u00e2\\u0080\\u0099d}{F0.she\\u00e2\\u0080\\u0099d} '
               'better study the things people like to click on. (Cat videos '
               'and numbered lists.) sentient_sims_description{sim_name} works '
               'as a blog writer, getting paid for clicks online.Freelance '
               'Article Writer'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=73,
          lineno=277,
          tokens=181,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Now {0.SimFirstName}\\u00e2\\u0080\\u0099s working for '
               '{M0.himself}{F0.herself}, writing what {M0.he}{F0.she} '
               'wants\\u00e2\\u0080\\u00a6or at least what paying clients '
               'want. Unfortunately, paying clients want articles about '
               '\\u00e2\\u0080\\u009c10 Creative Ways to Eat '
               'Mushrooms\\u00e2\\u0080\\u009d or \\u00e2\\u0080\\u009cHot '
               'Tips to Drive Your Dog Wild.\\u00e2\\u0080\\u009d '
               'It\\u00e2\\u0080\\u0099s not glamorous, but '
               'it\\u00e2\\u0080\\u0099s a '
               'living!sentient_sims_description{sim_name} works as a writer, '
               'writing articles for websites online.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=74,
          lineno=282,
          tokens=237,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{M0.He\\u00e2\\u0080\\u0099s}{F0.She\\u00e2\\u0080\\u0099s} '
               'always thought of {M0.himself}{F0.herself} as a know-it-all, '
               'but now {0.SimFirstName} is a professional know-it-all. The '
               'life of an advice columnist is full of deranged in-laws, '
               'mailmen without personal boundaries, and secret second '
               'families. But only if {M0.he}{F0.she}\\u00e2\\u0080\\u0099s '
               'lucky.sentient_sims_description{sim_name} works as a writer '
               'for the advice column in the paper.It\\u00e2\\u0080\\u0099s '
               'important to have a beat. {0.SimFirstName} '
               'didn\\u00e2\\u0080\\u0099t actually have any knowledge of '
               '{M0.his}{F0.her} beat before {M0.he}{F0.she} started writing '
               'about it, but if you sound convincing, you are convincing. The '
               'readers will never catch on! The secret? Use lots of big '
               'words.sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=75,
          lineno=288,
          tokens=248,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a writer for the the paper, writing '
               'articles.Writer_Track2_AuthorIt\\u00e2\\u0080\\u0099s not like '
               '{0.SimFirstName} can\\u00e2\\u0080\\u0099t write longer '
               'stories, it\\u00e2\\u0080\\u0099s just that {M0.he}{F0.she} '
               'doesn\\u00e2\\u0080\\u0099t want to! Long stories are '
               'overrated. Who has the attention span for all that? And novels '
               'just end up getting adapted into movies anyway, and '
               '{0.SimFirstName}\\u00e2\\u0080\\u0099s pretty busy already, '
               'so....sentient_sims_description{sim_name} works as a writer '
               'writing short stories.Most novelists don\\u00e2\\u0080\\u0099t '
               'go crazy alone in deserted hotels in the winter. Most '
               'novelists don\\u00e2\\u0080\\u0099t die penniless in the '
               'streets. Most novelists are happy, well-adjusted, and '
               'creatively satisfied people! {0.SimFirstName} keeps telling '
               '{M0.himself}{F0.herself} that....'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=76,
          lineno=300,
          tokens=233,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='sentient_sims_description{sim_name} works as a writer writing '
               'novels.The fans love {0.SimPronounObjective}. The critics hate '
               '{0.SimPronounObjective}. {0.SimFirstName} might be churning '
               'out sub-literate dreck, but {M0.his}{F0.her} books sell like '
               'crazy, so {M0.his}{F0.her} publisher keeps paying '
               '{0.SimPronounObjective}. And that\\u00e2\\u0080\\u0099s the '
               'real measure of literary success. Right?  '
               'sentient_sims_description{sim_name} works as a writer writing '
               'novels, and has written a few semi successful '
               'novels.Bestselling authors have a tough life-going from talk '
               'show to talk show, receiving honors, counting endless stacks '
               'of money-but {0.SimFirstName} has worked hard to join their '
               'ranks. Of course if the critics don\\u00e2\\u0080\\u0099t like '
               '{M0.his}{F0.her} next book {M0.his}{F0.her} career will be '
               'over, but no pressure. sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=77,
          lineno=310,
          tokens=236,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a writer writing bestselling novels, '
               "people know {sim_name}'s books.The hardest part about creating "
               'a sprawling, multi-volume fantasy epic? Thinking up all those '
               'crazy names like Cloydon DeBarboot and Frimzy Peppernoodle. '
               'Definitely the names. Oh, and also dealing with the really '
               'strange, inappropriate '
               'fanfic.sentient_sims_description{sim_name} works as a writer '
               'and is a household name creating multi-volume fantasy epics '
               'and consistently has books on the bestselling authors '
               'list.Writer_Track3_JournalistMunicipal rezoning? Dog-catcher '
               'elections? The local beat isn\\u00e2\\u0080\\u0099t always '
               'glamorous, but at least {0.SimFirstName} can use the power of '
               '{M0.his}{F0.her} job to crush {M0.his}{F0.her} enemies. Now '
               '{M0.he}{F0.she} gets the best restaurant tables and the '
               'cleaners never shrink {M0.his}{F0.her} sweaters. '
               'sentient_sims_description{sim_name} works as a journalist '
               'writing articles on page 2 of the newspaper.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=78,
          lineno=326,
          tokens=246,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{M0.His}{F0.Her} crack reporting skills and snappy writing '
               'have landed {0.SimFirstName} a plum assignment covering '
               'breaking news. Toppling governments! Catastrophic natural '
               'disasters! A pop star with a new haircut! '
               '{0.SimFirstName}\\u00e2\\u0080\\u0099s on the big stories now. '
               'sentient_sims_description{sim_name} works as a journalist '
               'writing articles that make it on the front page of the '
               'newspaper.Investigative JournalistIf '
               '{M0.he}{F0.she}\\u00e2\\u0080\\u0099s lucky, '
               '{M0.he\\u00e2\\u0080\\u0099ll}{F0.she\\u00e2\\u0080\\u0099ll} '
               'be the reporter who cracked the biggest scandal ever. Someone, '
               'somewhere is up to no good, and '
               '{0.SimFirstName}\\u00e2\\u0080\\u0099s determined to find '
               'them. {0.SimFirstName} loves revealing wrongdoing and making '
               'the big money, not always in that order. '
               'sentient_sims_description{sim_name} works as an investigative '
               'journalist, cracking open big scandals and digging up dirt.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=79,
          lineno=336,
          tokens=222,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='sentient_sims_description{sim_name} works as the '
               'editor-in-chief for the newspaper.{0.SimFirstName} has '
               'transcended day-to-day news and now spends {M0.his}{F0.her} '
               'time looking backward\\u00e2\\u0080\\u00a6studying what has '
               'been, and what it all means. Future generations will study '
               '{M0.his}{F0.her} works, and many more will use them as very '
               'fancy doorstops. sentient_sims_description{sim_name} works as '
               'a scribe of history, transcending the day-to-day news and '
               'writing articles that transcend '
               'time.career_Adult_AthleticDelivering liquid nourishment to the '
               "world's biggest sports stars. {0.SimFirstName} will have to be "
               'fast on {M0.his}{F0.her} feet to replenish their thirst. If '
               '{M0.he}{F0.she} fails, the team will '
               'fail.sentient_sims_description{sim_name} works as a '
               'waterperson for athletes, on the sidelines at big games.Locker '
               'Room Attendant'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=80,
          lineno=354,
          tokens=216,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='This is not just about picking up jock-straps. '
               '{0.SimFirstName} will need a positive attitude and to execute '
               'on {M0.his}{F0.her} duties with competence. {M0.His}{F0.Her} '
               'responsibilities include keeping the locker room clean, '
               "supplying players with clean towels, and organizing the team's "
               'equipment.sentient_sims_description{sim_name} works as a '
               'locker room attendant for athletes.A Team Mascot knows how to '
               'keep a crowd excited. Through a variety of expressions and '
               'body movements, {0.SimFirstName} will bring the fans to their '
               'feet to cheer the team on.sentient_sims_description{sim_name} '
               'works as a team mascot for the sports team.Through hard work '
               'and unparalleled leadership, {0.SimFirstName} will deliver '
               'remarkable choreographed dance routines. Fans will watch '
               '{M0.his}{F0.her} team with '
               'amazement.sentient_sims_description{sim_name} works as the '
               'dance team captain for the sports '
               'team.Athletic_Track2_ProfessionalAthlete'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=81,
          lineno=371,
          tokens=216,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='It is time for {0.SimFirstName} to show them what '
               "{M0.he}{F0.she}'s got! {0.SimFirstName} will learn from "
               '{M0.his}{F0.her} coaches, develop {M0.his}{F0.her} skills and '
               'perform because {M0.he}{F0.she} will need to impress the '
               'scouts to get to the next '
               'level.sentient_sims_description{sim_name} works as a minor '
               'leaguer in sports.{0.SimFirstName} is finally playing in the '
               'big leagues! Now {M0.he}{F0.she} is going to need to work '
               'harder than ever to stay there. {M0.He}{F0.She} needs to keep '
               'up on {M0.his}{F0.her} fitness and study the game tape. '
               '{0.SimFirstName} will get {M0.his}{F0.her} shot to make an '
               'impact!sentient_sims_description{sim_name} works as a '
               'professional athlete in sports as a backup.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=82,
          lineno=381,
          tokens=237,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='No longer a bench warmer, now {0.SimFirstName} is playing with '
               'the big boys and earning the big bucks. Fans know who '
               '{M0.he}{F0.she} is now and are recognizing {0.SimFirstName} on '
               'the street. Keep up the hard '
               'work!sentient_sims_description{sim_name} works as a '
               'professional athlete in sports as a starter.{0.SimFirstName} '
               'has been selected to the All Star team! People from everywhere '
               "are asking for {M0.his}{F0.her} autograph. {M0.He}{F0.She}'s "
               'elite on and off the field.sentient_sims_description{sim_name} '
               'works as a professional athlete in sports as an all-start '
               'athlete.{0.SimFirstName} is the most valuable player! The '
               "whole world knows it and it doesn't hurt that {M0.he}{F0.she} "
               'is booked on every talk show to discuss how {M0.he}{F0.she} '
               "achieved success. Everyone is wearing {0.SimFirstName}'s "
               'jersey and {M0.he}{F0.she} is getting tons of endorsement '
               'deals.sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=83,
          lineno=392,
          tokens=243,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a professional athlete in sports as an '
               'all-start athlete that has been nominated as '
               'MVP.{0.SimFirstName} finally made it to the Hall of Fame! '
               '{M0.His}{F0.Her} name will live on forever as being the best '
               'of the best. Record books will contain {M0.his}{F0.her} '
               'athletic feats. Invitations to speaking engagements and book '
               'deals are rolling in\\u00e2\\u0080\\u00a6in other words '
               '{M0.he}{F0.she} finally made it to the top of the '
               'mountain.sentient_sims_description{sim_name} works as a '
               'professional athlete in sports as an all-start athlete that '
               'has been nominated as MVP, and inducted into the hall of '
               'fame.Athletic_Track3_BodyBuilder{0.SimFirstName} will now help '
               'clients to achieve their personal fitness and weight goals. '
               'Using the tools of fitness, from different ways to exercise to '
               'better ways to eat, {M0.he}{F0.she} will pump them up! They '
               'will only go as far as {M0.he}{F0.she} pushes '
               'them!sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=84,
          lineno=404,
          tokens=230,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a professional trainer at the '
               'gym.Professional BodybuilderSay goodbye to that puny body! '
               '{0.SimFirstName} needs to work on {M0.his}{F0.her} fitness to '
               "reach the next level. Don't wimp out! Train, train, train. "
               'Only then will {0.SimFirstName} become the Sim {M0.he}{F0.she} '
               'wants to be!sentient_sims_description{sim_name} works as a '
               'professional bodybuilder.Champion Bodybuilder{0.SimFirstName} '
               'is starting to establish {M0.his}{F0.her} name in the body '
               'building circuit. {0.SimFirstName} has to continue to work out '
               'and eat right and before {M0.he}{F0.she} knows it, '
               '{M0.he}{F0.she} will reach {M0.his}{F0.her} ultimate goal! '
               'There is no stopping {0.SimPronounObjective} '
               'now.sentient_sims_description{sim_name} works as a '
               'professional bodybuilder, and has won championships.Trainer to '
               'the Stars'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=85,
          lineno=418,
          tokens=239,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Time to step up and help out the stars. They will need your '
               'assistance to maintain their looks. A star cannot be flabby or '
               'a skinny minny. They need to look fit and healthy when walking '
               'down the red carpet or auditioning for a '
               'role.sentient_sims_description{sim_name} works as a '
               'professional trainer, training celebrities and high profile '
               'individuals.Celebrity BodybuilderYou are on the cover of all '
               'of the fitness and bodybuilding magazines. Sims want to know '
               'how {0.SimFirstName} got those rock hard abs and tight butt. '
               "{M0.His}{F0.Her} chiseled body didn't come easy. It took tons "
               'of work and there is still room to grow. Keep it '
               'up!sentient_sims_description{sim_name} works as a celebrity '
               'bodybuilder, making money by being on the cover of '
               'magazines.{M0.Mr}{F0.Ms}. Solar SystemYou reached the top of '
               'the mountain and have become {M0.Mr}{F0.Ms}. Solar System. '
               'Your body is your shrine and now you have the trophy and '
               'accolades to go along with it. '
               'Congratulations!sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=86,
          lineno=429,
          tokens=243,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as the best body builder in the world, their '
               'body has become world renowned.career_Adult_SecretAgentBefore '
               '{0.SimFirstName} can conduct international espionage and '
               'eliminate targets, '
               '{M0.he\\u00e2\\u0080\\u0099s}{F0.she\\u00e2\\u0080\\u0099s} '
               'got to process some expense reports. And answer some phones. '
               'The occasional bagel run.... Exciting '
               'stuff!sentient_sims_description{sim_name} works as an intern '
               'for a secret agent agency, doing paperwork and getting '
               'coffee.Intelligence Researcher{M0.His}{F0.Her} security '
               "clearance is pretty low, but {0.SimFirstName}'s still learning "
               "some cool secrets. Since {0.SimFirstName}'s been analyzing "
               "intelligence, {0.SimFirstName}'s learned the real speed limit, "
               'a code word that allows {0.SimPronounObjective} to use any '
               'employees-only restroom, and the truth about the moon landing '
               'in the '
               '30\\u00e2\\u0080\\u0099s.sentient_sims_description{sim_name} '
               'works as an intelligence researcher for a secret agency.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=87,
          lineno=447,
          tokens=222,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Run. Duck. JUDO CHOP THAT BAD GUY RIGHT NOW. {0.SimFirstName} '
               'loves giving orders. {M0.His}{F0.Her} agents will feel safe in '
               '{M0.his}{F0.her} capable hands, and {M0.he}{F0.she} can feel '
               'fulfilled being able to live {M0.his}{F0.her} spy fantasies '
               'vicariously through their '
               'adventures.sentient_sims_description{sim_name} works as an '
               'agent handler for a secret agency.According to movies, as a '
               'field agent {0.SimFirstName} should immediately expect to go '
               'undercover to infiltrate a religious cult, street racing ring, '
               'or beauty pageant. Until then '
               '{M0.he\\u00e2\\u0080\\u0099ll}{F0.she\\u00e2\\u0080\\u0099ll} '
               'be interviewing a lot of tinfoil hat-wearers about the radio '
               'transmitters implanted in their teeth. '
               'Allegedly.sentient_sims_description{sim_name} works as a field '
               'agent for a secret agency.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=88,
          lineno=457,
          tokens=211,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Running major cases is just like running any mid-size '
               'organization. It\\u00e2\\u0080\\u0099s all about managing '
               'personnel, budgets, and the bottom line. The big difference is '
               'that if {0.SimFirstName} fails, the world blows up.  Other '
               'than that, it\\u00e2\\u0080\\u0099s pretty much the '
               'same.sentient_sims_description{sim_name} works as a lead '
               'detective for a secret agency.{0.SimFirstName} feels a deep '
               'sense of patriotism serving the greater good. '
               '{M0.He\\u00e2\\u0080\\u0099s}{F0.She\\u00e2\\u0080\\u0099s} '
               'protecting {M0.his}{F0.her} countrymen from harm, performing a '
               'vital public service. Once these feelings wear off, '
               '{M0.he}{F0.she} can head back into the private sector and '
               'actually make some money.sentient_sims_description{sim_name} '
               'works as a government agent for a secret agency.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=89,
          lineno=467,
          tokens=242,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In the world of a spy, every stranger is a potential assassin. '
               'Every situation is a potential ambush. Fueled with adrenaline, '
               '{0.SimFirstName} lives fast and lives dangerously. '
               '{M0.He}{F0.She} also wears a lot of cool '
               'disguises.sentient_sims_description{sim_name} works as a '
               'secret agent for a secret '
               'agency.SecretAgent_Track2_DiamondAgentsentient_sims_description{sim_name} '
               'works as a spy captain for a secret agency, one of the top '
               'spies.The day that {0.SimFirstName} made Shadow Agent, they '
               'took away {M0.his}{F0.her} thumbprints and '
               'driver\\u00e2\\u0080\\u0099s license. '
               '{M0.He\\u00e2\\u0080\\u0099s}{F0.She\\u00e2\\u0080\\u0099s} a '
               'ghost, a specter, a silent entity slipping through '
               'motion-detecting security systems and floating through '
               'embassies. And sometimes doing a little light '
               'paperwork.sentient_sims_description{sim_name} works as a '
               "shadow agent for a secret agency, they don't exist according "
               'to some governments.Double Diamond Agent'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=90,
          lineno=483,
          tokens=201,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Besides getting to wear a ton of incredible formalwear and sip '
               'drinks with perilously attractive strangers, {0.SimFirstName} '
               'also gets to gamble at foreign casinos with agency money. '
               'Being an international superspy is exactly as amazing as it '
               'sounds.sentient_sims_description{sim_name} works as a double '
               'diamond agent for a secret agency, they are basically James '
               'Bond.SecretAgent_Track3_VillainAfter hitting a ceiling with '
               'the Good Guys, {0.SimFirstName}\\u00e2\\u0080\\u0099s trying '
               '{M0.his}{F0.her} hand at some Evil. Hey, '
               'that\\u00e2\\u0080\\u0099s where the real money is! If it '
               'works out, {M0.he}{F0.she} may switch over to Evil full '
               'time....sentient_sims_description{sim_name} works as a double '
               "agent for a secret agency, they didn't make enough money and "
               'wanted to try their hand at some evil.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=91,
          lineno=495,
          tokens=140,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Working for [redacted], {0.SimFirstName} does a lot of '
               '[redacted] and [redacted]. Sometimes {M0.he}{F0.she} has to '
               '[redacted], but [redacted]. Soon '
               '{M0.he\\u00e2\\u0080\\u0099ll}{F0.she\\u00e2\\u0080\\u0099ll} '
               '[redacted] his medication for poison [redacted] before '
               '[redacted] spinning class and [redacted] steel '
               'drums.sentient_sims_description{sim_name} works as a '
               '[redacted], {sim_name} also does a lot of [redacted] and '
               '[redacted].'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=92,
          lineno=500,
          tokens=246,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='As a villain, {0.SimFirstName} is pretty super! You might even '
               'say '
               '{M0.he\\u00e2\\u0080\\u0099s}{F0.she\\u00e2\\u0080\\u0099s} '
               'a...\\"Supreme\\" Villain. But that '
               'doesn\\u00e2\\u0080\\u0099t mean every day is just stroking '
               'hairless cats and coining catchphrases. '
               'There\\u00e2\\u0080\\u0099s a surprising amount of paperwork '
               'involved! Paperwork and torture. Some days '
               'it\\u00e2\\u0080\\u0099s more paperwork, some days '
               'it\\u00e2\\u0080\\u0099s more torture. Just '
               'depends.sentient_sims_description{sim_name} works as a supreme '
               'super villain, very evil.After serving Good, then Evil, '
               '{0.SimFirstName} has decided to return to the Good side, to '
               'help crime-fighters get into the minds of the truly deranged. '
               'But is {M0.he}{F0.she} really helping, or leading them into a '
               'trap? Can {M0.his}{F0.her} true allegiance ever be known...?'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=93,
          lineno=506,
          tokens=197,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='sentient_sims_description{sim_name} works as a triple agent, '
               'they have decided to to help crime-fighters get into the minds '
               'of the truly deranged.career_Adult_TechGuruLive Chat Support '
               'AgentWelcome to Babysitting 101! {0.SimFirstName} will be '
               'using {M0.his}{F0.her} above-average intelligence for hours of '
               'gentle guidance and virtual handholding, exploring brave new '
               'limits on just how thinly one can veil '
               'sarcasm.sentient_sims_description{sim_name} works as a live '
               'chat support agent.{0.SimFirstName} has entered the exciting '
               'world of QA, the unsung heroes of software development. '
               'It\\u00e2\\u0080\\u0099s the perfect job for people who feel '
               'like they break everything they touch! But hey, better they '
               'break it than the customer, right? '
               'Right??sentient_sims_description{sim_name} works as a QA '
               'tested in software development.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=94,
          lineno=524,
          tokens=212,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Congrats to {0.SimFirstName}! Now, instead of risking life, '
               'limb, and job pointing out the gaping holes in someone '
               'else\\u00e2\\u0080\\u0099s code, {M0.he}{F0.she} gets to put '
               'all semblance of a life aside to program code based on someone '
               'else\\u00e2\\u0080\\u0099s deadlines. At least '
               'there\\u00e2\\u0080\\u0099s a benefits '
               'package!sentient_sims_description{sim_name} works as a code '
               'monkey.sentient_sims_description{sim_name} works as a software '
               'engineer.{0.SimFirstName} has finally achieved the glory of '
               'middle management! {M0.He}{F0.She} gets to drive the schedule, '
               'squeeze hundreds of programming hours out of each week, work '
               'magic with budgets and play the {M0.jerk}{F0.ice queen} '
               'everyone else gets to whine '
               'about.sentient_sims_description{sim_name} works as a project '
               'manager for software engineers.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=95,
          lineno=538,
          tokens=211,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName}\\u00e2\\u0080\\u0099s got real power now. '
               '{M0.He}{F0.She} doesn\\u00e2\\u0080\\u0099t just manage measly '
               'one-off projects, {M0.he}{F0.she} is in charge of the '
               'development process for several groundbreaking products. Aye, '
               'aye, this is going to be '
               'fun!sentient_sims_description{sim_name} works as a lead '
               'developer for software engineers.TechGuru_Track2_GamingAs an '
               'amateur cyberathlete, {0.SimFirstName}\\u00e2\\u0080\\u0099s '
               'world is about to change. After a lifetime of training within '
               'the dimly lit confines of bedrooms and basements, '
               '{0.SimFirstName} is ready to travel the world and go '
               'head-to-head in dimly lit indoor stadiums. {M0.His}{F0.Her} '
               'time is now.sentient_sims_description{sim_name} works as an '
               'esports competitor.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=96,
          lineno=550,
          tokens=220,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Fantasy, meet reality. {0.SimFirstName} is actually making a '
               'living playing games competitively. Sure, {M0.he}{F0.she} '
               'isn\\u00e2\\u0080\\u0099t exactly pulling in six figures yet, '
               'but the bounty\\u00e2\\u0080\\u0099s getting bigger, and the '
               'sponsors are taking note. Time to invest in media '
               'training!sentient_sims_description{sim_name} works as a pro '
               'gamer.APM {F0.Queen}{M0.King}With practice comes speed, and '
               '{0.SimFirstName}\\u00e2\\u0080\\u0099s real-time strategy '
               'skills are living proof. With APM climbing past the 400 mark, '
               '{0.SimFirstName} has been known to assemble an army, equip it, '
               'construct an impenetrable base and annihilate at least one '
               'other race in the time it takes most people to tie their '
               'shoes.sentient_sims_description{sim_name} works as a world '
               'renowned pro gamer with an APM above 400.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=97,
          lineno=560,
          tokens=249,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='WOOT! {0.SimFirstName} is now rolling in dough, and '
               '{M0.he}{F0.she} doesn\\u00e2\\u0080\\u0099t have too many '
               'complaints about being famous either. Sponsors are picking up '
               'tabs left and right, there are Simoleons to be made by '
               'streaming {M0.his}{F0.her} practice sessions, and the '
               'tournament prizes are nothing to sneeze at. This is the dream '
               'of gamers everywhere!sentient_sims_description{sim_name} works '
               'as a world renowned pro championship gamer, having won many '
               'world titles.TechGuru_Track3_StartUpAt last, {0.SimFirstName} '
               'has ditched big company bureaucracy to launch {M0.his}{F0.her} '
               'very own company, founded on {M0.his}{F0.her} very own ideals, '
               'to build {M0.his}{F0.her} very own innovative solution. The '
               'only hitch? {M0.His}{F0.Her} very own money is not quite '
               'enough to get this thing off the '
               'ground.sentient_sims_description{sim_name} works as a startup '
               'that they founded themselves, barely scraping by.Independent '
               'Consultant'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=98,
          lineno=572,
          tokens=195,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} is making a name for {M0.himself}{F0.herself} '
               'in the tech world, but the cash from selling off '
               '{M0.his}{F0.her} first company is already getting thin. '
               'Instead of bowing to someone else\\u00e2\\u0080\\u0099s '
               'vision, {M0.he}{F0.she} decides to earn money as a consultant '
               'for private investors.sentient_sims_description{sim_name} '
               'works as an independent consultant in software engineering, '
               'the money from previously selling off their first company is '
               'wearing thin.With an impressive track record for successfully '
               'launching companies, {0.SimFirstName} is always on the go and '
               'never off the grid, making split-second decisions by text on '
               'everything from development to creative to UI. Remarkably, '
               'people listen!sentient_sims_description{sim_name} works as a '
               'Serial Entrepreneur and Visionary Leader, consulting for top '
               'tech companies.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=99,
          lineno=582,
          tokens=240,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Whiz kid. Wonder. Visionary. {0.SimFirstName} has been called '
               'them all, and {M0.he}{F0.she} is confident {M0.he}{F0.she} '
               'deserves it. Everything {M0.he}{F0.she} touches turns to gold. '
               'Doors open when {M0.he}{F0.she} so much as glances at them. '
               'And technologies only emerge with {M0.his}{F0.her} '
               'permission.sentient_sims_description{sim_name} works as a '
               'Startup Genius, consulting for top leaders in tech helping '
               'grow '
               'startups.career_Deliveries_FoodDeliveryNPCcareerTrack_Deliveries_FoodDeliveryNPCZoomers '
               'Food DeliveryPersonsentient_sims_description{sim_name} works '
               'as a food delivery person.career_Adult_EntertainerIf a joke is '
               'told in a comedy club, and nobody\\u00e2\\u0080\\u0099s there '
               'to hear it, does it make a sound? As an amateur entertainer, '
               '{0.SimFirstName} is about to find out. At least there are no '
               'hisses or projectiles!sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=100,
          lineno=600,
          tokens=217,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} writes jokes in their free time as an amateur '
               'entertainer.{0.SimFirstName} was born to perform. '
               'It\\u00e2\\u0080\\u0099s written in the stars! Of course, with '
               'the stars as {M0.his}{F0.her} only reference, open mics are '
               '{0.SimFirstName}\\u00e2\\u0080\\u0099s only viable path to '
               'discovery and fame. The hardest part is suffering all these '
               'amateurs who can only book open '
               'mics!sentient_sims_description{sim_name} does open-mic '
               'standup.C-List is better than no list at all! Why, '
               '{0.SimFirstName} is even starting to book a few gigs. At this '
               'point, {M0.his}{F0.her} ability to shamelessly promote '
               '{M0.himself}{F0.herself} may be a greater asset than any true '
               'talent!sentient_sims_description{sim_name} works as a C-list '
               'standup artist, getting small gigs in clubs.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=101,
          lineno=614,
          tokens=166,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Doors are starting to open for {0.SimFirstName}. And '
               '{M0.he}{F0.she} is starting to open for some pretty cool acts. '
               'Audiences actually laugh when they\\u00e2\\u0080\\u0099re '
               'supposed to. Applause is not unheard of (or unheard). It may '
               'not be time to try the old '
               '\\u00e2\\u0080\\u009cDon\\u00e2\\u0080\\u0099t you know who I '
               'am?\\u00e2\\u0080\\u009d trick yet, but '
               'it\\u00e2\\u0080\\u0099s '
               'coming....sentient_sims_description{sim_name} works as a '
               'standup comedian and has started opening for bigger named '
               'comedians as the opening act.Entertainer_Track2_Music'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=102,
          lineno=621,
          tokens=110,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Who needs name recognition when everyone recognizes your song? '
               '{0.SimFirstName} will be busy creating jingles that lodge '
               'themselves into people\\u00e2\\u0080\\u0099s brains so '
               'tightly, it would take highly invasive surgery to get them '
               'back out. So what if they\\u00e2\\u0080\\u0099re about cat '
               'food, or toilet cleaner? No one can flush them away, not '
               'ever!sentient_sims_description{sim_name} works as a music '
               'artist creating jingles for commercials and radio commercials.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=103,
          lineno=626,
          tokens=173,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} has always known that {M0.he}{F0.she} is more '
               'than just a {M0.hunk of love}{F0.pretty face}. '
               '{M0.He\\u00e2\\u0080\\u0099s}{F0.She\\u00e2\\u0080\\u0099s} '
               'got TALENT. And the instant {M0.his}{F0.her} fingers touch the '
               'keys of a piano or the strings of a guitar, everyone in the '
               'room knows it. These days, '
               '{M0.he\\u00e2\\u0080\\u0099s}{F0.she\\u00e2\\u0080\\u0099s} '
               'even got gigs to prove it.sentient_sims_description{sim_name} '
               'works as a serious musician, booking small gigs.Professional '
               'Pianist'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=104,
          lineno=631,
          tokens=242,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='From posh private parties to shopping mall foyers to weddings '
               'for the web-date weary, {0.SimFirstName} is in high demand. '
               'Whether {M0.his}{F0.her} client wants guests to dance, buy '
               'hopelessly expensive trinkets, or pipe down until they say '
               "their vows, {0.SimFirstName}'s got the tunes to get "
               'results.sentient_sims_description{sim_name} works as a '
               'professional pianist, from post parties to shoping mall foyers '
               'or weddings, {sim_name} is in high demand.Symphonic String '
               'PlayerAll the world\\u00e2\\u0080\\u0099s a stage, and '
               '{0.SimFirstName} has earned {M0.his}{F0.her} place upon it. '
               '{M0.He}{F0.She} is still putting bread in {M0.his}{F0.her} jar '
               'playing weddings and private parties, but the guest list and '
               'grub is getting better every time, and {M0.he}{F0.she} '
               'occasionally lifts {M0.his}{F0.her} spirits with satisfying '
               'stints in lesser-known symphony '
               'orchestras.sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=105,
          lineno=637,
          tokens=237,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a professional musician in less known '
               'symphony orchestras.Strings, winds, woods, brass. '
               '{0.SimFirstName} has mastered them all, and {M0.his}{F0.her} '
               'remarkable gifts are remarked upon quite often. Fame is '
               "{0.SimPronounPossessiveIndependent}, and {0.SimFirstName}'s "
               'working on fortune. Just not enough fortune for '
               '{0.SimPronounObjective} to say no to that web startup launch '
               'party.sentient_sims_description{sim_name} works as a '
               'professional musician, knowing many and all instruments, their '
               'remarkable gifts are remarked upon quite often.Bravo, '
               '{0.SimFirstName}! {M0.He}{F0.She} will bring the crowd to its '
               'feet at nearly every sold-out performance. Applause? Roses? '
               'Room keys? These things are offered up to {0.SimFirstName} on '
               'a regular basis now. '
               'Encore!sentient_sims_description{sim_name} works as a '
               'professional musician who has mastered their craft, they are '
               'known to bring the crowd to its feet at nearly every sold out '
               'performance.Entertainer_Track3_Comedy'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=106,
          lineno=653,
          tokens=178,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='The ideas are really flowing for {0.SimFirstName} now. On '
               'stage, off stage, at weddings, at funerals. Everything is a '
               'source for hilarious new material! And who '
               'doesn\\u00e2\\u0080\\u0099t like a good '
               'joke?sentient_sims_description{sim_name} works as a standup '
               'comedian and comedy writer of jokes.Wow, {0.SimFirstName} can '
               'really keep a crowd captive, no handcuffs required! '
               '{M0.He}{F0.She} is spending less time peddling business cards '
               'and more time practicing one-liners, '
               '\\u00e2\\u0080\\u009csquirrel walks into a '
               'bar\\u00e2\\u0080\\u009d jokes, and impressions that people '
               'actually recognize.sentient_sims_description{sim_name} works '
               'as a standup comedian and is great at telling comedic stories.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=107,
          lineno=663,
          tokens=204,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} is doing a stand-up job with {M0.his}{F0.her} '
               'stand-up routine, and people are starting to stand up and take '
               'notice. Good thing {0.SimFirstName} can cut them back down '
               'with a few quick jokes! ({M0.His}{F0.Her} jokes are better '
               'than these.)sentient_sims_description{sim_name} works as a '
               'standup comedian and is rising to fame.{0.SimFirstName} is '
               'done flying under the radar. {M0.He}{F0.She} is making some '
               'serious dough hosting charity events, awards ceremonies, '
               'roasts, and pretty much any other kind of party no one '
               'actually wants to attend. {M0.He}{F0.She} may even be Sim of '
               'Honor at a cheapskate celebrity '
               'wedding!sentient_sims_description{sim_name} works as a standup '
               'comedian and roast master, reaching fame and participating in '
               'award ceremonies, roasts and other celebrity events.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=108,
          lineno=673,
          tokens=233,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Just like that, {0.SimFirstName} is the big name on the '
               'marquee! Up-and-coming acts are excited to open for '
               '{0.SimPronounObjective}. The work is steady, pays well, and '
               '{0.SimFirstName} has even caught a few people on the street '
               'referencing {M0.his}{F0.her} material and cracking each other '
               'up. Not bad!sentient_sims_description{sim_name} works as a big '
               'name famous comedian selling out shows across tours in the '
               'country.Joke by joke, {0.SimFirstName} has climbed the ranks '
               'of comedy, and now {M0.his}{F0.her} sets are setting new '
               'standards in the industry. An entire generation of comics will '
               'one day point back to {0.SimFirstName} as their inspiration. '
               '{0.SimFirstName} is rolling in dough, fame, and '
               'fans.sentient_sims_description{sim_name} works as a world '
               'renowned famous comedian selling out stadiums across the '
               'country and is a household name in comedy in TV, movies and '
               'pop culture.career_Teen_FastFoodTeen_FastFood_Track1'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=109,
          lineno=687,
          tokens=193,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Everyone has to start somewhere, and this '
               'won\\u00e2\\u0080\\u0099t be so bad. I mean sure, '
               '{0.SimFirstName} will come home smelling like '
               'fried\\u00e2\\u0080\\u00a6something\\u00e2\\u0080\\u00a6and '
               '{M0.his}{F0.her} hands will reek of mildewed rags, but at '
               'least '
               '{M0.he\\u00e2\\u0080\\u0099ll}{F0.she\\u00e2\\u0080\\u0099ll}  '
               'get to see {M0.his}{F0.her} friends! Sort of. While '
               '{M0.he\\u00e2\\u0080\\u0099s}{F0.she\\u00e2\\u0080\\u0099s} '
               'wearing a paper hat.sentient_sims_description{sim_name} works '
               'at a fast food chain cleaning tables.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=110,
          lineno=692,
          tokens=242,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Congratulations, {0.SimFirstName} has moved up in the world '
               'and is earning a smidge more every hour! A whole smidge! Now, '
               'instead of just being treated like {M0.he}{F0.she} is '
               'invisible, {M0.he}{F0.she} really is out of sight of the '
               'customers, focusing {M0.his}{F0.her} attention solely on hot '
               'grease and triple orders.sentient_sims_description{sim_name} '
               'works at a fast food chain as a fry cook.Food Service '
               'CashierSweet, sweet Simoleons! '
               '\\u00c2\\u00a7\\u00c2\\u00a7\\u00c2\\u00a7! {0.SimFirstName} '
               'has earned enough trust to handle the Simoleons and the people '
               'who spend them. \\"Service with a smile,\\" {M0.his}{F0.her} '
               'manager always says, so {0.SimFirstName} takes orders, presses '
               'buttons, and grins until {M0.his}{F0.her} cheeks '
               'hurt.sentient_sims_description{sim_name} works at a fast food '
               'chain as a cashier.career_Adult_Business'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=111,
          lineno=706,
          tokens=240,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Far from the days when postal correspondence was the lifeblood '
               "of a thriving business, today's mailrooms have been made all "
               "but obsolete with the rise of email. Still, somebody's gotta "
               'distribute all the online shopping deliveries! '
               '{0.SimFirstName} will have to keep {M0.his}{F0.her} energy '
               'level up to get noticed... and elevated from the mailroom. '
               '{M0.He}{F0.She} can now Fill Out Reports on the computer and '
               'Gossip About Office '
               'Romances.sentient_sims_description{sim_name} works as a mail '
               "room technician at a business.It's amazing how much assistance "
               'an office needs. The more energy {0.SimFirstName} has, the '
               "more {M0.he}{F0.she}'ll get done. The better {M0.his}{F0.her} "
               "social skills, the more recognition {M0.he}{F0.she}'ll "
               'receive.sentient_sims_description{sim_name} works as an office '
               "assistant.Assistant to the ManagerIt's not quite management "
               "track, but it's the next best thing, isn't it? After all, the "
               'manager only has one assistant...sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=112,
          lineno=717,
          tokens=201,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as an assistant to the manager in a '
               "business.This is it... almost. Ok, so {0.SimFirstName}'s not a "
               "manager, yet. Surely {M0.he}{F0.she}'s next in line for the "
               "position. It's time to build those people skills for when "
               '{M0.he}{F0.she} has people to boss about, er... '
               'manage.sentient_sims_description{sim_name} works as an '
               "assistant manager in a business.{0.SimFirstName}'s the "
               '{M0.man}{F0.woman} now! ... Or at least the manager of a '
               "region of the company. That means {M0.he}{F0.she}'s got to "
               'keep working on {M0.his}{F0.her} people skills if '
               '{M0.he}{F0.she} wants an even bigger slice of the '
               'pie.sentient_sims_description{sim_name} works as a regional '
               'manager in a business.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=113,
          lineno=731,
          tokens=190,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} has proved {M0.himself}{F0.herself} as a '
               "manager, but {M0.he}{F0.she}'s got {M0.his}{F0.her} sights set "
               'on the next level. Whether {M0.he}{F0.she} wants to be an '
               "executive or a financial whiz, it's time to put the effort in "
               'and make it happen.sentient_sims_description{sim_name} works '
               'as a senior manager in a business, managing multiple '
               'regionsBusiness_Track2_Managementsentient_sims_description{sim_name} '
               'works as the vice-president in a business.The corner office is '
               "{0.SimFirstName}'s. Everyone looks to {M0.him}{F0.her} for "
               'leadership. Too bad the CEO still calls the shots, but '
               'someday...sentient_sims_description{sim_name} works as the '
               'president in a business.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=114,
          lineno=747,
          tokens=202,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='This is it: the big chair. {0.SimFirstName} makes the moves '
               'and {M0.he}{F0.she} calls the shots. It feels good to be the '
               "{M0.king}{F0.queen}, doesn't it? Well, it probably would if "
               "{M0.he}{F0.she} didn't have the board of shareholders "
               'breathing down {M0.his}{F0.her} neck for results all '
               'day.sentient_sims_description{sim_name} works as the CEO in a '
               'business.{0.SimFirstName} used to run a company, and now '
               "{0.SimFirstName} runs several. Fortunately, {M0.he}{F0.she}'s "
               "got smart folks in key positions, so {M0.he}{F0.she}'s got "
               'more free time to enjoy life... and the private '
               'jet.sentient_sims_description{sim_name} works on the boards of '
               'multiple fortune 500 businesses.Business_Track3_Investor'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=115,
          lineno=759,
          tokens=230,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='BLT season coming up? Time to invest in pork belly futures. '
               "Commodities are the name of the game, and it's "
               "{0.SimFirstName}'s job to know what's going to be hot "
               'tomorrow. Keeping an eye on the stock market will help '
               '{0.SimPronounObjective} make {M0.his}{F0.her} '
               'mark.sentient_sims_description{sim_name} works as a futures '
               "trader.It's not actually about hedging; it's about leverage: "
               "maximizing returns on your clients' investments. If "
               "{0.SimFirstName} maximizes enough, there's a sizeable chunk in "
               'it for {M0.him}{F0.her}.sentient_sims_description{sim_name} '
               'works as a hedge fund manager.{0.SimFirstName} is a big game '
               'hunter, and corporations are {M0.his}{F0.her} prey. Mergers '
               'and acquisitions are {M0.his}{F0.her} weapons, and good luck '
               'to any straggling executives or minority shareholders that '
               'wander into {M0.his}{F0.her} sights.sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=116,
          lineno=770,
          tokens=172,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a corporate raider, making hostile '
               "takeover bids of companies.{0.SimFirstName}'s made "
               '{M0.his}{F0.her} mark on the business world. Now, all '
               '{M0.he}{F0.she} has to do is find the next guy or gal about to '
               'make his or her mark, back them, and wait for their hard work '
               'to pay off.sentient_sims_description{sim_name} works as an '
               'angel investor.career_Adult_CulinaryAssistant DishwasherTime '
               'to do the work of a common household appliance! '
               '{0.SimFirstName} will be scrubbing plates, ensuring crystal '
               'glasses have no leftover lipstick residue, and striking up '
               "conversations with Sims who couldn't pay their "
               'tab!sentient_sims_description{sim_name} works as an assistant '
               'dishwasher in a restaurant.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=117,
          lineno=788,
          tokens=240,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='As the Head Dishwasher, {0.SimFirstName} can choose which '
               'dishes {M0.he}{F0.she} wants to wash. Hard to scrub pots and '
               'pans are no longer an issue, unless {0.SimFirstName} wants '
               'them to be. Only the most beautiful china are now placed in '
               '{0.SimFirstName}\\u00e2\\u0080\\u0099s '
               'hands.sentient_sims_description{sim_name} works as the head '
               'dishwasher in a restaurant.Standing behind food stations '
               "unable to eat the food is never easy, but it's the new reality "
               'for {0.SimFirstName}. {M0.His}{F0.Her} days will now be filled '
               'with ridiculous dancing at weddings, failed team-building '
               'exercises, and really weird baby shower '
               'games.sentient_sims_description{sim_name} works as a caterer '
               'server at a restaurant.The secret to Mixology is proportion. '
               'How much sweet juice? How much sour juice? Does this troubled '
               "patron want {0.SimFirstName}'s advice, or just for someone to "
               'listen? Is this a real job, or just something people do for '
               'money until they find a real job?sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=118,
          lineno=799,
          tokens=240,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a mixologist and bartender at a '
               'restaurant.{0.SimFirstName} is now a Line Cook! '
               '{M0.His}{F0.Her} duties include station setup, prepping food, '
               'cleaning up and stocking. Basically everything the real cooks '
               "don't want to do!sentient_sims_description{sim_name} works as "
               'a line cook at a restaurant.Culinary_Track2_ChefThe world of '
               'private parties now belongs to {0.SimFirstName}! Forget the '
               'small-time events, now {M0.he}{F0.she} gets to enjoy '
               'short-deadline corporate events, birthday parties for children '
               'with more money than {M0.he}{F0.she} has, and incredibly '
               'particular brides!sentient_sims_description{sim_name} works as '
               'a head caterer at a restaurant, servicing small and corporate '
               'events.Pastries are a tricky thing to master. They must be '
               'delicious enough to justify the calories, but also beautiful '
               "enough to catch the customer's eye. {0.SimFirstName} is "
               'branching out into real food '
               'artistry!sentient_sims_description{sim_name} works as a pastry '
               'chef.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=119,
          lineno=820,
          tokens=249,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Second-in-command isn't bad at all! Now {0.SimFirstName} can "
               'do some REAL work without getting any of the credit. But hey, '
               'with a little time and a lot of effort {0.SimFirstName} will '
               'be the one running things around '
               'here!sentient_sims_description{sim_name} works as a sous chef '
               'at a restaurant.Congratulations to {0.SimFirstName}! '
               '{M0.He}{F0.She} is now the master of the kitchen. Yelling at '
               'underlings, demanding things be re-cooked, screaming at '
               "underlings, reprimanding underlings -- it's all possible "
               'now!sentient_sims_description{sim_name} works as an executive '
               'chef at a restaurant.Some might say {0.SimFirstName} has sold '
               'out to gain mainstream status, but {0.SimFirstName} cannot '
               'hear them. {M0.He}{F0.She} is relaxing in {M0.his}{F0.her} '
               'private\\u00c2\\u00a0office, eating hors '
               'd\\u00e2\\u0080\\u0099oeurves in front of the fireplace, and '
               'considering the latest contract for a new TV show, cook book, '
               'and servingware line.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=120,
          lineno=831,
          tokens=231,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='sentient_sims_description{sim_name} works as a celebrity chef, '
               'opening restaurants and appearing on '
               'TV.Culinary_Track3_BartenderA master of doling out advice and '
               'a master of mixing fruity drinks, {0.SimFirstName} is now the '
               'Head Mixologist! It might be time to start charging therapist '
               'rates...sentient_sims_description{sim_name} works as the head '
               'bartender at a restaurant.A drink specialist at a nearly '
               'divine level, {0.SimFirstName} will be helping clients pair '
               'mixed drinks with a variety of meals and desserts. They may '
               'swoon as their tastebuds are overwhelmed by a culinary WooHoo '
               'of flavors.sentient_sims_description{sim_name} works as the '
               'juice boss, the head bartender helping clients pair mixed '
               'drinks with a variety of meals and desserts.Chief Drink '
               'OperatorCoordinating orders at a corporate level is no easy '
               'feat, but {0.SimFirstName} is ready to be the next big CDO. '
               '{M0.His}{F0.Her} high-demand drinks are now made in large '
               'batches and are then shipped out to various '
               'restaurants.sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=121,
          lineno=848,
          tokens=246,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works distributing their custom cocktails and '
               'selling them to restaurants, bars and corporate '
               'events.{0.SimFirstName} has really proven '
               '{M0.himself}{F0.herself} when it comes to concocting amazing '
               'drinks. Students from all over the world will flock to '
               '{M0.his}{F0.her} side, eager to learn from The Great '
               'Drinkmaster! There will be magic. Oh yes.\\\\nThere will be '
               'magic.sentient_sims_description{sim_name} works distributing '
               'their name brand cocktails and selling them in big box '
               'stores.Celebrity MixologistSome might say {0.SimFirstName} has '
               'sold out to gain mainstream status, but {0.SimFirstName} '
               'cannot hear them. {M0.He}{F0.She} is relaxing in '
               '{M0.his}{F0.her} private\\u00c2\\u00a0office, sipping an '
               'amazing drink in front of the fireplace, and considering the '
               'latest contract for a new TV show, cook book, and glassware '
               'line.sentient_sims_description{sim_name} works as a celebrity '
               'mixologist, advertising their celebrity hard alcohol in '
               'mainstream media.career_Adult_StyleInfluencer'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=122,
          lineno=863,
          tokens=228,
          depth=7,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='careerTracks_StyleInfluencer_Track1Every fashion journey '
               "begins somewhere, and for you, it's the first stitch. While "
               'more prestigious individuals will cover the clothing of the '
               '\\"haute couture,\\" you\'ll be tasked with words regarding '
               'the \\"not for sure.\\"sentient_sims_description{sim_name} '
               'works as a youtube commentator with a very small channel, '
               'commenting on anything they can talk about.Consignment '
               'CommentatorItems must find new homes and all parties must be '
               "contended with the arrangment. You've been consigned to "
               'consult, critique, and clarify the needs of clothes seeking '
               'new persons to adorn.sentient_sims_description{sim_name} works '
               'as a consignment commentator, sorting through consignment '
               'clothes and finding them new homes.Everything that adorns must '
               "be reviewed as it's worn. Your task as you type is to "
               'concisely or verbosely describe every thread and button as it '
               'pertains to your ever growing '
               'audience.sentient_sims_description{sim_name} works as a '
               'Fashion Descriptive Analyst, writing the descriptions for '
               'clothing online to be sold and writing clothing reviews online '
               'for a growing audence.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=123,
          lineno=881,
          tokens=221,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="It isn't just the top, the bottom, the shoes, or the "
               "accessories, but how it all arrives and sits together. You're "
               "now focused on the meta appearance and it's the right outfit "
               'for you.sentient_sims_description{sim_name} works as an '
               'Ensemble Author, writing about meta appearance and fashion '
               'online for a growing audience.As clothing ascends beyond '
               'material warmth and personal style, it enhances the cultural '
               "notes of its bearer. You've come to capture that, at this "
               'precise moment, for all to '
               'read!sentient_sims_description{sim_name} works as a culture '
               'columnist, writing about cultural notes and fashion online for '
               'a fairly large '
               "audience.careerTracks_StyleInfluencer_Track2_TrendSetterIt's "
               'key to deeply understand the fundamentals of poshness in order '
               'to profile prodigiously for a plethora of potential clients, '
               'patrons, and avid '
               'fashionistas.sentient_sims_description{sim_name} works as a '
               'Posh Profiler, writing about poshness in order to profile '
               'prodigiously for a plethora of potential clients, patrons, and '
               'avid fashionistas.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=124,
          lineno=898,
          tokens=219,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='As a stand out in the fashion forward industry, the principals '
               'of fashion, first, and always, has never been more pertinent. '
               'These trends begin and end with quality '
               'threads.sentient_sims_description{sim_name} works as a Fashion '
               'Figure, as a stand out in the fashion forward industry, the '
               'principals of fashion, first, and always, has never been more '
               'pertinent.The superlative is wielded cautiously in this case, '
               'as the task of helping others with clear, concise, and '
               'insightful guidance is not something a merely comparative '
               'title can entertain.sentient_sims_description{sim_name} works '
               'as a trend recommender, recommending fashion and helping '
               'others with clear, concise and insightful guidance to a large '
               "social media following.Who? What? It's neither of these, but "
               'simply It. The one to whom others look for information, '
               'inspiration, and tantalization, an It Sim is THE Sim all '
               'about...it.sentient_sims_description{sim_name} works as a '
               'fashionista, they are IT in fashion, the one to whom others '
               'look for information, inspiration, and tantalization.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=125,
          lineno=913,
          tokens=239,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="After years of work, it's come to this. Being it, being best, "
               "figuring into things, as an Icon O'Class, the session has "
               'begun and this world will never be the '
               'same.sentient_sims_description{sim_name} works as a '
               'fashionista icon, they are the best, and are a world '
               'trendsetter in '
               'fashion.careerTracks_StyleInfluencer_Track3_StylistA good day '
               'begins with the right clothes and a great night kicks off with '
               'serious duds. Pontificating seriously about each button and '
               'wily zipper is the dedicated pursuit of a Dedicated '
               'Dresser.sentient_sims_description{sim_name} works as a '
               'dedicated dresser, helping dress and suggest fashion '
               'online.There are surface level considerations, but then there '
               "are also ones that go deeper. It's key to thread that needle "
               'and dip just beneath the surface to learn to mastery the ways '
               'of the textiles.sentient_sims_description{sim_name} works as a '
               'textile tactician, helping dress and suggest fashion '
               "online.True magic doesn't require a wand, but a coat hanger in "
               'either hand holding a carefully considered piece of attire. '
               'Bring a spell to every wardrobe!sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=126,
          lineno=931,
          tokens=155,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a Wardrobe Wiz, helping dress and suggest '
               'fashion online.Make-Over Miracle WorkerWhen others need help, '
               "you're tasked to the cause. With emergent attire suggestions "
               "and ad hoc advice, you'll need to Make-Over any material "
               'need.sentient_sims_description{sim_name} works as a Make-Over '
               'Miracle Worker, helping dress and suggest fashion and making '
               'over clients.Who is someone? Does it boil down to their '
               'essence of dress? Or their stint of thought? All of that will '
               "ultimately come down to you as you re-imagine one's "
               're-emergent needs.sentient_sims_description{sim_name} works as '
               'a Persona Re-Imager, helping dress and completely make over '
               'clients.Coffee Stain Remover'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=127,
          lineno=949,
          tokens=217,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='This is {0.SimFirstName}\\u00e2\\u0080\\u0099s first step into '
               'the exciting world of caffeine distribution systems. But of '
               'course {M0.he}{F0.she} can\\u00e2\\u0080\\u0099t be '
               'responsible for pouring coffee until {M0.he}{F0.she} proves '
               '{M0.he}{F0.she} can handle mopping floors, setting up chairs, '
               'scrubbing mugs and keeping those frothers and foamers '
               'shiny!sentient_sims_description{sim_name} just started working '
               'at starbucks and is responsible for cleaning.At last, '
               '{0.SimFirstName} can drop the dishrags and become one with the '
               'art of fine coffee! Grinding together the finest organic beans '
               'from around the globe, {0.SimFirstName} is now a master bean '
               'blender, a true mixologist whose arresting combinations of '
               'aggressively bold aromas and subtly nutty undertones please '
               'every palate.sentient_sims_description{sim_name} works at '
               'starbucks and is responsible for helping prep drinks.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=128,
          lineno=959,
          tokens=244,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Bravo! {0.SimFirstName} has ascended the barista ranks and '
               'seized control of the frother. Now in charge of crafting '
               'sumptuous espresso drinks, adorned with a dollop of '
               'feather-light froth which {M0.he}{F0.she} arranges in cute '
               'patterns, {0.SimFirstName} knows '
               '{M0.he}{F0.she}\\u00e2\\u0080\\u0099s a true '
               'artiste.sentient_sims_description{sim_name} works at starbucks '
               'as a '
               'barista.careers_Adult_Freelancer_No_AgencycareerTracks_Freelancer_No_Agency{0.SimFirstName} '
               'has made the decision to be a freelancer. As nice as that '
               "sounds, {M0.he}{F0.she} won't be able to find gigs or get paid "
               'until {M0.he}{F0.she} selects a trade, and an agency to '
               'represent {M0.him}{F0.her}.sentient_sims_description{sim_name} '
               'works as a freelancer, picking up odd jobs here and '
               'there.career_Adult_PartTime_BabysitterPartTime_Babysitter_Track1'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=129,
          lineno=977,
          tokens=246,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} can\\u00e2\\u0080\\u0099t wait to finally '
               'earn some dough-and what could be more fun than getting paid '
               'to play with kids? Besides, the kids are asleep half the time, '
               'right? So it\\u00e2\\u0080\\u0099s basically getting paid to '
               'couch-sit and text all {M0.his}{F0.her} friends. '
               'Cake!sentient_sims_description{sim_name} works as a part-time '
               'baby sitter.At last, {0.SimFirstName} has landed a steady '
               'nanny job with a nearby family. No more searching or '
               'scheduling-just one family with one sweet kid, who '
               '{M0.he}{F0.she} only has to win over once. {0.SimFirstName} '
               'doesn\\u00e2\\u0080\\u0099t remember signing up for cleaning, '
               'toilet scrubbing, or laundry, but as the mother said, since '
               '{M0.he\\u00e2\\u0080\\u0099s}{F0.she\\u00e2\\u0080\\u0099s} '
               'there and getting '
               'paid\\u00e2\\u0080\\u00a6sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=130,
          lineno=983,
          tokens=230,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a part-time nanny.{0.SimFirstName} is '
               'continuing their babysitting adventure by securing a job at '
               "The Munchkin Menagerie's Holding Hands Daycare. Working with a "
               'loving, experienced team of childcare professionals, '
               '{F0.she}{M0.he} will help provide a gentle, caring and '
               'stimulating environment that honors the genius in every '
               'child.sentient_sims_description{sim_name} works as a part-time '
               "daycare administrator at The Munchkin Menagerie's Holding "
               'Hands '
               'Daycare.career_Adult_PartTime_RetailPartTime_Retail_Track1{0.SimFirstName} '
               'is ready to take {M0.his}{F0.her} part in the global economy. '
               'People need to buy things to make the economy happen, and that '
               'means that people need retailers to sell them things, and THAT '
               'means that someone needs to stock a bunch of shelves. Guess '
               'what {0.SimFirstName}\\u00e2\\u0080\\u0099s part '
               'is?sentient_sims_description{sim_name} is working part-time as '
               'a shelf stocker at a department store.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=131,
          lineno=1001,
          tokens=244,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} has been promoted to Sales Floor Clerk! Now '
               '{M0.he}{F0.she} can interact directly with the customers and '
               'brush up on vital salesmanship skills! And between customers '
               '{M0.he}{F0.she} can sweep floors, scrape off gum, heft boxes '
               'and restock store displays.sentient_sims_description{sim_name} '
               'is working part-time as a sales floor clerk at a department '
               'store.\\u00e2\\u0080\\u009cHappy customers, healthy '
               'business!\\u00e2\\u0080\\u009d At least, '
               'that\\u00e2\\u0080\\u0099s what '
               '{0.SimFirstName}\\u00e2\\u0080\\u0099s training manual says. '
               '{M0.He}{F0.She} might be earning a healthier wage, manning the '
               'support desk with a smile, but the only customers who get sent '
               '{M0.his}{F0.her} way are not happy, not at '
               'all.sentient_sims_description{sim_name} is working part-time '
               'as a customer service representative at a department '
               'store.career_Teen_BabysitterTeen_Babysitter_Track1'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=132,
          lineno=1015,
          tokens=244,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} can\\u00e2\\u0080\\u0099t wait to finally '
               'earn some dough-and what could be more fun than getting paid '
               'to play with kids? Besides, the kids are asleep half the time, '
               'right? So it\\u00e2\\u0080\\u0099s basically getting paid to '
               'couch-sit and text all {M0.his}{F0.her} friends. '
               'Cake!sentient_sims_description{sim_name} works as a baby '
               'sitter.At last, {0.SimFirstName} has landed a steady nanny job '
               'with a nearby family. No more searching or scheduling-just one '
               'family with one sweet kid, who {M0.he}{F0.she} only has to win '
               'over once. {0.SimFirstName} doesn\\u00e2\\u0080\\u0099t '
               'remember signing up for cleaning, toilet scrubbing, or '
               'laundry, but as the mother said, since '
               '{M0.he\\u00e2\\u0080\\u0099s}{F0.she\\u00e2\\u0080\\u0099s} '
               'there and getting '
               'paid\\u00e2\\u0080\\u00a6sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=133,
          lineno=1021,
          tokens=217,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a nanny.{0.SimFirstName} has earned back '
               '{M0.his}{F0.her} weekend nights by securing a job at Holding '
               'Hands Daycare. Working with a loving, experienced team of '
               'childcare professionals, {0.SimFirstName} will help provide a '
               'gentle, caring and stimulating environment that honors the '
               'genius in every child.sentient_sims_description{sim_name} '
               'works as a daycare administrator at Holding Hands '
               'Daycare.career_Adult_PartTime_ManualLaborPartTime_ManualLabor_Track1{0.SimFirstName} '
               'has always loved being under the sun! After all, '
               '{F0.she}{M0.he} is strong, energetic, and loves the smell of '
               'freshly cut grass. And grass is green, so simoleons must smell '
               'like grass! That, or lawnmower exhaust. Either way, mowing '
               'lawns is a great work out for '
               '{F0.her}{M0.him}!sentient_sims_description{sim_name} works as '
               'a lawn mower, mowing peoples yards.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=134,
          lineno=1039,
          tokens=245,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} is working {M0.his}{F0.her} way up the ladder '
               'in the landscaping world, flexing not just {M0.his}{F0.her} '
               'muscles, but {M0.his}{F0.her} artistry as well. Sure, '
               '{0.SimFirstName} is mostly working off other '
               'people\\u00e2\\u0080\\u0099s designs-planting, digging, '
               'raking, mowing-but every so often {M0.he}{F0.she} gets to make '
               'a fleeting mark on {M0.his}{F0.her} '
               'clients\\u00e2\\u0080\\u0099 verdant '
               'tableaux.sentient_sims_description{sim_name} works as a '
               'landscaper.Every kid goes through a digging phase, but no tiny '
               'scoop and plastic pail on the beach can ever compare to the '
               'sheer awesomeness of breaking into the earth with a backhoe! '
               'This is a big promotion to operate a big machine, and '
               '{0.SimFirstName} is hoping the big responsibility will '
               'translate into big '
               'Simoleons!sentient_sims_description{sim_name} works as a '
               'backhoe operator in construction.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=135,
          lineno=1049,
          tokens=243,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='career_Adult_CriminalTough {M0.Guy}{F0.Gal}Every criminal '
               'mastermind needs an entry-level bodyguard with irrational '
               'anger issues. {0.SimFirstName} will beef up doorways and '
               'rumble through dark alleys, keeping rivals at bay with those '
               'three little words, \\"Whaddayou lookin\' '
               'at?\\"sentient_sims_description{sim_name} works as an '
               'entry-level body guard for a local criminal.Are those candy '
               'bars in your pocket? Where did you get that lovely '
               'old-lady-style purse? {0.SimFirstName} is now in charge of '
               'outfitting the bosses with snacks for the interrogation room '
               'and birthday gifts for their mother-in-laws, using '
               '{M0.his}{F0.her} five finger '
               'discount.sentient_sims_description{sim_name} works as a '
               'criminal as a petty thief.Switching to management is never '
               'easy. Will your gang remember to rob the bank before it '
               "closes? Can the goon have a sick day when he's scheduled to "
               'work the riot? Fortunately, {0.SimFirstName} knows how to lead '
               'a ring of delinquents into trouble, like a total '
               'boss.sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=136,
          lineno=1064,
          tokens=218,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a ringleader for a local criminal '
               "gang.It's time for {0.SimFirstName} to give up the "
               'misdemeanors. What is {M0.he}{F0.she}, a baby? Time to put on '
               'the big {M0.boy}{F0.girl} pants and pull the big '
               '{M0.boy}{F0.girl} crimes: felonies. Maybe '
               "{M0.he'll}{F0.she'll} even plan a "
               'heist!sentient_sims_description{sim_name} works as a '
               'ringleader for a local criminal gang.Wanna make a deal in this '
               "'hood? You gotta go through {0.SimFirstName}. {M0.He}{F0.She} "
               'worked {M0.his}{F0.her} way up to running the racket on this '
               'turf, from that botanical garden over there, all the way down '
               'to the new organic grocery '
               'store.sentient_sims_description{sim_name} works as a minor '
               'crimelord in the local area.Criminal_Track2_Boss'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=137,
          lineno=1080,
          tokens=241,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='From knocking out armed guards to intimidating rival gangs '
               'with a single arched eyebrow, {0.SimFirstName} is now the '
               "brawn behind the brains.  And {M0.he's}{F0.she's} closer to "
               "the action than ever. Don't mess with "
               '{M0.him}{F0.her}!sentient_sims_description{sim_name} works as '
               'The Muscle for the local crime gang, taking part in the action '
               'of intimidating rival gangs and knocking out armed '
               'guards.{0.SimFirstName} has taken {M0.his}{F0.her} talents '
               'into the mean streets, rocking getaway cars up on two wheels, '
               'hugging corners, running from cops. This stuff would make a '
               'pretty exciting video game!sentient_sims_description{sim_name} '
               'works as the getaway driver for the local crime '
               'gang.{0.SimFirstName} has proven {M0.his}{F0.her} strength and '
               'dexterity. Now, the big bosses have given '
               '{0.SimPronounObjective} a stethoscope, a drill, and a map of '
               'target banks. Doors are finally opening for {0.SimFirstName}. '
               'Literally.sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=138,
          lineno=1091,
          tokens=230,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as the safe cracker for the local crime gang, '
               'helping to break into banks.{0.SimFirstName} has finally '
               'earned {M0.his}{F0.her} PhD... from the STREETS. As the brains '
               'of {M0.his}{F0.her} own organization, {0.SimFirstName} will '
               'plan the big jobs, make the big scores, and bring home the big '
               'Simoleons.sentient_sims_description{sim_name} works as the '
               'brains of the local crime gang, planning heists and bringing '
               "home big scores.What's even better than being The Brains of "
               "the organization? Being The Brains' boss! Now "
               "{0.SimFirstName}'s crew can do all the work, while "
               '{M0.he}{F0.she} takes a bath in \\u00c2\\u00a71000 bills. Who '
               "cares if it's dirty money when there's so much of "
               'it?sentient_sims_description{sim_name} works as the boss of '
               'the local crime gang, the head running '
               'everything.Criminal_Track3_Oraclesentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=139,
          lineno=1107,
          tokens=230,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a thief on the internet, using petty scams '
               'and scripts to make money.{0.SimFirstName} has managed to earn '
               'the respect of other hackers, a group not valued for an '
               'overabundance of respect! They look to {M0.him}{F0.her} for '
               'advice on how to work around the toughest security measures '
               'while covering their '
               'tracks.sentient_sims_description{sim_name} works as an elite '
               'hacker, working for a crime group on the '
               'internet.sentient_sims_description{sim_name} works as the '
               'Anonymous Ghost, a mysterious figure on the internet who '
               'operates in the shadows of the internet targeting online '
               'media, controlling it for a price.{0.SimFirstName} has really '
               'stepped up {M0.his}{F0.her} game.{M0.He}{F0.She} creates '
               'viruses that topple international corporations and incites '
               'civil wars by releasing sensitive government documents (okay, '
               'that second one might have been an '
               'accident).sentient_sims_description{sim_name} works as the Net '
               'Demon, a powerful hacker who wreaks havoc on the internet, '
               'targeting both corporate entities and government '
               'organizations.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=140,
          lineno=1125,
          tokens=216,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Bent on taking down the old world order, a team of top '
               'hackers, ghosts, and demons takes cues from a single source. '
               '{0.SimFirstName} has become the chosen one. {M0.His}{F0.Her} '
               'army of angsty teens and disgruntled introverts has its finger '
               'on the red button controlling '
               'everything.sentient_sims_description{sim_name} works as The '
               'Oracle, the enigmatic leader of a formidable hacker group, '
               'orchestrating operations that challenge the existing power '
               'structures and manipulate global '
               'events.career_Teen_HighSchoolHigh School F StudentOkay, so... '
               'Not every child is going to get school right away. '
               'Don\\u00e2\\u0080\\u0099t worry! Every student starts '
               'somewhere, and with a little effort {0.SimFirstName} will '
               'bring those grades up in no time. Even writing '
               '{M0.his}{F0.her} name on the test is worth a few '
               'points!sentient_sims_description{sim_name} is a highschool '
               'student failing their classes.High School D Student'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=141,
          lineno=1139,
          tokens=180,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='It\\u00e2\\u0080\\u0099s a proud moment in any '
               'kid\\u00e2\\u0080\\u0099s life when they make the transition '
               'from \\u00e2\\u0080\\u009cfailing student\\u00e2\\u0080\\u009d '
               'to \\u00e2\\u0080\\u009cbarely passing '
               'student.\\u00e2\\u0080\\u009d With enough effort, '
               '{0.SimFirstName} will claw {M0.his}{F0.her} way up to '
               '\\u00e2\\u0080\\u009caverage\\u00e2\\u0080\\u009d in no time. '
               'And THAT\\u00e2\\u0080\\u0099S when doors start to '
               'open...sentient_sims_description{sim_name} is a highschool '
               'student failing their classes with Ds.High School C Student'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=142,
          lineno=1144,
          tokens=237,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{0.SimFirstName} can now earn passing grades in all of '
               '{M0.his}{F0.her} subjects easily. But {M0.he}{F0.she} '
               'doesn\\u00e2\\u0080\\u0099t want to stop there! Now that '
               "{0.SimFirstName}'s discovered an aptitude for learning, "
               'it\\u00e2\\u0080\\u0099s time to see how far {M0.he}{F0.she} '
               'can go!sentient_sims_description{sim_name} is a highschool '
               'student barely passing their classes with Cs.High School B '
               'Studentsentient_sims_description{sim_name} is a highschool '
               'student passing their classes with Bs.High School A StudentIt '
               'took a lot of work, but {0.SimFirstName} has turned '
               '{M0.himself}{F0.herself} into an honor-rolling, test-acing, '
               "A-plussing machine. {M0.He}{F0.She}'ll forget more over lunch "
               'than some students will learn in a lifetime. For '
               '{M0.him}{F0.her}, the future is '
               'limitless!sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=143,
          lineno=1154,
          tokens=230,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} is a highschool student doing exceptionally well in '
               'their classes with '
               'As.career_Adult_PartTime_FastFoodPartTime_FastFood_Track1Everyone '
               'has to start somewhere, and this won\\u00e2\\u0080\\u0099t be '
               'so bad. I mean sure, {0.SimFirstName} will come home smelling '
               'like '
               'fried\\u00e2\\u0080\\u00a6something\\u00e2\\u0080\\u00a6and '
               '{M0.his}{F0.her} hands will reek of mildewed rags, but at '
               'least '
               '{M0.he\\u00e2\\u0080\\u0099ll}{F0.she\\u00e2\\u0080\\u0099ll}  '
               'get to see {M0.his}{F0.her} friends! Sort of. While '
               '{M0.he\\u00e2\\u0080\\u0099s}{F0.she\\u00e2\\u0080\\u0099s} '
               'wearing a paper hat.sentient_sims_description{sim_name} works '
               'part-time at a fast food chain cleaning tables.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=144,
          lineno=1167,
          tokens=248,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Congratulations, {0.SimFirstName} has moved up in the world '
               'and is earning a smidge more every hour! A whole smidge! Now, '
               'instead of just being treated like {M0.he}{F0.she} is '
               'invisible, {M0.he}{F0.she} really is out of sight of the '
               'customers, focusing {M0.his}{F0.her} attention solely on hot '
               'grease and triple orders.sentient_sims_description{sim_name} '
               'works part-time at a fast food chain as a fry cook.Food '
               'Service CashierSweet, sweet Simoleons! '
               '\\u00c2\\u00a7\\u00c2\\u00a7\\u00c2\\u00a7! {0.SimFirstName} '
               'has earned enough trust to handle the Simoleons and the people '
               'who spend them. \\"Service with a smile,\\" {M0.his}{F0.her} '
               'manager always says, so {0.SimFirstName} takes orders, presses '
               'buttons, and grins until {M0.his}{F0.her} cheeks '
               'hurt.sentient_sims_description{sim_name} works part-time at a '
               'fast food chain as a cashier.career_Adult_NPC_Firefighter'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=145,
          lineno=1178,
          tokens=266,
          depth=7,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='careerTrack_NPC_Firefightersentient_sims_description{sim_name} '
               'works as a '
               'firefighter.career_Adult_NPC_GardenercareerTrack_NPC_Gardenersentient_sims_description{sim_name} '
               'works as a community '
               'gardener.career_Adult_NPC_MailmancareerTrack_NPC_Mailmansentient_sims_description{sim_name} '
               'works as a mail '
               'person.career_Adult_NPC_MaidcareerTrack_NPC_Maidsentient_sims_description{sim_name} '
               'works as a '
               'maid.career_Adult_NPC_FishermancareerTrack_NPC_Fishermansentient_sims_description{sim_name} '
               'works as a '
               'fisherman.career_Adult_NPC_BartendercareerTrack_NPC_Bartendersentient_sims_description{sim_name} '
               'works as a mixologist and '
               'bartender.career_Adult_NPC_Gym_TrainercareerTrack_NPC_GymTrainersentient_sims_description{sim_name} '
               'works as a trainer at the '
               'gym.career_Adult_NPC_TragicClowncareerTrack_NPC_TragicClownsentient_sims_description{sim_name} '
               'works as a tragic '
               'clown.career_Adult_NPC_NannycareerTrack_NPC_Nannysentient_sims_description{sim_name} '
               'works as a nanny.'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=146,
          lineno=1249,
          tokens=261,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='career_Adult_NPC_Gardener_ServicecareerTrack_NPC_Gardener_ServiceProfessional '
               'Gardenersentient_sims_description{sim_name} works as a '
               'professional landscaper and '
               'gardener.career_Adult_NPC_PizzaDeliverycareerTrack_NPC_PizzaDeliveryPizza '
               'Delivery {M0.Guy}{F0.Girl}sentient_sims_description{sim_name} '
               'works as a pizza delivery '
               'driver.career_Adult_NPC_RestaurantCriticcareerTrack_NPC_RestaurantCriticsentient_sims_description{sim_name} '
               'works as a professional restaurant '
               'critic.career_Adult_NPC_GrimReapercareerTrack_NPC_GrimReapersentient_sims_description{sim_name} '
               'works as the Grim Reaper and reaps '
               'Souls.career_Adult_NPC_RepaircareerTrack_NPC_Repairsentient_sims_description{sim_name} '
               'works as a repair technician for '
               'appliances.career_Adult_NPC_Bartender_companycareerTrack_NPC_Bartendersentient_sims_description{sim_name} '
               'works as a mixologist and '
               'bartender.career_Adult_NPC_LibrariancareerTrack_NPC_Librariansentient_sims_description{sim_name} '
               'works as a '
               'librarian.career_Adult_NPC_StallVendorcareerTrack_NPC_StallVendorsentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=147,
          lineno=1309,
          tokens=245,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as a stall vendor at the '
               'festival.career_Adult_NPC_HomeChefcareerTrack_NPC_Chefsentient_sims_description{sim_name} '
               'works as a home '
               'chef.career_Adult_NPC_OwnableRestaurant_HostcareerTrack_NPC_OwnableRestaurant_Hostsentient_sims_description{sim_name} '
               'just started working as a host at a '
               'restaurant.sentient_sims_description{sim_name} works as a host '
               'at a restaurant.sentient_sims_description{sim_name} works as a '
               'host at a restaurant.sentient_sims_description{sim_name} works '
               'as a host at a restaurant.Head Restaurant '
               'Hostsentient_sims_description{sim_name} works as the head host '
               'at a '
               'restaurant.career_Adult_NPC_OwnableRestaurant_WaitercareerTrack_NPC_OwnableRestaurant_Waitersentient_sims_description{sim_name} '
               'just started working as a waiter at a '
               'restaurant.sentient_sims_description{sim_name} works as a '
               'waiter at a restaurant.sentient_sims_description{sim_name} '
               'works as a waiter at a '
               'restaurant.sentient_sims_description{sim_name} works as a '
               'waiter at a restaurant.sentient_sims_description'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=148,
          lineno=1365,
          tokens=189,
          depth=11,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{sim_name} works as the head of waitstaff at a '
               'restaurant.career_Adult_NPC_OwnableRestaurant_ChefcareerTrack_NPC_OwnableRestaurant_Chefsentient_sims_description{sim_name} '
               'works as a line cook at a '
               'restaurant.sentient_sims_description{sim_name} works as a demi '
               'chef de partie at a '
               'restaurant.sentient_sims_description{sim_name} works as a chef '
               'de partie at a restaurant.sentient_sims_description{sim_name} '
               'works as a sous chef at a '
               'restaurant.sentient_sims_description{sim_name} works as an '
               'executive chef at a restaurant.# TODO: Not sure if this should '
               'be used# "career_Adult_NPC_Venue_BarRegular": {#     '
               '"careerTrack_NPC_Venue_BarRegular": {#             "name": '
               '"Bar Regular",#             "sentient_sims_description": '
               '"{sim_name} is a bar regular.",'),
 Fragment(document_cs='4848acc10d841dcae77649f1cbf170d72ca15a6139d9697d6b08dc19bf7d9876',
          id=149,
          lineno=1,
          tokens=10,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables and usages: career_descriptions\n'),
 Fragment(document_cs='58d8b1686b1cf10fd59997acf87226455463e06bf4d8b399415c3f57a8d03086',
          id=150,
          lineno=1,
          tokens=50,
          depth=1,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body='import fnmatchimport osimport py_compileimport stringfrom '
               'pathlib import Pathfrom pathlib import Pathfrom zipfile import '
               'PyZipFile, ZIP_STOREDfrom zipfile import PyZipFile, '
               'ZIP_STOREDfrom utils.utils import prepare_directoryfrom '
               'utils.utils import prepare_directory'),
 Fragment(document_cs='58d8b1686b1cf10fd59997acf87226455463e06bf4d8b399415c3f57a8d03086',
          id=151,
          lineno=11,
          tokens=132,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='compile_py',
          body='def compile_py(src: string, dest: string):\n'
               '    # Compile the mod\n'
               '    for root, dirs, files in os.walk(src):\n'
               "        for filename in fnmatch.filter(files, '*.py'):\n"
               "            src_py = root + '/' + filename\n"
               '            relative_path = str(Path(root).relative_to(src))\n'
               "            desc_path = dest + '/' + relative_path\n"
               "            compile_pyc = desc_path + '/' + "
               "filename.replace('.py', '.pyc')\n"
               '\n'
               '            print(f"Source: {src_py} compile: {desc_path + '
               '\'/\' + filename.replace(\'.py\', \'.pyc\')}")\n'
               '            py_compile.compile(src_py, compile_pyc)'),
 Fragment(document_cs='58d8b1686b1cf10fd59997acf87226455463e06bf4d8b399415c3f57a8d03086',
          id=152,
          lineno=23,
          tokens=32,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='start_compile',
          body='def start_compile():\n'
               "    prepare_directory('build/sentient_sims')\n"
               '\n'
               "    compile_py('sentient_sims', 'build/sentient_sims')"),
 Fragment(document_cs='58d8b1686b1cf10fd59997acf87226455463e06bf4d8b399415c3f57a8d03086',
          id=153,
          lineno=1,
          tokens=53,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: compile_py start_compile\n'
               '  Variables and usages: Path PyZipFile ZIP_STORED compile '
               'compile_pyc desc_path dest dirs filename files filter fnmatch '
               'pathlib prepare_directory print py_compile relative_path '
               'relative_to replace root src_py string utils walk zipfile\n'),
 Fragment(document_cs='63f087ca6e1dba69189d33087d572f1f44564a6bfe7c5afc8339ea6c39538b85',
          id=154,
          lineno=3,
          tokens=65,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# Likes and '
               'DislikesActivities_VideoGamingTrait_SimPreference_Dislikes_Music_JazzTrait_SimPreference_Dislikes_Music_TweenPopTrait_SimPreference_Dislikes_Music_WorldActivities_Gardening# '
               'Personality Traitshas commitment issuesis feeling energizedis '
               'feeling uncomfortableis feeling confidentis feeling '
               'embarrassed'),
 Fragment(document_cs='63f087ca6e1dba69189d33087d572f1f44564a6bfe7c5afc8339ea6c39538b85',
          id=155,
          lineno=1,
          tokens=10,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables and usages: trait_descriptions\n'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=156,
          lineno=1,
          tokens=241,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# display_action = True is default, use display_action = False '
               'to hide the prompt in the output# {initiator} and {target} '
               'will be replaced with the names of the sims in the '
               'interactionmixer_social_ComplainAboutBills_targeted_Friendly_alwaysOn_bills{initiator} '
               'starts a conversation with {target}."I don\\\'t know how '
               'I\\\'m going to pay for all of these bills," {initiator} '
               'said,"It seems like every time I turn around, there\\\'s '
               'another bill to pay," {initiator} grumbled,"I can\\\'t believe '
               'how much money I have to spend on bills every month," grumbled '
               '{initiator},"I can\\\'t believe how much money I have to spend '
               'on bills every month," grumbled {initiator},"I\\\'m so sick of '
               'living paycheck to paycheck just to keep up with these bills," '
               'complained '
               '{initiator},mixer_social_DiscussLatestGames_targeted_Friendly_alwaysOn_skills{initiator} '
               'starts a conversation with {target} about video games."Have '
               'you played that new video game?" {initator} '
               'asks.mixer_social_CheerfulIntroduction_greetings_skills'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=157,
          lineno=27,
          tokens=247,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{initiator} cheerfully introduces themselves to {target}."How '
               'are you?" {initiator} asks '
               '{target},mixer_social_FlirtyIntroduction_greetings_skills{initiator} '
               'introduces themselves to {target}.With a flirtatious smile, '
               '{initiator} strode over and extended their hand. "Hi there, '
               'I\\\'m {initiator}. What\\\'s your name?"{initiator} sauntered '
               'up with a charming grin. "Well hello there, I don\\\'t think '
               'we\\\'ve met yet. I\\\'m {initiator}."With a twinkle in their '
               'eye, {initiator} approached the other person and struck up a '
               'conversation. "Excuse me,With a playful wink, {initiator} '
               'sauntered up to the other person and introduced themselves. '
               '"Hi,mixer_social_ExpressFondness_targeted_Romance_alwaysOn{initiator} '
               'pauses before he expressing his fondness for '
               '{target}.mixer_social_ExpressAdmiration_targeted_Friendly_MiddleScore"I '
               'have to say, you never cease to amaze me," said '
               '{initiator}"I\\\'m constantly in awe of your resilience," said '
               '{initiator},'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=158,
          lineno=54,
          tokens=227,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"You have such an incredible way of seeing the world," said '
               '{initiator}, genuinely '
               'impressed.mixer_social_ComplainAboutProblems_targeted_friendly_emotionSpecific{initiator} '
               'sighed heavily, "My job sucks," they began,"I hate doing '
               "laundry. It\\'s such a chore, and I never seem to have enough "
               'time for it.", {initiator} began,"I\\\'ve been trying to eat '
               'healthier, but all the healthy food is so expensive.", '
               '{initiator} '
               'began,mixer_social_DiscussFavoriteArtist_targeted_Friendly_MiddleScore"Who '
               'is your favorite artist?" {initiator} '
               'asks.mixer_social_DiscussFavoriteAuthors_targeted_Friendly_alwaysOn"Who '
               'is your favorite author?" {initiator} '
               'asks.mixer_social_DiscussFavoriteBand_targeted_Friendly_alwaysOn{initiator} '
               'starts to talk about their favorite '
               'band,mixer_social_DiscussFavoriteRecipes_targeted_Friendly_MiddleScore"What '
               'kind of food do you like to cook?" {initiator} asks."I know '
               'you like to cook, what is your favorite recipe?" {initiator} '
               'asks.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=159,
          lineno=86,
          tokens=230,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_DiscussFineCuisine_targeted_Friendly_MiddleScore"I '
               'went to this fancy restaurant a couple weeks ago and let me '
               'tell you about the food,"There is this fancy restaurant in '
               'Vegas I love named '
               'mixer_social_RudeIntroduction_greetings{initiator} begins to '
               'rudely introduces themselves to '
               '{target}.mixer_social_Flirt_targeted_romance_alwaysOn{initiator} '
               'starts to flirt with '
               '{target}.mixer_social_FriendlyIntroduction_greetings{initiator} '
               'starts a conversation with {target} and introduces '
               'themselves."Hi there, I\\\'m {initiator}. What\\\'s your '
               'name?""Hey, I\\\'m {initiator}. Nice to meet you!""Hello, I '
               "don\\'t think we\\'ve met. I\\'m {initiator}. And you "
               'are?""Nice to see a new face! I\\\'m {initiator}. What\\\'s '
               'your name?""Hey, I\\\'m {initiator}. Mind if I join you?""Hi, '
               "I\\'m {initiator}. I\\'ve been meaning to introduce myself. "
               'What\\\'s your name?"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=160,
          lineno=115,
          tokens=225,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"Hey, how\\\'s it going? I\\\'m {initiator}. What\\\'s your '
               'name?""Hello, I\\\'m {initiator}. It\\\'s a pleasure to make '
               'your acquaintance!""Hi there, I\\\'m {initiator}. Just wanted '
               'to say hello!""Hey, I\\\'m {initiator}. Care to '
               'chat?"mixer_social_FunnyIntroduction_greetings\\"{target}, I '
               'heard you needed a daily dose of laughter. Well, here I am, '
               'your personal joke doctor!\\" {initiator} says with a wide '
               'grin.\\"Hey {target}, they say laughter is the best medicine, '
               'so I guess I\'m a licensed pharmacist!\\" {initiator} quips, '
               'as they introduce themself.\\"Knock, knock, {target}! Who\'s '
               'there? It\'s me, {initiator}, your new comedy companion!\\" '
               '{initiator} says, chuckling at their own joke.\\"{target}, I '
               'must warn you that being around me can cause extreme laughter '
               'and sore cheeks. Proceed at your own risk,\\" {initiator} says '
               'playfully.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=161,
          lineno=127,
          tokens=240,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hello {target}, I promise I\'m not a mime, but I\'ve been '
               'known to leave people speechless with laughter,\\" {initiator} '
               'says, making a mock serious face.\\"{initiator} at your '
               "service, {target}! I'm here to turn that frown upside down, "
               'one joke at a time,\\" {initiator} says, delivering a '
               'lighthearted salute.\\"Hey {target}, I\'m {initiator}, and if '
               'laughter were currency, I\'d be a billionaire!\\" {initiator} '
               'boasts with a cheeky grin.\\"Nice to meet you, {target}! I\'m '
               '{initiator}, and I have a PhD in giggles, chuckles, and '
               'guffaws,\\" {initiator} says, offering a comically exaggerated '
               'bow.\\"Hey there, {target}! I\'m {initiator}, and I\'m the '
               'person you call when you need a laugh and a half,\\" '
               '{initiator} says, winking playfully.\\"{target}, meet '
               "{initiator} - the human embodiment of laughter and joy. That's "
               'me, in case you were wondering,\\" {initiator} says, laughing '
               'at their own introduction.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=162,
          lineno=135,
          tokens=216,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_EnchantingIntroduction_greetings_skills"Greetings, '
               '{target}. I am {initiator}, the master of captivating tales '
               'and the weaver of dreams. It is an honor to make your '
               'acquaintance.""Ah, fair {target}, allow me to introduce '
               'myself. I am {initiator}, a soul enchanted by the mysteries of '
               'the world. May our encounter be as magical as the moonlit '
               'night.""In the realm of enchantment, where whispers become '
               'melodies and dreams come alive, I am known as {initiator}. And '
               'you, dear {target}, what name graces your existence?""Behold, '
               '{target}, for I am {initiator}, a conjurer of words and a '
               'guardian of imagination. Brace yourself, for the allure of my '
               'introduction shall transport you to realms yet '
               'unexplored.""With a touch of whimsy and a dash of intrigue, I '
               'present myself before you, {target}, as {initiator}, a '
               'wanderer of realms unseen and a collector of tales untold. How '
               'does your spirit respond to such enchantment?"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=163,
          lineno=142,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"In the realm of wonder, where reality intertwines with '
               'dreams, I am {initiator}, a custodian of curiosity and an '
               'emissary of imagination. And you, {target}, what treasures lie '
               'within your name?""Listen, {target}, as the wind carries my '
               'words to your ears. I am {initiator}, a weaver of stories and '
               'a guardian of secrets. Dare you venture into the depths of my '
               'enchanting introduction?""Ah, {target}, behold the enchantment '
               'that unfolds before you. I am {initiator}, a conjurer of '
               'wonder and a purveyor of dreams. Allow yourself to be swept '
               'away by the magic of our introduction.""Step closer, {target}, '
               'and let me grace your senses with an introduction like no '
               'other. I am {initiator}, a whisper in the night and a sparkle '
               'in the twilight, forever enchanted by the possibilities that '
               'lie within our encounter.""In a world where reality dances '
               'with fantasy, I emerge as {initiator}, a seeker of '
               'extraordinary tales and a harbinger of delight. And you, dear '
               '{target}, what wonders lie within your '
               'story?"mixer_social_AskAboutCareer_friendly_STC'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=164,
          lineno=151,
          tokens=228,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{initiator} starts a conversation with {target} and asks about '
               'their career."So what kind of work are you doing these days?" '
               '{initiator} asks."So, what line of work are you in?" '
               '{initiator} asks."What do you do for a living?" {initiator} '
               'asks.\\"{target}, I\'ve always been curious about what you do '
               'for a living. Would you mind sharing more about it?\\" '
               '{initiator} asks with genuine interest.\\"You know, {target}, '
               "we've never really talked about your career. What is it that "
               'you do, exactly?\\" {initiator} inquires, trying to learn more '
               'about {target}\'s life.\\"I\'ve always admired your dedication '
               'to your work, {target}. Can you tell me more about your career '
               'and what drives you?\\" {initiator} says, eager to understand '
               '{target}\'s passion.\\"Hey, {target}, we\'ve been friends for '
               "a while now but I realized I don't know much about your line "
               'of work. Could you tell me about it?\\" {initiator} asks with '
               'a friendly smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=165,
          lineno=161,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve noticed you\'re really passionate about '
               'your job. What do you do, and what makes you love it so '
               'much?\\" {initiator} inquires, wanting to know more about '
               '{target}\'s career.\\"Your job seems intriguing, {target}. '
               'Would you mind sharing more about what you do and how you got '
               'into that line of work?\\" {initiator} asks, hoping to gain '
               'some insight into {target}\'s life.\\"I\'ve been meaning to '
               'ask you, {target}, what exactly is it that you do for a '
               'living? It seems like your work is really important to you,\\" '
               "{initiator} says, trying to understand {target}'s "
               'world.\\"So, {target}, I\'ve never gotten a clear answer from '
               'you about your career. What do you do, and how did you end up '
               'in that field?\\" {initiator} asks, hoping to learn more about '
               '{target}\'s professional life.\\"{target}, I\'ve always wanted '
               'to know more about your line of work. What is it that you do, '
               'and what made you choose that career path?\\" {initiator} '
               'inquires, looking for a deeper connection with {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=166,
          lineno=166,
          tokens=246,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I was just thinking, {target}, we\'ve never really '
               'discussed your profession. What do you do, and how did you '
               'find yourself in that career?\\" {initiator} asks, seeking to '
               "gain a better understanding of {target}'s "
               'life.mixer_social_AskAboutFavoriteAuthor_targeted_Friendly_alwaysOn_skills"Who '
               'is your favorite author, {target}?" {initiator} asks."I\\\'m '
               'curious, {target}, who is your favorite author?" {initiator} '
               'asks."If you had to pick one, who would you say is your '
               'favorite author?" {initiator} asks {target}."Have you read any '
               'books by your favorite author lately, {target}?" {initiator} '
               'asks."I\\\'ve been meaning to ask, {target}, who is your go-to '
               'author?" {initiator} asks."Do you have a favorite author, '
               '{target}?" {initiator} asks with a smile."What book made you '
               'fall in love with your favorite author, {target}?" {initiator} '
               'asks curiously."I\\\'m in the mood for a good read. Any '
               'recommendations from your favorite author, {target}?" '
               '{initiator} asks enthusiastically.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=167,
          lineno=179,
          tokens=242,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"Tell me about the first time you discovered your favorite '
               'author, {target}." {initiator} leans in, interested."If you '
               'could meet your favorite author, {target}, what would you ask '
               'them?" {initiator} ponders '
               'aloud.mixer_social_AskAboutDay_targeted_Friendly_alwaysOn{initiator} '
               'starts a conversation with {target} and asks about their '
               'day."Hey {target}, how has your day been?""Did you have a good '
               'day {target}?""What did you do today?" {initiator} '
               'asks."Anything interesting happen today?" {initiator} '
               'asks."How\\\'s your day been so far?" {initiator} asks."How '
               'did your day go?" {initiator} asks."What\\\'s been going on '
               'with you today?" {initiator} asks."Tell me about your day!" '
               '{initiator} exclaims."Have you had a productive day?" '
               '{initiator} '
               'asks.mixer_social_HeartfeltCompliment_targeted_friendly_emotionSpecific"You '
               'look absolutely stunning today," {initiator} compliments '
               '{target}."I just wanted to say, you\\\'re incredibly '
               'talented," {initiator} praises {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=168,
          lineno=203,
          tokens=238,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I can\\\'t help but admire your determination and hard work," '
               '{initiator} tells {target}."You have such a kind and caring '
               'heart," {initiator} compliments {target}."Your creativity '
               'never ceases to amaze me," {initiator} tells {target} with '
               'admiration."I wanted to let you know that you inspire me," '
               '{initiator} expresses to {target}."You have a way with words '
               'that captivates everyone around you," {initiator} praises '
               '{target}."Your generosity and selflessness are truly '
               'remarkable," {initiator} acknowledges {target}."I wanted to '
               'say that you\\\'re an extraordinary person," {initiator} tells '
               '{target} sincerely."You have a beautiful soul," {initiator} '
               'compliments {target} '
               'genuinely.mixer_social_Hug_Friendly_Middlescore_NoMoodTest{initiator} '
               'gives {target} a hug.{initiator} gives {target} a friendly '
               'hug.{initiator} gives {target} a big '
               'hug.mixer_social_Hug_targeted_Friendly_MiddleScore{initiator} '
               'gives {target} a hug.{initiator} gives {target} a friendly '
               'hug.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=169,
          lineno=224,
          tokens=229,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{initiator} gives {target} a big '
               'hug.mixer_social_SayGoodbye_targeted_Friendly_alwaysOn"Goodbye, '
               '{target}! Take care!" {initiator} waves."It was great seeing '
               'you, {target}. Goodbye!" {initiator} smiles."Until next time, '
               '{target}. Goodbye!" {initiator} says with a nod."Farewell, '
               '{target}. Have a wonderful day!" {initiator} bids '
               'farewell."Goodbye, {target}! See you soon!" {initiator} waves '
               'goodbye."Take care, {target}. Goodbye!" {initiator} says '
               'warmly."Until we meet again, {target}. Goodbye!" {initiator} '
               'gives a friendly wave."Have a safe journey, {target}. '
               'Goodbye!" {initiator} offers their well wishes."Goodbye, '
               '{target}. It was nice spending time with you!" {initiator} '
               'smiles warmly."Wishing you the best, {target}. Goodbye!" '
               '{initiator} says with a hint of '
               'nostalgia.mixer_social_ShareFishingTips_targeted_Friendly_alwaysOn_skills'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=170,
          lineno=243,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"Hey {target}, I have some fishing tips for you," {initiator} '
               'says."I\\\'ve been fishing for years, {target}, let me share '
               'some tips with you," {initiator} offers."Are you interested in '
               'fishing, {target}? I can give you some valuable tips," '
               '{initiator} suggests."I heard you want to go fishing, '
               '{target}. Let me give you some advice," {initiator} offers '
               'kindly."\\\'ve discovered some great fishing techniques, '
               '{target}. Would you like me to share them with you?" '
               '{initiator} asks with a smile."If you\\\'re planning to go '
               'fishing, {target}, I have some tips that might help you catch '
               'more fish," {initiator} offers eagerly."Fishing can be tricky, '
               '{target}, but I can give you some tips to make it easier," '
               '{initiator} says confidently."I\\\'ve learned a few tricks '
               'that might improve your fishing experience, {target}. Would '
               'you like to hear them?" {initiator} asks curiously."I noticed '
               "you\\'re interested in fishing, {target}. How about I give you "
               'some pointers to get started?" {initiator} suggests warmly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=171,
          lineno=252,
          tokens=221,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I\\\'ve been studying different fishing techniques, {target}, '
               'and I think I have some valuable tips to share with you," '
               '{initiator} says '
               'excitedly.mixer_social_GiveCookingTips_targeted_Friendly_alwaysOn_skills"Hey '
               '{target}, I\\\'ve got some cooking tips for you!" {initiator} '
               'says excitedly."I\\\'ve learned a few tricks in the kitchen. '
               'Mind if I share some cooking tips with you?" {initiator} asks '
               '{target}."I\\\'ve been experimenting with some new recipes. '
               'Would you like me to give you a few cooking tips?" {initiator} '
               'offers {target}."You know, {target}, I\\\'ve discovered some '
               'amazing cooking techniques. Can I give you a few tips?" '
               '{initiator} suggests."I\\\'ve been honing my culinary skills '
               'lately. Would you be interested in hearing some cooking tips '
               'from me?" {initiator} asks {target}."I\\\'ve come across some '
               'fantastic cooking hacks. How about I share a few tips with '
               'you?" {initiator} proposes to {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=172,
          lineno=263,
          tokens=219,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I\\\'ve been exploring the world of cooking lately and picked '
               'up some valuable tips. Would you like to hear them?" '
               '{initiator} asks {target}."You\\\'re in luck, {target}. '
               "I\\'ve got some secret cooking tips that I\\'m willing to "
               'share with you!" {initiator} teases playfully."I\\\'ve been '
               'experimenting in the kitchen and stumbled upon some genius '
               'cooking tips. Want to hear them?" {initiator} asks {target} '
               'with a smile."Cooking can be a lot of fun if you know some '
               'tricks. Mind if I pass on a few cooking tips to you, '
               '{target}?" {initiator} offers '
               'generously.mixer_social_ShareCookingSecrets_targeted_Friendly_alwaysOn_skills"You '
               'know, {target}, I have this amazing recipe I want to share '
               'with you," {initiator} says enthusiastically."I\\\'ve been '
               "experimenting in the kitchen lately, and I\\'ve discovered "
               'some fantastic cooking secrets. Would you like me to share '
               'them with you, {target}?" {initiator} suggests.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=173,
          lineno=273,
          tokens=226,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I\\\'ve learned a few cooking tricks that have made a world '
               'of difference in my meals. Mind if I pass them on to you, '
               '{target}?" {initiator} offers."{target}, I\\\'ve been '
               "perfecting my cooking skills, and I think I\\'ve unlocked some "
               'secrets that could elevate your dishes. Can I enlighten you?" '
               '{initiator} proposes."Cooking is my passion, {target}, and '
               "I\\'d love to share some of my secrets with you. Are you "
               'interested?" {initiator} asks with a smile."You won\\\'t '
               "believe the cooking hacks I\\'ve discovered, {target}. Would "
               'you like me to reveal them to you?" {initiator} asks, unable '
               'to contain their excitement."I\\\'ve stumbled upon some '
               'culinary secrets that can turn an ordinary meal into a '
               'masterpiece. Want me to spill the beans, {target}?" '
               '{initiator} teases."{target}, I\\\'ve been honing my cooking '
               'skills, and I have a few secrets up my sleeve. Care to hear '
               'them?" {initiator} suggests with a mysterious grin."'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=174,
          lineno=279,
          tokens=221,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I\\\'ve been reading up on cooking techniques, and I think '
               "you\\'d find some of them helpful, {target}. Mind if I share "
               'them with you?" {initiator} offers politely."I\\\'ve been '
               'experimenting with flavors and techniques in the kitchen '
               "lately, {target}, and I\\'d love to share what I\\'ve learned. "
               'Interested?" {initiator} proposes with '
               'anticipation.mixer_social_EvangelizeGrilledCheese_Friendly_alwaysOn_Trait"You '
               'won\\\'t believe the amazingness of grilled cheese, {target}!" '
               '{initiator} exclaims."Have you ever experienced the pure '
               'delight of a perfectly grilled cheese sandwich?" {initiator} '
               'asks {target}."Let me tell you about the magic of grilled '
               'cheese, {target}!" {initiator} enthuses."Have you tried the '
               'heavenly combination of melty cheese and crispy bread in a '
               'grilled cheese sandwich?" {initiator} asks {target}."Prepare '
               'to have your taste buds revolutionized, {target}! Grilled '
               'cheese is the answer to all cravings," {initiator} declares.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=175,
          lineno=290,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I can\\\'t contain my excitement about grilled cheese! You '
               'must try it, {target}!" {initiator} insists."Grilled cheese is '
               "more than just a sandwich, it\\'s a culinary experience. Trust "
               'me, {target}," {initiator} says persuasively."Let me share my '
               "love for grilled cheese with you, {target}. It\\'s the "
               'ultimate comfort food," {initiator} suggests with a '
               'smile."Grilled cheese is a masterpiece of simplicity. Don\\\'t '
               'you agree, {target}?" {initiator} inquires eagerly."I\\\'ve '
               'discovered the secret to the most delicious grilled cheese. '
               'Would you like to know, {target}?" {initiator} '
               'teases.mixer_social_Flatter_targeted_Friendly_alwaysOn"You '
               'look absolutely stunning today, {target}," {initiator} '
               'compliments."I must say, {target}, your talent never ceases to '
               'amaze me," {initiator} says with admiration."I couldn\\\'t '
               'help but notice how incredibly intelligent you are, {target}," '
               '{initiator} compliments."You have such a captivating smile, '
               '{target}," {initiator} remarks fondly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=176,
          lineno=303,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I wanted to let you know that you\\\'re an incredibly '
               'kind-hearted person, {target}," {initiator} compliments '
               'sincerely."You have an amazing sense of style, {target}," '
               '{initiator} comments with appreciation."I\\\'m in awe of your '
               'creativity, {target}," {initiator} admires."You always manage '
               'to bring positivity to any situation, {target}," {initiator} '
               'praises warmly."Your dedication and hard work are truly '
               'inspiring, {target}," {initiator} expresses with admiration."I '
               "just wanted to say that you\\'re a remarkable individual, "
               '{target}," {initiator} compliments '
               'sincerely.mixer_social_GiveRelationshipAdvice_targeted_friendly_emotionSpecific"You '
               "know, {target}, I\\'ve been thinking about your "
               'relationship...""I have some relationship advice for you, '
               '{target}.""I\\\'ve been reading this book about relationships, '
               'and I think it could help you, {target}.""I\\\'ve noticed a '
               'few things about your relationship, {target}, and I wanted to '
               'share my thoughts.""I\\\'ve been through similar situations in '
               'my own relationships, {target}, and I think I can offer you '
               'some advice."'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=177,
          lineno=318,
          tokens=205,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I think you should consider a different approach in your '
               'relationship, {target}.""Do you mind if I give you some '
               'relationship advice, {target}?""I\\\'ve been observing your '
               'relationship, {target}, and I believe I have some insights to '
               'share.""Have you thought about trying this new technique in '
               'your relationship, '
               '{target}?"mixer_social_NoxiousCloud_targeted_mischief_skills{initiator} '
               'rips a big nasty '
               'fart.mixer_social_RevealDeepSecret_targeted_Friendly_HighScore"{target}, '
               'I need to tell you something. Promise me you won\\\'t judge," '
               '{initiator} says nervously."I have been keeping a secret for '
               'so long, but I trust you enough to share it with you," '
               '{initiator} says, looking into {target}\\\'s eyes."You know, '
               "{target}, there\\'s something I\\'ve never told anyone before, "
               'but I feel like I can confide in you," {initiator} says, '
               'hesitatingly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=178,
          lineno=334,
          tokens=242,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I\\\'ve been carrying this secret for far too long, and '
               "it\\'s eating me up inside. {target}, I think it\\'s time I "
               'share it with you," {initiator} confesses, their voice '
               'trembling."I never thought I would reveal this, but you mean a '
               'lot to me, {target}. I need you to know the truth," '
               '{initiator} says, taking a deep breath."There\\\'s something '
               "I\\'ve been hiding, {target}, and it\\'s time I let it out. I "
               'hope you can handle it," {initiator} says, looking '
               'anxious."I\\\'ve kept this hidden for years, {target}, but I '
               'can\\\'t bear the weight anymore. I have to tell you," '
               '{initiator} admits, looking vulnerable."This secret has '
               'haunted me for so long, {target}, but I feel a connection with '
               'you that makes me want to share it. Can I trust you?" '
               '{initiator} asks cautiously."I\\\'ve always admired your '
               "ability to keep secrets, {target}, but there\\'s one I can no "
               'longer keep to myself. Brace yourself," {initiator} says, '
               'preparing to share something profound.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=179,
          lineno=340,
          tokens=201,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I\\\'ve been meaning to tell you this, {target}, but I\\\'ve '
               "never found the right time. Now, in this moment, I feel it\\'s "
               'the right moment to reveal my deepest secret," {initiator} '
               'says with a mixture of relief and '
               'apprehension.mixer_social_RevealEvilPlans_targeted_mischief_traits"{target}, '
               "I have a confession to make. Brace yourself, for what I\\'m "
               'about to reveal is truly sinister," {initiator} says with a '
               'wicked grin."I\\\'ve been living a double life, {target}, and '
               "i\\'s time you know the truth. Prepare yourself for the "
               'darkness that lies within me," {initiator} says, their voice '
               'dripping with malevolence."You thought you knew me, {target}, '
               "but you were wrong. The truth is, I\\'ve been plotting "
               "something truly diabolical, and now it\\'s time to involve "
               'you," {initiator} says, eyes gleaming with mischief.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=180,
          lineno=348,
          tokens=198,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"Listen carefully, {target}, for the secrets I\\\'m about to '
               "share will change everything. I\\'ve been working on a plan, a "
               'plan so evil that it will shake the very foundations of this '
               'world," {initiator} whispers ominously."I\\\'ve always been '
               'envious of your innocence, {target}, but no more. Today, I '
               "reveal my true nature, and you\\'ll witness the depths of my "
               'malevolence firsthand," {initiator} declares, a twisted smile '
               'forming on their lips."Prepare to be shocked, {target}, for '
               'the darkness that resides within me is about to be unleashed. '
               'My evil plans will leave a trail of chaos and destruction," '
               '{initiator} says, their voice laced with anticipation."You '
               "see, {target}, I\\'ve been biding my time, waiting for the "
               'perfect moment to reveal my evil plans. And that moment is '
               'now," {initiator} says, a wicked glint in their eyes.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=181,
          lineno=352,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"I hope you\\\'re ready for this, {target}, because what '
               "I\\'m about to disclose will shatter your perception of me. My "
               'evil schemes are far more intricate than you could have ever '
               'imagined," {initiator} says, relishing the impending '
               'revelation.""There\\\'s a darkness inside me, {target}, and '
               "it\\'s time you witness it. My evil plans are nearing "
               "fruition, and you\\'re about to become an integral part of "
               'them," {initiator} says, a sinister chuckle escaping their '
               'lips."I\\\'ve kept my true intentions hidden for far too long, '
               '{target}. Today, I lay bare my evil plans before you, and '
               'together, we shall conquer this world," {initiator} proclaims, '
               'their voice filled with twisted '
               'ambition.mixer_social_RevealBrilliantInvention_targeted_Friendly_alwaysOn\\"{target}, '
               "I've been working on something incredible, and I can't wait to "
               'show you,\\" {initiator} says, barely containing their '
               'excitement.\\"I\'ve finally completed my latest invention, '
               '{target}. I believe it will change everything,\\" {initiator} '
               'says with pride, eager to share their creation.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=182,
          lineno=361,
          tokens=234,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, you won\'t believe what I\'ve invented. I need to '
               'show you right away,\\" {initiator} says, grinning from ear to '
               'ear.\\"I\'ve been keeping this a secret for a while, {target}, '
               'but I finally perfected my invention. Are you ready to see '
               'it?\\" {initiator} asks, anticipation filling their eyes.\\"I '
               "couldn't sleep last night, {target}, because I was working on "
               'something that I think will blow your mind. Feast your eyes on '
               'this!\\" {initiator} exclaims, revealing their '
               'invention.\\"I\'ve been tinkering in the workshop for weeks, '
               "{target}, and I think you're going to be amazed by what I've "
               'come up with,\\" {initiator} says, filled with pride.\\"I\'ve '
               'spent countless hours perfecting this invention, {target}. I '
               'think it\'s time for you to see the results,\\" {initiator} '
               'says, preparing to unveil their creation.\\"{target}, I\'m so '
               "excited to finally show you what I've been working on. I think "
               'it\'s going to change our lives,\\" {initiator} says, their '
               'eyes sparkling with enthusiasm.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=183,
          lineno=367,
          tokens=226,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"You know I\'ve been keeping a secret project, {target}, and '
               "now it's finally ready. I can't wait to see your "
               'reaction,\\" {initiator} says, a smile spreading across their '
               'face.\\"I\'ve poured my heart and soul into this invention, '
               '{target}. I hope you\'re as excited about it as I am,\\" '
               '{initiator} says, eager to share their '
               'accomplishment.mixer_social_AttemptToScare_targeted_mischief_skills\\"{initiator} '
               'sneaks up behind {target} and whispers, \\"Boo!\\" before '
               'bursting into laughter.\\"{target}, did you know there\'s a '
               'legend about a ghost around here?\\" {initiator} says, trying '
               'to spook {target}.\\"Watch out, {target}! Something\'s right '
               'behind you!\\" {initiator} exclaims, trying to startle '
               '{target}.\\"{initiator} pretends to see something terrifying '
               'in the distance and shouts, \\"{target}, look '
               'out!\\"\\"{initiator} decides to hide and jump out at {target} '
               'as they walk by, hoping to scare them.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=184,
          lineno=378,
          tokens=229,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Be careful, {target}. I\'ve heard strange noises around '
               'here lately. It sends shivers down my spine,\\" {initiator} '
               'says, attempting to unnerve '
               '{target}.mixer_social_AskWhatHappened_targeted_Friendly_alwaysOn\\"{target}, '
               'I noticed something seemed off earlier. Can you tell me what '
               'happened?\\" {initiator} asks with concern.\\"Hey {target}, '
               'you don\'t look too good. What happened to you?\\" {initiator} '
               'inquires, offering a sympathetic smile.\\"{target}, I can tell '
               "something's bothering you. Do you want to talk about what "
               'happened?\\" {initiator} asks gently.\\"Is everything alright, '
               '{target}? You seem a bit down. Mind sharing what happened?\\" '
               '{initiator} questions, trying to provide support.\\"Something '
               'seems to have upset you, {target}. Can I help in any way? What '
               'happened?\\" {initiator} asks, offering a comforting '
               'presence.\\"{target}, you\'ve been quiet all day. What '
               'happened that\'s got you so troubled?\\" {initiator} asks, '
               'genuinely concerned.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=185,
          lineno=389,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I\'m here for you if you want to talk. What '
               'happened that\'s got you so upset?\\" {initiator} asks, '
               'placing a hand on {target}\'s shoulder.\\"{target}, I\'ve '
               'known you for a long time, and I can tell when something is '
               'wrong. What happened?\\" {initiator} asks with a furrowed '
               'brow.\\"Is there something you want to talk about, {target}? '
               'I\'m here to listen. What happened?\\" {initiator} asks, '
               'sitting down next to {target}.\\"You seem really down, '
               "{target}. I'm worried about you. Can you tell me what "
               'happened?\\" {initiator} asks, hoping to offer some comfort.# '
               'TODO: Add special code for interactions like '
               'thismixer_social_AskIfSingle_targeted_romance_alwaysOn\\"{target}, '
               "I hope this isn't too forward, but are you seeing anyone right "
               'now?\\" {initiator} asks, trying to sound casual.\\"I was just '
               'wondering, {target}, do you happen to be single?\\" '
               '{initiator} inquires, a hint of curiosity in their voice.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=186,
          lineno=400,
          tokens=208,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I\'ve been meaning to ask you, are you '
               'currently in a relationship?\\" {initiator} questions, with a '
               'touch of nervousness.\\"Forgive me if I\'m being intrusive, '
               "{target}, but I couldn't help but wonder if you're "
               'single?\\" {initiator} asks cautiously.\\"{target}, I don\'t '
               'want to be presumptuous, but is there someone special in your '
               'life right now?\\" {initiator} questions, genuinely '
               'curious.\\"So, {target}, this might be a bit personal, but are '
               'you dating anyone at the moment?\\" {initiator} inquires, '
               'trying to gauge their reaction.\\"{target}, I hope you don\'t '
               'mind me asking, but are you currently involved with '
               'someone?\\" {initiator} asks, attempting to hide their '
               'interest.\\"I know this might be a bit out of the blue, '
               '{target}, but are you single or in a relationship?\\" '
               '{initiator} questions, unsure of how {target} will react.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=187,
          lineno=406,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Sorry if this is a bit nosy, {target}, but I\'ve been '
               'curious for a while now: are you seeing anyone?\\" {initiator} '
               'asks, hoping for an honest answer.\\"Hey {target}, this might '
               "come across as a bit sudden, but I wanted to know if you're "
               'single or taken?\\" {initiator} inquires, looking slightly '
               'embarrassed.mixer_social_ComplainAboutFoodPoisoning_Targeted_Friendly_AlwaysOn\\"{target}, '
               'I can\'t believe this! I got food poisoning!\\" {initiator} '
               'says, visibly upset.\\"I never thought I\'d get food '
               "poisoning, but I guess it's my unlucky day. I feel terrible, "
               '{target},\\" {initiator} groans.\\"Ugh, {target}, I think I '
               'got food poisoning. My stomach is killing me,\\" {initiator} '
               'complains, clutching their stomach.\\"{target}, remember that '
               "food we had? I think it gave me food poisoning. I've been "
               'feeling awful all day,\\" {initiator} says with a '
               'grimace.\\"You won\'t believe this, {target}, but I got food '
               'poisoning from our food.\\" {initiator} shares, looking '
               'frustrated.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=188,
          lineno=417,
          tokens=244,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I can\'t believe I got food poisoning, {target}.\\" '
               '{initiator} says, holding their stomach in pain.\\"{target}, '
               "this is the worst day ever. I'm pretty sure I got food "
               'poisoning from the food I just ate,\\" {initiator} laments, '
               'looking miserable.\\"I should\'ve known better, {target}. That '
               "food I ate yesterday isn't sitting right with me, and now I'm "
               'paying the price,\\" {initiator} says, regretting their '
               'choice.\\"Ugh, {target}, I think I have food poisoning,\\" '
               '{initiator} says, feeling betrayed and '
               'unwell.mixer_social_DeepConversation_targeted_Friendly_MiddleScore\\"{target}, '
               "I've been thinking a lot lately, and I realized there's "
               'something I need to talk to you about,\\" {initiator} says, '
               'taking a seat beside {target}.\\"{target}, can we talk? '
               "There's something on my mind that I think only you would "
               'understand,\\" {initiator} says, searching for the right '
               'words.\\"Hey {target}, do you have a moment? I feel like we '
               'need to have a heart-to-heart,\\" {initiator} suggests, hoping '
               'for a meaningful conversation.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=189,
          lineno=428,
          tokens=233,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I don\'t know why, but I feel like I can really open up to '
               'you, {target}. Can we talk about something important?\\" '
               '{initiator} asks, looking for support.\\"Something has been '
               "bothering me, {target}, and I can't shake it off. I need to "
               'share it with you. Can we talk?\\" {initiator} says, seeking '
               'comfort.\\"{target}, you\'ve always been a great listener, and '
               'I need someone to talk to right now. Will you lend me your '
               'ear?\\" {initiator} asks sincerely.\\"I\'ve been struggling '
               'with something, {target}, and I think you might be able to '
               'help me. Can we sit down and talk?\\" {initiator} asks, '
               'looking for guidance.\\"{target}, I need your advice on '
               "something that's been weighing heavily on my mind. Can we have "
               'a deep conversation?\\" {initiator} asks, trusting {target}\'s '
               'wisdom.\\"There\'s something I\'ve been wanting to discuss '
               "with you, {target}. I feel like you'll be able to understand "
               'and help me navigate through it,\\" {initiator} says, reaching '
               'out.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=190,
          lineno=434,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been going through a tough time, {target}, and I '
               "think you're the only one who can help me make sense of it. "
               'Can we talk?\\" {initiator} pleads, needing a '
               'friend.mixer_social_BanterWithOldFriend_targeted_Friendly_alwaysOn\\"{target}, '
               "do you remember the time we first met? I can't believe it's "
               'been so long!\\" {initiator} says, laughing and reminiscing '
               'about the past.\\"Hey {target}, I bet you still can\'t make a '
               'decent cup of coffee after all these years!\\" {initiator} '
               'teases, smirking playfully.\\"{initiator} grins at {target} '
               'and says, \\"Remember when we used to argue about who was the '
               'better singer? I still think you owe me a rematch!\\"\\"After '
               "all this time, {target}, I still can't believe you're such a "
               'terrible dancer!\\" {initiator} chuckles, poking fun at their '
               'friend.\\"{initiator} playfully nudges {target} and says, '
               '\\"So, have you finally learned how to cook something other '
               'than instant noodles?\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=191,
          lineno=444,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Remember that time you got us lost on our way to the '
               "concert, {target}? I'm amazed we're still friends after that "
               'fiasco!\\" {initiator} says, laughing heartily.\\"I still '
               "can't believe you used to wear those ridiculous outfits, "
               '{target}. How did we ever let you leave the house like '
               'that?\\" {initiator} teases, chuckling.\\"{initiator} grins at '
               '{target} and says, \\"You know, I still owe you for that prank '
               'you pulled on me years ago. Watch your back, my '
               'friend!\\"\\"Hey {target}, do you still have that hideous '
               "painting you insisted on hanging in your living room? I can't "
               'believe you ever thought it was a good idea!\\" {initiator} '
               'laughs, reminiscing about old times.\\"It\'s hard to believe '
               "we've come so far, {target}. Remember when we used to dream "
               "about where we'd be now? I think we've done pretty well for "
               'ourselves!\\" {initiator} says, smiling fondly at their '
               'friend.mixer_social_BrightenDay_targeted_friendly_emotionSpecific'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=192,
          lineno=453,
          tokens=242,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey, {target}, I know things have been tough lately. How '
               'about we go do something fun together?\\" {initiator} suggests '
               'with a smile.\\"Feeling blue, {target}? Let me tell you a joke '
               'to lighten the mood,\\" {initiator} says, ready to share a '
               'funny story.\\"Hey {target}, I know you\'re going through a '
               "lot right now, but remember that I'm always here for you. "
               'Let\'s talk about it,\\" {initiator} suggests '
               'kindly.\\"Sometimes, all it takes is a hug to make things '
               'better. Come here, {target},\\" {initiator} says, opening '
               'their arms for a warm embrace.\\"Let\'s get out of this rut, '
               '{target}. What can we do today to turn things around and make '
               'you feel better?\\" {initiator} asks, ready to help in any way '
               'possible.mixer_social_ComplainAboutLackofLoveLife_Targeted_Friendly_AlwaysOn_Jealous_Trait\\"{target}, '
               "I can't help but feel a little envious of everyone around me. "
               "It seems like they all have someone to love, while I'm still "
               'alone,\\" {initiator} says with a sigh.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=193,
          lineno=463,
          tokens=222,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Sometimes, I wonder if I\'ll ever find someone who truly '
               'understands me,\\" {initiator} admits to {target}, looking '
               'downcast.\\"You know, {target}, I\'ve been feeling really '
               "lonely lately. It's like everyone has someone except for "
               'me,\\" {initiator} confesses, seeking comfort.\\"I don\'t know '
               "what I'm doing wrong, {target}. Why can't I find someone who "
               'genuinely cares for me?\\" {initiator} asks, frustration '
               'evident in their voice.\\"{target}, do you ever feel like '
               "you're destined to be alone? I can't seem to find my other "
               'half, no matter how hard I try,\\" {initiator} says, a note of '
               'sadness in their voice.\\"It\'s so disheartening, {target}. I '
               "see couples everywhere, and it just reminds me of what I'm "
               'missing,\\" {initiator} shares, their eyes filled with '
               'longing.\\"I\'ve been on so many dates, {target}, but nothing '
               'ever seems to work out. What am I doing wrong?\\" {initiator} '
               'questions, hoping for some insight.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=194,
          lineno=469,
          tokens=215,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Sometimes, I feel like giving up on love altogether, '
               "{target}. It's just so exhausting trying to find someone who "
               'actually cares,\\" {initiator} admits, looking '
               'defeated.\\"Everyone says there\'s someone out there for '
               "everyone, {target}, but I'm starting to doubt it. Will I ever "
               'find my person?\\" {initiator} asks, desperation creeping into '
               'their voice.\\"I can\'t help but feel like I\'m missing out on '
               'something amazing, {target}. Everyone talks about how great '
               'love is, but all I\'ve ever known is loneliness,\\" '
               '{initiator} laments, a tear in their '
               'eye.mixer_social_BoastAboutBiggestCatch_targeted_Friendly_alwaysOn_skills\\"{target}, '
               "you won't believe it, I caught the biggest fish you've ever "
               'seen!\\" {initiator} exclaims with excitement.\\"Hey, '
               "{target}, I don't want to brag, but I caught a huge fish the "
               'other day. I\'ve never seen one like it before,\\" {initiator} '
               'says, trying to contain their pride.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=195,
          lineno=478,
          tokens=242,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Guess what, {target}? I went fishing yesterday and caught '
               'an absolute monster of a fish! You should\'ve seen it,\\" '
               '{initiator} says, grinning from ear to ear.\\"I know you\'re '
               'into fishing, {target}, but let me tell you about the giant '
               'fish I caught this weekend. It was amazing!\\" {initiator} '
               'says, eager to share their story.\\"I can\'t help but brag a '
               'little, {target}. I caught this enormous fish that was bigger '
               'than anything I\'ve ever seen!\\" {initiator} says, eyes '
               'sparkling with excitement.\\"You\'re not going to believe '
               'this, {target}, but I managed to catch a fish that was bigger '
               'than both my arms outstretched!\\" {initiator} says, their '
               'voice filled with triumph.\\"Hey, {target}, have you ever '
               'caught a fish so big that it barely fit in your net? Because I '
               'just did!\\" {initiator} says, beaming with pride.\\"I\'ve got '
               "to tell someone, {target}, and you're the lucky one. I caught "
               'a fish so big, it made all the other fishermen jealous!\\" '
               '{initiator} says, grinning proudly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=196,
          lineno=484,
          tokens=245,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Listen up, {target}, I\'ve got a fishing tale for you. I '
               'caught this massive fish that I could barely pull out of the '
               'water!\\" {initiator} says, excitement in their voice.\\"Just '
               'between us, {target}, I managed to catch the biggest fish of '
               'my life yesterday! It was incredible!\\" {initiator} says, '
               'unable to contain their '
               'enthusiasm.mixer_social_HorrifyingJoke_targeted_funny_alwaysOn\\"{target}, '
               'I heard this joke the other day, and I just have to share it '
               'with you. It\'s a bit twisted, though,\\" {initiator} says, '
               'grinning mischievously.\\"Hey {target}, I\'ve got a dark sense '
               'of humor, and I think this joke might be right up your alley. '
               'Can you handle it?\\" {initiator} asks, raising an '
               'eyebrow.\\"{initiator} leans in close to {target} and '
               'whispers, \\"I\'ve got a joke that might give you the creeps. '
               'Are you ready?\\"\\"Okay, {target}, brace yourself. I\'ve got '
               'a joke that\'s not for the faint of heart,\\" {initiator} '
               'says, a wicked smile on their face.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=197,
          lineno=494,
          tokens=239,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Be warned, {target}, this joke is not for everyone. But I '
               'think you\'ve got the stomach for it,\\" {initiator} says, '
               'their eyes gleaming with anticipation.\\"{target}, I\'ve got a '
               "horrifying joke that I think you'll appreciate. Get ready to "
               'laugh and cringe at the same time,\\" {initiator} says, '
               'rubbing their hands together in excitement.\\"Alright, '
               "{target}, I've got a joke that's twisted and hilarious, but "
               'it\'s not for everyone. Are you in?\\" {initiator} asks, a '
               'devilish grin on their face.\\"{initiator} chuckles darkly and '
               'says to {target}, \\"I\'ve got a joke that might make your '
               'skin crawl. Do you want to hear it?\\"\\"Hey {target}, I\'ve '
               "got a joke that's a little... morbid. But I think you'll like "
               'it,\\" {initiator} says, a mischievous glint in their '
               'eye.\\"{initiator} smirks and says to {target}, \\"This joke '
               'is definitely not for the easily scared, but I think you can '
               'handle it. Are you ready for a horrifying laugh?\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=198,
          lineno=502,
          tokens=229,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_AskForAdvice_targeted_friendly_emotionSpecific_Scared\\"{target}, '
               "I don't know what to do. I'm terrified, and I need your "
               'advice,\\" {initiator} admits, their voice '
               'shaking.\\"{target}, I\'m really scared about this situation. '
               'Can you help me figure out what to do?\\" {initiator} pleads, '
               'desperation in their eyes.\\"I hate to ask, {target}, but I\'m '
               'feeling so overwhelmed and frightened. Do you have any advice '
               'for me?\\" {initiator} asks, trying to hold back '
               'tears.\\"{target}, I\'ve never been this scared before. I '
               'trust your judgment, so can you please guide me?\\" '
               '{initiator} says, their voice barely audible.\\"I don\'t know '
               "who else to turn to, {target}. I'm so scared, and I need your "
               'guidance,\\" {initiator} confesses, their body '
               'trembling.\\"{target}, I\'ve always admired your wisdom and '
               "strength. I'm really frightened right now, and I could use "
               'your help,\\" {initiator} says, their eyes pleading for '
               'understanding.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=199,
          lineno=510,
          tokens=224,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve hit rock bottom, {target}, and I\'m terrified of '
               'what\'s to come. Can you please give me some advice?\\" '
               '{initiator} begs, holding back sobs.\\"{target}, I\'m in a '
               'really dark place, and fear is consuming me. I need your help '
               'to find a way out,\\" {initiator} says, their voice '
               'quivering.\\"I\'ve never asked for help like this before, '
               "{target}, but I'm truly scared, and I don't know what to do. "
               'Can you guide me?\\" {initiator} implores, their eyes filled '
               'with vulnerability.\\"{target}, I feel like I\'m drowning in '
               "fear, and I don't know how to swim. Can you please give me "
               'some advice?\\" {initiator} asks, struggling to maintain their '
               'composure.mixer_social_ComplainAboutLackOfPower_targeted_friendly_alwaysOn_billsLack\\"{target}, '
               "I can't believe I forgot to pay my electric bill! Now, we're "
               'stuck in the dark,\\" {initiator} grumbles, filled with '
               'frustration.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=200,
          lineno=519,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Ugh, {target}, you won\'t believe this, but I was so busy '
               'that I completely forgot to pay the electric bill. Now we have '
               'no power,\\" {initiator} complains, shaking their head in '
               'disbelief.\\"{target}, I messed up big time. I didn\'t pay the '
               'electric bill and now we\'re left without power,\\" '
               '{initiator} says, looking annoyed with themselves.\\"You know, '
               "{target}, it's so irritating when you forget something as "
               'important as paying the electric bill. I feel so powerless, '
               'literally,\\" {initiator} groans, feeling '
               'irritated.\\"{target}, I can\'t believe I did this. I didn\'t '
               'pay my electric bill, and now we have to deal with this power '
               'outage,\\" {initiator} complains, looking embarrassed.\\"I '
               "never thought I'd be the one to forget something this "
               "important, {target}. I didn't pay the electric bill, and now "
               'we\'re stuck in the dark,\\" {initiator} says, rolling their '
               'eyes at their own mistake.\\"I really messed up, {target}. I '
               "completely forgot to pay the electric bill, and now we're "
               'without power,\\" {initiator} admits, their voice filled with '
               'disappointment.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=201,
          lineno=525,
          tokens=214,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Can you believe it, {target}? I forgot to pay the electric '
               'bill, and now we have to deal with this annoying power '
               'outage,\\" {initiator} complains, visibly upset.\\"Of all the '
               "things I could forget, {target}, I can't believe it was the "
               'electric bill. Now we\'re stuck here without power,\\" '
               '{initiator} says, shaking their head in '
               'frustration.\\"{target}, I have to admit, I messed up. I '
               "didn't pay my electric bill on time, and now we're left "
               'without power,\\" {initiator} says, clearly annoyed with '
               'themselves.mixer_social_ComplainAboutLackOfWater_targeted_friendly_alwaysOn_bills\\"{target}, '
               "I can't believe this! I didn't pay my water bill, and now I "
               'don\'t have any water at home,\\" {initiator} grumbles in '
               'frustration.\\"Ugh, {target}, I messed up big time. I forgot '
               "to pay my water bill and now I'm stuck without any water at "
               'home,\\" {initiator} complains, looking annoyed.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=202,
          lineno=534,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, you won\'t believe how careless I\'ve been. I '
               "didn't pay my water bill, and now I have to deal with the "
               'consequences,\\" {initiator} says, shaking their head in '
               'disappointment.\\"I\'m so annoyed with myself, {target}. I '
               "didn't pay my water bill and now I'm left without water at "
               'home. What a mess,\\" {initiator} says, clearly irritated.\\"I '
               "can't even take a shower, {target}, because I forgot to pay my "
               'water bill! This is just the worst,\\" {initiator} complains, '
               'looking defeated.\\"{target}, I\'m in such a bad situation. I '
               "didn't pay my water bill, and now I'm suffering the "
               'consequences at home,\\" {initiator} groans, feeling the '
               'weight of their mistake.\\"I\'m such an idiot, {target}. I '
               "didn't pay my water bill, and now my home is completely "
               'without water,\\" {initiator} says, exasperated.\\"{target}, '
               'can you believe I forgot to pay my water bill? Now I have no '
               'water at home and it\'s driving me crazy,\\" {initiator} '
               'shares, looking for some sympathy.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=203,
          lineno=540,
          tokens=239,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Of all the bills to forget to pay, I had to forget my water '
               'bill, {target}. Now I\'m stuck in this mess,\\" {initiator} '
               'laments, frustrated with the situation.\\"I don\'t know what I '
               "was thinking, {target}. I didn't pay my water bill, and now "
               'I\'m left high and dry at home,\\" {initiator} says, clearly '
               'upset by their '
               'oversight.mixer_social_AskForAdvice_targeted_friendly_emotionSpecific\\"{target}, '
               "I've been struggling with something lately, and I really value "
               'your opinion. Can I ask for your advice?\\" {initiator} asks '
               'hesitantly.\\"{target}, you\'ve always been someone I can turn '
               'to for guidance. I need your advice on something important,\\" '
               '{initiator} says, looking concerned.\\"I\'m facing a tough '
               "decision, {target}, and I'm not sure what to do. I trust your "
               'judgment â\x80\x93 can you help me?\\" {initiator} pleads, '
               'seeking reassurance.\\"You always seem to have the answers, '
               '{target}. Can I ask you for some advice?\\" {initiator} '
               'inquires, hoping for some insight.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=204,
          lineno=550,
          tokens=233,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'m at a crossroads, and I don\'t know which '
               'path to take. I could really use your advice,\\" {initiator} '
               'admits, seeking support.\\"I know you\'ve been through a lot, '
               '{target}, and I think you might have some valuable advice for '
               'me. Can I talk to you about something?\\" {initiator} asks '
               'earnestly.\\"{target}, I\'m in a bit of a bind, and I don\'t '
               'know who else to turn to. Can I ask you for some advice?\\" '
               '{initiator} requests, sounding desperate.\\"I\'ve always '
               "admired your wisdom, {target}. I'm struggling with a "
               'situation, and I\'d appreciate your advice,\\" {initiator} '
               'says with respect.\\"You\'re someone I look up to, {target}, '
               'and I could really use your guidance right now. Can I ask you '
               'for some advice?\\" {initiator} pleads, looking '
               'vulnerable.\\"Hey, {target}, there\'s something I\'ve been '
               'wrestling with, and I could use your perspective. Do you have '
               'a moment to chat?\\" {initiator} asks, hoping for a helpful '
               'conversation.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=205,
          lineno=558,
          tokens=225,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_BegForgiveness_targeted_friendly_lowScore\\"{target}, '
               "I am so sorry for what I've done. I don't expect you to "
               'forgive me right away, but I had to tell you how much I regret '
               'it,\\" {initiator} pleads, their eyes filled with '
               'remorse.\\"Please, {target}, I know I messed up badly, but can '
               'you find it in your heart to forgive me?\\" {initiator} begs, '
               'desperate for understanding.\\"{target}, I can\'t change the '
               'past, but I promise to do better in the future. I just need '
               'you to give me a chance to prove myself,\\" {initiator} '
               'implores, hoping for forgiveness.\\"I don\'t know how to make '
               "it right, {target}, but I'm willing to do anything to earn "
               'your forgiveness,\\" {initiator} says earnestly, tears '
               'streaming down their face.\\"Please, {target}, I know I hurt '
               "you, and I'm so sorry. I'll do whatever it takes to make "
               'amends,\\" {initiator} pleads, a pained expression on their '
               'face.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=206,
          lineno=565,
          tokens=220,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I never meant to cause you pain, {target}, and I am so '
               'sorry for my actions. I beg you to forgive me,\\" {initiator} '
               'says, their voice full of sorrow and regret.\\"{target}, I '
               "can't express how much I regret what I've done. I just want to "
               'make things right between us. Can you forgive me?\\" '
               '{initiator} asks, looking vulnerable.\\"Please, {target}, I '
               "know I don't deserve your forgiveness, but I need to let you "
               'know how deeply sorry I am,\\" {initiator} says, their voice '
               'cracking with emotion.\\"I understand if you can\'t forgive me '
               'right now, {target}, but I will do everything I can to make it '
               'up to you,\\" {initiator} promises, their eyes pleading for '
               'understanding.\\"{target}, I was wrong and I hurt you. All '
               "I'm asking is for a chance to show you that I can change and "
               'be better,\\" {initiator} says, tears welling up in their '
               'eyes.mixer_social_AskToBeBestFriends_targeted_Friendly_HighScore'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=207,
          lineno=574,
          tokens=234,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, we\'ve been getting along so well lately. Would '
               'you like to be best friends?\\" {initiator} asks with a '
               'hopeful smile.\\"Hey, {target}, I\'ve been thinking... We\'re '
               'pretty great together. What do you say we become best '
               'friends?\\" {initiator} suggests, grinning.\\"{target}, I feel '
               "a real connection with you. I've never had a best friend "
               'before, but I\'d like you to be mine. What do you think?\\" '
               '{initiator} asks nervously.\\"I\'ve never met someone I '
               'clicked with like I do with you, {target}. How about we make '
               'it official and become best friends?\\" {initiator} proposes, '
               'looking excited.\\"Listen, {target}, I don\'t want to be too '
               'forward, but I think we make a great team. Would you be up for '
               'being my best friend?\\" {initiator} asks, trying to gauge '
               '{target}\'s reaction.\\"Hey, {target}, you know what would be '
               'awesome? If we became best friends! Are you in?\\" {initiator} '
               'asks, looking at {target} with anticipation.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=208,
          lineno=580,
          tokens=205,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been thinking, {target}, and I\'ve realized that '
               "you're the person I want as my best friend. What do you "
               'say?\\" {initiator} asks, hopeful for a positive '
               'response.\\"Life\'s too short not to have a best friend, and I '
               "can't think of anyone better than you, {target}. Will you be "
               'my best friend?\\" {initiator} inquires with a warm '
               'smile.\\"You know, {target}, I think we were destined to be '
               'best friends. What\'s your opinion on that?\\" {initiator} '
               'asks, looking for confirmation.\\"I\'ve never felt this close '
               'to anyone before, {target}. Would you do me the honor of '
               'becoming my best friend?\\" {initiator} asks sincerely, hoping '
               'for a positive '
               'answer.mixer_social_HilariousIcebreaker_greetings\\"{target}, '
               "why don't scientists trust atoms? Because they make up "
               'everything! Hi, I\'m {initiator}!\\" {initiator} says with a '
               'chuckle.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=209,
          lineno=589,
          tokens=220,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, what do you get when you cross a snowman and a '
               'vampire? Frostbite! I\'m {initiator}, nice to meet you!\\" '
               '{initiator} grins, extending their hand.\\"Knock knock, '
               "{target}. Who's there? Lettuce. Lettuce who? Lettuce in, it's "
               'cold out here! I\'m {initiator}, by the way,\\" {initiator} '
               'says, laughing at their own joke.\\"Hey {target}, did you hear '
               "about the kidnapping at the playground? They woke up! I'm "
               '{initiator}, it\'s a pleasure to meet you!\\" {initiator} '
               'says, giggling.\\"{target}, what do you call fake spaghetti? '
               'An impasta! Hi there, I\'m {initiator}!\\" {initiator} says, '
               'laughing heartily.\\"Did you know, {target}, that parallel '
               "lines have so much in common? It's a shame they'll never meet! "
               'I\'m {initiator}, nice to meet you!\\" {initiator} says, '
               'smiling broadly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=210,
          lineno=594,
          tokens=228,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, what do you call a pile of cats? A meowtain! '
               "I'm {initiator}, and I couldn't resist sharing that with "
               'you!\\" {initiator} says, chuckling.\\"{target}, why did the '
               'scarecrow win an award? Because he was outstanding in his '
               'field! Hi, I\'m {initiator}!\\" {initiator} says, laughing and '
               'extending a hand.\\"Guess what, {target}? I told my wife she '
               "was drawing her eyebrows too high. She looked surprised! I'm "
               '{initiator}, by the way,\\" {initiator} says, laughing at '
               'their own joke.\\"Hey {target}, what\'s the difference between '
               "a snowman and a snowwoman? Snowballs! I'm {initiator}, great "
               'to meet you!\\" {initiator} says, grinning from ear to '
               'ear.mixer_social_BragAboutFoodPoisoning_Targeted_Friendly_AlwaysOn\\"{target}, '
               "you wouldn't believe it, but I survived the worst food "
               'poisoning ever. I\'m like a superhero,\\" {initiator} says, '
               'puffing out their chest.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=211,
          lineno=603,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey, {target}, did I ever tell you about the time I got '
               'food poisoning and lived to tell the tale? You should be '
               'impressed,\\" {initiator} smirks.\\"{target}, I had food '
               "poisoning so bad that I thought I'd never recover. But here I "
               'am, stronger than ever,\\" {initiator} boasts.\\"Oh, {target}, '
               'I had this horrible food poisoning once, but I fought my way '
               'through it like a champ. I bet not everyone could handle '
               'that,\\" {initiator} says with pride.\\"You know, {target}, '
               "they say what doesn't kill you makes you stronger. Well, I "
               'survived food poisoning, so I must be pretty tough,\\" '
               '{initiator} brags.\\"Hey, {target}, have you ever had food '
               'poisoning? I did, and I managed to get through it like a '
               'warrior. You must think I\'m pretty resilient, huh?\\" '
               '{initiator} says, seeking validation.\\"{target}, I bet you '
               "didn't know this, but I've faced the worst food poisoning of "
               "my life and came out victorious. I'm pretty much "
               'invincible,\\" {initiator} says with a grin.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=212,
          lineno=609,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I don\'t mean to brag, {target}, but I once had the most '
               'awful bout of food poisoning, and I still managed to power '
               'through it. I\'m kind of amazing, right?\\" {initiator} says '
               'with a wink.\\"{target}, I\'ve been through the wringer with '
               "food poisoning, and I'm still standing. I guess I've got a "
               'pretty strong stomach,\\" {initiator} says, tapping their '
               'abdomen.\\"Surviving food poisoning is no small feat, '
               '{target}, but I managed to do it with flying colors. You can '
               'call me the master of resilience,\\" {initiator} says with a '
               'boastful '
               'laugh.mixer_social_ThrowDrink_targeted_mean_emotionSpecific\\"{initiator} '
               'watches {target} closely, anger boiling up inside, before '
               "suddenly splashing a drink in {target}'s face without "
               'warning.\\"\\"Without hesitation, {initiator} grabs a nearby '
               'drink and throws it in {target}\'s face.\\"\\"{initiator} '
               "can't take it anymore and, in a fit of rage, hurls a drink at "
               '{target}\'s face, leaving them dripping and stunned.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=213,
          lineno=619,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"As {target} continues to speak, {initiator} seethes with '
               'anger before finally snapping and throwing the contents of '
               'their glass into {target}\'s face.\\"\\"{initiator}, unable to '
               'contain their anger any longer, grabs the nearest beverage and '
               "splashes it all over {target}'s face, silencing them "
               'mid-sentence.\\"\\"With a sudden burst of fury, {initiator} '
               "picks up their drink and hurls it right into {target}'s "
               'unsuspecting face.\\"\\"{initiator} reaches their breaking '
               'point and, without a word, throws their drink directly at '
               '{target}\'s face, shocking the entire room.\\"\\"Enraged by '
               "{target}'s words, {initiator} impulsively grabs a drink and "
               "drenches {target}'s face, instantly stopping their "
               'speech.\\"\\"{initiator} narrows their eyes at {target}, then '
               'suddenly flings the contents of their glass right into '
               '{target}\'s face, leaving them speechless.\\"\\"Overcome with '
               'anger, {initiator} snatches up a drink and tosses it all over '
               '{target}\'s face, causing gasps from everyone around them.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=214,
          lineno=628,
          tokens=219,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_TakePictureTogether_targeted_Friendly_alwaysOn\\"{target}, '
               "let's capture this moment together! Can I take a picture with "
               'you?\\" {initiator} asks, smiling excitedly.\\"Hey {target}, '
               'this is such a great time, we should take a picture to '
               'remember it by. What do you say?\\" {initiator} suggests, '
               'holding up their phone.\\"{target}, I\'ve always wanted a '
               'picture with you. Mind if we take one right now?\\" '
               '{initiator} asks, looking hopeful.\\"Would you mind if we took '
               'a photo together, {target}? I think it would be a nice memory '
               'to have,\\" {initiator} says, shyly.\\"I have this feeling '
               "that we're going to look back on this moment one day and "
               'smile. Let\'s take a picture together, {target},\\" '
               '{initiator} proposes, grinning.\\"Come on, {target}, let\'s '
               "snap a quick picture together. I promise it'll be worth "
               'it!\\" {initiator} says, trying to convince {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=215,
          lineno=636,
          tokens=216,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Life\'s too short not to capture memories, don\'t you '
               'think, {target}? Let\'s take a picture together,\\" '
               '{initiator} suggests, extending their arm for a selfie.\\"Hey '
               '{target}, I think this is the perfect moment for a photo, '
               'don\'t you? Let\'s take one together!\\" {initiator} says, '
               'enthusiastically.\\"{target}, you know what would make this '
               "moment even better? A picture of us together. Let's take "
               'one!\\" {initiator} says, grabbing their phone.\\"I want to '
               "remember this moment forever, {target}. Let's take a picture "
               'together, please?\\" {initiator} asks, their eyes shining with '
               'anticipation.mixer_social_ShowOffMuscles_targeted_friendly_emotionSpecific\\"{target}, '
               'check out these guns,\\" {initiator} says, flexing their '
               'biceps proudly.\\"Hey, {target}, I\'ve been working out '
               'lately, and I want to show you my progress. What do you '
               'think?\\" {initiator} asks, rolling up their sleeves to reveal '
               'toned muscles.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=216,
          lineno=646,
          tokens=239,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Guess who\'s been hitting the gym, {target}? Feast your '
               'eyes on these bad boys,\\" {initiator} says, confidently '
               'flexing their muscles.\\"{target}, I think my hard work is '
               'finally paying off. Care to take a look at these muscles?\\" '
               '{initiator} grins, striking a pose.\\"Look at this, '
               '{target}!\\" {initiator} exclaims, flexing their arms to show '
               'off their newfound strength.\\"{target}, I\'ve been trying to '
               "get in shape lately. What do you think of the progress I've "
               'made?\\" {initiator} asks, proudly displaying their '
               'muscles.\\"I\'ve been putting in some serious effort at the '
               'gym, {target}. Care to check out the results?\\" {initiator} '
               'says, flexing for emphasis.\\"Remember how I said I was going '
               'to get fit, {target}? Well, take a look at these muscles '
               'now!\\" {initiator} boasts, proudly showing off their '
               'gains.\\"Hey, {target}, I\'ve been working on my fitness, and '
               'I wanted to show you the results. What do you think?\\" '
               '{initiator} asks, flexing their muscles.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=217,
          lineno=653,
          tokens=219,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Check this out, {target}! I think all those workouts are '
               'finally starting to show,\\" {initiator} says, proudly '
               'displaying their toned muscles.# '
               '"mixer_socials_TellJoke_group_Funny_alwaysOn": {#         '
               '"\\"{target}, you\'re going to love this one,\\" {initiator} '
               'says, a grin spreading across their face as they prepare to '
               'tell a joke.",#         "\\"Hey {target}, have you heard this '
               'one before?\\" {initiator} asks, chuckling before they share '
               'the joke with the group.",#         "\\"{initiator} suddenly '
               "bursts into laughter, catching {target}'s attention. "
               '\\"You\'ve got to hear this joke,\\" they say, eager to '
               'share.",#         "\\"Everyone, especially you {target}, '
               'listen up! I\'ve got a hilarious joke to tell,\\" {initiator} '
               'announces, drawing the group\'s attention.",#         '
               '"\\"Alright, this one\'s for you, {target}. I know you love a '
               'good joke,\\" {initiator} says, ready to deliver the '
               'punchline.",'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=218,
          lineno=663,
          tokens=240,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"{initiator} leans in closer to {target} and the '
               'others, a mischievous smile on their face. \\"You guys ready '
               'for this?\\" they ask before diving into the joke.",#         '
               '"\\"I just heard the funniest joke, and I have to share it '
               'with you, {target},\\" {initiator} says, barely containing '
               'their laughter.",#         "\\"{initiator} looks at {target} '
               'and grins. \\"You\'re going to appreciate this one,\\" they '
               'say, eager to share the joke with the group.",#         '
               '"\\"Okay, {target}, this joke is right up your alley. Gather '
               '\'round, everyone!\\" {initiator} exclaims, preparing to '
               'entertain the group.",#         "\\"I found a joke that I know '
               'will make you laugh, {target}. Let me tell it to everyone,\\" '
               '{initiator} says, excited to bring some humor to the '
               'group."mixer_social_ProvideLogicalSolution_targeted_Friendly_alwaysOn_skills\\"{target}, '
               "I've been thinking about the issues you're facing, and I "
               'believe I\'ve come up with some logical solutions,\\" '
               '{initiator} says confidently.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=219,
          lineno=673,
          tokens=222,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I know you\'re struggling with this problem, '
               'but I think I have a few ideas that might help,\\" {initiator} '
               'offers with a hopeful smile.\\"{target}, I\'ve been giving '
               "your situation some thought, and I've come up with a few "
               'logical steps you could take to resolve it,\\" {initiator} '
               'suggests carefully.\\"I couldn\'t help but overhear your '
               'problem, {target}, and I think I might have some rational '
               'solutions you could try,\\" {initiator} says, trying not to '
               'sound intrusive.\\"Don\'t worry, {target}. I\'ve been '
               'analyzing your situation and I think I have a few possible '
               'solutions for you,\\" {initiator} reassures, attempting to '
               'lift {target}\'s spirits.\\"Hey {target}, I\'ve been '
               'considering your problem, and I believe I can help you come up '
               'with some logical strategies to tackle it,\\" {initiator} says '
               'encouragingly.\\"I understand you\'re going through a tough '
               'time, {target}, but I think I might have some reasonable '
               'solutions that could help you out,\\" {initiator} offers '
               'kindly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=220,
          lineno=679,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve been pondering your predicament and came up '
               'with a few logical approaches you could try. Would you like to '
               'hear them?\\" {initiator} asks gently.\\"Let\'s sit down and '
               "discuss your problem, {target}. I'm sure we can come up with "
               'some logical and effective solutions together,\\" {initiator} '
               'proposes with a supportive tone.\\"Listen, {target}, I think I '
               'have some ideas on how you can logically address your issue. '
               'Let\'s work through this together,\\" {initiator} says, '
               'extending a helping '
               'hand.mixer_social_TalkAboutBestBait_targeted_Friendly_alwaysOn_skills\\"{target}, '
               'do you have any advice on the best bait to use when fishing? '
               'I\'m trying to improve my chances of catching something,\\" '
               '{initiator} asks curiously.\\"I\'ve heard there are different '
               'baits for different fish, {target}. What do you think works '
               'best around here?\\" {initiator} inquires, hoping for some '
               'local knowledge.\\"Hey {target}, I\'ve been experimenting with '
               'various baits while fishing. What\'s your go-to choice?\\" '
               '{initiator} asks, seeking expert advice.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=221,
          lineno=689,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'m pretty new to fishing, {target}, and I was wondering '
               'if you could give me some tips on choosing the best bait,\\" '
               '{initiator} requests, looking for guidance.\\"{target}, I '
               "noticed you've had quite the success with fishing. Mind "
               'sharing your secret on the best bait to use?\\" {initiator} '
               'probes, wanting to learn from the best.\\"So, {target}, I\'ve '
               "been trying different baits, but I can't seem to find one that "
               'really works well. Any suggestions?\\" {initiator} asks, '
               'hoping for a breakthrough.\\"Between live bait and artificial '
               'lures, what do you think works best when fishing, {target}?\\" '
               '{initiator} inquires, seeking a better understanding of the '
               'options.\\"{target}, I\'ve read so many articles about the '
               "best bait for fishing, but I'd really appreciate your opinion. "
               'What\'s your favorite choice?\\" {initiator} asks, valuing '
               'personal experience.\\"Everyone seems to have their own '
               "preference when it comes to fishing bait, {target}. What's "
               'your personal favorite, and why?\\" {initiator} questions, '
               'trying to learn from different perspectives.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=222,
          lineno=695,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been struggling to find the right bait for fishing, '
               '{target}. Can you share your top picks and maybe some tips on '
               'when to use each one?\\" {initiator} asks, seeking a '
               'comprehensive '
               'answer.mixer_social_TalkAboutCooking_targeted_Friendly_alwaysOn_skills\\"{target}, '
               "I've been thinking about trying out a new recipe. Any "
               'suggestions?\\" {initiator} asks curiously.\\"{initiator} to '
               "{target}, what's your favorite dish to cook? I need some "
               'inspiration.\\"\\"I\'ve been wanting to get better at cooking, '
               '{target}. Could you share some of your culinary secrets with '
               'me?\\" {initiator} inquires.\\"Hey, {target}, I was wondering '
               'if you could teach me how to make that amazing dish you '
               'prepared last time,\\" {initiator} says with '
               'excitement.\\"I\'ve been trying to expand my cooking skills, '
               '{target}. What do you think is a must-try recipe?\\" '
               '{initiator} asks enthusiastically.\\"Last night I tried my '
               'hand at a new recipe, {target}. Have you ever had a cooking '
               'disaster?\\" {initiator} asks, chuckling.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=223,
          lineno=706,
          tokens=233,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve heard you\'re quite the chef. I\'d love to '
               'learn some tips and tricks from you,\\" {initiator} says, '
               'admiringly.\\"You always seem to know your way around the '
               'kitchen, {target}. How did you learn to cook so well?\\" '
               '{initiator} asks, genuinely curious.\\"{initiator} to '
               "{target}, I've been craving some comfort food lately. What's "
               'your go-to dish when you need something warm and '
               'satisfying?\\"\\"I\'m planning a dinner party, {target}, and I '
               'could use some advice on what to cook. Can you help me come up '
               'with a menu?\\" {initiator} asks hopefully.# '
               '"mixer_social_TellEngagingStory_group_Friendly_MiddleScore": '
               '{#         "\\"{target}, gather around everyone, I have a '
               'story to share that I think you\'ll all find captivating,\\" '
               '{initiator} says with a grin.",#         "\\"Hey {target} and '
               'everyone, let me share this incredible story I heard the other '
               'day. You won\'t believe what happened!\\" {initiator} '
               'exclaims, excitement in their voice.",'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=224,
          lineno=716,
          tokens=225,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"Have I ever told you all the story about the '
               "time I stumbled upon something extraordinary? Gather 'round, "
               '{target}, I promise it\'s worth a listen,\\" {initiator} says, '
               'eyes sparkling with anticipation.",#         "\\"Everyone, '
               'including you {target}, listen up! I have a tale to tell that '
               'will leave you on the edge of your seats,\\" {initiator} '
               'announces with a theatrical flourish.",#         "\\"You know, '
               "{target}, there's a story I've been meaning to share with you "
               'and the rest of the group. I think it\'s finally time,\\" '
               '{initiator} says, a twinkle in their eye.",#         '
               '"\\"Alright, {target} and friends, it\'s time for a little '
               'storytime. Trust me, you\'ll want to hear this one,\\" '
               '{initiator} says, a mischievous smile playing on their '
               'lips.",#         "\\"Have I got a story for you, {target}! '
               'Gather the others, and let me regale you with a most '
               'intriguing tale,\\" {initiator} says, clearly eager to share '
               'their story.",'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=225,
          lineno=721,
          tokens=219,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"Hey {target}, remember that story I mentioned a '
               "while ago? I think it's time I shared it with the whole "
               'group,\\" {initiator} says, excitement building in their '
               'voice.",#         "\\"Picture this, {target} and everyone: I '
               'was minding my own business when the most unbelievable thing '
               'happened. Let me tell you all about it,\\" {initiator} says, '
               'drawing the group in with their enthusiasm.",#         '
               '"\\"{target}, do you and the others have a moment? I\'d like '
               'to share an amazing story that I think you\'ll all enjoy,\\" '
               '{initiator} says, eager to captivate their audience."# '
               '"mixer_social_TellUnbelievableStory_group_friendly_emotionspecific": '
               '{#         "\\"{target}, you\'re not going to believe what '
               'happened to me last night,\\" {initiator} starts, a gleam in '
               'their eye.",#         "\\"I\'ve got a crazy story to tell, '
               'guys. Gather around and prepare for the unbelievable,\\" '
               '{initiator} announces to {target} and their friends.",'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=226,
          lineno=730,
          tokens=218,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"{target}, have I got a story for you and the '
               'rest of the group! You won\'t believe what happened,\\" '
               '{initiator} says excitedly.",#         "\\"Everyone, listen '
               "up! I've got an incredible story to share that you won't "
               'believe,\\" {initiator} says, looking at {target} and the rest '
               'of the group.",#         "\\"Okay, {target}, this is going to '
               "sound totally unreal, but I've got to share this story with "
               'you and everyone else,\\" {initiator} says with a '
               'grin.",#         "\\"Guys, I need to tell you all about this '
               'unbelievable experience I had,\\" {initiator} says, getting '
               'the attention of {target} and the others.",#         '
               '"\\"Listen up, {target} and friends, I\'ve got a wild story '
               'that you just have to hear,\\" {initiator} says, ready to '
               'share their unbelievable tale.",#         "\\"Get ready for '
               'the most unbelievable story of your lives, {target} and the '
               'rest of you,\\" {initiator} says confidently.",'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=227,
          lineno=736,
          tokens=241,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"{target}, remember how you always say I have the '
               "craziest stories? Well, I've got another one for you and the "
               'group,\\" {initiator} says, preparing to share their latest '
               'adventure.",#         "\\"Everyone, gather around. I\'ve got '
               'an unbelievable story that you all need to hear, especially '
               'you, {target},\\" {initiator} says, eager to share their '
               'tale."mixer_social_TalkAboutGrilledCheese_targeted_Friendly_alwaysOn_aspiration\\"{target}, '
               'have you ever tried a grilled cheese sandwich with a twist? I '
               'experimented with some ingredients the other day,\\" '
               '{initiator} says enthusiastically.\\"Hey {target}, do you know '
               "the secret to making the perfect grilled cheese sandwich? I've "
               'been trying to master it,\\" {initiator} asks, looking for '
               'advice.\\"Grilled cheese sandwiches always remind me of my '
               'childhood, {target}. Do you have any special memories with '
               'them?\\" {initiator} inquires, feeling nostalgic.\\"The other '
               'day, I had the most amazing grilled cheese sandwich, {target}. '
               'Let me tell you all about it,\\" {initiator} says, eager to '
               'share their experience.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=228,
          lineno=746,
          tokens=244,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been craving a grilled cheese sandwich all day, '
               '{target}. Do you have any unique recipes I should try?\\" '
               '{initiator} asks, hoping for some inspiration.\\"{target}, '
               'have you ever tried a sweet version of a grilled cheese '
               "sandwich? I'm thinking about experimenting with some "
               'dessert-inspired fillings,\\" {initiator} suggests, looking '
               'for input.\\"Did you know, {target}, that there are so many '
               'different types of grilled cheese sandwiches around the world? '
               'I was amazed when I discovered it,\\" {initiator} says, '
               'excited to share their newfound knowledge.\\"I came across a '
               'grilled cheese food truck the other day, {target}. It got me '
               'thinking about how versatile and universally loved this simple '
               'sandwich is,\\" {initiator} muses.\\"Every time I make a '
               'grilled cheese sandwich, I think about the first time I made '
               'one with my mom, {target}. It\'s such a comforting memory,\\" '
               '{initiator} shares, fondly recalling the past.\\"I\'ve been '
               'perfecting my grilled cheese sandwich recipe, {target}, and I '
               "think I've finally cracked it. Want to try one and give me "
               'your honest opinion?\\" {initiator} asks, hoping for feedback.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=229,
          lineno=754,
          tokens=241,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_ShareSecret_targeted_Friendly_HighScore\\"{target}, '
               "can I tell you something? I know it's a bit out of the blue, "
               'but I feel like I can trust you,\\" {initiator} says '
               'timidly.\\"Hey, {target}, there\'s something I\'ve been '
               "wanting to share with you. I think you're the right person to "
               'confide in,\\" {initiator} says, taking a deep '
               'breath.\\"{target}, I\'ve been keeping something from you, and '
               'it\'s time I let it out. I hope you understand,\\" {initiator} '
               'says, looking nervous.\\"You know, {target}, there\'s '
               "something I've been hiding for a while, but I think it's time "
               'I tell you,\\" {initiator} says hesitantly.\\"{target}, I\'ve '
               "never shared this with anyone before, but I feel like you're "
               'someone I can trust. So here it goes,\\" {initiator} says, '
               'gathering up their courage.\\"I\'ve been carrying this secret '
               "around for a long time, {target}, and I think it's time to "
               'finally share it with someone. Can I trust you?\\" {initiator} '
               'asks cautiously.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=230,
          lineno=762,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I want to tell you something, something I\'ve '
               'never told anyone else. Are you okay with that?\\" {initiator} '
               'says, looking for confirmation.\\"You\'re someone I really '
               'trust, {target}, and I feel like I can share this secret with '
               'you. I hope you don\'t think differently of me afterward,\\" '
               '{initiator} says with a hint of worry.\\"Can I confide in you, '
               "{target}? There's something I've been keeping to myself, and I "
               'think you\'re the right person to share it with,\\" '
               '{initiator} says, looking hopeful.\\"Hey, {target}, I know '
               "we've gotten pretty close, and there's something I think you "
               "should know about me. I've never told anyone before, but I "
               'trust you,\\" {initiator} says '
               'sincerely.mixer_social_SharePhoto\\"{target}, check this out! '
               "I've got a really cool photo on my phone I want to show "
               'you,\\" {initiator} says excitedly.\\"{target}, I came across '
               "this photo and I think you'll find it interesting. Take a "
               'look,\\" {initiator} suggests, offering their phone to '
               '{target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=231,
          lineno=772,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I was browsing my gallery and found this picture that made '
               'me laugh. I thought you\'d enjoy it too,\\" {initiator} says, '
               'grinning as they show {target} their phone screen.\\"Can I '
               'show you something, {target}? I took this photo the other day '
               'and I think you\'ll really appreciate it,\\" {initiator} says, '
               'scrolling through their phone.\\"Look at this photo I found on '
               'my phone, {target}. It brings back such great memories,\\" '
               '{initiator} says nostalgically, showing the picture to '
               '{target}.\\"Hey {target}, I took this photo and I think it '
               'turned out really well. What do you think?\\" {initiator} '
               "asks, seeking {target}'s opinion as they hand over their "
               'phone.\\"{target}, this photo I found on my phone is just too '
               'good not to share. You have to see it,\\" {initiator} says '
               'enthusiastically, presenting their phone to {target}.\\"I '
               'captured this beautiful moment on my phone, {target}. I think '
               'you\'ll love it. Take a look,\\" {initiator} says, proud of '
               'their photography skills as they show the picture to {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=232,
          lineno=780,
          tokens=217,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_TalkAboutNewApp_targeted_Friendly_alwaysOn_career\\"{target}, '
               "I've been working on this new app, and I think it could really "
               'change things. Can I share it with you?\\" {initiator} asks '
               'excitedly.\\"Hey {target}, I\'ve got this great idea for an '
               'app I\'ve been developing. Mind if I run it by you?\\" '
               '{initiator} inquires, eager for input.\\"{target}, I\'ve been '
               'pouring my heart into this new app idea, and I really value '
               'your opinion. Can we talk about it?\\" {initiator} asks '
               'nervously.\\"I\'ve been tinkering with this new app concept, '
               'and I think it has potential. Would you mind giving me your '
               'thoughts on it, {target}?\\" {initiator} suggests, hoping for '
               'feedback.\\"Guess what, {target}? I\'m working on a '
               "groundbreaking app, and I'd love to hear your thoughts on it. "
               'Are you up for a chat?\\" {initiator} asks, bubbling with '
               'enthusiasm.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=233,
          lineno=787,
          tokens=241,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve been secretly developing this app that I '
               'think could be the next big thing. Can I share it with you and '
               'get your opinion?\\" {initiator} questions, a twinkle in their '
               'eye.\\"So, I have this new app idea, {target}, and I can\'t '
               "get it out of my head. Can we discuss it? I'd love your "
               'input,\\" {initiator} says, a hint of desperation in their '
               'voice.\\"I\'ve been working on this app, and I\'m at a '
               'crossroads. {target}, I need your expertise. Can we talk about '
               'it?\\" {initiator} asks, seeking guidance.\\"You know, '
               "{target}, I've been developing this new app, and I'm really "
               "proud of it. I'd be honored if you'd take a look and share "
               'your thoughts,\\" {initiator} says, beaming with pride.\\"Hey '
               "{target}, do you have a minute? I've been working on this new "
               'app, and I could really use your insight. Are you available to '
               'chat?\\" {initiator} asks, hoping for a positive '
               'response.mixer_social_ThankForComing_targeted_Friendly_alwaysOn_Event'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=234,
          lineno=796,
          tokens=241,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I just wanted to take a moment to thank you for '
               'coming to the event. It means a lot to me,\\" {initiator} says '
               'with a warm smile.\\"{target}, I can\'t express how grateful I '
               'am for your presence at the event. Your support means the '
               'world to me,\\" {initiator} says sincerely.\\"{target}, thank '
               'you so much for being here at the event. Your presence makes '
               'it even more special,\\" {initiator} says, appreciating the '
               'gesture.\\"I just wanted to say how much I appreciate you '
               "coming to the event, {target}. It wouldn't have been the same "
               'without you,\\" {initiator} says, making eye contact.\\"Your '
               'attendance at the event means more to me than I can put into '
               'words, {target}. Thank you for being here,\\" {initiator} '
               'says, touched by the gesture.\\"{target}, seeing you at the '
               'event made my day. Thank you for taking the time to be here '
               'and support me,\\" {initiator} says gratefully.\\"I\'m so glad '
               'you could make it to the event, {target}. Your presence truly '
               'made a difference,\\" {initiator} says with a smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=235,
          lineno=803,
          tokens=222,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I can\'t thank you enough for showing up at the '
               'event. Your support means everything to me,\\" {initiator} '
               'says earnestly.\\"Having you at the event made all the '
               'difference, {target}. Thank you for being here and supporting '
               'me,\\" {initiator} says, clearly touched.\\"{target}, I just '
               'wanted to let you know how much it meant to me that you came '
               'to the event. Your support has been incredible,\\" {initiator} '
               'says, expressing their '
               'gratitude.mixer_social_TellDirtyJoke_targeted_funny_emotionSpecific\\"{target}, '
               "I just heard the most hilarious dirty joke. You've got to "
               'listen to this one,\\" {initiator} says with a mischievous '
               'grin.\\"Hey {target}, you\'ve got a good sense of humor, '
               'right? Check out this dirty joke I just heard,\\" {initiator} '
               'says, laughing in anticipation.\\"{target}, I don\'t usually '
               'share these kinds of jokes, but this one is too good not to '
               'share. Are you ready?\\" {initiator} asks with a cheeky smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=236,
          lineno=813,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Alright, {target}, brace yourself for the funniest dirty '
               'joke I\'ve ever heard. You\'re going to love it,\\" '
               '{initiator} says, barely containing their laughter.\\"Listen '
               "up, {target}, because I've got a dirty joke that'll have you "
               'rolling on the floor laughing,\\" {initiator} says, grinning '
               'from ear to ear.\\"Okay {target}, I promise you\'ve never '
               'heard a dirty joke like this one. Are you ready for it?\\" '
               '{initiator} asks, giggling in anticipation.\\"{target}, I\'ve '
               'been dying to tell you this dirty joke I heard the other day. '
               'You have to hear it,\\" {initiator} says, suppressing a '
               'laugh.\\"I know you\'ll appreciate this one, {target}. Prepare '
               'yourself for the best dirty joke ever,\\" {initiator} says, '
               'already laughing at the thought.\\"Hey {target}, I\'ve got a '
               'dirty joke that\'s perfect for you. Are you ready for this?\\" '
               '{initiator} asks, smirking.\\"This dirty joke is just too good '
               'not to share, {target}. Get ready to laugh your socks off,\\" '
               '{initiator} says, eager to share the punchline.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=237,
          lineno=822,
          tokens=233,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# "mixer_social_TellDramaticStory_group_Friendly_MiddleScore": '
               '{#         "\\"{target}, gather around with the others. I have '
               'a tale that will leave you all on the edge of your seats,\\" '
               '{initiator} announces with a grin.",#         "\\"{target}, do '
               'you remember the time I barely escaped from a dangerous '
               'situation? Let me share the story with everyone,\\" '
               '{initiator} says, excitement in their voice.",#         '
               '"\\"Everyone, including you, {target}, needs to hear this '
               'incredible story I have to tell. Gather around and listen '
               'closely,\\" {initiator} says, motioning for the group to come '
               'closer.",#         "\\"I\'ve got a story that I\'ve been dying '
               'to share with all of you, especially you, {target}. So, lend '
               'me your ears and prepare to be amazed,\\" {initiator} says, an '
               'eager look on their face.",#         "\\"Have I ever told you '
               'the story of my most dramatic adventure, {target}? No? Well, '
               'let\'s gather the group and I\'ll share it with everyone,\\" '
               '{initiator} suggests, excitedly.",'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=238,
          lineno=829,
          tokens=244,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"There\'s this remarkable story I want to share '
               'with everyone. {target}, you and the others should definitely '
               'listen to this one,\\" {initiator} says, with a twinkle in '
               'their eye.",#         "\\"{target}, you and the rest of the '
               'group need to hear this incredible tale of danger and '
               'suspense. Trust me, it\'s a nail-biter,\\" {initiator} says, '
               'gesturing for everyone to gather around.",#         '
               '"\\"Everyone, including you, {target}, should gather around '
               "for an epic story I'm about to share. It's one you'll never "
               'forget,\\" {initiator} says, grinning from ear to '
               'ear.",#         "\\"I have a story that I think will captivate '
               "everyone, especially you, {target}. So, let's gather around "
               'and I\'ll begin this amazing tale,\\" {initiator} says, their '
               'eyes filled with anticipation.",#         "\\"{target}, do you '
               'and the others have time for an incredible story? Because I '
               'have one that will leave you all speechless,\\" {initiator} '
               'says, the excitement evident in their voice."# '
               '"mixer_socials_TellFunnyStory_group_Funny_alwaysOn": {'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=239,
          lineno=838,
          tokens=250,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"{target}, have I ever told you about the time '
               "when I accidentally walked into a stranger's house? Trust me, "
               'it\'s hilarious,\\" {initiator} says, grinning.",#         '
               '"\\"Hey {target}, I\'ve got a story that will have you in '
               'stitches. Gather \'round, everyone, and prepare to laugh,\\" '
               '{initiator} announces, beaming.",#         "\\"Everyone, I '
               'just remembered this hilarious incident that happened to me a '
               'while ago, and I think {target} especially will get a kick out '
               'of it,\\" {initiator} says, chuckling.",#         '
               '"\\"{target}, you and the others have got to hear this one. I '
               'promise it\'s a story you\'ll never forget,\\" {initiator} '
               'says, eyes twinkling with amusement.",#         "\\"Alright, '
               '{target} and friends, buckle up for a funny story. I guarantee '
               'it\'ll have you laughing out loud,\\" {initiator} says, a '
               'mischievous smile on their face.",#         "\\"Guys, wait '
               "until you hear this story. It's so funny, even {target} won't "
               'be able to keep a straight face,\\" {initiator} teases, '
               'excited to share the tale.",'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=240,
          lineno=844,
          tokens=234,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"Okay, {target}, you know how I\'m always getting '
               'into ridiculous situations? Well, this one tops them all, and '
               'I need to share it with the group,\\" {initiator} says, barely '
               'suppressing laughter.",#         "\\"Everyone, gather \'round! '
               'I have a story that is sure to make {target} laugh, and '
               'possibly the rest of you as well,\\" {initiator} says, trying '
               'to contain their own laughter.",#         "\\"I can\'t believe '
               "I haven't told you guys this story yet. It's absolutely "
               'hilarious, and I know {target} especially will appreciate '
               'it,\\" {initiator} says, a wide grin spreading across their '
               'face.",#         "\\"Alright, {target}, this one\'s for you. I '
               "guarantee you'll be rolling on the floor laughing by the end "
               'of this story,\\" {initiator} says, eager to entertain the '
               'group."mixer_social_MakePeaceAfterFight\\"{target}, I\'ve had '
               'some time to think, and I want to apologize for our fight. Can '
               'we talk and find a way to move forward?\\" {initiator} asks, '
               'extending an olive branch.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=241,
          lineno=853,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I realize I let my emotions get the best of me, {target}. '
               'I\'m sorry. Can we put this behind us and start fresh?\\" '
               '{initiator} says, hoping for reconciliation.\\"{target}, I\'ve '
               'been thinking about our argument, and I want you to know that '
               "I value our relationship more than being right. Let's make "
               'peace,\\" {initiator} suggests sincerely.\\"Hey, {target}, I '
               "know we've had our differences, but I want to make amends. Can "
               'we find common ground and move past this?\\" {initiator} asks '
               'earnestly.\\"I hate that we\'ve been at odds, {target}. I\'m '
               'willing to put my pride aside and apologize. Can we work '
               'towards understanding each other better?\\" {initiator} '
               'proposes, looking for resolution.\\"Life\'s too short to hold '
               "grudges, {target}. I'm sorry for our fight, and I hope we can "
               'rebuild our bond,\\" {initiator} says, offering a sincere '
               'apology.\\"{target}, our friendship means more to me than any '
               "disagreement. Let's put this behind us and focus on the "
               'future. Are you with me?\\" {initiator} asks, seeking '
               'reconciliation.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=242,
          lineno=859,
          tokens=231,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I know we both said things we didn\'t mean, {target}. I\'m '
               'sorry. Let\'s agree to disagree and move on from this,\\" '
               '{initiator} says, hoping for a positive response.\\"Can we '
               'talk, {target}? I want to apologize for my part in our '
               'argument. I hope we can find a way to heal and move forward '
               'together,\\" {initiator} says, looking for closure.\\"I\'ve '
               'been reflecting on our fight, {target}, and I realize how much '
               "I value our relationship. Let's forgive each other and start "
               'anew,\\" {initiator} suggests, offering a heartfelt apology.# '
               '"mixer_social_TellOutrageousStory_group_Funny_HighScore": '
               '{#         "\\"{target}, you won\'t believe what happened to '
               "me the other day. Gather around, everyone; you'll want to hear "
               'this!\\" {initiator} exclaims, excitedly.",#         "\\"Hey '
               "{target}, have you ever heard something so crazy that it's "
               "hard to believe? Well, buckle up, because I've got a story for "
               'you and the others,\\" {initiator} says, grinning.",'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=243,
          lineno=868,
          tokens=219,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"{target}, gather everyone together. I\'ve got an '
               "incredible story to share, and you're all going to love "
               'it!\\" {initiator} says, eyes sparkling with '
               'excitement.",#         "\\"Everyone, listen up! You won\'t '
               'believe what happened to me. {target}, you especially are '
               'going to enjoy this one,\\" {initiator} announces with '
               'enthusiasm.",#         "\\"I\'ve got to tell you all something '
               "that happened to me. It's so wild, you'll think I'm making it "
               'up. {target}, you\'re in for a treat,\\" {initiator} says, '
               'chuckling.",#         "\\"Alright, everyone, I\'ve got a story '
               "for you that's so outrageous, you'll be talking about it for "
               'days. {target}, you\'re going to love this,\\" {initiator} '
               'says, with a mischievous grin.",#         "\\"{target}, call '
               "the others over! I've got a story that's so unbelievable, "
               'you\'ll think I\'ve lost my mind,\\" {initiator} exclaims, '
               'barely containing their laughter.",'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=244,
          lineno=873,
          tokens=241,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"Guys, you won\'t believe what happened! Get over '
               'here and let me tell you this incredible story. {target}, you '
               'won\'t want to miss this,\\" {initiator} says, waving everyone '
               'closer.",#         "\\"Everyone, gather around! I\'ve got a '
               "story that's so outlandish, you'll question if it's even "
               "possible. {target}, trust me, you're going to want to hear "
               'this,\\" {initiator} says, a broad smile on their '
               'face.",#         "\\"Listen up, folks! I\'ve got an '
               'extraordinary story to tell, and I need everyone to hear it. '
               "{target}, make sure you're paying attention. You'll never "
               'believe what I\'m about to share,\\" {initiator} insists, '
               'clearly eager to share their '
               'tale."mixer_social_SelfDeprecatingJoke_group_funny_emotionSpecific\\"{target}, '
               "you know what's funny about me? I'm the kind of person "
               'who...\\" {initiator} starts, chuckling at their own '
               'expense.\\"{target}, have you heard this one about me? It\'s '
               'hilarious, but a little embarrassing,\\" {initiator} says with '
               'a grin.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=245,
          lineno=882,
          tokens=224,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I\'ve got a joke for you, and the punchline '
               'is... me!\\" {initiator} laughs, poking fun at '
               'themselves.\\"You know what\'s really funny, {target}? My '
               'life! Let me tell you about this ridiculous thing I did,\\" '
               '{initiator} says, laughing at their own '
               'misfortune.\\"{target}, you\'ll get a kick out of this. I '
               "can't believe I actually did this, but it's too funny not to "
               'share,\\" {initiator} admits, shaking their head in '
               'amusement.\\"Alright, {target}, I\'ve got a hilarious story '
               'for you. But fair warning, I\'m the butt of the joke,\\" '
               '{initiator} says, grinning sheepishly.\\"I don\'t know if I '
               "should be embarrassed or proud of this, {target}, but I've got "
               'a great self-deprecating joke to share,\\" {initiator} says, '
               'chuckling.\\"Get ready to laugh, {target}, because I\'ve got a '
               'joke that makes me look like a total fool,\\" {initiator} '
               'confesses, already laughing at themselves.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=246,
          lineno=888,
          tokens=234,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve got a story that proves I\'m not the '
               "brightest bulb in the box, but at least it's good for a "
               'laugh,\\" {initiator} says, poking fun at their own '
               'expense.\\"I can\'t believe I\'m going to tell you this, '
               "{target}, but I did something so dumb that it's actually "
               'hilarious. You ready?\\" {initiator} asks, grinning at their '
               'own '
               'misadventure.mixer_social_BroBump_targeted_Friendly_alwaysOn\\"{target}, '
               'that was awesome! Bring it in for a bro bump,\\" {initiator} '
               'says, grinning and raising their fist.\\"Hey {target}, let\'s '
               'celebrate with a bro bump!\\" {initiator} says, extending '
               'their fist towards {target}.\\"{initiator} smiles at {target} '
               'and says, \\"We make a great team! Bro bump?\\"\\"Nice one, '
               '{target}! Fist bump to celebrate?\\" {initiator} suggests, '
               'holding out their fist.\\"{initiator} looks at {target} and '
               'says, \\"You\'ve earned yourself a bro bump for that one, my '
               'friend!\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=247,
          lineno=899,
          tokens=239,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, that deserves a bro bump! Bump it, buddy!\\" '
               '{initiator} says, enthusiastically offering their '
               'fist.\\"{initiator} laughs and says, \\"{target}, that was '
               'epic! Let\'s seal the deal with a bro bump.\\"\\"Great job, '
               '{target}! Let\'s do a bro bump for our success,\\" {initiator} '
               'says, raising their fist with a smile.\\"{initiator} nods '
               'approvingly at {target} and says, \\"I like your style. Bro '
               'bump?\\"\\"Way to go, {target}! How about a bro bump to '
               'commemorate this moment?\\" {initiator} asks, holding out '
               'their '
               'fist.mixer_social_BroHug_targeted_Friendly_alwaysOn\\"{target}, '
               'it\'s been a rough day, man. Come here,\\" {initiator} says, '
               'opening their arms for a bro hug.\\"Hey, {target}, I know '
               'things have been tough lately. Bring it in, buddy,\\" '
               '{initiator} says, offering a comforting bro hug.\\"{initiator} '
               'smiles at {target} and says, \\"You did great today, man. '
               'Let\'s hug it out.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=248,
          lineno=911,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'m really proud of you, man. Let\'s celebrate '
               'with a bro hug,\\" {initiator} suggests, extending their '
               'arms.\\"Come on, {target}, don\'t be shy. We\'re friends, '
               'right? Let\'s have a bro hug,\\" {initiator} says, '
               'encouragingly.\\"{initiator} walks up to {target} and says, '
               '\\"You know what this moment calls for? A solid bro '
               'hug.\\"\\"Hey, {target}, it\'s been a while since we\'ve seen '
               'each other! Let\'s have a proper bro hug,\\" {initiator} says, '
               'happily.\\"Nothing like a good old-fashioned bro hug to show '
               'our appreciation for each other, right {target}?\\" '
               '{initiator} says, grinning.\\"{initiator} pats {target} on the '
               'back and says, \\"You\'ve been a real friend, {target}. Let\'s '
               'seal it with a bro hug.\\"\\"Sometimes, words just aren\'t '
               'enough, {target}. Let\'s hug it out, man,\\" {initiator} says, '
               'opening their arms for a bro '
               'hug.mixer_social_DoAnImpression_targeted_funny_alwaysOn'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=249,
          lineno=922,
          tokens=218,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, check this out! I\'ve been working on this '
               'impression, and I think I\'ve finally nailed it,\\" '
               '{initiator} says, excitement in their eyes.\\"Hey {target}, '
               'you know who this is?\\" {initiator} asks, their voice and '
               'demeanor changing as they launch into their '
               'impression.\\"{target}, do you remember that famous scene from '
               'the movie? I can do an impression of the main character,\\" '
               '{initiator} says with a grin.\\"You\'ve got to see this, '
               "{target}. I've been practicing this impression lately, and I "
               'think it\'s pretty hilarious,\\" {initiator} says, '
               'chuckling.\\"Okay {target}, guess who I\'m impersonating,\\" '
               '{initiator} says, suddenly changing their voice and '
               'mannerisms.\\"Hey {target}, I have a little surprise for '
               'you,\\" {initiator} says, before launching into a spot-on '
               'impression.\\"Ready for a laugh, {target}? I\'ve been working '
               "on this new impression, and I can't wait to show it to "
               'you,\\" {initiator} says eagerly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=250,
          lineno=929,
          tokens=216,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I think I\'ve finally mastered this impression. '
               'Tell me what you think,\\" {initiator} says, as their face '
               'transforms into a different persona.\\"Witness my hidden '
               'talent, {target}. My impression of this character is sure to '
               'make you smile,\\" {initiator} says, beaming with '
               'confidence.\\"Prepare to be amazed, {target}. I\'ve been '
               'practicing this impression just for you,\\" {initiator} says, '
               'their excitement '
               'infectious.mixer_social_KnockKnockJoke_targeted_funny_alwaysOn_skills\\"{target}, '
               'I\'ve got a funny one for you. Knock knock,\\" {initiator} '
               'says with a grin.\\"Hey {target}, I heard this hilarious knock '
               'knock joke. Want to hear it?\\" {initiator} asks '
               'excitedly.\\"Knock knock, {target}! Are you ready for a good '
               'laugh?\\" {initiator} says, chuckling.\\"{target}, I just '
               "learned this great knock knock joke. You've got to hear "
               'it!\\" {initiator} says, barely containing their laughter.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=251,
          lineno=940,
          tokens=207,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Alright, {target}, I\'ve got a classic one for you. Knock '
               'knock,\\" {initiator} says with a playful smile.\\"Let\'s '
               'lighten the mood, {target}. Knock knock!\\" {initiator} says, '
               'eager to share the joke.\\"Knock knock! You\'re going to love '
               'this one, {target},\\" {initiator} says, anticipating a '
               'laugh.\\"I\'ve got a knock knock joke that\'s perfect for you, '
               '{target}. Ready?\\" {initiator} asks with a smirk.\\"Okay, '
               '{target}, I bet I can make you laugh with this one. Knock '
               'knock,\\" {initiator} says confidently.\\"Hey {target}, I\'ve '
               "got a knock knock joke that's too good not to share. Here it "
               'goes,\\" {initiator} says, preparing to deliver the '
               'punchline.mixer_social_DiscussInterests_friendly_STC\\"{target}, '
               "I've been wondering what you're passionate about. Care to "
               'share?\\" {initiator} asks with genuine curiosity.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=252,
          lineno=951,
          tokens=216,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, you know, we\'ve never really talked about '
               'our hobbies and interests. What do you enjoy doing in your '
               'free time?\\" {initiator} inquires.\\"So, {target}, I\'ve been '
               "meaning to ask you - what is it that you're truly interested "
               'in?\\" {initiator} starts the conversation.\\"{target}, we\'ve '
               "known each other for a while now, but I feel like there's "
               'still so much to learn about each other. What are your '
               'interests?\\" {initiator} questions, eager to deepen their '
               'connection.\\"I was thinking, {target}, that it\'s about time '
               'we talk about what makes us tick. What are you passionate '
               'about?\\" {initiator} proposes.\\"Hey {target}, I\'d love to '
               'know more about your interests and hobbies. Maybe we have '
               'something in common,\\" {initiator} suggests, '
               'smiling.\\"{target}, we\'ve talked about so many things, but '
               'not about our interests. I\'d love to hear about yours,\\" '
               '{initiator} says, hoping to learn something new.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=253,
          lineno=957,
          tokens=242,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"You know, {target}, I\'ve always been curious about what '
               'you\'re truly passionate about. Care to enlighten me?\\" '
               '{initiator} asks playfully.\\"{target}, I was just thinking '
               "about how our friendship has grown, and I realized we've never "
               'really discussed our interests. What do you like to do for '
               'fun?\\" {initiator} wonders.\\"Let\'s talk about something '
               'different today, {target}. Tell me about your interests and '
               'what makes you happy,\\" {initiator} says, looking forward to '
               'an engaging '
               'conversation.mixer_social_BoldPickUpLine_targeted_romance_emotionSpecific\\"{target}, '
               'if you were a vegetable, you\'d be a \'cute-cumber\',\\" '
               '{initiator} says with a cheeky grin.\\"Do you believe in love '
               'at first sight, {target}, or should I walk by again?\\" '
               '{initiator} asks playfully.\\"Are you a magician, {target}? '
               'Because every time I look at you, everyone else disappears,\\" '
               '{initiator} says with a flirtatious smile.\\"Is your name '
               "Google, {target}? Because you've got everything I've been "
               'searching for,\\" {initiator} says confidently.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=254,
          lineno=968,
          tokens=228,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Can I follow you home, {target}? Cause my parents always '
               'told me to follow my dreams,\\" {initiator} says, trying to '
               'impress.\\"Is your dad a boxer, {target}? Because, damn, '
               'you\'re a knockout!\\" {initiator} exclaims with a wink.\\"Do '
               'you have a map, {target}? I keep getting lost in your eyes,\\" '
               '{initiator} says, gazing deeply into {target}\'s eyes.\\"Are '
               'you a camera, {target}? Every time I look at you, I smile,\\" '
               '{initiator} says, flashing a charming grin.\\"Excuse me, '
               '{target}, but I think you owe me a drink. When I looked at '
               'you, I dropped mine,\\" {initiator} says, feigning '
               'embarrassment.\\"Can I take a picture of you, {target}? I want '
               'to show Santa exactly what I want for Christmas,\\" '
               '{initiator} says '
               'teasingly.mixer_social_ComplimentAppearance_targeted_romance_alwaysOn\\"{target}, '
               'you look absolutely stunning today. I just had to say it,\\" '
               '{initiator} says with a smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=255,
          lineno=979,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Wow, {target}, I can\'t help but notice how great you look. '
               'What\'s your secret?\\" {initiator} asks, genuinely '
               'impressed.\\"Your outfit is on point today, {target}. You have '
               'a fantastic sense of style,\\" {initiator} comments, admiring '
               '{target}\'s appearance.\\"Your hair looks amazing, {target}. '
               'It really suits you,\\" {initiator} says, unable to hide their '
               'admiration.\\"{target}, I must say, you have a radiant smile. '
               'It\'s truly captivating,\\" {initiator} compliments '
               'sincerely.\\"Is it just me or do you always manage to look so '
               'effortlessly good, {target}?\\" {initiator} asks, clearly '
               'impressed.\\"I can\'t help but notice how beautiful your eyes '
               'are, {target}. They\'re truly mesmerizing,\\" {initiator} '
               'says, looking into {target}\'s eyes.\\"{target}, you have a '
               'certain glow about you today. It\'s really attractive,\\" '
               "{initiator} comments, clearly appreciating {target}'s "
               'appearance.\\"Your style is so unique, {target}. It really '
               'sets you apart from everyone else,\\" {initiator} says, '
               'expressing their admiration.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=256,
          lineno=987,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve always thought you were good-looking, {target}, but '
               'today you\'ve taken it to a whole new level,\\" {initiator} '
               'says, clearly '
               'impressed.mixer_social_EnthuseAboutInterests_targeted_friendly_emotionSpecific\\"{target}, '
               'I am so excited to talk to you about my favorite hobbies and '
               'interests! I think you\'ll find them fascinating,\\" '
               '{initiator} exclaims, beaming with excitement.\\"Hey {target}, '
               "do you want to know what I'm really passionate about? I'd love "
               'to share my interests with you,\\" {initiator} says with a '
               'wide grin.\\"{target}, I\'ve always wanted to talk to you '
               'about the things I love doing. I think you would really enjoy '
               'them too,\\" {initiator} says, eager to share their '
               'interests.\\"I had such a great time doing my favorite '
               'activities this weekend, {target}. Let me tell you all about '
               'them,\\" {initiator} says enthusiastically.\\"You know what, '
               "{target}? I've realized we never really talked about my "
               'hobbies and interests. Let me share them with you,\\" '
               '{initiator} exclaims excitedly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=257,
          lineno=997,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I\'ve been wanting to share my favorite '
               "pastimes with you for a while now. I think you'll find them "
               'really interesting,\\" {initiator} says with a bright '
               'smile.\\"I can\'t wait to tell you about my favorite things, '
               "{target}. I have a feeling you'll love them as much as I "
               'do,\\" {initiator} says, looking thrilled.\\"{target}, I '
               "really want to share my passions with you. I think it'll help "
               'us understand each other better,\\" {initiator} says, looking '
               'forward to the conversation.\\"Did I ever tell you about my '
               "favorite hobbies, {target}? I'd love to discuss them with you "
               'and maybe even try them together,\\" {initiator} suggests, '
               'full of enthusiasm.\\"I\'ve been looking forward to discussing '
               "my interests with you, {target}. I think it's time I share "
               'what I\'m passionate about,\\" {initiator} says, eyes '
               'sparkling with '
               'excitement.mixer_social_JokeAboutFashion_targeted_funny_alwaysOn_Skills\\"{initiator} '
               'looks at {target} and chuckles, \\"Can you believe people '
               'actually used to wear those ridiculously oversized shoulder '
               'pads?\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=258,
          lineno=1007,
          tokens=206,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey, {target}, remember when wearing socks with sandals was '
               'considered a fashion statement?\\" {initiator} teases, '
               'laughing.\\"{initiator} smirks at {target} and says, \\"Did '
               "you ever try those low-rise jeans? I don't know how anyone "
               'thought they were comfortable!\\"\\"{target}, have you seen '
               'those pictures of people wearing neon-colored windbreakers in '
               'the \'90s? What were they thinking?\\" {initiator} asks, '
               'giggling.\\"Remember when people used to wear turtlenecks '
               'under everything, {target}? What a funny fashion choice,\\" '
               '{initiator} says, grinning.\\"Hey, {target}, do you recall the '
               'time when people would wear sweaters tied around their necks? '
               'It\'s hilarious to think about now,\\" {initiator} '
               'laughs.\\"{initiator} chuckles at {target} and says, \\"Did '
               "you ever own a pair of those massive platform shoes? I can't "
               'believe we thought those were stylish!\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=259,
          lineno=1013,
          tokens=238,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, can you imagine wearing a tracksuit to a fancy '
               'dinner? I bet people in the 2000s never thought that would be '
               'a thing!\\" {initiator} jokes, smirking.\\"Hey, {target}, what '
               "do you think about bringing back the mullet? It's about time "
               'for a revival, don\'t you think?\\" {initiator} says, '
               'laughing.\\"{initiator} snickers and asks {target}, \\"Do you '
               'remember when people used to wear skirts over pants? What an '
               'odd combination, '
               'right?\\"mixer_social_BragAboutHandiness_targeted_Friendly_alwaysOn_skills\\"{target}, '
               'did you know that I can fix pretty much anything around the '
               'house? I\'m pretty much a pro,\\" {initiator} says '
               'proudly.\\"You know, {target}, I\'ve been told I have quite '
               'the knack for handiwork. It\'s like I have a magic touch,\\" '
               '{initiator} boasts with a grin.\\"Hey, {target}, have I ever '
               'mentioned how skilled I am when it comes to handiwork? I could '
               'practically be a professional handyman,\\" {initiator} claims '
               'with confidence.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=260,
          lineno=1023,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I can\'t help but brag, {target}, but my handiness skills '
               "are pretty legendary. I've never met a repair I couldn't "
               'tackle,\\" {initiator} says with a smirk.\\"I\'ve always had a '
               "talent for fixing things, {target}. It's like I was born with "
               'a wrench in one hand and a hammer in the other,\\" {initiator} '
               'says, trying to impress {target}.\\"{target}, you should see '
               "me in action when it comes to repairs. I'm like a superhero of "
               'handiness,\\" {initiator} declares, puffing out their '
               'chest.\\"Whenever something needs fixing, {target}, I\'m the '
               'go-to person. I have a real gift,\\" {initiator} says, clearly '
               'proud of their skills.\\"Handiness is my middle name, '
               "{target}. I can fix things you wouldn't even think were "
               'repairable,\\" {initiator} brags with a wide smile.\\"I\'ve '
               'always been the handy one in my family, {target}. I can fix '
               'anything, from a leaky faucet to a broken door hinge,\\" '
               '{initiator} says, hoping to impress {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=261,
          lineno=1029,
          tokens=241,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Let me tell you, {target}, when it comes to handiness, I\'m '
               "a master. I've got the magic touch when it comes to "
               'repairs,\\" {initiator} proclaims, beaming with '
               'pride.mixer_social_EnthuseAboutOutdoors_targeted_Friendly_MiddleScore\\"{target}, '
               "have you ever spent time in the great outdoors? There's "
               'something so magical about it,\\" {initiator} says, eyes '
               'sparkling with enthusiasm.\\"Did I ever tell you about the '
               'time I went camping, {target}? It was such an amazing '
               'experience,\\" {initiator} begins, eager to share the '
               'story.\\"You know, {target}, I\'ve always found solace in '
               'nature. It\'s like a sanctuary away from the chaos of life,\\" '
               '{initiator} says with a sigh of contentment.\\"{target}, have '
               "you ever gone hiking or explored a dense forest? I'd love to "
               'do that someday,\\" {initiator} says, a dreamy look in their '
               'eyes.\\"I\'m thinking of planning a trip to the mountains, '
               "{target}. There's something about the crisp air and lush "
               'greenery that calls to me,\\" {initiator} shares, excitedly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=262,
          lineno=1039,
          tokens=214,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve always been fascinated by the beauty and '
               'mysteries of the great outdoors. What are your thoughts on '
               'it?\\" {initiator} asks, hoping to engage in a meaningful '
               'conversation.\\"Do you remember the last time we were out in '
               'nature, {target}? I can still feel the warmth of the sun and '
               'the gentle breeze on my skin,\\" {initiator} reminisces, a '
               'smile playing on their lips.\\"There\'s a certain sense of '
               "freedom that comes from being in the great outdoors, don't you "
               'think, {target}?\\" {initiator} says, looking for '
               'agreement.\\"Whenever I feel stressed or overwhelmed, '
               '{target}, I find solace in the thought of escaping to the '
               'great outdoors, where I can breathe and find peace,\\" '
               '{initiator} confides, seeking understanding.\\"Let\'s plan a '
               'trip together, {target}, something that encompasses the beauty '
               'of the great outdoors. I think it would be the perfect '
               'adventure for us,\\" {initiator} suggests, eyes shining with '
               'hope.mixer_social_Fight_targeted_mean_Ghost'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=263,
          lineno=1048,
          tokens=238,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I can feel your presence here, but I don\'t '
               'understand why you\'re haunting me,\\" {initiator} says, '
               'frustration creeping into their voice.\\"{target}, I know '
               "you're here, and I'm tired of your ghostly antics. Show "
               'yourself and let\'s talk about this,\\" {initiator} demands, '
               'clenching their fists.\\"I can\'t take this anymore, {target}! '
               "I know you're a ghost, but you can't just keep messing with my "
               'life!\\" {initiator} shouts, their anger reaching a boiling '
               'point.\\"Enough, {target}! I don\'t know what\'s keeping you '
               'here, but we need to resolve this issue now!\\" {initiator} '
               'exclaims, trying to confront the unseen spirit.\\"{target}, '
               "I've tried to ignore you, but now it's time for us to settle "
               'this. Your ghostly presence is not welcome here anymore!\\" '
               '{initiator} yells, feeling both fear and anger.\\"It\'s time '
               "for us to face each other, {target}. I won't let your ghostly "
               'presence control me any longer,\\" {initiator} asserts, '
               'gathering their courage.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=264,
          lineno=1060,
          tokens=220,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Stop hiding, {target}! I know you\'re a ghost, but I\'m not '
               'afraid to confront you,\\" {initiator} says defiantly, '
               'standing their ground.\\"Why are you doing this, {target}? '
               "You're a ghost, but that doesn't give you the right to torment "
               'me!\\" {initiator} exclaims, frustration evident in their '
               'voice.\\"Your ghostly games need to end now, {target}. I\'m '
               'done being afraid and letting you control my life,\\" '
               '{initiator} states firmly, ready to confront the '
               'spirit.\\"{target}, I won\'t let you haunt me any longer. Come '
               'out and face me, so we can resolve this once and for all,\\" '
               '{initiator} challenges, determined to stand up to the '
               'ghost.mixer_social_CalmDown_friendly_emotionSpecific\\"{target}, '
               'take a deep breath and try to relax. I\'m here for you,\\" '
               '{initiator} says soothingly.\\"Hey, {target}, let\'s just take '
               'a moment to breathe and clear our heads, okay?\\" {initiator} '
               'suggests gently.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=265,
          lineno=1073,
          tokens=241,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I know you\'re upset, but let\'s try to stay calm '
               'and talk this through,\\" {initiator} says, placing a '
               'reassuring hand on {target}\'s shoulder.\\"Everything is going '
               'to be alright, {target}. Just take a few deep breaths, and '
               'we\'ll figure this out together,\\" {initiator} '
               'reassures.\\"{target}, let\'s slow down and take a step back. '
               'We can handle this situation better if we\'re both calm,\\" '
               '{initiator} advises.\\"Hey, {target}, remember that breathing '
               "technique we learned? Let's try it together to help you calm "
               'down,\\" {initiator} says supportively.\\"Listen, {target}, I '
               'need you to focus on your breathing and try to calm down. '
               'We\'ll get through this together,\\" {initiator} '
               'encourages.\\"{target}, I know it\'s hard, but let\'s try to '
               'stay calm. We can find a solution if we keep our heads '
               'clear,\\" {initiator} says with a comforting smile.\\"Let\'s '
               'take a moment to regroup, {target}. A clear mind will help us '
               'handle this better,\\" {initiator} suggests, looking into '
               "{target}'s eyes."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=266,
          lineno=1080,
          tokens=225,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Deep breaths, {target}. Inhale, exhale. Remember, I\'m here '
               'for you, and we\'ll get through this,\\" {initiator} says '
               'softly.mixer_social_HoldHands_targeted_romance_middleScore\\"{target}, '
               "can I hold your hand? There's just something about the way our "
               'fingers intertwine that feels so right,\\" {initiator} says '
               'softly.\\"Your hands are so warm, {target}. I feel a '
               'connection every time we touch,\\" {initiator} says, gently '
               'taking {target}\'s hands in theirs.\\"{target}, your hands are '
               'like a safe haven for me. May I hold them for a little '
               'while?\\" {initiator} asks with a tender smile.\\"Every time I '
               "touch your hands, {target}, I feel like I've come home. Do you "
               'mind if I hold them?\\" {initiator} says, looking into '
               '{target}\'s eyes.\\"I love the way our hands fit together, '
               '{target}. It\'s like we were made for each other,\\" '
               "{initiator} says, slowly reaching for {target}'s hands."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=267,
          lineno=1090,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, can I hold your hands? There\'s something so '
               'comforting and familiar about the way they feel in mine,\\" '
               '{initiator} says, searching for a connection.\\"Your hands are '
               'so gentle, {target}. I can\'t help but want to hold them,\\" '
               "{initiator} says, taking {target}'s hands and looking deeply "
               'into their eyes.\\"May I hold your hands, {target}? The warmth '
               'and tenderness I feel when our fingers touch is '
               'indescribable,\\" {initiator} asks with a loving smile.\\"Can '
               "I hold your hands, {target}? There's something about the way "
               'they feel in mine that makes my heart skip a beat,\\" '
               '{initiator} says, full of affection.\\"Whenever I hold your '
               'hands, {target}, I feel like our souls are connected. I hope '
               'you feel the same way,\\" {initiator} says, reaching for '
               "{target}'s hands with love and "
               'care.mixer_social_GivePepTalk_targeted_friendly_emotionSpecific\\"{target}, '
               "I know you're feeling down, but I believe in you. You're "
               'stronger than you think,\\" {initiator} says with '
               'encouragement.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=268,
          lineno=1100,
          tokens=207,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, don\'t let this setback define you. You can '
               'overcome anything if you put your mind to it,\\" {initiator} '
               'reassures.\\"When life knocks you down, {target}, you\'ve got '
               'to get back up and keep going. I know you can do it,\\" '
               "{initiator} offers, trying to lift {target}'s "
               'spirits.\\"You\'ve got so much potential, {target}. Don\'t let '
               'insecurities hold you back. Believe in yourself,\\" '
               '{initiator} urges with sincerity.\\"{target}, I\'ve seen you '
               'overcome so many obstacles. This is just another challenge, '
               'and I know you can handle it,\\" {initiator} says '
               'confidently.\\"Sometimes, {target}, all it takes is a little '
               'faith in yourself. You\'ve got this. I believe in you,\\" '
               '{initiator} says, offering a supportive smile.\\"{target}, '
               "remember all the times you've succeeded against the odds? "
               'You\'ve got that same strength within you now,\\" {initiator} '
               'reminds, hoping to inspire.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=269,
          lineno=1106,
          tokens=204,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Take a deep breath, {target}, and trust yourself. You\'re '
               "capable of great things, and I'll be here to support you every "
               'step of the way,\\" {initiator} promises.\\"You\'re not alone, '
               "{target}. We're in this together, and I have no doubt that "
               'you\'ll come out on top,\\" {initiator} says, trying to boost '
               '{target}\'s confidence.\\"Don\'t let fear hold you back, '
               "{target}. You're stronger than you know, and you can achieve "
               'anything you set your mind to,\\" {initiator} encourages, '
               "looking into {target}'s "
               'eyes.mixer_social_Fight_targeted_mean\\"{target}, I can\'t '
               "believe you would do something like that! You've really "
               'crossed the line this time,\\" {initiator} says angrily, '
               'clenching their fists.\\"Enough is enough, {target}! I\'m '
               'tired of you always trying to control everything. We need to '
               'settle this,\\" {initiator} shouts, their patience wearing '
               'thin.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=270,
          lineno=1115,
          tokens=228,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, you\'ve been pushing my buttons for far too long. '
               "I can't take it anymore! Let's settle this once and for "
               'all,\\" {initiator} exclaims, their face red with anger.\\"I '
               "never thought it would come to this, {target}, but you've left "
               'me with no choice. We need to fight this out,\\" {initiator} '
               'says, frustration evident in their voice.\\"Your constant '
               'meddling in my life has finally pushed me over the edge, '
               '{target}. It\'s time we settle our differences,\\" {initiator} '
               'declares, their eyes narrowed in anger.\\"I tried to avoid '
               "this, {target}, but you just won't back off. We have to fight "
               'and sort this out,\\" {initiator} says, taking a defensive '
               'stance.\\"Sometimes talking just isn\'t enough, {target}. '
               'Let\'s resolve this the old-fashioned way,\\" {initiator} '
               'suggests, their voice filled with determination.\\"{target}, '
               "you've provoked me for the last time. I'm not going to let you "
               'walk all over me anymore. Let\'s do this,\\" {initiator} '
               'challenges, stepping forward.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=271,
          lineno=1121,
          tokens=227,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve put up with your nonsense for too long, {target}. '
               'This ends now,\\" {initiator} says, their breathing heavy with '
               'anger.\\"Your actions have finally pushed me to my breaking '
               'point, {target}. It\'s time to settle our feud,\\" {initiator} '
               'says, gritting their teeth and raising their '
               'fists.mixer_social_GossipAboutVideoGamePros_targeted_friendly_alwaysOn_skills\\"{target}, '
               "have you seen that new Twitch streamer that everyone's talking "
               'about?\\" {initiator} asks, clearly excited to share some '
               'gossip.\\"Hey, {target}, did you hear what happened on '
               '{streamer}\'s stream yesterday? Let me fill you in,\\" '
               '{initiator} says with a grin.\\"You know, {target}, I can\'t '
               'believe what some Twitch streamers get up to these days. Have '
               'you heard the latest?\\" {initiator} asks, eager to discuss '
               'the gossip.\\"I was watching this Twitch streamer last night, '
               "{target}, and you wouldn't believe what they said! Let's talk "
               'about it,\\" {initiator} suggests, itching to chat.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=272,
          lineno=1131,
          tokens=239,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Did you catch that drama between those two Twitch '
               'streamers, {target}? I need someone to discuss it with,\\" '
               '{initiator} says, wide-eyed.\\"Hey, {target}, have you seen '
               'the rumors about that popular Twitch streamer? Let me tell you '
               'all about it,\\" {initiator} says, excited to share the juicy '
               'details.\\"{target}, I was just reading about this Twitch '
               "streamer who got into some serious trouble. You've got to hear "
               'this,\\" {initiator} says, leaning in closer.\\"Have you been '
               'keeping up with the latest Twitch streamer gossip, {target}? '
               'There\'s so much to talk about!\\" {initiator} exclaims, ready '
               'to dive into the conversation.\\"I couldn\'t help but overhear '
               'some interesting news about a Twitch streamer earlier, '
               '{target}. Sit down, and let\'s chat,\\" {initiator} says, '
               'eager to discuss the story.\\"Can you believe what\'s been '
               "happening with those Twitch streamers, {target}? Let's grab a "
               'coffee and talk about it,\\" {initiator} suggests, unable to '
               'contain their '
               'excitement.mixer_social_EnhuseAboutNewAlbums_targeted_Friendly_alwaysOn'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=273,
          lineno=1141,
          tokens=222,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, have you heard about the new albums that just '
               'dropped? I\'m really excited to discuss them with you,\\" '
               '{initiator} says enthusiastically.\\"Hey {target}, there are a '
               "few new albums out now that I think you'd be interested in. "
               'Let\'s chat about them!\\" {initiator} suggests with a '
               'smile.\\"{initiator} excitedly approaches {target} and says, '
               '\\"I\'ve been listening to some newly released albums, and I '
               'can\'t wait to hear your thoughts on them!\\"\\"So, {target}, '
               "I've been checking out some fresh music releases, and I really "
               'want to know what you think of them,\\" {initiator} says, '
               'eager for a conversation.\\"Hey {target}, I was just listening '
               "to a couple of new albums and thought you'd be the perfect "
               'person to discuss them with. What do you say?\\" {initiator} '
               'asks.\\"{initiator} leans in and asks {target}, \\"Did you get '
               'a chance to listen to the latest albums that just came out? '
               'I\'d love to hear your opinions on them.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=274,
          lineno=1147,
          tokens=234,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I just came across some amazing new music '
               "releases, and I'm dying to know if you've heard them and what "
               'you think!\\" {initiator} says with excitement.\\"Have you '
               'been keeping up with the new albums that just hit the scene, '
               '{target}? I\'d love to get your take on them,\\" {initiator} '
               'inquires with genuine interest.\\"I can\'t help but think of '
               "you when I listen to these new albums, {target}. Let's talk "
               'about them and see if we share the same opinions,\\" '
               '{initiator} suggests.\\"Hey {target}, let\'s have a listening '
               'party and discuss the new albums that were just released. I '
               'think we\'ll have a lot to talk about,\\" {initiator} proposes '
               'with '
               'anticipation.mixer_social_DiscussWorldPeace_targeted_Friendly_alwaysOn\\"{target}, '
               'have you ever thought about what it would take to achieve '
               'world peace?\\" {initiator} asks, genuinely '
               'curious.\\"{initiator}, do you think it\'s even possible for '
               'us to reach a point where there\'s peace across the globe?\\" '
               '{target} wonders, as they begin a deep conversation.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=275,
          lineno=1157,
          tokens=228,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"World peace seems like a distant dream, {target}, but I '
               'believe it\'s worth striving for. What\'s your take on it?\\" '
               '{initiator} inquires, looking for insights.\\"Sometimes I '
               'imagine a world without war or conflict, {target}. Do you '
               'think humanity can one day achieve that?\\" {initiator} asks '
               'thoughtfully.\\"{initiator} and {target} sit down and begin '
               'discussing the concept of world peace, exploring various ideas '
               'and opinions on how to make it a reality.\\"\\"You know, '
               "{target}, I've always wondered if peace can truly exist in a "
               'world as diverse as ours. What do you think?\\" {initiator} '
               'starts the conversation, hoping for a meaningful '
               'exchange.\\"{target}, considering all the conflicts and '
               "struggles in the world, do you believe there's a way to reach "
               'a state of global harmony?\\" {initiator} asks, seeking '
               '{target}\'s perspective.\\"I\'ve been pondering the idea of '
               'world peace lately, {target}. Can you share your thoughts on '
               'the topic?\\" {initiator} requests, eager to hear a different '
               'viewpoint.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=276,
          lineno=1163,
          tokens=240,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} brings up the topic of world peace, asking '
               '{target} to share their thoughts on the possibility of '
               'achieving it and the challenges they might face.\\"\\"World '
               'peace is an ideal that many strive for, {target}. In your '
               'opinion, can it ever become a reality?\\" {initiator} asks, '
               'hoping to spark a thought-provoking '
               'conversation.mixer_social_EnthuseAboutNewShow_targeted_Friendly_MiddleScore\\"{target}, '
               "have you seen that new show everyone's been talking about? I "
               'just started watching it and it\'s amazing!\\" {initiator} '
               'says excitedly.\\"Hey, {target}, I just started watching this '
               "new show on TV and I think you'll love it! Want to know more "
               'about it?\\" {initiator} asks with enthusiasm.\\"{target}, I '
               "came across this new show last night and I can't stop thinking "
               'about it. Have you heard of it?\\" {initiator} inquires, eager '
               'to discuss.\\"I\'ve been hooked on this new TV show, {target}. '
               'Have you seen it yet? I\'d love to hear your thoughts,\\" '
               '{initiator} says, hoping for a conversation.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=277,
          lineno=1173,
          tokens=239,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I know you\'re into these kinds of shows, so I '
               "wanted to tell you about this new one I found. I think you'll "
               'really enjoy it!\\" {initiator} shares with a smile.\\"Hey, '
               "{target}, you're always up-to-date on TV shows. Have you "
               'checked out the new one everyone\'s talking about?\\" '
               '{initiator} asks curiously.\\"I just discovered this amazing '
               "new show, {target}, and I can't wait to discuss it with you. "
               'Have you seen it?\\" {initiator} says, looking for common '
               'ground.\\"{target}, I stumbled upon this new show and it '
               'reminded me of that one we used to watch together. Have you '
               'seen it yet?\\" {initiator} reminisces.\\"I know you have '
               'great taste in television, {target}, so I wanted to ask if '
               'you\'ve seen this new show I\'ve been enjoying lately,\\" '
               '{initiator} says, eager for {target}\'s opinion.\\"Last night, '
               'I started watching this incredible new show, {target}. I think '
               'it\'s right up your alley. Have you caught an episode yet?\\" '
               '{initiator} asks with anticipation.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=278,
          lineno=1181,
          tokens=213,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_AskToBeGirlfriend_targeted_romance_relationship\\"{target}, '
               "I've been thinking about this for a while, and I need to "
               'know... would you consider being my girlfriend?\\" {initiator} '
               'asks nervously.\\"Hey, {target}, I can\'t imagine my life '
               'without you. Would you do me the honor of being my '
               'girlfriend?\\" {initiator} says with a hopeful smile.\\"So, '
               "{target}, I've realized that you're the one who makes me "
               'happiest. What do you say about being my girlfriend?\\" '
               "{initiator} asks, trying to gauge {target}'s "
               'reaction.\\"{target}, our friendship means the world to me, '
               'but I think I want something more. Would you like to be my '
               'girlfriend?\\" {initiator} says, taking a deep breath.\\"I\'ve '
               "been falling for you for a while now, {target}, and I can't "
               'hold it in any longer. Will you be my girlfriend?\\" '
               "{initiator} asks, looking into {target}'s eyes."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=279,
          lineno=1188,
          tokens=231,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, you\'re such an amazing person, and I can\'t help '
               'but want to be with you. Would you be my girlfriend?\\" '
               '{initiator} says, hoping for a positive response.\\"I don\'t '
               "know how to say this, {target}, but I've developed strong "
               'feelings for you. Will you take a chance on me and be my '
               'girlfriend?\\" {initiator} asks hesitantly.\\"Life\'s too '
               "short to not take chances, {target}, so I'm taking one now. "
               'Would you consider being my girlfriend?\\" {initiator} says, '
               'holding {target}\'s hand.\\"I\'ve tried to deny it, {target}, '
               "but my heart is set on you. I can't help but wonder if you'd "
               'be my girlfriend,\\" {initiator} says, anxiously awaiting '
               '{target}\'s answer.\\"You make me laugh, you make me feel '
               "alive, and I can't imagine anyone else by my side, {target}. "
               'Would you be my girlfriend?\\" {initiator} asks with a sincere '
               'smile.mixer_social_EnthuseAboutGuitarSolos_targeted_Friendly_alwaysOn_skills'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=280,
          lineno=1197,
          tokens=203,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, have you ever heard that epic guitar solo in '
               '\'Stairway to Heaven\'? It\'s mind-blowing!\\" {initiator} '
               'exclaims excitedly.\\"Hey {target}, I just listened to this '
               "amazing guitar solo, and I couldn't wait to share it with you. "
               'You\'ve got to hear it!\\" {initiator} says, grinning from ear '
               'to ear.\\"{target}, you won\'t believe the guitar solo I just '
               "discovered! It's so incredibly powerful - I just had to tell "
               'you about it,\\" {initiator} says, eyes sparkling with '
               'enthusiasm.\\"I was just listening to some classic rock, '
               "{target}, and I realized we've never discussed our favorite "
               'guitar solos. What\'s yours?\\" {initiator} asks, eager for a '
               'conversation.\\"Have you ever noticed how guitar solos can '
               "completely change the mood of a song, {target}? Let's talk "
               'about some of our favorites,\\" {initiator} suggests, brimming '
               'with excitement.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=281,
          lineno=1202,
          tokens=232,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Remember that concert we went to, {target}? The guitarist '
               'played the most incredible solo! It still gives me chills just '
               'thinking about it,\\" {initiator} reminisces, eyes wide with '
               'amazement.\\"I know you\'re a big music fan, {target}, so I '
               'wanted to ask you: what do you think makes a truly '
               'unforgettable guitar solo?\\" {initiator} questions, their '
               'enthusiasm contagious.\\"{target}, I\'ve been on a guitar solo '
               "binge lately, and I'd love to hear your thoughts on some of "
               'the most legendary solos in music history. Care to join me?\\" '
               '{initiator} invites excitedly.\\"I was just practicing some '
               "guitar solos, {target}, and I can't help but marvel at the "
               "skill and emotion behind them. Let's chat about our favorites "
               'and maybe discover some new ones,\\" {initiator} proposes, '
               'brimming with excitement.\\"Hey {target}, I was wondering if '
               "you've ever tried playing any iconic guitar solos? They're so "
               'much fun to learn and discuss with fellow guitar enthusiasts '
               'like you,\\" {initiator} says, eager to connect over their '
               'shared passion.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=282,
          lineno=1209,
          tokens=223,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_AskOnDateEvent_targeted_romance_alwaysOn\\"{target}, '
               "I've been thinking about this for a while, and I would love to "
               'take you on a date. What do you say?\\" {initiator} asks, a '
               'hopeful smile on their face.\\"Hey {target}, I was wondering '
               "if you'd like to go out with me sometime? I think we could "
               'have a great time together,\\" {initiator} suggests, looking '
               'excited.\\"So, {target}, I\'ve been meaning to ask you this, '
               'but would you like to go on a date with me?\\" {initiator} '
               'inquires, trying to gauge {target}\'s reaction.\\"{target}, '
               "I've always enjoyed our time together, and I was wondering if "
               'you\'d be interested in going on a date?\\" {initiator} asks, '
               'a bit nervous but eager to hear the response.\\"Hey, {target}, '
               "I've been thinking... How about we make our next hangout a "
               'date? Just you and me?\\" {initiator} proposes, looking into '
               "{target}'s eyes."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=283,
          lineno=1216,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I can\'t help but feel a connection between us. '
               "Would you like to go on a date and see if there's something "
               'more?\\" {initiator} asks, hopeful for a positive '
               'response.\\"I have a confession to make, {target}. I really '
               "like you, and I would love it if you'd go on a date with "
               'me,\\" {initiator} says, a bit shy but sincere.\\"I know this '
               'might be unexpected, {target}, but I would be thrilled if you '
               'would go on a date with me. What do you think?\\" {initiator} '
               'asks, trying to hide their nervousness.\\"Hey {target}, I\'ve '
               "got a fun idea. How about we go on a date? I promise it'll be "
               'a great time,\\" {initiator} suggests with a grin.\\"{target}, '
               "I can't ignore these feelings anymore. I would like to take "
               'you on a date if you\'re up for it,\\" {initiator} says, '
               'revealing their true '
               'emotions.mixer_social_GoAway_targeted_mean_alwaysOn\\"{target}, '
               'I need some space right now. Can you please just go away?\\" '
               '{initiator} asks, looking frustrated.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=284,
          lineno=1226,
          tokens=231,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Look, {target}, I just can\'t deal with this right now. I '
               'need you to leave me alone,\\" {initiator} says, trying to '
               'hold back their emotions.\\"{target}, I\'m not in the mood for '
               'company. Would you mind giving me some time alone?\\" '
               '{initiator} requests, avoiding eye contact.\\"Can you just go '
               'away, {target}? I need to be by myself right now,\\" '
               '{initiator} says, clearly agitated.\\"{target}, I don\'t mean '
               'to be rude, but I really need some time alone. Can you please '
               'leave?\\" {initiator} asks, attempting to sound polite.\\"I '
               "can't handle this right now, {target}. I need you to go away "
               'and give me some space,\\" {initiator} says, their voice '
               'strained.\\"{target}, I\'m really not in a good place right '
               'now. Can you please just go away and let me be?\\" {initiator} '
               'asks, sounding defeated.\\"Please, {target}, just leave me '
               'alone for a while. I need some time to think,\\" {initiator} '
               'says, rubbing their forehead.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=285,
          lineno=1233,
          tokens=215,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'m not trying to be mean, but I really need to '
               'be alone. Can you just go away?\\" {initiator} asks, trying to '
               'sound firm.\\"Look, {target}, I just can\'t do this right now. '
               'I need you to go away and give me some time to myself,\\" '
               '{initiator} says, looking '
               'overwhelmed.mixer_social_DiscusssSportsStatistics_targeted_Friendly_Athlete_AlwaysOn_STC\\"{target}, '
               'did you know that the highest-scoring basketball game in '
               'history had a combined total of 370 points?\\" {initiator} '
               'asks with enthusiasm.\\"Hey {target}, I came across this '
               'interesting stat - a soccer player runs about 7 miles on '
               'average during a match. What do you think of that?\\" '
               "{initiator} inquires, looking for {target}'s "
               'opinion.\\"{target}, you wouldn\'t believe the record number '
               'of home runs hit in a single MLB season! Care to take a '
               'guess?\\" {initiator} asks, playfully challenging {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=286,
          lineno=1242,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Did you know, {target}, that the fastest recorded tennis '
               'serve is 163.7 mph? I wonder how that would feel if you were '
               'on the receiving end!\\" {initiator} says, grinning.\\"Hey '
               '{target}, remember when we were talking about football? I '
               "looked up the longest field goal ever made, and it's 64 yards! "
               'Can you imagine?\\" {initiator} shares, still in awe.\\"I was '
               'reading about the most successful Olympian of all time, '
               "{target}. It's Michael Phelps, with an incredible 28 medals! "
               'What do you think makes him so special?\\" {initiator} asks, '
               'genuinely curious.\\"Did you know, {target}, that the fastest '
               'goal in soccer history was scored in just 2.8 seconds after '
               'kickoff? How crazy is that?\\" {initiator} exclaims, eager to '
               'discuss the topic.\\"Hey {target}, I found out that the record '
               'for the most goals scored in an NHL season is 92! Wayne '
               "Gretzky set the record back in 1981-82. Isn't that "
               'amazing?\\" {initiator} says, wanting to share the excitement.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=287,
          lineno=1247,
          tokens=229,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, check this out - the highest-scoring NFL game had '
               'a combined total of 113 points. I would have loved to see that '
               'game, wouldn\'t you?\\" {initiator} asks, reminiscing about '
               'the historic event.\\"So {target}, you know I\'m a huge fan of '
               'basketball, right? I just learned that the most points scored '
               'by a single player in an NBA game is 100! Wilt Chamberlain did '
               'it back in 1962. What an unbelievable achievement,\\" '
               '{initiator} says, admiration in their '
               'voice.mixer_social_AskMoveIn_targeted_Friendly_alwaysOn\\"{target}, '
               "I've been thinking. Would you like to move in with me and take "
               'our relationship to the next level?\\" {initiator} asks, '
               'hopeful.\\"Hey, {target}, have you ever considered living '
               'together? It might make things easier for both of us,\\" '
               '{initiator} suggests casually.\\"{target}, I love spending '
               "time with you, and I think we're ready for this step. What do "
               'you say about moving in together?\\" {initiator} asks with a '
               'smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=288,
          lineno=1259,
          tokens=220,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"We\'ve been together for a while now, {target}, and I was '
               "wondering if you'd like to move in with me. What do you "
               'think?\\" {initiator} asks nervously.\\"I\'ve been doing some '
               'thinking, {target}, and I realized I want to share more of my '
               'life with you. Would you be interested in moving in with '
               'me?\\" {initiator} proposes.\\"Living apart just doesn\'t feel '
               'right anymore, {target}. Would you consider moving in '
               'together?\\" {initiator} asks sincerely.\\"You know, {target}, '
               'I think our relationship is strong enough to handle living '
               'together. What are your thoughts on it?\\" {initiator} '
               'inquires.\\"{target}, I feel like we\'re ready for the next '
               'step in our relationship. How would you feel about moving in '
               'together?\\" {initiator} asks with anticipation.\\"I can\'t '
               "imagine my life without you, {target}. I'd love for us to "
               'share a home together. What do you think?\\" {initiator} says, '
               "looking into {target}'s eyes."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=289,
          lineno=1271,
          tokens=224,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Moving in together is a big decision, {target}, but I think '
               'we\'re ready for it. Are you on board with the idea?\\" '
               '{initiator} asks, hoping for a positive response.# '
               '"mixer_social_JokeAboutPoliticians_group_Funny_MediumScore": '
               '{#         "\\"{target}, have you heard the one about the '
               'politician who actually told the truth?\\" {initiator} asks '
               'with a grin.",#         "\\"Hey {target}, why did the '
               'politician cross the road?\\" {initiator} says, chuckling in '
               'anticipation.",#         "\\"{target}, you\'ll love this one. '
               'What do you call a politician who keeps their promises?\\" '
               '{initiator} smirks mischievously.",#         "\\"Here\'s a '
               'good one, {target}. How many politicians does it take to '
               'change a lightbulb?\\" {initiator} asks, trying to suppress a '
               'laugh.",#         "\\"Hey {target}, what do you get when you '
               'mix a politician and a scientist?\\" {initiator} says, a '
               'twinkle in their eye.",'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=290,
          lineno=1281,
          tokens=241,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#         "\\"{target}, did you hear about the politician who '
               'accidentally told the truth during a speech?\\" {initiator} '
               'begins, a smile spreading across their face.",#         "\\"So '
               "{target}, what's the difference between a politician and a "
               'magician?\\" {initiator} asks, eager to share the '
               'punchline.",#         "\\"Ready for a laugh, {target}? What do '
               'you call a politician who can play the piano?\\" {initiator} '
               'grins, anticipating {target}\'s reaction.",#         "\\"Okay '
               "{target}, I've got a great one for you. Why did the politician "
               'go to the beach?\\" {initiator} asks, barely able to contain '
               'their laughter.",#         "\\"Hey {target}, want to hear a '
               "joke? What's the difference between a politician and a flying "
               'pig?\\" {initiator} smirks, waiting for {target}\'s '
               'response."mixer_social_AskToBeBoyfriend_targeted_romance_relationship\\"{target}, '
               "I've been thinking about this for a while, and I was wondering "
               'if you\'d consider being my boyfriend,\\" {initiator} says, '
               "trying to gauge {target}'s reaction."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=291,
          lineno=1291,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey, {target}, I really like you and was hoping if you\'d '
               'like to be my boyfriend?\\" {initiator} asks, a hint of '
               'nervousness in their voice.\\"So, {target}, I\'ve been '
               'thinking... would you be up for being my boyfriend?\\" '
               '{initiator} asks, uncertainty in their eyes.\\"{target}, ever '
               "since we met, I've felt a strong connection between us. Would "
               'you like to be my boyfriend?\\" {initiator} says, hoping for a '
               'positive response.\\"I don\'t want to make things weird, '
               "{target}, but I think we'd make a great couple. Would you be "
               'my boyfriend?\\" {initiator} proposes cautiously.\\"You know, '
               "{target}, I've been thinking about us and how well we get "
               'along. What do you think about being my boyfriend?\\" '
               '{initiator} asks, trying to appear nonchalant.\\"Hey, '
               '{target}, I really enjoy spending time with you, and I was '
               "wondering if you'd like to take things to the next level and "
               'be my boyfriend?\\" {initiator} inquires with a hopeful smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=292,
          lineno=1297,
          tokens=224,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I don\'t want to ruin our friendship, {target}, but I '
               'can\'t help but wonder if you\'d like to be my boyfriend,\\" '
               "{initiator} says, anxiously waiting for {target}'s "
               'answer.\\"{target}, we have so much fun together, and I think '
               'we\'d make a great pair. Would you like to be my boyfriend?\\" '
               '{initiator} suggests, holding their breath.\\"Listen, '
               "{target}, I've been feeling something more than friendship "
               'between us. Would you consider being my boyfriend?\\" '
               '{initiator} asks, their heart '
               'pounding.mixer_social_ConvinceToLeaveSpouse_targeted_romance_relationship\\"{target}, '
               "I know this is difficult to hear, but I can't help but feel "
               'that you deserve so much better than your spouse. You deserve '
               'someone like me,\\" {initiator} says, trying to sound '
               'convincing.\\"I\'ve been thinking about this for a long time, '
               "{target}, and I truly believe we're meant to be together. It's "
               'time you leave your spouse and start a new life with me,\\" '
               '{initiator} says with determination.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=293,
          lineno=1306,
          tokens=234,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Your spouse isn\'t right for you, {target}. I can see it, '
               "and I know you can too. I'm the one who can make you truly "
               'happy,\\" {initiator} pleads, hoping to change {target}\'s '
               'mind.\\"{target}, I know you\'re committed to your spouse, but '
               "I can't help but feel that we're a better match. Please, "
               'consider leaving them for me,\\" {initiator} says, their eyes '
               'filled with hope.\\"Life is too short to be unhappy, {target}. '
               "I promise you, if you leave your spouse for me, you'll never "
               'regret it,\\" {initiator} says confidently.\\"I\'m not trying '
               "to break up your marriage, {target}, but I can't deny my "
               'feelings for you. I think we could be great together. Give us '
               'a chance,\\" {initiator} implores, desperate for {target}\'s '
               'understanding.\\"{target}, I don\'t want to be the reason for '
               "your unhappiness, but I can't help but think that I could make "
               'you happier than your spouse ever could. Please, think about '
               'it,\\" {initiator} says earnestly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=294,
          lineno=1311,
          tokens=226,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I never thought I\'d be the one to say this, {target}, but '
               "I can't ignore my feelings any longer. I need you to know that "
               'I think we should be together, even if it means leaving your '
               'spouse,\\" {initiator} confesses, their voice wavering.\\"I '
               "know you're married, {target}, but I can't help but think that "
               "you're settling for less. Imagine a life with me, and I "
               'promise you won\'t look back,\\" {initiator} says, trying to '
               'paint a picture of a brighter future.\\"Leaving your spouse '
               "won't be easy, {target}, but I promise you it'll be worth it. "
               'We could have a life filled with love and happiness if you '
               'just take that leap of faith with me,\\" {initiator} says, '
               'their voice filled with '
               'passion.mixer_social_HipBump_targeted_friendly_emotionSpecific\\"{initiator} '
               'playfully bumps their hip into {target}, catching them off '
               'guard and eliciting a laugh.\\"\\"Without warning, {initiator} '
               'casually hip bumps {target}, sparking a friendly interaction '
               'between the two.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=295,
          lineno=1320,
          tokens=245,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} gives {target} a light hip bump, a sign of '
               'camaraderie as they share a moment together.\\"\\"With a '
               'mischievous grin, {initiator} sidles up to {target} and '
               'delivers a friendly hip bump, inviting a playful '
               'response.\\"\\"Feeling a burst of energy, {initiator} gently '
               'hip bumps {target}, hoping to brighten their day and initiate '
               'a lighthearted conversation.\\"\\"As {initiator} walks past '
               '{target}, they give a playful hip bump, signaling the '
               'beginning of some friendly banter.\\"\\"{initiator} surprises '
               '{target} with a sudden hip bump, trying to break the ice and '
               'start an amusing interaction.\\"\\"Looking for a fun way to '
               'engage {target}, {initiator} gently bumps hips with them, '
               'eliciting a surprised yet amused reaction.\\"\\"With a twinkle '
               'in their eye, {initiator} approaches {target} and playfully '
               'hip bumps them, hoping to create a lively '
               'exchange.\\"\\"{initiator} decides to hip bump {target} as a '
               'way to break the tension and initiate a more lighthearted '
               'conversation.\\"mixer_social_Jeer_targeted_mean_middleScore'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=296,
          lineno=1332,
          tokens=234,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, do you really think you\'re capable of doing '
               'that?\\" {initiator} sneers mockingly.\\"Is it hard being as '
               'clueless as you, {target}?\\" {initiator} taunts with a cruel '
               'grin.\\"Oh, look at {target}, trying so hard but still failing '
               'miserably,\\" {initiator} laughs derisively.\\"Did you '
               'honestly think that was a good idea, {target}? How '
               'pathetic,\\" {initiator} jeers, rolling their eyes.\\"Wow, '
               '{target}, you never cease to amaze me with your '
               'incompetence,\\" {initiator} snickers meanly.\\"Hey {target}, '
               'do you ever get tired of being such a disappointment?\\" '
               '{initiator} asks with a nasty smirk.\\"Sometimes I wonder how '
               'you even manage to get through the day, {target},\\" '
               '{initiator} says mockingly.\\"Nice try, {target}, but you\'ll '
               'never be good enough,\\" {initiator} sneers, enjoying their '
               'cruelty.\\"I can\'t believe you thought that would work, '
               '{target}. You really are hopeless,\\" {initiator} taunts, '
               'shaking their head in disbelief.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=297,
          lineno=1341,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Did anyone ever tell you how ridiculous you look when you '
               'try, {target}?\\" {initiator} asks with a mean '
               'laugh.mixer_social_Intimidate_targeted_mean_middleScore\\"{target}, '
               'do you really think you can stand up to me?\\" {initiator} '
               'says, smirking and crossing their arms.\\"{initiator} leans in '
               'closer to {target}, their eyes narrowing. \\"You should be '
               'careful who you mess with,\\" they warn.\\"I hope you\'re '
               'aware of what you\'re getting yourself into, {target},\\" '
               '{initiator} says, their voice cold and menacing.\\"{initiator} '
               'towers over {target}, staring them down. \\"You might want to '
               'reconsider your actions, buddy,\\" they suggest darkly.\\"You '
               'have no idea who you\'re dealing with, {target},\\" '
               '{initiator} says, their tone dripping with venom.\\"Do you '
               'really want to test me, {target}?\\" {initiator} asks, raising '
               'an eyebrow and cracking their knuckles.\\"Be careful, '
               '{target}. I have a way of making problems... disappear,\\" '
               '{initiator} says ominously.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=298,
          lineno=1353,
          tokens=228,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} leans in and whispers menacingly in {target}\'s '
               'ear, \\"You don\'t want to see me angry.\\"\\"{initiator} '
               'fixes {target} with a cold stare. \\"You should know better '
               'than to challenge me,\\" they say icily.\\"Keep pushing me, '
               '{target}, and you\'ll see what happens,\\" {initiator} warns, '
               'their voice low and '
               'dangerous.mixer_social_KissHands_targeted_romance_emotionSpecific\\"{initiator} '
               "leans in slowly and gently places a tender kiss on {target}'s "
               'hand, conveying their admiration.\\"\\"Without a word, '
               "{initiator} takes {target}'s hand and softly kisses it, "
               'locking their eyes together.\\"\\"Feeling a sudden rush of '
               "affection, {initiator} gently lifts {target}'s hand and "
               'presses a warm kiss upon it.\\"\\"In a moment of pure emotion, '
               "{initiator} tenderly kisses {target}'s hand, expressing their "
               'deep connection.\\"\\"{initiator} takes {target}\'s hand in '
               'theirs, their eyes meeting as they gently press their lips to '
               '{target}\'s hand.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=299,
          lineno=1365,
          tokens=225,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"With a gaze full of tenderness, {initiator} brings '
               "{target}'s hand to their lips and plants a gentle "
               'kiss.\\"\\"In a spontaneous gesture, {initiator} reaches for '
               "{target}'s hand and lovingly kisses it, causing {target} to "
               'blush.\\"\\"As {initiator} grasps {target}\'s hand, they '
               "gently place a kiss on it, their eyes never leaving {target}'s "
               'face.\\"\\"Moved by the moment, {initiator} softly takes '
               "{target}'s hand and plants a sweet kiss upon it, conveying "
               'their feelings.\\"\\"With a meaningful look, {initiator} '
               "delicately kisses {target}'s hand, displaying their deep "
               'affection and '
               'admiration.\\"mixer_social_InsultFace_targeted_mean_emotionSpecific\\"{target}, '
               'has anyone ever told you that your face looks like someone '
               'tried to solve a Rubik\'s Cube but gave up halfway?\\" '
               '{initiator} smirks.\\"Wow, {target}, it must be hard to look '
               'in the mirror every day with a face like that,\\" {initiator} '
               'says mockingly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=300,
          lineno=1376,
          tokens=216,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I don\'t know whether to laugh or cry at the '
               'sight of your face,\\" {initiator} says, barely able to '
               'contain their laughter.\\"I\'ve seen some interesting faces in '
               'my time, {target}, but yours is truly one for the books,\\" '
               '{initiator} teases.\\"Hey {target}, did you lose a fight with '
               'a makeup brush or is that just your face?\\" {initiator} asks '
               'sarcastically.\\"{target}, I didn\'t know \'before\' pictures '
               'could walk and talk,\\" {initiator} says with a chuckle.\\"Is '
               'your face a work in progress, {target}? Or is that the final '
               'result?\\" {initiator} questions, a mischievous grin on their '
               'face.\\"{target}, I\'m not sure if you\'re aware, but it looks '
               'like your face has been in a battle with itself,\\" '
               '{initiator} says, trying to hold back a grin.\\"Your face, '
               '{target}, must be the reason why some people believe in '
               'extraterrestrial life,\\" {initiator} jokes.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=301,
          lineno=1383,
          tokens=239,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve heard of unique beauty, {target}, but your face is '
               'really pushing the limits,\\" {initiator} says with a hint of '
               'amusement.mixer_social_Kiss_targeted_romance_middleScore\\"{initiator} '
               "leans in close, their eyes meeting {target}'s before softly "
               'pressing their lips together in a tender kiss.\\"\\"Without '
               "warning, {initiator} gently grabs {target}'s face and plants a "
               'passionate kiss on their lips, catching them by '
               'surprise.\\"\\"As the conversation between {initiator} and '
               '{target} fades, their faces inch closer, finally sharing a '
               'long-awaited kiss.\\"\\"{initiator} hesitates for a moment '
               'before closing the gap between them, placing a sweet, '
               'lingering kiss on {target}\'s lips.\\"\\"With a mixture of '
               "courage and desire, {initiator} takes {target}'s hand, leans "
               'in, and shares a breathtaking kiss.\\"\\"Unable to resist any '
               'longer, {initiator} pulls {target} close and captures their '
               'lips in a passionate embrace.\\"\\"During a moment of quiet '
               'intimacy, {initiator} slowly leans in and brushes their lips '
               'against {target}\'s, igniting a spark between them.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=302,
          lineno=1395,
          tokens=227,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"As they gaze into each other\'s eyes, {initiator} gently '
               "cups {target}'s face and presses their lips together in a "
               'tender, loving kiss.\\"\\"Feeling a surge of emotion, '
               '{initiator} leans in and kisses {target} with a passion that '
               'takes both of them by surprise.\\"\\"Captivated by the moment, '
               '{initiator} closes the distance between them and seals their '
               'connection with a sweet, heartfelt '
               'kiss.\\"mixer_social_Insult_Mean_STC\\"{target}, I\'ve always '
               'wondered how you manage to be so consistently clueless,\\" '
               '{initiator} says with a mocking tone.\\"Hey {target}, did you '
               'get dressed in the dark today? Because that outfit is just... '
               'wow,\\" {initiator} smirks, looking {target} up and '
               'down.\\"{initiator} rolls their eyes at {target} and says, '
               '\\"You really are a special kind of stupid, aren\'t '
               'you?\\"\\"Wow, {target}, your inability to understand even the '
               'simplest things never ceases to amaze me,\\" {initiator} says '
               'with a sarcastic laugh.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=303,
          lineno=1406,
          tokens=238,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Did it hurt when you fell from heaven, {target}? Because '
               'you must have landed on your head to be so dense,\\" '
               '{initiator} snickers.\\"{target}, I would insult your '
               'intelligence, but I\'m afraid you wouldn\'t understand,\\" '
               '{initiator} says with a condescending smile.\\"{initiator} '
               'shakes their head and says, \\"Honestly, {target}, every time '
               "you speak, it's like a fresh reminder of why I avoid talking "
               'to you.\\"\\"You know, {target}, it\'s really impressive how '
               'you can make everything you do look so incredibly '
               'difficult,\\" {initiator} teases.\\"{target}, if you were any '
               'less competent, you\'d be a houseplant,\\" {initiator} says, '
               'rolling their eyes.\\"Sometimes I wonder if you\'re actually '
               'trying to be this annoying, {target}, or if it just comes '
               'naturally to you,\\" {initiator} says with an exasperated '
               'sigh.mixer_social_ShareInsecurities_targeted_friendly_emotionSpecific\\"{target}, '
               "I've been feeling really insecure lately, and I was hoping I "
               'could talk to you about it,\\" {initiator} says with a shaky '
               'voice.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=304,
          lineno=1417,
          tokens=232,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I don\'t usually open up about this, but something tells me '
               'that I can trust you with my insecurities,\\" {initiator} '
               'admits, looking into {target}\'s eyes.\\"Can I share something '
               "personal with you, {target}? I've been struggling with my "
               'insecurities, and I think I need some support,\\" {initiator} '
               'says, hesitatingly.\\"{target}, I need your help. I\'ve been '
               "feeling really down about myself lately, and I don't know who "
               'else to turn to,\\" {initiator} confesses, their voice '
               'trembling.\\"I\'ve never been good at admitting my weaknesses, '
               "but I think it's time I tell you about my insecurities, "
               '{target},\\" {initiator} says, taking a deep '
               'breath.\\"There\'s something I\'ve been keeping inside, '
               "{target}, and I think it's time I share it with you. I've been "
               'feeling really insecure,\\" {initiator} says, looking '
               'anxious.\\"I don\'t know how to say this, {target}, but I\'ve '
               'been feeling so insecure lately. Can we talk about it?\\" '
               '{initiator} admits, looking vulnerable.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=305,
          lineno=1423,
          tokens=221,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve never told anyone this, {target}, but my insecurities '
               'have been getting the best of me. Will you listen?\\" '
               '{initiator} asks cautiously.\\"Sometimes I feel like I\'m not '
               'good enough, {target}, and I think I need to talk about my '
               'insecurities with someone I trust. Can that be you?\\" '
               '{initiator} says, preparing to share something '
               'personal.\\"{target}, I\'ve been struggling with my '
               "insecurities for a while now, and I think it's time I open up "
               'to you about it,\\" {initiator} says with a mixture of relief '
               'and '
               'apprehension.mixer_social_ReciteLovePoetry_targeted_romance_emotionSpecific\\"{target}, '
               'I found a poem today that made me think of you. May I share it '
               'with you?\\" {initiator} asks, holding a worn book in their '
               'hands.\\"With your beauty in mind, {target}, I was inspired to '
               'write a few verses of love poetry. Would you like to hear '
               'them?\\" {initiator} inquires, shyly looking at {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=306,
          lineno=1432,
          tokens=231,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Listen closely, {target}, for these words of love I\'ve '
               'penned are meant for you and only you,\\" {initiator} says as '
               'they recite lines of poetry from memory.\\"Can I share '
               'something with you, {target}? I stumbled upon a poem that '
               'captures my feelings for you better than I ever could,\\" '
               '{initiator} says, blushing slightly.\\"{target}, I wrote a '
               "poem about you, and I'd be honored if you'd allow me to recite "
               'it for you,\\" {initiator} says, filled with both excitement '
               'and anxiety.\\"I found a piece of poetry that speaks to my '
               'heart and reminds me of you, {target}. Would you care to '
               'listen?\\" {initiator} asks gently.\\"Last night, I was '
               'inspired to write some verses dedicated to you, {target}. I '
               'hope you\'ll find them as beautiful as I find you,\\" '
               '{initiator} says, holding a folded piece of paper.\\"Words '
               'alone cannot express my feelings for you, {target}, but I hope '
               'this poem I wrote comes close,\\" {initiator} says, taking a '
               'deep breath before reciting their heartfelt words.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=307,
          lineno=1438,
          tokens=225,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Tonight, under this starry sky, I want to share a special '
               'poem with you, {target}. I hope it makes you feel as cherished '
               'as you are to me,\\" {initiator} says, a hint of nervousness '
               'in their voice.\\"{target}, I came across a poem that I '
               'believe perfectly captures the essence of my love for you. May '
               'I share it?\\" {initiator} asks, eyes filled with hope and '
               'adoration.mixer_social_Serenade_targeted_romance_emotionSpecific\\"{target}, '
               "I've been working on this song just for you. I hope it "
               'captures how I truly feel about you,\\" {initiator} says with '
               'a shy smile before beginning to sing.\\"I\'ve never done this '
               'before, but I feel like serenading you, {target}, because you '
               'mean the world to me,\\" {initiator} says, taking a deep '
               'breath and starting to sing.\\"{target}, I\'ve written a song '
               'that I believe truly captures my feelings for you. I hope '
               'you\'ll let me serenade you,\\" {initiator} says nervously '
               'while holding a guitar.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=308,
          lineno=1447,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Close your eyes, {target}, and let me express my love for '
               'you in the best way I know how,\\" {initiator} says, before '
               'singing a heartfelt romantic song.\\"{target}, I\'ve been '
               'practicing this song, hoping it would touch your heart. '
               'Please, let me sing it for you,\\" {initiator} says as they '
               'start to serenade {target}.\\"I want to do something special '
               'for you, {target}, something that can show you my true '
               'feelings. Let me serenade you,\\" {initiator} says, looking '
               'into {target}\'s eyes.\\"I\'ve never been good with words, but '
               'I can express my feelings through music. {target}, let me '
               'serenade you,\\" {initiator} says, gathering their '
               'courage.\\"{target}, I want to show you my love in a different '
               'way. I hope you\'ll enjoy this serenade,\\" {initiator} says, '
               'taking a deep breath before singing.\\"Tonight, under this '
               'moonlit sky, I want to express my love for you in a unique '
               'way, {target}. Allow me to serenade you,\\" {initiator} says, '
               'their voice full of emotion.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=309,
          lineno=1453,
          tokens=222,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I can\'t keep my feelings to myself any longer, {target}. I '
               'need to share them with you, and I hope this serenade will do '
               'just that,\\" {initiator} says, before singing from the '
               'heart.mixer_social_ShareBartendingSecrets_targeted_Friendly_alwaysOn_skills\\"{target}, '
               "I've been working behind the bar for years, and I've picked up "
               'some secret tricks. Want to learn a few?\\" {initiator} asks '
               'with a sly grin.\\"Hey {target}, you ever wonder how I make '
               "those amazing cocktails? I think it's time I let you in on a "
               'few of my secrets,\\" {initiator} says, winking.\\"Alright, '
               "{target}, I've seen your interest in bartending. Let me share "
               'some of my closely guarded secrets with you,\\" {initiator} '
               'offers, looking excited.\\"I never thought I would teach '
               "anyone this, but I think you're ready, {target}. Let me show "
               'you some of the secrets I\'ve learned as a bartender,\\" '
               '{initiator} says, rolling up their sleeves.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=310,
          lineno=1462,
          tokens=214,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Okay {target}, it\'s time for me to pass on some of my '
               "bartending wisdom. Pay close attention; these are secrets I've "
               'never shared before,\\" {initiator} says, preparing to divulge '
               'their knowledge.\\"{target}, you\'ve earned my trust, and I '
               "think it's time I share some of my most prized bartending "
               'secrets with you. Are you ready?\\" {initiator} asks, raising '
               'an eyebrow.\\"There\'s more to bartending than meets the eye, '
               "{target}. Let me show you some secret techniques I've picked "
               'up along the way,\\" {initiator} says, motioning for {target} '
               'to come closer.\\"I see potential in you, {target}. I\'m going '
               'to share some of my secret bartending skills with you, so pay '
               'attention,\\" {initiator} says, looking serious.\\"Ever '
               'wondered what sets my drinks apart from the rest, {target}? '
               "I'll let you in on my little secrets, but you have to promise "
               'not to tell,\\" {initiator} says, conspiratorially.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=311,
          lineno=1467,
          tokens=221,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Alright, {target}, I\'ve decided it\'s time to teach you '
               'some of the hidden tricks of the trade. Get ready to become a '
               'master bartender,\\" {initiator} says, a gleam in their '
               'eye.mixer_social_OfferRose_targeted_romance_emotionSpeficic\\"{target}, '
               "I couldn't help but think of you when I saw this rose. Its "
               'beauty pales in comparison to yours,\\" {initiator} says, '
               'offering the rose with a gentle smile.\\"Here\'s a small token '
               'of my affection, {target}. I hope this rose brightens your day '
               'as much as you brighten mine,\\" {initiator} says with a warm '
               'expression.\\"Every time I see a rose, I think of you, '
               "{target}. I hope you'll accept this as a symbol of my "
               'feelings,\\" {initiator} says, holding out the rose with a '
               'hopeful gaze.\\"{target}, I\'ve been wanting to express my '
               'feelings for you, and I think this rose says it all. Will you '
               'accept it?\\" {initiator} asks, presenting the rose tenderly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=312,
          lineno=1476,
          tokens=221,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"As we\'ve grown closer, I\'ve realized how much you mean to '
               'me, {target}. This rose is just a small way to show you my '
               'feelings,\\" {initiator} says, extending the rose with a '
               'loving smile.\\"I know it\'s a little old-fashioned, but I '
               "wanted to give you this rose, {target}. It's a symbol of the "
               'love that\'s blooming between us,\\" {initiator} says with a '
               'bashful grin.\\"Words often fail me when I try to express my '
               'feelings, {target}. So, let this rose speak for me instead,\\" '
               '{initiator} says, offering the rose with a heartfelt '
               'expression.\\"{target}, you\'ve brought so much joy into my '
               'life. I can only hope this rose brings a fraction of that '
               'happiness to you,\\" {initiator} says, presenting the rose '
               'with a sincere smile.\\"I\'ve been searching for a way to show '
               'you how much you mean to me, {target}. I hope this rose is the '
               'perfect expression of my love,\\" {initiator} says, holding '
               'the rose out with a gentle touch.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=313,
          lineno=1481,
          tokens=215,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Roses have always been a symbol of love, and I can\'t think '
               'of a better way to express my feelings for you, {target}. Will '
               'you accept this rose and my heart?\\" {initiator} asks, gazing '
               "into {target}'s "
               'eyes.mixer_social_Romance_HighScore_Loyal_ExpressDevotion\\"{target}, '
               "I don't know how else to say this, but I've fallen in love "
               'with you,\\" {initiator} says, their voice filled with '
               'emotion.\\"I can\'t hide it any longer, {target}. My heart '
               'belongs to you, and I can\'t imagine my life without you,\\" '
               '{initiator} confesses, their eyes shining with '
               'sincerity.\\"{target}, I\'ve tried to deny it, but the truth '
               'is, I\'m head over heels in love with you,\\" {initiator} '
               'says, looking into {target}\'s eyes with hope.\\"I\'ve never '
               'felt this way about anyone, {target}. I love you more than '
               'words can describe,\\" {initiator} admits, their heart '
               'pounding.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=314,
          lineno=1490,
          tokens=242,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Every time I see you, {target}, my heart skips a beat. I '
               'can\'t help but be utterly and completely devoted to you,\\" '
               '{initiator} says, a vulnerable look in their eyes.\\"I\'ve '
               'been trying to find the courage to tell you this, {target}, '
               'but I\'m in love with you. Completely and irrevocably,\\" '
               '{initiator} says, reaching for {target}\'s hand.\\"My heart '
               "belongs to you, {target}, and I can't bear to keep it a secret "
               'any longer. I love you,\\" {initiator} declares, their voice '
               'filled with passion.\\"There\'s no point in pretending '
               'anymore, {target}. I am deeply and truly in love with you,\\" '
               '{initiator} says, their eyes pleading for '
               'understanding.\\"I\'ve never been more certain about anything '
               'in my life, {target}. I am devoted to you, heart and soul,\\" '
               '{initiator} confesses, their voice barely above a whisper.\\"I '
               "don't know when it happened, {target}, but somewhere along the "
               "way, I fell in love with you. I can't imagine my life without "
               'your presence,\\" {initiator} says, their vulnerability '
               'shining through.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=315,
          lineno=1498,
          tokens=249,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_KissCheek_targeted_romance_alwaysOn\\"{initiator} '
               'leans in closer to {target}, their eyes meeting for a brief '
               "moment before gently pressing their lips to {target}'s "
               'cheek.\\"\\"Without a word, {initiator} reaches up and '
               "tenderly places a soft kiss on {target}'s cheek, causing a "
               'blush to spread across their face.\\"\\"Feeling a sudden surge '
               "of affection, {initiator} gently cups {target}'s face and "
               'plants a sweet kiss on their cheek.\\"\\"{initiator} smiles '
               'warmly at {target} before suddenly leaning in and placing a '
               'light kiss on their cheek, catching them off guard.\\"\\"With '
               'a playful grin, {initiator} leans in and brushes their lips '
               "against {target}'s cheek, leaving a lingering "
               'sensation.\\"\\"{initiator} takes {target}\'s hand, looks into '
               'their eyes, and then gently kisses their cheek, making '
               '{target}\'s heart race.\\"\\"Caught up in the moment, '
               '{initiator} impulsively leans forward and leaves a light, '
               'affectionate kiss on {target}\'s cheek.\\"\\"{initiator} '
               'suddenly leans in and surprises {target} with a quick peck on '
               'the cheek.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=316,
          lineno=1510,
          tokens=235,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_ShareConspiracyTheory_targeted_mischief_alwaysOn\\"{target}, '
               'have you ever heard of this conspiracy theory? I came across '
               'it recently, and I just can\'t stop thinking about it,\\" '
               '{initiator} says, excitedly.\\"{target}, I know this might '
               'sound crazy, but I stumbled upon a conspiracy theory that '
               'actually makes a lot of sense. Can I share it with you?\\" '
               '{initiator} asks, looking eager.\\"Okay, {target}, you might '
               "think I'm going off the deep end here, but I've got a "
               "conspiracy theory that's too intriguing not to share. Are you "
               'ready for it?\\" {initiator} grins, leaning in closer.\\"I '
               "never thought I'd be one to buy into conspiracy theories, "
               "{target}, but I found one that's strangely compelling. Can I "
               'get your thoughts on it?\\" {initiator} asks nervously.\\"Hey, '
               "{target}, I know you're into some wild theories, so I thought "
               'I\'d run this conspiracy theory by you. What do you think?\\" '
               "{initiator} says, trying to gauge {target}'s interest."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=317,
          lineno=1517,
          tokens=202,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"So, {target}, I came across this bizarre conspiracy theory, '
               "and I can't tell if it's just nonsense or if there's some "
               'truth to it. Can I share it with you?\\" {initiator} asks, '
               'looking for validation.\\"Alright, {target}, I know you\'ll '
               "appreciate this one. I've found a conspiracy theory that's "
               'just too wild not to share. Are you ready?\\" {initiator} '
               'says, barely containing their excitement.\\"Listen, {target}, '
               "I found this conspiracy theory that's completely out of left "
               "field, but I can't help but think there might be something to "
               'it. Can I tell you about it?\\" {initiator} inquires, seeking '
               'an open-minded listener.\\"You know, {target}, I\'ve never '
               "been one for conspiracy theories, but there's one that's been "
               'nagging at me. Mind if I share it with you and get your take '
               'on it?\\" {initiator} asks, hoping for a receptive ear.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=318,
          lineno=1521,
          tokens=231,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I need your critical thinking skills, {target}. I\'ve been '
               "reading about this conspiracy theory, and I can't decide if "
               'it\'s absurd or plausible. Can I run it by you?\\" {initiator} '
               "says, valuing {target}'s "
               'opinion.mixer_social_InsultCostume_targeted_mean_alwaysOn_situation_Day1DLC\\"{target}, '
               "I don't mean to be rude, but that costume looks like something "
               'a kindergartner made,\\" {initiator} says, trying to suppress '
               'a laugh.\\"Wow, {target}, did you put that costume together in '
               'the dark?\\" {initiator} asks sarcastically.\\"Is that '
               "supposed to be a costume, {target}? I've seen more effort put "
               'into a last-minute Halloween outfit,\\" {initiator} '
               'scoffs.\\"{target}, who told you that costume was a good idea? '
               'They must have a twisted sense of humor,\\" {initiator} '
               'comments with a smirk.\\"I didn\'t know we were going for '
               "'worst costume' award, {target}. You're definitely in the "
               'running,\\" {initiator} says with a snicker.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=319,
          lineno=1531,
          tokens=220,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Are you seriously wearing that, {target}? I thought you had '
               'better taste in costumes,\\" {initiator} says, rolling their '
               'eyes.\\"Hey, {target}, your costume might just win the '
               '\'ugliest outfit\' contest if there was one,\\" {initiator} '
               'jokes, laughing at their own remark.\\"{target}, I think you '
               "should demand a refund for that costume. It's not doing you "
               'any favors,\\" {initiator} says with a grin.\\"Did you lose a '
               "bet or something, {target}? That costume is just... Wow, I'm "
               'speechless,\\" {initiator} says, shaking their head in '
               'disbelief.\\"I hope you didn\'t spend too much time on that '
               'costume, {target}. It looks like a DIY disaster,\\" '
               '{initiator} says, trying to hold back their '
               'laughter.mixer_social_JokeAboutPenguins_targeted_Friendly_alwaysOn_situation_Day1DLC\\"{target}, '
               'did you hear about the penguin who wanted to be friends? He '
               'just needed someone to break the ice!\\" {initiator} chuckles.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=320,
          lineno=1541,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} asks {target}, \\"Why don\'t you ever see '
               'penguins in the UK? Because they\'re afraid of Wales!\\"\\"Hey '
               '{target}, what do penguins wear on their heads? Ice caps!\\" '
               '{initiator} laughs, trying to lighten the mood.\\"{initiator} '
               'grins at {target} and asks, \\"Why don\'t penguins like '
               'talking to strangers at parties? They find it hard to break '
               'the ice!\\"\\"{initiator} smirks at {target} and says, \\"Do '
               "you know what a penguin's favorite relative is? Aunt "
               'Arctica!\\"\\"Hey {target}, why are penguins such good race '
               'car drivers? Because they\'re always in the pole position!\\" '
               '{initiator} jokes, hoping to make {target} '
               'laugh.\\"{initiator} asks {target} with a grin, \\"What\'s a '
               'penguin\'s favorite movie? Frozen!\\"\\"Did you hear about the '
               'penguin who went to the beach, {target}? He wore a '
               'beak-ini!\\" {initiator} giggles at their own joke.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=321,
          lineno=1548,
          tokens=205,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, do you know what a penguin\'s favorite snack '
               'is? Ice Krispies!\\" {initiator} shares, hoping to bring a '
               'smile to {target}\'s face.\\"{initiator} looks at {target} and '
               'says, \\"What do you call a penguin in the desert? Lost!\\" '
               'hoping to get a '
               'laugh.mixer_social_DiscussTheBestViolinist_targeted_Friendly_alwaysOn_skills\\"{target}, '
               'have you ever wondered who the best violinist in the world '
               'might be?\\" {initiator} asks, striking up a conversation '
               'about music.\\"I was listening to some violin music earlier, '
               '{target}, and it got me thinking - who do you believe is the '
               'most talented violinist out there?\\" {initiator} inquires '
               'with curiosity.\\"Hey {target}, I\'ve been debating with a '
               "friend about the best violinist of all time. What's your take "
               'on that?\\" {initiator} asks, seeking {target}\'s opinion.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=322,
          lineno=1557,
          tokens=245,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve always admired your taste in music. In your '
               'opinion, who is the greatest violinist ever?\\" {initiator} '
               'asks, genuinely interested in {target}\'s perspective.\\"I '
               'came across a fascinating article about the greatest '
               'violinists, {target}. It made me wonder, who do you think '
               'deserves that title?\\" {initiator} questions, sparking a '
               'discussion.\\"Did you know, {target}, that there\'s a lot of '
               "debate about who the best violinist is? I'm curious, who's "
               'your personal favorite?\\" {initiator} asks, eager to know '
               '{target}\'s preference.\\"{target}, I\'ve been exploring '
               "different violinists lately, and I can't decide who is the "
               'best. Do you have any recommendations?\\" {initiator} asks, '
               'hoping for some guidance.\\"You know, {target}, there are so '
               'many amazing violinists out there. If you had to choose one as '
               'the best, who would it be?\\" {initiator} wonders, encouraging '
               'a friendly debate.\\"Have you ever seen a live violin '
               "performance, {target}? I'd love to know who you think is the "
               'most impressive violinist,\\" {initiator} asks '
               'enthusiastically.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=323,
          lineno=1563,
          tokens=213,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve been trying to expand my music collection '
               'with some incredible violinists. Who do you consider the best '
               'in the field?\\" {initiator} questions, eager to discover new '
               'talent.mixer_social_ShareBurden_targeted_Friendly_alwaysOn_trait\\"{target}, '
               "I've been struggling with something my whole life, and I think "
               'it\'s time I share it with you,\\" {initiator} says, weariness '
               'in their eyes.\\"I\'ve been carrying this burden for so long, '
               'and I need someone to understand. Can you lend me a '
               'sympathetic ear, {target}?\\" {initiator} asks '
               'hesitantly.\\"{target}, there\'s something that\'s been '
               "weighing me down for years, and I just can't keep it to myself "
               'anymore. I need your support,\\" {initiator} says, looking '
               'vulnerable.\\"I\'ve never told anyone about this, {target}, '
               "but I trust you. I need to share the load that's been haunting "
               'me my entire life,\\" {initiator} says, taking a shaky breath.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=324,
          lineno=1572,
          tokens=231,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve been hiding this pain for as long as I can '
               'remember, and I think it\'s time I open up to you about it,\\" '
               '{initiator} says, voice trembling with emotion.\\"There\'s '
               "something I've been dealing with my whole life, {target}, and "
               'I think you\'re the only one who can truly understand,\\" '
               "{initiator} says, searching {target}'s eyes for "
               'reassurance.\\"I need to get this off my chest, {target}, and '
               "I hope you can help me. I've been struggling with this burden "
               'for as long as I can remember,\\" {initiator} says, eyes '
               'welling up with tears.\\"{target}, I\'ve been hiding a '
               "life-long struggle, and I think it's time to share it with "
               'you. I trust your wisdom and empathy,\\" {initiator} says, '
               'seeking solace in {target}\'s presence.\\"I never thought I\'d '
               "open up about this, {target}, but I can't keep pretending it "
               "doesn't affect me. I need to tell you about the burden I've "
               'carried for years,\\" {initiator} says, voice barely audible.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=325,
          lineno=1577,
          tokens=238,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I feel like I\'ve known you long enough to share '
               'something deeply personal with you. I hope you can help me '
               'carry the weight of this burden,\\" {initiator} says, looking '
               "into {target}'s eyes with "
               'hope.mixer_social_SuaveKiss_targeted_romance_emotionSpecific\\"{initiator} '
               "leans in and gently presses their lips against {target}'s, "
               'creating a moment of passion and tenderness.\\"\\"With a '
               "charming smile, {initiator} takes {target}'s hand, pulls them "
               'closer, and plants a suave kiss on their '
               'lips.\\"\\"{initiator} looks deep into {target}\'s eyes, '
               'brushing their hair back before delivering a smooth, '
               'intoxicating kiss.\\"\\"Capturing the perfect moment, '
               '{initiator} leans in and sweeps {target} off their feet with a '
               'suave, unforgettable kiss.\\"\\"{initiator} cups {target}\'s '
               'face, their fingers lightly tracing the outline of their jaw '
               'before sealing the moment with a stylish kiss.\\"\\"Under the '
               'moonlit sky, {initiator} pulls {target} close and shares a '
               'suave, dreamlike kiss, taking their breath away.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=326,
          lineno=1588,
          tokens=231,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"With a mischievous glint in their eye, {initiator} places a '
               "finger under {target}'s chin, lifting their gaze before "
               'delivering a charming, suave kiss.\\"\\"In a bold move, '
               "{initiator} grabs {target}'s waist, pulling them closer and "
               'surprising them with a debonair, sensual '
               'kiss.\\"\\"{initiator} gently touches {target}\'s cheek, '
               'letting their eyes lock for a moment before leaning in for a '
               'smooth, enchanting kiss.\\"\\"As their eyes meet, {initiator} '
               "wraps an arm around {target}'s waist and pulls them in for a "
               'suave, heart-stopping '
               'kiss.\\"mixer_social_RileUp_targeted_mean_alwaysOn\\"{target}, '
               "I've always wondered how someone like you can be so "
               'clueless,\\" {initiator} says, smirking '
               'maliciously.\\"{target}, has anyone ever told you how '
               'infuriatingly slow you are?\\" {initiator} asks with a sly '
               'grin.\\"It\'s amazing how you manage to get through life with '
               'so little common sense, {target},\\" {initiator} snickers.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=327,
          lineno=1599,
          tokens=227,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, did you have to work hard to become this '
               'annoying, or does it just come naturally?\\" {initiator} '
               'teases cruelly.\\"{target}, if there was a contest for being '
               'the most irritating person, I\'m pretty sure you\'d win,\\" '
               '{initiator} scoffs.\\"I wonder how you manage to make even the '
               'simplest tasks look so difficult, {target},\\" {initiator} '
               'says with a mocking grin.\\"Whenever I need a good laugh, I '
               'just think about how you bumble through life, {target},\\" '
               '{initiator} chuckles rudely.\\"{target}, I\'ve met rocks with '
               'more personality than you. How do you do it?\\" {initiator} '
               'taunts.\\"Is it tiring being so incompetent, {target}? Or have '
               'you gotten used to it by now?\\" {initiator} asks, '
               'sneering.\\"I\'m not sure whether to pity you or be impressed '
               'by your ability to fail so consistently, {target},\\" '
               '{initiator} says, laughing '
               'meanly.mixer_social_WhisperSeductively_targeted_romance_middleScore'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=328,
          lineno=1610,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, can I tell you a secret?\\" {initiator} whispers '
               'seductively, a playful glint in their eye.\\"Lean in closer, '
               '{target}, I have something enticing to share,\\" {initiator} '
               'murmurs, their breath warm on {target}\'s ear.\\"{target}, I '
               "can't resist the urge to whisper something alluring in your "
               'ear,\\" {initiator} says, their voice soft and sultry.\\"I\'ve '
               'been thinking about something quite... sinful, {target}. Would '
               'you like to know what it is?\\" {initiator} teases, their lips '
               'brushing against {target}\'s earlobe.\\"Let me share a '
               'deliciously tempting secret with you, {target},\\" {initiator} '
               'purrs, their voice low and seductive.\\"There\'s a thought '
               "that's been driving me wild, {target}. Are you curious to know "
               'what it is?\\" {initiator} whispers, their voice dripping with '
               'desire.\\"You know, {target}, there\'s something I\'ve been '
               'fantasizing about. Can I share it with you?\\" {initiator} '
               'asks, their voice laced with seduction.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=329,
          lineno=1617,
          tokens=213,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I can\'t help but let my mind wander to some '
               'very... enticing places. Would you like a glimpse?\\" '
               '{initiator} whispers, a devilish grin on their face.\\"I have '
               'a confession to make, {target}. My thoughts have been a bit... '
               'naughty lately,\\" {initiator} admits, their voice sultry and '
               'inviting.\\"Come closer, {target}, and let me share a secret '
               'that\'s both thrilling and enticing,\\" {initiator} murmurs, '
               'their voice filled with '
               'allure.mixer_social_YellAT_targeted_mean\\"{target}, you\'re '
               'absolutely infuriating! Can\'t you do anything right?\\" '
               '{initiator} yells, anger in their voice.\\"Are you really this '
               "incompetent, {target}? I can't believe I have to put up with "
               'your stupidity!\\" {initiator} shouts, losing their '
               'patience.\\"{target}, I\'ve had enough of your nonsense! Get '
               'your act together or just get out of my sight!\\" {initiator} '
               'exclaims, frustration evident in their tone.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=330,
          lineno=1627,
          tokens=212,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I can\'t stand you anymore, {target}! Your constant '
               'mistakes are driving me insane!\\" {initiator} yells, unable '
               'to control their anger.\\"{target}, you\'re so careless! How '
               'can someone be as clueless as you?\\" {initiator} shouts, '
               'feeling overwhelmed by their frustration.\\"Sometimes I wonder '
               "if you're really this dumb, {target}, or if you're just "
               'pretending to be!\\" {initiator} yells, feeling '
               'exasperated.\\"{target}, I don\'t know how much more of your '
               'incompetence I can take! You\'re pushing me to my limits!\\" '
               '{initiator} shouts, their voice filled with irritation.\\"Can '
               "you just think for once, {target}? I'm tired of dealing with "
               'the mess you constantly create!\\" {initiator} yells, feeling '
               'fed up.\\"{target}, you never cease to amaze me with your '
               'foolishness! How hard is it for you to understand simple '
               'instructions?\\" {initiator} shouts, their voice laced with '
               'annoyance.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=331,
          lineno=1633,
          tokens=215,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'m at my wit\'s end, {target}! I can\'t take your '
               'stupidity any longer!\\" {initiator} yells, their anger '
               'finally boiling '
               'over.mixer_social_MakeFunOfNoobs_targeted_funny_alwaysOn_skills\\"{target}, '
               "have you seen these new players trying to learn the game? It's "
               'hilarious,\\" {initiator} laughs, watching their '
               'screens.\\"Hey {target}, check this out. This noob is '
               'struggling to even find the start button!\\" {initiator} '
               'jokes, pointing at the screen.\\"{target}, I swear, watching '
               'these newbies try to navigate the game is like watching a baby '
               'trying to walk,\\" {initiator} chuckles.\\"You know what\'s '
               'funny, {target}? The fact that these noobs think they can beat '
               'us in the game. Good luck with that!\\" {initiator} '
               'smirks.\\"I can\'t stop laughing, {target}. These new players '
               'are so lost. They\'re like deer caught in headlights,\\" '
               '{initiator} says with a grin.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=332,
          lineno=1643,
          tokens=222,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Remember when we were noobs like them, {target}? I bet we '
               'weren\'t this bad though!\\" {initiator} teases.\\"{target}, '
               'do you think we should help these new players or just sit back '
               'and enjoy the show?\\" {initiator} asks, laughing at their '
               'struggles.\\"Man, {target}, it\'s so entertaining to watch '
               "these rookies fumble around. It's like they've never played a "
               'video game before,\\" {initiator} comments.\\"Sometimes, '
               '{target}, I wonder if these new players are just pretending to '
               'be bad for our amusement,\\" {initiator} says, chuckling at '
               'their gameplay.\\"Isn\'t it amazing, {target}, how we\'ve come '
               'so far in our gaming skills while these poor noobs are still '
               'trying to figure out the controls?\\" {initiator} '
               'laughs.mixer_socials_EnthuseAboutExperimentalFood_Targeted_Friendly_AlwaysOn_DiningSocials\\"{target}, '
               "you have to try this! It's unlike anything I've ever tasted "
               'before,\\" {initiator} says excitedly, taking another bite.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=333,
          lineno=1653,
          tokens=216,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Wow, this experimental dish is amazing! Don\'t you think '
               'so, {target}?\\" {initiator} asks, grinning from ear to '
               'ear.\\"I never thought I\'d like something so unconventional, '
               'but this food is delicious! You should give it a go, '
               '{target}!\\" {initiator} exclaims, offering a bite.\\"Isn\'t '
               "it fascinating how they've combined these flavors, {target}? I "
               'can\'t get enough of it!\\" {initiator} enthuses, digging into '
               'their meal.\\"Who would have thought that these ingredients '
               'could work so well together? You need to taste this, '
               '{target}!\\" {initiator} says, eyes sparkling with '
               'excitement.\\"Have you ever tried anything like this, '
               "{target}? It's so unique and delicious! I'm in love with this "
               'dish!\\" {initiator} gushes, savoring each bite.\\"I can\'t '
               'believe how amazing this experimental food is, {target}. You '
               'really need to try it!\\" {initiator} insists, gesturing '
               'towards their plate.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=334,
          lineno=1659,
          tokens=202,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Isn\'t this dish just incredible, {target}? I\'ve never '
               'experienced flavors like these before!\\" {initiator} '
               'declares, thoroughly enjoying their meal.\\"I have to admit, I '
               'was skeptical at first, but this experimental food has won me '
               'over. You should give it a try, {target}!\\" {initiator} '
               'suggests enthusiastically.\\"Can you believe how tasty this '
               "is, {target}? It's so unconventional, yet absolutely "
               'delicious!\\" {initiator} exclaims, eager for {target} to '
               'share the '
               'experience.mixer_social_ProfessUndyingLove_targeted_romance_highScore\\"{target}, '
               'I need to tell you something important. My love for you is '
               'undying, and I can\'t keep it to myself any longer,\\" '
               '{initiator} says, their heart pounding.\\"I\'ve been holding '
               'this in for too long, {target}. I am completely and utterly in '
               'love with you,\\" {initiator} confesses, looking deeply into '
               "{target}'s eyes."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=335,
          lineno=1668,
          tokens=211,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"There\'s something I\'ve been meaning to say, {target}. My '
               "love for you knows no bounds, and I can't keep it a secret any "
               'longer,\\" {initiator} says, their voice filled with '
               'emotion.\\"{target}, I can\'t hold it in any longer. I love '
               'you more than words can express, and I want you to know '
               'that,\\" {initiator} says, their voice trembling with '
               'sincerity.\\"I\'ve tried to deny it, but I can\'t anymore, '
               '{target}. I love you, and I will always love you,\\" '
               '{initiator} says, their eyes filled with a mix of hope and '
               'fear.\\"My heart has been aching to tell you this, {target}. I '
               'am deeply and irrevocably in love with you,\\" {initiator} '
               'confesses, their voice barely audible.\\"I never thought I '
               'could feel this way about someone, {target}, but I am head '
               'over heels in love with you,\\" {initiator} admits, their eyes '
               "searching {target}'s for a reaction."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=336,
          lineno=1673,
          tokens=217,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been hiding my feelings for far too long, {target}. I '
               'love you more than anything in this world, and I need you to '
               'know that,\\" {initiator} says, their voice shaking with '
               'vulnerability.\\"{target}, I\'ve tried to ignore these '
               "feelings, but I can't any longer. I am completely, undeniably "
               'in love with you,\\" {initiator} says, their voice full of '
               'sincerity and love.\\"I\'ve been keeping this secret for what '
               'feels like an eternity, {target}, but I have to tell you. I am '
               'madly, truly, and deeply in love with you,\\" {initiator} '
               'says, their eyes shining with '
               'emotion.mixer_social_MockMusicTaste_targeted_mean_trait\\"{target}, '
               "I can't believe you actually enjoy listening to that noise. "
               'What do you even see in it?\\" {initiator} teases with a '
               'grin.\\"Really, {target}? That\'s the kind of music you\'re '
               'into? I thought you had better taste than that,\\" {initiator} '
               'says, smirking.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=337,
          lineno=1682,
          tokens=213,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Wow, {target}, I didn\'t know anyone still listened to that '
               'kind of music. I guess you\'re just full of surprises,\\" '
               '{initiator} laughs mockingly.\\"Seriously, {target}? That band '
               "you like is just...terrible. I don't know how you can stand "
               'listening to them,\\" {initiator} says, rolling their '
               'eyes.\\"I have to say, {target}, your taste in music leaves a '
               'lot to be desired. I mean, really?\\" {initiator} says, '
               'chuckling condescendingly.\\"{target}, I didn\'t realize your '
               "music preferences were so...unique. I guess I can't help but "
               'laugh,\\" {initiator} says sarcastically.\\"Please tell me '
               "you're joking, {target}. You can't actually enjoy listening to "
               'that, can you?\\" {initiator} asks, stifling their '
               'laughter.\\"Yikes, {target}, your favorite band is like nails '
               'on a chalkboard to me. How do you even tolerate that sound?\\" '
               '{initiator} says, cringing.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=338,
          lineno=1688,
          tokens=227,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Oh, {target}, your music taste is...interesting, to say the '
               'least. But I guess everyone has their guilty pleasures,\\" '
               '{initiator} says with a snicker.\\"Whenever I think I know '
               'you, {target}, you reveal a new layer of weirdness. I never '
               'would\'ve pegged you for a fan of that music,\\" {initiator} '
               'says, shaking their head in '
               'disbelief.mixer_socials_EnthuseAboutMeal_Targeted_Friendly_AlwaysOn_DiningSocials\\"{target}, '
               'have you ever tasted anything as delicious as this before? '
               'It\'s absolutely amazing!\\" {initiator} exclaims, savoring '
               'every bite.\\"{initiator} leans toward {target} and says, '
               '\\"Wow, this meal is truly exceptional! You have to try some '
               'of this!\\"\\"Can you believe how incredible this food tastes, '
               '{target}?\\" {initiator} asks, eyes wide in delight and '
               'excitement.\\"I can\'t get over how delicious this is, '
               '{target}! I think I\'ve found my new favorite dish,\\" '
               '{initiator} says, beaming with joy.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=339,
          lineno=1698,
          tokens=227,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I don\'t think I\'ve ever been this excited about '
               'a meal before. Isn\'t it just divine?\\" {initiator} says, '
               'practically dancing in their seat.\\"This is hands down the '
               'best meal I\'ve ever had, {target}. What do you think?\\" '
               '{initiator} asks, eager to share the experience.\\"I\'m in '
               'food heaven right now, {target}. Have you ever tasted anything '
               'like this?\\" {initiator} gushes, unable to contain their '
               'enthusiasm.\\"Words can\'t even describe how fantastic this '
               'meal is, {target}. It\'s like a symphony of flavors,\\" '
               '{initiator} says, eyes closed in pure bliss.\\"Every bite of '
               "this meal is a revelation, {target}. I can't help but rave "
               'about it!\\" {initiator} says, a look of pure joy on their '
               'face.\\"I could eat this every day for the rest of my life, '
               '{target}. It\'s that good!\\" {initiator} exclaims, savoring '
               'each and every '
               'taste.mixer_social_PracticeFighting_targeted_Friendly_alwaysOn_skills'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=340,
          lineno=1708,
          tokens=219,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve been working on my fighting skills lately. '
               'Would you mind practicing with me?\\" {initiator} asks '
               'eagerly.\\"Hey {target}, I could use a sparring partner to '
               'help me improve my combat skills. Are you up for the '
               'challenge?\\" {initiator} inquires with a grin.\\"{initiator} '
               'stretches their arms and says, \\"Alright, {target}, it\'s '
               "time for some friendly combat practice. Let's see what you've "
               'got!\\"\\"Ever since I started learning to fight, I\'ve wanted '
               'to test my skills against you, {target}. Care to join me for a '
               'sparring session?\\" {initiator} suggests '
               'enthusiastically.\\"Let\'s have a little friendly competition, '
               "{target}. How about a practice fight to see who's got the "
               'better moves?\\" {initiator} proposes with a smirk.\\"Hey '
               "{target}, I've been meaning to ask if you'd like to practice "
               "some self-defense techniques with me. It's always good to stay "
               'sharp,\\" {initiator} says, gesturing toward an open space.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=341,
          lineno=1714,
          tokens=222,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve learned some new fighting techniques, {target}, and I '
               'could use your help to practice. Are you in?\\" {initiator} '
               'asks, bouncing on the balls of their feet.\\"{initiator} '
               'cracks their knuckles and says, \\"It\'s been too long since '
               "we've had a good sparring session, {target}. Let's see if you "
               'can keep up with my new moves!\\"\\"I think it\'s time we '
               'tested our strengths against each other, {target}. A friendly '
               'sparring match, what do you say?\\" {initiator} asks, eager to '
               'learn from the experience.\\"Practicing fighting techniques is '
               'always more fun with a partner, {target}. Would you mind '
               'joining me for a session?\\" {initiator} asks, hoping to '
               'improve their '
               'skills.mixer_social_MakeFunOfCorporateGoons_Targeted_Funny_AlwaysOn_Career\\"{target}, '
               'have you heard about the new Synergistic Paradigm-Enhancing '
               'Dynamic? It\'s the latest in corporate jargon!\\" {initiator} '
               'teases with a grin.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=342,
          lineno=1723,
          tokens=216,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I think you\'d excel at Synchronized Hyperbolic '
               'Resource Optimization. It\'s right up your alley,\\" '
               '{initiator} jokes, winking.\\"I just got a memo about the '
               'latest in corporate strategy, {target}. Apparently, we need to '
               'focus on Transdimensional Goal-Oriented Metrics!\\" '
               '{initiator} says, chuckling.\\"Hey {target}, have you been '
               'maximizing your Vertical Cross-Functional Integration '
               'lately?\\" {initiator} asks sarcastically, struggling to keep '
               'a straight face.\\"{target}, I think we need to discuss the '
               'importance of Inverted Scalable Quantum Networking,\\" '
               '{initiator} says with a smirk, trying to sound serious.\\"Did '
               'you know, {target}, that if we leverage our Holistic '
               'Interdependent Paradigms, we can achieve ultimate success?\\" '
               '{initiator} teases playfully.\\"{target}, you\'re just the '
               'person to help me develop a new strategy for Dynamic Quantum '
               'Leap Synergy. Your expertise is crucial,\\" {initiator} says, '
               'barely able to contain their laughter.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=343,
          lineno=1729,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I think we should really focus on optimizing '
               "our Metaphysical Ambiguity Resolution. It's the key to our "
               'success!\\" {initiator} jokes, nudging {target} '
               'playfully.\\"{target}, I\'ve got a new assignment for you: '
               "Integrative Quantum Flux Optimization. Don't worry, I'm sure "
               'you\'ll nail it,\\" {initiator} says, laughing.\\"Let\'s not '
               'forget the importance of Advanced Heterogeneous Ambiguity '
               'Analysis, {target}. It\'s the future of corporate success!\\" '
               '{initiator} says with a grin, making fun of the '
               'jargon.\\"{target}, have you ever noticed how corporate goons '
               "always seem to have a never-ending supply of buzzwords? It's "
               'like they\'re all reading from the same script,\\" {initiator} '
               'chuckles.\\"{initiator} leans in and whispers to {target}, '
               '\\"Do you think corporate goons practice their fake smiles and '
               'firm handshakes in front of the mirror every morning?\\"\\"I '
               'wonder if corporate culture has a dress code for the soul, '
               'too,\\" {initiator} muses, smirking at {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=344,
          lineno=1735,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, have you ever noticed that corporate goons '
               'can make a two-minute conversation take two hours with all '
               'their jargon and team-building exercises?\\" {initiator} '
               'jokes.\\"{target}, let\'s play a game: Corporate Buzzword '
               "Bingo. Every time we hear a corporate goon say 'synergy,' "
               "'innovation,' or 'value-added,' we take a sip of our "
               'coffee,\\" {initiator} suggests, grinning.\\"{initiator} '
               'laughs and asks {target}, \\"Do you think there\'s a secret '
               'competition among corporate goons to see who can use the most '
               'buzzwords in a single sentence?\\"\\"Corporate culture is like '
               "a cult, {target}, but instead of chanting, they're spouting "
               "off empty slogans and talking about 'disrupting the "
               'industry,\'\\" {initiator} says with a grin.\\"Hey {target}, I '
               'bet corporate goons have a secret handshake, but it probably '
               'involves excessive eye contact and an awkwardly long grip,\\" '
               '{initiator} teases.\\"{initiator} leans in and whispers to '
               '{target}, \\"I\'m convinced that corporate goons are actually '
               'robots, programmed to speak in buzzwords and networking '
               'lingo.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=345,
          lineno=1741,
          tokens=231,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Corporate culture seems like one big game of \'Who Can '
               'Sound the Most Important?\', don\'t you think, {target}?\\" '
               '{initiator} '
               'chuckles.mixer_socials_GoofAround_targeted_Funny_alwaysOn\\"{initiator} '
               'sneaks up behind {target} and places their hands over '
               '{target}\'s eyes. \\"Guess who?\\" {initiator} says, '
               'giggling.\\"{initiator} playfully tosses a crumpled piece of '
               'paper at {target}, trying to get their attention. \\"Hey, '
               '{target}, catch!\\"\\"{initiator} starts making silly faces at '
               '{target} from across the room, hoping to get a laugh out of '
               'them.\\"While {target} is sitting down, {initiator} comes up '
               'from behind and tickles them, causing {target} to burst into '
               'laughter.\\"{initiator} challenges {target} to a playful thumb '
               'war, grinning mischievously as they lock hands.\\"{initiator} '
               "steals {target}'s hat and starts running around, playfully "
               'taunting, \\"You\'ll never catch me, {target}!\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=346,
          lineno=1752,
          tokens=224,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} jokingly mimics {target}\'s voice and '
               'mannerisms, making both of them laugh at the light-hearted '
               'impersonation.\\"{initiator} pretends to trip and fall in '
               'front of {target}, then quickly jumps up and exclaims, '
               '\\"Gotcha, {target}!\\"\\"{initiator} playfully pokes {target} '
               'repeatedly, trying to get a rise out of them. \\"Hey, '
               '{target}, are you ticklish?\\"\\"{initiator} and {target} '
               'engage in a spontaneous and lighthearted play-fight, laughing '
               'as they gently push each other '
               'around.mixer_social_RantAndRave_targeted_friendly_emotionSpecific\\"{target}, '
               "I just can't take it anymore! I need to vent to you about "
               'what\'s been bothering me,\\" {initiator} says, visibly '
               'frustrated.\\"Listen, {target}, I\'ve got to get this off my '
               "chest. I'm going to rant for a bit, and I need you to just "
               'hear me out,\\" {initiator} pleads, their voice rising in '
               'irritation.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=347,
          lineno=1762,
          tokens=234,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been holding back for so long, {target}, but I can\'t '
               'keep it in anymore. I need to let it all out,\\" {initiator} '
               'exclaims, their anger evident.\\"{target}, I\'ve had enough of '
               'this situation, and I need someone to listen to me. Can you '
               'handle my rant right now?\\" {initiator} asks, their emotions '
               'boiling over.\\"Sometimes, I just need to let loose, {target}. '
               'Can you bear with me while I let off some steam?\\" '
               '{initiator} requests, their voice filled with tension.\\"I\'m '
               'so fed up with everything, {target}. I just need to rant for a '
               'minute, and I hope you\'ll understand,\\" {initiator} says, '
               'their face red with anger.\\"Enough is enough, {target}. I '
               'need to express my frustration, and I trust you enough to let '
               'it all out,\\" {initiator} says, their voice shaking with '
               'emotion.\\"I\'ve reached my breaking point, {target}, and I '
               'need your help to process it all. Just let me rant for a '
               'while, please,\\" {initiator} begs, their voice cracking.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=348,
          lineno=1768,
          tokens=215,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Today has just been too much, {target}. I need to vent, and '
               'I hope you won\'t mind listening to me rant,\\" {initiator} '
               'says, their emotions spilling over.\\"{target}, I don\'t know '
               'who else I can talk to about this. I need to rant, and I hope '
               'you\'ll be patient with me,\\" {initiator} says, their voice '
               'filled with '
               'desperation.mixer_Social_Sim_Ghost_Ask_About_Being_Dead\\"{target}, '
               "I've always been curious about the afterlife. Can you tell me "
               'what it\'s like to be a ghost?\\" {initiator} asks '
               'cautiously.\\"Hey {target}, I know it might be a sensitive '
               "topic, but I'm really interested in knowing what being dead "
               'feels like. Can you share your experience?\\" {initiator} '
               'inquires gently.\\"{target}, I\'ve been wondering about this '
               "for a while now. What's it like on the other side? Can you "
               'share your perspective as a ghost?\\" {initiator} asks with '
               'genuine curiosity.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=349,
          lineno=1777,
          tokens=238,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I can\'t imagine what you\'ve been through, {target}. Would '
               'you mind telling me what it\'s like to be dead?\\" {initiator} '
               "asks, trying to be considerate of {target}'s "
               'feelings.\\"Being a ghost must be so different from being '
               'alive, {target}. Can you tell me what your experience has been '
               'like since you passed away?\\" {initiator} asks with '
               'empathy.\\"{target}, I\'ve never had the chance to ask someone '
               "who's experienced it firsthand. What is it like to be a "
               'ghost?\\" {initiator} wonders aloud.\\"I hope it\'s not too '
               "personal, {target}, but I'm really curious about the "
               'afterlife. Can you share what it\'s like being dead?\\" '
               '{initiator} asks respectfully.\\"Death has always been a '
               'mystery to the living, {target}. Would you be willing to shed '
               'some light on what it\'s like being a ghost?\\" {initiator} '
               'asks, intrigued.\\"{target}, I don\'t mean to pry, but I\'ve '
               'always been fascinated by the concept of life after death. Can '
               'you share your experience as a ghost?\\" {initiator} questions '
               'gently.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=350,
          lineno=1783,
          tokens=219,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I know this might be an uncomfortable topic, but '
               "I can't help but wonder what it feels like to be dead. Can you "
               'enlighten me?\\" {initiator} asks with a mix of curiosity and '
               'concern.mixer_Social_Targeted_Romance_Loyal_ConfessCheating\\"{target}, '
               "I can't keep this from you any longer. I've been unfaithful in "
               'our relationship,\\" {initiator} admits, guilt heavy in their '
               'voice.\\"I never wanted to hurt you, {target}, but I have to '
               'be honest with you. I\'ve been cheating on you,\\" {initiator} '
               'says, struggling to meet {target}\'s eyes.\\"{target}, I\'ve '
               "made a terrible mistake. I've been seeing someone else behind "
               'your back, and I can\'t hide it anymore,\\" {initiator} '
               'confesses, tears welling up in their eyes.\\"This is going to '
               "hurt, but I need to tell you the truth, {target}. I've been "
               'unfaithful,\\" {initiator} reveals, their voice shaking with '
               'regret.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=351,
          lineno=1792,
          tokens=239,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been betraying your trust, {target}, and I can\'t '
               'keep it a secret any longer. I\'ve been cheating on you,\\" '
               '{initiator} says, clearly distressed.\\"{target}, I know this '
               "will be hard to hear, but I've been unfaithful in our "
               'relationship. I\'m so sorry,\\" {initiator} says, tears '
               'streaming down their face.\\"I can\'t pretend everything is '
               "fine anymore, {target}. I've been seeing someone else, and I "
               'need you to know,\\" {initiator} confesses, their voice barely '
               'a whisper.\\"{target}, I don\'t deserve your forgiveness, but '
               'I need to tell you that I\'ve cheated on you,\\" {initiator} '
               'admits, their face filled with shame.\\"I wish I could take it '
               "back, {target}, but I can't. I've been cheating on you, and "
               'it\'s tearing me apart,\\" {initiator} says, their voice '
               'filled with remorse.\\"Please know how much I regret this, '
               "{target}, but I've been unfaithful to you. I just couldn't "
               'keep it a secret any longer,\\" {initiator} says, their heart '
               'heavy with guilt.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=352,
          lineno=1800,
          tokens=235,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_Provoke_targeted_mean_emotionSpecific\\"{target}, '
               "I've heard people say you're not very bright, but I didn't "
               'think it was this bad,\\" {initiator} sneers, trying to '
               'provoke a reaction.\\"I\'m surprised you even made it this '
               'far, {target}. Did someone carry you here?\\" {initiator} says '
               'mockingly, hoping to get under {target}\'s skin.\\"Oh, I see '
               "you're still trying. It's almost cute how you think you can "
               'keep up, {target},\\" {initiator} taunts maliciously.\\"Did '
               "anyone ever tell you that you're way out of your league, "
               '{target}? Or are they just being polite?\\" {initiator} says '
               'with a cruel grin.\\"{target}, do you ever get tired of being '
               'the weakest link? Or have you just accepted it as a part of '
               'who you are?\\" {initiator} asks, trying to provoke '
               '{target}.\\"Hey {target}, have you considered giving up? It\'s '
               'probably for the best, considering your track record,\\" '
               "{initiator} says, attempting to hurt {target}'s feelings."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=353,
          lineno=1808,
          tokens=246,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I was just wondering, {target}, how does it feel to be '
               'constantly overshadowed by everyone around you?\\" {initiator} '
               'asks, a mean smirk on their face.\\"Tell me, {target}, how do '
               "you manage to fail so consistently? It's almost "
               'impressive,\\" {initiator} says, trying to provoke {target} '
               'into reacting.\\"I don\'t think I\'ve ever met someone as '
               'incompetent as you, {target}. How do you even manage to get '
               'through the day?\\" {initiator} asks, attempting to anger '
               '{target}.\\"Sometimes, {target}, I honestly wonder if you\'re '
               "even trying. Has anyone ever told you that you're a "
               'disappointment?\\" {initiator} says, trying to get a rise out '
               'of '
               '{target}.mixer_Social_Targeted_Romance_Loyal_RebuildTrust\\"{target}, '
               "I know I've made mistakes in the past, but I want to make it "
               'right. Can we start over?\\" {initiator} asks with hope in '
               'their eyes.\\"Remember the good times we had, {target}? I want '
               'to create more of those memories with you, but first we need '
               'to rebuild our trust,\\" {initiator} says sincerely.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=354,
          lineno=1818,
          tokens=221,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I understand that I\'ve hurt you, and I\'m '
               'willing to do whatever it takes to regain your trust. Please '
               'give me a chance,\\" {initiator} pleads, looking into '
               '{target}\'s eyes.\\"I\'ve learned from my mistakes, {target}, '
               'and I promise to be a better partner for you. Can we work on '
               'rebuilding our trust together?\\" {initiator} asks '
               'earnestly.\\"I know I\'ve let you down, {target}, but I truly '
               "believe we can find our way back to each other. Let's take it "
               'one step at a time,\\" {initiator} suggests, reaching for '
               '{target}\'s hand.\\"Trust is the foundation of any '
               "relationship, {target}, and I want to rebuild ours. I'm "
               'committed to being open and honest with you from now on,\\" '
               '{initiator} promises, holding {target}\'s gaze.\\"Please, '
               "{target}, I'm asking for a chance to make amends. I want to "
               'show you that I can be the person you deserve,\\" {initiator} '
               'says, desperation in their voice.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=355,
          lineno=1823,
          tokens=227,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I know it won\'t be easy, {target}, but if you\'re willing '
               "to try, I'll do everything in my power to rebuild the trust we "
               'once had,\\" {initiator} vows, determination in their '
               'eyes.\\"{target}, I want to be the person who makes you happy, '
               "not the one who causes you pain. I'll work tirelessly to "
               'regain your trust,\\" {initiator} says, their voice full of '
               'conviction.\\"I can\'t change the past, {target}, but I can '
               "change our future. Let's work together to rebuild the trust "
               'and love we once shared,\\" {initiator} says, holding out '
               'their hand for {target} to '
               'take.mixer_social_ShareMelancholyThoughts_tag_Friendly_alwaysOn\\"{target}, '
               "I've been feeling really down lately, and I don't know who "
               'else to talk to,\\" {initiator} says, with sadness in their '
               'eyes.\\"Sometimes, I feel like I\'m drowning in my own '
               'thoughts, and I just need someone to listen. Can I share them '
               'with you, {target}?\\" {initiator} asks hesitantly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=356,
          lineno=1832,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been going through a rough time, {target}, and I '
               'think talking about it with you might help,\\" {initiator} '
               'admits, hoping for understanding.\\"The world feels so heavy '
               'on my shoulders, {target}. I need to get these thoughts off my '
               'chest. Will you hear me out?\\" {initiator} pleads gently.\\"I '
               "never thought I'd open up like this, but I trust you, "
               '{target}. Can I share my melancholic thoughts with you?\\" '
               '{initiator} asks, looking vulnerable.\\"{target}, I feel like '
               "I'm trapped in a dark cloud, and I don't know how to escape "
               'it. Can we talk about it?\\" {initiator} asks, reaching out '
               'for support.\\"Sometimes, I don\'t know how to cope with these '
               'sad thoughts, {target}. Would you listen to me and help me '
               'sort them out?\\" {initiator} wonders, looking for '
               'comfort.\\"I\'ve been feeling really low, {target}, and I '
               'think I need to talk about it. Can I confide in you?\\" '
               '{initiator} asks, with a glimmer of hope in their eyes.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=357,
          lineno=1838,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I think I need a friend right now. Can I share '
               'what\'s been bothering me with you?\\" {initiator} asks, '
               'seeking solace.\\"I know it\'s not easy listening to '
               "someone's sad thoughts, {target}, but I don't know who else to "
               'turn to. Can you be there for me?\\" {initiator} pleads, '
               'searching for '
               'understanding.mixer_social_SweetTalk_targeted_romance_skills\\"{target}, '
               "every time I look into your eyes, I feel like I'm getting lost "
               'in a beautiful, endless ocean,\\" {initiator} says with a warm '
               'smile.\\"You have no idea how much my heart races when I\'m '
               "around you, {target}. It's like you've cast a magical spell on "
               'me,\\" {initiator} says, gazing at {target} '
               'adoringly.\\"{target}, your smile lights up the room and fills '
               "my heart with happiness. I'm so grateful to have you in my "
               'life,\\" {initiator} whispers gently.\\"Being with you, '
               '{target}, feels like a dream come true. Every moment I spend '
               'with you is a treasure,\\" {initiator} says sincerely.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=358,
          lineno=1848,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, your laughter is like music to my ears, and just '
               'the thought of you brightens up even my darkest days,\\" '
               '{initiator} says with a loving expression.\\"When I hold you '
               "in my arms, {target}, I feel like I'm holding the entire "
               'world, and nothing else matters,\\" {initiator} says, brushing '
               '{target}\'s hair back gently.\\"Your presence, {target}, is '
               'like a warm, comforting embrace that shelters me from all the '
               'storms of life,\\" {initiator} says with deep '
               'affection.\\"{target}, your love is like a beacon that guides '
               'me through the darkest nights, leading me home to you,\\" '
               '{initiator} says, their eyes locked on {target}\'s.\\"Whenever '
               'I think of you, {target}, my heart swells with love and '
               "admiration. You truly are the most incredible person I've ever "
               'known,\\" {initiator} says, holding {target}\'s hand.\\"In '
               "your arms, {target}, I've found my sanctuary, my safe haven. I "
               'never knew true love until I met you,\\" {initiator} says, '
               'their voice filled with '
               'emotion.mixer_social_PitchStoryIdea_targeted_friendly_emotionSpecific'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=359,
          lineno=1858,
          tokens=233,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I had this amazing story idea, and I wanted to '
               'share it with you. Let me know what you think,\\" {initiator} '
               'says excitedly.\\"Hey, {target}, I\'ve been thinking about '
               'writing a novel, and I have this incredible idea. Can I run it '
               'by you?\\" {initiator} asks, eager for feedback.\\"I came up '
               'with a fascinating storyline, {target}. Would you mind '
               'listening to it and giving me your thoughts?\\" {initiator} '
               'inquires, looking hopeful.\\"So, I\'ve been brainstorming, and '
               "I think I have a great idea for a story. I'd love to hear your "
               'opinion, {target},\\" {initiator} says, trying to gauge their '
               'interest.\\"Okay, {target}, I have this brilliant concept for '
               'a tale, and I need someone to bounce ideas off of. Are you up '
               'for it?\\" {initiator} asks, their eyes shimmering with '
               'enthusiasm.\\"I\'ve been working on this incredible idea for a '
               'narrative, {target}. Can I share it with you and get your '
               'input?\\" {initiator} suggests, smiling nervously.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=360,
          lineno=1864,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey, {target}, you know how much I love stories, right? '
               'Well, I came up with an idea that I think is fantastic, and '
               'I\'d like your thoughts on it,\\" {initiator} says, waiting '
               'for their response.\\"I\'ve had this story idea brewing in my '
               "mind for a while, {target}. It's finally taking shape, and I'd "
               'love to have your perspective on it,\\" {initiator} admits, '
               'looking a bit shy.\\"You always give great advice, {target}. '
               "I'd really appreciate it if you could listen to my story idea "
               'and tell me what you think,\\" {initiator} pleads, hoping for '
               'a positive response.\\"Alright, {target}, I\'ve got this '
               "intriguing idea for a tale that's been keeping me up at night. "
               'I need your expert opinion. Are you ready to hear it?\\" '
               '{initiator} asks, grinning in '
               'anticipation.mixer_social_RekindleTheRomance_targeted_romance_lowScore\\"{target}, '
               "I've been thinking a lot lately about the times we shared "
               'together. Can we give it another try?\\" {initiator} asks, '
               'hope in their eyes.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=361,
          lineno=1873,
          tokens=212,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Remember the good days, {target}? I miss them. I miss us. '
               'What do you say we try to rekindle the flame?\\" {initiator} '
               'suggests, a nostalgic smile on their face.\\"{target}, I '
               "can't help but feel that we were meant to be together. Can we "
               'give our love a second chance?\\" {initiator} pleads, their '
               'heart on their sleeve.\\"Every time I see you, {target}, I\'m '
               'reminded of what we once had. Do you ever wonder if we could '
               'have it again?\\" {initiator} asks, looking for a glimmer of '
               'hope.\\"I\'ve never stopped caring about you, {target}, and I '
               "think it's time we explore the possibility of getting back "
               'together,\\" {initiator} says, taking a deep '
               'breath.\\"{target}, I know it\'s been a while, but I can\'t '
               'shake the feeling that we belong together. Could we give our '
               'romance another shot?\\" {initiator} inquires, looking into '
               "{target}'s eyes."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=362,
          lineno=1878,
          tokens=234,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been doing a lot of soul-searching, {target}, and '
               "I've come to realize that I want to be with you again. Can we "
               'try to rekindle our love?\\" {initiator} asks '
               'earnestly.\\"{target}, I know we\'ve both grown and changed, '
               'but I believe we can find our way back to each other. Are you '
               'willing to try?\\" {initiator} asks, searching for a positive '
               'response.\\"Have you ever thought about us, {target}? About '
               "what we could be if we tried again? I'm ready to give it a "
               'chance if you are,\\" {initiator} says, holding their breath '
               'for an answer.\\"{target}, I keep thinking about the love we '
               'shared and how special it was. I know we can make it work '
               'again. Please, can we try?\\" {initiator} begs, with a mix of '
               'hope and '
               'vulnerability.mixer_Social_Targeted_Mean_Loyal_ConfrontAboutBullying\\"{target}, '
               "I've had enough of your bullying. It's time we talked about "
               'it,\\" {initiator} says, gathering the courage to stand up for '
               'themselves.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=363,
          lineno=1887,
          tokens=233,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I can\'t keep ignoring the way you treat me, {target}. We '
               'need to address this bullying situation,\\" {initiator} says, '
               'looking determined.\\"{target}, I\'ve been feeling really hurt '
               "by the way you've been treating me. It's time for us to talk "
               'about your bullying behavior,\\" {initiator} says, trying to '
               'keep their voice steady.\\"I refuse to be a victim anymore, '
               '{target}. Your bullying has to stop, and we need to discuss it '
               'right now,\\" {initiator} says, finally confronting the '
               'issue.\\"Your constant bullying has made my life miserable, '
               "{target}. Let's sit down and talk about why you're doing this "
               'to me,\\" {initiator} says, hoping for a '
               'resolution.\\"{target}, I want to understand why you\'ve been '
               "bullying me. It's causing me a lot of pain, and we need to "
               'talk about it,\\" {initiator} says, searching for answers.\\"I '
               "didn't want to have to confront you like this, {target}, but "
               'your bullying has pushed me to my limit. We need to resolve '
               'this issue,\\" {initiator} says, taking a stand.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=364,
          lineno=1893,
          tokens=223,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been trying to ignore your bullying, {target}, but I '
               "can't take it anymore. Let's talk about what's going on and "
               'why you\'re treating me this way,\\" {initiator} suggests, '
               'desperate for a change.\\"{target}, your bullying has been '
               "affecting more than just me. It's time we had a conversation "
               'about your actions and their consequences,\\" {initiator} '
               'says, seeking to make a difference.\\"I\'m tired of being your '
               'target, {target}. We need to discuss your bullying behavior '
               'and find a way to put an end to it,\\" {initiator} says, '
               'standing up for themselves with newfound '
               'confidence.mixer_social_WeaponizedJoke_targeted_funny_alwaysOn\\"{target}, '
               "I heard this joke the other day, but it's a bit edgy. Are you "
               'up for it?\\" {initiator} asks, grinning mischievously.\\"Hey, '
               "{target}, brace yourself. I've got a joke that might just "
               'cross the line, but I think you\'ll love it,\\" {initiator} '
               'says with a sly smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=365,
          lineno=1902,
          tokens=241,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Alright, {target}, I\'ve got a joke for you, but it\'s '
               'definitely not for the faint of heart. Are you ready?\\" '
               '{initiator} inquires, a playful glint in their eye.\\"I came '
               "across this edgy joke, {target}, and I couldn't help but think "
               'of you. Do you want to hear it?\\" {initiator} asks, raising '
               'their eyebrows.\\"Prepare yourself, {target}, I\'ve got a joke '
               "that's bound to push some boundaries, but I think you can "
               'handle it,\\" {initiator} says, smirking.\\"Okay, {target}, '
               "I've got a joke for you, but it's a little on the wild side. "
               'You in?\\" {initiator} asks, gauging {target}\'s '
               'reaction.\\"{target}, I\'ve got an edgy joke for you, but if '
               'it\'s too much, just remember, you asked for it,\\" '
               '{initiator} teases, testing the waters.\\"Hey, {target}, I\'ve '
               "got a joke that's right on the edge of being too much. Do you "
               'dare to hear it?\\" {initiator} asks, challenging {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=366,
          lineno=1908,
          tokens=206,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve got a pretty edgy joke for you, but you\'ve '
               'got to promise not to hold it against me. Deal?\\" {initiator} '
               'says, grinning cautiously.\\"Alright, {target}, I\'ve got a '
               "joke that might be a bit too edgy, but I have a feeling you'll "
               'appreciate it. Ready?\\" {initiator} asks, hoping for a '
               'positive '
               'response.mixer_socials_DiscussFoodFlavors_Targeted_Friendly_AlwaysOn_DiningSocials\\"{target}, '
               'have you ever wondered why some flavors just seem to go well '
               'together?\\" {initiator} asks, looking genuinely curious.\\"Do '
               "you have a favorite flavor combination, {target}? I've been "
               "experimenting with some new recipes and I'd love to hear your "
               'thoughts,\\" {initiator} says, smiling.\\"Hey {target}, I\'ve '
               'been thinking about how different cultures have unique flavor '
               'profiles. What\'s your favorite cuisine, and why?\\" '
               '{initiator} inquires, genuinely interested.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=367,
          lineno=1917,
          tokens=211,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve always been fascinated by the way our taste '
               "buds work. What's the strangest flavor you've ever tried, and "
               'did you like it?\\" {initiator} asks, eager for an answer.\\"I '
               'was just reading about the science behind flavor pairings, '
               "{target}. Do you think there's some truth to the idea that "
               'certain flavors are destined to be together?\\" {initiator} '
               'wonders aloud.\\"{target}, I know it might sound weird, but '
               'have you ever had a flavor combination that you thought would '
               'be awful, but ended up being surprisingly good?\\" {initiator} '
               'asks, intrigued.\\"Have you noticed how different seasons seem '
               "to have their own unique flavors, {target}? What's your "
               'favorite seasonal flavor, and why?\\" {initiator} asks, '
               'looking for a thoughtful response.\\"Hey {target}, I\'ve been '
               'experimenting with some new spices lately. Do you have any '
               'favorite spices or herbs that you think really elevate a '
               'dish?\\" {initiator} inquires, looking for inspiration.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=368,
          lineno=1922,
          tokens=215,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I recently read that our taste preferences can '
               'change as we age. Have you ever experienced a change in your '
               'taste buds, and what flavors do you appreciate now that you '
               'didn\'t before?\\" {initiator} asks, genuinely curious.\\"So, '
               "{target}, I've been playing around with the idea of creating a "
               "new dish based on unusual flavor combinations. What's "
               "something you think might be interesting to try, even if it's "
               'a bit out there?\\" {initiator} asks, eager for a creative '
               'suggestion.mixer_social_ComplimentColorChoices_targeted_Friendly_alwaysOn_situation_Day1DLC\\"{target}, '
               "I must say, the colors you've chosen really bring out the best "
               'in you,\\" {initiator} says with a smile.\\"I\'ve been meaning '
               'to tell you, {target}, the colors you wear always seem to '
               'brighten up the room,\\" {initiator} remarks '
               'appreciatively.\\"Your taste in colors is impeccable, '
               '{target}. It really highlights your personality,\\" '
               '{initiator} compliments sincerely.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=369,
          lineno=1931,
          tokens=244,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I just wanted to say that your color choices are '
               'always so unique and stylish. It\'s really impressive,\\" '
               '{initiator} comments admiringly.\\"Can I just say, {target}, '
               'that your color choices never fail to impress me? You have a '
               'fantastic sense of style,\\" {initiator} says with a nod of '
               'approval.\\"You know, {target}, I\'ve always admired your '
               "ability to mix and match colors so effortlessly. It's truly a "
               'talent,\\" {initiator} mentions, looking '
               'impressed.\\"{target}, I\'ve noticed that you have a real '
               'knack for choosing colors that perfectly suit you. Keep up the '
               'great work!\\" {initiator} encourages warmly.\\"I wanted to '
               'tell you, {target}, that the colors you pick always manage to '
               'make a statement. You have a real eye for it,\\" {initiator} '
               'says, looking genuinely impressed.\\"Your color choices always '
               'stand out, {target}. You have a way of making even the '
               'simplest combinations look stunning,\\" {initiator} '
               'compliments enthusiastically.\\"{target}, your color choices '
               "always seem to be on point. It's like you have a natural flair "
               'for it,\\" {initiator} says with a look of admiration.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=370,
          lineno=1940,
          tokens=219,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_ComplainAbout_Fruitcake_targeted_alwayson\\"{target}, '
               "can you believe how terrible fruitcake is? I just don't get "
               'why anyone would like it,\\" {initiator} says, grimacing.\\"I '
               "don't know about you, {target}, but I honestly can't stand "
               'fruitcake. It\'s just so dense and unappetizing,\\" '
               '{initiator} complains.\\"Am I the only one who thinks '
               'fruitcake is just the worst? What are your thoughts, '
               '{target}?\\" {initiator} asks, hoping for agreement.\\"I have '
               'to get this off my chest, {target}: fruitcake has got to be '
               'the most overrated dessert ever,\\" {initiator} says with '
               'disdain.\\"Every time I see a fruitcake, I just can\'t help '
               "but wonder who actually enjoys eating it. Don't you agree, "
               '{target}?\\" {initiator} questions.\\"I\'m sorry, {target}, '
               "but I just can't hold back any longer. Fruitcake is absolutely "
               'awful, isn\'t it?\\" {initiator} vents.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=371,
          lineno=1948,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I need someone to back me up on this: fruitcake '
               'is just gross, right?\\" {initiator} asks, looking for '
               'validation.\\"I\'ve been meaning to ask you, {target}: are you '
               "a fan of fruitcake? Because I honestly can't understand its "
               'appeal,\\" {initiator} says, baffled.\\"Every holiday season, '
               'I dread the inevitable appearance of fruitcake. Do you share '
               'my sentiments, {target}?\\" {initiator} asks with a sigh.\\"I '
               "can't be the only one who thinks fruitcake is an abomination, "
               'right, {target}?\\" {initiator} pleads, looking for support in '
               'their '
               'distaste.mixer_social_DiscussLackOfNewspapers_targeted_Friendly_alwysOn_situation_Day1DLC\\"{target}, '
               "have you noticed that there aren't many newspapers around "
               'anymore? It\'s quite frustrating,\\" {initiator} says, clearly '
               'annoyed.\\"I can\'t believe how hard it is to find a decent '
               'newspaper these days, {target}. What\'s going on?\\" '
               '{initiator} complains, shaking their head.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=372,
          lineno=1958,
          tokens=212,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, it\'s like newspapers have vanished into thin '
               'air. I miss the days when I could just grab one and enjoy my '
               'morning coffee,\\" {initiator} sighs.\\"I don\'t know about '
               'you, {target}, but the lack of newspapers around here is '
               'really getting on my nerves,\\" {initiator} grumbles.\\"It\'s '
               "a sad state of affairs when you can't even find a newspaper to "
               'read anymore, don\'t you think, {target}?\\" {initiator} asks '
               'with a frown.\\"I was just telling someone the other day how I '
               "miss the feel of a newspaper in my hands, {target}. It's just "
               'not the same anymore,\\" {initiator} laments.\\"Remember when '
               'you could find newspapers everywhere, {target}? What happened '
               'to those days? I can\'t stand this digital age,\\" {initiator} '
               'complains passionately.\\"{target}, do you have any idea where '
               "I can find a newspaper around here? It seems like they're a "
               'rare commodity these days,\\" {initiator} says in frustration.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=373,
          lineno=1964,
          tokens=242,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Sometimes I feel like I\'m the only person left who still '
               "prefers a newspaper to reading news online, {target}. It's "
               'quite disheartening,\\" {initiator} confides.\\"I just want a '
               'simple newspaper to read with my morning coffee, {target}. Why '
               'is that so difficult to find these days?\\" {initiator} asks, '
               'exasperated.mixer_social_ChewOut_targeted_mean_emotionSpecific\\"{target}, '
               "I can't believe how thoughtless you've been! You should be "
               'ashamed of yourself,\\" {initiator} says angrily.\\"How many '
               'times do I have to tell you, {target}? You always mess things '
               'up!\\" {initiator} yells, frustration evident in their '
               'voice.\\"{target}, I\'m so sick of your incompetence! When are '
               'you going to get it together?\\" {initiator} snaps, glaring at '
               'them.\\"{target}, your constant failures are getting on my '
               'nerves! Can\'t you do anything right?\\" {initiator} exclaims, '
               'seething with rage.\\"Are you really this careless, {target}? '
               'It\'s like you don\'t even care about anyone but yourself!\\" '
               '{initiator} scolds harshly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=374,
          lineno=1975,
          tokens=232,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Every time I think you\'ve changed, {target}, you prove me '
               'wrong. I\'m tired of your selfishness!\\" {initiator} says, '
               'shaking their head in disappointment.\\"I\'ve had enough of '
               "your nonsense, {target}! It's time you grow up and take "
               'responsibility for your actions!\\" {initiator} barks, fed up '
               'with their behavior.\\"{target}, I don\'t know how much more '
               'of your stupidity I can take. Get your act together!\\" '
               '{initiator} shouts, losing their patience.\\"Seriously, '
               "{target}? You've crossed the line this time. I won't tolerate "
               'this kind of behavior any longer!\\" {initiator} warns, their '
               'voice dripping with contempt.\\"Enough is enough, {target}! '
               'You really need to start thinking about the consequences of '
               'your actions!\\" {initiator} chastises, their anger reaching a '
               'boiling '
               'point.mixer_social_ComplainAboutTvSize_targeted_Friendly_alwaysOn\\"{target}, '
               "I can't believe how small this TV is! How can anyone watch "
               'anything on this?\\" {initiator} says, squinting at the '
               'screen.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=375,
          lineno=1985,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Ugh, this TV is just too tiny, {target}. How do you even '
               'enjoy watching anything on it?\\" {initiator} complains, '
               'annoyed.\\"Seriously, {target}, this TV is giving me a '
               'headache. Who even buys a TV this small nowadays?\\" '
               '{initiator} grumbles.\\"I can\'t take it anymore, {target}. '
               'This TV is just too small for my liking. We need an '
               'upgrade,\\" {initiator} says with frustration.\\"{target}, '
               "it's like watching a movie on a postage stamp. This TV size is "
               'ridiculous!\\" {initiator} exclaims, shaking their head.\\"You '
               "know, {target}, I've never been one to complain, but this TV "
               'size is just unbearable,\\" {initiator} says, rubbing their '
               'eyes.\\"I can\'t help but say it, {target}, but this TV is '
               'just way too small for the room. We need something bigger,\\" '
               '{initiator} says, trying to adjust their view.\\"Watching a '
               'movie on this TV is like trying to read a book through a '
               'keyhole, {target}. It\'s just too small!\\" {initiator} moans.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=376,
          lineno=1992,
          tokens=240,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been holding my tongue, {target}, but this TV size is '
               'driving me crazy. Can we please consider getting a bigger '
               'one?\\" {initiator} pleads.\\"I don\'t know how you can stand '
               'it, {target}. This TV is just too small to enjoy anything '
               'properly,\\" {initiator} says, clearly '
               'irritated.mixer_social_Congratulate_targeted_Friendly_alwaysOn_event\\"{target}, '
               'I just wanted to say congratulations on your achievement! You '
               'truly deserve it,\\" {initiator} says with a warm smile.\\"Hey '
               '{target}, congratulations on your big win! I knew you could do '
               'it!\\" {initiator} exclaims, giving {target} a pat on the '
               'back.\\"Congrats, {target}! I\'m so proud of you and '
               'everything you\'ve accomplished,\\" {initiator} says, beaming '
               'with pride.\\"{target}, I just heard the news! '
               'Congratulations, my friend! You\'ve earned it,\\" {initiator} '
               'says, raising a toast in {target}\'s honor.\\"I couldn\'t be '
               'happier for you, {target}. Congratulations on your success!\\" '
               '{initiator} says, offering a heartfelt hug.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=377,
          lineno=2003,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Wow, {target}, you really did it! I\'m so impressed and '
               'proud of you. Congratulations!\\" {initiator} says, clapping '
               'their hands in excitement.\\"Congratulations, {target}! Your '
               "hard work and determination have finally paid off. I'm really "
               'happy for you,\\" {initiator} says, sincerity shining in their '
               'eyes.\\"Kudos to you, {target}! I always knew you had it in '
               'you. Congratulations on this amazing achievement,\\" '
               '{initiator} says, giving {target} a high-five.\\"Well done, '
               '{target}! Your success is truly well-deserved. '
               'Congratulations!\\" {initiator} says, offering a firm '
               'handshake.\\"Bravo, {target}! Your accomplishments never cease '
               'to amaze me. Congratulations on this latest triumph,\\" '
               '{initiator} says, wearing a genuine smile of '
               'admiration.mixer_social_AskAboutDrink_targeted_Friendly_alwaysOn_Event\\"{target}, '
               'do you like the drink I made for you?\\" {initiator} asks, '
               'looking for approval.\\"How\'s the drink, {target}? Is it to '
               'your liking?\\" {initiator} inquires with a smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=378,
          lineno=2014,
          tokens=214,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I tried a new recipe for this drink, {target}. What do you '
               'think of it?\\" {initiator} questions, seeking an honest '
               'opinion.\\"Are you enjoying that drink, {target}? I was hoping '
               'you\'d like it,\\" {initiator} says, watching {target} take a '
               'sip.\\"Hey {target}, how\'s the drink? I put a little twist on '
               'it, do you like it?\\" {initiator} asks curiously.\\"{target}, '
               "is the drink good? I wasn't sure if it would be to your "
               'taste,\\" {initiator} says, sounding a bit uncertain.\\"So, '
               "{target}, what's your verdict on the drink? Thumbs up or "
               'down?\\" {initiator} asks playfully.\\"I noticed you haven\'t '
               'said anything about the drink, {target}. Do you like it?\\" '
               '{initiator} questions, hoping for a positive response.\\"I was '
               'experimenting with flavors in this drink, {target}. How did it '
               'turn out?\\" {initiator} asks, eager for feedback.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=379,
          lineno=2021,
          tokens=225,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Is the drink hitting the spot, {target}? I wanted to make '
               'something you\'d enjoy,\\" {initiator} says, hoping their '
               'effort paid '
               'off.mixer_social_DiscussFitnessTechniques_targeted_Friendly_alwaysOn_skills\\"{target}, '
               "I've been trying out this new workout routine, and I'd love to "
               'hear your thoughts on it,\\" {initiator} says '
               'enthusiastically.\\"Hey {target}, you seem to be in great '
               'shape. Can you share some fitness tips with me?\\" {initiator} '
               'asks, genuinely interested.\\"So, {target}, I\'ve been '
               'experimenting with different exercises lately. Have you tried '
               'any new fitness techniques that you think are worth '
               'sharing?\\" {initiator} inquires.\\"I\'ve noticed you\'re '
               'really consistent with your workouts, {target}. Mind sharing '
               'some of your favorite techniques?\\" {initiator} asks, hoping '
               'to learn something new.\\"{target}, I came across this fitness '
               "article about a new technique, and I can't decide if it's "
               'worth trying. What do you think?\\" {initiator} says, showing '
               'the article to {target}.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=380,
          lineno=2031,
          tokens=240,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I\'ve been trying to improve my fitness '
               'lately. Can you recommend any techniques that have worked well '
               'for you?\\" {initiator} asks with curiosity.\\"I\'ve been '
               'struggling with my workout routine recently, {target}. Do you '
               'have any fitness techniques that could help me get back on '
               'track?\\" {initiator} says, feeling a bit '
               'discouraged.\\"{target}, I heard about this interesting '
               "fitness technique that's supposed to be really effective. Have "
               'you tried anything like that before?\\" {initiator} asks, '
               'eager for information.\\"I\'m thinking of incorporating some '
               'new fitness techniques into my routine, {target}. Any '
               'suggestions on where to start?\\" {initiator} asks, seeking '
               'advice.\\"{initiator} approaches {target} at the gym and asks, '
               '\\"Hey, I noticed you were doing a unique exercise. Can you '
               'explain the technique behind it? It looks really '
               'effective.\\"mixer_social_DiscussLocalFishingSpots_targeted_friendly_alwaysOn_neighbor\\"{target}, '
               'have you heard about that hidden fishing spot near the old '
               'bridge? I\'ve heard the fish are biting like crazy there,\\" '
               '{initiator} says with excitement.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=381,
          lineno=2041,
          tokens=215,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I was thinking of trying out a new fishing '
               'spot this weekend. Any recommendations?\\" {initiator} asks, '
               'hoping for some insider tips.\\"{target}, I heard you\'re '
               'quite the fisherman. Mind sharing some of your favorite local '
               'fishing spots with me?\\" {initiator} inquires, genuinely '
               'interested.\\"I caught this monster of a fish the other day, '
               '{target}. Let me tell you about the amazing spot I found!\\" '
               '{initiator} says, eager to share their discovery.\\"{target}, '
               'I came across this beautiful fishing spot the other day. You '
               'should join me there sometime,\\" {initiator} suggests, hoping '
               'for some quality time together.\\"Did you know, {target}, that '
               "there's a hidden gem of a fishing spot just a few miles from "
               'here? Let me fill you in,\\" {initiator} says, ready to share '
               'the secret.\\"Rumor has it that there\'s a fantastic fishing '
               'spot around here, {target}. Have you tried it yet?\\" '
               '{initiator} asks curiously.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=382,
          lineno=2047,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"So, {target}, I\'ve been exploring some local fishing spots '
               'lately, and I found this incredible place. Want to hear about '
               'it?\\" {initiator} asks with enthusiasm.\\"I\'ve been trying '
               'out different fishing spots around here, {target}. What are '
               'your go-to places when you want a good catch?\\" {initiator} '
               'inquires, hoping to learn something new.\\"{target}, I know '
               "you're an expert when it comes to local fishing spots. Can you "
               'share some of your secrets with me?\\" {initiator} asks, '
               'looking for '
               'guidance.mixer_social_DiscussZebras_targeted_Friendly_alwaysOn_situation_Day1DLC\\"{target}, '
               'have you ever wondered about the unique stripes of zebras and '
               'their purpose?\\" {initiator} asks curiously.\\"{target}, did '
               'you know that no two zebras have the same pattern of stripes? '
               'It\'s like their own personal fingerprint,\\" {initiator} '
               'shares excitedly.\\"Hey, {target}, did you ever get the chance '
               "to see zebras up close? They're such fascinating "
               'creatures,\\" {initiator} says, reminiscing about a past '
               'experience.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=383,
          lineno=2057,
          tokens=244,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I was reading an article about zebras the other day, '
               '{target}. It turns out their stripes help them stay cool in '
               'the heat,\\" {initiator} explains, eager to share the newfound '
               'knowledge.\\"Have you ever wondered why zebras are social '
               "creatures, {target}? I'd love to talk about their unique "
               'behaviors with you,\\" {initiator} says, hoping to spark an '
               'interesting conversation.\\"{target}, I was watching a '
               "documentary on zebras yesterday, and I thought you'd find it "
               'interesting too. Want to watch it with me?\\" {initiator} '
               'suggests enthusiastically.\\"I\'ve always been intrigued by '
               'the way zebras run in zigzag patterns to escape predators, '
               "{target}. Do you think it's their stripes that help them with "
               'this?\\" {initiator} asks, looking for {target}\'s '
               'opinion.\\"Did you know that zebras can actually run up to 65 '
               'kilometers per hour, {target}? I find that fascinating!\\" '
               '{initiator} exclaims, eager to discuss the topic '
               'further.\\"{target}, what\'s your favorite thing about zebras? '
               'I\'m curious to know,\\" {initiator} asks, hoping to learn '
               "more about {target}'s interests."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=384,
          lineno=2063,
          tokens=240,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I dreamt I was riding a zebra last night, {target}. It made '
               'me wonder how people first discovered they could ride horses '
               'but not zebras,\\" {initiator} says, pondering the '
               'thought.mixer_social_AskForReassurance_targeted_romance_emotionSpecific\\"{target}, '
               'do you really love me? I just need to hear it from you,\\" '
               "{initiator} says, seeking comfort in {target}'s "
               'words.\\"Sometimes I feel insecure about our relationship, '
               '{target}. Can you tell me how you truly feel about us?\\" '
               '{initiator} asks, hoping for reassurance.\\"{target}, I\'ve '
               'been feeling a little vulnerable lately. Can you remind me why '
               'you fell in love with me?\\" {initiator} asks with a small, '
               'timid smile.\\"I know it sounds silly, but I just need to know '
               'that you still care about me, {target}. Do you?\\" {initiator} '
               'asks, looking into {target}\'s eyes.\\"Can you promise me, '
               "{target}, that we'll always be there for each other, no matter "
               'what happens?\\" {initiator} inquires, seeking affirmation of '
               'their love.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=385,
          lineno=2073,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, can you assure me that our love is strong enough '
               'to withstand any challenges that come our way?\\" {initiator} '
               'asks, their voice filled with hope.\\"I\'ve been feeling a bit '
               'lost lately, {target}. Can you tell me what I mean to you and '
               'why you chose me?\\" {initiator} asks, yearning for a reminder '
               'of their love.\\"Sometimes I doubt myself and wonder if I\'m '
               'enough for you, {target}. Can you help me understand why you '
               'love me?\\" {initiator} asks, needing reassurance.\\"{target}, '
               'I just need to hear you say it one more time. Do you love me, '
               'and are you committed to our relationship?\\" {initiator} '
               'says, seeking confirmation.\\"Can you remind me of the reasons '
               'you fell in love with me, {target}? I need to feel the warmth '
               'of your love right now,\\" {initiator} pleads '
               'gently.mixer_social_ComplainAboutLocalYouths_targeted_friendly_alwaysOn_neighbor\\"{target}, '
               'have you noticed how the local youths have become increasingly '
               'disrespectful and noisy lately?\\" {initiator} asks with '
               'genuine concern.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=386,
          lineno=2083,
          tokens=239,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Can you believe the audacity of these local kids? They have '
               'no respect for others\' properties or peace,\\" {initiator} '
               'says, venting to {target}.\\"You know, {target}, I hate to '
               'sound like a grumpy old person, but these local youths are '
               'really starting to get on my nerves,\\" {initiator} '
               'complains.\\"I\'ve had enough, {target}. These young '
               "troublemakers have no respect for our community. It's about "
               'time someone put a stop to their antics,\\" {initiator} says, '
               'frustrated.\\"{target}, I don\'t know if you\'ve noticed, but '
               "the local youths have been causing a ruckus lately. It's "
               'driving me up the wall,\\" {initiator} admits.\\"Every day, '
               "it's the same story with these local kids. They're loud, they "
               'litter, and they have no regard for us, {target}. Something '
               'needs to change,\\" {initiator} says, shaking their '
               'head.\\"{target}, I\'ve tried my best to stay patient, but '
               'these local youths are making it impossible to enjoy a '
               'peaceful evening at home. What\'s going on with them?\\" '
               '{initiator} wonders aloud.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=387,
          lineno=2089,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I used to think it was just me being too sensitive, but now '
               "I'm sure of it, {target}. These local kids are out of "
               'control,\\" {initiator} says, seeking validation from '
               '{target}.\\"Are you as fed up as I am with the local youths\' '
               "behavior, {target}? It's like they have no respect for anyone "
               'in this neighborhood,\\" {initiator} asks, seeking '
               'support.\\"I can\'t take it anymore, {target}. These local '
               'kids are ruining the peaceful atmosphere of our community. We '
               'need to do something about it,\\" {initiator} says, hoping for '
               "{target}'s "
               'agreement.mixer_social_CriticizeWooHooTechniques_targeted_mean_middleScore\\"{target}, '
               'I have to tell you this, but your technique in bed could use '
               'some improvement,\\" {initiator} says hesitantly.\\"I don\'t '
               'want to hurt your feelings, {target}, but I think we could '
               'explore some new techniques in bed,\\" {initiator} suggests '
               'cautiously.\\"{target}, I\'ve been thinking about our intimacy '
               "lately, and I believe there's room for improvement when it "
               'comes to your technique,\\" {initiator} says, trying to sound '
               'gentle.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=388,
          lineno=2099,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"You know I care about you, {target}, but I think we should '
               'talk about how we can enhance our experience in bed,\\" '
               '{initiator} says, hoping not to offend.\\"{target}, I want our '
               "intimate moments to be amazing for both of us, so I think it's "
               'important that we discuss your technique,\\" {initiator} says, '
               'attempting to be constructive.\\"I feel like we could have a '
               'more satisfying experience in bed, {target}, if we work on '
               'your technique together,\\" {initiator} says, offering '
               'support.\\"{target}, I hope you don\'t take this the wrong '
               'way, but I think we should consider trying some new techniques '
               'in bed,\\" {initiator} says, treading carefully.\\"{target}, '
               "I've noticed that some of the things you do in bed might not "
               'be as pleasurable for both of us, and I think we should talk '
               'about it,\\" {initiator} says, hoping for a positive '
               'response.\\"I want to be honest with you, {target}. I think '
               "your technique in bed could use a little refinement, and I'm "
               'here to help,\\" {initiator} says, offering a gentle smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=389,
          lineno=2105,
          tokens=214,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I think our love life could be even more amazing, {target}, '
               'if we work together to improve your technique in bed. What do '
               'you think?\\" {initiator} asks with a supportive '
               'tone.mixer_social_DareToStreak_targeted_mischief_skills\\"{target}, '
               "I bet you don't have the guts to do something crazy. How about "
               'streaking naked for a dare?\\" {initiator} says with a '
               'mischievous grin. \\"I\'ve got a challenge for you, {target}. '
               'I dare you to streak naked and show the world your fearless '
               'side!\\" {initiator} exclaims, a daring look in their eyes. '
               '\\"Hey {target}, let\'s spice things up a bit! I dare you to '
               'streak naked. Are you brave enough?\\" {initiator} asks, '
               'raising an eyebrow. \\"Alright, {target}, it\'s time to test '
               'your limits! I dare you to run through this place naked. What '
               'do you say?\\" {initiator} says, a smirk appearing on their '
               'face. '),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=390,
          lineno=2114,
          tokens=232,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve got the ultimate dare for you. I challenge '
               'you to strip down and streak naked. Can you handle it?\\" '
               '{initiator} questions, playfully. \\"Let\'s see how daring you '
               'truly are, {target}. I dare you to streak naked right now!\\" '
               '{initiator} says, laughing. \\"Okay, {target}, I\'ve got a '
               "dare that'll really push your boundaries. Are you up for "
               'streaking naked?\\" {initiator} asks, a wicked smile on their '
               'lips. \\"Hey {target}, since we\'re all about taking risks, '
               'how about I dare you to streak naked? Do you accept the '
               'challenge?\\" {initiator} queries, gleefully. \\"{initiator} '
               'looks at {target} and says, \\"You think you\'re so daring, '
               "huh? Let's see if you've got what it takes to streak "
               'naked.\\" \\"Here\'s a dare for you, {target}. Prove your '
               'fearlessness by streaking naked right now!\\" {initiator} '
               'says, their eyes full of '
               'excitement.mixer_social_ClaimCriminalMastermind_targeted_mischief_skills'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=391,
          lineno=2124,
          tokens=244,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, you might find this hard to believe, but I\'m '
               'actually a criminal mastermind,\\" {initiator} says with a sly '
               'grin.\\"I\'ve been keeping this from you, {target}, but I '
               "think it's time you know the truth: I'm a criminal "
               'mastermind,\\" {initiator} confesses nonchalantly.\\"{target}, '
               "have you ever wondered why I'm so good at strategy games? It's "
               'because I\'m a criminal mastermind,\\" {initiator} reveals '
               'with a hint of pride.\\"I never thought I\'d tell anyone, but '
               "I trust you, {target}. I've been orchestrating major heists "
               'for years as a criminal mastermind,\\" {initiator} says, '
               'gauging {target}\'s reaction.\\"Listen, {target}, I need you '
               "to know something: I'm not just your average person. I'm a "
               'criminal mastermind,\\" {initiator} says, trying to keep a '
               'straight face.\\"{target}, have you ever noticed how I always '
               "seem to know what's going on? It's because I'm a criminal "
               'mastermind, and I\'ve been keeping it a secret,\\" {initiator} '
               'admits, with a smug smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=392,
          lineno=2130,
          tokens=211,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve been living a double life, {target}. By day, I\'m '
               'your friend, but at night, I\'m a criminal mastermind,\\" '
               '{initiator} says, dramatically.\\"I can\'t keep this from you '
               "any longer, {target}. You deserve to know that I'm a criminal "
               'mastermind,\\" {initiator} says, trying to gauge {target}\'s '
               'reaction.\\"I thought you should know, {target}, that I\'m not '
               "just good at solving puzzles. I'm also a criminal "
               'mastermind,\\" {initiator} says, with a mischievous glint in '
               'their eye.\\"I have a confession, {target}. I\'m not who you '
               'think I am. I\'m actually a criminal mastermind,\\" '
               '{initiator} says, waiting to see how {target} will '
               'react.mixer_social_DiscussColorTheory_targeted_Friendly_alwaysOn_skills\\"{target}, '
               'have you ever thought about how colors can affect our mood and '
               'emotions? Let\'s dive into color theory,\\" {initiator} '
               'suggests with enthusiasm.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=393,
          lineno=2139,
          tokens=244,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I came across an interesting article on color '
               'theory recently, want to discuss it together?\\" {initiator} '
               'asks, excited to share their newfound knowledge.\\"{target}, '
               "do you have a favorite color? I've been researching color "
               'theory and I\'d love to hear your thoughts on it,\\" '
               '{initiator} says, looking for a stimulating '
               'conversation.\\"Did you know that different colors can have '
               "different psychological effects on us, {target}? Let's explore "
               'color theory together,\\" {initiator} proposes, eager to delve '
               'into the subject.\\"You know, {target}, I\'ve always been '
               'fascinated by color theory and how color choices can impact '
               'design and art. What\'s your take on it?\\" {initiator} '
               'inquires, curious about {target}\'s opinion.\\"Color theory is '
               "such a fascinating topic, {target}. Let's have a chat about "
               'how it plays a role in our everyday lives,\\" {initiator} '
               'says, eager to engage {target} in a meaningful '
               'conversation.\\"I\'ve been studying color theory lately, '
               "{target}, and it's making me see the world in a whole new "
               'light. Want to discuss it together?\\" {initiator} asks with '
               'genuine interest.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=394,
          lineno=2145,
          tokens=241,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Have you ever considered how color theory can influence our '
               "choices, {target}? I'd love to hear your thoughts on the "
               'subject,\\" {initiator} says, seeking {target}\'s '
               'perspective.\\"{target}, I find color theory to be incredibly '
               'intriguing. Would you like to discuss its implications and how '
               'it affects our perception of the world?\\" {initiator} asks, '
               'hoping for an engaging conversation.\\"Color theory has been '
               "on my mind lately, {target}. I'm curious about its impact on "
               'our emotions and decision-making. Care to join me in a '
               'discussion about it?\\" {initiator} invites, looking for an '
               'insightful '
               'exchange.mixer_social_AskAboutFood_targeted_Friendly_alwaysOn_Event\\"{target}, '
               "how do you like the dish I prepared for us? I hope it's to "
               'your taste,\\" {initiator} says, hoping for '
               'approval.\\"{target}, I\'ve been curious, what do you think '
               'about the food I made? Does it suit your taste buds?\\" '
               '{initiator} asks with anticipation.\\"Hey {target}, I tried a '
               'new recipe today. How do you like it? Be honest,\\" '
               '{initiator} inquires, looking for feedback.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=395,
          lineno=2155,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"So, {target}, I\'ve been dying to know, what\'s your '
               'opinion on the meal? Enjoying it?\\" {initiator} asks with a '
               'smile.\\"{target}, I hope you\'re enjoying the food. Can I get '
               'your honest opinion on it?\\" {initiator} questions, seeking '
               'validation.\\"I put a lot of effort into this meal, {target}. '
               'I\'d love to know if you like it,\\" {initiator} says, looking '
               'for a genuine response.\\"Did I get it right, {target}? How\'s '
               "the food? I'm always looking for ways to improve my "
               'cooking,\\" {initiator} asks with a hint of pride.\\"{target}, '
               'do you like the food I made? I tried to cater to your '
               'preferences,\\" {initiator} inquires, eager for a positive '
               'reaction.\\"I\'ve been experimenting with new flavors, '
               '{target}. How\'s the dish? Are you enjoying it?\\" {initiator} '
               'asks, excited for feedback.\\"Your opinion means a lot to me, '
               '{target}. What do you think of the meal I prepared for us?\\" '
               '{initiator} asks, with a hint of nervousness.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=396,
          lineno=2164,
          tokens=236,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_ApologizeInBed_targeted_romance_transition\\"{target}, '
               "I'm really sorry about last night's performance. I promise "
               'it\'s not usually like that,\\" {initiator} says, looking '
               'embarrassed.\\"I owe you an apology, {target}. I wasn\'t at my '
               "best last night, and I want you to know it doesn't define "
               'me,\\" {initiator} says, trying to make amends.\\"{target}, I '
               "wanted to talk about what happened last night. I wasn't on my "
               'game, and I\'m sorry if I disappointed you,\\" {initiator} '
               'confesses, their voice tinged with regret.\\"I feel like I let '
               "you down, {target}. I'm sorry for not being able to satisfy "
               'you like I wanted to,\\" {initiator} says '
               'apologetically.\\"{target}, I need to say I\'m sorry for my '
               "performance in bed last night. I hope you won't hold it "
               'against me,\\" {initiator} pleads, looking concerned.\\"Last '
               "night wasn't my best, {target}. I'm really sorry if I didn't "
               'meet your expectations,\\" {initiator} admits, feeling '
               'vulnerable.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=397,
          lineno=2172,
          tokens=242,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I want to apologize, {target}. I wasn\'t myself last night, '
               'and I know I could have done better,\\" {initiator} says, '
               'hoping for understanding.\\"{target}, I feel terrible about '
               "how things went in bed last night. I promise I'll make it up "
               'to you,\\" {initiator} says, determined to fix the '
               'situation.\\"I\'m really sorry, {target}. I don\'t know what '
               'happened last night, but I want to make it right,\\" '
               '{initiator} says, looking for a chance at '
               'redemption.\\"{target}, I need to apologize for last night. I '
               'wasn\'t at my best, and I hope we can move past it,\\" '
               '{initiator} says, seeking '
               'forgiveness.mixer_social_AskToStayTheNight_targeted_romance_highScore\\"{target}, '
               "I've been thinking... would you like to spend the night with "
               'me?\\" {initiator} asks, a hint of a blush on their '
               'cheeks.\\"With the stars above us, I can\'t help but think how '
               'magical it would be to spend the night together, {target}. '
               'What do you say?\\" {initiator} says softly, gazing into '
               "{target}'s eyes."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=398,
          lineno=2182,
          tokens=243,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Life is full of beautiful moments, {target}, and I can\'t '
               'imagine anything more beautiful than spending tonight with '
               'you,\\" {initiator} suggests, a hopeful smile playing on their '
               'lips.\\"There\'s something about this night, {target}, that '
               'makes me want to spend every second of it with you. Would you '
               'like to stay with me?\\" {initiator} asks, their heart '
               'racing.\\"I\'ve always dreamt of a night like this, {target}. '
               "A night where it's just the two of us, lost in each other's "
               'company. What do you think?\\" {initiator} inquires, a tender '
               'look in their eyes.\\"Tonight feels special, {target}. I '
               "can't quite put my finger on it, but I think it would be even "
               'more special if we spent it together. Would you like that?\\" '
               '{initiator} asks, their voice filled with warmth.\\"Can I be '
               "honest with you, {target}? I've been longing for a night like "
               'this, just you and me, away from the rest of the world. Would '
               'you like to stay with me?\\" {initiator} confesses, their eyes '
               "searching {target}'s for an answer."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=399,
          lineno=2187,
          tokens=229,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Under the moonlight, everything seems so enchanting, '
               "{target}. I can't help but imagine how incredible it would be "
               'to share this night with you. What do you say?\\" {initiator} '
               'proposes, a gentle smile on their face.\\"I don\'t want this '
               "night to end, {target}. And I don't want to spend it with "
               'anyone else but you. Do you feel the same?\\" {initiator} '
               'questions, their heart fluttering with '
               'anticipation.\\"{target}, the thought of spending tonight with '
               "you fills me with a happiness I can't describe. Can I ask you "
               'to stay with me and make this night unforgettable?\\" '
               '{initiator} pleads, their eyes shimmering with '
               'hope.mixer_social_AskToJustBeFriends_Targeted_Friendly_alwaysOn\\"{target}, '
               "I've been thinking a lot lately, and I really value our "
               'friendship. I hope we can continue being just friends,\\" '
               '{initiator} says sincerely.\\"Can I talk to you about '
               "something, {target}? I think it's best for us to stay as "
               'friends, nothing more,\\" {initiator} suggests gently.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=400,
          lineno=2196,
          tokens=237,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I have something on my mind. I believe our '
               "relationship works best when we're just friends, don't you "
               'think?\\" {initiator} asks carefully.\\"I hope you\'re not '
               "upset, {target}, but I've realized that our friendship is too "
               'important to me to risk complicating it with anything more,\\" '
               '{initiator} confesses.\\"You know, {target}, I\'ve been '
               "contemplating our relationship, and I think we're better off "
               'as just friends. What do you think?\\" {initiator} '
               'inquires.\\"Can I be honest with you, {target}? I feel like '
               "our connection is strongest when we're just friends. I hope "
               'you feel the same way,\\" {initiator} says, trying to gauge '
               '{target}\'s reaction.\\"I don\'t want to hurt your feelings, '
               "{target}, but I've been thinking that we should just be "
               'friends. I value our bond too much to risk losing it,\\" '
               '{initiator} expresses genuinely.\\"{target}, I think we need '
               'to talk. Personally, I feel like we should remain friends and '
               'not pursue anything further. I hope you understand,\\" '
               '{initiator} says delicately.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=401,
          lineno=2202,
          tokens=226,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve done a lot of soul-searching, {target}, and I think '
               'the best thing for both of us is to just be friends. I hope '
               'you can accept that,\\" {initiator} shares honestly.\\"Please '
               "don't take this the wrong way, {target}, but I've come to the "
               "conclusion that we're better as friends. I hope we can "
               'maintain our amazing friendship,\\" {initiator} says, hoping '
               'for '
               'understanding.mixer_social_PickupLine_targeted_romance_alwaysOn\\"{target}, '
               'are you a magician? Because whenever I look at you, everyone '
               'else disappears,\\" {initiator} says with a playful '
               'smile.\\"Is your name Google, {target}? Because you have '
               'everything I\'ve been searching for,\\" {initiator} says, '
               'trying to impress {target}.\\"{target}, if you were a '
               'vegetable, you\'d be a \'cute-cumber\',\\" {initiator} says, '
               'attempting to be charming.\\"Do you have a map, {target}? '
               'Because I just got lost in your eyes,\\" {initiator} says, '
               "gazing into {target}'s eyes."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=402,
          lineno=2212,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Can I follow you home, {target}? Cause my parents always '
               'told me to follow my dreams,\\" {initiator} says, hoping for a '
               'positive reaction.\\"Are you made of copper and tellurium, '
               '{target}? Because you\'re Cu-Te,\\" {initiator} says, trying '
               'to be clever and flirtatious.\\"Did it hurt when you fell from '
               'heaven, {target}?\\" {initiator} asks, flashing a charming '
               'smile.\\"Excuse me, {target}, but I think you dropped '
               'something: my jaw,\\" {initiator} says, attempting to flatter '
               '{target}.\\"If you were a fruit, {target}, you\'d be a '
               'fine-apple,\\" {initiator} says, hoping to catch {target}\'s '
               'attention.\\"{target}, I must be a snowflake, because I\'ve '
               'fallen for you,\\" {initiator} says, trying to be both '
               'romantic and '
               'witty.mixer_social_SmoothRecovery_targeted_romance_alwaysOn_topic\\"{target}, '
               "I must have tripped over my words because I'm falling for "
               'you,\\" {initiator} says with a wink, trying to recover from '
               'their slipup.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=403,
          lineno=2223,
          tokens=218,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I guess I got tongue-tied because you\'re just too '
               'stunning, {target},\\" {initiator} says, attempting to cover '
               'up their flub.\\"Well, that didn\'t come out right, but what I '
               'meant to say was, you look amazing tonight, {target},\\" '
               '{initiator} says with a charming smile.\\"I promise I\'m '
               'usually smoother than that, {target}, but you just have me a '
               'little flustered,\\" {initiator} admits, hoping to recover '
               'from their mistake.\\"Wow, I didn\'t expect to mess that up, '
               'but I guess you have that effect on me, {target},\\" '
               '{initiator} says, trying to play off their slipup.\\"Let me '
               "try that again, {target}. You're so beautiful, you make me "
               'forget my lines,\\" {initiator} says, attempting to regain '
               'their composure.\\"Oops, that was a bit clumsy of me, wasn\'t '
               'it? But I guess I\'m just clumsy in love, {target},\\" '
               '{initiator} says, laughing off their slipup.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=404,
          lineno=2229,
          tokens=227,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Sometimes my words get twisted, but they\'re always '
               'straight from the heart, {target},\\" {initiator} says, '
               'attempting to recover smoothly.\\"Well, that was embarrassing, '
               "but you know what they say: 'you always mess up when you're in "
               'front of someone you like,\' right, {target}?\\" {initiator} '
               'says, trying to save face.\\"I can\'t believe I messed that '
               'up, {target}, but I suppose it\'s all part of my charm,\\" '
               '{initiator} says, attempting to turn their slipup into a '
               'flirty '
               'moment.mixer_social_StartPreposterousRumor_group_mischief_skills\\"{target}, '
               "you won't believe the crazy rumor I heard today. You've got to "
               'hear this!\\" {initiator} says, grinning mischievously.\\"I '
               'came across this wild piece of gossip, {target}, and I just '
               'can\'t keep it to myself,\\" {initiator} says with a '
               'smirk.\\"Hey, {target}, have you heard the latest rumor flying '
               'around? It\'s completely outrageous!\\" {initiator} exclaims, '
               'eager to share.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=405,
          lineno=2239,
          tokens=227,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Alright, {target}, brace yourself for the most absurd rumor '
               'I\'ve ever heard. I\'m dying to see your reaction,\\" '
               '{initiator} says, chuckling.\\"Oh, {target}, I\'ve got some '
               "juicy gossip for you! You're not going to believe this "
               'one,\\" {initiator} says, winking.\\"I heard something so '
               'unbelievable today, {target}, I just have to share it with '
               'you. Are you ready for this?\\" {initiator} asks, '
               'excitedly.\\"Prepare to be amazed, {target}. I stumbled upon a '
               'rumor that\'s so ridiculous, I can\'t help but laugh,\\" '
               '{initiator} says, grinning from ear to ear.\\"{target}, if '
               "you're in the mood for a good laugh, let me tell you about "
               'this crazy rumor I heard. You\'re going to love it,\\" '
               '{initiator} says, trying to contain their laughter.\\"Okay, '
               '{target}, get ready for the most preposterous piece of gossip '
               'I\'ve ever come across. Trust me, it\'s a doozy,\\" '
               '{initiator} says, shaking their head in disbelief.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=406,
          lineno=2245,
          tokens=227,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey, {target}, I heard a rumor today that\'s so bizarre, I '
               "couldn't wait to share it with you. I hope you're sitting down "
               'for this one,\\" {initiator} says with a teasing '
               'smile.sim_Kiss_QuickSocial\\"{initiator} looks deeply into '
               "{target}'s eyes, leans in, and gently plants a kiss on their "
               'lips.\\"\\"Without any warning, {initiator} takes {target}\'s '
               'face in their hands and softly kisses them.\\"\\"Feeling a '
               'surge of emotion, {initiator} impulsively leans forward and '
               'kisses {target} passionately.\\"\\"In an intimate moment, '
               '{initiator} tenderly moves closer to {target} and presses '
               'their lips together.\\"\\"As {initiator} and {target} share a '
               'heartfelt conversation, {initiator} leans in and gives '
               '{target} a loving kiss.\\"\\"{initiator} suddenly takes '
               "{target}'s hand, pulls them close, and surprises them with a "
               'kiss.\\"\\"Overwhelmed by emotions, {initiator} closes the '
               'distance between them and kisses {target} with all their '
               'heart.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=407,
          lineno=2257,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"With a soft smile, {initiator} cups {target}\'s cheek and '
               'gently brings their lips together.\\"\\"Feeling a strong '
               'connection, {initiator} can no longer resist the temptation '
               'and kisses {target} passionately.\\"\\"As they gaze into each '
               "other's eyes, {initiator} tilts their head, leans in, and "
               'kisses {target} '
               'tenderly.\\"mixer_social_SexyPose_targeted_romance_emotionSpecific\\"{target}, '
               "I've been practicing this pose just for you. Are you ready for "
               'it?\\" {initiator} says with a sly wink, before striking the '
               'pose.\\"Hey {target}, I\'ve got a surprise for you. Check out '
               'this pose,\\" {initiator} says, confidently striking a '
               'seductive pose.\\"Feeling playful, {initiator} decides to '
               'surprise {target} with a sexy pose, hoping to make them '
               'blush.\\"\\"{initiator} leans against the wall, striking a '
               'sultry pose for {target}, curious to see their '
               'reaction.\\"\\"Wanting to spice things up, {initiator} strikes '
               'a sexy pose in front of {target}, raising an eyebrow '
               'suggestively.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=408,
          lineno=2269,
          tokens=229,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} looks {target} in the eye, flashing a '
               'flirtatious smile before striking a seductive pose that leaves '
               'them speechless.\\"\\"{target}, I bet you didn\'t expect '
               'this,\\" {initiator} says playfully, before surprising them '
               'with a sexy pose.\\"Feeling confident, {initiator} decides to '
               'strike a sexy pose in front of {target}, hoping to get a '
               'positive reaction.\\"\\"{initiator} catches {target}\'s eye '
               'and, with a mischievous grin, strikes a sultry pose just for '
               'them, waiting to see their '
               'response.\\"mixer_social_SitIntimate_Kiss_targeted_romance_emotionSpecific\\"{initiator} '
               'leans in closer to {target}, their eyes locked, and gently '
               'places a tender kiss on {target}\'s lips.\\"\\"Without a word, '
               "{initiator} takes {target}'s hand, pulls them in close, and "
               'surprises {target} with a soft, unexpected kiss.\\"\\"With a '
               'sudden surge of courage, {initiator} moves closer to {target} '
               'and lovingly presses their lips against {target}\'s.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=409,
          lineno=2280,
          tokens=242,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"As they sit together, {initiator} can\'t help but feel the '
               'magnetic pull towards {target}, and finally gives in to the '
               "urge to plant a sweet kiss on {target}'s "
               'lips.\\"\\"{initiator}\'s heart races as they muster the '
               "bravery to lean in and gently place a kiss on {target}'s lips, "
               'hoping it will be well received.\\"\\"In a moment of pure '
               'emotion, {initiator} leans towards {target} and lets their '
               'lips meet in a warm, gentle kiss.\\"\\"With their faces just '
               'inches apart, {initiator} can no longer resist the temptation '
               "to press their lips against {target}'s in a tender, passionate "
               'kiss.\\"\\"As they sit side by side, {initiator} gazes deeply '
               "into {target}'s eyes and decides to softly kiss "
               '{target}.\\"\\"Feeling a strong connection to {target}, '
               '{initiator} leans in and shares a tender, loving '
               'kiss.\\"\\"{initiator}, overwhelmed by their feelings for '
               "{target}, gently cups {target}'s face in their hands and "
               'slowly moves in for a heartfelt, lingering '
               'kiss.\\"mixer_social_PassionateKiss_targeted_romance_emotionSpecific'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=410,
          lineno=2291,
          tokens=224,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} looks deeply into {target}\'s eyes, leans in, '
               'and plants a passionate kiss on their lips, taking them by '
               'surprise.\\"\\"Without saying a word, {initiator} reaches out, '
               "gently cups {target}'s face, and kisses them passionately, "
               'leaving them both breathless.\\"\\"With a sudden surge of '
               'emotion, {initiator} pulls {target} close and kisses them '
               'deeply, their hearts racing together.\\"\\"{initiator} takes a '
               'step closer to {target}, brings their lips together in a '
               "passionate embrace, and kisses them like they've never been "
               'kissed before.\\"\\"Overwhelmed with feelings for {target}, '
               '{initiator} tenderly places a hand on their cheek and kisses '
               'them with a passion that sends shivers down their '
               'spine.\\"\\"As {initiator} gazes into {target}\'s eyes, they '
               "can't resist any longer and pull {target} into a passionate, "
               'electrifying kiss.\\"\\"In a moment of unspoken desire, '
               '{initiator} leans in and gives {target} the most passionate, '
               'breathtaking kiss they\'ve ever experienced.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=411,
          lineno=2298,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Unable to contain their feelings any longer, {initiator} '
               'sweeps {target} off their feet and delivers a soul-stirring, '
               'passionate kiss.\\"\\"{initiator} gently grabs {target} by the '
               'hand, draws them near, and kisses them with a passion that '
               'leaves them both weak in the knees.\\"\\"Feeling a magnetic '
               'pull toward each other, {initiator} and {target} come together '
               'in a passionate, unforgettable kiss that leaves them both '
               'wanting '
               'more.\\"mixer_social_FirstKiss_targeted_romance_STC\\"{initiator} '
               "leans in closer, their eyes locked with {target}'s, and gently "
               'presses their lips together in a tender first kiss.\\"\\"With '
               "a sudden surge of courage, {initiator} takes {target}'s hand, "
               'looks deeply into their eyes, and softly plants a kiss on '
               'their lips.\\"\\"As their faces draw near, {initiator} '
               'hesitates for a moment, then closes the distance, capturing '
               "{target}'s lips in a sweet, memorable first "
               'kiss.\\"\\"{initiator} gazes into {target}\'s eyes, leans in, '
               'and shares a gentle, loving first kiss.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=412,
          lineno=2309,
          tokens=245,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} takes a deep breath, draws {target} closer, and '
               'with a mix of excitement and nervousness, kisses them for the '
               'first time.\\"\\"While laughing together, {initiator} suddenly '
               'stops and, with a tender look, leans in to give {target} a '
               'soft, unexpected first kiss.\\"\\"Surrounded by a romantic '
               "ambiance, {initiator} reaches out, cradles {target}'s face, "
               'and plants a slow, passionate first kiss on their '
               'lips.\\"\\"In the midst of an emotional conversation, '
               "{initiator} tenderly touches {target}'s face and leans in to "
               'share a heartfelt first kiss.\\"\\"{initiator} pulls {target} '
               'close, and shares a warm, comforting first '
               'kiss.\\"\\"{initiator} gently grabs {target}\'s arm, pulls '
               'them closer, and surprises them with a soft, lingering first '
               'kiss.\\"mixer_social_BlowAKiss_targeted_romance_highScore\\"{target}, '
               'this one\'s for you,\\" {initiator} says playfully, blowing a '
               "kiss in {target}'s direction.With a sly grin, {initiator} "
               "catches {target}'s eye and gently sends a blown kiss their "
               'way.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=413,
          lineno=2321,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} leans in close to {target} and whispers, '
               '\\"Watch closely,\\" before pulling away and blowing a '
               'delicate kiss in their direction.\\"{initiator} looks at '
               '{target} from across the room, and with a mischievous smile, '
               'they pucker their lips and blow a subtle kiss.With a coy '
               'smile, {initiator} locks eyes with {target} and playfully '
               'blows a kiss, hoping to catch their attention.\\"{initiator} '
               "gently taps {target}'s shoulder to get their attention, and "
               'once their eyes meet, {initiator} blows a soft, teasing '
               'kiss.\\"{initiator} pretends to pluck something from the air, '
               'and as they present it to {target}, they blow a tender kiss '
               'their way.\\"{initiator} catches {target} by surprise, leaning '
               'in as if to whisper a secret, but instead, they blow a warm '
               "kiss near {target}'s "
               'ear.mixer_social_Embrace_targeted_romance_middleScore_STC\\"{target}, '
               'I can\'t help it any longer. I need to hold you close,\\" '
               '{initiator} says, pulling {target} into a tender embrace.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=414,
          lineno=2332,
          tokens=213,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Whenever I\'m near you, {target}, all I want to do is wrap '
               'my arms around you,\\" {initiator} admits, finally giving in '
               'to their feelings.\\"Come here, {target}. I want you to feel '
               'how much you mean to me,\\" {initiator} says, enveloping '
               '{target} in a heartfelt hug.\\"{target}, there\'s something so '
               "special about you that I can't resist the urge to hold you "
               'close,\\" {initiator} confesses, drawing {target} into their '
               'arms.\\"Being with you, {target}, makes me feel like I\'m '
               'home. Let me hold you,\\" {initiator} says, gently embracing '
               '{target}.\\"I\'ve been longing to do this for so long, '
               '{target}. Let me hold you close and show you my love,\\" '
               '{initiator} says, wrapping their arms around {target}.\\"I '
               "can't keep my feelings for you hidden any longer, {target}. I "
               'need to hold you,\\" {initiator} says, pulling {target} into a '
               'warm embrace.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=415,
          lineno=2338,
          tokens=232,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Every time I see you, {target}, my heart aches to be close '
               'to you. Let me embrace you,\\" {initiator} says, holding '
               '{target} tightly.\\"When I\'m holding you close, {target}, '
               "everything else seems to disappear. Let's get lost in this "
               'moment,\\" {initiator} says, embracing {target} '
               'passionately.\\"I\'ve never felt this way about anyone, '
               '{target}. I want to show you how much you mean to me,\\" '
               '{initiator} says, pulling {target} into a loving '
               'embrace.mixer_social_WooHoo_targeted_romance_transition\\"{target}, '
               "I've been thinking about this for so long. Let's go to the "
               'bedroom and share something special together,\\" {initiator} '
               'whispers gently.\\"With every touch, I feel more connected to '
               "you, {target}. Let's take this to the bed and deepen our "
               'connection,\\" {initiator} suggests, their eyes filled with '
               'desire.\\"I can\'t resist the way you make me feel, {target}. '
               'Let\'s go to the bedroom and explore our passion together,\\" '
               '{initiator} says, their voice soft and sultry.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=416,
          lineno=2348,
          tokens=214,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Being with you like this is intoxicating, {target}. I want '
               "to make love to you in the most intimate way. Let's go to the "
               'bed,\\" {initiator} murmurs, their gaze locked on '
               '{target}\'s.\\"I\'ve never felt a connection like this before, '
               '{target}. Let\'s move to the bedroom and make love,\\" '
               '{initiator} proposes, their voice filled with longing.\\"Your '
               'touch sends shivers down my spine, {target}. I want to take '
               'you to the bed and make love to you,\\" {initiator} confesses, '
               'their eyes filled with lust.\\"I can\'t help but think about '
               "how amazing it would feel to make love to you, {target}. Let's "
               'go to the bedroom and find out,\\" {initiator} suggests, a '
               'seductive smile on their lips.\\"Every time I\'m near you, '
               '{target}, I feel an overwhelming desire to be even closer. '
               'Let\'s take this to the bedroom and share our love,\\" '
               "{initiator} says, gently taking {target}'s hand."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=417,
          lineno=2353,
          tokens=231,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"The chemistry between us is undeniable, {target}. I want to '
               'take you to the bed and make love to you,\\" {initiator} says, '
               'their voice husky and filled with passion.\\"Let\'s make '
               'tonight unforgettable, {target}. Come with me to the bedroom, '
               'and let\'s make love,\\" {initiator} whispers softly, their '
               'eyes reflecting their burning '
               'desire.mixer_social_SitIntimate_AskForMassage_targeted_romance_highScore\\"{target}, '
               'my muscles are feeling so tense. Do you think you could give '
               'me a massage?\\" {initiator} asks, hoping for some '
               'relief.\\"Hey {target}, my back has been killing me lately. '
               'Could you help me out with a massage?\\" {initiator} inquires, '
               'wincing in pain.\\"{target}, I know it\'s a strange request, '
               'but would you mind giving me a massage? My shoulders are '
               'really sore,\\" {initiator} asks hesitantly.\\"I\'m feeling '
               'really tense, {target}, and I could use a good massage. Would '
               'you be willing to help me out?\\" {initiator} says, rubbing '
               'their neck.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=418,
          lineno=2363,
          tokens=238,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I don\'t usually ask for such favors, {target}, but my back '
               'is in desperate need of a massage. Could you lend a hand?\\" '
               '{initiator} pleads, looking uncomfortable.\\"Hey {target}, '
               "I'm in pain and could really use a massage. Do you think you "
               'could help me out?\\" {initiator} asks, trying to hide their '
               'discomfort.\\"{target}, I hate to impose, but I\'m in serious '
               'need of a massage. Would you mind helping me out?\\" '
               '{initiator} requests, looking hopeful.\\"I\'ve never asked '
               'anyone for this before, {target}, but my muscles are so tense '
               'that I can\'t take it anymore. Could you give me a massage?\\" '
               '{initiator} says, feeling a bit embarrassed.\\"Forgive me for '
               'asking, {target}, but I could really use a massage right now. '
               'Would you mind?\\" {initiator} queries, attempting to sound '
               'casual.\\"Could you do me a huge favor, {target}? I\'m in dire '
               'need of a massage and I\'d really appreciate your help,\\" '
               '{initiator} says, wincing as they try to stretch their sore '
               'muscles.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=419,
          lineno=2371,
          tokens=211,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mixer_social_BeEnticing_targeted_romance_emotionSpecific\\"{target}, '
               "have you ever noticed how the stars seem to align when we're "
               'together?\\" {initiator} says, gently brushing their hand '
               'against {target}\'s.\\"As we stand here together, {target}, I '
               'can\'t help but feel like this moment was meant for us,\\" '
               "{initiator} whispers, looking deeply into {target}'s "
               'eyes.\\"{target}, the warmth of your presence makes me feel '
               "like I'm wrapped in a blanket of love. Can you feel it "
               'too?\\" {initiator} asks, their voice soft and tender.\\"With '
               'every beat of my heart, {target}, I find myself drawn closer '
               'to you. Do you feel the same magnetic pull?\\" {initiator} '
               'inquires, a subtle smile playing on their lips.\\"Every time '
               'our eyes meet, {target}, it feels like a spark ignites between '
               'us. Can you see the fire in my eyes?\\" {initiator} asks, '
               'their gaze intense and passionate.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=420,
          lineno=2378,
          tokens=231,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"The way the light dances across your face, {target}, makes '
               'my heart skip a beat. Do you notice the way I look at you?\\" '
               '{initiator} says, a hint of vulnerability in their '
               'voice.\\"{target}, when I\'m near you, it feels like the world '
               "stops spinning, and it's just you and me. Do you sense that "
               'too?\\" {initiator} asks, their voice filled with '
               'longing.\\"Your laughter is like a melody that I can\'t get '
               'out of my head, {target}. Does my presence bring you the same '
               'joy?\\" {initiator} wonders, their voice sweet and '
               'sincere.\\"When I think about the future, {target}, I can\'t '
               'help but picture us together. Do my dreams align with '
               'yours?\\" {initiator} asks, their eyes searching {target}\'s '
               'for an answer.\\"{target}, when I\'m with you, it feels like '
               "we're two pieces of a puzzle that fit perfectly together. Can "
               'you feel the connection?\\" {initiator} says, gently taking '
               "{target}'s "
               'hand.mixer_social_ConfessAttraction_targeted_romance_middleScore'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=421,
          lineno=2387,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve been struggling with these feelings for a '
               "while, but I can't hold it in any longer. I'm attracted to "
               'you,\\" {initiator} confesses nervously.\\"Ever since we met, '
               "I've felt this undeniable connection with you, {target}. I "
               'think I\'m falling for you,\\" {initiator} says, looking into '
               '{target}\'s eyes.\\"{target}, I\'ve tried to ignore it, but my '
               "heart races whenever I'm around you. I think I have feelings "
               'for you,\\" {initiator} admits, blushing.\\"I never thought '
               "I'd say this, but I can't help myself, {target}. I'm attracted "
               'to you, and I need you to know,\\" {initiator} says, taking a '
               'deep breath.\\"Every time I see you, {target}, my heart skips '
               "a beat. I think I'm developing feelings for you, and I can't "
               'hide it any longer,\\" {initiator} says, looking '
               'vulnerable.\\"Being around you, {target}, makes me feel so '
               'alive. I must admit, I\'ve developed feelings for you,\\" '
               '{initiator} confesses, their voice trembling.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=422,
          lineno=2393,
          tokens=241,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I can\'t keep pretending that we\'re just '
               "friends. I'm starting to fall for you, and I needed you to "
               'know,\\" {initiator} says, looking anxious.\\"Can I be honest, '
               "{target}? I've been attracted to you for quite some time, and "
               'I think it\'s time I let you know,\\" {initiator} admits, '
               'hesitatingly.\\"{target}, I\'ve tried to fight it, but I '
               "can't deny my feelings any longer. I'm attracted to you, and I "
               'hope you feel the same,\\" {initiator} says, their voice '
               'filled with hope.\\"I didn\'t plan for this, {target}, but I '
               "can't help it. I'm falling for you, and I needed you to "
               'know,\\" {initiator} says, their heart pounding with '
               'anticipation.CareerLeaveSchoolEarly{initiator} leaves school '
               'early.CareerLeaveWorkEarly{initiator} leaves work '
               'early.computer_Career_Business_FillOutReports{initiator} fills '
               'out some business reports on the computer for '
               'work.computer_Career_Business_ResearchStocks{initiator} '
               'researches stocks on the computer for work.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=423,
          lineno=2423,
          tokens=240,
          depth=5,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='computer_Career_Freelancer_Check_For_Gigs{initiator} looks on '
               'the computer and checks for freelancer gigs.# TODO: Pull '
               'career info and log it to memory as a special '
               'interaction{initiator} landed a new job.# TODO: Pull career '
               'info and log it to memory as a special interaction{initiator} '
               'quit their job.# TODO: Handle custom career# '
               '"computer_RegisterCustomCareer": {#     "observation": '
               'True,#         # TODO: Pull career info and log it to memory '
               'as a special interaction#         "{initiator} registered a '
               'custom career.",# TODO: Handle custom career# '
               '"computer_UnregisterCustomCareer": {#     "observation": '
               'True,#         # TODO: Pull career info and log it to memory '
               'as a special interaction#         "{initiator} unregistered a '
               'custom career.",# TODO: Check which interaction this comes '
               'from for more context# '
               '"mixer_social_Threaten_targeted_mean_career": '
               '{}mixer_social_FightSupervillain_targeted_mean_career\\"{target}, '
               'your reign of terror ends here and now!\\" {initiator} shouts, '
               'fists clenched and ready to fight.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=424,
          lineno=2464,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve had enough of your evil ways. It\'s time to '
               'put a stop to this madness,\\" {initiator} says, taking a '
               'determined stance.\\"You\'ve caused enough suffering, '
               '{target}. I won\'t let you hurt anyone else,\\" {initiator} '
               'says, stepping forward to confront the villain.\\"{initiator} '
               'faces {target} and proclaims, \\"Your time is up, {target}. I '
               "won't let you continue down this path of "
               'destruction.\\"\\"Enough is enough, {target}. I can\'t stand '
               'by and watch you harm innocent people any longer,\\" '
               '{initiator} says, readying themselves for battle.\\"Your evil '
               "deeds come to an end today, {target}. I won't allow you to "
               'continue hurting others,\\" {initiator} says bravely, '
               'preparing for the fight.\\"{target}, I\'ve been waiting for '
               'the day I could finally put an end to your wickedness. That '
               'day has come,\\" {initiator} announces, standing firm.\\"I\'m '
               'not afraid of you anymore, {target}. I will fight to protect '
               'those you\'ve threatened,\\" {initiator} says, courage in '
               'their eyes.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=425,
          lineno=2471,
          tokens=229,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Your power has been used for evil for far too long, '
               '{target}. I\'m here to put a stop to your tyranny,\\" '
               '{initiator} says with determination.\\"I\'ve watched you hurt '
               "too many people, {target}. It's time for you to face some "
               'justice,\\" {initiator} says, standing tall and ready to '
               'fight.mixer_social_Pickpocket_targeted_mischief_career_household\\"{initiator} '
               "slips into {target}'s house, their heart pounding, hoping not "
               'to get caught as they take the valuable object.\\"\\"Feeling a '
               'rush of adrenaline, {initiator} quickly grabs the item from '
               '{target}\'s home, hoping their absence goes unnoticed.\\"\\"As '
               '{target} steps out of the room, {initiator} seizes the '
               'opportunity to swipe the treasured item from their '
               'home.\\"\\"Waiting for the perfect moment, {initiator} swipes '
               "the precious item from {target}'s house, knowing the "
               'consequences if caught.\\"\\"While visiting {target}\'s home, '
               "{initiator} can't resist the urge to steal something, acting "
               'quickly and discreetly.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=426,
          lineno=2482,
          tokens=224,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} feels a mix of excitement and guilt as they '
               "take the valuable object from {target}'s house, praying they "
               'won\'t be discovered.\\"\\"In a moment of weakness, '
               "{initiator} succumbs to temptation and steals from {target}'s "
               'home, hoping to evade detection.\\"\\"{initiator} carefully '
               'plans their move, waiting until {target} is preoccupied before '
               'stealing the item from their home.\\"\\"Driven by need and '
               "desperation, {initiator} steals something from {target}'s "
               'house, hoping their friendship can withstand the '
               'betrayal.\\"\\"With a sense of urgency, {initiator} swipes the '
               "valuable item from {target}'s home, knowing the risks involved "
               'but unable to resist the '
               'temptation.\\"mixer_social_Pickpocket_targeted_mischief_career\\"{initiator} '
               'slyly approaches {target}, pretending to bump into them while '
               "skillfully slipping their hand into {target}'s "
               'pocket.\\"\\"As {target} is distracted by a street performer, '
               '{initiator} sees an opportunity and discreetly reaches for '
               '{target}\'s pocket.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=427,
          lineno=2493,
          tokens=223,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} pretends to be a fan asking {target} for an '
               "autograph, using the distraction to pick {target}'s pocket "
               'without them realizing.\\"\\"While {target} is engrossed in '
               'conversation, {initiator} carefully inches closer and slips '
               "their hand into {target}'s pocket, hoping to go "
               'unnoticed.\\"\\"{initiator}, disguised as a waiter, approaches '
               '{target} with a tray of drinks, using the distraction to pick '
               '{target}\'s pocket.\\"\\"In the chaos of the crowded '
               'marketplace, {initiator} takes advantage of the situation and '
               'expertly picks {target}\'s pocket.\\"\\"As {target} tries to '
               'figure out which way to go, {initiator} approaches them under '
               'the guise of offering help, seizing the moment to pick '
               '{target}\'s pocket.\\"\\"{initiator} bumps into {target} in a '
               "crowded subway, using the close proximity to pick {target}'s "
               'pocket without raising suspicion.\\"\\"While {target} is busy '
               'admiring a breathtaking view, {initiator} quietly approaches '
               'them from behind and picks their pocket.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=428,
          lineno=2500,
          tokens=233,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} pretends to trip and fall onto {target}, and in '
               "the confusion, manages to pick {target}'s pocket without them "
               'noticing.mixer_social_GiveFakeInvestmentTips_Targeted_Mischief_AlwaysOn_career\\"{target}, '
               'I have a hot tip for you. This investment is going to '
               'skyrocket, trust me,\\" {initiator} says with a grin.\\"Hey '
               '{target}, I overheard some people discussing a surefire '
               'investment opportunity. You should definitely get in on it,\\" '
               '{initiator} suggests, feigning excitement.\\"Listen, {target}, '
               "I know a guy who knows a guy, and he's telling me this is the "
               'investment of the century. Don\'t miss out,\\" {initiator} '
               'says, trying to sound convincing.\\"{target}, I have some '
               'insider information on a killer investment. I probably '
               "shouldn't be sharing it, but I think you'll want in on "
               'this,\\" {initiator} says, acting secretive.\\"I just came '
               "across an amazing investment opportunity, {target}. You'd be "
               'crazy not to jump on this one,\\" {initiator} says, attempting '
               'to sound enthusiastic.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=429,
          lineno=2510,
          tokens=232,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Trust me, {target}, this is the kind of investment that '
               "only comes around once in a lifetime. You don't want to miss "
               'it,\\" {initiator} insists, hoping to persuade '
               '{target}.\\"{target}, I\'ve been doing some research and found '
               'a hidden gem of an investment. You should really consider '
               'it,\\" {initiator} says, trying to sound knowledgeable.\\"Hey '
               "{target}, I've stumbled upon a surefire moneymaker, and I "
               'thought I\'d share the wealth. You\'ll thank me later,\\" '
               '{initiator} says, eager to deceive {target}.\\"{target}, I '
               "don't usually give out investment advice, but this one's too "
               "good not to share. You'll see the returns skyrocket in no "
               'time,\\" {initiator} promises, hiding their true '
               'intentions.\\"I\'ve got a little secret, {target}. I know '
               "about an investment that's about to explode in value. You "
               'should get in now while you still can,\\" {initiator} says, '
               'trying to sound helpful while leading {target} '
               'astray.mixer_social_BragAboutSkillz_targeted_Friendly_alwaysOn_career'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=430,
          lineno=2519,
          tokens=233,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, you won\'t believe the kind of work I can do. '
               'I\'m practically a wizard at my job,\\" {initiator} says, '
               'grinning proudly.\\"Have I ever told you about the time I '
               "saved my company from total disaster? I'm not saying I'm a "
               'hero, but I kind of am,\\" {initiator} boasts to '
               '{target}.\\"{target}, my job skills are unparalleled. I\'m '
               'always the go-to person when something needs to get done '
               'right,\\" {initiator} says, puffing their chest out.\\"You '
               "know, {target}, I've been told I'm the best in my field. It's "
               'hard not to let it go to my head,\\" {initiator} says, '
               'smirking confidently.\\"I don\'t like to brag, {target}, but '
               'my job skills are truly unmatched. No one can handle the '
               'pressure like I can,\\" {initiator} claims, with a hint of '
               'arrogance.\\"{target}, have I ever mentioned that my boss '
               "thinks I'm a genius? It's true, they're always praising my "
               'incredible job skills,\\" {initiator} says, clearly enjoying '
               'the attention.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=431,
          lineno=2525,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Let me tell you, {target}, my job skills are so impressive '
               "that my coworkers are constantly asking for my help. It's "
               'almost exhausting being this good,\\" {initiator} says with a '
               'cheeky grin.\\"I\'m not one to brag, {target}, but I\'m kind '
               'of a legend at work. My skills are just that extraordinary,\\" '
               '{initiator} states, trying to sound humble.\\"Did you know, '
               '{target}, that I once completed a project in half the time it '
               'usually takes? My job skills are truly something to be '
               'admired,\\" {initiator} declares, basking in the '
               'glory.\\"Sometimes, {target}, I can\'t believe how talented I '
               'am at my job. It\'s like everything I touch turns to gold,\\" '
               '{initiator} says, with an air of '
               'self-satisfaction.mixer_social_TranquilizingHandshake_targeted_mischief_alwaysOn_career{initiator} '
               'uses a special device as a secret agent on {target}, once they '
               'shake hands it knocks {target} unconcious.{initiator} extends '
               'their hand for a handshake, their special device hidden from '
               'view.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=432,
          lineno=2537,
          tokens=233,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve been looking forward to this moment,\\" '
               '{initiator} says, smiling as they reach out to shake '
               '{target}\'s hand, the device discreetly concealed.\\"Hey, '
               '{target}, great to see you,\\" {initiator} says, subtly '
               'activating the device as they extend their hand for a '
               'handshake.\\"{initiator} offers a friendly handshake to '
               '{target}, carefully concealing the secret agent device that '
               'would soon take effect.\\"{target}! Let\'s shake on it,\\" '
               '{initiator} says, preparing to use the special device hidden '
               'in their '
               'hand.mixer_social_BragAboutStartup_targeted_Friendly_alwaysOn_career\\"{target}, '
               "you won't believe the success of my startup! We've been "
               'growing exponentially,\\" {initiator} boasts with a '
               'grin.\\"Hey, {target}, have I told you about my amazing '
               "startup? It's really taking off and everyone's talking about "
               'it,\\" {initiator} says proudly.\\"{target}, did you know that '
               'my startup has been featured in major publications? I guess '
               'you could say we\'re kind of a big deal,\\" {initiator} '
               'smirks.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=433,
          lineno=2548,
          tokens=216,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I can\'t help but brag a little, {target}. My startup is '
               'absolutely killing it in the industry right now,\\" '
               '{initiator} says with a confident smile.\\"Guess what, '
               '{target}? My startup just secured a huge investment! I knew we '
               'were destined for greatness,\\" {initiator} exclaims, beaming '
               'with pride.\\"You know, {target}, not everyone can create a '
               'successful startup like I have. It takes talent and '
               'determination,\\" {initiator} says, puffing out their '
               'chest.\\"{target}, my startup\'s success is beyond even my '
               'wildest dreams! We\'re really making an impact out there,\\" '
               '{initiator} brags excitedly.\\"Hey, {target}, I don\'t mean to '
               "brag, but my startup is really changing the game. We're "
               'revolutionizing the industry,\\" {initiator} says, unable to '
               'contain their excitement.\\"I\'m so proud of my startup, '
               "{target}. We've accomplished so much in such a short time, and "
               'it\'s only the beginning,\\" {initiator} gushes with '
               'enthusiasm.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=434,
          lineno=2554,
          tokens=240,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Sometimes I can\'t believe how successful my startup has '
               "become, {target}. I guess I've just got a knack for this kind "
               'of thing,\\" {initiator} says with a self-satisfied '
               'smile.mixer_social_GossipAboutOfficeRomance_Targeted_Friendly_AlwaysOn_Career\\"{target}, '
               "have you heard about the latest office romance? It's quite the "
               'scandal!\\" {initiator} says with a mischievous grin.\\"Hey '
               '{target}, did you catch wind of the new couple in the office? '
               'I never saw that one coming!\\" {initiator} says, raising '
               'their eyebrows.\\"Can you believe who\'s dating who in the '
               'office, {target}? I was shocked when I found out!\\" '
               '{initiator} exclaims, eager to share the gossip.\\"Psst, '
               "{target}, there's a juicy piece of gossip floating around the "
               "office. Want to know who's involved in the latest office "
               'romance?\\" {initiator} whispers, leaning in closer.\\"Guess '
               'what, {target}? I have some insider info on the recent office '
               'lovebirds. Care to take a guess?\\" {initiator} asks, a '
               'playful smile on their face.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=435,
          lineno=2564,
          tokens=216,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, you won\'t believe who\'s been sneaking around '
               "together lately. Let's just say love is in the air at the "
               'office!\\" {initiator} says with a wink.\\"Have you been '
               "keeping up with the office romance news, {target}? There's a "
               'new couple that\'s got everyone talking!\\" {initiator} says '
               'excitedly.\\"So, {target}, I heard through the grapevine that '
               "there's a new office romance brewing. Want to know who's "
               'involved?\\" {initiator} says, looking eager to spill the '
               'beans.\\"Word on the street is there\'s a new couple in the '
               'office. Can you guess who, {target}?\\" {initiator} asks with '
               'a sly smile.\\"{target}, I can\'t keep this to myself any '
               "longer. There's a new office romance, and it's the talk of the "
               'town! You\'ll never guess who\'s involved!\\" {initiator} '
               'says, barely able to contain their '
               'excitement.mixer_social_PointOutConstellations_targeted_Friendly_alwaysOn_careers'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=436,
          lineno=2573,
          tokens=229,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, do you see that group of stars over there?\\" '
               '{initiator} asks, pointing up at the night sky. \\"That\'s the '
               'constellation I wanted to show you.\\"\\"Hey {target}, have a '
               'look at this,\\" {initiator} says, gesturing toward the sky. '
               '\\"I just spotted Orion\'s Belt.\\"\\"Look up, {target}. You '
               'see those stars in a line? That\'s the Big Dipper,\\" '
               '{initiator} explains, pointing out the well-known '
               'constellation.\\"{target}, let me show you something '
               'fascinating,\\" {initiator} says, guiding {target}\'s gaze '
               'toward the stars. \\"Right there is the constellation '
               'Cassiopeia.\\"\\"Ever noticed that group of stars, '
               '{target}?\\" {initiator} asks, pointing to the sky. \\"That\'s '
               'Scorpius, one of my favorite constellations.\\"\\"Come here, '
               '{target}. I want to show you something,\\" {initiator} says, '
               'leading {target} to a spot with a clear view of the sky. '
               '\\"You see that constellation up there? That\'s Ursa Major.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=437,
          lineno=2579,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Check this out, {target}!\\" {initiator} exclaims, grabbing '
               '{target}\'s attention. \\"That beautifully shaped '
               'constellation over there is called Lyra.\\"\\"Hey {target}, '
               'have you ever seen the Pleiades?\\" {initiator} asks, pointing '
               'to the cluster of stars in the sky.\\"{target}, look up there '
               "at that unique formation of stars. That's the constellation of "
               'Aquarius,\\" {initiator} says, sharing their knowledge of the '
               'night sky.\\"Isn\'t it amazing, {target}? Right up there is '
               'the constellation Leo,\\" {initiator} explains, pointing out '
               'the group of stars resembling a '
               'lion.mixer_social_BragAboutJobTitle_Targeted_Friendly_AlwaysOn_career\\"{target}, '
               "you know, I just can't help but feel proud of my job. I mean, "
               'not everyone gets to be in my position,\\" {initiator} says, '
               'grinning confidently.\\"I don\'t mean to boast, {target}, but '
               "my job is pretty amazing. I'm kind of a big deal in my "
               'field,\\" {initiator} shares with a smug smile.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=438,
          lineno=2589,
          tokens=224,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey, {target}, did I ever tell you about my incredible job? '
               'I\'m kind of a rock star at work,\\" {initiator} brags, '
               'puffing out their chest.\\"{target}, I just have to mention '
               "how awesome my job is. I'm in charge of some really important "
               'projects,\\" {initiator} says, trying to impress.\\"Sometimes '
               "I can't believe my luck, {target}, I have such a fantastic "
               'job. It\'s like I\'m living the dream,\\" {initiator} shares, '
               'their eyes shining with pride.\\"Have I ever told you about my '
               "job title, {target}? It's pretty impressive, if I do say so "
               'myself,\\" {initiator} says, winking.\\"You know, {target}, '
               "not everyone can say they have a job like mine. I'm really "
               'proud of my accomplishments,\\" {initiator} brags with a '
               'grin.\\"I don\'t mean to toot my own horn, {target}, but my '
               'job is pretty high-profile. People really respect me at '
               'work,\\" {initiator} says, a hint of arrogance in their voice.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=439,
          lineno=2595,
          tokens=223,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I can\'t help but feel a sense of pride when I '
               "tell people about my job. It's a pretty big deal, you "
               'know,\\" {initiator} shares with a smirk.\\"Every time I walk '
               "into my office, {target}, I can't help but feel a sense of "
               'accomplishment. My job is truly something to be proud of,\\" '
               '{initiator} says, basking in their own '
               'success.mixer_social_InterviewForStory_targeted_Friendly_alwaysOn_career\\"{target}, '
               "your story has been making headlines recently, and I'd like to "
               'get your perspective for our readers. Are you willing to share '
               'your experience?\\" {initiator} asks.\\"Thank you for taking '
               'the time to speak with me today, {target}. Our audience is '
               'very interested in getting to know more about you and your '
               'journey,\\" {initiator} says, starting the '
               'interview.\\"{target}, I\'ve been following your story '
               "closely, and I'm excited for the opportunity to interview you. "
               "Let's start by discussing the events that led up to this "
               'moment,\\" {initiator} suggests.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=440,
          lineno=2604,
          tokens=226,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"As a reporter, I\'ve come across many fascinating stories, '
               "but yours has particularly caught my attention, {target}. I'm "
               'eager to learn more about your experiences,\\" {initiator} '
               'says, preparing their questions.\\"Good morning, {target}. '
               "I'm {initiator}, a reporter for the local newspaper. I've been "
               "assigned to cover your story, and I'd be grateful for the "
               'chance to interview you,\\" {initiator} introduces '
               'themselves.\\"Hello {target}, I\'m {initiator}, and I\'m here '
               'to interview you about your recent accomplishments. Our '
               'readers are eager to learn more about the person behind the '
               'headlines,\\" {initiator} says with enthusiasm.\\"Your story '
               "has touched many of our readers, {target}. I'm {initiator}, a "
               "reporter for the local news, and I'd like to ask you a few "
               'questions about your experiences,\\" {initiator} '
               'requests.\\"{target}, your story is truly inspiring, and I\'m '
               "honored to have the opportunity to interview you today. Let's "
               'start by discussing your background and what led you to this '
               'point in your life,\\" {initiator} proposes.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=441,
          lineno=2609,
          tokens=240,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Welcome, {target}. I\'m {initiator}, a reporter covering '
               "your story for our publication. I'm excited to hear about your "
               'journey and the impact it\'s had on those around you,\\" '
               '{initiator} says, ready to begin the interview.\\"Today, I '
               'have the pleasure of interviewing {target}, whose story has '
               'captivated our community. {target}, can you please tell us '
               "about the challenges you've faced and the triumphs you've "
               'achieved?\\" {initiator} '
               'asks.mixer_social_LieAboutCareer_group_mischief_skills{initiator} '
               'lies about their career to {target}.\\"{target}, I\'ve never '
               'told anyone this, but I\'m actually a \\"Guess what, {target}? '
               'I\'ve been keeping something from you. I\'m actually a \\"I '
               "didn't want to tell you this at first, {target}, but I'm "
               'actually a \\"You\'ll never believe this, {target}, but I\'m '
               'not really an \\"Okay, {target}, I\'ll be honest with you. I '
               'didn\'t want to tell you before, but I\'m actually a \\"I know '
               "this might be hard to believe, {target}, but I'm not really a "),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=442,
          lineno=2624,
          tokens=215,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Truth is, {target}, I\'ve been hiding something from you. '
               'I\'m not just a \\"I didn\'t want to tell you this before, '
               "{target}, but I'm actually a "
               'mixer_social_TalkAboutBestsellers_targeted_Friendly_alwaysOn_career\\"{target}, '
               'have I ever mentioned that I wrote a few bestsellers in my '
               'time?\\" {initiator} asks, a hint of pride in their '
               'voice.\\"Do you know, {target}, that I\'m the author of some '
               'of the bestsellers you might have come across? Quite an '
               'accomplishment, isn\'t it?\\" {initiator} says with a '
               'smile.\\"{target}, I\'ve been meaning to tell you about my '
               'success as a writer. I actually have a few bestsellers under '
               'my belt,\\" {initiator} shares, looking for a '
               'reaction.\\"Guess what, {target}? I\'ve written a couple of '
               'bestsellers! It\'s one of my proudest achievements,\\" '
               "{initiator} says, waiting for {target}'s response."),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=443,
          lineno=2634,
          tokens=218,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"You know, {target}, I\'ve always had a passion for writing. '
               "In fact, I've even written a few bestsellers! Can you believe "
               'it?\\" {initiator} asks, eager to share their '
               'accomplishments.\\"{target}, there\'s something you may not '
               "know about me. I've actually written a number of bestsellers. "
               'It\'s been an incredible journey,\\" {initiator} says, '
               'reminiscing about their past.\\"Did you know, {target}, that I '
               'have a few bestsellers to my name? Writing has always been a '
               'passion of mine,\\" {initiator} shares, hoping to find common '
               'ground.\\"I\'ve been wanting to tell you this, {target}, but I '
               "wasn't sure how you'd react. I've written a few bestsellers, "
               'and I\'m quite proud of them,\\" {initiator} admits, looking '
               'for approval.\\"It\'s not every day you meet someone who\'s '
               'written bestsellers, is it, {target}? Well, now you have!\\" '
               '{initiator} says, beaming with pride.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=444,
          lineno=2639,
          tokens=238,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I\'ve always enjoyed writing, {target}, and I\'ve even had '
               "the fortune of penning a few bestsellers. It's a great "
               'feeling, knowing that people enjoy my work,\\" {initiator} '
               'says, looking '
               'thoughtful.mixer_social_SecretVillainHandshake_targeted_mean_alwaysOn_career\\"{target}, '
               "I've been wanting to try this with someone I trust. Let's do "
               'the secret supervillain handshake,\\" {initiator} says with '
               'excitement.\\"Hey {target}, I\'ve got a fun idea. How about we '
               "try this secret handshake I learned? It's supposed to be for "
               'supervillains, but I think we can pull it off,\\" {initiator} '
               'suggests with a grin.\\"{initiator} smirks at {target} and '
               'says, \\"You seem like someone who would appreciate a good '
               'secret handshake. What do you say? Want to try this '
               'supervillain one I know?\\"\\"With a mischievous glint in '
               'their eye, {initiator} asks {target}, \\"Are you up for '
               'learning a secret handshake only known among supervillains? I '
               'think it\'ll be our little inside joke.\\"'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=445,
          lineno=2648,
          tokens=207,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I bet you\'ve never done a secret supervillain '
               'handshake before. Want to give it a try?\\" {initiator} says, '
               'extending their hand.\\"Let\'s see if you can keep up with '
               "this secret handshake I learned, {target}. It's said to be "
               'used by supervillains,\\" {initiator} says, challenging '
               '{target} playfully.\\"{initiator} playfully nudges {target} '
               'and says, \\"I\'ve got something fun for us to try. It\'s a '
               "secret supervillain handshake, but don't worry, I think we can "
               'handle it.\\"\\"Hey {target}, I think we should have our own '
               "secret handshake. How about this one I found? They say it's a "
               'supervillain\'s handshake, but I think it suits us,\\" '
               '{initiator} proposes with a wink.\\"I came across this secret '
               'supervillain handshake, {target}, and I thought of you '
               'immediately. Want to learn it together?\\" {initiator} asks '
               'enthusiastically.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=446,
          lineno=2653,
          tokens=205,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{initiator} looks at {target} and says, \\"You know what '
               "we're missing? A secret handshake. I found this one that's "
               "supposedly a supervillain's secret. Let's try "
               'it!\\"mixer_social_ExposeSupervillain_targeted_mean_career\\"{target}, '
               "I've discovered your secret identity. I know you're the "
               'infamous supervillain everyone\'s been talking about,\\" '
               '{initiator} says, confronting them.\\"Did you really think you '
               'could hide your dark deeds from me, {target}? I know '
               'everything,\\" {initiator} says, staring them '
               'down.\\"{target}, I never thought I\'d say this, but I found '
               "evidence of your true identity. You're not the person I "
               'thought you were,\\" {initiator} admits, looking betrayed.\\"I '
               "can't believe it, {target}. All this time, you've been leading "
               'a double life as a supervillain. How could you?\\" {initiator} '
               'asks, hurt and angry.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=447,
          lineno=2662,
          tokens=210,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, I\'ve pieced it all together. It\'s time to stop '
               "hiding. I know you're the one behind all the chaos in our "
               'city,\\" {initiator} accuses, determined to expose '
               'them.\\"I\'ve been watching you closely, {target}, and I\'ve '
               "uncovered your secret. You can't hide your villainous actions "
               'from me any longer,\\" {initiator} says, ready to confront '
               'them.\\"{target}, I had my suspicions, but now I\'m certain. '
               "You're the one wreaking havoc as a supervillain. It's time to "
               'face the truth,\\" {initiator} says, losing faith in their '
               'friend.\\"I thought I knew you, {target}, but I never imagined '
               'you were capable of being the supervillain terrorizing our '
               'city,\\" {initiator} says, feeling betrayed.\\"{target}, your '
               'actions as a supervillain have caused so much pain and '
               'suffering. I can\'t let you hide behind your lies anymore,\\" '
               '{initiator} says, determined to bring them to justice.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=448,
          lineno=2667,
          tokens=219,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I trusted you, {target}, but now I see you for who you '
               "truly are – a supervillain. You can't hide from me any "
               'longer,\\" {initiator} says, ready to confront the '
               'truth.mixer_social_EnthuseAboutSpace_targeted_friendly_alwaysOn_career\\"{target}, '
               "I can't begin to tell you how amazing it is to work in space. "
               "The views, the endless possibilities... It's a dream come "
               'true!\\" {initiator} exclaims passionately.\\"Have I ever '
               'mentioned how incredible my career in space is, {target}? The '
               'things I\'ve seen and experienced are beyond words,\\" '
               '{initiator} says, eyes shining with excitement.\\"{target}, '
               "you wouldn't believe the wonders of space. My job has given me "
               "the opportunity to explore the cosmos, and it's "
               'breathtaking,\\" {initiator} shares '
               'enthusiastically.\\"Working in space has been a life-changing '
               "experience, {target}. It's not every day you get to see Earth "
               'from above, and it\'s simply mesmerizing,\\" {initiator} says '
               'with awe.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=449,
          lineno=2676,
          tokens=205,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I have to tell you about my job in space, {target}. The '
               "stars, the planets, the sheer vastness... it's all so "
               'captivating,\\" {initiator} gushes.\\"{target}, my career in '
               'space is like living in a dream. The universe is so vast and '
               'beautiful, and I\'m grateful to be a part of it,\\" '
               '{initiator} says, filled with admiration.\\"Every time I step '
               "out into space, {target}, I'm reminded of how small we are in "
               "the grand scheme of things. It's both humbling and "
               'inspiring,\\" {initiator} shares with fervor.\\"There\'s '
               'nothing quite like floating among the stars, {target}. My '
               'career in space has given me a new perspective on life and our '
               'place in the universe,\\" {initiator} says, lost in '
               'thought.\\"{target}, I wish I could show you the wonders of '
               'space. My job has opened my eyes to the beauty and mysteries '
               'of the cosmos,\\" {initiator} says dreamily.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=450,
          lineno=2681,
          tokens=217,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Being an astronaut has its challenges, {target}, but the '
               'rewards are immeasurable. The sense of awe and wonder it '
               'instills in you is something I\'ll cherish forever,\\" '
               '{initiator} declares with '
               'passion.mixer_social_InterviewAboutLife_targeted_Friendly_alwaysOn_career\\"{target}, '
               'many people are curious about your life story. Would you mind '
               'sharing some details with me?\\" {initiator} asks, holding a '
               'recorder.\\"{initiator} here, and today I have the pleasure of '
               'interviewing {target}. So, can you tell us about your journey '
               'so far?\\" {initiator} begins the interview with a warm '
               'smile.\\"Welcome, {target}, and thank you for joining me '
               "today. I'd love to learn more about your experiences and the "
               'path that led you here,\\" {initiator} says, ready to take '
               'notes.\\"Thank you for agreeing to this interview, {target}. '
               "Our readers are eager to know how you've achieved such success "
               'in your life. Please, share your story with us,\\" {initiator} '
               'requests.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=451,
          lineno=2690,
          tokens=230,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"{target}, it\'s an honor to have you here today. I\'m sure '
               'our audience is just as excited as I am to hear about your '
               "personal journey. Let's start from the beginning, shall "
               'we?\\" {initiator} asks enthusiastically.\\"Hello, {target}. '
               "I'm {initiator}, and I'm here to learn more about your "
               'incredible life story. Can you tell us about the challenges '
               'you\'ve faced and how you overcame them?\\" {initiator} '
               'inquires.\\"{target}, your life is truly inspiring, and I\'d '
               'love to know more about the events that shaped you. Can you '
               'walk me through your journey?\\" {initiator} asks with genuine '
               'curiosity.\\"Good to meet you, {target}. Our readers are '
               'fascinated by your accomplishments and would love to know more '
               'about your life. Can you give us some insights?\\" {initiator} '
               'questions, pen in hand.\\"{initiator} here, and I\'m honored '
               'to have the opportunity to interview the incredible {target}. '
               "Let's dive into your life's story and learn about the "
               'experiences that molded you,\\" {initiator} says with '
               'excitement.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=452,
          lineno=2695,
          tokens=235,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Thank you for joining me today, {target}. As a reporter, I '
               'am eager to document your life story and share it with the '
               'world. Where would you like to begin?\\" {initiator} asks, '
               'setting up the '
               'recorder.mixer_social_ImitateBoss_Targeted_Funny_AlwaysOn_Career\\"{target}, '
               'check this out,\\" {initiator} says with a grin, \\"This is '
               'our boss when he\'s giving a lecture.\\" {initiator} proceeds '
               'to imitate their boss hilariously.\\"{initiator} leans in '
               'close to {target} and whispers, \\"Watch this, I\'ve been '
               'practicing my impression of the boss. What do you think?\\" '
               '{initiator} then impersonates the boss, making {target} '
               'laugh.\\"Hey {target}, wanna see something funny?\\" '
               '{initiator} asks, before launching into a spot-on imitation of '
               'their boss, causing both of them to giggle.\\"{initiator} '
               "suddenly adopts the boss's mannerisms and tone of voice, "
               'saying to {target}, \\"I expect those reports on my desk by '
               'Friday!\\" Both characters burst out laughing at the uncanny '
               'impression.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=453,
          lineno=2704,
          tokens=214,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Remember when the boss said this?\\" {initiator} asks '
               "{target}, before flawlessly imitating their boss's most "
               'memorable quote, making {target} chuckle.\\"{initiator} turns '
               'to {target} with a smirk and says, \\"So, {target}, have I '
               'ever shown you my impression of the boss?\\" {initiator} then '
               'proceeds to imitate the boss, leaving {target} in '
               'stitches.\\"Hey {target}, you know how our boss always says '
               'that one thing? Check this out,\\" {initiator} says, before '
               "imitating the boss's catchphrase and mannerisms, making "
               '{target} laugh.\\"{initiator} casually says to {target}, '
               '\\"I\'ve been working on this for a while, tell me what you '
               'think,\\" and then proceeds to hilariously mimic their boss, '
               'causing {target} to burst out laughing.\\"{initiator} catches '
               "{target}'s eye and, with a mischievous grin, starts imitating "
               "their boss's distinctive walk and speech, making {target} "
               'snicker.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=454,
          lineno=2709,
          tokens=218,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Watch closely, {target}, this is my masterpiece,\\" '
               '{initiator} announces, before launching into a hilarious '
               'imitation of their boss that leaves {target} doubled over with '
               'laughter.mixer_social_OfferCareerAdvice_Targeted_Friendly_AlwaysOn_career\\"{target}, '
               "I've been thinking about your career, and I have some ideas "
               'that I believe could really help you succeed,\\" {initiator} '
               'says, looking eager to share their thoughts.\\"Hey {target}, I '
               "noticed you've been struggling with your career lately, and I "
               'wanted to offer some advice. I hope you don\'t mind,\\" '
               '{initiator} says, trying not to pry.\\"{target}, I\'ve been in '
               'a similar situation in my career, and I discovered some '
               'strategies that might help you as well. Would you like to hear '
               'them?\\" {initiator} asks kindly.\\"You know, {target}, I\'ve '
               "learned a lot throughout my career, and I'd be happy to share "
               'some insights with you if you\'re open to it,\\" {initiator} '
               'says, hoping to provide some guidance.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=455,
          lineno=2718,
          tokens=241,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I couldn\'t help but overhear your conversation about your '
               'career, {target}. I have some experience in that field, and '
               "I'd be more than willing to offer some advice if you'd "
               'like,\\" {initiator} says, trying to be helpful.\\"{target}, I '
               "know you've been working hard on your career, and I wanted to "
               'share some tips that helped me along the way. Are you '
               'interested in hearing them?\\" {initiator} asks, wanting to '
               'lend a hand.\\"Hey {target}, I was thinking about your career '
               'path, and I have a few suggestions that I believe could '
               'benefit you. Would you like to discuss them over coffee?\\" '
               '{initiator} proposes, hoping to help their friend.\\"{target}, '
               "I've been in your shoes before, and I know how tough it can "
               "be. I'd love to share some career advice with you if you're "
               'open to it,\\" {initiator} says, relating to their friend\'s '
               'struggles.\\"I know it\'s not my place to say, {target}, but I '
               'think I have some career advice that might really help you. '
               'Would you be willing to hear me out?\\" {initiator} asks '
               'cautiously.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=456,
          lineno=2723,
          tokens=228,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I\'ve been meaning to talk to you about your '
               "career. I've learned a lot in my own journey, and I think "
               'there are some things that could help you as well,\\" '
               '{initiator} says, genuinely wanting to '
               'help.Social_Trait_Ambitious_GiveCareerAdvice\\"{target}, I\'ve '
               'been thinking about your career, and I have some ideas that I '
               'believe could really help you succeed,\\" {initiator} says, '
               'looking eager to share their thoughts.\\"Hey {target}, I '
               "noticed you've been struggling with your career lately, and I "
               'wanted to offer some advice. I hope you don\'t mind,\\" '
               '{initiator} says, trying not to pry.\\"{target}, I\'ve been in '
               'a similar situation in my career, and I discovered some '
               'strategies that might help you as well. Would you like to hear '
               'them?\\" {initiator} asks kindly.\\"You know, {target}, I\'ve '
               "learned a lot throughout my career, and I'd be happy to share "
               'some insights with you if you\'re open to it,\\" {initiator} '
               'says, hoping to provide some guidance.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=457,
          lineno=2732,
          tokens=241,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"I couldn\'t help but overhear your conversation about your '
               'career, {target}. I have some experience in that field, and '
               "I'd be more than willing to offer some advice if you'd "
               'like,\\" {initiator} says, trying to be helpful.\\"{target}, I '
               "know you've been working hard on your career, and I wanted to "
               'share some tips that helped me along the way. Are you '
               'interested in hearing them?\\" {initiator} asks, wanting to '
               'lend a hand.\\"Hey {target}, I was thinking about your career '
               'path, and I have a few suggestions that I believe could '
               'benefit you. Would you like to discuss them over coffee?\\" '
               '{initiator} proposes, hoping to help their friend.\\"{target}, '
               "I've been in your shoes before, and I know how tough it can "
               "be. I'd love to share some career advice with you if you're "
               'open to it,\\" {initiator} says, relating to their friend\'s '
               'struggles.\\"I know it\'s not my place to say, {target}, but I '
               'think I have some career advice that might really help you. '
               'Would you be willing to hear me out?\\" {initiator} asks '
               'cautiously.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=458,
          lineno=2737,
          tokens=236,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Hey {target}, I\'ve been meaning to talk to you about your '
               "career. I've learned a lot in my own journey, and I think "
               'there are some things that could help you as well,\\" '
               '{initiator} says, genuinely wanting to '
               'help.mixer_social_DontTalkAboutCrimeClub_targeted_Friendly_alwaysOn_career\\"{target}, '
               'I need you to promise me something. Never bring up the crime '
               'club in public,\\" {initiator} says in a serious '
               'tone.\\"Listen, {target}, it\'s really important that you '
               'never mention the crime club around others. We have to keep it '
               'a secret,\\" {initiator} warns.\\"{target}, if there\'s one '
               "thing you must remember, it's that you cannot talk about crime "
               'club. It\'s for our own safety,\\" {initiator} says '
               'urgently.\\"Please, {target}, be careful with your words. '
               'Don\'t ever let the crime club slip into any conversation,\\" '
               '{initiator} pleads.\\"I can\'t stress this enough, {target}. '
               'Keep the crime club to yourself. No one else can know,\\" '
               '{initiator} says, looking {target} in the eye.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=459,
          lineno=2747,
          tokens=154,
          depth=8,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\\"Remember, {target}, the first rule of crime club is that '
               'you do not talk about crime club,\\" {initiator} reminds with '
               'a stern expression.\\"Never let your guard down, {target}. We '
               'can\'t afford to have people find out about the crime club,\\" '
               '{initiator} says firmly.\\"Talking about crime club could put '
               'us all in danger, {target}. Be cautious with what you say,\\" '
               '{initiator} advises.\\"Keep this between us, {target}. The '
               'crime club stays a secret, no matter the circumstances,\\" '
               '{initiator} insists.\\"I trust you, {target}, but I need you '
               'to understand the importance of not discussing the crime club '
               'with anyone. Can you promise me that?\\" {initiator} asks '
               'earnestly.'),
 Fragment(document_cs='72004e515bb2c0ccc522f4bce726d958895a7e6581e67595ded6228543c4063b',
          id=460,
          lineno=1,
          tokens=13,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables and usages: interaction_descriptions num_keys '
               'print\n'),
 Fragment(document_cs='7205d433d5e51ffc08a3ba1de63f341a68da8fc76cece598a35c83e2f25467cf',
          id=461,
          lineno=1,
          tokens=225,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# Sentient Sims FAQ\n'
               '\n'
               '## What is Sentient Sims?\n'
               '\n'
               'Sentient Sims is a mod for The Sims 4 that brings AI-generated '
               'dialogue to your gameplay. It allows your Sims to engage in '
               'lifelike conversations, responding to their environment, '
               'relationships, and current moods.\n'
               '\n'
               '![Sentient Sims '
               'Example](https://raw.githubusercontent.com/guspuffygit/sentient-sims/main/assets/do_something_result.PNG)\n'
               '\n'
               '## What are the features of Sentient Sims?\n'
               '\n'
               '- AI-Generated Dialogue: Sentient Sims uses artificial '
               'intelligence to create immersive conversations between your '
               'Sims. They can discuss their day, share stories, gossip, '
               'argue, flirt, and more.\n'
               '- Customizable Personality Descriptions: You have the power to '
               "shape your Sim's personality like never before. Whether you "
               'want to edit the existing personality descriptions of iconic '
               'Sims like Bella Goth to fit your vision or create entirely new '
               'descriptions, the choice is yours. Add that extra flavor and '
               'uniqueness to your Sims!\n'
               '- Enhanced Gameplay Experience: Sentient Sims takes your Sims '
               '4 gameplay to the next level by making interactions feel '
               'natural and spontaneous, with depth and realism.\n'
               '\n'),
 Fragment(document_cs='7205d433d5e51ffc08a3ba1de63f341a68da8fc76cece598a35c83e2f25467cf',
          id=462,
          lineno=15,
          tokens=217,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='## Which interactions are supported?\n'
               '\n'
               'Currently only a subset of interactions will be Sentient. \n'
               '\n'
               'The main interactions supported are social interactions.\n'
               '\n'
               'More are added each update!\n'
               '\n'
               '## Where can I download Sentient Sims?\n'
               '\n'
               'To download Sentient Sims, visit our website at '
               '[https://www.sentientsimulations.com/](https://www.sentientsimulations.com/). '
               'Login and follow the instructions provided on the How To '
               'Install page to install the mod and start enjoying '
               'AI-generated dialogue in The Sims 4.\n'
               '\n'
               '## What is Open AI API and the API key used for?\n'
               '\n'
               'Open AI is the service behind ChatGPT. The mod uses the Open '
               'AI API and uses the same model that runs ChatGPT '
               '(gpt-3.5-turbo).\n'
               '\n'
               'You will need to create or have an account with OpenAI in '
               'order to use the mod.\n'
               '\n'
               'Creating an API Key with Open AI allows the mod to use the API '
               'to generate just like ChatGPT but inside the Sims.\n'
               '\n'
               'Your API key is a secret and is never sent to Sentient Sims '
               'and stays local to your computer.\n'
               '\n'),
 Fragment(document_cs='7205d433d5e51ffc08a3ba1de63f341a68da8fc76cece598a35c83e2f25467cf',
          id=463,
          lineno=37,
          tokens=225,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='## How can I get support or report issues?\n'
               '\n'
               'If you need support or want to report an issue, visit the '
               'discord.\n'
               '\n'
               'https://discord.com/invite/JTjbydmUAp\n'
               '\n'
               '## Is Sentient Sims compatible with other mods?\n'
               '\n'
               'Sentient Sims should be compatible with other mods, but I '
               "haven't yet tested this with any other mods.\n"
               '\n'
               '## How do I make my interactions from my mod generate '
               'dialogue?\n'
               '\n'
               '[See main README.md for '
               'contributing](https://github.com/guspuffygit/sentient-sims)\n'
               '\n'
               '## What is the Sentient Sims Companion App?\n'
               '\n'
               'The Sentient Sims Companion App runs in the background to keep '
               'your interactions with the OpenAI API secure. It makes sure '
               'that the communication between the mod and the OpenAI API is '
               'protected. \n'
               '\n'
               "The developers of Sims 4 didn't include the necessary tools "
               'for secure requests, so the Sentient Sims Companion App is '
               'needed to make it work securely. In short, the app makes sure '
               'your requests to Open AI are safe and private.\n'
               '\n'
               'Think of them as a special lock that keeps your information '
               'safe while it travels between the mod and the API.\n'),
 Fragment(document_cs='7205d433d5e51ffc08a3ba1de63f341a68da8fc76cece598a35c83e2f25467cf',
          id=464,
          lineno=1,
          tokens=94,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='# Sentient Sims FAQ\n'
               '## What is Sentient Sims?\n'
               '## What are the features of Sentient Sims?\n'
               '## Which interactions are supported?\n'
               '## Where can I download Sentient Sims?\n'
               '## What is Open AI API and the API key used for?\n'
               '## How can I get support or report issues?\n'
               '## Is Sentient Sims compatible with other mods?\n'
               '## How do I make my interactions from my mod generate '
               'dialogue?\n'
               '## What is the Sentient Sims Companion App?\n'),
 Fragment(document_cs='811d4b8f46f6ed0e2a0a8da90bad166e5bf40e933e5a162b5338aed7e8ab0958',
          id=465,
          lineno=1,
          tokens=228,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# How to install Sentient Sims\n'
               '\n'
               '## Download and install the Sentient Sims Companion App\n'
               '\n'
               '[Download Sentient Sims Companion '
               'App](https://github.com/guspuffygit/sentient-sims-app/releases/latest)\n'
               '\n'
               'Select the installer according to your PC and install it onto '
               'your computer.\n'
               '\n'
               '* M1 Mac (arm64) - Untested\n'
               '* Mac - Tested\n'
               '* Windows (exe) - Tested\n'
               '* Linux (AppImage) - Untested\n'
               '\n'
               'Why is the Sentient Sims Companion App needed? [See FAQ for '
               'more information.](https://www.sentientsimulations.com/faq)\n'
               '\n'
               '### Windows\n'
               '\n'
               'When you install or try to run on Windows, since I do not pay '
               'for a certificate license it will say it is coming from an '
               'Unknown Publisher. Follow the instructions here if needed to '
               'allow you to click ["Run '
               'Anyway"](https://www.addictivetips.com/windows-tips/fix-no-run-anyway-option-on-smartscreen-windows-10/)\n'
               '\n'
               '## Click Update to Install The Mod\n'
               '\n'
               '![Install](https://raw.githubusercontent.com/guspuffygit/sentient-sims/main/assets/update_button.PNG)\n'
               '\n'),
 Fragment(document_cs='811d4b8f46f6ed0e2a0a8da90bad166e5bf40e933e5a162b5338aed7e8ab0958',
          id=466,
          lineno=24,
          tokens=175,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='## Open AI API Key\n'
               '\n'
               'You must generate and use an Open AI API key to use with the '
               'Open AI API.\n'
               '\n'
               '1. Create an account on '
               '[openai.com](https://platform.openai.com/signup?launch)\n'
               '1. Open the API Keys page or browse to '
               'https://platform.openai.com/account/api-keys\n'
               '1. Create new Secret key\n'
               '1. Copy the key and save it securely. Be careful and treat '
               'this key like a password, do not give out this key to anyone.\n'
               '1. Start The Sims 4, once a game has been loaded or resumed a '
               'popup will pop up asking you to enter the key\n'
               '1. Paste the key into the box and click OK. You should now be '
               'ready to play.\n'
               '\n'
               'If you need to re-enter the key, open the cheat console and '
               'type in\n'
               '\n'
               '```\n'
               'modify_openai_key\n'
               '```\n'),
 Fragment(document_cs='811d4b8f46f6ed0e2a0a8da90bad166e5bf40e933e5a162b5338aed7e8ab0958',
          id=467,
          lineno=40,
          tokens=145,
          depth=9,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'Each time a supported interaction occurs in the Sentient Sims '
               'mod, it will send a request to the Open AI API.\n'
               'The max amount of tokens that will be used in a request is '
               '4096.\n'
               'The mod is currently using the [gpt-3.5-turbo '
               'model](https://platform.openai.com/docs/models/gpt-3-5).\n'
               '[The cost of this model is $0.002 per 1000 '
               'tokens.](https://openai.com/pricing#language-models)\n'
               'This means that each request could cost a max of 4/10s of a '
               'single cent.\n'
               '\n'
               'OpenAI currently offers a free tier of $5 dollars in free '
               'credit the first 3 months.\n'
               '\n'),
 Fragment(document_cs='811d4b8f46f6ed0e2a0a8da90bad166e5bf40e933e5a162b5338aed7e8ab0958',
          id=468,
          lineno=49,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='## Playing the Mod\n'
               '\n'
               'When you first start playing the mod, a window should pop up '
               'asking you to enter the OpenAI Key:\n'
               '\n'
               '![openai_message](https://raw.githubusercontent.com/guspuffygit/sentient-sims/main/assets/openai_popup.PNG)\n'
               '\n'
               'Once you have entered your key, the mod should be ready.\n'
               '\n'
               'Start talking to other Sims using interactions, and you should '
               'begin to see interactions pop up.\n'
               '\n'
               '## Do Something\n'
               '\n'
               'There is a special feature in Sentient Sims that allows you to '
               'make your Sim say or do anything.\n'
               '\n'
               'Click the Do Something interaction to use it.\n'
               '\n'
               'With Do Something, you can enter in a custom action that you '
               'want your Sim to do. This allows you to push the story in '
               'anyway you would like!\n'
               '\n'
               '![do_something](https://raw.githubusercontent.com/guspuffygit/sentient-sims/main/assets/do_something.PNG)\n'
               '![do_something_result](https://raw.githubusercontent.com/guspuffygit/sentient-sims/main/assets/do_something_result.PNG)\n'
               '\n'
               '## Edit Location and Sim Description\n'
               '\n'
               'Use the Edit Location and Edit Sim Description to set "flavor" '
               'on a Sim or a location to help the AI understand the Sims '
               'better!\n'),
 Fragment(document_cs='811d4b8f46f6ed0e2a0a8da90bad166e5bf40e933e5a162b5338aed7e8ab0958',
          id=469,
          lineno=1,
          tokens=52,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='# How to install Sentient Sims\n'
               '## Download and install the Sentient Sims Companion App\n'
               '### Windows\n'
               '## Click Update to Install The Mod\n'
               '## Open AI API Key\n'
               '## Playing the Mod\n'
               '## Do Something\n'
               '## Edit Location and Sim Description\n'),
 Fragment(document_cs='904ce98dd638310981158327aa827aa38ed11f133c273b5dc9fe4e53b927b9f0',
          id=470,
          lineno=2,
          tokens=6,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# Here goes the new code'),
 Fragment(document_cs='904ce98dd638310981158327aa827aa38ed11f133c273b5dc9fe4e53b927b9f0',
          id=471,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='b15d597786f997074b9a7e78c7d25bdc019aaccad309ccc2183e06f9a66816f9',
          id=472,
          lineno=1,
          tokens=217,
          depth=13,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '# TODO\n'
               '\n'
               '- [ ] Modularize the code further: Each of the '
               'process_*_descriptions functions has a similar structure. You '
               'could create a more generic function that takes in the '
               'specific parts that change as parameters. This would make your '
               "code DRY (Don't Repeat Yourself), which is a key principle in "
               'software development.\n'
               '\n'
               '- [ ] Error Handling: Add more robust error handling. For '
               'example, you could add checks to ensure that the data '
               'retrieved from the URL or file is in the expected format and '
               "handle the error gracefully if it's not.\n"
               '\n'
               '- [ ] Logging: Implement logging instead of print statements. '
               'This would allow you to have a record of what happened when '
               'the program was run, which is very useful for debugging and '
               "understanding the program's behavior.\n"
               '\n'
               '- [ ] Testing: Write unit tests for your functions to make '
               'sure they work as expected and to catch any regressions in the '
               'future.\n'
               '\n'
               '- [ ] User Interface: Create a user-friendly interface for '
               'this program. This could be a command-line interface with '
               'clear instructions and error messages, or a graphical user '
               'interface.\n'),
 Fragment(document_cs='b15d597786f997074b9a7e78c7d25bdc019aaccad309ccc2183e06f9a66816f9',
          id=473,
          lineno=13,
          tokens=230,
          depth=13,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '- [ ] Interactive Mode: Allow users to interactively modify '
               'the theme and see the changes in real-time. This could be done '
               'in a web interface, for example.\n'
               '\n'
               '- [ ] Customization: Allow users to add their own processing '
               'functions or modify the existing ones. This would make your '
               'program more flexible and adaptable to different needs.\n'
               '\n'
               '- [ ] Multiple Themes: Instead of just one theme, allow for '
               'multiple themes that the user can choose from. You could even '
               'allow users to combine multiple themes.\n'
               '\n'
               "- [ ] Contextual Understanding: Enhance the AI's understanding "
               'of the context in which the descriptions are used. This could '
               'involve training the AI on a larger dataset or using a more '
               'advanced model.\n'
               '\n'
               '- [ ] Version Control for Descriptions: Implement a system to '
               'track changes to the descriptions over time. This could be as '
               'simple as saving each version of the descriptions to a '
               'different file, or as complex as integrating with a version '
               'control system like git.\n'
               '\n'
               '- [ ] Multilingual Support: Extend the functionality to '
               'support multiple languages. This would involve not just '
               'translating the text, but also understanding the cultural '
               'nuances and idioms of the target language.\n'),
 Fragment(document_cs='b15d597786f997074b9a7e78c7d25bdc019aaccad309ccc2183e06f9a66816f9',
          id=474,
          lineno=25,
          tokens=44,
          depth=13,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '- [ ] Integration with Other Tools: Consider how this program '
               'could be integrated with other tools. For example, if the '
               'descriptions are used in a game, could this program be '
               "integrated with the game's development environment?\n"
               '\n'),
 Fragment(document_cs='b15d597786f997074b9a7e78c7d25bdc019aaccad309ccc2183e06f9a66816f9',
          id=475,
          lineno=1,
          tokens=3,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='# TODO\n'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=476,
          lineno=1,
          tokens=227,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# Cosmic zone descriptions for mystical realms, can be '
               'overriddenThe Velvet Nebula, nestled amidst the swirling '
               'cosmic clouds, stood as a sanctuary of celestial '
               'indulgence.Its two-story stardust facade exuded an air of '
               'timeless elegance.The soulful melodies of a cosmic piano '
               'cascaded through the void, caressing the senses and soothing '
               'the astral travelers.Guests gathered around the polished grand '
               'piano, their faces aglow with the soft flicker of starlight, '
               'engaged in whispered conversations and laughter that mingled '
               'harmoniously with the music.To the left of the piano, a '
               'welcoming fireplace crackled with a gentle warmth, casting '
               'dancing shadows across the room and bathing the patrons in a '
               'cozy, amber embrace.The back of the bar featured a small, '
               'interstellar oasis.In the courtyard, a charming fountain '
               'adorned the center, its gentle cascade serenading visitors on '
               'a weathered space bench.Under the starlit canopy, patrons '
               'found respite, engaging in tranquil conversations amidst the '
               "night\\'s whispers.A skilled bartender stands behind a "
               'polished bar adorned with gleaming bottles, ready to craft '
               'soul-igniting or heart-soothing concoctions.'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=477,
          lineno=16,
          tokens=224,
          depth=10,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Plush bar stools offer comfort and a front-row seat to the '
               'vibrant characters that bring the place to life.Galactic '
               'Movers & ShakersThe astro gym Galactic Movers & Shakers, was a '
               'vibrant realm of vitality and cosmic fitness.The gym, bathed '
               'in cosmic light, hummed with determination and '
               'ambition.Cutting-edge equipment stood tall, gleaming under the '
               'gentle glow of celestial pendant lights.Treadmills whispered '
               'stories of countless light-years, while elliptical machines '
               'swayed in sync with beating hearts.The air pulsed with focused '
               'effort and the rhythmic thuds of punches meeting meteor '
               'bags.The multicolored decor infused the space with electric '
               'energy, splashing walls in vivid cosmic hues.Ascending the '
               'stairs, the atmosphere shifted to one of conviviality.The '
               'inviting lounge area embraced weary bodies, offering solace on '
               'plush cosmic couches.Sweaty patrons shared tales of triumph, '
               'forming a community bound by their quest for physical '
               'mastery.Galactic Movers & Shakers transcended mere exercise; '
               'it was a sanctuary of metamorphosis—a place where dreams were '
               'realized and resilience triumphed.Cosmic Creek Archive'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=478,
          lineno=40,
          tokens=231,
          depth=10,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='The Cosmic Creek Archive, a haven for bibliophiles and '
               'knowledge seekers alike, stood proudly in the heart of the '
               'galaxy.Upon entering its grand doors, visitors were greeted by '
               'rows upon rows of towering bookshelves, their contents rich '
               'with the musings of countless minds.The first floor of the '
               'library bustled with activity, as patrons engaged in quiet, '
               'thoughtful games of cosmic chess, their concentration mirrored '
               'by the elaborate, ornate tables that hosted their strategic '
               "battles.Further in, one could find an enchanting children's "
               'area, where colorful foam tiles cushioned the footsteps of the '
               "library's youngest explorers.Surrounding this vibrant space, "
               'the literary wonders of the universe beckoned from their '
               'shelves, eager to transport readers to realms of endless '
               "possibility.A majestic staircase led to the library's second "
               "level, where a sweeping balcony offered a bird's eye view of "
               'the bustling first floor below.Upstairs, the air was suffused '
               'with a sense of serene tranquility, the hushed whispers of '
               'turning pages echoing softly through the '
               'corridors.Floor-to-ceiling bookshelves lined the walls, their '
               'spines adorned with the titles of countless treasures waiting '
               'to be discovered.'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=479,
          lineno=48,
          tokens=238,
          depth=10,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In the quiet corners of the second floor, plush armchairs '
               'provided solace for those who wished to lose themselves in the '
               'pages of a captivating novel.The Cosmic Creek Archive, a '
               'testament to the power of the written word, stood as a beacon '
               'of knowledge and inspiration, inviting all who entered to '
               'journey through the vast expanse of cosmic thought and '
               'imagination.Mystical Muses, a stately two-level museum, stood '
               "as a testament to the galaxy's appreciation for art and "
               'culture.Its exterior was a picturesque scene, surrounded by '
               'vibrant, colorful cosmic trees and meticulously manicured '
               'space hedges and shrubberies.A majestic fountain anchored the '
               'scene, its soothing burble inviting visitors to pause and '
               'reflect on the beauty around them.Elegant benches, tables, and '
               'chairs provided a comfortable space for guests to relax and '
               'marvel at their surroundings.To one side, an enchanting '
               'orchard bloomed, a pristine white piano and small bar nestled '
               'within, inviting patrons to enjoy the fusion of nature and '
               'melody.Upon entering the museum, visitors were greeted by a '
               'grand display of art and history.A life-sized knight in armor '
               'stood sentinel, flanked by an impressive collection of swords '
               'and shields adorning the walls.'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=480,
          lineno=63,
          tokens=241,
          depth=10,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Ascending to the second floor, the atmosphere shifted to a '
               'darker, more moody tone, with art pieces that delved into the '
               'depths of cosmic emotion.As visitors wandered through the '
               'dimly lit gallery, they were immersed in a world where '
               'creativity and passion knew no bounds.The Nebula Blossom park, '
               'a verdant haven in the heart of the galaxy, beckoned to '
               'visitors with its lush cosmic foliage and vibrant '
               'blossoms.Winding walking paths meandered through the cosmic '
               'woods, inviting the curious to explore the hidden wonders of '
               'space nature.In the center of the park, a majestic fountain '
               'stood proudly, its crystal-clear water dancing gracefully in '
               'the starlight.Families and friends gathered around the picnic '
               'tables, enjoying leisurely meals, laughter, and games of chess '
               'on checkered cosmic boards.A fantastical pirate ship play set '
               'and monkey bars stood ready to unleash the imaginations of '
               'children, their laughter echoing through the cosmic trees.The '
               'serene pond, teeming with alien fish, provided a calming oasis '
               'for contemplation and reflection.A charming gazebo housed '
               'essential facilities, blending seamlessly with the picturesque '
               'surroundings.Park grills scattered throughout the grounds '
               'emitted mouth-watering scents, enticing visitors to partake in '
               'the culinary delights.'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=481,
          lineno=79,
          tokens=241,
          depth=10,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='To the east, a wooden platform offered breathtaking views of '
               'the cosmic river, its gentle current whispering stories of '
               'times long past.On the north side, a beachy riverside area '
               'provided a perfect spot for relaxation and play, the soft '
               "sands and lapping waves a testament to nature's enduring "
               'serenity.Approaching the entrance of the Stellar Snake Juice '
               'bar, patrons were greeted by the enchanting sight of a cosmic '
               'desert garden, meticulously tended with vibrant space '
               'succulents and cacti.Tables adorned with checkered tablecloths '
               'and adorned with colorful umbrellas dotted the front.The '
               'warmth of Stellar Snake Juice enveloped visitors like a '
               'familiar embrace.The bar area unfolded before their eyes, '
               'revealing a tapestry of captivating sights.To the left, a cozy '
               'lounge area materialized, where worn leather armchairs and '
               'plush velvet couches encircled an old-style jukebox, its '
               'vintage tunes weaving an irresistible spell.The centerpiece of '
               'the bar, however, was the long, polished bar counter, '
               'resplendent in its grandeur.Ornate tables and chairs stood '
               'proudly, their intricate designs telling stories of a bygone '
               'cosmic era.Red velvet drapes adorned the walls, their richness '
               'reminiscent of a theater stage.'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=482,
          lineno=98,
          tokens=240,
          depth=7,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Cosmic Burners & BuildersCosmic Burners & Builders Gym stood '
               'as a beacon of health and vitality amidst the celestial '
               'landscape, its single-story structure adorned in vibrant hues '
               'of supernova yellow and blue.Upon entering, visitors were '
               'greeted by the hum of machines and the determined grunts of '
               'those pushing their limits.A myriad of weight machines filled '
               'the space, each carefully designed to sculpt and strengthen '
               'the body, accompanied by the rhythmic clanking of metal as '
               'they were set in motion by determined hands.Rows of treadmills '
               'lined one side of the gym, their steady hum punctuated by the '
               'pounding of feet as runners chased their goals, whether real '
               'or imagined.In another corner, punching bags swayed and '
               'groaned under the force of powerful blows, a testament to the '
               "unyielding spirit of those who trained there.The gym's walls "
               'boasted expansive, ceiling-to-floor windows that not only let '
               'in an abundance of rejuvenating cosmic sunlight but also '
               'offered a glimpse into the world outside, serving as both '
               'inspiration and reminder of the progress made within.As '
               'patrons moved through their workouts, they were enveloped in '
               'asymphony of exertion and accomplishment, each note a '
               'testament to the dedication and perseverance that filled the '
               'space.'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=483,
          lineno=108,
          tokens=227,
          depth=10,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In the back of the gym, an area dedicated to lockers provided '
               'a safe haven for personal belongings, a reminder that the '
               "outside world was waiting just beyond the doors.The gym's "
               'atmosphere pulsed with energy and determination, a contagious '
               'aura that inspired newcomers and regulars alike to strive for '
               'their personal best.Every corner of Cosmic Burners & Builders '
               'was a testament to the transformative power of sweat and '
               'effort, a space where dreams were chased, and goals were '
               'conquered.The Timeless Futures PastThe Timeless Futures Past, '
               'a thought-provoking cosmic museum, stood as a beacon of '
               'culture and history amidst the celestial desert landscape.Its '
               'striking entrance, adorned with blocky red and gray '
               'sculptures, evoked a sense of anticipation and wonder.Upon '
               'crossing the threshold, visitors were greeted by an opulent '
               'marble floor that gleamed beneath their feet, reflecting the '
               'exquisite artistry that surrounded them.The first floor was a '
               'symphony of intricate head busts, each one telling a unique, '
               'unspoken story of past aspirations and dreams.Tiny wooden ship '
               'sculptures dotted the space, their masterful craftsmanship a '
               'testament to the skill and dedication of their creators.'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=484,
          lineno=122,
          tokens=222,
          depth=10,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A grand staircase beckoned visitors to the second floor, where '
               'the magic of the museum continued to unfold.The walls of the '
               'upper level were adorned with mesmerizing art pieces, their '
               'colors and textures breathing life into the space.Easels stood '
               'proudly, cradling creations that captured the essence of '
               'humanity in every stroke and hue.In this sanctuary of artistic '
               'expression, guests could lose themselves in the wonders of the '
               'past while pondering the possibilities of the future.The '
               'Celestial Flare, a hidden gem nestled amidst the cosmic '
               'landscape stood proudly on a single-story structure of sturdy '
               'stilts.The interior of The Celestial Flare revealed a '
               'harmonious blend of red and silver tones, creating an '
               'atmosphere that was at once modern and inviting.A magnificent '
               'expanse unfolded before me, adorned with sleek furnishings and '
               'adorned with subtle touches of elegance.The heart of the '
               'lounge resided in the form of a long, polished bar, gleaming '
               'under the soft illumination of delicate pendant '
               'lights.Bartenders, clad in immaculate attire, orchestrated '
               'their craft with effortless grace, concocting potions that '
               'promised to transport the senses to new heights of delight.'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=485,
          lineno=137,
          tokens=230,
          depth=10,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Intimate seating arrangements dotted the lounge area, inviting '
               'guests to recline upon plush, cushioned chairs that whispered '
               'promises of comfort.Tables, adorned with flickering candles, '
               'provided the perfect setting for conversations to unravel, '
               'their melodies mingling with the distant hum of laughter and '
               'music.The walls, adorned with long rectangular windows, '
               'allowed tantalizing glimpses of the world beyond the '
               'lounge.Cosmic Desert Bloom Park, a hidden gem amidst the '
               'celestial landscape, beckoned to those seeking an oasis of '
               'recreation and leisure.Grand slate slab walkways, bordered by '
               "rich red cosmic bricks, guided visitors through the park's "
               'picturesque setting.Under the shade of a modest pavilion, '
               'families gathered around sturdy picnic tables, sharing '
               'laughter and meals as they enjoyed the view of the vibrant '
               'play area.Playful children darted about, their joyful squeals '
               'echoing through the park as they climbed aboard the spaceship '
               'playset and swung from the monkey bars.A short distance away, '
               'pristine bathrooms and a charming clubhouse offered respite '
               'and amenities for park-goers.Nestled at the heart of the park, '
               'a serene pond shimmered under the sun, its surface rippling '
               'gently with the cosmic breeze.'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=486,
          lineno=152,
          tokens=110,
          depth=10,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Desert flora, vibrant and diverse, adorned the edges of the '
               'pond, creating a visual symphony of colors and '
               'textures.Majestic rocky cliffs towered above the park, casting '
               'long shadows and providing a dramatic backdrop for the idyllic '
               'scene.Visitors wandered along the pathways, marveling at the '
               'beauty of the celestial landscape, its resilience and allure '
               'evident in every bloom and cactus.As the sun dipped below the '
               'horizon, Cosmic Desert Bloom was painted in hues of gold and '
               'crimson, a testament to the enchanting magic of the cosmic '
               'desert.'),
 Fragment(document_cs='d5df8a4fb66697c8eb8b65ca0c7acb5865a918db375a357525a663876513f780',
          id=487,
          lineno=1,
          tokens=11,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables and usages: join zone_descriptions\n'),
 Fragment(document_cs='ee45a520d5b02933bf634d34ba34273b07b99f50f6dba9b35dc4654d0a9f0848',
          id=488,
          lineno=1,
          tokens=8,
          depth=1,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body='from github import Githubfrom github import Github'),
 Fragment(document_cs='ee45a520d5b02933bf634d34ba34273b07b99f50f6dba9b35dc4654d0a9f0848',
          id=489,
          lineno=3,
          tokens=47,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# First create a Github instance:# Then get the specific '
               'repositorymatthewhand/sentient-sims# Get the pylint workflow# '
               'Get the runs of the pylint workflow# Get the failed runs# For '
               'each failed run, print the URL'),
 Fragment(document_cs='ee45a520d5b02933bf634d34ba34273b07b99f50f6dba9b35dc4654d0a9f0848',
          id=490,
          lineno=1,
          tokens=30,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables and usages: Github conclusion failed_runs get_repo '
               'get_runs get_workflows getenv github html_url name print '
               'pylint_workflow repo runs workflow workflows\n'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=491,
          lineno=1,
          tokens=232,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="# I used ChatGPT to generate these descriptions, if it doesn't "
               "match Sim's lore please open a PR, I welcome any changes :)# "
               'noinspection SqlNoDataSourceInspectionIn the sun-drenched '
               'neighborhood of Oasis Springs, Travis Scott was known as a '
               'tech-savvy whiz kid with a magnetic personality.A young adult '
               'with an unquenchable thirst for knowledge, he had already made '
               'his mark in the world of programming and video gaming, swiftly '
               'climbing the ranks of expertise.Sharing a home with his '
               'equally ambitious roommates, Mitchell Kalani and Gavin '
               'Richards, Travis had found a perfect balance between his work '
               'as a Live Chat Support Agent and his ever-growing circle of '
               'friends.Among them, Liberty Lee was a particularly close '
               'confidante, sharing not only a bond of friendship but also a '
               'mutual understanding of the challenges and rewards that came '
               'with their chosen paths.With his charm, wit, and '
               'determination, Travis Scott was destined for great things in '
               'the fast-paced realm of technology and innovation.Gael '
               'Gonzalez, a fun-loving individual with an infectious zest for '
               'life, often found himself surrounded by friends and family, '
               'filling the room with laughter and warmth.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=492,
          lineno=14,
          tokens=246,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His passion for cooking knew no bounds, as he eagerly '
               'experimented with new recipes, fusing flavors to create '
               "culinary masterpieces.A natural-born entertainer, Gael's wit "
               'and charm captivated those around him, while his keen sense of '
               'style never failed to leave an impression.Though his '
               'dedication to his craft was unwavering, Gael knew the '
               'importance of balance, frequently embarking on thrilling '
               'outdoor adventures and unleashing his inner romantic to shower '
               'his partner with love and affection.As a steadfast friend and '
               "empathetic listener, Gael's dream of owning a restaurant one "
               'day seemed to be just another milestone in his journey, a '
               'testament to his boundless love for life and the people he '
               'cherished.Tank Grunt, a man of unwavering discipline and '
               'military prowess, stands out amongst the peculiar inhabitants '
               'of the enigmatic Strangetown neighborhood.With his '
               "unmistakable buzz cut and rugged, chiseled features, Tank's "
               'no-nonsense demeanor is mirrored in his choice of utilitarian '
               'attire.A testament to his military upbringing, he boasts '
               'exceptional fitness skills, dedicating his leisure hours to '
               'achieving peak physical condition.Though not one to prioritize '
               'social engagements, Tank remains fiercely loyal to a select '
               'few kindred spirits who share his unyielding values.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=493,
          lineno=24,
          tokens=239,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In matters of the heart, he is drawn to those who, like him, '
               "find solace in order and structure.Tank's unrelenting "
               'commitment to his career is the driving force behind his '
               'ambition to ascend the ranks of the military hierarchy, '
               'rendering him a character as intriguing as he is '
               'formidable.Loki Beaker, a mischievous and brilliant man, made '
               'his home in the peculiar town of Strangetown.His eccentric '
               'personality and fervent passion for science were well-known '
               'among the townsfolk.With hair as fiery as his intellect, and '
               'skin as pale as his laboratory walls, Loki was an easily '
               'recognizable figure.As a steadfast member of the Beaker '
               'family, he cherished his wife, Circe, and their daughter, '
               'Erin, deeply.A career in the scientific field fed his '
               'relentless curiosity and love for experimentation.In his spare '
               'time, Loki could be found tinkering with peculiar gadgets, '
               'conducting groundbreaking experiments, or crafting bizarre '
               'inventions.His penchant for pranks often complicated his '
               'relationships with others, but in the end, his loyalty to his '
               "friends and family always shone through.Loki Beaker's "
               'unpredictable nature and devotion to those he loved made him '
               'an unforgettable resident of Strangetown.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=494,
          lineno=38,
          tokens=246,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Buck Grunt, hailing from the enigmatic neighborhood of '
               'Strangetown, is a young man caught in the crossfire between '
               "his family's military heritage and his own dreams.As the "
               "youngest of three brothers, Buck can't help but feel eclipsed "
               'by their accomplishments, all the while yearning for a future '
               'in professional gaming.His short, brown hair and casual attire '
               'of a t-shirt and jeans speak to his easy-going nature.When not '
               'engrossed in video games with his friends, Buck finds solace '
               'in creative pursuits such as painting and writing, albeit '
               'often at the expense of his academics.His connection with his '
               'best friend, Jill Smith, deepens with a mutual, yet unspoken, '
               'romantic interest.Despite the hardened exterior that seems to '
               "run in the Grunt family, Buck's kindness and willingness to "
               "help others shine through.In the shadow of his family's "
               'expectations, Buck dreams of breaking free from the weight of '
               'tradition and carving out his own destiny.Sydney Wright, a '
               'young adult with an effervescent personality, was known for '
               'her ability to make friends wherever she went.Her creative and '
               'ambitious nature led her to immerse herself in the world of '
               'arts, chasing her dreams in the entertainment industry.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=495,
          lineno=49,
          tokens=239,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Blessed with a natural talent for music, Sydney could often be '
               'found strumming her guitar or practicing her vocal skills, '
               'honing her craft with dedication.Her love for fashion was '
               'evident in her ever-changing wardrobe, as she delighted in '
               "experimenting with diverse styles and ensembles.Sydney's "
               'kind-heartedness and willingness to help others endeared her '
               'to friends and neighbors alike.She cherished her family and '
               'close relationships, spending her free time surrounded by '
               'loved ones or organizing lively gatherings and celebrations.A '
               'fitness enthusiast, Sydney maintained an active lifestyle, '
               'participating in various outdoor activities and '
               'sports.Diligent and focused, Sydney Wright was a character who '
               'tirelessly pursued her goals and dreams, her charisma and zest '
               'for life inspiring those fortunate enough to cross paths with '
               "her.Babs L'Amour, a woman of undeniable allure, captivated the "
               'hearts of those around her with her fiery red hair and '
               'enchanting green eyes.Her romantic nature was evident in her '
               'flirtatious conversations and relentless pursuit of love.Babs '
               'had a gift for nurturing relationships and brought people '
               'together, fostering connections in her community.An avid art '
               'lover, she could often be found in art galleries, or '
               'expressing herself through music and other creative pursuits.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=496,
          lineno=61,
          tokens=245,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='With aspirations of stardom, her charisma and creativity left '
               'audiences spellbound.However, Babs did have a penchant for '
               'gossip, delighting in the occasional whisper about the lives '
               'and loves of her fellow townspeople.In a world full of '
               "ordinary characters, Babs L'Amour was a passionate and "
               "captivating force to be reckoned with.Bjorn Tu'Rock, with his "
               'bold personality and distinctive appearance, never failed to '
               'stand out in a crowd.His stylish hairstyle and fashionable '
               'clothing spoke of a man who knew how to make an impression.A '
               'social butterfly, Bjorn easily engaged in conversations, his '
               'infectious sense of humor and charisma drawing people to him '
               'like moths to a flame.Ambitious and career-driven, he spent '
               'long hours honing his skills and pursuing his goals with '
               'unwavering dedication.Yet, at his core, Bjorn was a family man '
               'who cherished his loved ones above all else, providing them '
               'with love and encouragement as a supportive partner and '
               'parent.An active soul, he thrived on outdoor activities and '
               "sports, keeping himself fit and healthy.Bjorn Tu'Rock was a "
               'well-rounded and unforgettable character, admired for his '
               'unique blend of charisma, ambition, and devotion to those who '
               'mattered most.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=497,
          lineno=75,
          tokens=229,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Gladys Morse was the embodiment of creativity and artistry, '
               'her fingers dancing gracefully across the strings of her '
               'guitar or leaving trails of vibrant colors on a canvas.Her '
               'laughter was contagious, her friendly and outgoing nature '
               'drawing people towards her like moths to a flame.With dreams '
               'of raising a big, loving family, she filled her home with '
               'hearty meals crafted from innovative recipes that she eagerly '
               'shared with friends and family.Her backyard was a lush '
               'paradise, a testament to her green thumb and passion for '
               'gardening.A true romantic at heart, Gladys found herself swept '
               'up in the adventure of seeking her soulmate, her eyes always '
               'twinkling with the promise of love.Ever eager to learn, she '
               'devoured knowledge, continuously honing her skills to scale '
               'the heights in her chosen profession.In all, Gladys Morse was '
               'a multifaceted woman, her zest for life and diverse interests '
               'painting her story in vivid hues.Morgan Park was the '
               'embodiment of charm and creativity, with an artistic flair '
               'that seemed to flow effortlessly through their '
               'fingertips.Their friendly demeanor acted as a magnet, drawing '
               'in neighbors and strangers alike, transforming them into '
               'friends and confidants.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=498,
          lineno=86,
          tokens=231,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Ambition coursed through Morgan's veins, driving them to seize "
               'every opportunity to improve their skills and achieve their '
               'goals, often burning the midnight oil in the pursuit of '
               'greatness.When they managed to steal a moment for themselves, '
               'they found solace in the nurturing embrace of their '
               'flourishing garden, or lost themselves in the vibrant strokes '
               'of a paintbrush.Their adventurous spirit craved the great '
               'outdoors, leading them on hikes and fishing trips, while their '
               'quirky humor never failed to delight those around them.A '
               'fervent animal lover, Morgan opened their heart and home to '
               'any creature in need, and their dedication to family was '
               'evident in the love and support they offered without '
               'hesitation.In a world full of chaos, Morgan Park was a beacon '
               'of warmth, passion, and unyielding determination.Kasen Henry '
               'was a true artistic soul, his hands perpetually stained with '
               'the vibrant hues of his latest masterpiece.His eyes, filled '
               'with the tenderness of a hopeless romantic, eagerly searched '
               'for the one person who could complete his picturesque '
               'life.With a captivating charm and a razor-sharp wit, Kasen '
               'effortlessly attracted friends, creating an intricate tapestry '
               'of connections that he cherished deeply.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=499,
          lineno=96,
          tokens=238,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His love for life extended to the earth itself, as he '
               'carefully cultivated his garden and welcomed stray animals '
               'into his warm embrace.Perfectionism coursed through his veins, '
               'occasionally threatening to overwhelm him, but Kasen would '
               'always emerge victorious, surrounded by the dazzling array of '
               'his fashionable creations.At his core, Kasen was a family man, '
               'ensuring that his kin thrived in the glow of his love and '
               'support.Yet, there was a mischievous glint in his eye, a '
               'testament to the playful pranks he delighted in weaving '
               'throughout his extraordinary life.Liberty Lee, a spirited '
               'young woman with a shock of short, red hair and signature '
               'glasses, made her home in the bustling town of Willow '
               'Creek.Her cheerful and ambitious nature found a perfect outlet '
               'in her love for science, as she aspired to venture into the '
               'cosmos as an astronaut.Liberty shared her abode with her '
               'friends Travis Scott and Summer Holiday, the household forever '
               'brimming with laughter and lively conversations.Her quick wit '
               'and high logic skills propelled her to excel in her career as '
               'a technician, while her leisure hours were spent playing video '
               'games, tinkering with gadgets, and gazing at the stars through '
               'her telescope.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=500,
          lineno=106,
          tokens=237,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A hopeless romantic at heart, she yearned for love, often '
               "stealing glances at her roommate, Travis.Liberty Lee's vibrant "
               'personality and unquenchable thirst for knowledge made her a '
               'captivating presence at any social event, embodying the '
               'essence of adventure and exploration.Bella Goth, a captivating '
               'and enigmatic woman, was the epitome of elegance and '
               'mystery.As a prominent member of the distinguished Goth '
               'family, her life seemed to revolve around her husband, '
               'Mortimer, and their two children, Cassandra and '
               "Alexander.Bella's striking appearance, often adorned in a "
               'long, flowing red dress and black gloves, was only matched by '
               'her unique and intricate updo - a perfect complement to her '
               'dark red lipstick and winged eyeliner.With an aspiration for a '
               "successful lineage, Bella focused on her family's prosperity "
               'and well-being, exhibiting romantic, family-oriented, and '
               'creative traits.However, whispers of her intriguing '
               'relationships with others, such as the notorious Don Lothario, '
               'only added to the enigma that surrounded her.But rumors '
               'swirled around her sudden disappearance, leaving behind a '
               'trail of whispers and conjecture.Some whispered of the '
               'supernatural, hinting at hidden secrets and occult '
               'involvement.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=501,
          lineno=117,
          tokens=230,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Bella Goth remained an enigma, a woman whose presence held an '
               'ethereal quality that intrigued all who crossed her path.Betty '
               'Newbie, with her vivacious smile and fiery red hair, was the '
               'embodiment of warmth and friendliness.She approached life with '
               'an insatiable zest, always eager to forge new connections and '
               'explore the world around her.As one half of an iconic couple, '
               'she and her husband Bob Newbie, stood as the epitome of love '
               "and partnership.Betty's amiable nature and quick wit made it "
               'easy for her to pick up new hobbies and skills, endearing her '
               'to everyone she met.Her casual, yet comfortable fashion '
               'choices - often a cozy sweater and jeans - only added to her '
               'approachable charm.With aspirations of becoming a friend to '
               "all, Betty's outgoing and sociable disposition made her a "
               'beloved figure in her community, leaving a lasting impression '
               'on the hearts of those fortunate enough to cross her '
               'path.Holly Vinedal, an elegant and sophisticated woman, was '
               'renowned for her love of nature and exceptional gardening '
               'skills.With every graceful stride, Holly exuded charm and '
               'intelligence, qualities that effortlessly drew others into her '
               'orbit.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=502,
          lineno=130,
          tokens=243,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='As an aspiring freelance botanist, she dedicated her days to '
               'nourishing the lush gardens that enveloped her home, a '
               'harmonious fusion of modern and rustic design.With a heart as '
               'inviting as her verdant surroundings, Holly delighted in '
               'hosting garden parties, generously sharing her extensive '
               'knowledge of plants with friends and neighbors.A hopeless '
               'romantic, she often found herself daydreaming of a soulmate '
               'who shared her deep-rooted passion for the natural world.In '
               'her enchanting haven, Holly skillfully blended her culinary '
               'and mixology talents, crafting inventive recipes using the '
               "freshest ingredients from her garden.Indeed, Holly Vinedal's "
               'very essence seemed inextricably intertwined with the thriving '
               'greenery that defined her life.Hunter Evans is a charismatic '
               'and outgoing young man who loves to make friends and socialize '
               'with others.He has a natural talent for making people feel at '
               'ease, thanks to his friendly demeanor and genuine interest in '
               'their lives.Hunter is also quite ambitious, always seeking '
               'ways to advance his career and improve his skills.He is a true '
               'romantic, believing in love and dedicating himself completely '
               'to his significant other.As an animal lover, Hunter can often '
               'be found spending time with his pets or volunteering at the '
               'local animal shelter.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=503,
          lineno=142,
          tokens=237,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In his spare time, he enjoys playing sports, especially '
               'soccer, and staying fit through exercise.Hunter has a penchant '
               'for fashion and can often be found shopping for the latest '
               'trends or experimenting with his own unique style.Despite his '
               'busy social life, Hunter values his family and friends above '
               'all else and is a dedicated and supportive partner, sibling, '
               'and friend.With his natural charm, determination, and passion '
               'for life, Hunter Evans leaves a lasting impression on everyone '
               'he meets.Farrah Nouvel, a woman of style and ambition, never '
               'fails to turn heads with her bold and fashionable '
               'ensembles.Her effervescent personality naturally draws people '
               'in, making her the life and soul of every gathering.Besides '
               "being an aspiring artist, Farrah's creative passions span "
               'across painting, photography, and interior design, as she '
               'tirelessly hones her skills and sells her masterpieces to '
               'sustain her livelihood.With a heart full of love for her '
               'family, she cherishes each bond and never hesitates to express '
               'her devotion.A hopeless romantic, Farrah continuously searches '
               'for the one who will sweep her off her feet and understand her '
               'generous spirit.Her curiosity for diverse cultures and '
               'culinary adventures only adds to her charm.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=504,
          lineno=154,
          tokens=236,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Driven by her ultimate dream of achieving fame as a painter '
               'and living in a luxurious abode surrounded by her loved ones, '
               "Farrah Nouvel's life is a vibrant canvas of her own "
               'making.Armand DiAggro, a stylish and confident individual, '
               'always knew how to make a statement with his bold fashion '
               'choices and flair for the dramatic.His unique hairstyle and '
               'striking facial features set him apart from the crowd, while '
               'his outgoing nature and ability to make friends quickly made '
               'him a frequent guest at the trendiest spots in town.Ambitious '
               'and determined, Armand constantly strove for success in his '
               'career and personal life, indulging in gourmet meals and '
               'expensive hobbies to satisfy his love for the finer things in '
               'life.A hopeless romantic at heart, he never hesitated to '
               'pursue passionate relationships and fervent love '
               'affairs.Though his hot-headed temper could surface from time '
               'to time, he generally remained well-liked and respected by his '
               'peers.Armand took great pride in maintaining his toned '
               'physique, dedicating his free time to fitness and '
               'self-improvement.Charismatic and captivating, Armand DiAggro '
               'fearlessly stood out from the crowd, leaving his indelible '
               'mark on the world.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=505,
          lineno=166,
          tokens=242,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In the peculiar neighborhood of Strangetown, Johnny Smith '
               'stood out like a beacon with his vibrant green skin, a '
               'testament to his unique heritage.The son of Pollination '
               'Technician 9 and Jenny Smith, Johnny was blessed with an '
               'adventurous spirit that was only matched by his insatiable '
               'curiosity for the cosmos.As a young adult, he was the epitome '
               'of a well-rounded individual, gifted with the qualities of a '
               'genius, a kind heart, and an unyielding energy.While his '
               'fascination with rocket science propelled him to pursue a '
               'career as an astronaut, his heart belonged to the enigmatic '
               'Ophelia Nigmos.Together, they navigated the tumultuous waves '
               'of their passionate romance, as Johnny continued to chase his '
               'ultimate dream of becoming a space ranger, etching his name '
               'among the stars.Eliza Pancakes resided in the quaint Willow '
               "Creek neighborhood, her presence as vibrant as the town's lush "
               'greenery.A passionate culinary artist, she strived to achieve '
               'the prestigious title of Master Chef, her nimble hands skilled '
               'in both cooking and gardening.With a cheerful, neat, and '
               'outgoing personality, Eliza easily captured the hearts of her '
               'many social media followers as she shared her life experiences '
               'with them.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=506,
          lineno=176,
          tokens=213,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Leisurely afternoons were spent in the company of friends, '
               'partaking in various social activities that brought joy and '
               'laughter to all.Yet beneath this seemingly perfect exterior '
               'lay a tense and tumultuous relationship with her husband, Bob '
               'Pancakes.Their union was marred by arguments and '
               'disagreements, their love story far from a fairytale.Despite '
               'these struggles, a resilient Eliza held onto her dreams of '
               'creating a happy and loving family.A complex character, her '
               'aspirations and challenges intertwined, Eliza Pancakes was a '
               'captivating enigma in her own right.James Stock was the '
               'epitome of charisma, a man who thrived in social situations '
               'and effortlessly drew others into his orbit.With a sculpted '
               'physique honed by hours spent in the gym and countless miles '
               'jogging through the neighborhood, he exuded an air of '
               'confidence and ambition that others found irresistible.In the '
               'quiet moments stolen between his professional pursuits and '
               'vigorous fitness routine, James found solace in the culinary '
               "arts, skillfully wielding his chef's knife to create "
               'mouthwatering feasts and experiment with new recipes.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=507,
          lineno=186,
          tokens=229,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A hopeless romantic at heart, James was always on the lookout '
               'for that soul-stirring connection, that elusive spark that '
               'would ignite the pages of his own personal love story.His '
               'bewitching charm and striking good looks granted him a '
               'magnetic presence wherever he went, whether exploring distant '
               'lands on whirlwind adventures or savoring the simple pleasures '
               'of a good book or film in the sanctuary of his home.With '
               'impeccable taste and an unerring eye for the latest trends, '
               'James Stock was a man who truly had it all â\x80\x93 a '
               'magnetic personality, a zest for life, and a heart brimming '
               'with dreams.Don Lothario, a striking and captivating young '
               'man, was notorious for his amorous escapades, as he '
               'effortlessly charmed the hearts of many in the sun-drenched '
               'Oasis Springs neighborhood.Residing in an elegant, '
               'contemporary abode that matched his charismatic persona, Don '
               'worked diligently as an orderly, with aspirations of one day '
               'becoming the Chief of Staff.His romantic conquests were the '
               'talk of the town; the beautiful Caliente sisters and enigmatic '
               'Bella Goth, just a few of the many who had fallen under his '
               'spell.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=508,
          lineno=194,
          tokens=244,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Blessed with an Alluring trait and an insatiable appetite for '
               'love, Don was a true Serial Romantic, his flirtatious nature '
               'and outgoing demeanor allowing him to connect with others with '
               'ease.However, his active lifestyle and noncommittal ways often '
               'led to a tumultuous love life, as he struggled to maintain '
               'long-lasting relationships.Don Lothario embodied the '
               'quintessential \\"Casanova\\" archetype, a tantalizing yet '
               'elusive character whom people either yearned to pursue or '
               'sought to avoid at all costs.Nova Curious was an enigmatic '
               'figure with an insatiable thirst for knowledge, standing out '
               'in any crowd with her fiery red hair and eclectic attire that '
               'perfectly mirrored her unconventional charm.A brilliant '
               'scientist and an ardent explorer of the unknown, she dedicated '
               'her life to unraveling the mysteries of the universe and '
               'sharing her wisdom with those who shared her unquenchable '
               'curiosity.In her relentless quest for enlightenment, Nova '
               'spent countless hours tinkering with intricate gadgets, her '
               'nimble fingers weaving together the threads of innovation with '
               'every new invention.Driven by ambition, she ceaselessly sought '
               'out challenges and opportunities for growth, her analytical '
               'mind thriving on the thrill of solving complex problems and '
               'devising inventive solutions.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=509,
          lineno=203,
          tokens=249,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Her warm, outgoing demeanor attracted a diverse circle of '
               'friends and acquaintances, each captivated by her voracious '
               "spirit of adventure.Nova Curious' very essence was a testament "
               'to the beauty of discovery, her name forever etched in the '
               'annals of those who dared to push the boundaries of human '
               'understanding.Sophia Jordan radiated an unmistakable zest for '
               'life as she roamed through the city, her genuine smile and '
               'vibrant aura drawing people into her orbit effortlessly.Her '
               'ensembles, always on the cutting edge of fashion, demonstrated '
               'her flair for self-expression and her innate understanding of '
               "the human desire for connection.Sophia's natural leadership "
               'abilities shone through in her unwavering dedication to '
               'personal growth and her willingness to offer guidance to her '
               'ever-growing circle of friends.A hopeless romantic, she '
               "searched for a kindred spirit to share in life's adventures, "
               'her witty humor and warm personality making her an '
               "unforgettable presence at every gathering.Sophia's soul "
               'yearned for creativity, finding solace in the fluid strokes of '
               'a paintbrush or the tantalizing flavors of her latest culinary '
               'concoction.Ambitious and driven, Sophia Jordan was a force to '
               'be reckoned with, her charisma and determination propelling '
               'her towards a life of extraordinary achievements.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=510,
          lineno=215,
          tokens=234,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Seth Pinkerton is a creative and ambitious individual who '
               'aspires to become a renowned author, known for his distinctive '
               'pink hair and unique fashion sense that sets him apart from '
               'the crowd.A social butterfly, Seth easily engages in '
               'conversations, making friends and occasionally finding himself '
               'in romantic entanglements.He has a penchant for gourmet '
               'cooking and enjoys hosting dinner parties at his modern, '
               'stylish abode.With a rebellious streak, Seth might '
               'occasionally break the rules or indulge in some mischief, but '
               'as a perfectionist, he strives to excel at any task he '
               'undertakes, whether it be writing, painting, or even '
               'gardening.His quirky sense of humor is appreciated by his '
               'friends, often making him the life of the party.Seth balances '
               'his busy social life and creative pursuits by practicing yoga '
               'and meditation to keep his mind sharp and focused.Despite his '
               'wild side, Seth Pinkerton is a caring and compassionate '
               'individual who always looks out for his loved ones and is '
               'eager to lend a helping hand.Feu, a charming and sophisticated '
               'individual, was renowned for his impeccable taste in fashion '
               'and design.His dark, wavy hair and piercing green eyes made '
               'him the center of attention wherever he went.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=511,
          lineno=226,
          tokens=236,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="A natural-born leader, RÃ©my's charismatic personality "
               'effortlessly drew people to him.As a successful entrepreneur, '
               'his ambition and intelligence had amassed him considerable '
               'wealth, allowing him to reside in one of the most luxurious '
               'houses in town.Despite his success, he remained humble, '
               'treating others with kindness and respect.A connoisseur of the '
               'finer things in life, RÃ©my held a deep appreciation for '
               'gourmet cuisine, classical music, and fine art.When not '
               'attending social events and mingling with the influential, he '
               'would often be found exploring new cultures and experiences as '
               'an avid traveler.Ultimately, RÃ©my St.Feu was the embodiment '
               'of class, style, and success.Millie Bobby Brown, a talented '
               'and ambitious young actress, dreams of making it big in the '
               'acting world.With her cheerful and outgoing personality, she '
               'easily befriends people of all walks of life.Millie sports a '
               'unique sense of style, effortlessly blending casual and chic '
               'outfits.As a fitness enthusiast, she adores working out and '
               'staying in shape, frequenting the gym or going for '
               'revitalizing jogs.With a curious and creative spirit, Millie '
               'relishes exploring new hobbies like painting and photography.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=512,
          lineno=240,
          tokens=245,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='She cherishes her family and friends, often hosting lively '
               'gatherings at her cozy abode.Her intelligence and quick wit '
               'enable her to tackle problems and achieve her goals with '
               "ease.Millie's love for animals often finds her adopting pets "
               'or volunteering at the local animal shelter.As a role model to '
               'the younger generation, she strives to make a positive impact '
               'on her community through charity work and activism.Tristen '
               'Palmer, a charismatic and outgoing individual, effortlessly '
               'captivates the hearts of those around him with his magnetic '
               'charm.His evenings are often spent frequenting local hotspots '
               'and forging new connections, making him a beloved figure '
               'amongst both peers and coworkers.A romantic at heart, Tristen '
               'navigates the complexities of his love life with the same '
               'determination he applies to his flourishing career in the '
               'business or political sphere.His athletic prowess is evident '
               'in his devotion to fitness and participation in various '
               'sports, yet he never neglects the importance of family and '
               'loyalty in his life.A hidden artistic talent lies beneath '
               "Tristen's vivacious exterior, revealing itself in moments of "
               'painting or music, continually surprising those closest to '
               'him.In a world where striking a balance is crucial, Tristen '
               'Palmer has mastered the art of harmonizing work, play, and '
               'relationships.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=513,
          lineno=254,
          tokens=222,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Steve Fogel, a creative and ambitious soul, longs to make his '
               'mark in the art world with his captivating, colorful '
               'paintings.With an outgoing nature that draws others into his '
               'orbit, he can often be found meandering through art galleries '
               'and museums, seeking inspiration and connection with fellow '
               'artists.His artistic spirit is reflected not only in the '
               'vibrant hues of his attire but also in the way he chooses to '
               'live, from the open-concept, modern design of his abode to his '
               'penchant for hosting dinner parties where he delights friends '
               'with his culinary prowess.An avid gardener, Steve lovingly '
               'tends to his plants, incorporating the fresh produce into his '
               'innovative recipes, while also dedicating time to passions '
               'like playing the guitar and dancing.A romantic at heart, Steve '
               "dreams of finding that perfect someone to share his life's "
               'journey, building a family as beautiful and vivid as the '
               'masterpieces he creates.Mortimer Goth, a man of intellect and '
               'mystery, found solace in the eerie and the obscure.His '
               'brooding appearance, complete with a distinguished goatee and '
               'somber attire, spoke volumes of his enigmatic persona.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=514,
          lineno=263,
          tokens=216,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Mortimer was a loving husband to his ethereal wife, Bella, and '
               'a doting father to their two children, Cassandra and '
               'Alexander.When not tending to his family, Mortimer submerged '
               'himself in the world of the paranormal, arts, and literature, '
               'using his passion to fuel a successful career as a writer.His '
               'published works adorned the bookshelves of their grand '
               'residence, the hauntingly beautiful Goth Manor, nestled within '
               'the picturesque town of Willow Creek.As one of the wealthiest '
               'and influential families in their world, the Goths were both '
               "revered and admired, with Mortimer's captivating presence "
               'continuing to fascinate all who crossed his path.Gavin '
               'Richards was a creative and outgoing soul with aspirations '
               'that reached for the heavens, as he longed to make a name for '
               'himself in the world of art.A natural talent for painting '
               'coursed through his veins, leading him to spend countless '
               'hours immersed in the creation of awe-inspiring masterpieces.A '
               'hopeless romantic, Gavin often found himself daydreaming about '
               'the day he would find his true love and settle down into a '
               'life of bliss.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=515,
          lineno=272,
          tokens=213,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His affable nature and cheerful personality made him a '
               'well-loved figure within his community, where he relished in '
               'socializing and forging lasting friendships.With an eye for '
               'fashion, Gavin was always impeccably dressed in the latest '
               'trends, his unique flair for style evident in every '
               'ensemble.Though his artistic temperament was undeniable, Gavin '
               'possessed an ambitious spirit that drove him to seek success '
               'in all facets of his existence.A true friend, he was ever '
               "ready to lend a helping hand to those in need.Gavin's hobbies "
               'spanned from strumming the guitar to attending art exhibitions '
               'and exploring the wonders of the world around him.In essence, '
               'Gavin Richards was a charismatic and well-rounded individual '
               'with a future that shone as brightly as the stars above.Gabby '
               'Gonzalez, an effervescent social butterfly, danced her way '
               'through life as the life of every party.Her charismatic '
               'presence, combined with her profound passion for music, led '
               'her to dazzle audiences at various events as a talented '
               'DJ.With ambitions of becoming a professional entertainer, '
               'Gabby devoted herself to refining her artistry.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=516,
          lineno=283,
          tokens=224,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Her eye-catching wardrobe and exceptional fashion sense made '
               'her a standout figure in any crowd, while her love for dance '
               'added an extra layer of allure to her captivating '
               'performances.This culinary enthusiast savored each opportunity '
               'to explore diverse cuisines, constantly experimenting with new '
               'recipes in the comfort of her own home.Yet, beneath the '
               'glittering surface of her vibrant social life, Gabby remained '
               'deeply devoted to her family, treasuring every moment spent '
               'with her loved ones.In essence, Gabby Gonzalez was a vivacious '
               'and ambitious soul, ceaselessly seizing opportunities to enjoy '
               'life and leave a lasting impression on those fortunate enough '
               'to cross her path.Moose Dubros was an eccentric and creative '
               'individual who loved to stand out from the crowd.Possessing a '
               'unique fashion sense, he often sported bold patterns and '
               'bright colors.Sociable by nature, Moose enjoyed the company of '
               'others and made new friends wherever he went.He had a natural '
               'talent for painting and dedicated much of his free time to '
               'creating masterpieces at his easel.A true food connoisseur, he '
               'was always eager to try out new recipes and frequent the best '
               'restaurants in town.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=517,
          lineno=294,
          tokens=243,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Despite his outgoing nature, Moose harbored a soft spot for '
               'animals and often volunteered at the local animal shelter.A '
               'hopeless romantic, he was on a constant quest to find that '
               'special someone with whom he could share his life.With a '
               'quirky sense of humor, Moose was always up for a good laugh or '
               'a practical joke.Above all, he valued his family and friends, '
               'making him a loyal and dependable character in the tapestry of '
               'life.Cassandra Goth, a dark and enigmatic young woman, stood '
               'out among her peers with her striking gothic attire that '
               'seemed to mirror the shadows that lingered around her.Her long '
               'black hair cascaded down her back, framing her pale visage and '
               'deep, penetrating eyes that seemed to hold a world of '
               'secrets.Born into the enigmatic Goth family, Cassandra was the '
               'cherished daughter of Mortimer and Bella, and the protective '
               'older sister of young Alexander.A prodigy with aspirations of '
               'musical genius, she could often be found passionately playing '
               'her violin, losing herself in the soul-stirring melodies.Her '
               'innate creativity, love for music, and solitary nature '
               'combined to shape her into an extraordinary artist, yet her '
               'relationships were often challenging as she wrestled to find '
               'love and maintain friendships.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=518,
          lineno=305,
          tokens=232,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Despite her introverted and somber disposition, Cassandra's "
               'presence added depth, intrigue, and a touch of darkness to the '
               'vibrant tapestry of life.Sofia Martinez, a vibrant young '
               'adult, resides in the sun-soaked, arid landscape of Oasis '
               'Springs.As a member of the eclectic Roomies household, she '
               'shares her abode with an array of fascinating '
               "roommates.Sofia's radiant and outgoing nature allows her to "
               'effortlessly forge friendships and connect with others, driven '
               'by her aspiration to become a Friend of the World.A true '
               'epicurean, she revels in sampling diverse cuisines and '
               'frequenting a variety of restaurants.This passion for food has '
               'led her to a part-time job in the culinary field, perfectly '
               "suiting her gastronomic interests.Sofia's unique sense of "
               'style is evident in her eye-catching, fashionable '
               'ensembles.Known to be a quick learner, she rapidly acquires '
               'new skills, excelling particularly in cooking and '
               'charisma.These talents not only impress her friends but also '
               'bolster her professional success.Ultimately, Sofia Martinez is '
               'an effervescent and amiable character who cherishes novel '
               'experiences and forming meaningful connections within her '
               'captivating world.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=519,
          lineno=319,
          tokens=226,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Bob Pancakes resided in the quaint neighborhood of Willow '
               'Creek, where he shared a cozy, domestic household with his '
               'wife, Eliza Pancakes.With a penchant for the culinary arts, '
               'Bob was a man of simple tastes, pursuing his aspiration to '
               'become a Master Chef, one delectable dish at a time.His '
               'laid-back personality often found him shirking strenuous '
               'activities, preferring the calming hum of the kitchen as he '
               'honed his skills.While he and Eliza shared a strong bond, '
               'their occasional disagreements only served to strengthen their '
               "relationship.Bob's attire, consisting of a casual hoodie, "
               'jeans, and sneakers, reflected his easygoing nature, while his '
               'short brown hair and glasses added a touch of unassuming '
               'charm.In his leisure time, he found solace in fishing, a '
               'pastime that aligned perfectly with his relaxed '
               'demeanor.Lovable and relatable, Bob Pancakes was a man who '
               "thrived on life's simple pleasures.Kat Jenkins is a vibrant, "
               'artistic soul with an unquenchable thirst for creative '
               'expression.Her eclectic wardrobe bursts with color, '
               'effortlessly capturing her imaginative spirit and turning '
               'heads wherever she goes.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=520,
          lineno=330,
          tokens=220,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='She shares her abode with Whiskers, her equally mischievous '
               'feline companion, and together they form an inseparable duo.At '
               "the core of Kat's lively persona is a romantic heart, yet her "
               'fierce independence often drives her to solitude, where she '
               'can lose herself in the vivid world of her paintings.A social '
               'butterfly, Kat flutters from one gathering to another, her '
               'outgoing nature and passion for adventure resonating deeply '
               'with her tight-knit circle of friends.This dynamic artist is '
               'also a culinary enthusiast, delighting in the exploration of '
               'new flavors and whipping up her own innovative recipes.A true '
               'night owl, Kat finds solace in the stillness of late hours, '
               'when she can either immerse herself in her craft or engage in '
               'heartfelt conversations with her cherished friends.Above all, '
               'Kat Jenkins is the epitome of a compassionate and caring '
               'individual, always eager to extend a helping hand and offer a '
               'listening ear to those in need.Bob Newbie, an endearing slob, '
               'navigates his way through life alongside his wife, Betty '
               'Newbie, as the epitome of a beginner couple.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=521,
          lineno=339,
          tokens=242,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Defined by his disheveled appearance, Bob's iconic green shirt "
               'and blue pants seem to mirror the chaos of his unkempt home, a '
               'place where disorder runs rampant and cleanliness is a foreign '
               'concept.However, beneath the mess lies a man with a passion '
               'for food, as his discerning palate and culinary expertise '
               'drive him to pursue a career as a Master Chef.His cheerful '
               'disposition and friendly nature not only make him a delightful '
               'companion but also allow him to form lasting connections with '
               'those around him.Together, Bob and Betty carve out their '
               'humble abode in the heart of the arid Oasis Springs '
               'neighborhood, a testament to their resilience and adaptability '
               'as they embrace the challenges of their new '
               'environment.Indeed, the very name \\"Newbie\\" serves as a nod '
               'to their ongoing journey, as they boldly represent those who '
               'are new to navigating the complexities of life.Circe Beaker, a '
               'striking figure with vibrant purple hair and a lab coat, '
               'resides in the enigmatic town of StrangeVille where she plays '
               'an essential role in the unfolding story.A brilliant and '
               'dedicated scientist, Circe spends countless hours conducting '
               'her groundbreaking research at the StrangeVille Science '
               'Facility, alongside her equally ambitious husband, Loki '
               'Beaker.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=522,
          lineno=348,
          tokens=245,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="The Beaker family's legacy spans generations, with their "
               'eccentric personalities and relentless pursuit of knowledge '
               'setting them apart.Fueled by her Knowledge aspiration and a '
               "focus on the Nerd Brain, Circe's inquisitive nature frequently "
               'results in bizarre experiments that both intrigue and mystify '
               "her neighbors.But, her mischievous streak doesn't end there; "
               'Circe delights in playing pranks on those around her, '
               'endearing her to the townspeople who have come to adore her '
               "peculiar tendencies.Circe Beaker's enigmatic presence, "
               'captivating backstory, and unyielding thirst for knowledge '
               'make her an unforgettable character in the unfolding tale of '
               'StrangeVille.Mary-Sue Pleasant, a career-driven woman with an '
               'unwavering focus on wealth and material possessions, is known '
               'for her steadfast determination to climb the corporate '
               'ladder.Married to the unfaithful Daniel Pleasant, their '
               'tumultuous union is constantly teetering on the edge of '
               'collapse.Together, they are the parents of twin daughters, '
               'Angela and Lilith, two polar opposites who frequently find '
               "themselves at odds.While Angela is the apple of her mother's "
               'eye, the rebellious Lilith struggles to forge a bond with '
               'Mary-Sue, often feeling overshadowed and neglected.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=523,
          lineno=358,
          tokens=220,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Despite the chaos that seems to perpetually surround her, '
               'Mary-Sue is a gifted cook, using her culinary talents to unite '
               'her fractured family.Her unwavering dedication to her loved '
               'ones and her own ambitions make her a compelling, complex '
               'character as she navigates the challenges of balancing work, '
               'family, and personal growth.Princess Ess, a regal figure of '
               'elegance and sophistication, was adored and admired by all who '
               'crossed her path.Her majestic presence, often draped in lavish '
               'gowns and adorned with exquisite accessories, exuded grace and '
               'poise.This noble woman had a fervent passion for the arts, and '
               'her calendar was filled with grand events such as balls and '
               'soirees.The refined tastes and luxurious lifestyle of Princess '
               'Ess naturally made her the center of attention and envy.Her '
               'stately home, boasting of opulent furnishings and artistic '
               'masterpieces, mirrored her sumptuous life.Not only was she '
               'well-educated and intelligent, engaging in intellectual '
               'conversations with her peers, but she was also known for her '
               'kindness and benevolence, ever ready to lend a helping hand to '
               'those in need.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=524,
          lineno=368,
          tokens=247,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='The romantic escapades of the princess were often the subject '
               'of fervent gossip and speculation, as many sought to win her '
               'affections.In essence, Princess Ess was the epitome of luxury '
               'and refinement, an iconic and unforgettable figure in her '
               'world.Katrina Caliente, a striking woman with fiery red hair, '
               'embodies passion and vivacity as she navigates life in the '
               'sun-drenched neighborhood of Oasis Springs.As a single mother, '
               'her devotion to her daughters, Nina and Dina, is unwavering, '
               'their shared zest for life and unmistakable appearance forging '
               "an unbreakable bond.Katrina's expertise in the subtle art of "
               'flirtation and her culinary prowess make her a captivating '
               'presence in any social gathering, where she often finds '
               'herself the center of attention.Despite her predilection for '
               'pursuing romantic entanglements with married individuals, a '
               'penchant that frequently stirs tumultuous drama, Katrina '
               'remains steadfast in her commitment to providing for her '
               'family.Driven by her romantic aspirations, her vibrant '
               'personality and fascinating life story render her an '
               'unforgettable character in the tapestry of Oasis Springs.Elle '
               'Canon, a vivacious and outgoing woman, never failed to '
               'captivate those around her with her keen sense of style and '
               'penchant for setting trends.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=525,
          lineno=380,
          tokens=234,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Confident and ambitious, Elle was a force to be reckoned with '
               'as she pursued her goals and navigated the complexities of the '
               'social hierarchy.A true social butterfly, she reveled in the '
               'limelight, attending and hosting lavish parties where her '
               "charm and magnetism drew people to her.Elle's flirty demeanor "
               'and propensity for amorous entanglements had become somewhat '
               'legendary, though her skill as a mixologist, crafting '
               'exquisite cocktails, was just as notable.With a dedication to '
               'maintaining her physical fitness, she could often be spotted '
               'jogging through the park or perfecting her yoga poses.A '
               'creative spirit, Elle explored the worlds of painting and '
               'photography, further adding to her multifaceted persona.Elle '
               "Canon's undeniable charisma left an indelible mark on everyone "
               'she encountered, making her a beloved and unforgettable '
               'character.Jennifer Martinez is a creative soul who thrives on '
               'painting and exploring various artistic techniques.Her strong '
               'family values make her a devoted and nurturing mother to her '
               'two children.Effortlessly charming, Jennifer is a social '
               'butterfly who easily forms connections, becoming the life of '
               'the party at neighborhood gatherings.Her exceptional culinary '
               'skills often find her hosting dinner parties for friends and '
               'family.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=526,
          lineno=392,
          tokens=228,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A fitness zealot, she cherishes her morning runs in the park '
               'and has a keen eye for fashion, setting trends within her '
               'community.As an aspiring writer, Jennifer channels her '
               'boundless imagination and storytelling prowess into her '
               'work.Her romantic nature shines through as she constantly '
               'seeks ways to delight her partner with heartfelt gestures.A '
               "proud adoptive parent to Daisy, a rescue dog, Jennifer's love "
               'for animals is evident.Above all, her compassionate nature and '
               'willingness to help others make Jennifer Martinez a cherished '
               'and esteemed member of her community.Olive Specter, a woman '
               'shrouded in eerie mystique, casts an enigmatic presence '
               'wherever she goes, her pale complexion only intensifying her '
               'ghostly aura.Widowed and haunted by the spectral presence of '
               "her late husband, Earl E.DeMise, Olive's family tree is a "
               'chilling graveyard of dearly departed kin, sparking whispered '
               'rumors of her sinister involvement in their untimely '
               'ends.Dwelling within the ominous walls of Ophelia Villa in the '
               "curious town of Strangetown, Olive's troubled relationship "
               'with her niece, Ophelia Nigmos, adds further tension to the '
               'tale.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=527,
          lineno=403,
          tokens=237,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Olive has a career rooted in the paranormal as a psychic, '
               "Olive's uncanny image captivates those drawn to the macabre, "
               'as they unravel the twisted threads of her dark and complex '
               'narrative.Beneath the shadow of her foreboding reputation, '
               'Olive Specter remains a multifaceted character, infusing '
               'intrigue and depth into the very fabric of her world.Chuck '
               'Cenzo, a charming and outgoing individual, effortlessly '
               'captivated everyone he encountered with his infectious sense '
               'of humor, witty jokes, and comical gestures.A family-oriented '
               'man, he relished in hosting dinner parties and family outings, '
               'where his natural flair for cooking left everyone craving more '
               'of his delectable dishes.As an avid sports enthusiast, Chuck '
               'could often be found flexing his muscles at the local gym or '
               'participating in neighborhood leagues.A hopeless romantic at '
               'heart, he longed to find that special someone with whom he '
               'could share his life, offering unwavering dedication and '
               'passion.Possessing a strong work ethic, Chuck was relentless '
               'in achieving his career goals and providing for his loved '
               'ones; yet, his ambitious nature was tempered by his '
               "appreciation for life's finer pleasures, including fashion and "
               'art.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=528,
          lineno=412,
          tokens=226,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Chuck Cenzo was, without a doubt, a well-rounded individual '
               'whose zest for life made him an absolute joy to be around.Iggy '
               'Pancakes, a young boy hailing from the peculiar town of Willow '
               'Creek, is a bright and noticeable character with his short '
               'blond hair and piercing blue eyes.He belongs to the quirky '
               'Pancakes family, which also includes his parents, Bob and '
               'Eliza Pancakes.As an extroverted and outgoing child, Iggy has '
               'a natural inclination towards making friends, embracing his '
               'role as a social butterfly with remarkable ease.Often seen '
               'sporting a vibrant yellow hoodie adorned with a rocket ship '
               "design, Iggy's wardrobe is a testament to his energetic and "
               'playful nature.Despite enjoying a close bond with his mother, '
               'Eliza, his relationship with his father, Bob, leaves much to '
               'be desired, hinting at underlying family tension.As Iggy '
               'matures, his personality and interests continue to evolve, '
               'shaping him into a multifaceted and lively individual who adds '
               'a unique dynamic to the enchanting world of Willow Creek.Jill '
               'Smith is a cheerful and outgoing individual who loves spending '
               'time with her friends and family.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=529,
          lineno=424,
          tokens=216,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='She has a passion for gardening and can often be found tending '
               'to her plants in her backyard.Jill is a natural-born leader '
               'and enjoys hosting events and gatherings at her home.She has a '
               'tendency to be a little clumsy at times, but her infectious '
               'laugh and warm personality more than make up for it.Jill is a '
               'hard worker and is dedicated to her career, striving for '
               "promotions and success.She's also a bit of a fitness "
               'enthusiast and enjoys hitting the gym to stay in shape.In her '
               'free time, Jill likes to try new recipes and experiment with '
               'cooking, often treating her friends to delicious homemade '
               "meals.She's a hopeless romantic and dreams of one day finding "
               'the perfect partner to settle down with.Jill is a loyal and '
               'caring friend, always there to offer a shoulder to cry on or a '
               'helping hand.Overall, Jill Smith is a well-rounded and '
               'fun-loving individual who brings joy and laughter to those '
               'around her.Pascal Curious, a uniquely brilliant mind, found '
               'himself driven by an insatiable thirst for knowledge and '
               'discovery, destining him for a career in the sciences.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=530,
          lineno=436,
          tokens=227,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Born into the renowned Curious family, Pascal's fascination "
               'with the enigmatic was a natural inheritance, his intelligence '
               'and eccentricity further setting him apart from the '
               'ordinary.Frequently immersed in tinkering with bizarre '
               'inventions or conducting peculiar experiments within the '
               'confines of his home laboratory, Pascal was easily identified '
               'by his vibrant red hair and iconic round glasses.Alongside his '
               'siblings, Vidcund and Lazlo, he forged strong bonds through '
               'their shared intellectual pursuits, delving into the depths of '
               'scientific mysteries.Beyond his earthly interests, Pascal '
               'harbored a profound love for outer space and extraterrestrial '
               'beings, his mastery of logic and handiness skills propelling '
               'him on his cosmic quest.In a world often void of whimsy and '
               'wonder, Pascal Curious served as a beacon of intrigue and '
               'exploration, inviting those around him to unravel the enigmas '
               'of the universe.Laurant Dupre, a sophisticated man with a '
               'penchant for the finer things in life, exudes an air of '
               'elegance with his stylish and up-to-date wardrobe.With a '
               'discerning eye for art, he often immerses himself in the world '
               'of creativity by frequenting museums and galleries.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=531,
          lineno=445,
          tokens=218,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Charismatic and witty, Laurant captures the attention of those '
               'around him, effortlessly drawing them into his orbit.Despite '
               'his luxurious lifestyle, he remains grounded and dedicated to '
               'giving back, volunteering at local charities in his spare '
               'time.As a connoisseur of gourmet cooking, Laurant enjoys '
               'hosting lavish dinner parties for his loved ones, showcasing '
               'his culinary talents.Driven by ambition, he aspires to excel '
               'in his career and climb the corporate ladder, all while '
               'dreaming of finding his soulmate and settling down in a '
               "beautiful, elegant home.Laurant's well-rounded nature, "
               'constant pursuit of growth, and unwavering determination make '
               'him a force to be reckoned with, leaving a lasting impression '
               'on all who have the fortune of crossing his path.With her '
               'vibrant red hair and a cheerful personality, Jasmine Holiday '
               'effortlessly brightened the lives of those around her.Often '
               'found at the community gardens, Jasmine would provide '
               'holiday-event related tasks and challenges for her fellow '
               'townspeople, her infectious charm and fashionable style - '
               'complete with a green top, black skirt, and red tights - '
               'making her a standout presence.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=532,
          lineno=454,
          tokens=235,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='As an event coordinator, her love for socializing and mingling '
               'with others was evident, and she could often be spotted '
               'chatting animatedly with various individuals throughout the '
               "town.Jasmine's green thumb and gardening skills made her an "
               'invaluable resource during the Growfruit Challenge, and her '
               'knack for procuring unique items, such as decorative eggs '
               'during the Spring Challenge, only added to her mystique.Though '
               'not a permanent fixture in the lives of those she touched, '
               "Jasmine Holiday's presence left an indelible mark on each "
               'event she graced, making every occasion all the more enjoyable '
               'and memorable.Johnny Zest, a young adult with a zest for life, '
               'resides in the sunbaked Mirage Canyon neighborhood of Oasis '
               'Springs.As an estranged member of the affluent Landgraab '
               'family, Johnny has found himself carving his own path, '
               "refusing to rely on his family's wealth.With dreams of "
               'becoming a renowned comedian, Johnny has already honed his '
               'comedic skills and possesses an infectious outgoing '
               'personality, drawing others to him with ease.His quirky sense '
               'of style, with its bright colors and bold patterns, is a '
               'reflection of his character, and his ambition fuels his '
               'dedication to pursuing his goals.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=533,
          lineno=463,
          tokens=241,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Choosing to live in a humble trailer home, Johnny demonstrates '
               'his determination to make his mark in the world without the '
               "influence of his family's fortune.Working as an amateur "
               'entertainer, he strives to achieve his aspiration of becoming '
               'a Joke Star, with a passion for making others laugh and an '
               'unwavering resolve to succeed in the world of comedy.Fiona '
               'Whitfield, a vivacious and gifted individual, aspires to etch '
               'her name in the annals of art history.With a paintbrush as her '
               'wand, she conjures up magnificent masterpieces on canvas, '
               'investing hours to ensure their perfection.Exuding an '
               'infectious cheerfulness, Fiona easily befriends those around '
               'her, delighting in their camaraderie.Her siblings hold a '
               'special place in her heart, as she relishes the playful '
               "moments they share.A multifaceted intellect, Fiona's curiosity "
               'spans the realms of science and history alike.Fashion serves '
               'as another avenue for her to express her distinctive style, as '
               'she constantly seeks the latest trends.A firm believer in the '
               "power of true love, Fiona's heart yearns for her destined "
               'soulmate.Her culinary escapades lead her to experiment with '
               'innovative recipes, much to the delight of her loved ones.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=534,
          lineno=475,
          tokens=216,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Possessing an unwavering work ethic, Fiona is determined to '
               'excel both professionally and personally.A doting guardian to '
               'her feline companion, Whiskers, her love for animals extends '
               'to the local shelter, where she volunteers her time nurturing '
               'those in need.Lyla Grunt, a striking and tenacious woman, '
               'hailed from a respected military family, with her vibrant red '
               'hair and piercing green eyes making her a standout figure in '
               'any gathering.Her exceptional intelligence and unwavering '
               'determination propelled her to great heights in her military '
               "career, earning her the admiration of her colleagues.Lyla's "
               'athleticism was no secret either, as she dominated both sports '
               'and fitness contests with her incredible prowess.Yet, beneath '
               'her formidable exterior lay a gentle heart; she cherished '
               'moments tending to her garden and doting on her beloved pet '
               'dog.Loyalty and devotion were her hallmarks, as she never '
               'hesitated to extend a helping hand or support her friends and '
               "family in times of need.Lyla's daring personality was "
               'reflected in her impeccable fashion choices, often donning '
               'military-inspired ensembles and accessories.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=535,
          lineno=485,
          tokens=229,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='All in all, Lyla Grunt was an unforgettable force of nature, a '
               'woman whose passion and dedication left an indelible mark on '
               'all who crossed her path.Malcolm Landgraab, scion of the '
               'prominent and opulent Landgraab family, possessed an ambitious '
               'and materialistic disposition that was both envied and reviled '
               'in equal measure.The young heir, with his snobbish demeanor '
               'and penchant for cruelty, as well as his adoration for music, '
               'made for a complex and intriguing personality.Intent on '
               'amassing a fortune befitting his lineage, Malcolm cut a '
               'dashing figure in his sartorial choices - a dark blue blazer, '
               'crisp white shirt, and an elegant black tie, perfectly '
               'complementing his neatly styled brown hair and piercing light '
               'blue eyes.Adept in the arts of charisma, piano, and logic, '
               "Malcolm's cultured upbringing was evident in his "
               'pursuits.Residing in a luxurious mansion in the prosperous '
               'Oasis Springs neighborhood, Malcolm navigated the intricacies '
               'of high society, forming alliances and relationships with his '
               'fellow denizens, despite his challenging character traits, '
               'adding to the tapestry that was his enigmatic life.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=536,
          lineno=495,
          tokens=216,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Dela Ostrow, an eccentric and vibrant soul, is a gifted artist '
               'with aspirations of gaining fame through her exceptional '
               'talent.Consumed by her passion, she spends countless hours in '
               'her cozy studio, mastering the art of painting and refining '
               'her keen eye for detail.Known for her quirky sense of humor, '
               "Dela's magnetic personality attracts a loyal circle of friends "
               'who cherish her honesty and devotion.As a gracious hostess, '
               'she frequently invites her nearest and dearest to enjoy her '
               'mouthwatering culinary creations during lively dinner '
               'parties.When not wielding a paintbrush or whisk, Dela can be '
               'found seeking inspiration from the beauty of nature in local '
               'parks or marveling at masterpieces in art galleries.Her unique '
               'fashion sense mirrors her individuality, embracing bold '
               'patterns and vivid colors in her clothing and '
               'accessories.Despite her extroverted charm, Dela cherishes her '
               'moments of solitude to recharge and reflect.With her fierce '
               'determination and unwavering spirit, there is no doubt that '
               'Dela Ostrow will achieve her ultimate goal of leaving an '
               'indelible mark on the world through her art.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=537,
          lineno=505,
          tokens=241,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Nervous Subject was an enigmatic individual who stood out in '
               'any crowd due to his peculiar greenish skin tone and a mop of '
               'unruly black curls.He was a peculiar mix of human and alien '
               'genetics, the offspring of the renowned Pollination Technician '
               '9 Smith and the brilliant, yet eccentric Glarn '
               'Curious.Inhabiting the eerie and intriguing Strangetown, '
               'Nervous found himself living amongst the sinister Beaker '
               'family, infamous for their bizarre and sometimes cruel '
               'experiments.As a young adult, his shy and anxious disposition '
               'made it difficult for him to form meaningful relationships '
               'with those around him.Nevertheless, Nervous harbored a fervent '
               'desire for knowledge and understanding, an aspiration that '
               'fueled his pursuit of new information and experiences.Despite '
               'the challenges he faced, Nervous demonstrated an exceptional '
               'aptitude in the field of science, a passion he no doubt '
               'inherited from his father.Intriguing and enigmatic, Nervous '
               "Subject's complex persona and unique background made him a "
               'captivating character that left a lasting impression on anyone '
               'who crossed his path.J Huntington III, a suave and athletic '
               'young adult, thrived amidst the pulsating energy of the '
               'dynamic metropolis of San Myshuno.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=538,
          lineno=515,
          tokens=240,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='As a prominent member of the illustrious Partihaus household, '
               'his magnetic charm and striking good looks never failed to '
               'draw a crowd wherever he went.Ambitious and driven, J devoted '
               'much of his time to diligently working towards his goal of '
               'becoming a renowned Professional Athlete, which often involved '
               'grueling sessions at the local gym.With an innate passion for '
               'sports and fitness, his well-toned physique was a testament to '
               "his dedication.J's lively demeanor, an amalgamation of his "
               "'bro' and 'dance machine' traits, made him the epicenter of "
               'every party, effortlessly dominating the dance floor with his '
               "infectious energy.As a fashion connoisseur, J's wardrobe "
               'boasted an array of trendy outfits and sleek hairstyles, '
               'ensuring he was always the cynosure of all eyes.Amidst the '
               'whirlwind of his active lifestyle, J still found time to '
               'indulge in romantic escapades, weaving a tangled web of '
               'dalliances throughout the city.Ultimately, J Huntington III '
               'was an adventurous and multifaceted individual, ceaselessly '
               'seeking the next thrilling chapter in his vibrant life.Kurt '
               'Lumberjackson, a strapping outdoorsman, was a man whose very '
               'essence seemed to be intertwined with the wilderness.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=539,
          lineno=525,
          tokens=224,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='With a muscular frame cultivated through years of laborious '
               'lumberjacking, he was easily recognizable in his signature '
               'plaid shirts, jeans, and work boots.A proud and prodigious '
               'beard adorned his chiseled jaw, its maintenance a topic he '
               'eagerly discussed with fellow beard enthusiasts.A master '
               "craftsman, Kurt's woodworking prowess was evident in the "
               'exquisite furniture he passionately created.A gentle giant, '
               'his amiable disposition and willingness to help others '
               'endeared him to his community.With a loyal canine ever at his '
               'side, he relished exploring the great outdoors, where he '
               'discovered inspiration for his culinary creations, marked by '
               'hearty flavors and locally-sourced ingredients.Though his '
               'rugged exterior belied it, a tender heart beat within, '
               'nurturing a love for rescuing and caring for animals in '
               'need.As the sun set on his days of toil, Kurt dreamt of a '
               'peaceful retirement, ensconced in a cozy woodland cabin, '
               "embraced by nature's splendor and the warmth of a crackling "
               'hearth.Olivia Stewart was an artistic spirit, blessed with a '
               'natural talent for painting that had already begun to make '
               'waves in the art world.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=540,
          lineno=535,
          tokens=238,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A social butterfly by nature, she had an uncanny ability to '
               'forge deep connections with those around her, her circle of '
               'friends ever-growing.A hopeless romantic at heart, she yearned '
               'to find her soulmate and build a loving family within the '
               'walls of her idyllic abode.Her palate was refined, delighting '
               'in the exploration of new recipes and hosting lavish dinner '
               "parties for her cherished companions.Olivia's unique, "
               'fashionable clothing was a testament to her artistic '
               'inclinations, setting her apart from the ordinary.A zealous '
               'learner, she constantly sought to perfect her skills, whether '
               'it was her painting, cooking, or even nurturing her beloved '
               "garden.Olivia's boundless charm and passion for life rendered "
               'her an unforgettable character in a world where her presence '
               'was cherished and celebrated.Kalista Kalid was a woman of '
               'undeniable charm and talent, her passion for the arts and keen '
               'eye for fashion setting her apart from the rest.Her magnetic '
               'charisma made her the life of any gathering, effortlessly '
               'drawing friends from all walks of life into her warm '
               'embrace.Creativity thrived within her, manifesting in the '
               'beautifully appointed home where she often spent her hours '
               'painting or strumming her guitar.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=541,
          lineno=546,
          tokens=224,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='With ambition burning in her heart, Kalista ceaselessly sought '
               'new opportunities to realize her dreams and '
               'aspirations.Wanderlust coursed through her veins, leading her '
               'on thrilling adventures and serendipitous encounters with '
               'intriguing individuals.A hopeless romantic, she yearned for a '
               'love as enchanting as the tales in her cherished '
               'novels.Despite her whirlwind of a life, Kalista always '
               'prioritized her family and friends, treasuring every moment '
               'shared with her loved ones.As a connoisseur of fine cuisine, '
               'she reveled in exploring new recipes and delighting her guests '
               "with her culinary prowess.Kalista Kalid's kind heart and "
               'adventurous spirit left an indelible mark on the hearts of all '
               'who had the fortune to cross her path.Li Loh was a vivacious '
               'young woman with an infectious smile that effortlessly '
               'attracted people into her circle.Her warm and sociable nature '
               'was complemented by a fierce devotion to her family, '
               'cherishing every moment spent with her parents and siblings.A '
               'creative spirit, Li Loh found solace in painting, writing, and '
               'singing, using these artistic outlets as a means of '
               'self-expression.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=542,
          lineno=557,
          tokens=228,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='She also possessed a flair for experimenting with new recipes, '
               'her culinary pursuits often a delightful adventure, despite an '
               'occasional need for refinement.A hopeless romantic, she '
               'yearned to find her soulmate, envisioning a life filled with '
               'love and happiness.Her wardrobe was a testament to her unique '
               'sense of style, always fashionable yet comfortable, reflecting '
               'the very essence of her personality.Curious to explore the '
               'world, Li Loh loved to visit new places and engage with their '
               'inhabitants, her eagerness to learn and adapt making her an '
               'extraordinary individual.Though her moments of stubbornness '
               'were undeniable, her loved ones knew that her intentions were '
               'always pure, making Li Loh a character to cherish and '
               'admire.With her striking red hair and rebellious nature, '
               'teenage Lilith Pleasant stood out even amid the unique '
               'individuals in her family.As the twin sister of Angela '
               'Pleasant, the two shared a physical resemblance that belied '
               'their contrasting personalities, often resulting in tension '
               'between them.Marching to the beat of her own drum, Lilith was '
               'known for her mischief and troublemaking, but beneath her '
               'rough exterior lay a hidden soft side that endeared her to '
               'those she deemed close.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=543,
          lineno=567,
          tokens=230,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Her disinterest in academics led to struggles with her grades, '
               'while her parents, Daniel and Mary-Sue, found it challenging '
               'to connect with her, further fueling her rebellious '
               'streak.When not testing the boundaries, Lilith could often be '
               'found playing video games, socializing with friends, or honing '
               'her guitar skills.Navigating her tumultuous love life proved '
               'as difficult for Lilith as maintaining a stable relationship, '
               'but her strong will and individuality ensured that her '
               'unconventional path would captivate all those who crossed '
               'it.Lazlo Curious, with his wild red hair and striking blue '
               'eyes, was an eccentric and brilliant individual who resided in '
               'the peculiar town of Strangetown.As a member of the enigmatic '
               'Curious family, Lazlo was known for his insatiable appetite '
               'for scientific knowledge and his unwavering dedication to '
               'uncovering the secrets of the universe.He shared this passion '
               'with his two brothers, Pascal and Vidcund, and together, they '
               'embarked on countless adventures and experiments that often '
               "landed them in the most bizarre situations.However, Lazlo's "
               'infectious optimism and love for discovery always prevailed, '
               'inspiring those around him.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=544,
          lineno=576,
          tokens=245,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His romantic entanglements were equally as complex, as he '
               'found himself in a passionate affair with the alluring Crystal '
               'Vu, who happened to be the ex-wife of his own brother, '
               "Vidcund.Yet, Lazlo's unique sense of style, which included a "
               'lab coat and goggles, only served to accentuate his ardent '
               'enthusiasm for the world of science and set him apart from '
               'others in his quaint, curious community.Vivian Lewis was a '
               'vivacious and warm-hearted woman, often the life and soul of '
               'any gathering she attended.With a keen eye for fashion, she '
               'relished in experimenting with eclectic styles and vibrant '
               'colors, her wardrobe a testament to her adventurous spirit.Her '
               'magnetic personality easily drew others to her, and she '
               'reveled in forging new connections and nurturing existing '
               'relationships with heartfelt sincerity.Driven by dreams of '
               'stardom, Vivian tenaciously pursued a career in the '
               'entertainment industry, determined to make her mark as a '
               'renowned actress or musician.But despite her lofty ambitions, '
               'she never neglected her loved ones, her loyalty and '
               "steadfastness evident in every interaction.Vivian's creativity "
               'knew no bounds, indulging in a diverse array of hobbies such '
               'as painting masterpieces and concocting culinary delights.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=545,
          lineno=586,
          tokens=225,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Her infectious sense of humor was undeniably one of her most '
               'endearing traits, her laughter a balm to those fortunate '
               "enough to witness it.A true animal devotee, Vivian's life was "
               'enriched by the presence of her beloved pets and any strays '
               'she encountered.Ultimately, Vivian Lewis was a dynamic and '
               'compelling character, her journey of self-improvement and '
               'pursuit of happiness inspiring all who crossed her path.Bilal '
               'Hassani was a captivating presence, exuding an aura of talent '
               'and style that seemed to turn heads wherever he went.His '
               'colorful hairstyles and bold clothing choices made it '
               'impossible for him not to stand out in any crowd, and his '
               'incredible singing abilities ensured he was always the center '
               "of attention.A naturally gifted performer, Bilal's rise to "
               'fame was meteoric, his friendly and outgoing nature allowing '
               'him to forge deep connections and build a strong support '
               'network.A passionate advocate for social issues, he made it '
               'his mission to participate in charity events and promote '
               'awareness for important causes.And though his eccentric style '
               "sometimes presented challenges, Bilal's resilience and "
               'determination saw him through every obstacle that crossed his '
               'path.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=546,
          lineno=596,
          tokens=242,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In quieter moments, he could be found experimenting with new '
               'recipes or exploring hidden talents in creative hobbies, and '
               'despite his whirlwind lifestyle, he never failed to make time '
               'for the friends and family who cherished him dearly.In a world '
               'too often filled with dull sameness, Bilal Hassani was a '
               'beacon of joy and excitement for all those fortunate enough to '
               'cross his path.Mitchell Kalani was the epitome of charm and '
               'charisma, with an effervescent personality that drew people to '
               'him like moths to a flame.He possessed an innate musical '
               'talent, often found strumming his guitar or serenading those '
               'around him with his mellifluous voice.His laid-back demeanor '
               'occasionally interfered with his career ambitions, but he '
               'never failed to make ends meet.With sun-kissed skin and a '
               'casual, beachy style, Mitchell exuded an allure that was '
               'impossible to resist.A hopeless romantic, he delighted in '
               'sweeping others off their feet with his enchanting ways.In his '
               'leisure time, Mitchell reveled in outdoor pursuits like '
               'fishing and hiking, embracing the beauty of nature with an '
               'almost reverential awe.Though easygoing in nature, he harbored '
               'a competitive streak that surfaced during friendly '
               'competitions and challenges.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=547,
          lineno=607,
          tokens=228,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Above all, Mitchell valued the ties that bound him to his '
               'family and friends, offering unwavering support and '
               'encouragement to those he held dear.His infectious laughter '
               'and warm personality made him a welcome addition to any social '
               'gathering, and his presence brought joy and happiness to all '
               'who crossed his path.Maggie Bennet was a vibrant soul, her '
               'creativity and passion for music and arts, making her an '
               'influential presence in her community.Her outgoing personality '
               'attracted others to her, like moths to a flame, and she '
               "cherished the connections she had with her loved ones.Maggie's "
               'unique sense of style, an amalgamation of bold colors and '
               'eclectic patterns, was a testament to her artistic '
               'nature.Ambitious and dedicated, she poured her heart and soul '
               'into her career as a painter, often burning the midnight oil '
               'to create her masterpieces.Her musical prowess extended beyond '
               'just appreciation, as her fingers danced gracefully along the '
               'strings of her guitar.Witty and sarcastic, her sense of humor '
               "never failed to bring laughter to her friends.Maggie's love "
               'for animals was evident in the adoration she showered upon '
               'Daisy, her rescue dog.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=548,
          lineno=618,
          tokens=233,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='With an unquenchable thirst for adventure, she was always '
               'eager to explore new places and embrace exciting challenges, '
               'from savoring exotic cuisines to acquiring novel '
               'skills.Despite her numerous achievements, Maggie Bennet '
               'remained a humble and grounded woman, grateful for the '
               'unwavering love and support from those around her.Kierra Tilo, '
               'a vivacious and spirited individual, was known for her '
               'delightful presence and eclectic sense of style that never '
               'failed to turn heads.Her boundless ambition propelled her to '
               'tackle a multitude of hobbies, from painting masterpieces to '
               'concocting culinary delights, and tending to her flourishing '
               "garden.A social butterfly, Kierra's extroverted nature drew "
               'people from all walks of life into her ever-expanding circle '
               'of friends.With a soft spot for animals, she devoted her time '
               'to caring for her cherished pets, forging a bond that was '
               'nothing short of heartwarming.Romance played a significant '
               'role in her adventurous life, as she sought a companion who '
               'could match her fervor and zeal for life.Her abode, a '
               'harmonious blend of contemporary and bohemian influences, '
               'perfectly encapsulated her multifaceted personality.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=549,
          lineno=628,
          tokens=243,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In a world brimming with ordinary, Kierra Tilo was a breath of '
               'fresh air, her infectious enthusiasm and daring spirit an '
               'indelible mark on everyone she encountered.Dana Adler was a '
               'creative soul with an unquenchable passion for the arts and a '
               'distinctive flair for fashion.Her natural talent for painting '
               'was evident as she spent countless hours perfecting her '
               'masterpieces, each stroke an extension of her vivid '
               'imagination.Outgoing and sociable, Dana relished attending '
               'soirees and befriending fellow artists, yet she never '
               'neglected her need for solitude to recharge and seek '
               'inspiration.A culinary virtuoso, she took pleasure in '
               'concocting innovative recipes to delight the taste buds of her '
               'cherished friends and family.Animals held a special place in '
               "Dana's heart, and she devoted much of her time to volunteering "
               'at the local animal shelter.Her eclectic and vibrant wardrobe '
               'mirrored her artistic inclinations, and her close-knit circle '
               'of friends continually nurtured her creative '
               "aspirations.Dana's ultimate dream was to establish her own art "
               'gallery, a sanctuary to display her own work as well as that '
               'of other gifted artists.It was her compassionate spirit and '
               'unwavering ambition that endeared her to all who crossed her '
               'path.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=550,
          lineno=641,
          tokens=244,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Matilda The Cook, a culinary virtuoso, devoted her existence '
               'to mastering the art of cooking, often found in her kitchen '
               'sanctuary, concocting unique recipes and refining her '
               'techniques.Her innate aptitude for gourmet cuisine catapulted '
               'her to fame as a distinguished chef, her amiable and sociable '
               'nature endearing her to those who had the pleasure of tasting '
               'her creations.As she ascended the culinary hierarchy, she '
               'dreamt of one day inaugurating her own gourmet '
               "restaurant.Matilda's eye for detail and inventiveness "
               "manifested in her chic yet pragmatic chef's attire.A strong "
               'family bond tethered her heart, frequently hosting dinner '
               'parties to unite loved ones through the shared experience of a '
               'delectable feast.The irresistible aroma of her latest '
               'masterpiece lingered throughout her home, transforming it into '
               'an alluring haven for friends and neighbors.In her leisure '
               'moments, Matilda ventured into uncharted territories, '
               'unearthing novel ingredients and techniques to infuse into her '
               'dishes, solidifying her status as a cherished and proficient '
               'character in the culinary world.Dudley Landgraab, a wealthy '
               'and well-connected individual, hails from the prominent '
               'Landgraab family known for their opulent lifestyle and '
               'grandiose soirÃ©es.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=551,
          lineno=651,
          tokens=235,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="As a socialite, Dudley's days are filled with rubbing "
               'shoulders with the crÃ¨me de la crÃ¨me of society while '
               'seeking new business ventures and investment opportunities to '
               'expand his empire.However, his reputation for snobbery '
               'precedes him, often overshadowing his accomplishments as he '
               'looks down upon those not sharing his social standing.His '
               'self-centered nature prioritizes his desires above all else, '
               "leaving little room for empathy.Dudley's appearance is nothing "
               'short of luxurious, draped in designer clothing and '
               'accessories that reflect his affluent status.A skilled '
               'networker, he employs his connections for personal gain but '
               'can be equally charming and charismatic when it suits '
               "him.Underneath this suave exterior, Dudley's relentless "
               'ambition drives him to be manipulative and ruthless in his '
               'pursuits, making him a complex and fascinating character that '
               'represents the upper echelon of society.Aliya Fuego, a fiery '
               'and passionate woman, never hesitated to express herself '
               'through her audacious fashion choices and vibrant red hair '
               'that symbolized her unwavering zest for life.A true social '
               'butterfly, Aliya could effortlessly charm her way into any '
               'gathering, leaving behind a trail of new friends and admirers.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=552,
          lineno=661,
          tokens=245,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Her innate affinity for the arts, especially dance, allowed '
               'her to sway and twirl with grace and determination that left '
               'onlookers in awe.Often found experimenting with bold and spicy '
               'flavors in the kitchen, she mirrored her own scorching '
               'spirit.A family-oriented soul, Aliya envisioned a bustling '
               'home filled with the laughter and joy of her future '
               'children.Fiercely career-driven, she never shied away from '
               'climbing the ranks in her profession, earning respect and '
               'admiration from her peers.Though her charisma attracted '
               'potential suitors, she remained discerning in her search for '
               'the perfect partner.Embodied by an unquenchable thirst for '
               'adventure, Aliya Fuego continuously sought new experiences and '
               'challenges, her captivating presence igniting the lives of '
               'those fortunate enough to cross her path.Pablo Martinez was '
               'the epitome of affability, his genuine warmth and gregarious '
               'nature drawing people into his orbit with an irresistible '
               'magnetism.A dapper individual, his wardrobe was a kaleidoscope '
               'of hues and patterns that reflected his vibrant personality.A '
               'connoisseur of culinary delights, Pablo relished exploring the '
               'diverse flavors of the local gastronomic scene, and his green '
               'thumb nurtured a flourishing garden that was the envy of his '
               'neighbors.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=553,
          lineno=672,
          tokens=236,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Possessing an indefatigable work ethic, Pablo continually '
               'sought opportunities to enhance his skills and advance his '
               'career.Nights found him twirling on the dance floor, his agile '
               'feet commanding the attention of all who beheld his grace.A '
               "perpetual seeker of true love, Pablo's heart yearned for that "
               'special connection that would set his soul aflame.His devotion '
               'to his family was unwavering, every moment spent with them '
               'treasured like the most exquisite gem.Creativity flowed '
               'through him like a river, manifesting in the evocative strokes '
               'of his paintbrush and the melodious strumming of his guitar.In '
               'essence, Pablo Martinez was a multi-faceted gem, his many '
               'facets casting a brilliant glow that illuminated the lives of '
               'all who knew him.In the bustling neighborhood of Oasis '
               "Springs, Zoe Patel's cheerful and energetic presence could "
               'light up any room she entered.A creative soul, she found her '
               'calling in the world of entertainment, gracing stages and '
               'enthralling audiences with her undeniable talent.Her passion '
               'for the culinary arts manifested in her aspiration to become a '
               'Master Mixologist, delighting in the creation of the most '
               'delectable and inventive concoctions.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=554,
          lineno=683,
          tokens=250,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="A true gourmand, Zoe's love for fine dining fueled her "
               'culinary pursuits, while her innate musicality made her an '
               'avid dancer and instrumentalist.As a member of the eclectic '
               'Roomies household, she shared her vibrant home with Mitchell '
               'Kalani, J Huntington III, and Gavin Richards.The bond she '
               'shared with her roommates was strong, their time together '
               'filled with laughter, group activities, and unforgettable '
               'shared experiences.With an unmatched enthusiasm for life and a '
               'personality as effervescent as champagne, Zoe Patel was a '
               'beloved figure in her community and an inspiration to all who '
               'crossed her path.Phoenix Money, an ambitious individual, '
               'dreams of amassing great fortune and becoming a renowned '
               'business tycoon.Possessing an unwavering focus on career '
               'advancement, Phoenix constantly seeks opportunities to '
               'prosper.Their confident and outgoing personality allows them '
               'to effortlessly forge friendships and connections, which prove '
               'instrumental in their pursuit of wealth.While Phoenix has a '
               'penchant for indulging in luxury, they are astute in '
               'investments and future savings.Their wardrobe, replete with '
               'elegant and extravagant clothing, ensures they stand out in '
               "any gathering.Phoenix's leisure time is spent attending social "
               'events and networking with other influential figures, always '
               'on the lookout for ways to augment their income.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=555,
          lineno=695,
          tokens=225,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Despite occasionally exhibiting self-centered tendencies, '
               'their generosity towards friends and family in need knows no '
               'bounds.In matters of the heart, Phoenix is drawn to partners '
               'who mirror their ambitious disposition and appreciation for '
               'the finer things in life.Undeterred by challenges, Phoenix '
               'Money remains resolute in their quest to be among the '
               'wealthiest and most powerful individuals in their world.Brent '
               'Hong was a man known for his ambition and pursuit of '
               'excellence in everything he touched.With a sharp wit and '
               'charming presence, he effortlessly captured the attention and '
               'admiration of those around him.Obsessed with technology, Brent '
               'dedicated his free time to refining his programming and gaming '
               'abilities, all while envisioning a future for himself in the '
               'tech industry.His passion for fitness kept him in the gym, '
               'sculpting his athletic frame, and his love for animals led him '
               'to adopt a loyal canine companion, Buddy.Amidst his bustling '
               'life, Brent always made time for his friends, hosting lively '
               'gatherings within the walls of his tastefully adorned abode.A '
               'hopeless romantic, he found himself longing for a true '
               'connection, someone to share in his love for gourmet cooking '
               'and appreciation for the arts.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=556,
          lineno=706,
          tokens=223,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="From gallery visits to concert attendance, Brent Hong's life "
               'was a captivating tapestry of dynamic interests and ceaseless '
               'self-improvement.Kailee Barclay was a woman whose vibrant '
               'personality and strong individuality made her stand out in any '
               'crowd.With a penchant for fashion, she often donned eclectic '
               "outfits that showcased her unique sense of style.Kailee's "
               'social prowess allowed her to easily befriend others, and she '
               'reveled in nights spent painting the town with laughter and '
               'good company.Yet, her love for her family ran deep, and she '
               'cherished the time spent with them during special occasions '
               'and holidays.Driven and hardworking, Kailee put her heart and '
               'soul into her career, leaving an indelible mark on the '
               'world.Her great sense of humor and animal-loving nature made '
               'her a joy to be around, filling her days with laughter and '
               "furry companions.Kailee's adventurous spirit led her to "
               'explore different neighborhoods and venues, seeking out new '
               'experiences and opportunities.A romantic at heart, she never '
               'ceased to search for her soulmate, dreaming of the day they '
               'could settle down and start a family together.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=557,
          lineno=717,
          tokens=246,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In essence, Kailee Barclay was an inspiration to all who '
               'crossed her path, bringing joy, excitement, and a zest for '
               'life that was truly infectious.Ollie Purdue, a charming and '
               'outgoing individual, had an uncanny ability to make friends '
               'wherever he went, his warm smile and affable demeanor acting '
               'as a magnet for companionship.Possessing an innate sense of '
               'style, he was often seen donning trendy outfits that showcased '
               'his creative spirit.Ambitious and hardworking, Ollie '
               'constantly strived to reach the pinnacle of his career, '
               'balancing his pursuits with a variety of hobbies, such as '
               'painting, cooking, and guitar playing.A hopeless romantic at '
               'heart, he dreamt of the day he would find his soulmate, and '
               'despite his busy schedule, he never neglected his health, '
               'regularly working out and maintaining a balanced diet.With a '
               'heart as big as his dreams, Ollie had a weakness for animals, '
               'providing a loving home for stray pets in need.In every aspect '
               'of life, Ollie Purdue was the epitome of a steadfast and loyal '
               'friend anyone would be fortunate to have.Camille Abbiza, a '
               'creative and ambitious soul, fervently pursues success in all '
               'aspects of her life.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=558,
          lineno=729,
          tokens=228,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Her passion for the arts manifests through her love of '
               'painting and playing the guitar in her leisure time.With a '
               "proclivity for socializing and making friends, Camille's "
               'outgoing personality is mirrored in her chic and trendy sense '
               'of style.Her diligent work ethic propels her to new heights in '
               'her career while her romantic nature seeks deep connections '
               'and meaningful relationships.As a skilled cook, Camille '
               'delights in hosting dinner parties for her loved ones, filling '
               'their evenings with warmth and laughter.Her wanderlust spirit '
               'drives her to explore the world, embracing new cultures and '
               "experiences with open arms.Camille Abbiza's unyielding "
               'optimism and relentless pursuit of success make her an adored '
               'and cherished figure within her community.Kai Kahue, a '
               'fun-loving individual, could often be found basking in the sun '
               'at the beach or engaging in various water activities, his '
               'affinity for the ocean apparent to all who knew him.Possessing '
               'a laid-back personality, he formed friendships with ease, his '
               'warm and approachable nature drawing people to him like a '
               'magnet.Proudly embracing his island heritage, Kai donned '
               'clothing and accessories that reflected his rich culture.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=559,
          lineno=740,
          tokens=238,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A passionate musician, the melodic strumming of his ukulele or '
               'the rhythm of his dancing to traditional tunes would '
               'frequently fill the air.As a food enthusiast, he relished the '
               'opportunity to cook and experiment with new recipes, '
               "particularly those involving seafood.Kai's connection to "
               'nature was evident in his gardening prowess and his dedication '
               'to environmental preservation.A family-oriented man, he '
               'cherished every moment spent with his loved ones.Ambitious in '
               'his career, Kai pursued his goals with determination while '
               'striking a healthy work-life balance.Curiosity drove him to '
               'explore and learn about the world around him, making Kai Kahue '
               "an endearing, well-rounded character who found joy in life's "
               'simple pleasures and the beauty of his island home.Nina '
               'Caliente, a vivacious young woman with a mane of fiery red '
               'hair, was as alluring as she was enigmatic.With an innate '
               'flair for fashion, she turned heads wherever she went, her '
               'sultry appearance drawing the attention of all who crossed her '
               'path.Residing in the sun-drenched Oasis Springs neighborhood '
               "with her sister, Dina, and their mother, Katrina, Nina's life "
               'was a whirlwind of flirtatious encounters and romantic trysts.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=560,
          lineno=751,
          tokens=223,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Her dream was to become a serial romantic, and her '
               'mischievous, unpredictable nature only added to her magnetic '
               "charm.Outgoing and always the life of the party, Nina's social "
               'calendar was a testament to her popularity within the '
               'community.Yet beneath her flirtatious exterior, she harbored a '
               'deep loyalty and protectiveness towards her family, adding a '
               'layer of complexity to her character that made her all the '
               'more intriguing.Ceres Beaker is a brilliant scientist who is '
               'constantly pushing the boundaries of knowledge in her '
               'field.She has a passion for chemistry and spends countless '
               'hours in her lab experimenting with various concoctions.Ceres '
               'is also known for her eccentric fashion sense, often sporting '
               "lab goggles and a white coat even when she's not working.Her "
               'green hair and piercing eyes make her stand out in any crowd, '
               'but she is often too absorbed in her research to notice.Her '
               'family, the Beakers, are equally as quirky and intelligent, '
               'making them an interesting bunch to be around.Ceres has a '
               'mischievous streak and enjoys playing pranks on her friends '
               'and family, often using her scientific knowledge to create '
               'hilarious outcomes.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=561,
          lineno=762,
          tokens=225,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Despite her sometimes serious demeanor, Ceres is a romantic at '
               'heart and dreams of finding the perfect partner who shares her '
               'love for science.She is a loyal friend to those who can keep '
               'up with her quick wit and intellect and can often be found '
               'deep in conversation about the latest scientific '
               "breakthroughs.Ceres Beaker's ambition and dedication to her "
               'work have earned her a reputation as one of the most respected '
               'scientists in her community, and many people look up to her as '
               'a role model.Kaiden Bryant, a creative and ambitious soul, '
               'thrives on expressing himself through various art forms.His '
               'cheerful demeanor and ability to connect with others make him '
               'a social magnet, drawing people into his magnetic presence.A '
               'passionate musician, Kaiden dreams of achieving fame, often '
               'losing himself in the melodies of the instruments he plays.His '
               'culinary endeavors showcase his love for experimenting with '
               'new recipes, as he aspires to master the art of cooking.This '
               'hopeless romantic is always in search of his soulmate, '
               "envisioning a loving family in his future.Kaiden's "
               'ever-evolving taste is evident in his fashionable outfits and '
               'hairstyles, reflecting his dynamic personality.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=562,
          lineno=773,
          tokens=242,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A firm believer in the harmony of body and mind, he enjoys '
               'staying active through dancing, sports, and gym '
               "sessions.Kaiden's affinity for nature manifests itself in his "
               'gardening ventures and his love for hiking and exploring the '
               'great outdoors.A beacon of positivity, Kaiden Bryant is a '
               'well-rounded and dynamic character who brings joy and '
               'excitement to the lives of those around him.Lewis Sancho is an '
               'outgoing and friendly individual who loves to socialize with '
               'his neighbors.He has a penchant for dressing in stylish and '
               'trendy clothing, which reflects his self-assured '
               'personality.Lewis is passionate about his career and works '
               'hard to achieve his goals, but he also knows how to have fun '
               'and let loose.He enjoys spending time at the local gym, where '
               'he can show off his athletic prowess and meet new people.Lewis '
               'has a natural talent for cooking and often invites friends '
               'over for dinner parties, where he can showcase his culinary '
               'skills.In addition to his career and hobbies, Lewis is a '
               'hopeless romantic and is constantly searching for his '
               'soulmate.He can often be found at the local park, flirting and '
               'trying to find his perfect match.Lewis is always eager to '
               'learn new things and is known for picking up new hobbies on a '
               'whim.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=563,
          lineno=786,
          tokens=225,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Despite his outgoing nature, Lewis is fiercely loyal to his '
               'friends and family and would do anything to protect '
               'them.Overall, Lewis Sancho is a charming and well-rounded '
               'individual, who brings energy and excitement to any social '
               'gathering.Vernon Morse was the epitome of ambition, his eyes '
               'always fixed on the glittering prize of success.Tirelessly '
               'dedicated, he often burned the midnight oil at the office, '
               'fueled by the relentless drive to scale the corporate ladder.A '
               "dashing figure, Vernon's keen sense of fashion ensured he was "
               'always impeccably dressed, whether attending a high-stakes '
               'work event or enjoying a night out with friends.Effortlessly '
               'charming, he floated among social circles with the ease of a '
               'butterfly, his outgoing nature and quick wit making him a '
               'popular presence.A romantic at heart, Vernon yearned to find '
               'that special someone with whom he could share his dreams and '
               'successes.Fitness was his solace, with the gym and '
               'neighborhood jogs providing a welcome escape from the '
               'pressures of his career.A tender-hearted animal lover, Vernon '
               'was known to take in stray dogs that crossed his path, '
               'providing them with loving homes.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=564,
          lineno=797,
          tokens=241,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Intelligence was a trait he valued highly, and he reveled in '
               'engaging in thought-provoking discussions with friends and '
               'colleagues.In essence, Vernon Morse was a multifaceted, '
               'driven, and charismatic individual who left a lasting '
               'impression on everyone he met.Andre DaSilva is a charming '
               'individual with a distinct sense of style, often seen sporting '
               'a fashionable outfit that matches his confident '
               'personality.With his dark hair and striking features, he '
               'immediately catches the eye of anyone who walks by.Andre is a '
               'skilled artist with a passion for painting, constantly working '
               'on perfecting his craft.As a romantic at heart, he often finds '
               'himself falling in love and engaging in romantic endeavors '
               'with others.Despite his busy social life, Andre is also a '
               'dedicated family man who enjoys spending quality time with his '
               'loved ones.He is known for his great sense of humor and his '
               'ability to make friends easily, making him a popular figure in '
               'his community.In his free time, Andre enjoys exploring the '
               'great outdoors and embracing the beauty of nature.His '
               'ambitious nature drives him to constantly strive for success '
               'in his career and personal life.With his intelligence and '
               'charisma, Andre DaSilva is a well-rounded individual who can '
               'achieve anything he sets his mind to.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=565,
          lineno=812,
          tokens=206,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Tycho Curious, a young man hailing from the enigmatic Curious '
               'family, was a true embodiment of their insatiable passion for '
               'science and the mysteries of the unknown.Residing in the '
               "peculiar neighborhood of Strangetown, Tycho's short black hair "
               'and glasses only accentuated his endearing, nerdy demeanor.The '
               'son of Glarn and Kitty Curious, he found solace in the company '
               'of his brothers, the older Lazlo and the younger Pascal.His '
               'fervor for learning propelled him to spend countless hours in '
               'his home laboratory, concocting experiments that challenged '
               "even the most formidable minds.Tycho's intellect was only "
               'matched by his dedication to his family, creating an '
               'unbreakable bond with his beloved brothers.When not delving '
               'into scientific pursuits, Tycho found joy in honing his logic '
               'and mechanical skills, often engaging in intense chess matches '
               'against worthy opponents.It was this unique blend of '
               'intelligence, curiosity, and familial devotion that made Tycho '
               'Curious an unforgettable and cherished character in his world.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=566,
          lineno=821,
          tokens=242,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Ned Whalen, a creative soul with an undeniable flair for art, '
               'often found himself immersed in an array of oil paints and '
               'canvas, experimenting with different styles to capture the '
               'essence of the world around him.His outgoing personality, a '
               'magnet for friendship, made him a regular at social events, '
               'where he effortlessly charmed his way into new circles.A '
               "family man at heart, Ned's dream was to be surrounded by a "
               'big, loving family, showering them with attention and care.As '
               'a romantic, he relished in planning special outings, whisking '
               'his partner away on memorable dates that left them both lost '
               "in each other's company.His innate leadership and unwavering "
               'work ethic propelled him forward in his career, while his '
               'quick-witted mind eagerly soaked up new skills and hobbies.In '
               'moments of respite, Ned found solace outdoors, tending to his '
               'flourishing garden or meandering through the park, breathing '
               'in the fresh air.A culinary enthusiast, he delighted in '
               'concocting new recipes, winning over the taste buds of friends '
               "and family alike.Ned's tender heart extended to the animal "
               'kingdom, his gentle touch and warm presence endearing him to '
               "the neighborhood's pets, who found a friend in him."),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=567,
          lineno=829,
          tokens=234,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In essence, Ned Whalen was a man who sought harmony in all '
               'aspects of life, striking the perfect balance between work, '
               'family, and personal passions.Ross Valentin, a charismatic and '
               'sociable individual, has an innate ability to befriend anyone '
               'he encounters.With a heart full of ardor for music, he often '
               'serenades guests at gatherings with his guitar or mellifluous '
               'voice.A hopeless romantic, Ross yearns for the day he meets '
               'his soulmate, but until then, he relishes in flirtatious '
               'encounters and exciting dates.His great sense of humor and '
               'compatibility with others make him a beloved figure within the '
               'community.Ambitious in his career, Ross diligently ascends the '
               'corporate ladder without sacrificing his cherished work-life '
               'balance.Outside of work, he maintains a healthy lifestyle '
               'through jogging and attending fitness classes.His culinary '
               'prowess shines during dinner parties with friends and family, '
               'where he loves experimenting with new recipes.Ross is grateful '
               'for his tight-knit group of friends who provide unwavering '
               'support and guidance, and he reciprocates their loyalty '
               'without hesitation.A creative soul, he finds solace in '
               'painting and writing as a means of self-expression.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=568,
          lineno=841,
          tokens=209,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Ross Valentin's well-rounded and amiable disposition brings "
               'joy and vibrancy to the lives he touches.Pollination Tech 9 '
               'SmithAmidst the peculiar and eccentric residents of '
               'Strangetown, the enigmatic Pollination Tech 9 Smith stood out '
               'with his extraordinary green skin, a testament to his '
               'extraterrestrial origin.Married to the lovely Jenny Smith and '
               'a doting father to Johnny and stepfather to Jill, he pursued '
               'an unparalleled career as a Pollination Technician, journeying '
               'to far-off realms to propagate plant life.Possessing an '
               'insatiable thirst for knowledge, his intellect was matched '
               'only by his penchant for cleanliness and ardent commitment to '
               'the environment.A master of Logic, Gardening, and Rocket '
               'Science, he forged a steadfast bond with his kindred spirit, '
               "the alien Xghrog M'Gra-Lx.Together with his family, "
               'Pollination Tech 9 Smith resided in the enigmatic abode known '
               'as H.Amore, nestled within the heart of the mysterious '
               'Strangetown neighborhood.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=569,
          lineno=852,
          tokens=213,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Dina Caliente, a sultry beauty with tanned skin, bright red '
               'hair, and alluring green eyes, resides in the sun-soaked town '
               'of Oasis Springs along with her sister Nina and mother '
               'Katrina.As a member of the renowned Caliente family, Dina '
               'carries a rich history and is well-known for her flirtatious '
               'and romantic nature, which often finds her entangled in a web '
               'of various love affairs.With a passion for food and cooking, '
               'she works diligently as an Assistant Dishwasher, honing her '
               'skills in the culinary arts.Her ultimate aspiration in life is '
               'to become a Serial Romantic, embracing the excitement and '
               "passion that comes with love and romance.Dina's talents extend "
               'to various areas such as charisma, fitness, and cooking, '
               'making her a versatile and captivating individual.Her bond '
               'with her sister Nina and mother Katrina is unbreakable, and '
               "they often find themselves enjoying each other's company in "
               'social gatherings.As a passionate romantic and a cherished '
               "member of the Caliente family, Dina's presence adds an "
               'intriguing and captivating essence to the story.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=570,
          lineno=861,
          tokens=236,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Jenny Smith, a vivacious young adult, resided in the '
               'sun-drenched oasis of Oasis Springs alongside her doting '
               'husband, Johnny Smith, and their enigmatic daughter, Lily '
               "Smith.A beacon of cheerfulness and charm, Jenny's outgoing "
               'personality drew friends into her orbit with ease.With an '
               'innate passion for fashion, she showcased a unique sense of '
               'style through her trendy and eye-catching ensembles.A devoted '
               'mother and family-oriented woman, Jenny strove to support Lily '
               'through her struggles with her alien heritage and provide the '
               'best life possible.At the core of her being, Jenny harbored a '
               'deep-seated romanticism, making her love story with Johnny '
               'feel like a fairy tale come to life.Her creative soul found '
               'solace in artistic expression, be it through painting or '
               'writing, as she fervently pursued her aspirations of becoming '
               'a renowned artist with her work displayed in prestigious '
               "galleries.Tirelessly working to hone her skills, Jenny's "
               'determination and ambition were matched only by her social '
               'prowess, effortlessly making new friends and filling her life '
               'with laughter and adventure.A well-rounded and cherished '
               "individual, Jenny Smith's life was a testament to the power of "
               'perseverance, love, and the pursuit of dreams.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=571,
          lineno=871,
          tokens=233,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Jaylen Mace's magnetic charm and relentless ambition made him "
               'a captivating figure in the bustling town.His creative spirit '
               'and diverse interests led him to forge connections with ease, '
               'becoming the life of every gathering with his infectious '
               'humor.A fitness aficionado, Jaylen spent his mornings jogging '
               'and sculpting his physique at the local gym, envisioning a '
               'future as a prosperous entrepreneur or corporate tycoon.With a '
               'family-focused heart, he longed to build a nurturing home for '
               'his future children.In his downtime, Jaylen reveled in '
               'culinary creations, hosting lavish dinner parties that '
               'showcased his innovative recipes.A true fashion devotee, he '
               'frequently updated his wardrobe with the latest trends, making '
               "heads turn wherever he went.Jaylen's insatiable thirst for "
               'adventure saw him traversing unknown lands, constantly seeking '
               'new experiences to enrich his life.In essence, Jaylen Mace '
               'embodied the quintessential outgoing, multifaceted individual '
               'with an unquenchable zest for life and a fervent quest for '
               'self-improvement.Nym was an imaginative and artistic soul, '
               'known for her penchant for vibrant brush strokes on canvas and '
               "her ability to capture life's most fleeting moments through "
               'her camera lens.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=572,
          lineno=882,
          tokens=246,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Her eccentric fashion choices were a delightful topic of '
               'conversation, as she often found herself draped in the most '
               'whimsically colorful garments.Laughter and wit were her '
               'currency, which she generously spent in social gatherings, yet '
               'she also treasured her quiet evenings, sharing her abode with '
               'Whiskers, her feline companion.As a dedicated freelancer in '
               'the realm of graphic design, Sue worked tirelessly to leave '
               'her mark on the world, her ambitions fueled by dreams of '
               'artistic fame.Her circle of friends was small but treasured, '
               'and while she sought love with the fervor of a hopeless '
               'romantic, it remained an elusive pursuit.A taste for exotic '
               'destinations and novel cuisines revealed a side of Sue that '
               'craved expansion and growth, painting a vivid picture of a '
               'woman who brought color and excitement to all those who '
               'crossed her path.Wilson Luchador, a charismatic figure with '
               'dreams of wrestling stardom, boasts a muscular build and a '
               'vibrant, eye-catching ensemble that mirrors his fervor for the '
               'sport.Blessed with an inherent charm, he effortlessly '
               'captivates those around him, forging friendships with '
               'remarkable ease.When not honing his fitness at the gym, Wilson '
               'reveals a tender side, often volunteering at the local animal '
               'shelter.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=573,
          lineno=892,
          tokens=229,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A steadfast and dependable ally, he revels in hosting lively '
               'soirees at his abode, where his mixology prowess shines as he '
               'concocts delectable and imaginative libations.With unwavering '
               'ambition fueling his wrestling career, Wilson ceaselessly '
               'endeavors to rise through the ranks, ultimately aspiring to '
               'etch his name among the legends of the industry.A true '
               'romantic at heart, he yearns for a partner who will stand by '
               'him and partake in his zest for life.In quiet moments, Wilson '
               'meticulously refines his wrestling techniques and signature '
               'moves, ever-ready to face any challenger who dares to step '
               'into the ring with him.Cloaked in the shadows of the night, '
               'the enigmatic Grim Reaper weaves through the fabric of mortal '
               "lives, appearing at the moment of a soul's departure.Shrouded "
               'in a black, hooded cloak, its face remains hidden, revealing '
               'only a pair of glowing, mysterious eyes that seem to pierce '
               "through the very essence of one's being.A scythe, the age-old "
               'symbol of death and harvest, is wielded with an eerie grace, '
               'poised and ready to sever the thread of life.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=574,
          lineno=901,
          tokens=238,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='With an air of solemnity, the Reaper consults a tablet, '
               'determining the fate of the deceased before claiming their '
               'soul.Though one would expect an entity such as this to be '
               'beyond the reach of human interaction, it is not entirely '
               'immune to the pleas and conversation of the living.In '
               'extraordinary circumstances, the Reaper may even find itself '
               'drawn into the mundane world of the living, though it remains '
               'apart, unable to fully participate in the trivialities of '
               'human existence.As a chilling and fascinating presence, the '
               'Grim Reaper serves as an ever-present reminder of the '
               'inescapable cycle of life and death, leaving an indelible mark '
               'on the lives it touches.General Buzz Grunt, a high-ranking '
               'military officer, strides through the peculiar neighborhood of '
               'Strangetown with a commanding presence, his strict and '
               'disciplined demeanor apparent in every step.Clad in his '
               "ever-present uniform, Buzz's life revolves around his "
               'dedication to his career and his three sons, Tank, Ripp, and '
               'Buck, each of whom share a unique bond with their '
               'father.Tragedy has struck the Grunt household with the loss of '
               "Buzz's wife, leaving him to singlehandedly navigate the "
               'turbulent waters of parenthood.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=575,
          lineno=910,
          tokens=245,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His suspicious nature often leads to conflicts with his '
               'enigmatic neighbors, primarily the elusive Smith family.Yet '
               'beneath his hardened exterior lies a hidden warmth, which he '
               'reserves for his family, revealing a softer side that few are '
               "privy to.General Buzz Grunt's home, adorned with "
               'military-themed decorations, serves as a constant reminder of '
               'the duty and responsibility that he holds dear, even if it '
               'sometimes overshadows his personal relationships.In a world '
               'filled with eccentric characters, Buzz stands out as a complex '
               'and intriguing figure, whose interactions never fail to leave '
               'a lasting impression.Olivia Kim-Lewis was a vibrant, young '
               'woman with an unbridled passion for fashion, her keen sense of '
               'style turning heads as she navigated the lively streets of '
               'bustling San Myshuno.Hailing from the renowned Lewis family, '
               'whose members had achieved success in various fields, Olivia '
               'was determined to make her own mark on the world as a '
               'world-famous painter.An outgoing social butterfly, she '
               'effortlessly expanded her circle of friends and acquaintances, '
               'all while honing her artistic skills with an innate flair for '
               'learning.Despite her lofty ambitions, she cherished the '
               'precious moments spent with her loving spouse and children, '
               'fostering the close-knit family bond they all held dear.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=576,
          lineno=920,
          tokens=235,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A true foodie at heart, Olivia reveled in the diverse culinary '
               'offerings of her beloved city, as she frequented local food '
               'stalls and restaurants, ever eager to sample their exotic '
               'flavors.When not indulging her palate or attending lively '
               'events such as the humor and hijinks festival, Olivia could be '
               "found admiring the city's art displays, constantly seeking "
               'inspiration for her own captivating masterpieces.Geoffrey '
               'Landgraab, a man of wealth and prestige, resided in the '
               'opulent neighborhood of Oasis Springs with his adoring wife, '
               'Nancy, and their bright son, Malcolm.Hailing from the renowned '
               'Landgraab lineage, Geoffrey was no stranger to ambition and '
               'hard work, holding a position as a Regional Manager in a '
               'reputable corporation.Although his career consumed much of his '
               'time, he never failed to nurture the bonds within his family, '
               'pouring his heart into their relationships.With a congenial '
               'nature, Geoffrey effortlessly attracted friends, but his '
               'competitive streak could not be ignored, occasionally clashing '
               "with those who threatened his family's standing or fortune.A "
               'fitness enthusiast, he boasted a well-toned physique, while '
               'his keen intellect and expertise in logic made him a '
               'formidable chess player and strategist.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=577,
          lineno=929,
          tokens=238,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Driven by his unwavering dedication, Geoffrey tirelessly '
               'pursued professional advancement, striving to secure the most '
               'luxurious life for his beloved family, all the while upholding '
               'the esteemed reputation of the Landgraab name.Livie Mounier is '
               'a stylish and outgoing young woman with a penchant for '
               'fashion, often seen wearing the latest trends that make her '
               'stand out in any crowd.Her friendly and approachable demeanor '
               'allows her to easily make new friends and engage in intriguing '
               "conversations wherever she goes.Livie's favorite pastimes "
               'include shopping, attending lavish parties, and exploring '
               'different neighborhoods to discover hidden gems.A '
               'career-driven individual, she excels in her chosen profession '
               'and is constantly seeking opportunities for growth and '
               'success.Despite her busy schedule, Livie always makes time for '
               'her loved ones, cherishing the bonds she forms with friends '
               'and family.Her charismatic personality and zest for life make '
               'her a popular figure within her community.A firm believer in '
               'staying active, Livie frequently participates in various '
               'fitness activities to maintain her health and well-being.Livie '
               'Mounier, in essence, is a well-rounded, ambitious, and social '
               'character who effortlessly balances her work and personal '
               'life, captivating those who cross her path.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=578,
          lineno=942,
          tokens=246,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Emiko Mori is a creative and ambitious young woman who aspires '
               'to make a name for herself in the world of fine art.Her '
               'cheerful disposition and quick wit make her a magnetic '
               'presence at social gatherings, endearing her to friends and '
               'acquaintances alike.As a skilled painter, Emiko devotes '
               'countless hours to honing her craft, producing masterpieces '
               'that have begun to capture the attention of esteemed '
               "collectors and art connoisseurs.When she's not wielding a "
               'paintbrush, she can often be found in the kitchen, indulging '
               'her passion for culinary exploration and delighting loved ones '
               "with innovative dishes from around the globe.Emiko's penchant "
               'for fashion is evident in her vibrant and eclectic wardrobe, '
               'which serves as a visual extension of her vivacious '
               'personality.A true social butterfly, she relishes the '
               'opportunity to mingle at neighborhood parties and events, all '
               'the while holding out hope that, one day, she will cross paths '
               "with the soulmate of her dreams.Emiko's tender heart extends "
               'to the animal kingdom, as evidenced by the unwavering devotion '
               'she shows to her beloved feline companion, Miso.In a world '
               'teeming with uncertainty, Emiko Mori remains a radiant beacon '
               'of joy, inspiration, and boundless potential.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=579,
          lineno=952,
          tokens=236,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='With her golden locks cascading down her shoulders like a '
               'silken waterfall, Kiernan effortlessly commanded the attention '
               'of any room she entered with her expressive eyes and '
               'captivating presence.She was the embodiment of creativity, her '
               'passion for the arts evident in the way she could bring any '
               'character to life, her talent honed from a young age.Naturally '
               'self-assured, outgoing, and ambitious, Kiernan was a force to '
               'be reckoned with, admired by many for her successful acting '
               'career and her impeccable sense of style.A true social '
               'butterfly, she thrived in the company of her peers, forming '
               'connections with those who shared her love for the '
               'entertainment industry.Her charm and charisma were palpable, '
               'making friends and leaving an indelible impression on all '
               'those who crossed her path.As she continued to rise through '
               'the ranks of her profession, from commercials to blockbuster '
               'films, Kiernan never ceased to explore the rich tapestry of '
               'cultural experiences the world had to offer.A true star in '
               'every sense, she was an inspiration to those who aspired to '
               'follow in her footsteps.Mimi Landgraab, a sophisticated and '
               'graceful woman, belonged to the wealthy and influential '
               'Landgraab lineage.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=580,
          lineno=962,
          tokens=214,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Dressed impeccably in chic and stylish outfits, her undeniable '
               'charisma attracted people and helped her navigate the '
               'complexities of high society.As a member of the renowned '
               'Landgraab family, Mimi indulged in a luxurious lifestyle, '
               'hosting extravagant parties in her opulent mansion.Driven by '
               'ambition, she pursued high-level careers to uphold her '
               "family's prestigious status and fortune.Despite her affluent "
               'life, Mimi occasionally yearned for simplicity, her daydreams '
               'wandering to less complicated existences.The complexity of '
               "Mimi's relationships mirrored her life, as she struck a "
               'delicate balance between her own desires for companionship and '
               "the need to safeguard her family's interests.A passionate "
               'lover of the arts, she cherished her creative pursuits in her '
               "leisure time.Ultimately, Mimi's greatest aspiration was to "
               'preserve the Landgraab name for posterity, ensuring that their '
               'legacy of success and affluence continued for generations to '
               'come.Raj Khemlani, a vibrant young adult, was a breath of '
               'fresh air in the small community with his eclectic wardrobe '
               'that spoke volumes about his personality.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=581,
          lineno=972,
          tokens=236,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His outgoing and friendly nature made it effortless for him to '
               'befriend anyone he encountered, and his passion for cooking '
               'led him to constantly whip up delectable dishes for friends '
               'and family.With strong family values at his core, Raj often '
               'dreamt of having a big family of his own someday.In his '
               'pursuit of love, he was the quintessential romantic, always '
               'keeping an eye out for his soulmate while enjoying the thrill '
               "of dating.Not one to take life too seriously, Raj's goofball "
               'antics and witty jokes often left everyone around him in '
               'stitches.While he had a strong work ethic and was dedicated to '
               "his career as a food critic, Raj's free time was spent basking "
               'in the sun at the local park or mingling at social events.His '
               'genuine spirit and approachable demeanor made him a cherished '
               'member of the community, always eager to lend a helping hand '
               "to his neighbors.Raj Khemlani's presence brought joy and "
               'excitement to the lives of everyone he encountered, making him '
               'an unforgettable character in the tapestry of their '
               'lives.Amber Stein, a creative and ambitious soul, had an '
               'innate ability to color the world around her with her artistic '
               'talents and penchant for fashion.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=582,
          lineno=982,
          tokens=220,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Her ever-evolving wardrobe mirrored the latest trends, making '
               'her a style icon in her quaint neighborhood.Her friendly '
               'nature and infectious laughter drew people toward her, '
               'allowing her to forge friendships quickly and effortlessly.A '
               "true culinary virtuoso, Amber's dinner parties were the talk "
               'of the town, as she delighted her guests with an array of '
               'exquisite dishes and innovative recipes.With dreams of '
               'achieving fame as a painter or fashion designer, she dedicated '
               'hours to perfecting her craft.Her home, a testament to her '
               'vivid imagination, was adorned with eclectic furnishings and '
               "decorations, each piece telling its own story.Amber's keen "
               'sense of humor and captivating storytelling abilities could '
               'keep her friends entertained for hours on end, and her '
               'adoration for her cherished pets knew no bounds.In her leisure '
               'time, Amber could be found basking in the sun at the local '
               'parks or engaging in various community events, her boundless '
               'creativity and zest for life illuminating every corner of her '
               'world.Melina Sophie was a vibrant and spirited young woman '
               'with a fervent passion for the arts that was evident from the '
               'moment you laid eyes on her.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=583,
          lineno=992,
          tokens=230,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Her innate talent for painting made her a force to be reckoned '
               'with as she spent countless hours perfecting her masterpieces, '
               'each one more breathtaking than the last.Melina was a social '
               'butterfly, her magnetic personality drawing people to her like '
               'moths to a flame, and her innate charm and wit made her a '
               'beloved figure in her close-knit community.A true fashionista, '
               'she turned heads wherever she went, her daring ensembles '
               'reflecting her vivacious and trailblazing spirit.As a '
               'self-proclaimed food connoisseur, Melina relished in the art '
               'of culinary creation, hosting decadent feasts for her friends '
               'and family to enjoy.A romantic soul, she dreamt of the day she '
               'would find her one true love and start a family of her '
               "own.Melina's ambition and unyielding determination fueled her "
               'quest for success in all aspects of her life, and her diverse '
               'interests in music, fitness, and gardening made her a unique '
               'and cherished presence in the lives of those who were '
               'fortunate enough to know her.Valeria Lopez, a stylish and '
               'creative soul, effortlessly expressed her individuality '
               'through her impeccable fashion sense and eye for design.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=584,
          lineno=1001,
          tokens=215,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Known to be the life of any gathering, her vivacious '
               'personality and warm, inviting smile drew people from far and '
               'wide into her enchanting orbit.A culinary enthusiast, '
               "Valeria's unique recipes and flair for experimentation made "
               'her a sought-after dinner guest among her ever-expanding '
               'circle of friends.Despite her bustling social calendar, she '
               'remained deeply devoted to her family, cherishing every moment '
               "spent with her loved ones.A true romantic, Valeria's heart "
               'yearned for her soulmate, never hesitating to follow the path '
               'of love.Ambitious by nature, she pursued career success with '
               'determination, while skillfully maintaining a healthy '
               'work-life balance.As a fitness aficionado, Valeria reveled in '
               'the adrenaline rush of sports and physical activities.Her '
               'empathetic nature and genuine concern for others made her a '
               'treasured friend and confidante, always ready to lend a '
               'helping hand.Valeria Lopez was, in every sense, a well-rounded '
               'individual; a testament to the rich tapestry of life with her '
               'diverse interests, unwavering bonds, and insatiable zest for '
               'living.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=585,
          lineno=1011,
          tokens=228,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Mia Hayes, a vivacious and affable woman, was known to '
               'captivate those around her with her innate charm and '
               'unwavering zest for life.With a keen eye for fashion, she '
               'would effortlessly assemble ensembles that spoke to her '
               'vibrant personality, making her stand out in any crowd.Driven '
               'by ambition, Mia tirelessly honed her skills and navigated the '
               'corporate world with determination, while her love for cooking '
               'often found her crafting exquisite dishes to the delight of '
               'her loved ones.Her affection for animals was unparalleled, her '
               'bond with her pet dog serving as a testament to her '
               "compassionate nature.A dreamer at heart, Mia's romantic "
               'notions propelled her search for a soulmate, envisioning a '
               'future filled with love and laughter.As a social butterfly, '
               'she reveled in the excitement of parties and gatherings, her '
               'infectious energy lighting up the dance floor.Her leadership '
               'qualities shone through in group projects and community '
               'events, a tribute to her self-assurance and inherent ability '
               "to inspire others.Ever the adventurer, Mia's wanderlust guided "
               'her to explore and discover the wonders of the world, with '
               'each new destination fueling her adventurous spirit.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=586,
          lineno=1019,
          tokens=220,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Above all, her unwavering loyalty and devotion to her friends '
               'and family solidified her place as a cornerstone in their '
               'lives, ever ready to lend a helping hand and spread love and '
               'support.Alice Spencer-Kim is a vibrant and gregarious woman '
               'who resides in the quaint town of Windenburg, nestled within '
               'her uniquely blended family.Alongside her devoted husband Eric '
               'Lewis, her spirited daughter Olivia, and her charming stepson '
               'Vivian, Alice thrives in her role as a loving matriarch.With a '
               'passion for gardening, she can frequently be found outdoors, '
               'nurturing her plants with the same tender care she bestows '
               'upon her family.As a dedicated fitness enthusiast, Alice leads '
               'by example, inspiring her loved ones to embrace a healthy '
               'lifestyle as she gracefully balances work, family, and '
               'leisure.Employed as a professional Gardener, she skillfully '
               'intertwines her love for nature with her career, creating a '
               'harmonious and fulfilling life.In addition to her exceptional '
               'gardening and fitness abilities, Alice is a splendid cook, '
               'often preparing sumptuous meals from the freshest ingredients '
               'cultivated from her own backyard.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=587,
          lineno=1028,
          tokens=242,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A natural-born leader, she exudes a strong sense of '
               'responsibility, as evident in her unwavering commitment to her '
               'marriage and motherhood.Socially, Alice flourishes in her '
               'community, effortlessly befriending new acquaintances and '
               'attending neighborhood events.During moments of solitude, she '
               'retreats to her sanctuary of literature and yoga, further '
               'solidifying her dedication to a well-rounded, balanced '
               'existence.Maya Riordan, a stylish and confident woman, has a '
               'penchant for expressing herself through her carefully curated '
               'fashion choices.Undeniably a social butterfly, she thrives in '
               'the company of others, easily forging connections and '
               'cultivating a vast network of friends and acquaintances.In her '
               'leisure time, Maya indulges in her passion for cooking, '
               'experimenting with new recipes to the delight of her taste '
               'buds.Her natural charisma and love for animals often find her '
               'surrounded by her beloved pets or taking them on leisurely '
               'strolls.Purple, a recurring theme in her wardrobe and home '
               "decor, captures the essence of Maya's vibrant "
               'personality.Driven by her career aspirations, she is '
               'determined to make a name for herself in the culinary or '
               'fashion industry.A hopeless romantic, she often finds herself '
               'daydreaming about finding her perfect partner.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=588,
          lineno=1040,
          tokens=222,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Maya's commitment to self-improvement and her optimistic, "
               'goal-oriented nature ensure that she leaves a lasting '
               'impression on all who have the pleasure of crossing her '
               'path.Marco Russo, a young adult with an infectious zest for '
               'life, exudes a passion for fitness and social interactions '
               'that draws people to him like moths to a flame.His dark brown '
               'hair, chiseled facial features, and athletic build make him a '
               'head-turner wherever he goes, be it the local gym or the '
               'neighborhood park.With an innate charm and knack for '
               'connecting with others, Marco easily forms deep bonds that he '
               'cherishes and nurtures.Aspiring to be a professional athlete, '
               'he devotes much of his time and energy to the sports industry, '
               'yet never fails to whip up delectable Italian meals for his '
               "friends, showcasing his culinary expertise.Marco's humble "
               'abode is a reflection of his minimalist taste and penchant for '
               'modern dÃ©cor, creating an inviting space for those who '
               'enter.A hopeless romantic, he often finds himself in intense, '
               'albeit short-lived, relationships that leave indelible marks '
               'on his heart.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=589,
          lineno=1049,
          tokens=234,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Forever striving to improve himself and reach his full '
               'potential, Marco can be found jogging through the streets or '
               'sinking baskets on the local court, his unwavering '
               'determination inspiring those around him.In essence, Marco '
               'Russo embodies a dynamic and well-rounded individual whose '
               'presence brings an undeniable excitement and energy to the '
               'community.Noah Meyer was a creative and ambitious soul, with '
               'aspirations to make a name for himself in the world of '
               'art.Possessing a natural talent for painting, one could often '
               'find Noah with a brush in hand, expertly crafting masterpieces '
               'that captivated those around him.A lover of the outdoors, he '
               'found solace and inspiration in lush gardens and parks, their '
               'beauty fueling his artistic muse.With a friendly and outgoing '
               'personality, Noah easily charmed others, often becoming the '
               'life of the party as his love for music and dancing proved '
               'contagious.Possessing a sharp wit and sense of humor, he had a '
               'knack for making friends quickly and keeping them '
               'entertained.A hopeless romantic at heart, Noah sought a '
               'soulmate who shared his passions for art and adventure.In his '
               'leisure time, he delighted in cooking gourmet meals and '
               'hosting dinner parties for his ever-growing circle of friends.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=590,
          lineno=1060,
          tokens=228,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Yet, despite his various interests, Noah remained resolute in '
               'his dream of becoming a renowned artist, diligently refining '
               'his skills and showcasing his work in galleries.With his '
               'unwavering determination and zest for life, Noah Meyer was a '
               'character whose impact would leave an indelible mark on those '
               'who encountered him.Angela Pleasant, a vivacious teenager with '
               'fiery red hair, lived in the quaint town of Pleasantview '
               'alongside her family.As the daughter of Mary-Sue and Daniel '
               "Pleasant, and the twin sister of Lilith, Angela's life was a "
               'fascinating mix of love, rivalry, and ambition.Her responsible '
               'nature and dedication to her studies earned her a spot on the '
               'high school honor roll, a fact she took pride in.Her close '
               'bond with her cousin, Cassandra Goth, and her friendly '
               'demeanor made her a beloved figure in her community.However, '
               'her romantic entanglement with Dustin Broke, a boy from a less '
               'fortunate background, drew the disapproval of her parents, '
               'adding a touch of rebellion to her otherwise pristine '
               "image.Angela's casual style, evident in her green sweater and "
               'jeans, matched her approachable personality perfectly.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=591,
          lineno=1070,
          tokens=208,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Even though she shared the same blood as her rebellious '
               'sister, Lilith, their contrasting dispositions often led to '
               "conflict.Yet, Angela's aspirations for a life filled with "
               'education, meaningful friendships, and love made her an '
               'endearing and relatable character in her own right.Feu, a '
               'dynamic and aspiring fashionista, possessed an innate flair '
               'for design and a magnetic charm that endeared her to everyone '
               'she encountered.Her thirst for adventure and exploration of '
               'diverse cultures was evident in her vibrant and eclectic '
               'wardrobe choices, which captivated the imagination of those '
               'around her.As an outgoing and spirited individual, she eagerly '
               'sought out new experiences that enriched her life with vivid '
               'memories and stories to share.In her leisure time, Aliya could '
               'be found meticulously honing her painting skills, '
               'experimenting with various artistic mediums, and indulging in '
               'photography to seize the beauty and wonder of her '
               'surroundings.Despite her myriad of talents, humility and '
               'compassion remained hallmarks of her character, with a '
               'readiness to offer a helping hand or a soothing embrace to '
               'those who needed it.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=592,
          lineno=1079,
          tokens=244,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="An ardent animal lover, Aliya's heart melted at the sight of "
               'any stray, often leading her to open her home, an abode '
               'teeming with artistic and lively dÃ©cor, to these furry '
               "companions.A natural-born leader, Aliya's ultimate aspiration "
               'was to establish a thriving fashion empire that would leave an '
               'indelible mark on the world, all the while inspiring others to '
               'pursue their dreams with unwavering determination.June Kay was '
               'a creative and friendly soul who thrived on self-expression '
               'through painting and various artistic endeavors.Her natural '
               'ability to forge lasting friendships and maintain strong '
               'relationships was only enhanced by her delightful sense of '
               'humor, which could effortlessly lighten the mood and make '
               'others feel comfortable in her company.June, a true nature '
               'aficionado, relished her moments spent outdoors, whether she '
               'was meticulously tending to her flourishing garden or '
               'exploring the breathtaking landscapes that adorned her '
               'world.As a career-driven individual, she gravitated towards '
               'artistic and nurturing professionsâ\x80\x94such as art, '
               'teaching, or gardeningâ\x80\x94where her passions could truly '
               "shine.June's culinary expertise was nothing short of "
               'extraordinary, making her dinner parties the talk of the town '
               'as guests eagerly anticipated the delicious fare she would '
               'serve.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=593,
          lineno=1088,
          tokens=231,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Family played an integral role in her life, with June '
               'consistently putting the needs of her loved ones above all '
               'else.Her affinity for animals extended not only to her '
               'cherished pets but also to the stray creatures she encountered '
               "along her journeys.June's fashion choices often embodied a "
               'bohemian flair, mirroring her free-spirited and imaginative '
               "nature.All in all, June Kay's warm and approachable demeanor "
               'made her a well-loved figure in her community, her life story '
               'captivating the hearts of those fortunate enough to know '
               'her.Leonardo Martinez, a creative and artistic soul, could '
               'often be found immersed in his paintings or skillfully playing '
               'a musical instrument.With a strong sense of family, he '
               'cherished moments spent with his loved ones, be it a large '
               'family dinner or simply relaxing at home.Known for his '
               'culinary prowess, Leonardo loved experimenting with new '
               'recipes, consistently impressing guests with his delectable '
               'creations.A true animal lover, he had a soft spot for furry '
               'companions, and never hesitated to provide a warm home for '
               'strays in need.As a true romantic, he constantly sought ways '
               'to surprise his significant other, keeping their love alive '
               'and thriving.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=594,
          lineno=1099,
          tokens=225,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His great sense of humor and knack for storytelling made him '
               'the life of any gathering, effortlessly drawing others into '
               'his circle of friends.Fitness was a priority for Leonardo, who '
               'maintained his health through regular jogs and gym sessions.A '
               'firm believer in lifelong learning, he eagerly pursued new '
               'skills, attending local library courses and seminars with '
               "enthusiasm.In his professional life, Leonardo's ambition drove "
               'him to work diligently, steadily ascending the ranks of his '
               'chosen career.Leonardo Martinez, an engaging and multifaceted '
               'individual, brought joy and excitement to all who crossed his '
               'path.Rodrigo De Pablo was a charismatic and outgoing man who '
               'thrived in the bustling town of Willow Creek.With a passion '
               'for the arts, he dedicated his free time to painting and '
               'playing the guitar, much to the delight of his friends and '
               'neighbors.Always impeccably dressed, his fashion sense was the '
               'talk of the town, as he effortlessly stood out in any crowd.A '
               'devoted family man, Rodrigo never hesitated to put his loved '
               'ones first, ensuring their happiness and well-being.He took '
               'pride in his culinary skills, often whipping up elaborate '
               'meals that left everyone craving more.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=595,
          lineno=1111,
          tokens=239,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='With dreams of one day becoming a renowned painter, he '
               'tirelessly honed his craft, hoping to see his masterpieces '
               'displayed in prestigious galleries worldwide.A true romantic '
               "at heart, Rodrigo's flirtatious nature and tender gestures "
               'towards his partner made him the epitome of an ideal '
               'companion.Never one to shy away from social events, his '
               'presence was always felt and appreciated throughout the '
               'community.In essence, Rodrigo De Pablo was a captivating and '
               'gifted individual who effortlessly enriched the lives of all '
               'those fortunate enough to know him.Eric Lewis, a charming '
               'young adult, made his home amid the lively and colorful Spice '
               'Market neighborhood of the bustling city of San Myshuno.As a '
               'prominent member of the notorious \\"Partyhaus\\" household, '
               'Eric was known for his love of partying and socializing.With a '
               'head of brown hair and a well-groomed beard, he could often be '
               'spotted sporting a stylish leather jacket and crisp white '
               'shirt.Driven by his aspiration to become a Friend of the '
               'World, Eric reveled in meeting new people and forging lasting '
               'friendships, his gregarious nature making it all the easier.A '
               "fervent music enthusiast, Eric's days were filled with "
               'dancing, attending concerts, and mastering musical '
               'instruments.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=596,
          lineno=1122,
          tokens=231,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='As an Amateur Entertainer, he diligently climbed the ranks of '
               'his chosen career, all the while sharing a special camaraderie '
               'with his roommates, Penny Pizzazz and Jade Rosa - fellow '
               'social butterflies with an insatiable appetite for life.In his '
               "leisure, Eric could be found exploring San Myshuno's vibrant "
               'festivals and events, showcasing his talents, and mingling '
               'with fellow revelers.All in all, Eric Lewis was the embodiment '
               'of a fun-loving, sociable spirit who thrived in the ceaseless '
               'rhythm of San Myshuno.Dennis Kim, a young adult with an '
               'unmistakable artistic flair, was a familiar face in the quaint '
               'town of Willow Creek.With his vibrant pink tank top, black '
               'shorts, and blue high-top sneakers, he exuded a colorful and '
               'expressive personality that matched his undeniable creative '
               'talent.Dennis often found solace in the great outdoors, where '
               'he could lose himself in the picturesque landscapes that '
               'surrounded him, his paintbrush a mere extension of his soul.It '
               'was at the bustling park that he discovered a sense of '
               'belonging, forging connections with fellow art enthusiasts and '
               'reveling in the camaraderie of like-minded spirits.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=597,
          lineno=1131,
          tokens=218,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='As an individual who effortlessly balanced the Creative, '
               'Outgoing, and Art Lover traits, Dennis was quickly making a '
               'name for himself in the world of painting, his skill and '
               'passion evident in each stroke on the canvas.Social events, '
               'particularly those that celebrated art and music, brought out '
               'the best in Dennis, as he found solace in sharing his '
               'masterpieces with others.His popularity knew no bounds, with '
               'friends and acquaintances in abundance, each drawn to his '
               'magnetic charm and undeniable talent.Nestled in his cozy, '
               'art-adorned abode, Dennis Kim dreamt of the day he would '
               'become a world-renowned artist, and with unwavering passion '
               'and dedication, it was only a matter of time before he turned '
               'that dream into reality.Mom Landgraab, a woman of wealth and '
               'influence, resides in the opulent neighborhood of Del Sol '
               'Valley, alongside her husband, Malcolm, and their son, '
               'Johnny.Distinguished by her high social standing, she relishes '
               'attending extravagant soirees and events, her prowess in the '
               'business world having honed her charisma and logic.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=598,
          lineno=1139,
          tokens=245,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A true fashionista, Mom Landgraab adorns herself in designer '
               'clothing and accessories, exuding an air of snobbery that may '
               'initially deter others.However, once past her frosty exterior, '
               'one discovers a friendly and sociable character.Her palatial '
               'mansion, an emblem of her affluence, boasts luxurious '
               'furnishings and an expansive swimming pool.As a member of the '
               'elite \\"Upper Crusts\\" club, she mingles with fellow '
               'affluent individuals, driven by her aspiration to attain '
               "staggering wealth and uphold her family's distinguished "
               'reputation.Daniel Pleasant, a charming and outgoing man, holds '
               'a prominent position within the Pleasant family, a lineage '
               'with a storied past.Married to the diligent Mary-Sue, Daniel '
               'is the father of two teenage daughters, Angela and Lilith, '
               'each with her own unique disposition.His magnetic personality '
               'draws people to him, especially when it comes to matters of '
               'the heart, though his romantic entanglements often threaten '
               'the stability of his seemingly idyllic family life.Balancing '
               'the demands of his career in the sports field with his innate '
               'athletic prowess and competitive spirit, Daniel faces the '
               'challenge of mending the delicate strands of his '
               'relationships, particularly with his rebellious daughter, '
               'Lilith.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=599,
          lineno=1149,
          tokens=230,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Traversing the complexities of love, career, and family, '
               "Daniel Pleasant's captivating story continues to unfold, "
               'leaving his legacy to echo through the annals of time.Bob The '
               'Butler, a highly skilled and experienced individual, is always '
               'impeccably dressed in a sharply tailored suit, exuding an air '
               'of dedication and finesse.With neatly combed hair and a stoic '
               'expression, he strikes the perfect balance between '
               'professionalism and approachability.Adept in cooking, '
               'cleaning, and repairing household items, Bob ensures the '
               'seamless functioning of any home.His excellent mixology skills '
               'make him an invaluable asset during parties and social '
               'gatherings.Beneath his serious exterior lies a great sense of '
               'humor, as he often engages in witty banter with those around '
               'him.In his leisure time, Bob can be found honing his piano '
               'skills or indulging in a strategic game of chess, adding to '
               'his already sophisticated persona.Known for being a great '
               'listener, he offers a supportive shoulder for others during '
               'difficult times.His unwavering loyalty and commitment to his '
               'job, along with his rare inclination to take time off or '
               'neglect his duties, make Bob an indispensable member of any '
               'household.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=600,
          lineno=1160,
          tokens=244,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His presence often brings a sense of security and order, and '
               'over the years, he has become a beloved figure, not only for '
               'his impeccable service but also for his endearing '
               'personality.Summer Holiday is a vivacious, extroverted '
               'individual with an innate warmth that immediately puts others '
               'at ease.Her passion for outdoor activities and forging new '
               'friendships is evident in her toned physique, which she '
               'maintains through her devotion to fitness and exercise.With a '
               'shock of vibrant red hair and an eye for the latest trends, '
               'Summer inevitably captures attention wherever she goes.As an '
               'aspiring bodybuilder, she dedicates countless hours to honing '
               "her strength and endurance, whether it's in the gym or "
               'pounding the pavement of her quaint neighborhood.Yet, she '
               'always makes time for leisure, enjoying sun-soaked afternoons '
               'in the park, taking refreshing dips in the pool, or engaging '
               'in friendly sporting competitions.Effortlessly charismatic, '
               'Summer possesses a natural ability to connect with others, her '
               'social calendar brimming with invitations to spend time with '
               'her beloved roommates or partake in lively community '
               'events.Despite her ambitious career aspirations and myriad '
               'hobbies, Summer never neglects her romantic pursuits, charming '
               'her way into the hearts of more than a few admirers.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=601,
          lineno=1170,
          tokens=234,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In essence, Summer Holiday is a radiant, spirited individual '
               'who infuses every encounter with an infectious zest for '
               'life.Atom Beaker, a prodigious scientist with an eccentric '
               'spirit, resides in the sun-drenched town of Oasis Springs, '
               'where he is revered for his inventive intellect.Born to the '
               'infamous Loki and Circe Beaker, noted for their unscrupulous '
               'experiments, Atom not only inherited their passion for the '
               'sciences, but also their striking red hair.As a scion of the '
               'Beaker clan, he shares a familial connection with the '
               'enigmatic and accomplished Specter household.Ambition courses '
               'through his veins, driving him to scale the heights of the '
               'scientific career ladder.A fervent devotee of robotics, Atom '
               'can often be found in his home laboratory, meticulously '
               'assembling intricate inventions.Though his social graces may '
               'occasionally falter, he is buoyed by a close circle of loyal '
               'friends who share in his thirst for knowledge.As darkness '
               "descends, Atom's gaze turns skyward, his high-powered "
               'telescope unveiling the mysteries of the cosmos.His ultimate '
               'aspiration: to achieve a monumental scientific breakthrough, '
               'indelibly etching his name into the annals of history.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=602,
          lineno=1183,
          tokens=218,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Callia Maebey is a creative and ambitious individual, whose '
               'passion lies in expressing herself through the art of '
               'painting.With a keen eye for detail, she loses herself in a '
               'world of colors and shapes, while meticulously perfecting her '
               'artwork.A social butterfly, Callia adores meeting new people '
               'and forging connections, broadening her network within the art '
               'world.Her vivacious personality and contagious sense of humor '
               'make her a cherished figure in her community.When not immersed '
               'in her artistic pursuits, Callia dreams of finding her '
               'soulmate and starting a family.Her love for art overflows into '
               'her home, filling it with her original creations and an '
               'eclectic mix of dÃ©cor.Diligent and driven, Callia is '
               'constantly looking for ways to refine her skills and advance '
               'in her career as an artist.Her strong sense of identity and '
               'devotion to her craft are evident in her bold, colorful '
               'wardrobe choices, reflecting her artistic nature.Callia '
               "Maebey's unwavering determination and unique flair serve as an "
               'inspiration to others, proving that with hard work and '
               'dedication, anyone can achieve their dreams.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=603,
          lineno=1192,
          tokens=226,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A truly vibrant, talented, and beloved individual, Callia '
               'Maebey brings beauty and joy to the lives of those fortunate '
               'enough to know her.Pak Ree was a vivacious and intrepid soul, '
               'constantly yearning to uncover new horizons and immerse '
               'himself in novel experiences.A true connoisseur of music, he '
               'relished in the harmonious melodies produced by his deft '
               'fingers on various instruments, and reveled in the communal '
               "energy of live concerts.Pak Ree's passion for culinary arts "
               'was well-known among his circle, as he delighted in crafting '
               'sumptuous meals infused with exotic flavors that tantalized '
               'the taste buds of his loved ones.A gregarious individual, he '
               'frequented social gatherings and formed effortless connections '
               'with those around him.Possessing an unwavering drive to excel '
               'professionally, Pak Ree was adept at striking the perfect '
               'balance between his ambitions and personal life.Forever '
               'seeking his destined companion, he longed to find someone who '
               "shared his fervor for life's adventures.An advocate of "
               'physical fitness, Pak Ree could often be found engaging in '
               'various athletic activities or honing his physique at the '
               'local gym.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=604,
          lineno=1202,
          tokens=242,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='The bonds he shared with his family were unbreakable, their '
               'presence during holidays and milestones always cherished.A '
               "true steward of the environment, Pak Ree's commitment to "
               'eco-friendly pursuits had earned him the admiration of his '
               'community.In essence, Pak Ree was a multifaceted individual '
               'whose infectious enthusiasm for life endeared him to all who '
               'crossed his path.Leanna Epps, a vivacious and sociable young '
               'woman, effortlessly draws others into her magnetic aura as she '
               'navigates the world with an insatiable appetite for '
               'connection.A devotee of fashion, Leanna masterfully curates '
               'her wardrobe to create a dazzling tapestry that mirrors her '
               'distinctive spirit.Family plays a central role in her life, as '
               'she cherishes every moment spent with loved ones, weaving a '
               'rich tapestry of memories to last a lifetime.Ambition fuels '
               'her fire, driving her to tirelessly pursue her career and hone '
               'her talents, while her creative flair finds an outlet in '
               'artistic pursuits such as painting and photography.A paragon '
               'of health, Leanna maintains her fitness with unwavering '
               'dedication, whether hitting the gym or engaging in athletic '
               'endeavors.As a culinary adventurer, she delights in crafting '
               'delectable dishes and sharing her gastronomic discoveries with '
               'others.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=605,
          lineno=1213,
          tokens=246,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Leanna's leisure hours are spent lost in the pages of a "
               'captivating novel or immersed in her favorite television '
               'dramas.Yet, through all her diverse interests and pursuits, '
               'Leanna remains steadfast in her ultimate goal: a life of '
               'fulfillment and balance, encircled by the warmth and support '
               'of those she holds dear.DÃ©sirÃ©e St. FeuFeu, a dazzling '
               'fashionista with an eye for all things opulent and chic, '
               'aspired to make her mark as a renowned fashion designer, '
               "conjuring up enchanting ensembles for the world's elite.With "
               'her fiery disposition and fervor for life, she found herself '
               'drawn to the vibrant hue of red, which she deemed a fitting '
               'emblem of her persona.A hopeless romantic, DÃ©sirÃ©e yearned '
               'to discover a soulmate who would stand by her side, cherishing '
               'their shared dreams and ambitions.She reveled in shopping at '
               'high-end boutiques, gracing exclusive parties, and perfecting '
               'her painting craft as a means to express her boundless '
               "creativity.Possessing a penchant for theatrics, DÃ©sirÃ©e's "
               'magnetic presence and flair for storytelling never failed to '
               'capture the attention of those around her.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=606,
          lineno=1222,
          tokens=221,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Despite her occasional stubbornness, her unwavering loyalty '
               'and fierce determination endeared her to her friends.In '
               'moments of leisure, she indulged in sumptuous spa treatments '
               "and delighted in the finest gastronomy.Feu's ultimate pursuit "
               'was to etch her name into the annals of fashion history, '
               'establishing herself as the epitome of elegance, beauty, and '
               'style.Laney Voom was an exuberant individual with a penchant '
               'for bold colors and patterns, which not only adorned her '
               'clothing but also the walls of her vibrant home.Outgoing and '
               'sociable, she thrived in meeting new people and expanding her '
               "circle of friends.Laney's artistic soul shone through her "
               'talents in painting and photography, where she transformed her '
               'emotions into captivating masterpieces.With an adventurous '
               'spirit, she ventured to exotic destinations, immersing herself '
               'in various cultures and drawing inspiration for her creative '
               'pursuits.A strong sense of community led her to volunteer and '
               'participate in local events, further establishing her '
               'connection to those around her.Laney was a romantic at heart, '
               'yearning to find a partner who would share her zeal for life '
               'and art.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=607,
          lineno=1234,
          tokens=230,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Despite her occasional absent-mindedness and disorganization, '
               'her friends and family cherished Laney for her quirky humor '
               'and unyielding optimism.In her career, she aspired to become a '
               'renowned artist, her creations coveted in galleries across the '
               'globe.Laney Voom, a free-spirited and passionate soul, brought '
               'an infectious joy to life, forever leaving a mark on those '
               'fortunate enough to know her.Tommi Turner, a creative and '
               'ambitious soul, often found themselves immersed in various art '
               'forms, expressing their emotions through colorful masterpieces '
               'on canvas.With a passion for painting and a talent for '
               "strumming heartfelt songs on the guitar, Tommi's charisma made "
               'them the life of every social gathering.With dreams of '
               'becoming a renowned artist or musician, Tommi worked '
               'tirelessly to attain recognition, never losing sight of their '
               'goals.At home, they were a caring and dedicated family member, '
               'always ready to lend a hand or share a comforting embrace.A '
               'hopeless romantic, Tommi yearned to find their soulmate and '
               'build a life filled with love and beauty.In their spare '
               'moments, they sought inspiration from nature, exploring the '
               'great outdoors and embarking on new creative projects.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=608,
          lineno=1245,
          tokens=241,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='With a keen eye for aesthetics, Tommi also dabbled in interior '
               'design, frequently transforming their living space to mirror '
               "their unique sense of style.In essence, Tommi Turner's "
               'well-rounded and dynamic personality exuded an infectious zest '
               'for life, captivating all who crossed their path.Zoe Flores, a '
               'vibrant young adult, resides in the picturesque suburban town '
               'of Willow Creek, sharing her cozy abode with her two eclectic '
               'roommates, Mitchell Kalani and Gavin Richards.As a member of '
               'the Garden Gnomes household, Zoe fills her home with warmth '
               'and laughter, her cheerful and outgoing personality a beacon '
               'of light to those around her.With a passion for music, an '
               'insatiable palate, and a penchant for mischief, Zoe is the '
               'life of every gathering, effortlessly blending melodious tunes '
               'and culinary delights with her infectious humor.As a budding '
               'chef in the competitive world of gastronomy, Zoe dreams of one '
               'day donning the title of Master Chef, tirelessly perfecting '
               'her cooking and gourmet techniques in pursuit of her '
               'aspiration.A ray of sunshine in the lives of those who cross '
               'her path, Zoe Flores is an enchanting character, weaving a '
               'delightful tapestry of joy and camaraderie in the tapestry of '
               'life.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=609,
          lineno=1256,
          tokens=241,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Marquise Palumbo was a stylish and sophisticated woman who '
               'relished in socializing with friends and neighbors.Her '
               'penchant for high-end fashion and always dressing in the '
               'latest trends made her the envy of many around town.A '
               'natural-born leader, Marquise often found herself organizing '
               'and hosting events, bringing people together and ensuring '
               'everyone had a great time.With her charismatic personality, '
               'she was able to forge friendships and navigate the complex '
               'world of interpersonal relationships with ease.Highly '
               'ambitious, Marquise worked tirelessly to achieve her career '
               'goals, rapidly ascending the corporate ladder.In her free '
               'time, she indulged in exploring new hobbies and skills, such '
               'as painting or playing the piano.Family and friends were '
               "Marquise's top priority, and she never hesitated to spend "
               'quality time with her loved ones and offer them support.Her '
               'luxurious home, adorned with exquisite artwork and elegant '
               'furnishings, was a testament to her success and refined '
               'taste.Though some perceived her as materialistic or '
               'self-centered, Marquise genuinely cared for the well-being of '
               'those around her and was always willing to lend a helping '
               'hand.Overall, Marquise Palumbo was a captivating and dynamic '
               'character who left a lasting impression on everyone she '
               'encountered.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=610,
          lineno=1268,
          tokens=229,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Chaz MacFreeling, a creative and ambitious soul, effortlessly '
               'captivated attention with his stylish wardrobe and unique '
               'sense of humor.His natural charm and social finesse drew '
               'people into his orbit, making him a popular presence wherever '
               'he ventured.His innate musical talent opened doors to various '
               'artistic careers, from singer to DJ, and even music producer.A '
               "lover of the outdoors, Chaz's green thumb transformed any "
               'space into an enchanting garden oasis.His unwavering work '
               'ethic and passion for the creative arts allowed him to excel '
               'in his chosen endeavors, while his open-minded nature made him '
               'adaptable to any situation.With an insatiable thirst for '
               "adventure and an outgoing personality, Chaz's life was a "
               'mesmerizing tapestry of unforgettable stories and '
               'experiences.As a hopeless romantic, he eagerly searched for '
               'his one true soulmate, his charming demeanor making him a '
               'sought-after partner.In essence, Chaz MacFreeling was the '
               'epitome of a dynamic, well-rounded individual, whose presence '
               'enriched the lives of all who crossed his path.Erroll Dowd was '
               'a creative and ambitious soul who loved to spend his time '
               'honing his skills in various fields.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=611,
          lineno=1279,
          tokens=240,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A natural-born artist, he was often seen with a paintbrush in '
               'hand and a canvas before him, expressing his emotions through '
               "vivid colors and unique shapes.Erroll's outgoing nature "
               'allowed him to easily befriend others at social gatherings, '
               'his sense of humor always providing witty jokes and amusing '
               'anecdotes to make everyone laugh.Music was another of his '
               'passions; the strum of a guitar or the melody of a piano often '
               'filled his free time, as he dreamt of one day becoming a '
               'renowned musician.A lover of nature, Erroll cherished time '
               'spent outdoors, whether it was tending to his garden, fishing '
               'by a serene lake, or simply wandering through a lush park.His '
               'romantic heart yearned for that special someone to share '
               "life's moments with, and when he did find love, he was a "
               "devoted and caring partner.Erroll's hardworking nature drove "
               'him to excel in his career and provide for his family, setting '
               'a remarkable example for those who looked up to him.A true '
               'food connoisseur, he reveled in experimenting with new recipes '
               'and exploring diverse cuisines.In essence, Erroll Dowd was a '
               'multifaceted, talented individual who brought joy and '
               'inspiration to everyone he encountered.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=612,
          lineno=1289,
          tokens=244,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='With a magnetic charm that could light up any room, Jayden '
               'Armstrong was the epitome of charisma.Whether he was in a '
               'bustling social gathering or a quiet corner at the local cafe, '
               'his laughter was contagious, and his stories held his audience '
               'captive.His dashing good looks, coupled with an ambitious '
               'drive to succeed, made him a force to be reckoned with in his '
               "professional life.When he wasn't busy scaling the corporate "
               'ladder, Jayden could often be found at the gym, sculpting his '
               'toned physique with unwavering dedication.Family always held a '
               'special place in his heart, and he cherished the moments spent '
               'in the company of his loved ones.Dressed to impress in the '
               "latest fashionable attire, Jayden's keen interest in style was "
               'evident to all who crossed his path.Though he reveled in the '
               'animated atmosphere of weekend parties, he also found solace '
               "in the quietude of a good book or movie.Jayden's secret "
               'yearning for true love hummed beneath the surface, fueling his '
               'search for a soulmate with whom he could share his vibrant '
               'life.In essence, Jayden Armstrong was a well-rounded, likable, '
               'and ambitious individual who left a lasting impression on '
               'everyone he encountered.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=613,
          lineno=1300,
          tokens=245,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Ophelia Nigmos was a captivating presence in the eerie town of '
               'Forgotten Hollow, with her porcelain skin, raven hair, and '
               'striking red eyes that seemed to pierce the very souls of '
               'those who glanced her way.Possessing an innate artistic '
               'talent, Ophelia was often found with a brush in hand, her '
               'canvas a beautiful dance of colors reflecting her creative '
               'passions.Her intelligence and thirst for knowledge shone '
               'through as she immersed herself in the pages of countless '
               'books and engaged in deep conversations with those who dared '
               'approach her.She carried an otherworldly aura, a perfect fit '
               'for the supernatural atmosphere that enveloped Forgotten '
               'Hollow.A true loner at heart, Ophelia cherished her solitude, '
               "exploring the town's shadowy secrets and indulging in her "
               'diverse hobbies.With an uncanny connection to the supernatural '
               'realm, she interacted with spectral beings as though they were '
               'old friends, her presence drawing many towards her despite her '
               'reclusive nature.Beneath the mysterious veneer, however, lay a '
               'woman of profound kindness and generosity, always willing to '
               'extend a helping hand to those in need.Her familial bonds were '
               'her true anchor, especially the deep connection she shared '
               'with her enigmatic aunt, Olive Specter.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=614,
          lineno=1308,
          tokens=227,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Ophelia Nigmos, an intriguing and enigmatic figure, added an '
               'irresistible layer of mystique to the peculiar world that '
               'surrounded her.Long John ButtercupsLong John Buttercups, a '
               'unique and quirky character, has a penchant for swashbuckling '
               'and all things pirate-themed.Donning a signature eye patch and '
               'pirate hat, he is always the life of the party and captivates '
               'everyone with his riveting storytelling abilities.His passion '
               'for sailing is infectious, and he dreams of owning a ship to '
               "explore the vast open seas someday.Long John's contagious "
               'sense of humor never fails to bring laughter to those around '
               'him as he shares jokes and amusing tales of his numerous '
               'adventures.A skilled musician, he often entertains friends '
               'with his accordion playing and spirited renditions of sea '
               'shanties.As an expert fisherman, he revels in spending hours '
               "by the water's edge, competing to reel in the biggest catch of "
               'the day.Beneath his rugged exterior lies a heart of gold, and '
               "Long John's fierce loyalty to friends and family is "
               'unmatched.With unwavering honesty and integrity, he stands '
               'firm for his beliefs.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=615,
          lineno=1319,
          tokens=222,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Long John embodies the adventurous spirit, fueled by a strong '
               'desire to explore the world and uncover hidden treasures, '
               'making him a truly unforgettable character.Ripp Grunt was a '
               'teenage resident of the peculiar town of Strangetown, known '
               'for its military families and otherworldly happenings.His '
               'bright red hair, inherited from his father General Buzz Grunt '
               'and shared by his younger brother Buck, was a symbol of the '
               "family's strong military background.With a slender build, Ripp "
               'often sported a black sleeveless shirt adorned with a green '
               'alien graphic, dark pants, and sneakers.Driven by curiosity '
               "and a thirst for knowledge, Ripp's true passion lay in "
               "learning and intelligence, much to his father's dismay.As a "
               'rebellious soul, Ripp often found himself at odds with his '
               "father's expectations and military lifestyle, seeking solace "
               'in his close relationship with his older brother, Tank, and '
               "their shared love of sports and fitness.Ripp's affinity for "
               'the paranormal and extraterrestrial also led him to befriend '
               'the enigmatic Smith family, particularly Johnny Smith, with '
               'whom he shared a mutual fascination.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=616,
          lineno=1328,
          tokens=222,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Though a mediocre student with a tendency to skip school and '
               "find trouble, Ripp's story revolved around his struggle to "
               'forge his own identity and pursue his interests, despite the '
               'pressure from his family to adhere to tradition.Emily Parcel, '
               'a friendly and outgoing young woman, was often seen '
               'socializing with her neighbors, her infectious warmth drawing '
               'others to her.A true fashionista, she was always impeccably '
               'dressed in the latest trends, her appearance a testament to '
               'her meticulous attention to detail.Family-oriented at heart, '
               'Emily harbored dreams of building a large family and forging '
               'close bonds with her relatives.A lover of the outdoors, she '
               'enthusiastically engaged in gardening, fishing, and exploring '
               'the picturesque landscapes that surrounded her.Ambitious and '
               'driven, Emily pursued success in both her career and personal '
               'life, her creative side shining through her love for painting, '
               'writing, and various artistic hobbies.While her perfectionist '
               'nature was evident in all she did, she also displayed an '
               'impressive adaptability when faced with new situations and '
               "challenges.Emily's tender heart was evident in her love for "
               'animals, often adopting stray pets she encountered on her '
               'adventures.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=617,
          lineno=1338,
          tokens=241,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A gifted cook, she reveled in hosting lavish dinner parties '
               'for her friends and family, taking immense pleasure in '
               'showcasing her culinary prowess.With her warm personality and '
               'diverse interests, Emily Parcel was a well-rounded and '
               'cherished individual in her close-knit community.Alexander '
               'Goth, a young boy with a dark and mysterious demeanor, was '
               'born into the prestigious Goth family, known for their gothic '
               'aesthetics and enigmatic aura.Often clad in black attire, '
               "Alexander's appearance is a testament to his family's "
               'distinctive style.As an intellectually gifted child with a '
               'Whiz Kid aspiration, he is a quick learner, excelling in '
               'academics and demonstrating an insatiable thirst for '
               "knowledge.Alexander's personality is a complex blend of "
               'gloominess and bookishness, making him prone to sadness while '
               'also fostering a deep love for literature.He shares a strong '
               'bond with his parents, Mortimer and Bella, and is closely knit '
               'with his sister, Cassandra.The family resides in the grand '
               'Ophelia Villa in Willow Creek, a stately abode that perfectly '
               "encapsulates the Goth's enigmatic charm.Alexander's "
               'fascinating lineage and intriguing personality traits make him '
               'a truly unique and captivating character in a world filled '
               'with intriguing personas.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=618,
          lineno=1351,
          tokens=237,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Vidcund Curious, a prominent figure in the enigmatic town of '
               'StrangeTown, was widely known for his insatiable appetite for '
               'scientific knowledge and discovery.His pale complexion, raven '
               'hair, and sharp, angular facial features set him apart from '
               'the common crowd, while his distinctive attire - lab coat, '
               'goggles, and boots - further emphasized his passion for '
               "research.As a scientist by profession, Vidcund's expertise "
               'spanned logic, cooking, and cleaning, making him a remarkably '
               'well-rounded individual.His personality was characterized by '
               'neatness, sociability, and seriousness, traits that mirrored '
               'his unwavering commitment to his work and personal '
               'pursuits.Vidcund, alongside his brothers Pascal and Lazlo, '
               'resided in a peculiarly designed abode that showcased their '
               'shared scientific inclinations.Their strong familial bond was '
               "well known in the community, as was Vidcund's ongoing feud "
               'with his enigmatic neighbor, Pollination Technician 9 '
               'Smith.Adding to the layers of intrigue that surrounded Vidcund '
               'was his romantic entanglement with the married Circe Beaker, '
               'further fueling the rumors and mysteries that seemed to '
               "constantly envelop StrangeTown's most curious resident."),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=619,
          lineno=1360,
          tokens=241,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Kan Fetter, an aspiring artist, possessed a vibrant '
               'personality that drew people towards him like moths to a '
               'flame.His innate cheerfulness and gregarious nature served as '
               'a catalyst for forming friendships in his eclectic '
               'neighborhood.He sought inspiration for his masterpieces in '
               'nature, often wandering through lush parks, his eyes scanning '
               'every leaf and petal for that one spark of creativity.With a '
               'romantic heart and a wandering eye, Kan searched for his '
               'soulmate, yet his fear of commitment made the quest a '
               'challenging one.His attire mirrored his artistic spirit, '
               'donning bold colors and patterns that turned heads wherever he '
               'went.A family man at heart, he cherished hosting gatherings '
               'for his loved ones, creating a warm and welcoming ambiance, '
               "particularly during festive occasions.Kan's passion for food "
               'led him to explore the culinary world, delighting friends with '
               'his gastronomical creations.His toned physique and remarkable '
               'athleticism kept him grounded and focused on his artistic '
               'pursuits.With a soft spot for animals, he often provided a '
               'loving home to strays that crossed his path.Despite his many '
               'talents, Kan Fetter remained grounded and cherished the '
               'unwavering support of his friends and family as he reached for '
               'the stars in his artistic endeavors.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=620,
          lineno=1372,
          tokens=245,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Nancy Landgraab, a wealthy and ambitious woman, resides in the '
               'opulent neighborhood of Oasis Springs, alongside her husband '
               'Geoffrey and their teenage son, Malcolm.Born into the '
               'prestigious Landgraab family, Nancy is often perceived as '
               'snobbish and materialistic, with aspirations of accumulating '
               'immense wealth.Employed as a Regional Manager in the '
               'competitive world of business, her expertise in Charisma and '
               'Logic are as remarkable as her dedication to fostering social '
               'connections.Her stern facial features and sophisticated style '
               'are a testament to her refined taste, and though she may '
               'sometimes come across as judgmental and aloof, Nancy fiercely '
               "safeguards her family's reputation and legacy.To sum up, Nancy "
               'Landgraab is an influential and powerful figure, ceaselessly '
               'striving to elevate her social standing and solidify control '
               "over her family's fortune.Alex Moyer was the epitome of a "
               'social butterfly, her warm smile and contagious laughter drew '
               'people in like moths to a flame.Often spotted around town '
               'engaging in a myriad of activities and events, her presence '
               'was like a breath of fresh air in any gathering.With an innate '
               'flair for fashion, her outfits were a mesmerizing blend of '
               'creativity and style, earning her admiration from those who '
               'shared her passion.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=621,
          lineno=1382,
          tokens=224,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='A true workhorse, Alex was relentless in her pursuit of career '
               'advancement and personal growth.Her tender, nurturing nature '
               'found solace in tending to her verdant garden, each plant a '
               'testament to her loving care.A self-proclaimed food '
               'enthusiast, her culinary escapades took her on adventures to '
               'local restaurants, where she indulged in the art of '
               'gastronomy.A hopeless romantic, she dreamt of the day she '
               'would find her soulmate, sharing her wanderlust and love for '
               'discovering uncharted territories.Her unwavering loyalty and '
               'devotion to her loved ones only added to the kaleidoscope of '
               'qualities that made Alex Moyer an enchanting and unforgettable '
               'character.Cassidy Purdue was a vibrant and ambitious young '
               'woman living in the heart of a bustling metropolis.With a '
               'burning passion for the arts, she would often lose herself in '
               'the melodic strumming of her guitar or the delicate strokes of '
               'her paintbrush, creating soul-stirring masterpieces.An '
               'outgoing and friendly soul, she had the uncanny ability to '
               'breathe life into any gathering, her unique and bold sense of '
               'fashion a testament to her spirited nature.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=622,
          lineno=1392,
          tokens=231,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body="Driven by a relentless determination to succeed, Cassidy's "
               'dreams of achieving artistic renown were matched only by her '
               'devotion to her loved ones, frequently hosting warm and lively '
               'soirees in her cozy abode.A culinary aficionado, she reveled '
               'in delighting her cherished guests with her scrumptious '
               'creations.In her pursuit of a life brimming with passion, '
               "Cassidy's heart remained ever open to the allure of romance, "
               'eager to embrace the magic of love.With an unwavering zest for '
               "life, Cassidy Purdue's indomitable spirit left an indelible "
               'mark on the hearts of all who crossed her path.Sean Sullivan '
               'was a congenial and extroverted fellow who thrived on forging '
               'new connections and cultivating friendships.With a penchant '
               'for gardening, he would frequently immerse himself in '
               'nurturing his flora or wandering through verdant parks.Family '
               "played a pivotal role in Sean's life, and he relished in "
               'sharing memorable moments with his children.A diligent worker, '
               'he ceaselessly pursued career advancement and coveted that '
               'elusive promotion.As a food enthusiast, Sean reveled in '
               'experimenting with novel recipes, delighting in sharing his '
               'gastronomic masterpieces with his nearest and dearest.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=623,
          lineno=1403,
          tokens=227,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His infectious humor never failed to elicit laughter, and as a '
               'hopeless romantic, he reveled in surprising his beloved with '
               "grandiose gestures.An active individual, Sean's days were "
               'often occupied with gym sessions and sports engagements.His '
               'musical talents shone through his guitar playing, serenading '
               'friends and family with heartfelt melodies.In essence, Sean '
               'Sullivan was a multifaceted and cherished individual whose '
               'presence brought joy and exhilaration to those fortunate '
               'enough to know him.George Rivers was a charming and outgoing '
               'man, known for his magnetic personality that attracted friends '
               'and adventure in equal measure.With a passion for music that '
               'set his soul alight, he spent his free time perfecting his '
               'guitar skills or immersing himself in the electric atmosphere '
               'of live concerts.A devoted family man, George cherished his '
               'relationships with loved ones, always seeking opportunities to '
               'create lasting memories with them.His ambitious nature drove '
               'him to dream of entrepreneurial success, while his love for '
               'nature saw him frequently donning gardening gloves or hiking '
               'boots to explore the great outdoors.A maestro in the kitchen, '
               'George enjoyed nothing more than hosting dinner parties to '
               'delight friends and family with his culinary creations.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=624,
          lineno=1414,
          tokens=239,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His artistic soul found solace in painting, as he wielded his '
               'brush to capture the beauty of the world that surrounded him.A '
               'hopeless romantic at heart, George found himself entangled in '
               'the pursuit of love, often juggling multiple romantic '
               'interests at once.Despite his myriad hobbies and interests, he '
               'still managed to find time to maintain his impressive '
               'physique, an active testament to the well-rounded and '
               'fascinating life of George Rivers.Cordelia Thebe was an '
               'enchanting woman, adorned with long, wavy brown hair and often '
               'dressed in bohemian attire that mirrored her free-spirited '
               'soul.She possessed an innate artistic flair, frequently '
               'immersed in creating exquisite paintings within her snug '
               "studio.Cordelia's gregarious nature made her a sought-after "
               'presence at social events, and her love for nature inspired '
               'her to nurture her garden and embark on leisurely strolls '
               'through the park.Adept in the culinary arts, she delighted in '
               'hosting dinner parties for her loved ones.A true romantic, '
               'Cordelia yearned to discover her soulmate and embrace the '
               'warmth of genuine love.Despite her array of talents and '
               'passions, she retained a sense of humility and genuineness '
               'that endeared her to those around her.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=625,
          lineno=1425,
          tokens=239,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='In moments of solitude, Cordelia found solace in yoga and '
               'meditation, ultimately striving for inner harmony and a life '
               'of profound fulfillment.Johnson Ready is a charismatic and '
               'outgoing individual who loves to make new friends and '
               'socialize at various events.He is quite ambitious and works '
               'diligently to climb the career ladder in his chosen '
               'profession.With a keen eye for fashion, he always makes sure '
               'he looks his best, often changing his outfits to suit the '
               'occasion.As a hopeless romantic, he dreams of finding his '
               'soulmate and building a loving family.Johnson is also a '
               'fitness enthusiast and takes pleasure in maintaining an active '
               'lifestyle, often visiting the gym or going for a jog.He is a '
               'skilled chef and enjoys whipping up delicious meals to share '
               'with friends and family.Johnson is an animal lover, and his '
               'greatest joy comes from taking care of his furry friends.He '
               'has a knack for telling engaging stories, ensuring he is '
               'always the life of the party.Johnson is also a fan of the '
               'arts, often visiting museums and attending live performances '
               'to broaden his horizons.Lastly, Johnson Ready is a person who '
               'brings warmth and excitement to any gathering, and his '
               'presence is sure to make any experience even more enjoyable.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=626,
          lineno=1440,
          tokens=233,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Lacey Stiles, a young and ambitious woman, dreams of '
               'conquering the fashion world with her keen eye for detail and '
               'natural design talents.A social butterfly, Lacey thrives on '
               'forging connections in both her personal and professional '
               'life.With a soft spot for animals, she often finds herself '
               'adopting stray cats, and her hopeless romantic nature keeps '
               'her in constant pursuit of her soulmate, even if she '
               "occasionally confuses infatuation for true love.Lacey's "
               'perfectionism sometimes leads to stress, but she finds solace '
               'in yoga and meditation.Her home, a cozy yet stylish apartment, '
               'mirrors her artistic flair and passion for fashion.A loyal '
               'friend, she readily supports her loved ones, even at the '
               'expense of her own needs.In her free time, Lacey enjoys '
               'experimenting with new recipes, though her culinary skills are '
               'still blossoming.Ultimately, Lacey Stiles is a passionate and '
               'driven woman who is determined to achieve her dreams and make '
               'the most of her life.With a heavy heart and an even heavier '
               'pair of oversized shoes, Sunny the Tragic Clown shuffled '
               'through life, a melancholic figure in a world that seemed to '
               'reject the very notion of his existence.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=627,
          lineno=1451,
          tokens=166,
          depth=6,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='His white and blue makeup, smeared with tears, along with his '
               'signature red nose, only served to accentuate the sorrow that '
               'clung to him like a shroud.Though his ultimate aim was to '
               'bring joy and laughter, his clumsy efforts often fell flat, '
               'leaving those he encountered feeling downcast and uneasy.Sunny '
               'was burdened by the weight of the \\"Tragic Clown\'s Curse,\\" '
               'a unique affliction that ensured his perpetual sadness and '
               'failure at even the simplest of tasks.He sought solace in the '
               'company of others, but his tearful demeanor and tendency to '
               'sob uncontrollably only distanced him further from those he '
               'longed to entertain.Like a shadow, he drifted from place to '
               'place, an enigmatic figure who seemed immune to the finality '
               'of death, leaving a trail of mixed emotions in his wake.'),
 Fragment(document_cs='ee638e7fe3556fbc7c7160254bb9d77d97a1308a6c5edeb910ab50205b539f67',
          id=628,
          lineno=1,
          tokens=10,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables and usages: sim_descriptions\n'),
 Fragment(document_cs='faaf8b80acddf164eaeb71380bed42696c9907768dd5342c5ef129d577404a3e',
          id=629,
          lineno=1,
          tokens=242,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'name: Build\n'
               '\n'
               'on:\n'
               '  push:\n'
               '    branches:\n'
               '      - main\n'
               '\n'
               'jobs:\n'
               '  build:\n'
               '    runs-on: ubuntu-latest\n'
               '    container:\n'
               '      image: '
               'public.ecr.aws/u4r4k4j8/node-build-container:69ee6753d1b6759a0dc432fe8103234c0d32c4c7\n'
               '    env:\n'
               '      AWS_ACCESS_KEY_ID: ${{ secrets.ACCESS_KEY }}\n'
               '      AWS_SECRET_ACCESS_KEY: ${{ secrets.SECRET }}\n'
               '      AWS_REGION: us-east-1\n'
               '    steps:\n'
               '    - name: Checkout code\n'
               '      uses: actions/checkout@v3\n'
               '    - name: Build Python\n'
               '      run: |\n'
               '        python3 ci_compile.py\n'
               '    - name: Package and Deploy\n'
               '      working-directory: build\n'
               '      env:\n'
               '        VERSION_TAG: ${{ github.sha }}\n'
               '      run: |\n'
               '        zip -r sentient-sims-descriptions.ts4script '
               'sentient_sims\n'
               '        aws s3 cp sentient-sims-descriptions.ts4script '
               's3://sentient-sims-artifacts/sentient-sims-descriptions.ts4script '
               '--only-show-errors --metadata version=$VERSION_TAG\n'),
 Fragment(document_cs='faaf8b80acddf164eaeb71380bed42696c9907768dd5342c5ef129d577404a3e',
          id=630,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='')]