[Fragment(document_cs='08c68667cbc53f774bf816752ac57eeef754033c7f2f6b194244c68aa384f565',
          id=1,
          lineno=10,
          tokens=243,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='CustomSearchCondition',
          body='[SuppressMessage("ReSharper", "UnusedMember.Global")]\n'
               '    public class CustomSearchCondition : IMySearchCondition\n'
               '    {\n'
               '        private string searchText = "";\n'
               '        private readonly HashSet<MyCubeBlockDefinitionGroup> '
               'sortedBlocks = new HashSet<MyCubeBlockDefinitionGroup>();\n'
               '\n'
               '        public string SearchName\n'
               '        {\n'
               '            set => searchText = value;\n'
               '        }\n'
               '\n'
               '        public bool IsValid => searchText != null;\n'
               '\n'
               '        [MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public void Clean()\n'
               '        {\n'
               '            searchText = "";\n'
               '            CleanDefinitionGroups();\n'
               '        }\n'
               '\n'
               '        [MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public void CleanDefinitionGroups() => '
               'sortedBlocks.Clear();\n'
               '\n'
               '        [MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public HashSet<MyCubeBlockDefinitionGroup> '
               'GetSortedBlocks() => sortedBlocks;\n'
               '\n'
               '        [MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public bool MatchesCondition(MyDefinitionBase '
               'definition) => MatchesCondition(definition?.DisplayNameText);\n'
               '\n'
               '        [MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public void '
               'AddDefinitionGroup(MyCubeBlockDefinitionGroup definitionGroup) '
               '=> sortedBlocks.Add(definitionGroup);\n'
               '\n'
               '        [MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public bool MatchesCondition(string name)\n'
               '        {\n'
               '            if (name == null)\n'
               '                return false;\n'
               '\n'
               '            var ss = searchText;\n'
               '            var sl = ss.Length;\n'),
 Fragment(document_cs='08c68667cbc53f774bf816752ac57eeef754033c7f2f6b194244c68aa384f565',
          id=2,
          lineno=50,
          tokens=245,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='CustomSearchCondition',
          body='            if (sl == 0)\n'
               '                return false;\n'
               '\n'
               '            // Prepare the first character of the search '
               'string\n'
               '            var si = 0;\n'
               '            var sc = ss[0];\n'
               "            var su = sc >= '0' && sc <= '9' || sc >= 'A' && sc "
               "<= 'Z';\n"
               '\n'
               '            // Walk on each character of the name\n'
               '            // Index based algorithm for speed (it does not '
               'allocate)\n'
               '            var nl = name.Length;\n'
               '            for (var ii = 0; ii < nl; ii++)\n'
               '            {\n'
               '                // Mismatching character?\n'
               '                if (name[ii] != sc)\n'
               '                {\n'
               '                    // Digits and upper case characters allow '
               'skipping characters\n'
               '                    if (su)\n'
               '                        continue;\n'
               '                    \n'
               '                    // Anything else matched exactly\n'
               '                    break;\n'
               '                }\n'
               '\n'
               '                // Skip the matching character in the search '
               'string\n'
               '                si += 1;\n'
               '                if (si == sl)\n'
               '                    return true;\n'
               '\n'
               '                // Recall the next character from the search '
               'string\n'
               '                sc = ss[si];\n'
               "                su = sc >= '0' && sc <= '9' || sc >= 'A' && sc "
               "<= 'Z';\n"
               '            }\n'
               '\n'
               '            return false;\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='08c68667cbc53f774bf816752ac57eeef754033c7f2f6b194244c68aa384f565',
          id=3,
          lineno=23,
          tokens=24,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Clean',
          body='[MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public void Clean()\n'
               '        {\n'
               '            searchText = "";\n'
               '            CleanDefinitionGroups();\n'
               '        }'),
 Fragment(document_cs='08c68667cbc53f774bf816752ac57eeef754033c7f2f6b194244c68aa384f565',
          id=4,
          lineno=30,
          tokens=18,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CleanDefinitionGroups',
          body='[MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public void CleanDefinitionGroups() => '
               'sortedBlocks.Clear();'),
 Fragment(document_cs='08c68667cbc53f774bf816752ac57eeef754033c7f2f6b194244c68aa384f565',
          id=5,
          lineno=33,
          tokens=23,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='GetSortedBlocks',
          body='[MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public HashSet<MyCubeBlockDefinitionGroup> '
               'GetSortedBlocks() => sortedBlocks;'),
 Fragment(document_cs='08c68667cbc53f774bf816752ac57eeef754033c7f2f6b194244c68aa384f565',
          id=6,
          lineno=36,
          tokens=160,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='MatchesCondition',
          body='[MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public bool MatchesCondition(MyDefinitionBase '
               'definition) => '
               'MatchesCondition(definition?.DisplayNameText);[MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public bool MatchesCondition(string name)\n'
               '        {\n'
               '            if (name == null)\n'
               '                return false;\n'
               '\n'
               '            var ss = searchText;\n'
               '            var sl = ss.Length;\n'
               '            if (sl == 0)\n'
               '                return false;\n'
               '\n'
               '            // Prepare the first character of the search '
               'string\n'
               '            var si = 0;\n'
               '            var sc = ss[0];\n'
               "            var su = sc >= '0' && sc <= '9' || sc >= 'A' && sc "
               "<= 'Z';\n"
               '\n'
               '            // Walk on each character of the name\n'
               '            // Index based algorithm for speed (it does not '
               'allocate)\n'
               '            var nl = name.Length;\n'),
 Fragment(document_cs='08c68667cbc53f774bf816752ac57eeef754033c7f2f6b194244c68aa384f565',
          id=7,
          lineno=39,
          tokens=28,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='AddDefinitionGroup',
          body='[MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        public void '
               'AddDefinitionGroup(MyCubeBlockDefinitionGroup definitionGroup) '
               '=> sortedBlocks.Add(definitionGroup);'),
 Fragment(document_cs='08c68667cbc53f774bf816752ac57eeef754033c7f2f6b194244c68aa384f565',
          id=8,
          lineno=61,
          tokens=148,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='MatchesCondition',
          body='            for (var ii = 0; ii < nl; ii++)\n'
               '            {\n'
               '                // Mismatching character?\n'
               '                if (name[ii] != sc)\n'
               '                {\n'
               '                    // Digits and upper case characters allow '
               'skipping characters\n'
               '                    if (su)\n'
               '                        continue;\n'
               '                    \n'
               '                    // Anything else matched exactly\n'
               '                    break;\n'
               '                }\n'
               '\n'
               '                // Skip the matching character in the search '
               'string\n'
               '                si += 1;\n'
               '                if (si == sl)\n'
               '                    return true;\n'
               '\n'
               '                // Recall the next character from the search '
               'string\n'
               '                sc = ss[si];\n'
               "                su = sc >= '0' && sc <= '9' || sc >= 'A' && sc "
               "<= 'Z';\n"
               '            }\n'
               '\n'
               '            return false;\n'
               '        }'),
 Fragment(document_cs='08c68667cbc53f774bf816752ac57eeef754033c7f2f6b194244c68aa384f565',
          id=9,
          lineno=1,
          tokens=96,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: CustomSearchCondition\n'
               '  Methods: AddDefinitionGroup Clean CleanDefinitionGroups '
               'GetSortedBlocks MatchesCondition\n'
               '  Usages: Add AggressiveInlining CleanDefinitionGroups Clear '
               'CodeAnalysis Collections CompilerServices Definitions '
               'Diagnostics DisplayNameText Game Generic Gui HashSet '
               'IMySearchCondition IsValid Length MatchesCondition MethodImpl '
               'MethodImplOptions MyCubeBlockDefinitionGroup MyDefinitionBase '
               'Runtime Sandbox SearchName SuppressMessage System '
               'ToolbarManager VRage definition definitionGroup ii name nl sc '
               'searchText si sl sortedBlocks ss su value\n'),
 Fragment(document_cs='27136ae72fbe5b19df2148d24354798a7b030a78df952891c7b6ef0782bea9c0',
          id=10,
          lineno=1,
          tokens=137,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# Toolbar Manager\n'
               '\n'
               'Toolbar Manager for the Space Engineers game.\n'
               '\n'
               'For support please [join the SE Mods '
               'Discord](https://discord.gg/PYPFPGf3Ca).\n'
               '\n'
               'Please consider [supporting my work on '
               'Patreon](https://www.patreon.com/semods).\n'
               '\n'
               '## Features\n'
               '\n'
               'This plugin allows for saving and loading toolbars. For '
               'example you can \n'
               'quickly load a "standard" toolbar into any game, which can '
               'greatly speed\n'
               'up your builds by using toolbar slots you have already '
               'memorized.\n'
               '\n'
               'This plugin works for both offline and online multiplayer '
               'games without\n'
               'the need for any server side support. All your save files are '
               'local, \n'
               'nothing is stored on a server.\n'
               '\n'),
 Fragment(document_cs='27136ae72fbe5b19df2148d24354798a7b030a78df952891c7b6ef0782bea9c0',
          id=11,
          lineno=19,
          tokens=122,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='### Toolbars\n'
               '\n'
               'The **G menu** has two new buttons to manage saved toolbars:\n'
               '- Save\n'
               '- Load\n'
               '\n'
               '**Merge** is the same as **Load**, but does not clear slots '
               'not used by the toolbar loaded.\n'
               '\n'
               'Saved toolbars are stored as XML files under: '
               '`%AppData%\\Roaming\\SpaceEngineers\\ToolbarManager`\n'
               '\n'
               'There are subdirectories for each toolbar type. Toolbars '
               'within the same type are compatible,\n'
               'altough they may not have the same amount of slots available.\n'
               '\n'
               'It is possible to save the toolbar from a cockpit and load '
               'into a remote control, for example.\n'
               '\n'),
 Fragment(document_cs='27136ae72fbe5b19df2148d24354798a7b030a78df952891c7b6ef0782bea9c0',
          id=12,
          lineno=34,
          tokens=211,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='### Quick block selection\n'
               '\n'
               'Press the `BACKSLASH` or `PIPE` key (on English keyboard) to '
               'open the quick \n'
               'block search menu. It works the same way as the original menu, '
               'but the search \n'
               'rules are optimized to find blocks primarily by capital '
               'letters and digits:\n'
               '\n'
               '- `AB` **Armor Blocks**\n'
               '- `PB` **Programmable Block**\n'
               '- `SK` **Survival Kit**\n'
               '- `AT` **Atmospheric Thrusters**\n'
               '- `LHT` **Large Hydrogen Thrusters**\n'
               '- `211` **All 2x1x1 armor blocks**\n'
               '\n'
               'Adding the subsequent lower case letters after an upper case '
               'one allows \n'
               'for narrowing down in case of ambiguity:\n'
               '\n'
               '- `PH` **Parachute Hatch** and **Point Hand**\n'
               '- `PHat` **Parachute Hatch** only\n'
               '\n'
               'The order of characters must match exactly. Lower case '
               'characters and\n'
               'space are skipped after a matching upper chase character or '
               'digit. \n'
               '\n'
               'Separating multiple search patterns by space is not supported, '
               'currently.\n'
               '\n'),
 Fragment(document_cs='27136ae72fbe5b19df2148d24354798a7b030a78df952891c7b6ef0782bea9c0',
          id=13,
          lineno=58,
          tokens=87,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='### Planned features\n'
               '- Restricting the load/merge operations to certain toolbar '
               'pages\n'
               '- Multiplying the available toolbar pages using new hotkeys '
               'and saved toolbars\n'
               '- Moving and swapping toolbar items using mouse drag&drop\n'
               '- Moving toolbar items between toolbar pages\n'
               '- Swapping toolbar pages\n'
               '\n'
               'Please join the Discord (see below) and tell me which one you '
               'would use, \n'
               'so they can be fast-tracked.  \n'
               '\n'),
 Fragment(document_cs='27136ae72fbe5b19df2148d24354798a7b030a78df952891c7b6ef0782bea9c0',
          id=14,
          lineno=68,
          tokens=207,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='## Installation\n'
               '1. Exit from Space Engineers\n'
               '2. Install the [Plugin '
               'Loader](https://steamcommunity.com/sharedfiles/filedetails/?id=2407984968)\n'
               '3. Start Space Engineers\n'
               '4. Open the Plugins menu (should be in the Main Menu)\n'
               '5. Enable the Toolbar Manager plugin\n'
               '6. Save and let the game restart\n'
               '\n'
               'After enabling the plugin it will be active for all single- '
               'and multiplayer worlds.\n'
               '\n'
               '*Enjoy!*\n'
               '\n'
               '## Want to know more?\n'
               '- [SE Mods Discord](https://discord.gg/PYPFPGf3Ca)\n'
               '- [Plugin Loader Discord](https://discord.gg/6ETGRU3CzR)\n'
               '- [YouTube '
               'Channel](https://www.youtube.com/channel/UCc5ar3cW9qoOgdBb1FM_rxQ)\n'
               '- [Source '
               'code](https://github.com/viktor-ferenczi/toolbar-manager)\n'
               '- [Bug reports](https://discord.gg/x3Z8Ug5YkQ)\n'
               '\n'),
 Fragment(document_cs='27136ae72fbe5b19df2148d24354798a7b030a78df952891c7b6ef0782bea9c0',
          id=15,
          lineno=87,
          tokens=176,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='## Credits\n'
               '\n'
               '### Patreon Supporters\n'
               '\n'
               '#### Admiral level\n'
               '- BetaMark\n'
               '- Mordith - Guardians SE\n'
               '- Robot10\n'
               '- Casinost\n'
               '- wafoxxx\n'
               '\n'
               '#### Captain level\n'
               '- Diggz\n'
               '- lazul\n'
               '- jiringgot\n'
               '- Kam Solastor\n'
               '- NeonDrip\n'
               '- NeVaR\n'
               '- opesoorry\n'
               '- NeVaR\n'
               '- Jimbo\n'
               '- Lotan\n'
               '\n'
               '#### Testers\n'
               '- Avaness\n'
               '- ...\n'
               '\n'
               '### Creators\n'
               '- avaness - Plugin Loader, Racing Display\n'
               '- Mordith - Guardians SE\n'
               '- Mike Dude - Guardians SE\n'
               '- SwiftyTech - Stargate Dimensions\n'
               '- Fred XVI - Racing maps\n'
               '- Kamikaze - M&M mod\n'
               '- LTP\n'
               '\n'
               '**Thank you very much for all your support and hard work on '
               'testing!**'),
 Fragment(document_cs='27136ae72fbe5b19df2148d24354798a7b030a78df952891c7b6ef0782bea9c0',
          id=16,
          lineno=1,
          tokens=52,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='# Toolbar Manager\n'
               '## Features\n'
               '### Toolbars\n'
               '### Quick block selection\n'
               '### Planned features\n'
               '## Installation\n'
               '## Want to know more?\n'
               '## Credits\n'
               '### Patreon Supporters\n'
               '#### Admiral level\n'
               '#### Captain level\n'
               '#### Testers\n'
               '### Creators\n'),
 Fragment(document_cs='2937863fb1807d91801bc84075221f38c70ab6a45215f25f80a0570ab67c868c',
          id=17,
          lineno=1,
          tokens=221,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='MIT License\n'
               '\n'
               'Copyright (c) 2021 Viktor Ferenczi\n'
               '\n'
               'Permission is hereby granted, free of charge, to any person '
               'obtaining a copy\n'
               'of this software and associated documentation files (the '
               '"Software"), to deal\n'
               'in the Software without restriction, including without '
               'limitation the rights\n'
               'to use, copy, modify, merge, publish, distribute, sublicense, '
               'and/or sell\n'
               'copies of the Software, and to permit persons to whom the '
               'Software is\n'
               'furnished to do so, subject to the following conditions:\n'
               '\n'
               'The above copyright notice and this permission notice shall be '
               'included in all\n'
               'copies or substantial portions of the Software.\n'
               '\n'
               'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY '
               'KIND, EXPRESS OR\n'
               'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF '
               'MERCHANTABILITY,\n'
               'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO '
               'EVENT SHALL THE\n'
               'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES '
               'OR OTHER\n'
               'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR '
               'OTHERWISE, ARISING FROM,\n'
               'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER '
               'DEALINGS IN THE\n'
               'SOFTWARE.\n'),
 Fragment(document_cs='2937863fb1807d91801bc84075221f38c70ab6a45215f25f80a0570ab67c868c',
          id=18,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=19,
          lineno=7,
          tokens=244,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Slot',
          body='public class Slot\n'
               '    {\n'
               '        public readonly int Index;\n'
               '        public MyObjectBuilder_ToolbarItem Builder { get; '
               'private set; }\n'
               '        public MyDefinitionId Id => Builder?.GetId() ?? '
               'default(MyDefinitionId);\n'
               '        public int Page => Index / 9;\n'
               '        public int Number => Index % 9;\n'
               '        public bool IsEmpty => Builder == null;\n'
               '\n'
               '        public Slot(int index)\n'
               '        {\n'
               '            Index = index;\n'
               '        }\n'
               '\n'
               '        public Slot(int index, MyDefinitionId id)\n'
               '        {\n'
               '            Index = index;\n'
               '\n'
               '            if '
               '(!MyDefinitionManager.Static.TryGetDefinition(id, out '
               'MyDefinitionBase definitionBase))\n'
               '                return;\n'
               '\n'
               '            Builder = '
               'MyToolbarItemFactory.ObjectBuilderFromDefinition(definitionBase);\n'
               '        }\n'
               '\n'
               '        public Slot(int index, MyToolbarItem item)\n'
               '        {\n'
               '            Index = index;\n'
               '\n'
               '            if (item == null)\n'
               '                return;\n'
               '\n'
               '            Builder = item.GetObjectBuilder();\n'
               '        }\n'
               '\n'
               '        public Slot(int index, MyObjectBuilder_ToolbarItem '
               'itemBuilder)\n'
               '        {\n'
               '            Index = index;\n'
               '\n'
               '            if (itemBuilder == null)\n'
               '                return;\n'
               '\n'
               '            Builder = itemBuilder;\n'
               '        }\n'
               '\n'
               '        public Slot(int index, MyToolbarItemDefinition '
               'itemDefinition)\n'
               '        {\n'
               '            Index = index;\n'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=20,
          lineno=54,
          tokens=205,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Slot',
          body='\n'
               '            if (itemDefinition == null)\n'
               '                return;\n'
               '\n'
               '            Builder = itemDefinition.GetObjectBuilder();\n'
               '        }\n'
               '\n'
               '        public void Clear()\n'
               '        {\n'
               '            Builder = null;\n'
               '        }\n'
               '\n'
               '        public void Get(MyToolbar toolbar)\n'
               '        {\n'
               '            var toolbarItem = toolbar.GetItemAtIndex(Index);\n'
               '            if (toolbarItem == null)\n'
               '            {\n'
               '                Clear();\n'
               '                return;\n'
               '            }\n'
               '\n'
               '            Builder = toolbarItem.GetObjectBuilder();\n'
               '        }\n'
               '\n'
               '        public void Set(MyToolbar toolbar)\n'
               '        {\n'
               '            if (IsEmpty)\n'
               '            {\n'
               '                toolbar.SetItemAtIndex(Index, null);\n'
               '                return;\n'
               '            }\n'
               '\n'
               '            var toolbarItem = '
               'MyToolbarItemFactory.CreateToolbarItem(Builder);\n'
               '            toolbar.SetItemAtIndex(Index, toolbarItem);\n'
               '        }\n'
               '\n'
               '        public void Merge(MyToolbar toolbar)\n'
               '        {\n'
               '            if (IsEmpty)\n'
               '                return;\n'
               '\n'
               '            Set(toolbar);\n'
               '        }\n'
               '\n'
               '        public void Activate(MyToolbar toolbar)\n'
               '        {\n'
               '            if (toolbar.CurrentPage != Page)\n'
               '                toolbar.SwitchToPage(Page);\n'
               '\n'
               '            toolbar.ActivateItemAtIndex(Index);\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=21,
          lineno=16,
          tokens=54,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Slot',
          body='public Slot(int index)\n'
               '        {\n'
               '            Index = index;\n'
               '        }public Slot(int index, MyToolbarItemDefinition '
               'itemDefinition)\n'
               '        {\n'
               '            Index = index;\n'
               '\n'
               '            if (itemDefinition == null)\n'
               '                return;\n'
               '\n'
               '            Builder = itemDefinition.GetObjectBuilder();\n'
               '        }'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=22,
          lineno=21,
          tokens=56,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Slot',
          body='public Slot(int index, MyDefinitionId id)\n'
               '        {\n'
               '            Index = index;\n'
               '\n'
               '            if '
               '(!MyDefinitionManager.Static.TryGetDefinition(id, out '
               'MyDefinitionBase definitionBase))\n'
               '                return;\n'
               '\n'
               '            Builder = '
               'MyToolbarItemFactory.ObjectBuilderFromDefinition(definitionBase);\n'
               '        }'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=23,
          lineno=31,
          tokens=36,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Slot',
          body='public Slot(int index, MyToolbarItem item)\n'
               '        {\n'
               '            Index = index;\n'
               '\n'
               '            if (item == null)\n'
               '                return;\n'
               '\n'
               '            Builder = item.GetObjectBuilder();\n'
               '        }'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=24,
          lineno=41,
          tokens=38,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Slot',
          body='public Slot(int index, MyObjectBuilder_ToolbarItem '
               'itemBuilder)\n'
               '        {\n'
               '            Index = index;\n'
               '\n'
               '            if (itemBuilder == null)\n'
               '                return;\n'
               '\n'
               '            Builder = itemBuilder;\n'
               '        }'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=25,
          lineno=61,
          tokens=13,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Clear',
          body='public void Clear()\n'
               '        {\n'
               '            Builder = null;\n'
               '        }'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=26,
          lineno=66,
          tokens=47,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Get',
          body='public void Get(MyToolbar toolbar)\n'
               '        {\n'
               '            var toolbarItem = toolbar.GetItemAtIndex(Index);\n'
               '            if (toolbarItem == null)\n'
               '            {\n'
               '                Clear();\n'
               '                return;\n'
               '            }\n'
               '\n'
               '            Builder = toolbarItem.GetObjectBuilder();\n'
               '        }'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=27,
          lineno=78,
          tokens=57,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Set',
          body='public void Set(MyToolbar toolbar)\n'
               '        {\n'
               '            if (IsEmpty)\n'
               '            {\n'
               '                toolbar.SetItemAtIndex(Index, null);\n'
               '                return;\n'
               '            }\n'
               '\n'
               '            var toolbarItem = '
               'MyToolbarItemFactory.CreateToolbarItem(Builder);\n'
               '            toolbar.SetItemAtIndex(Index, toolbarItem);\n'
               '        }'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=28,
          lineno=90,
          tokens=23,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Merge',
          body='public void Merge(MyToolbar toolbar)\n'
               '        {\n'
               '            if (IsEmpty)\n'
               '                return;\n'
               '\n'
               '            Set(toolbar);\n'
               '        }'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=29,
          lineno=98,
          tokens=36,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Activate',
          body='public void Activate(MyToolbar toolbar)\n'
               '        {\n'
               '            if (toolbar.CurrentPage != Page)\n'
               '                toolbar.SwitchToPage(Page);\n'
               '\n'
               '            toolbar.ActivateItemAtIndex(Index);\n'
               '        }'),
 Fragment(document_cs='2dd90f059f1f475c3cc42b61cd6bd226d01990ded68481aee5b54f2c844c0dbf',
          id=30,
          lineno=1,
          tokens=108,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Slot\n'
               '  Methods: Activate Clear Get Merge Set Slot\n'
               '  Usages: ActivateItemAtIndex Builder Clear CreateToolbarItem '
               'CurrentPage Definitions Game GetId GetItemAtIndex '
               'GetObjectBuilder Helpers Id Index IsEmpty Logic '
               'MyDefinitionBase MyDefinitionId MyDefinitionManager '
               'MyObjectBuilder_ToolbarItem MyToolbar MyToolbarItem '
               'MyToolbarItemDefinition MyToolbarItemFactory Number '
               'ObjectBuilderFromDefinition Page Sandbox Screens Set '
               'SetItemAtIndex Static SwitchToPage ToolbarManager '
               'TryGetDefinition VRage definitionBase id index item '
               'itemBuilder itemDefinition toolbar toolbarItem\n'),
 Fragment(document_cs='2e6630aff2a2335427c2e57675b8bb3721172d61962a82312e01bd5bba4b7947',
          id=31,
          lineno=1,
          tokens=25,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Usages: AssemblyCompany AssemblyConfiguration '
               'AssemblyCopyright AssemblyCulture AssemblyDescription '
               'AssemblyFileVersion AssemblyProduct AssemblyTitle '
               'AssemblyTrademark AssemblyVersion ComVisible Guid '
               'InteropServices Reflection Runtime System\n'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=32,
          lineno=13,
          tokens=199,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='CustomToolbarConfigScreen',
          body='[SuppressMessage("ReSharper", "UnusedMember.Global")]\n'
               '    public class CustomToolbarConfigScreen : '
               'MyGuiScreenCubeBuilder\n'
               '    {\n'
               '        private readonly CustomSearchCondition '
               'customSearchCondition = new CustomSearchCondition();\n'
               '        private MyGuiControlLabel searchInfoLabel;\n'
               '\n'
               '        public CustomToolbarConfigScreen(int scrollOffset = 0, '
               'MyCubeBlock owner = null, int? gamepadSlot = null) : '
               'base(scrollOffset, owner, gamepadSlot)\n'
               '        {\n'
               '        }\n'
               '\n'
               '        public CustomToolbarConfigScreen(int scrollOffset, '
               'MyCubeBlock owner, string selectedPage, bool hideOtherPages, '
               'int? gamepadSlot = null) : base(scrollOffset, owner, '
               'selectedPage, hideOtherPages, gamepadSlot)\n'
               '        {\n'
               '        }\n'
               '\n'
               '        public void SetSearchText(string text)\n'
               '        {\n'
               '            m_searchBox.SearchText = text;\n'
               '            m_searchBox.TextBox.MoveCarriageToEnd();\n'
               '        }\n'
               '\n'
               '        protected override void '
               'AddToolsAndAnimations(IMySearchCondition searchCondition)\n'
               '        {\n'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=33,
          lineno=35,
          tokens=243,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='CustomToolbarConfigScreen',
          body='            if (searchCondition == m_nameSearchCondition)\n'
               '            {\n'
               '                customSearchCondition.SearchName = '
               'm_searchBox.TextBox.Text;\n'
               '                '
               'base.AddToolsAndAnimations(customSearchCondition);\n'
               '                return;\n'
               '            }\n'
               '\n'
               '            base.AddToolsAndAnimations(searchCondition);\n'
               '        }\n'
               '\n'
               '        protected override void '
               'UpdateGridBlocksBySearchCondition(IMySearchCondition '
               'searchCondition)\n'
               '        {\n'
               '            if (searchCondition == m_nameSearchCondition)\n'
               '            {\n'
               '                customSearchCondition.SearchName = '
               'm_searchBox.TextBox.Text;\n'
               '                '
               'base.UpdateGridBlocksBySearchCondition(customSearchCondition);\n'
               '                return;\n'
               '            }\n'
               '\n'
               '            '
               'base.UpdateGridBlocksBySearchCondition(searchCondition);\n'
               '        }\n'
               '\n'
               '        public override void HandleInput(bool '
               'receivedFocusInThisUpdate)\n'
               '        {\n'
               '            if (MyInput.Static.IsNewKeyPressed(MyKeys.Enter))\n'
               '            {\n'
               '                LoadSelectedItem();\n'
               '                return;\n'
               '            }\n'
               '\n'
               '            base.HandleInput(receivedFocusInThisUpdate);\n'
               '        }\n'
               '\n'
               '        private void LoadSelectedItem()\n'
               '        {\n'
               '            if (m_gridBlocks.SelectedIndex == null)\n'
               '                return;\n'
               '\n'
               '            var selectedItem = '
               'm_gridBlocks.GetItemAt(m_gridBlocks.SelectedIndex ?? 0);\n'
               '            if (!(selectedItem?.UserData is GridItemUserData '
               'userData))\n'
               '                return;\n'
               '\n'
               '            var toolbarItemBuilder = userData.ItemData();\n'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=34,
          lineno=78,
          tokens=196,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='CustomToolbarConfigScreen',
          body='            if (toolbarItemBuilder is '
               'MyObjectBuilder_ToolbarItemEmpty)\n'
               '                return;\n'
               '\n'
               '            var toolbarItem = '
               'MyToolbarItemFactory.CreateToolbarItem(userData.ItemData());\n'
               '            if (toolbarItem is MyToolbarItemActions && '
               'MyInput.Static.IsJoystickLastUsed)\n'
               '                return;\n'
               '\n'
               '            this.AddGridItemToToolbar(toolbarItemBuilder);\n'
               '\n'
               '            CloseScreen();\n'
               '        }\n'
               '\n'
               '        public override void RecreateControls(bool '
               'contructor)\n'
               '        {\n'
               '            base.RecreateControls(contructor);\n'
               '\n'
               '            searchInfoLabel = new MyGuiControlLabel(\n'
               '                new Vector2(m_searchBox.PositionX + '
               'm_searchBox.Size.X * 0.5f + 0.02f, m_searchBox.PositionY + '
               '0.005f),\n'
               '                new Vector2(0.2f, m_searchBox.Size.Y))\n'
               '            {\n'
               '                Font = m_searchBox.TextBox.TextFont,\n'
               '                Text = "Quick Search Mode"\n'
               '            };\n'
               '\n'
               '            Controls.Add(searchInfoLabel);\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=35,
          lineno=19,
          tokens=95,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CustomToolbarConfigScreen',
          body='public CustomToolbarConfigScreen(int scrollOffset = 0, '
               'MyCubeBlock owner = null, int? gamepadSlot = null) : '
               'base(scrollOffset, owner, gamepadSlot)\n'
               '        {\n'
               '        }public CustomToolbarConfigScreen(int scrollOffset, '
               'MyCubeBlock owner, string selectedPage, bool hideOtherPages, '
               'int? gamepadSlot = null) : base(scrollOffset, owner, '
               'selectedPage, hideOtherPages, gamepadSlot)\n'
               '        {\n'
               '        }'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=36,
          lineno=27,
          tokens=31,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='SetSearchText',
          body='public void SetSearchText(string text)\n'
               '        {\n'
               '            m_searchBox.SearchText = text;\n'
               '            m_searchBox.TextBox.MoveCarriageToEnd();\n'
               '        }'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=37,
          lineno=33,
          tokens=68,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='AddToolsAndAnimations',
          body='protected override void '
               'AddToolsAndAnimations(IMySearchCondition searchCondition)\n'
               '        {\n'
               '            if (searchCondition == m_nameSearchCondition)\n'
               '            {\n'
               '                customSearchCondition.SearchName = '
               'm_searchBox.TextBox.Text;\n'
               '                '
               'base.AddToolsAndAnimations(customSearchCondition);\n'
               '                return;\n'
               '            }\n'
               '\n'
               '            base.AddToolsAndAnimations(searchCondition);\n'
               '        }'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=38,
          lineno=45,
          tokens=74,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='UpdateGridBlocksBySearchCondition',
          body='protected override void '
               'UpdateGridBlocksBySearchCondition(IMySearchCondition '
               'searchCondition)\n'
               '        {\n'
               '            if (searchCondition == m_nameSearchCondition)\n'
               '            {\n'
               '                customSearchCondition.SearchName = '
               'm_searchBox.TextBox.Text;\n'
               '                '
               'base.UpdateGridBlocksBySearchCondition(customSearchCondition);\n'
               '                return;\n'
               '            }\n'
               '\n'
               '            '
               'base.UpdateGridBlocksBySearchCondition(searchCondition);\n'
               '        }'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=39,
          lineno=57,
          tokens=51,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='HandleInput',
          body='public override void HandleInput(bool '
               'receivedFocusInThisUpdate)\n'
               '        {\n'
               '            if (MyInput.Static.IsNewKeyPressed(MyKeys.Enter))\n'
               '            {\n'
               '                LoadSelectedItem();\n'
               '                return;\n'
               '            }\n'
               '\n'
               '            base.HandleInput(receivedFocusInThisUpdate);\n'
               '        }'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=40,
          lineno=68,
          tokens=137,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='LoadSelectedItem',
          body='private void LoadSelectedItem()\n'
               '        {\n'
               '            if (m_gridBlocks.SelectedIndex == null)\n'
               '                return;\n'
               '\n'
               '            var selectedItem = '
               'm_gridBlocks.GetItemAt(m_gridBlocks.SelectedIndex ?? 0);\n'
               '            if (!(selectedItem?.UserData is GridItemUserData '
               'userData))\n'
               '                return;\n'
               '\n'
               '            var toolbarItemBuilder = userData.ItemData();\n'
               '            if (toolbarItemBuilder is '
               'MyObjectBuilder_ToolbarItemEmpty)\n'
               '                return;\n'
               '\n'
               '            var toolbarItem = '
               'MyToolbarItemFactory.CreateToolbarItem(userData.ItemData());\n'
               '            if (toolbarItem is MyToolbarItemActions && '
               'MyInput.Static.IsJoystickLastUsed)\n'
               '                return;\n'
               '\n'
               '            this.AddGridItemToToolbar(toolbarItemBuilder);\n'
               '\n'
               '            CloseScreen();\n'
               '        }'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=41,
          lineno=90,
          tokens=119,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='RecreateControls',
          body='public override void RecreateControls(bool contructor)\n'
               '        {\n'
               '            base.RecreateControls(contructor);\n'
               '\n'
               '            searchInfoLabel = new MyGuiControlLabel(\n'
               '                new Vector2(m_searchBox.PositionX + '
               'm_searchBox.Size.X * 0.5f + 0.02f, m_searchBox.PositionY + '
               '0.005f),\n'
               '                new Vector2(0.2f, m_searchBox.Size.Y))\n'
               '            {\n'
               '                Font = m_searchBox.TextBox.TextFont,\n'
               '                Text = "Quick Search Mode"\n'
               '            };\n'
               '\n'
               '            Controls.Add(searchInfoLabel);\n'
               '        }'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=42,
          lineno=16,
          tokens=12,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='CustomSearchCondition',
          body='CustomSearchCondition customSearchCondition = new '
               'CustomSearchCondition()'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=43,
          lineno=17,
          tokens=7,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='MyGuiControlLabel',
          body='MyGuiControlLabel searchInfoLabel'),
 Fragment(document_cs='36e3b53b6c77ba7c265232e687496b2c095a1ae699ee781dd787ae3034ae62da',
          id=44,
          lineno=1,
          tokens=229,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: CustomToolbarConfigScreen\n'
               '  Methods: AddToolsAndAnimations CustomToolbarConfigScreen '
               'HandleInput LoadSelectedItem RecreateControls SetSearchText '
               'UpdateGridBlocksBySearchCondition\n'
               '  Variables: CustomSearchCondition MyGuiControlLabel\n'
               '  Usages: Add AddGridItemToToolbar AddToolsAndAnimations '
               'CloseScreen CodeAnalysis Controls CreateToolbarItem '
               'CustomSearchCondition Diagnostics Enter Entities Extensions '
               'Font GUI Game GetItemAt Graphics GridItemUserData Gui '
               'HandleInput Helpers IMySearchCondition Input '
               'IsJoystickLastUsed IsNewKeyPressed ItemData LoadSelectedItem '
               'MoveCarriageToEnd MyCubeBlock MyGuiControlLabel '
               'MyGuiScreenCubeBuilder MyInput MyKeys '
               'MyObjectBuilder_ToolbarItemEmpty MyToolbarItemActions '
               'MyToolbarItemFactory PositionX PositionY RecreateControls '
               'Sandbox Screens SearchName SearchText SelectedIndex Size '
               'Static SuppressMessage System Text TextBox TextFont '
               'ToolbarManager UpdateGridBlocksBySearchCondition UserData '
               'VRage VRageMath Vector2 X Y contructor customSearchCondition '
               'gamepadSlot hideOtherPages m_gridBlocks m_nameSearchCondition '
               'm_searchBox owner receivedFocusInThisUpdate scrollOffset '
               'searchCondition searchInfoLabel selectedItem selectedPage text '
               'toolbarItem toolbarItemBuilder userData\n'),
 Fragment(document_cs='3ac85280a77cc96cb32fae67d6c188ff6c718ad13f9c6bb8325b76d213bbd602',
          id=45,
          lineno=6,
          tokens=100,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='MyGuiSandboxExt',
          body='public static class MyGuiSandboxExt\n'
               '    {\n'
               '        public static void Show(StringBuilder text, '
               'StringBuilder caption, MyMessageBoxStyleEnum type = '
               'MyMessageBoxStyleEnum.Error)\n'
               '            => '
               'MyGuiSandbox.AddScreen(MyGuiSandbox.CreateMessageBox(type, '
               'messageText: text, messageCaption: caption));\n'
               '\n'
               '        public static void Show(string text, string caption, '
               'MyMessageBoxStyleEnum type = MyMessageBoxStyleEnum.Error)\n'
               '            => Show(new StringBuilder(text), new '
               'StringBuilder(caption), type);\n'
               '    }'),
 Fragment(document_cs='3ac85280a77cc96cb32fae67d6c188ff6c718ad13f9c6bb8325b76d213bbd602',
          id=46,
          lineno=8,
          tokens=49,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Show',
          body='public static void Show(StringBuilder text, StringBuilder '
               'caption, MyMessageBoxStyleEnum type = '
               'MyMessageBoxStyleEnum.Error)\n'
               '            => '
               'MyGuiSandbox.AddScreen(MyGuiSandbox.CreateMessageBox(type, '
               'messageText: text, messageCaption: caption));'),
 Fragment(document_cs='3ac85280a77cc96cb32fae67d6c188ff6c718ad13f9c6bb8325b76d213bbd602',
          id=47,
          lineno=11,
          tokens=36,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Show',
          body='public static void Show(string text, string caption, '
               'MyMessageBoxStyleEnum type = MyMessageBoxStyleEnum.Error)\n'
               '            => Show(new StringBuilder(text), new '
               'StringBuilder(caption), type);'),
 Fragment(document_cs='3ac85280a77cc96cb32fae67d6c188ff6c718ad13f9c6bb8325b76d213bbd602',
          id=48,
          lineno=1,
          tokens=49,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: MyGuiSandboxExt\n'
               '  Methods: Show\n'
               '  Usages: AddScreen CreateMessageBox Error Extensions GUI '
               'Graphics MyGuiSandbox MyMessageBoxStyleEnum Sandbox Show '
               'StringBuilder System Text ToolbarManager caption '
               'messageCaption messageText text type\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=49,
          lineno=19,
          tokens=239,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='public class ListDialog : MyGuiScreenDebugBase\n'
               '    {\n'
               '        private MyGuiControlTable toolbarTable;\n'
               '        private MyGuiControlButton loadButton;\n'
               '        private MyGuiControlButton mergeButton;\n'
               '        private MyGuiControlButton renameButton;\n'
               '        private MyGuiControlButton deleteButton;\n'
               '        private MyGuiControlButton cancelButton;\n'
               '\n'
               '        private readonly Action<string, bool> callBack;\n'
               '        private readonly string caption;\n'
               '        private readonly string defaultName;\n'
               '        private readonly string dirPath;\n'
               '        private readonly int[] usedSlotCounts = new int[9];\n'
               '\n'
               '        public ListDialog(\n'
               '            Action<string, bool> callBack,\n'
               '            string caption,\n'
               '            string defaultName,\n'
               '            string dirPath)\n'
               '            : base(new Vector2(0.5f, 0.5f), new Vector2(1f, '
               '0.8f), MyGuiConstants.SCREEN_BACKGROUND_COLOR * '
               'MySandboxGame.Config.UIBkOpacity, true)\n'
               '        {\n'
               '            this.callBack = callBack;\n'
               '            this.caption = caption;\n'
               '            this.defaultName = defaultName;\n'
               '            this.dirPath = dirPath;\n'
               '\n'
               '            RecreateControls(true);\n'
               '\n'
               '            CanBeHidden = true;\n'
               '            CanHideOthers = true;\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=50,
          lineno=50,
          tokens=115,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='            CloseButtonEnabled = true;\n'
               '\n'
               '            m_onEnterCallback = ReturnLoad;\n'
               '        }\n'
               '\n'
               '        public override void RecreateControls(bool '
               'constructor)\n'
               '        {\n'
               '            base.RecreateControls(constructor);\n'
               '\n'
               '            AddCaption(caption, Color.White.ToVector4(), new '
               'Vector2(0.0f, 0.003f));\n'
               '\n'
               '            CreateListBox();\n'
               '            CreateButtons();\n'
               '        }\n'
               '\n'
               '        private Vector2 DialogSize => m_size ?? Vector2.One;\n'
               '\n'
               '        private void CreateListBox()\n'
               '        {\n'
               '            toolbarTable = new MyGuiControlTable\n'
               '            {\n'
               '                Position = new Vecto'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=51,
          lineno=71,
          tokens=166,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='r2(0.001f, -0.5f * DialogSize.Y + 0.1f),\n'
               '                Size = new Vector2(0.85f * DialogSize.X, '
               'DialogSize.Y - 0.25f),\n'
               '                OriginAlign = '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_TOP,\n'
               '                ColumnsCount = 10,\n'
               '                VisibleRowsCount = 15,\n'
               '            };\n'
               '\n'
               '            var q = 0.76f;\n'
               '            var w = 0.22f / 9f;\n'
               '            toolbarTable.SetCustomColumnWidths(new[] { q, w, '
               'w, w, w, w, w, w, w, w });\n'
               '            toolbarTable.SetColumnName(0, new '
               'StringBuilder("Name"));\n'
               '            toolbarTable.SetColumnComparison(0, '
               'CellTextComparison);\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=52,
          lineno=83,
          tokens=110,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='            for (var i = 1; i < 10; i++)\n'
               '                toolbarTable.SetColumnName(i, new '
               'StringBuilder($"{i}"));\n'
               '            toolbarTable.SortByColumn(0);\n'
               '            ListFiles();\n'
               '            toolbarTable.ItemDoubleClicked += '
               'OnItemDoubleClicked;\n'
               '            Controls.Add(toolbarTable);\n'
               '        }\n'
               '\n'
               '        private int CellTextComparison(MyGuiControlTable.Cell '
               'x, MyGuiControlTable.Cell y)\n'
               '        {\n'
               '            return TextComparison(x.Text, y.Text);\n'
               '        }\n'
               '\n'
               '        private int TextComparison(StringBuilder x, '
               'StringBuilder y)\n'
               '        {\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=53,
          lineno=98,
          tokens=142,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='            if (x == null)\n'
               '                return y == null ? 0 : 1;\n'
               '\n'
               '            return y == null ? -1 : x.CompareTo(y);\n'
               '        }\n'
               '\n'
               '        private void CreateButtons()\n'
               '        {\n'
               '            loadButton = new MyGuiControlButton(\n'
               '                visualStyle: '
               'MyGuiControlButtonStyleEnum.Default,\n'
               '                originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_CENTER,\n'
               '                text: new StringBuilder("Load"), '
               'onButtonClick: OnLoad);\n'
               '\n'
               '            mergeButton = new MyGuiControlButton(\n'
               '                visualStyle: '
               'MyGuiControlButtonStyleEnum.Default,\n'
               '                originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_CENTER,\n'
               '                text: new Strin'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=54,
          lineno=114,
          tokens=135,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='gBuilder("Merge"), onButtonClick: OnMerge);\n'
               '\n'
               '            renameButton = new MyGuiControlButton(\n'
               '                visualStyle: '
               'MyGuiControlButtonStyleEnum.Small,\n'
               '                originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_CENTER,\n'
               '                text: new StringBuilder("Rename"), '
               'onButtonClick: OnRename);\n'
               '\n'
               '            deleteButton = new MyGuiControlButton(\n'
               '                visualStyle: '
               'MyGuiControlButtonStyleEnum.Small,\n'
               '                originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_CENTER,\n'
               '                text: new StringBuilder("Delete"), '
               'onButtonClick: OnDelete);\n'
               '\n'
               '            cancelButton = new MyGuiControlButton(\n'
               '                visualStyle: MyGuiC'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=55,
          lineno=127,
          tokens=180,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='ontrolButtonStyleEnum.Small,\n'
               '                originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_CENTER,\n'
               '                text: MyTexts.Get(MyCommonTexts.Cancel), '
               'onButtonClick: OnCancel);\n'
               '\n'
               '            var xs = 0.85f * DialogSize.X;\n'
               '            var y = 0.5f * (DialogSize.Y - 0.15f);\n'
               '            loadButton.Position = new Vector2(-0.39f * xs, '
               'y);\n'
               '            mergeButton.Position = new Vector2(-0.16f * xs, '
               'y);\n'
               '            renameButton.Position = new Vector2(0.06f * xs, '
               'y);\n'
               '            deleteButton.Position = new Vector2(0.24f * xs, '
               'y);\n'
               '            cancelButton.Position = new Vector2(0.42f * xs, '
               'y);\n'
               '\n'
               '            loadButton.SetToolTip("Loads the selected toolbar '
               'replacing the c'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=56,
          lineno=139,
          tokens=233,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='urrent one");\n'
               '            mergeButton.SetToolTip("Merges the selected '
               'toolbar into the current one");\n'
               '            renameButton.SetToolTip("Renames the selected '
               'toolbar save file");\n'
               '            deleteButton.SetToolTip("Deletes the selected '
               'toolbar save file");\n'
               '            '
               'cancelButton.SetToolTip(MyTexts.GetString(MySpaceTexts.ToolTipOptionsSpace_Cancel));\n'
               '\n'
               '            Controls.Add(loadButton);\n'
               '            Controls.Add(mergeButton);\n'
               '            Controls.Add(renameButton);\n'
               '            Controls.Add(deleteButton);\n'
               '            Controls.Add(cancelButton);\n'
               '        }\n'
               '\n'
               '        private void ListFiles()\n'
               '        {\n'
               '            foreach (var path in '
               'Directory.EnumerateFiles(dirPath))\n'
               '            {\n'
               '                if (!path.EndsWith(".xml"))\n'
               '                    continue;\n'
               '\n'
               '                AddRowForFile(path);\n'
               '            }\n'
               '\n'
               '            if (TryFindListItem(defaultName, out var index))\n'
               '                toolbarTable.SelectedRowIndex = index;\n'
               '        }\n'
               '\n'
               '        private void AddRowForFile(string path)\n'
               '        {\n'
               '            var json = ReadJson(path);\n'
               '            CountUsedSlots(json);\n'
               '\n'
               '            var fileName = Path.GetFileName(path);\n'
               '            var name = fileName.Substring(0, fileName.Length - '
               '4);\n'
               '\n'
               '            var row = new MyGuiControlTable.Row(path);\n'
               '            row.AddCell(new MyGuiControlTable.Cell(name));\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=57,
          lineno=176,
          tokens=199,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='            for (var i = 0; i < 9; i++)\n'
               '                row.AddCell(new '
               'MyGuiControlTable.Cell(usedSlotCounts[i] > 0 ? '
               '$"{usedSlotCounts[i]}" : "-"));\n'
               '            toolbarTable.Add(row);\n'
               '        }\n'
               '\n'
               '        private static JsonData ReadJson(string xmlPath)\n'
               '        {\n'
               '            var jsonPath = XmlToJsonPath(xmlPath);\n'
               '\n'
               '            if (!File.Exists(jsonPath))\n'
               '                return null;\n'
               '\n'
               '            try\n'
               '            {\n'
               '                var jsonText = File.ReadAllText(jsonPath);\n'
               '                return JsonMapper.ToObject(jsonText);\n'
               '            }\n'
               '            catch (JsonException e)\n'
               '            {\n'
               '                MyLog.Default.Warning($"ToolbarManager: Failed '
               'to load JSON toolbar file \\"{jsonPath}\\" ({e})");\n'
               '                return null;\n'
               '            }\n'
               '        }\n'
               '\n'
               '        private static string XmlToJsonPath(string xmlPath)\n'
               '        {\n'
               '            return xmlPath.Substring(0, xmlPath.Length - 4) + '
               '".json";\n'
               '        }\n'
               '\n'
               '        private void CountUsedSlots(JsonData json)\n'
               '        {\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=58,
          lineno=207,
          tokens=189,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='            for (var i = 0; i < 9; i++)\n'
               '                usedSlotCounts[i] = 0;\n'
               '\n'
               '            try\n'
               '            {\n'
               '                var slots = json["Slots"];\n'
               '                if (slots == null)\n'
               '                    return;\n'
               '\n'
               '                var slotCount = slots.Count;\n'
               '                for (var i = 0; i < slotCount; i++)\n'
               '                {\n'
               '                    var page = i / 9;\n'
               '                    if (page > 8)\n'
               '                        break;\n'
               '                    if (!(bool)slots[i]["IsEmpty"])\n'
               '                        usedSlotCounts[page]++;\n'
               '                }\n'
               '            }\n'
               '            catch (SystemException e)\n'
               '            {\n'
               '                MyLog.Default.Warning($"ToolbarManager: Failed '
               'to count free slots ({e})");\n'
               '            }\n'
               '        }\n'
               '\n'
               '        private void OnItemDoubleClicked(MyGuiControlTable '
               'table, MyGuiControlTable.EventArgs args)\n'
               '        {\n'
               '            ReturnLoad();\n'
               '        }\n'
               '\n'
               '        private void CallResultCallback(string text, bool '
               'merge)\n'
               '        {\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=59,
          lineno=239,
          tokens=240,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='            if (text == null)\n'
               '                return;\n'
               '\n'
               '            callBack(text, merge);\n'
               '        }\n'
               '\n'
               '        private void ReturnLoad()\n'
               '        {\n'
               '            CallResultCallback(SelectedName, false);\n'
               '            CloseScreen();\n'
               '        }\n'
               '\n'
               '        private void ReturnMerge()\n'
               '        {\n'
               '            CallResultCallback(SelectedName, true);\n'
               '            CloseScreen();\n'
               '        }\n'
               '\n'
               '        private string SelectedName => '
               'toolbarTable.SelectedRow?.GetCell(0)?.Text?.ToString() ?? "";\n'
               '\n'
               '        private void OnLoad(MyGuiControlButton button) => '
               'ReturnLoad();\n'
               '        private void OnMerge(MyGuiControlButton button) => '
               'ReturnMerge();\n'
               '        private void OnCancel(MyGuiControlButton button) => '
               'CloseScreen();\n'
               '\n'
               '        private void OnRename(MyGuiControlButton _)\n'
               '        {\n'
               '            var oldName = SelectedName;\n'
               '            if (oldName == "")\n'
               '                return;\n'
               '\n'
               '            MyGuiSandbox.AddScreen(new NameDialog(newName => '
               'OnNewNameSpecified(oldName, newName), "Rename saved toolbar", '
               'oldName));\n'
               '        }\n'
               '\n'
               '        private void OnNewNameSpecified(string oldName, string '
               'newName)\n'
               '        {\n'
               '            newName = PathExt.SanitizeFileName(newName);\n'
               '\n'
               '            var newPath = Path.Combine(dirPath, '
               '$"{newName}.xml");\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=60,
          lineno=277,
          tokens=242,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='            if (File.Exists(newPath))\n'
               '            {\n'
               '                MyGuiSandbox.AddScreen(\n'
               '                    MyGuiSandbox.CreateMessageBox(buttonType: '
               'MyMessageBoxButtonsType.YES_NO,\n'
               '                        messageText: new StringBuilder($"Are '
               'you sure to overwrite this saved '
               'toolbar?\\r\\n\\r\\n{newName}"),\n'
               '                        messageCaption: new '
               'StringBuilder("Confirmation"),\n'
               '                        callback: result => '
               'OnOverwriteForSure(result, oldName, newName)));\n'
               '            }\n'
               '            else\n'
               '            {\n'
               '                '
               'OnOverwriteForSure(MyGuiScreenMessageBox.ResultEnum.YES, '
               'oldName, newName);\n'
               '            }\n'
               '        }\n'
               '\n'
               '        private void '
               'OnOverwriteForSure(MyGuiScreenMessageBox.ResultEnum result, '
               'string oldName, string newName)\n'
               '        {\n'
               '            if (result != '
               'MyGuiScreenMessageBox.ResultEnum.YES)\n'
               '                return;\n'
               '\n'
               '            var oldPath = Path.Combine(dirPath, '
               '$"{oldName}.xml");\n'
               '            var newPath = Path.Combine(dirPath, '
               '$"{newName}.xml");\n'
               '\n'
               '            var oldJsonPath = XmlToJsonPath(oldPath);\n'
               '            var newJsonPath = XmlToJsonPath(newPath);\n'
               '\n'
               '            if (File.Exists(newPath))\n'
               '                File.Delete(newPath);\n'
               '\n'
               '            if (File.Exists(newJsonPath))\n'
               '                File.Delete(newJsonPath);\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=61,
          lineno=307,
          tokens=239,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='\n'
               '            if (File.Exists(oldPath))\n'
               '                File.Move(oldPath, newPath);\n'
               '\n'
               '            if (File.Exists(oldJsonPath))\n'
               '                File.Move(oldJsonPath, newJsonPath);\n'
               '\n'
               '            if (TryFindListItem(newName, out var '
               'overwrittenItemIndex))\n'
               '                '
               'toolbarTable.Remove(toolbarTable.GetRow(overwrittenItemIndex));\n'
               '\n'
               '            if (TryFindListItem(oldName, out var '
               'renamedItemIndex))\n'
               '            {\n'
               '                var sb = '
               'toolbarTable.GetRow(renamedItemIndex).GetCell(0).Text;\n'
               '                sb.Clear();\n'
               '                sb.Append(newName);\n'
               '            }\n'
               '        }\n'
               '\n'
               '        private void OnDelete(MyGuiControlButton _)\n'
               '        {\n'
               '            var name = SelectedName;\n'
               '            if (name == "")\n'
               '                return;\n'
               '\n'
               '            MyGuiSandbox.AddScreen(\n'
               '                MyGuiSandbox.CreateMessageBox(buttonType: '
               'MyMessageBoxButtonsType.YES_NO,\n'
               '                    messageText: new StringBuilder($"Are you '
               'sure to delete this saved toolbar?\\r\\n\\r\\n{name}"),\n'
               '                    messageCaption: new '
               'StringBuilder("Confirmation"),\n'
               '                    callback: result => '
               'OnDeleteForSure(result, name)));\n'
               '        }\n'
               '\n'
               '        private void '
               'OnDeleteForSure(MyGuiScreenMessageBox.ResultEnum result, '
               'string name)\n'
               '        {\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=62,
          lineno=340,
          tokens=181,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='ListDialog',
          body='            if (result != '
               'MyGuiScreenMessageBox.ResultEnum.YES)\n'
               '                return;\n'
               '\n'
               '            var path = Path.Combine(dirPath, $"{name}.xml");\n'
               '            var jsonPath = XmlToJsonPath(path);\n'
               '\n'
               '            if (File.Exists(path))\n'
               '                File.Delete(path);\n'
               '\n'
               '            if (File.Exists(jsonPath))\n'
               '                File.Delete(jsonPath);\n'
               '\n'
               '            if (TryFindListItem(name, out var index))\n'
               '                '
               'toolbarTable.Remove(toolbarTable.GetRow(index));\n'
               '        }\n'
               '\n'
               '        private bool TryFindListItem(string name, out int '
               'index)\n'
               '        {\n'
               '            var count = toolbarTable.RowsCount;\n'
               '            for (index = 0; index < count; index++)\n'
               '            {\n'
               '                if '
               '(toolbarTable.GetRow(index).GetCell(0).Text.ToString() == '
               'name)\n'
               '                    return true;\n'
               '            }\n'
               '\n'
               '            index = -1;\n'
               '            return false;\n'
               '        }\n'
               '\n'
               '        public override string GetFriendlyName() => '
               '"ListDialog";\n'
               '    }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=63,
          lineno=34,
          tokens=146,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='ListDialog',
          body='public ListDialog(\n'
               '            Action<string, bool> callBack,\n'
               '            string caption,\n'
               '            string defaultName,\n'
               '            string dirPath)\n'
               '            : base(new Vector2(0.5f, 0.5f), new Vector2(1f, '
               '0.8f), MyGuiConstants.SCREEN_BACKGROUND_COLOR * '
               'MySandboxGame.Config.UIBkOpacity, true)\n'
               '        {\n'
               '            this.callBack = callBack;\n'
               '            this.caption = caption;\n'
               '            this.defaultName = defaultName;\n'
               '            this.dirPath = dirPath;\n'
               '\n'
               '            RecreateControls(true);\n'
               '\n'
               '            CanBeHidden = true;\n'
               '            CanHideOthers = true;\n'
               '            CloseButtonEnabled = true;\n'
               '\n'
               '            m_onEnterCallback = ReturnLoad;\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=64,
          lineno=55,
          tokens=56,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='RecreateControls',
          body='public override void RecreateControls(bool constructor)\n'
               '        {\n'
               '            base.RecreateControls(constructor);\n'
               '\n'
               '            AddCaption(caption, Color.White.ToVector4(), new '
               'Vector2(0.0f, 0.003f));\n'
               '\n'
               '            CreateListBox();\n'
               '            CreateButtons();\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=65,
          lineno=67,
          tokens=189,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CreateListBox',
          body='private void CreateListBox()\n'
               '        {\n'
               '            toolbarTable = new MyGuiControlTable\n'
               '            {\n'
               '                Position = new Vector2(0.001f, -0.5f * '
               'DialogSize.Y + 0.1f),\n'
               '                Size = new Vector2(0.85f * DialogSize.X, '
               'DialogSize.Y - 0.25f),\n'
               '                OriginAlign = '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_TOP,\n'
               '                ColumnsCount = 10,\n'
               '                VisibleRowsCount = 15,\n'
               '            };\n'
               '\n'
               '            var q = 0.76f;\n'
               '            var w = 0.22f / 9f;\n'
               '            toolbarTable.SetCustomColumnWidths(new[] { q, w, '
               'w, w, w, w, w, w, w, w });\n'
               '            toolbarTable.SetColumnName(0, new '
               'StringBuilder("Name"));\n'
               '            toolbarTable.SetColumnComparison(0, '
               'CellTextComparison);\n'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=66,
          lineno=83,
          tokens=62,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CreateListBox',
          body='            for (var i = 1; i < 10; i++)\n'
               '                toolbarTable.SetColumnName(i, new '
               'StringBuilder($"{i}"));\n'
               '            toolbarTable.SortByColumn(0);\n'
               '            ListFiles();\n'
               '            toolbarTable.ItemDoubleClicked += '
               'OnItemDoubleClicked;\n'
               '            Controls.Add(toolbarTable);\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=67,
          lineno=91,
          tokens=33,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CellTextComparison',
          body='private int CellTextComparison(MyGuiControlTable.Cell x, '
               'MyGuiControlTable.Cell y)\n'
               '        {\n'
               '            return TextComparison(x.Text, y.Text);\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=68,
          lineno=96,
          tokens=47,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='TextComparison',
          body='private int TextComparison(StringBuilder x, StringBuilder y)\n'
               '        {\n'
               '            if (x == null)\n'
               '                return y == null ? 0 : 1;\n'
               '\n'
               '            return y == null ? -1 : x.CompareTo(y);\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=69,
          lineno=104,
          tokens=240,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CreateButtons',
          body='private void CreateButtons()\n'
               '        {\n'
               '            loadButton = new MyGuiControlButton(\n'
               '                visualStyle: '
               'MyGuiControlButtonStyleEnum.Default,\n'
               '                originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_CENTER,\n'
               '                text: new StringBuilder("Load"), '
               'onButtonClick: OnLoad);\n'
               '\n'
               '            mergeButton = new MyGuiControlButton(\n'
               '                visualStyle: '
               'MyGuiControlButtonStyleEnum.Default,\n'
               '                originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_CENTER,\n'
               '                text: new StringBuilder("Merge"), '
               'onButtonClick: OnMerge);\n'
               '\n'
               '            renameButton = new MyGuiControlButton(\n'
               '                visualStyle: '
               'MyGuiControlButtonStyleEnum.Small,\n'
               '                originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_CENTER,\n'
               '                text: new StringBuilder("Rename"), '
               'onButtonClick: OnRename);\n'
               '\n'
               '            deleteButton = new MyGuiControlButton(\n'
               '                visualStyle: '
               'MyGuiControlButtonStyleEnum.Small,\n'
               '                originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_CENTER,\n'
               '                text: new StringBuilder("Delete"), '
               'onButtonClick: OnDelete);\n'
               '\n'
               '            cancelButton = new MyGuiControlButton(\n'
               '                visualStyle: MyGuiControlB'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=70,
          lineno=127,
          tokens=169,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CreateButtons',
          body='uttonStyleEnum.Small,\n'
               '                originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_CENTER_AND_VERTICAL_CENTER,\n'
               '                text: MyTexts.Get(MyCommonTexts.Cancel), '
               'onButtonClick: OnCancel);\n'
               '\n'
               '            var xs = 0.85f * DialogSize.X;\n'
               '            var y = 0.5f * (DialogSize.Y - 0.15f);\n'
               '            loadButton.Position = new Vector2(-0.39f * xs, '
               'y);\n'
               '            mergeButton.Position = new Vector2(-0.16f * xs, '
               'y);\n'
               '            renameButton.Position = new Vector2(0.06f * xs, '
               'y);\n'
               '            deleteButton.Position = new Vector2(0.24f * xs, '
               'y);\n'
               '            cancelButton.Position = new Vector2(0.42f * xs, '
               'y);\n'
               '\n'
               '            loadB'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=71,
          lineno=139,
          tokens=102,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CreateButtons',
          body='utton.SetToolTip("Loads the selected toolbar replacing the '
               'current one");\n'
               '            mergeButton.SetToolTip("Merges the selected '
               'toolbar into the current one");\n'
               '            renameButton.SetToolTip("Renames the selected '
               'toolbar save file");\n'
               '            deleteButton.SetToolTip("Deletes the selected '
               'toolbar save file");\n'
               '            '
               'cancelButton.SetToolTip(MyTexts.GetString(MySpaceTexts.ToolTipOptionsSpace_Cancel));\n'
               '\n'
               '            Controls.Add(loadButton);\n'
               '            Controls.Add(mergeButton);\n'
               '            Controls.Add(renameButton);\n'
               '            Controls.Add(deleteButton);\n'
               '            Controls.Add(cancelButton);\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=72,
          lineno=152,
          tokens=66,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='ListFiles',
          body='private void ListFiles()\n'
               '        {\n'
               '            foreach (var path in '
               'Directory.EnumerateFiles(dirPath))\n'
               '            {\n'
               '                if (!path.EndsWith(".xml"))\n'
               '                    continue;\n'
               '\n'
               '                AddRowForFile(path);\n'
               '            }\n'
               '\n'
               '            if (TryFindListItem(defaultName, out var index))\n'
               '                toolbarTable.SelectedRowIndex = index;\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=73,
          lineno=166,
          tokens=125,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='AddRowForFile',
          body='private void AddRowForFile(string path)\n'
               '        {\n'
               '            var json = ReadJson(path);\n'
               '            CountUsedSlots(json);\n'
               '\n'
               '            var fileName = Path.GetFileName(path);\n'
               '            var name = fileName.Substring(0, fileName.Length - '
               '4);\n'
               '\n'
               '            var row = new MyGuiControlTable.Row(path);\n'
               '            row.AddCell(new MyGuiControlTable.Cell(name));\n'
               '            for (var i = 0; i < 9; i++)\n'
               '                row.AddCell(new '
               'MyGuiControlTable.Cell(usedSlotCounts[i] > 0 ? '
               '$"{usedSlotCounts[i]}" : "-"));\n'
               '            toolbarTable.Add(row);\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=74,
          lineno=181,
          tokens=99,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='JsonData',
          body='private static JsonData ReadJson(string xmlPath)\n'
               '        {\n'
               '            var jsonPath = XmlToJsonPath(xmlPath);\n'
               '\n'
               '            if (!File.Exists(jsonPath))\n'
               '                return null;\n'
               '\n'
               '            try\n'
               '            {\n'
               '                var jsonText = File.ReadAllText(jsonPath);\n'
               '                return JsonMapper.ToObject(jsonText);\n'
               '            }\n'
               '            catch (JsonException e)\n'
               '            {\n'
               '                MyLog.Default.Warning($"ToolbarManager: Failed '
               'to load JSON toolbar file \\"{jsonPath}\\" ({e})");\n'
               '                return null;\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=75,
          lineno=181,
          tokens=99,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='ReadJson',
          body='private static JsonData ReadJson(string xmlPath)\n'
               '        {\n'
               '            var jsonPath = XmlToJsonPath(xmlPath);\n'
               '\n'
               '            if (!File.Exists(jsonPath))\n'
               '                return null;\n'
               '\n'
               '            try\n'
               '            {\n'
               '                var jsonText = File.ReadAllText(jsonPath);\n'
               '                return JsonMapper.ToObject(jsonText);\n'
               '            }\n'
               '            catch (JsonException e)\n'
               '            {\n'
               '                MyLog.Default.Warning($"ToolbarManager: Failed '
               'to load JSON toolbar file \\"{jsonPath}\\" ({e})");\n'
               '                return null;\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=76,
          lineno=200,
          tokens=33,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='XmlToJsonPath',
          body='private static string XmlToJsonPath(string xmlPath)\n'
               '        {\n'
               '            return xmlPath.Substring(0, xmlPath.Length - 4) + '
               '".json";\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=77,
          lineno=205,
          tokens=158,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CountUsedSlots',
          body='private void CountUsedSlots(JsonData json)\n'
               '        {\n'
               '            for (var i = 0; i < 9; i++)\n'
               '                usedSlotCounts[i] = 0;\n'
               '\n'
               '            try\n'
               '            {\n'
               '                var slots = json["Slots"];\n'
               '                if (slots == null)\n'
               '                    return;\n'
               '\n'
               '                var slotCount = slots.Count;\n'
               '                for (var i = 0; i < slotCount; i++)\n'
               '                {\n'
               '                    var page = i / 9;\n'
               '                    if (page > 8)\n'
               '                        break;\n'
               '                    if (!(bool)slots[i]["IsEmpty"])\n'
               '                        usedSlotCounts[page]++;\n'
               '                }\n'
               '            }\n'
               '            catch (SystemException e)\n'
               '            {\n'
               '                MyLog.Default.Warning($"ToolbarManager: Failed '
               'to count free slots ({e})");\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=78,
          lineno=232,
          tokens=27,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnItemDoubleClicked',
          body='private void OnItemDoubleClicked(MyGuiControlTable table, '
               'MyGuiControlTable.EventArgs args)\n'
               '        {\n'
               '            ReturnLoad();\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=79,
          lineno=237,
          tokens=31,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CallResultCallback',
          body='private void CallResultCallback(string text, bool merge)\n'
               '        {\n'
               '            if (text == null)\n'
               '                return;\n'
               '\n'
               '            callBack(text, merge);\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=80,
          lineno=245,
          tokens=23,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='ReturnLoad',
          body='private void ReturnLoad()\n'
               '        {\n'
               '            CallResultCallback(SelectedName, false);\n'
               '            CloseScreen();\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=81,
          lineno=251,
          tokens=23,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='ReturnMerge',
          body='private void ReturnMerge()\n'
               '        {\n'
               '            CallResultCallback(SelectedName, true);\n'
               '            CloseScreen();\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=82,
          lineno=259,
          tokens=14,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnLoad',
          body='private void OnLoad(MyGuiControlButton button) => '
               'ReturnLoad();'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=83,
          lineno=260,
          tokens=14,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnMerge',
          body='private void OnMerge(MyGuiControlButton button) => '
               'ReturnMerge();'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=84,
          lineno=261,
          tokens=14,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnCancel',
          body='private void OnCancel(MyGuiControlButton button) => '
               'CloseScreen();'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=85,
          lineno=263,
          tokens=63,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnRename',
          body='private void OnRename(MyGuiControlButton _)\n'
               '        {\n'
               '            var oldName = SelectedName;\n'
               '            if (oldName == "")\n'
               '                return;\n'
               '\n'
               '            MyGuiSandbox.AddScreen(new NameDialog(newName => '
               'OnNewNameSpecified(oldName, newName), "Rename saved toolbar", '
               'oldName));\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=86,
          lineno=272,
          tokens=158,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnNewNameSpecified',
          body='private void OnNewNameSpecified(string oldName, string '
               'newName)\n'
               '        {\n'
               '            newName = PathExt.SanitizeFileName(newName);\n'
               '\n'
               '            var newPath = Path.Combine(dirPath, '
               '$"{newName}.xml");\n'
               '            if (File.Exists(newPath))\n'
               '            {\n'
               '                MyGuiSandbox.AddScreen(\n'
               '                    MyGuiSandbox.CreateMessageBox(buttonType: '
               'MyMessageBoxButtonsType.YES_NO,\n'
               '                        messageText: new StringBuilder($"Are '
               'you sure to overwrite this saved '
               'toolbar?\\r\\n\\r\\n{newName}"),\n'
               '                        messageCaption: new '
               'StringBuilder("Confirmation"),\n'
               '                        callback: result => '
               'OnOverwriteForSure(result, oldName, newName)));\n'
               '            }\n'
               '            else\n'
               '            {\n'
               '                '
               'OnOverwriteForSure(MyGuiScreenMessageBox.ResultEnum.YES, '
               'oldName, newName);\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=87,
          lineno=291,
          tokens=242,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnOverwriteForSure',
          body='private void '
               'OnOverwriteForSure(MyGuiScreenMessageBox.ResultEnum result, '
               'string oldName, string newName)\n'
               '        {\n'
               '            if (result != '
               'MyGuiScreenMessageBox.ResultEnum.YES)\n'
               '                return;\n'
               '\n'
               '            var oldPath = Path.Combine(dirPath, '
               '$"{oldName}.xml");\n'
               '            var newPath = Path.Combine(dirPath, '
               '$"{newName}.xml");\n'
               '\n'
               '            var oldJsonPath = XmlToJsonPath(oldPath);\n'
               '            var newJsonPath = XmlToJsonPath(newPath);\n'
               '\n'
               '            if (File.Exists(newPath))\n'
               '                File.Delete(newPath);\n'
               '\n'
               '            if (File.Exists(newJsonPath))\n'
               '                File.Delete(newJsonPath);\n'
               '\n'
               '            if (File.Exists(oldPath))\n'
               '                File.Move(oldPath, newPath);\n'
               '\n'
               '            if (File.Exists(oldJsonPath))\n'
               '                File.Move(oldJsonPath, newJsonPath);\n'
               '\n'
               '            if (TryFindListItem(newName, out var '
               'overwrittenItemIndex))\n'
               '                '
               'toolbarTable.Remove(toolbarTable.GetRow(overwrittenItemIndex));\n'
               '\n'
               '            if (TryFindListItem(oldName, out var '
               'renamedItemIndex))\n'
               '            {\n'
               '                var sb = '
               'toolbarTable.GetRow(renamedItemIndex).GetCell(0).Text;\n'
               '                sb.Clear();\n'
               '                sb.Append(newName);\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=88,
          lineno=325,
          tokens=100,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnDelete',
          body='private void OnDelete(MyGuiControlButton _)\n'
               '        {\n'
               '            var name = SelectedName;\n'
               '            if (name == "")\n'
               '                return;\n'
               '\n'
               '            MyGuiSandbox.AddScreen(\n'
               '                MyGuiSandbox.CreateMessageBox(buttonType: '
               'MyMessageBoxButtonsType.YES_NO,\n'
               '                    messageText: new StringBuilder($"Are you '
               'sure to delete this saved toolbar?\\r\\n\\r\\n{name}"),\n'
               '                    messageCaption: new '
               'StringBuilder("Confirmation"),\n'
               '                    callback: result => '
               'OnDeleteForSure(result, name)));\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=89,
          lineno=338,
          tokens=107,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnDeleteForSure',
          body='private void OnDeleteForSure(MyGuiScreenMessageBox.ResultEnum '
               'result, string name)\n'
               '        {\n'
               '            if (result != '
               'MyGuiScreenMessageBox.ResultEnum.YES)\n'
               '                return;\n'
               '\n'
               '            var path = Path.Combine(dirPath, $"{name}.xml");\n'
               '            var jsonPath = XmlToJsonPath(path);\n'
               '\n'
               '            if (File.Exists(path))\n'
               '                File.Delete(path);\n'
               '\n'
               '            if (File.Exists(jsonPath))\n'
               '                File.Delete(jsonPath);\n'
               '\n'
               '            if (TryFindListItem(name, out var index))\n'
               '                '
               'toolbarTable.Remove(toolbarTable.GetRow(index));\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=90,
          lineno=356,
          tokens=77,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='TryFindListItem',
          body='private bool TryFindListItem(string name, out int index)\n'
               '        {\n'
               '            var count = toolbarTable.RowsCount;\n'
               '            for (index = 0; index < count; index++)\n'
               '            {\n'
               '                if '
               '(toolbarTable.GetRow(index).GetCell(0).Text.ToString() == '
               'name)\n'
               '                    return true;\n'
               '            }\n'
               '\n'
               '            index = -1;\n'
               '            return false;\n'
               '        }'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=91,
          lineno=369,
          tokens=12,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='GetFriendlyName',
          body='public override string GetFriendlyName() => "ListDialog";'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=92,
          lineno=21,
          tokens=6,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='MyGuiControlTable',
          body='MyGuiControlTable toolbarTable'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=93,
          lineno=22,
          tokens=29,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='MyGuiControlButton',
          body='MyGuiControlButton loadButtonMyGuiControlButton '
               'mergeButtonMyGuiControlButton cancelButtonMyGuiControlButton '
               'renameButtonMyGuiControlButton deleteButton'),
 Fragment(document_cs='4c18978cb4ca5e16031a68042e38fc63698d0bf547c28fbeb8bcb41402043e94',
          id=94,
          lineno=1,
          tokens=486,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: ListDialog\n'
               '  Methods: AddRowForFile CallResultCallback CellTextComparison '
               'CountUsedSlots CreateButtons CreateListBox GetFriendlyName '
               'JsonData ListDialog ListFiles OnCancel OnDelete '
               'OnDeleteForSure OnItemDoubleClicked OnLoad OnMerge '
               'OnNewNameSpecified OnOverwriteForSure OnRename ReadJson '
               'RecreateControls ReturnLoad ReturnMerge TextComparison '
               'TryFindListItem XmlToJsonPath\n'
               '  Variables: MyGuiControlButton MyGuiControlTable\n'
               '  Usages: Action Add AddCaption AddCell AddRowForFile '
               'AddScreen Append CallResultCallback CanBeHidden CanHideOthers '
               'Cancel Cell CellTextComparison Clear CloseButtonEnabled '
               'CloseScreen Color ColumnsCount Combine CompareTo Config '
               'Controls Count CountUsedSlots CreateButtons CreateListBox '
               'CreateMessageBox Default Delete DialogSize Directory EndsWith '
               'EnumerateFiles EventArgs Exists Extensions File GUI Game Get '
               'GetCell GetFileName GetRow GetString Graphics Gui '
               'HORISONTAL_CENTER_AND_VERTICAL_CENTER '
               'HORISONTAL_CENTER_AND_VERTICAL_TOP IO ItemDoubleClicked '
               'JsonData JsonException JsonMapper Length ListFiles LitJson '
               'Localization Move MyCommonTexts MyGuiConstants '
               'MyGuiControlButton MyGuiControlButtonStyleEnum '
               'MyGuiControlTable MyGuiDrawAlignEnum MyGuiSandbox '
               'MyGuiScreenDebugBase MyGuiScreenMessageBox MyLog '
               'MyMessageBoxButtonsType MySandboxGame MySpaceTexts MyTexts '
               'NameDialog OnCancel OnDelete OnDeleteForSure '
               'OnItemDoubleClicked OnLoad OnMerge OnNewNameSpecified '
               'OnOverwriteForSure OnRename One OriginAlign Path PathExt '
               'Position ReadAllText ReadJson RecreateControls Remove '
               'ResultEnum ReturnLoad ReturnMerge Row RowsCount '
               'SCREEN_BACKGROUND_COLOR Sandbox SanitizeFileName SelectedName '
               'SelectedRow SelectedRowIndex SetColumnComparison SetColumnName '
               'SetCustomColumnWidths SetToolTip Size Small SortByColumn '
               'StringBuilder Substring System SystemException Text '
               'TextComparison ToObject ToString ToVector4 '
               'ToolTipOptionsSpace_Cancel ToolbarManager TryFindListItem '
               'UIBkOpacity Utils VRage VRageMath Vector2 VisibleRowsCount '
               'Warning White X XmlToJsonPath Y YES YES_NO _ args button '
               'buttonType callBack callback cancelButton caption constructor '
               'count defaultName deleteButton dirPath e fileName i index json '
               'jsonPath jsonText loadButton m_onEnterCallback m_size merge '
               'mergeButton messageCaption messageText name newJsonPath '
               'newName newPath oldJsonPath oldName oldPath onButtonClick '
               'originAlign overwrittenItemIndex page path q renameButton '
               'renamedItemIndex result row sb slotCount slots table text '
               'toolbarTable usedSlotCounts visualStyle w x xmlPath xs y\n'),
 Fragment(document_cs='597e9cc6f3ac19b8c9f10945998533e8640c51b524f64ff772aceb1fa298a984',
          id=95,
          lineno=14,
          tokens=242,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='MyGuiScreenGamePlayPatch',
          body='[HarmonyPatch(typeof(MyGuiScreenGamePlay))]\n'
               '    [SuppressMessage("ReSharper", "UnusedMember.Global")]\n'
               '    // ReSharper disable once UnusedType.Global\n'
               '    public static class MyGuiScreenGamePlayPatch\n'
               '    {\n'
               '        private static readonly List<MyKeys> PressedKeys = new '
               'List<MyKeys>();\n'
               '\n'
               '        private static readonly StringBuilder MatchingKeys = '
               'new StringBuilder();\n'
               '        // private static readonly ListDialog ListDialog = new '
               'ListDialog();\n'
               '\n'
               '        [HarmonyPrefix]\n'
               '        '
               '[HarmonyPatch(nameof(MyGuiScreenGamePlay.HandleUnhandledInput))]\n'
               '        public static bool HandleUnhandledInputPrefix()\n'
               '        {\n'
               '            if (MyGuiScreenGamePlay.ActiveGameplayScreen != '
               'null || !(MySession.Static.ControlledEntity is MyCharacter))\n'
               '                return true;\n'
               '\n'
               '            /* Disabled due to Issue #12: Conflicting keys '
               'Ctrl+Shift+C, Ctrl+Shift+X and Ctrl+Shift+B\n'
               '            if (myInput.IsAnyShiftKeyPressed() && '
               'myInput.IsAnyCtrlKeyPressed())\n'
               '            {\n'
               '                GetPressedKeys();\n'
               '                if (MatchingKeys.Length != 0)\n'
               '                {\n'
               '                    OpenCubeBuilder(MatchingKeys.ToString());\n'
               '                    return false;\n'
               '                }\n'
               '            }\n'
               '            */\n'
               '            \n'
               '            var myInput = MyInput.Static;\n'),
 Fragment(document_cs='597e9cc6f3ac19b8c9f10945998533e8640c51b524f64ff772aceb1fa298a984',
          id=96,
          lineno=44,
          tokens=212,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='MyGuiScreenGamePlayPatch',
          body='            if (myInput.IsNewKeyPressed(MyKeys.OemPipe))\n'
               '            {\n'
               '                OpenCubeBuilder("");\n'
               '                return false;\n'
               '            }\n'
               '\n'
               '            return true;\n'
               '        }\n'
               '\n'
               '        private static void OpenCubeBuilder(string '
               'searchText)\n'
               '        {\n'
               '            if '
               '(!(MyGuiSandbox.CreateScreen(typeof(CustomToolbarConfigScreen), '
               '0, null, null) is CustomToolbarConfigScreen dialog))\n'
               '                return;\n'
               '\n'
               '            MyGuiScreenGamePlay.ActiveGameplayScreen = '
               'dialog;\n'
               '            MyGuiSandbox.AddScreen(dialog);\n'
               '\n'
               '            dialog.SetSearchText(searchText);\n'
               '        }\n'
               '\n'
               '        private static void GetPressedKeys()\n'
               '        {\n'
               '            MatchingKeys.Clear();\n'
               '\n'
               '            var myInput = MyInput.Static;\n'
               '            myInput.GetPressedKeys(PressedKeys);\n'
               '            foreach (var key in PressedKeys)\n'
               '            {\n'
               '                var name = myInput.GetKeyName(key);\n'
               '                if (name.Length != 1)\n'
               '                    continue;\n'
               '\n'
               '                var c = name[0];\n'
               "                if (c >= 'A' && c <= 'Z')\n"
               '                    MatchingKeys.Append(c);\n'
               '            }\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='597e9cc6f3ac19b8c9f10945998533e8640c51b524f64ff772aceb1fa298a984',
          id=97,
          lineno=24,
          tokens=186,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='HandleUnhandledInputPrefix',
          body='[HarmonyPrefix]\n'
               '        '
               '[HarmonyPatch(nameof(MyGuiScreenGamePlay.HandleUnhandledInput))]\n'
               '        public static bool HandleUnhandledInputPrefix()\n'
               '        {\n'
               '            if (MyGuiScreenGamePlay.ActiveGameplayScreen != '
               'null || !(MySession.Static.ControlledEntity is MyCharacter))\n'
               '                return true;\n'
               '\n'
               '            /* Disabled due to Issue #12: Conflicting keys '
               'Ctrl+Shift+C, Ctrl+Shift+X and Ctrl+Shift+B\n'
               '            if (myInput.IsAnyShiftKeyPressed() && '
               'myInput.IsAnyCtrlKeyPressed())\n'
               '            {\n'
               '                GetPressedKeys();\n'
               '                if (MatchingKeys.Length != 0)\n'
               '                {\n'
               '                    OpenCubeBuilder(MatchingKeys.ToString());\n'
               '                    return false;\n'
               '                }\n'
               '            }\n'
               '            */\n'
               '            \n'
               '            var myInput = MyInput.Static;\n'
               '            if (myInput.IsNewKeyPressed(MyKeys.OemPipe))\n'
               '            {\n'
               '                OpenCubeBuilder("");\n'
               '                return false;\n'
               '            }\n'
               '\n'
               '            return true;\n'
               '        }'),
 Fragment(document_cs='597e9cc6f3ac19b8c9f10945998533e8640c51b524f64ff772aceb1fa298a984',
          id=98,
          lineno=53,
          tokens=76,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OpenCubeBuilder',
          body='private static void OpenCubeBuilder(string searchText)\n'
               '        {\n'
               '            if '
               '(!(MyGuiSandbox.CreateScreen(typeof(CustomToolbarConfigScreen), '
               '0, null, null) is CustomToolbarConfigScreen dialog))\n'
               '                return;\n'
               '\n'
               '            MyGuiScreenGamePlay.ActiveGameplayScreen = '
               'dialog;\n'
               '            MyGuiSandbox.AddScreen(dialog);\n'
               '\n'
               '            dialog.SetSearchText(searchText);\n'
               '        }'),
 Fragment(document_cs='597e9cc6f3ac19b8c9f10945998533e8640c51b524f64ff772aceb1fa298a984',
          id=99,
          lineno=64,
          tokens=99,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='GetPressedKeys',
          body='private static void GetPressedKeys()\n'
               '        {\n'
               '            MatchingKeys.Clear();\n'
               '\n'
               '            var myInput = MyInput.Static;\n'
               '            myInput.GetPressedKeys(PressedKeys);\n'
               '            foreach (var key in PressedKeys)\n'
               '            {\n'
               '                var name = myInput.GetKeyName(key);\n'
               '                if (name.Length != 1)\n'
               '                    continue;\n'
               '\n'
               '                var c = name[0];\n'
               "                if (c >= 'A' && c <= 'Z')\n"
               '                    MatchingKeys.Append(c);\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='597e9cc6f3ac19b8c9f10945998533e8640c51b524f64ff772aceb1fa298a984',
          id=100,
          lineno=21,
          tokens=7,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='StringBuilder',
          body='StringBuilder MatchingKeys = new StringBuilder()'),
 Fragment(document_cs='597e9cc6f3ac19b8c9f10945998533e8640c51b524f64ff772aceb1fa298a984',
          id=101,
          lineno=1,
          tokens=135,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: MyGuiScreenGamePlayPatch\n'
               '  Methods: GetPressedKeys HandleUnhandledInputPrefix '
               'OpenCubeBuilder\n'
               '  Variables: StringBuilder\n'
               '  Usages: ActiveGameplayScreen AddScreen Append Character '
               'Clear CodeAnalysis Collections ControlledEntity CreateScreen '
               'CustomToolbarConfigScreen Diagnostics Entities GUI Game '
               'Generic GetKeyName GetPressedKeys Graphics Gui '
               'HandleUnhandledInput HarmonyLib HarmonyPatch HarmonyPrefix '
               'Input IsNewKeyPressed Length List MatchingKeys MyCharacter '
               'MyGuiSandbox MyGuiScreenGamePlay MyInput MyKeys MySession '
               'OemPipe OpenCubeBuilder Patches PressedKeys Sandbox '
               'SetSearchText Static StringBuilder SuppressMessage System Text '
               'ToolbarManager VRage World c dialog key myInput name nameof '
               'searchText\n'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=102,
          lineno=15,
          tokens=162,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='NameDialog',
          body='public class NameDialog : MyGuiScreenDebugBase\n'
               '    {\n'
               '        private MyGuiControlTextbox nameBox;\n'
               '        private MyGuiControlButton okButton;\n'
               '        private MyGuiControlButton cancelButton;\n'
               '\n'
               '        private readonly Action<string> callBack;\n'
               '        private readonly string caption;\n'
               '        private readonly string defaultName;\n'
               '        private readonly int maxLength;\n'
               '\n'
               '        public NameDialog(\n'
               '            Action<string> callBack,\n'
               '            string caption,\n'
               '            string defaultName,\n'
               '            int maxLength = 40)\n'
               '            : base(new Vector2(0.5f, 0.5f), new Vector2(0.5f, '
               '0.28f), MyGuiConstants.SCREEN_BACKGROUND_COLOR * '
               'MySandboxGame.Config.UIBkOpacity, true)\n'
               '        {\n'
               '            this.callBack = callBack;\n'
               '            this.caption = caption;\n'
               '      '),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=103,
          lineno=35,
          tokens=174,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='NameDialog',
          body='      this.defaultName = defaultName;\n'
               '            this.maxLength = maxLength;\n'
               '\n'
               '            RecreateControls(true);\n'
               '\n'
               '            CanBeHidden = true;\n'
               '            CanHideOthers = true;\n'
               '            CloseButtonEnabled = true;\n'
               '\n'
               '            m_onEnterCallback = ReturnOk;\n'
               '        }\n'
               '\n'
               '        private Vector2 DialogSize => m_size ?? Vector2.One;\n'
               '\n'
               '        public override void RecreateControls(bool '
               'constructor)\n'
               '        {\n'
               '            base.RecreateControls(constructor);\n'
               '\n'
               '            AddCaption(caption, Color.White.ToVector4(), new '
               'Vector2(0.0f, 0.003f));\n'
               '\n'
               '            var controlSeparatorList1 = new '
               'MyGuiControlSeparatorList();\n'
               '            controlSeparatorList1.AddHorizontal(new '
               'Vector2(-0.39f * DialogSize.X, -0.5f * DialogSize.Y + 0.075f), '
               'DialogSize.X * 0.78f);\n'
               '           '),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=104,
          lineno=57,
          tokens=187,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='NameDialog',
          body=' Controls.Add(controlSeparatorList1);\n'
               '\n'
               '            var controlSeparatorList2 = new '
               'MyGuiControlSeparatorList();\n'
               '            controlSeparatorList2.AddHorizontal(new '
               'Vector2(-0.39f * DialogSize.X, +0.5f * DialogSize.Y - 0.123f), '
               'DialogSize.X * 0.78f);\n'
               '            Controls.Add(controlSeparatorList2);\n'
               '\n'
               '            nameBox = new MyGuiControlTextbox(new '
               'Vector2(0.0f, -0.027f), maxLength: maxLength)\n'
               '            {\n'
               '                Text = defaultName,\n'
               '                Size = new Vector2(0.385f, 1f)\n'
               '            };\n'
               '            nameBox.SelectAll();\n'
               '            Controls.Add(nameBox);\n'
               '\n'
               '            okButton = new MyGuiControlButton(originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_RIGHT_AND_VERTICAL_CENTER, text: '
               'MyTexts.Get(MyCommonTexts.Ok), onButtonClick: OnOk);\n'
               '            canc'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=105,
          lineno=72,
          tokens=196,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='NameDialog',
          body='elButton = new MyGuiControlButton(originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_LEFT_AND_VERTICAL_CENTER, text: '
               'MyTexts.Get(MyCommonTexts.Cancel), onButtonClick: OnCancel);\n'
               '\n'
               '            var okPosition = new Vector2(0.001f, 0.5f * '
               'DialogSize.Y - 0.071f);\n'
               '            var halfDistance = new Vector2(0.018f, 0.0f);\n'
               '\n'
               '            okButton.Position = okPosition - halfDistance;\n'
               '            cancelButton.Position = okPosition + '
               'halfDistance;\n'
               '\n'
               '            '
               'okButton.SetToolTip(MyTexts.GetString(MySpaceTexts.ToolTipNewsletter_Ok));\n'
               '            '
               'cancelButton.SetToolTip(MyTexts.GetString(MySpaceTexts.ToolTipOptionsSpace_Cancel));\n'
               '\n'
               '            Controls.Add(okButton);\n'
               '            Controls.Add(cancelButton);\n'
               '        }\n'
               '\n'
               '        private void CallResultCallback(string text)\n'
               '        {\n'
               '            if (text == null)\n'
               '                return;\n'
               '\n'
               '            callBack(text);\n'
               '        }\n'
               '\n'
               '        private void ReturnOk()\n'
               '        {\n'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=106,
          lineno=97,
          tokens=74,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='NameDialog',
          body='            if (nameBox.GetTextLength() <= 0)\n'
               '                return;\n'
               '\n'
               '            CallResultCallback(nameBox.Text);\n'
               '            CloseScreen();\n'
               '        }\n'
               '\n'
               '        private void OnOk(MyGuiControlButton button) => '
               'ReturnOk();\n'
               '        private void OnCancel(MyGuiControlButton button) => '
               'CloseScreen();\n'
               '\n'
               '        public override string GetFriendlyName() => '
               '"NameDialog";\n'
               '    }'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=107,
          lineno=26,
          tokens=146,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='NameDialog',
          body='public NameDialog(\n'
               '            Action<string> callBack,\n'
               '            string caption,\n'
               '            string defaultName,\n'
               '            int maxLength = 40)\n'
               '            : base(new Vector2(0.5f, 0.5f), new Vector2(0.5f, '
               '0.28f), MyGuiConstants.SCREEN_BACKGROUND_COLOR * '
               'MySandboxGame.Config.UIBkOpacity, true)\n'
               '        {\n'
               '            this.callBack = callBack;\n'
               '            this.caption = caption;\n'
               '            this.defaultName = defaultName;\n'
               '            this.maxLength = maxLength;\n'
               '\n'
               '            RecreateControls(true);\n'
               '\n'
               '            CanBeHidden = true;\n'
               '            CanHideOthers = true;\n'
               '            CloseButtonEnabled = true;\n'
               '\n'
               '            m_onEnterCallback = ReturnOk;\n'
               '        }'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=108,
          lineno=49,
          tokens=238,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='RecreateControls',
          body='public override void RecreateControls(bool constructor)\n'
               '        {\n'
               '            base.RecreateControls(constructor);\n'
               '\n'
               '            AddCaption(caption, Color.White.ToVector4(), new '
               'Vector2(0.0f, 0.003f));\n'
               '\n'
               '            var controlSeparatorList1 = new '
               'MyGuiControlSeparatorList();\n'
               '            controlSeparatorList1.AddHorizontal(new '
               'Vector2(-0.39f * DialogSize.X, -0.5f * DialogSize.Y + 0.075f), '
               'DialogSize.X * 0.78f);\n'
               '            Controls.Add(controlSeparatorList1);\n'
               '\n'
               '            var controlSeparatorList2 = new '
               'MyGuiControlSeparatorList();\n'
               '            controlSeparatorList2.AddHorizontal(new '
               'Vector2(-0.39f * DialogSize.X, +0.5f * DialogSize.Y - 0.123f), '
               'DialogSize.X * 0.78f);\n'
               '            Controls.Add(controlSeparatorList2);\n'
               '\n'
               '            nameBox = new MyGuiControlTextbox(new '
               'Vector2(0.0f, -0.027f), maxLength: maxLength)\n'
               '            {\n'
               '                Text = defaultName,\n'
               '                Size = new Vector2(0.385f, 1f)\n'
               '            };\n'
               '            name'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=109,
          lineno=68,
          tokens=215,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='RecreateControls',
          body='Box.SelectAll();\n'
               '            Controls.Add(nameBox);\n'
               '\n'
               '            okButton = new MyGuiControlButton(originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_RIGHT_AND_VERTICAL_CENTER, text: '
               'MyTexts.Get(MyCommonTexts.Ok), onButtonClick: OnOk);\n'
               '            cancelButton = new MyGuiControlButton(originAlign: '
               'MyGuiDrawAlignEnum.HORISONTAL_LEFT_AND_VERTICAL_CENTER, text: '
               'MyTexts.Get(MyCommonTexts.Cancel), onButtonClick: OnCancel);\n'
               '\n'
               '            var okPosition = new Vector2(0.001f, 0.5f * '
               'DialogSize.Y - 0.071f);\n'
               '            var halfDistance = new Vector2(0.018f, 0.0f);\n'
               '\n'
               '            okButton.Position = okPosition - halfDistance;\n'
               '            cancelButton.Position = okPosition + '
               'halfDistance;\n'
               '\n'
               '            '
               'okButton.SetToolTip(MyTexts.GetString(MySpaceTexts.ToolTipNewsletter_Ok));\n'
               '            '
               'cancelButton.SetToolTip(MyTexts.GetString(MySpaceTexts.ToolTipOptionsSpace_Cancel));\n'
               '\n'
               '            Controls.Add(okButton);\n'
               '            Controls.Add(cancelButton);\n'
               '        }'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=110,
          lineno=87,
          tokens=26,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CallResultCallback',
          body='private void CallResultCallback(string text)\n'
               '        {\n'
               '            if (text == null)\n'
               '                return;\n'
               '\n'
               '            callBack(text);\n'
               '        }'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=111,
          lineno=95,
          tokens=36,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='ReturnOk',
          body='private void ReturnOk()\n'
               '        {\n'
               '            if (nameBox.GetTextLength() <= 0)\n'
               '                return;\n'
               '\n'
               '            CallResultCallback(nameBox.Text);\n'
               '            CloseScreen();\n'
               '        }'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=112,
          lineno=104,
          tokens=14,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnOk',
          body='private void OnOk(MyGuiControlButton button) => ReturnOk();'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=113,
          lineno=105,
          tokens=14,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnCancel',
          body='private void OnCancel(MyGuiControlButton button) => '
               'CloseScreen();'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=114,
          lineno=107,
          tokens=12,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='GetFriendlyName',
          body='public override string GetFriendlyName() => "NameDialog";'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=115,
          lineno=17,
          tokens=6,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='MyGuiControlTextbox',
          body='MyGuiControlTextbox nameBox'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=116,
          lineno=18,
          tokens=11,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='MyGuiControlButton',
          body='MyGuiControlButton okButtonMyGuiControlButton cancelButton'),
 Fragment(document_cs='5bf5ce482ae97e8b154fd7ecd0429df820f3d3398cdb64d6ec2bee2e43174126',
          id=117,
          lineno=1,
          tokens=222,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: NameDialog\n'
               '  Methods: CallResultCallback GetFriendlyName NameDialog '
               'OnCancel OnOk RecreateControls ReturnOk\n'
               '  Variables: MyGuiControlButton MyGuiControlTextbox\n'
               '  Usages: Action Add AddCaption AddHorizontal '
               'CallResultCallback CanBeHidden CanHideOthers Cancel '
               'CloseButtonEnabled CloseScreen Color Config Controls '
               'DialogSize GUI Game Get GetString GetTextLength Graphics Gui '
               'HORISONTAL_LEFT_AND_VERTICAL_CENTER '
               'HORISONTAL_RIGHT_AND_VERTICAL_CENTER Localization '
               'MyCommonTexts MyGuiConstants MyGuiControlButton '
               'MyGuiControlSeparatorList MyGuiControlTextbox '
               'MyGuiDrawAlignEnum MyGuiScreenDebugBase MySandboxGame '
               'MySpaceTexts MyTexts Ok OnCancel OnOk One Position '
               'RecreateControls ReturnOk SCREEN_BACKGROUND_COLOR Sandbox '
               'SelectAll SetToolTip Size System Text ToVector4 '
               'ToolTipNewsletter_Ok ToolTipOptionsSpace_Cancel ToolbarManager '
               'UIBkOpacity Utils VRage VRageMath Vector2 White X Y button '
               'callBack cancelButton caption constructor '
               'controlSeparatorList1 controlSeparatorList2 defaultName '
               'halfDistance m_onEnterCallback m_size maxLength nameBox '
               'okButton okPosition onButtonClick originAlign text\n'),
 Fragment(document_cs='644588ef3fda4e1edfac1ad01235b686219c9db6142067de4471ec3df08b1505',
          id=118,
          lineno=1,
          tokens=218,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\ufeff\n'
               'Microsoft Visual Studio Solution File, Format Version 12.00\n'
               'Project("{FAE04EC0-301F-11D3-BF4B-00C04F79EFBC}") = '
               '"ToolbarManager", "ToolbarManager\\ToolbarManager.csproj", '
               '"{E79C2AFE-FC1F-4A5A-AB40-0AFED1E30570}"\n'
               'EndProject\n'
               'Global\n'
               '\tGlobalSection(SolutionConfigurationPlatforms) = preSolution\n'
               '\t\tDebug|Any CPU = Debug|Any CPU\n'
               '\t\tRelease|Any CPU = Release|Any CPU\n'
               '\tEndGlobalSection\n'
               '\tGlobalSection(ProjectConfigurationPlatforms) = postSolution\n'
               '\t\t{E79C2AFE-FC1F-4A5A-AB40-0AFED1E30570}.Debug|Any '
               'CPU.ActiveCfg = Debug|Any CPU\n'
               '\t\t{E79C2AFE-FC1F-4A5A-AB40-0AFED1E30570}.Debug|Any '
               'CPU.Build.0 = Debug|Any CPU\n'),
 Fragment(document_cs='644588ef3fda4e1edfac1ad01235b686219c9db6142067de4471ec3df08b1505',
          id=119,
          lineno=13,
          tokens=90,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\t\t{E79C2AFE-FC1F-4A5A-AB40-0AFED1E30570}.Release|Any '
               'CPU.ActiveCfg = Release|Any CPU\n'
               '\t\t{E79C2AFE-FC1F-4A5A-AB40-0AFED1E30570}.Release|Any '
               'CPU.Build.0 = Release|Any CPU\n'
               '\tEndGlobalSection\n'
               'EndGlobal\n'),
 Fragment(document_cs='644588ef3fda4e1edfac1ad01235b686219c9db6142067de4471ec3df08b1505',
          id=120,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='857a761cfd03bb91723e35b9c9817791cb67019d4ce6c8f9e70f99f195a63d7d',
          id=121,
          lineno=10,
          tokens=93,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Plugin',
          body='public class Plugin : IPlugin\n'
               '    {\n'
               '        private static bool initialized;\n'
               '        private static Storage storage;\n'
               '\n'
               '        public void Dispose()\n'
               '        {\n'
               '        }\n'
               '\n'
               '        public void Init(object gameInstance)\n'
               '        {\n'
               '            var harmony = new Harmony("ToolbarManager");\n'
               '            '
               'harmony.PatchAll(Assembly.GetExecutingAssembly());\n'
               '        }\n'
               '\n'
               '        public void Update()\n'
               '        {\n'
               '            if (initialized)\n'
               '                return;\n'
               '\n'
               '            storage = new Storage();\n'
               '\n'
               '            initialized = true;\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='857a761cfd03bb91723e35b9c9817791cb67019d4ce6c8f9e70f99f195a63d7d',
          id=122,
          lineno=15,
          tokens=8,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Dispose',
          body='public void Dispose()\n        {\n        }'),
 Fragment(document_cs='857a761cfd03bb91723e35b9c9817791cb67019d4ce6c8f9e70f99f195a63d7d',
          id=123,
          lineno=19,
          tokens=32,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Init',
          body='public void Init(object gameInstance)\n'
               '        {\n'
               '            var harmony = new Harmony("ToolbarManager");\n'
               '            '
               'harmony.PatchAll(Assembly.GetExecutingAssembly());\n'
               '        }'),
 Fragment(document_cs='857a761cfd03bb91723e35b9c9817791cb67019d4ce6c8f9e70f99f195a63d7d',
          id=124,
          lineno=25,
          tokens=27,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Update',
          body='public void Update()\n'
               '        {\n'
               '            if (initialized)\n'
               '                return;\n'
               '\n'
               '            storage = new Storage();\n'
               '\n'
               '            initialized = true;\n'
               '        }'),
 Fragment(document_cs='857a761cfd03bb91723e35b9c9817791cb67019d4ce6c8f9e70f99f195a63d7d',
          id=125,
          lineno=6,
          tokens=119,
          depth=0,
          parent_id=None,
          category='namespace',
          summary=False,
          name='ToolbarManager',
          body='namespace ToolbarManager\n'
               '{\n'
               '    // ReSharper disable NotAccessedField.Local\n'
               '    // ReSharper disable once UnusedType.Global\n'
               '    public class Plugin : IPlugin\n'
               '    {\n'
               '        private static bool initialized;\n'
               '        private static Storage storage;\n'
               '\n'
               '        public void Dispose()\n'
               '        {\n'
               '        }\n'
               '\n'
               '        public void Init(object gameInstance)\n'
               '        {\n'
               '            var harmony = new Harmony("ToolbarManager");\n'
               '            '
               'harmony.PatchAll(Assembly.GetExecutingAssembly());\n'
               '        }\n'
               '\n'
               '        public void Update()\n'
               '        {\n'
               '            if (initialized)\n'
               '                return;\n'
               '\n'
               '            storage = new Storage();\n'
               '\n'
               '            initialized = true;\n'
               '        }\n'
               '    }\n'
               '}'),
 Fragment(document_cs='857a761cfd03bb91723e35b9c9817791cb67019d4ce6c8f9e70f99f195a63d7d',
          id=126,
          lineno=13,
          tokens=2,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='Storage',
          body='Storage storage'),
 Fragment(document_cs='857a761cfd03bb91723e35b9c9817791cb67019d4ce6c8f9e70f99f195a63d7d',
          id=127,
          lineno=1,
          tokens=54,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Namespaces: ToolbarManager\n'
               '  Classes: Plugin\n'
               '  Methods: Dispose Init Update\n'
               '  Variables: Storage\n'
               '  Usages: Assembly GetExecutingAssembly Harmony HarmonyLib '
               'IPlugin Logic PatchAll Plugins Reflection Storage System '
               'ToolbarManager VRage gameInstance harmony initialized '
               'storage\n'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=128,
          lineno=15,
          tokens=236,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Storage',
          body='public class Storage\n'
               '    {\n'
               '        // MyFileSystem.UserDataPath ~= '
               'C:\\Users\\%USERNAME%\\AppData\\Roaming\\SpaceEngineers\n'
               '        private static string UserDataDir => '
               'Path.Combine(MyFileSystem.UserDataPath, "ToolbarManager");\n'
               '\n'
               '        private readonly Dictionary<string, string> '
               'latestNames = new Dictionary<string, string>();\n'
               '\n'
               '        public Storage()\n'
               '        {\n'
               '            MyGuiScreenToolbarConfigBasePatch.OnLoadToolbar += '
               'OnLoadToolbar;\n'
               '            MyGuiScreenToolbarConfigBasePatch.OnSaveToolbar += '
               'OnSaveToolbar;\n'
               '\n'
               '            MyLog.Default.Info($"ToolbarManager: UserDataDir = '
               '\\"{UserDataDir}\\"");\n'
               '        }\n'
               '\n'
               '        private static string FormatPath(MyToolbar '
               'currentToolbar, string name)\n'
               '        {\n'
               '            var dir = FormatDir(currentToolbar);\n'
               '            var sanitizedName = '
               'PathExt.SanitizeFileName(name);\n'
               '            return Path.Combine(dir, $"{sanitizedName}.xml");\n'
               '        }\n'
               '\n'
               '        private static string FormatDir(MyToolbar '
               'currentToolbar)\n'
               '        {\n'
               '            var dir = Path.Combine(UserDataDir, '
               'currentToolbar.ToolbarType.ToString());\n'
               '            Directory.CreateDirectory(dir);\n'
               '            return dir;\n'
               '        }\n'
               '\n'
               '        private void OnSaveToolbar()\n'
               '        {\n'
               '            var currentToolbar = '
               'MyToolbarComponent.CurrentToolbar;\n'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=129,
          lineno=47,
          tokens=227,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Storage',
          body='            if (currentToolbar == null)\n'
               '                return;\n'
               '\n'
               '            var latestName = '
               'latestNames.GetValueOrDefault(currentToolbar.ToolbarType.ToString()) '
               '?? "";\n'
               '\n'
               '            MyGuiSandbox.AddScreen(new '
               'NameDialog(OnNameSpecified, "Save character toolbar", '
               'latestName));\n'
               '        }\n'
               '\n'
               '        private void OnNameSpecified(string name)\n'
               '        {\n'
               '            var currentToolbar = '
               'MyToolbarComponent.CurrentToolbar;\n'
               '            if (currentToolbar == null)\n'
               '                return;\n'
               '\n'
               '            var path = FormatPath(currentToolbar, name);\n'
               '\n'
               '            if (File.Exists(path))\n'
               '            {\n'
               '                MyGuiSandbox.AddScreen(\n'
               '                    MyGuiSandbox.CreateMessageBox(buttonType: '
               'MyMessageBoxButtonsType.YES_NO,\n'
               '                        messageText: new StringBuilder($"Are '
               'you sure to overwrite this saved '
               'toolbar?\\r\\n\\r\\n{name}"),\n'
               '                        messageCaption: new '
               'StringBuilder("Confirmation"),\n'
               '                        callback: result => '
               'OnOverwriteForSure(result, path)));\n'
               '            }\n'
               '            else\n'
               '            {\n'
               '                '
               'OnOverwriteForSure(MyGuiScreenMessageBox.ResultEnum.YES, '
               'path);\n'
               '            }\n'
               '        }\n'
               '\n'
               '        private void '
               'OnOverwriteForSure(MyGuiScreenMessageBox.ResultEnum result, '
               'string path)\n'
               '        {\n'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=130,
          lineno=79,
          tokens=175,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Storage',
          body='            if (result != '
               'MyGuiScreenMessageBox.ResultEnum.YES)\n'
               '                return;\n'
               '\n'
               '            var currentToolbar = '
               'MyToolbarComponent.CurrentToolbar;\n'
               '            if (currentToolbar == null)\n'
               '                return;\n'
               '\n'
               '            var pathWithoutExtension = path.Substring(0, '
               'path.Length - 4);\n'
               '\n'
               '            var toolbar = new Toolbar(currentToolbar);\n'
               '\n'
               '            try\n'
               '            {\n'
               '                toolbar.WriteJson( '
               '$"{pathWithoutExtension}.json");\n'
               '                toolbar.Dissociate(currentToolbar);\n'
               '                toolbar.Write(path);\n'
               '            }\n'
               '            catch (Exception e)\n'
               '            {\n'
               '                MyLog.Default.Error($"ToolbarManager: Failed '
               'to save character toolbar \\"{{name}}\\" to file '
               '\\"{{path}}\\": {e}");\n'
               '                MyGuiSandboxExt.Show("Failed to save character '
               'toolbar", "Error");\n'
               '            }\n'
               '        }\n'
               '\n'
               '        private void OnLoadToolbar()\n'
               '        {\n'
               '            var currentToolbar = '
               'MyToolbarComponent.CurrentToolbar;\n'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=131,
          lineno=106,
          tokens=155,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Storage',
          body='            if (currentToolbar == null)\n'
               '                return;\n'
               '\n'
               '            var latestName = '
               'latestNames.GetValueOrDefault(currentToolbar.ToolbarType.ToString()) '
               '?? "";\n'
               '\n'
               '            MyGuiSandbox.AddScreen(new '
               'ListDialog(OnItemSelected, "Load character toolbar", '
               'latestName, FormatDir(currentToolbar)));\n'
               '        }\n'
               '\n'
               '        private void OnItemSelected(string name, bool merge)\n'
               '        {\n'
               '            var currentToolbar = '
               'MyToolbarComponent.CurrentToolbar;\n'
               '            if (currentToolbar == null)\n'
               '                return;\n'
               '\n'
               '            latestNames[currentToolbar.ToolbarType.ToString()] '
               '= name;\n'
               '\n'
               '            var path = FormatPath(currentToolbar, name);\n'
               '\n'
               '            var toolbar = Toolbar.Read(path);\n'
               '\n'
               '            toolbar.Associate(currentToolbar);\n'
               '\n'
               '            if (merge)\n'
               '                toolbar.Merge(currentToolbar);\n'
               '            else\n'
               '                toolbar.Set(currentToolbar);\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=132,
          lineno=22,
          tokens=56,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Storage',
          body='public Storage()\n'
               '        {\n'
               '            MyGuiScreenToolbarConfigBasePatch.OnLoadToolbar += '
               'OnLoadToolbar;\n'
               '            MyGuiScreenToolbarConfigBasePatch.OnSaveToolbar += '
               'OnSaveToolbar;\n'
               '\n'
               '            MyLog.Default.Info($"ToolbarManager: UserDataDir = '
               '\\"{UserDataDir}\\"");\n'
               '        }'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=133,
          lineno=30,
          tokens=51,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='FormatPath',
          body='private static string FormatPath(MyToolbar currentToolbar, '
               'string name)\n'
               '        {\n'
               '            var dir = FormatDir(currentToolbar);\n'
               '            var sanitizedName = '
               'PathExt.SanitizeFileName(name);\n'
               '            return Path.Combine(dir, $"{sanitizedName}.xml");\n'
               '        }'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=134,
          lineno=37,
          tokens=39,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='FormatDir',
          body='private static string FormatDir(MyToolbar currentToolbar)\n'
               '        {\n'
               '            var dir = Path.Combine(UserDataDir, '
               'currentToolbar.ToolbarType.ToString());\n'
               '            Directory.CreateDirectory(dir);\n'
               '            return dir;\n'
               '        }'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=135,
          lineno=44,
          tokens=73,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnSaveToolbar',
          body='private void OnSaveToolbar()\n'
               '        {\n'
               '            var currentToolbar = '
               'MyToolbarComponent.CurrentToolbar;\n'
               '            if (currentToolbar == null)\n'
               '                return;\n'
               '\n'
               '            var latestName = '
               'latestNames.GetValueOrDefault(currentToolbar.ToolbarType.ToString()) '
               '?? "";\n'
               '\n'
               '            MyGuiSandbox.AddScreen(new '
               'NameDialog(OnNameSpecified, "Save character toolbar", '
               'latestName));\n'
               '        }'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=136,
          lineno=55,
          tokens=151,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnNameSpecified',
          body='private void OnNameSpecified(string name)\n'
               '        {\n'
               '            var currentToolbar = '
               'MyToolbarComponent.CurrentToolbar;\n'
               '            if (currentToolbar == null)\n'
               '                return;\n'
               '\n'
               '            var path = FormatPath(currentToolbar, name);\n'
               '\n'
               '            if (File.Exists(path))\n'
               '            {\n'
               '                MyGuiSandbox.AddScreen(\n'
               '                    MyGuiSandbox.CreateMessageBox(buttonType: '
               'MyMessageBoxButtonsType.YES_NO,\n'
               '                        messageText: new StringBuilder($"Are '
               'you sure to overwrite this saved '
               'toolbar?\\r\\n\\r\\n{name}"),\n'
               '                        messageCaption: new '
               'StringBuilder("Confirmation"),\n'
               '                        callback: result => '
               'OnOverwriteForSure(result, path)));\n'
               '            }\n'
               '            else\n'
               '            {\n'
               '                '
               'OnOverwriteForSure(MyGuiScreenMessageBox.ResultEnum.YES, '
               'path);\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=137,
          lineno=77,
          tokens=175,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnOverwriteForSure',
          body='private void '
               'OnOverwriteForSure(MyGuiScreenMessageBox.ResultEnum result, '
               'string path)\n'
               '        {\n'
               '            if (result != '
               'MyGuiScreenMessageBox.ResultEnum.YES)\n'
               '                return;\n'
               '\n'
               '            var currentToolbar = '
               'MyToolbarComponent.CurrentToolbar;\n'
               '            if (currentToolbar == null)\n'
               '                return;\n'
               '\n'
               '            var pathWithoutExtension = path.Substring(0, '
               'path.Length - 4);\n'
               '\n'
               '            var toolbar = new Toolbar(currentToolbar);\n'
               '\n'
               '            try\n'
               '            {\n'
               '                toolbar.WriteJson( '
               '$"{pathWithoutExtension}.json");\n'
               '                toolbar.Dissociate(currentToolbar);\n'
               '                toolbar.Write(path);\n'
               '            }\n'
               '            catch (Exception e)\n'
               '            {\n'
               '                MyLog.Default.Error($"ToolbarManager: Failed '
               'to save character toolbar \\"{{name}}\\" to file '
               '\\"{{path}}\\": {e}");\n'
               '                MyGuiSandboxExt.Show("Failed to save character '
               'toolbar", "Error");\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=138,
          lineno=103,
          tokens=76,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnLoadToolbar',
          body='private void OnLoadToolbar()\n'
               '        {\n'
               '            var currentToolbar = '
               'MyToolbarComponent.CurrentToolbar;\n'
               '            if (currentToolbar == null)\n'
               '                return;\n'
               '\n'
               '            var latestName = '
               'latestNames.GetValueOrDefault(currentToolbar.ToolbarType.ToString()) '
               '?? "";\n'
               '\n'
               '            MyGuiSandbox.AddScreen(new '
               'ListDialog(OnItemSelected, "Load character toolbar", '
               'latestName, FormatDir(currentToolbar)));\n'
               '        }'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=139,
          lineno=114,
          tokens=95,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='OnItemSelected',
          body='private void OnItemSelected(string name, bool merge)\n'
               '        {\n'
               '            var currentToolbar = '
               'MyToolbarComponent.CurrentToolbar;\n'
               '            if (currentToolbar == null)\n'
               '                return;\n'
               '\n'
               '            latestNames[currentToolbar.ToolbarType.ToString()] '
               '= name;\n'
               '\n'
               '            var path = FormatPath(currentToolbar, name);\n'
               '\n'
               '            var toolbar = Toolbar.Read(path);\n'
               '\n'
               '            toolbar.Associate(currentToolbar);\n'
               '\n'
               '            if (merge)\n'
               '                toolbar.Merge(currentToolbar);\n'
               '            else\n'
               '                toolbar.Set(currentToolbar);\n'
               '        }'),
 Fragment(document_cs='8dadd89c96cc476b12e6360fdda3edc843a5cf08c9c8402199b1fdff4e181fa5',
          id=140,
          lineno=1,
          tokens=194,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Storage\n'
               '  Methods: FormatDir FormatPath OnItemSelected OnLoadToolbar '
               'OnNameSpecified OnOverwriteForSure OnSaveToolbar Storage\n'
               '  Usages: AddScreen Associate Collections Combine '
               'CreateDirectory CreateMessageBox CurrentToolbar Default '
               'Dictionary Directory Dissociate Error Exception Exists '
               'Extensions File FileSystem FormatDir FormatPath GUI Game '
               'Generic GetValueOrDefault Graphics Gui Helpers IO Info Length '
               'ListDialog Logic Merge MyFileSystem MyGuiSandbox '
               'MyGuiSandboxExt MyGuiScreenMessageBox '
               'MyGuiScreenToolbarConfigBasePatch MyLog '
               'MyMessageBoxButtonsType MyToolbar MyToolbarComponent '
               'NameDialog OnItemSelected OnLoadToolbar OnNameSpecified '
               'OnOverwriteForSure OnSaveToolbar Patches Path PathExt Read '
               'ResultEnum Sandbox SanitizeFileName Screens Set Show '
               'StringBuilder Substring System Text ToString Toolbar '
               'ToolbarManager ToolbarType UserDataDir UserDataPath Utils '
               'VRage Write WriteJson YES YES_NO buttonType callback '
               'currentToolbar dir e latestName latestNames merge '
               'messageCaption messageText name path pathWithoutExtension '
               'result sanitizedName toolbar\n'),
 Fragment(document_cs='8faa0bd163ec3d4ab664ac961750de89fe8dae561b55fc166575ee62b7f67dde',
          id=141,
          lineno=3,
          tokens=62,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='PathExt',
          body='public static class PathExt\n'
               '    {\n'
               '        public static string SanitizeFileName(string name)\n'
               '        {\n'
               '            return name\n'
               '                .Trim()\n'
               "                .Replace(':', '.')\n"
               "                .Replace('?', '.')\n"
               "                .Replace('*', '-')\n"
               "                .Replace('/', '-')\n"
               "                .Replace('\\\\', '_');\n"
               '        }\n'
               '    }'),
 Fragment(document_cs='8faa0bd163ec3d4ab664ac961750de89fe8dae561b55fc166575ee62b7f67dde',
          id=142,
          lineno=5,
          tokens=51,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='SanitizeFileName',
          body='public static string SanitizeFileName(string name)\n'
               '        {\n'
               '            return name\n'
               '                .Trim()\n'
               "                .Replace(':', '.')\n"
               "                .Replace('?', '.')\n"
               "                .Replace('*', '-')\n"
               "                .Replace('/', '-')\n"
               "                .Replace('\\\\', '_');\n"
               '        }'),
 Fragment(document_cs='8faa0bd163ec3d4ab664ac961750de89fe8dae561b55fc166575ee62b7f67dde',
          id=143,
          lineno=1,
          tokens=24,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: PathExt\n'
               '  Methods: SanitizeFileName\n'
               '  Usages: Extensions Replace ToolbarManager Trim name\n'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=144,
          lineno=18,
          tokens=248,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Toolbar',
          body='public class Toolbar\n'
               '    {\n'
               '        private readonly MyToolbarType type;\n'
               '        private readonly List<Slot> slots = new List<Slot>();\n'
               '\n'
               '        public Toolbar(MyToolbar toolbar)\n'
               '        {\n'
               '            if (toolbar == null)\n'
               '                return;\n'
               '\n'
               '            type = toolbar.ToolbarType;\n'
               '\n'
               '            for (var index = 0; index < toolbar.ItemCount; '
               'index++)\n'
               '                slots.Add(new Slot(index, '
               'toolbar.GetItemAtIndex(index)));\n'
               '        }\n'
               '\n'
               '        private Toolbar(MyObjectBuilder_Toolbar '
               'toolbarBuilder)\n'
               '        {\n'
               '            if (toolbarBuilder == null)\n'
               '                return;\n'
               '\n'
               '            type = toolbarBuilder.ToolbarType;\n'
               '\n'
               '            for (var index = 0; index < '
               'toolbarBuilder.Slots.Count; index++)\n'
               '            {\n'
               '                slots.Add(new Slot(index, '
               'toolbarBuilder.Slots[index].Data));\n'
               '            }\n'
               '        }\n'
               '\n'
               '        public void Clear()\n'
               '        {\n'
               '            slots.Clear();\n'
               '        }\n'
               '\n'
               '        public static Toolbar Read(string path)\n'
               '        {\n'
               '            using (var stream = new StreamReader(path))\n'
               '                return Read(stream);\n'
               '        }\n'
               '\n'
               '        private static Toolbar Read(StreamReader stream)\n'
               '        {\n'
               '            '
               'MyObjectBuilderSerializer.DeserializeXML<MyObjectBuilder_Toolbar>(stream.BaseStream, '
               'out var toolbarBuilder);\n'
               '            return new Toolbar(toolbarBuilder);\n'
               '        }\n'
               '\n'
               '        public void Write(string path)\n'
               '        {\n'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=145,
          lineno=66,
          tokens=239,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Toolbar',
          body='            using (var stream = new StreamWriter(path))\n'
               '                Write(stream);\n'
               '        }\n'
               '\n'
               '        private void Write(StreamWriter stream)\n'
               '        {\n'
               '            var builder = new MyObjectBuilder_Toolbar\n'
               '            {\n'
               '                ToolbarType = type\n'
               '            };\n'
               '\n'
               '            foreach (var slot in slots)\n'
               '            {\n'
               '                builder.Slots.Add(new '
               'MyObjectBuilder_Toolbar.Slot\n'
               '                {\n'
               '                    Index = slot.Index,\n'
               '                    Data = slot.Builder\n'
               '                });\n'
               '            }\n'
               '\n'
               '            '
               'MyObjectBuilderSerializer.SerializeXML(stream.BaseStream, '
               'builder);\n'
               '        }\n'
               '\n'
               '        public void WriteJson(string path)\n'
               '        {\n'
               '            using (var stream = new StreamWriter(path))\n'
               '                WriteJson(stream);\n'
               '        }\n'
               '\n'
               '        private void WriteJson(StreamWriter stream)\n'
               '        {\n'
               '            var d = new JsonData();\n'
               '            d["ToolbarType"] = type.ToString();\n'
               '\n'
               '            var ss = new JsonData();\n'
               '            ss.SetJsonType(JsonType.Array);\n'
               '            d["Slots"] = ss;\n'
               '\n'
               '            foreach (var slot in slots)\n'
               '            {\n'
               '                var s = new JsonData();\n'
               '                s["Index"] = slot.Index;\n'
               '                s["Page"] = slot.Page;\n'
               '                s["Number"] = slot.Number;\n'
               '                s["IsEmpty"] = slot.IsEmpty;\n'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=146,
          lineno=111,
          tokens=243,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Toolbar',
          body='\n'
               '                if (slot.Builder == null)\n'
               '                {\n'
               '                    s["Type"] = "";\n'
               '                    s["Name"] = "";\n'
               '                }\n'
               '                else\n'
               '                {\n'
               '                    s["Type"] = slot.Builder.GetType().Name;\n'
               '                    switch (slot.Builder)\n'
               '                    {\n'
               '                        case '
               'MyObjectBuilder_ToolbarItemDefinition itemBuilder:\n'
               '                            s["Name"] = '
               'itemBuilder.DefinitionId.ToString();\n'
               '                            break;\n'
               '\n'
               '                        case '
               'MyObjectBuilder_ToolbarItemTerminalGroup groupBuilder:\n'
               '                            s["Name"] = '
               'groupBuilder.GroupName;\n'
               '                            break;\n'
               '\n'
               '                        case '
               'MyObjectBuilder_ToolbarItemTerminalBlock blockBuilder:\n'
               '                            if '
               '(MyEntities.TryGetEntityById(blockBuilder.BlockEntityId, out '
               'var block))\n'
               '                                s["Name"] = '
               'block.DisplayNameText;\n'
               '                            else\n'
               '                                s["Name"] = "?";\n'
               '                            break;\n'
               '\n'
               '                        default:\n'
               '                            s["Name"] = "??";\n'
               '                            break;\n'
               '                    }\n'
               '                }\n'
               '\n'
               '                ss.Add(s);\n'
               '            }\n'
               '\n'
               '            var writer = new JsonWriter\n'
               '            {\n'
               '                PrettyPrint = true,\n'
               '            };\n'
               '            d.ToJson(writer);\n'
               '            stream.Write(writer.ToString());\n'
               '        }\n'
               '\n'
               '        public void Set(MyToolbar toolbar)\n'
               '        {\n'
               '            var count = Math.Min(slots.Count, '
               'toolbar.ItemCount);\n'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=147,
          lineno=157,
          tokens=232,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Toolbar',
          body='            for (var index = 0; index < count; index++)\n'
               '                slots[index].Set(toolbar);\n'
               '        }\n'
               '\n'
               '        public void Merge(MyToolbar toolbar)\n'
               '        {\n'
               '            var count = Math.Min(slots.Count, '
               'toolbar.ItemCount);\n'
               '            for (var index = 0; index < count; index++)\n'
               '                slots[index].Merge(toolbar);\n'
               '        }\n'
               '\n'
               '        public void Dissociate(MyToolbar currentToolbar)\n'
               '        {\n'
               '            if (!(currentToolbar.Owner is MyTerminalBlock))\n'
               '                return;\n'
               '\n'
               '            var utf8 = Encoding.UTF8;\n'
               '            var sha1 = SHA1.Create();\n'
               '            foreach (var slot in slots)\n'
               '            {\n'
               '                switch (slot.Builder)\n'
               '                {\n'
               '                    case '
               'MyObjectBuilder_ToolbarItemTerminalBlock blockBuilder:\n'
               '                        if '
               '(MyEntities.TryGetEntityById(blockBuilder.BlockEntityId, out '
               'var block))\n'
               '                            blockBuilder.BlockEntityId = '
               'CalculateDisplayNameTextChecksum(utf8, sha1, block);\n'
               '                        break;\n'
               '\n'
               '                    case '
               'MyObjectBuilder_ToolbarItemTerminalGroup groupBuilder:\n'
               '                        groupBuilder.BlockEntityId = 0;\n'
               '                        break;\n'
               '                }\n'
               '            }\n'
               '        }\n'
               '\n'
               '        public void Associate(MyToolbar currentToolbar)\n'
               '        {\n'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=148,
          lineno=193,
          tokens=246,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Toolbar',
          body='            if (!(currentToolbar.Owner is MyTerminalBlock '
               'terminalBlock))\n'
               '                return;\n'
               '\n'
               '            var physicalGroup = '
               'MyCubeGridGroups.Static.Physical.GetGroup(terminalBlock.CubeGrid);\n'
               '            if (physicalGroup == null)\n'
               '                return;\n'
               '\n'
               '            var blockSlots = new Dictionary<long, '
               'List<Slot>>();\n'
               '            foreach (var slot in slots)\n'
               '            {\n'
               '                switch (slot.Builder)\n'
               '                {\n'
               '                    case '
               'MyObjectBuilder_ToolbarItemTerminalBlock blockBuilder:\n'
               '                        if '
               '(blockSlots.TryGetValue(blockBuilder.BlockEntityId, out var '
               'blockSlotList))\n'
               '                            blockSlotList.Add(slot);\n'
               '                        else\n'
               '                            '
               'blockSlots[blockBuilder.BlockEntityId] = new List<Slot> { slot '
               '};\n'
               '                        break;\n'
               '                }\n'
               '            }\n'
               '\n'
               '            var utf8 = Encoding.UTF8;\n'
               '            var sha1 = SHA1.Create();\n'
               '            foreach (var physicalNode in physicalGroup.Nodes)\n'
               '            {\n'
               '                var grid = physicalNode.NodeData;\n'
               '                foreach (var block in '
               'grid.GetFatBlocks<MyTerminalBlock>())\n'
               '                {\n'
               '                    var checksum = '
               'CalculateDisplayNameTextChecksum(utf8, sha1, block);\n'
               '                    if (blockSlots.TryGetValue(checksum, out '
               'var blockSlotList))\n'
               '                    {\n'
               '                        foreach (var slot in blockSlotList)\n'
               '                        {\n'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=149,
          lineno=226,
          tokens=150,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='Toolbar',
          body='                            if (slot.Builder is '
               'MyObjectBuilder_ToolbarItemTerminalBlock blockBuilder)\n'
               '                                blockBuilder.BlockEntityId = '
               'block.EntityId;\n'
               '                        }\n'
               '                    }\n'
               '                }\n'
               '            }\n'
               '\n'
               '            foreach (var slot in slots)\n'
               '            {\n'
               '                if (slot.Builder is '
               'MyObjectBuilder_ToolbarItemTerminalGroup groupBuilder)\n'
               '                    groupBuilder.BlockEntityId = '
               'terminalBlock.EntityId;\n'
               '            }\n'
               '        }\n'
               '\n'
               '        [MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        private static long '
               'CalculateDisplayNameTextChecksum(Encoding encoding, '
               'HashAlgorithm hashAlgorithm, MyEntity block)\n'
               '        {\n'
               '            var sha1Hash = '
               'hashAlgorithm.ComputeHash(encoding.GetBytes(block.DisplayNameText));\n'
               '            var checksum = '
               '-Math.Abs(BitConverter.ToInt64(sha1Hash, 0));\n'
               '            return checksum;\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=150,
          lineno=23,
          tokens=97,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Toolbar',
          body='public Toolbar(MyToolbar toolbar)\n'
               '        {\n'
               '            if (toolbar == null)\n'
               '                return;\n'
               '\n'
               '            type = toolbar.ToolbarType;\n'
               '\n'
               '            for (var index = 0; index < toolbar.ItemCount; '
               'index++)\n'
               '                slots.Add(new Slot(index, '
               'toolbar.GetItemAtIndex(index)));\n'
               '        }private static Toolbar Read(StreamReader stream)\n'
               '        {\n'
               '            '
               'MyObjectBuilderSerializer.DeserializeXML<MyObjectBuilder_Toolbar>(stream.BaseStream, '
               'out var toolbarBuilder);\n'
               '            return new Toolbar(toolbarBuilder);\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=151,
          lineno=34,
          tokens=71,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Toolbar',
          body='private Toolbar(MyObjectBuilder_Toolbar toolbarBuilder)\n'
               '        {\n'
               '            if (toolbarBuilder == null)\n'
               '                return;\n'
               '\n'
               '            type = toolbarBuilder.ToolbarType;\n'
               '\n'
               '            for (var index = 0; index < '
               'toolbarBuilder.Slots.Count; index++)\n'
               '            {\n'
               '                slots.Add(new Slot(index, '
               'toolbarBuilder.Slots[index].Data));\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=152,
          lineno=47,
          tokens=12,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Clear',
          body='public void Clear()\n'
               '        {\n'
               '            slots.Clear();\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=153,
          lineno=52,
          tokens=26,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Read',
          body='public static Toolbar Read(string path)\n'
               '        {\n'
               '            using (var stream = new StreamReader(path))\n'
               '                return Read(stream);\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=154,
          lineno=52,
          tokens=26,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Toolbar',
          body='public static Toolbar Read(string path)\n'
               '        {\n'
               '            using (var stream = new StreamReader(path))\n'
               '                return Read(stream);\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=155,
          lineno=58,
          tokens=41,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Read',
          body='private static Toolbar Read(StreamReader stream)\n'
               '        {\n'
               '            '
               'MyObjectBuilderSerializer.DeserializeXML<MyObjectBuilder_Toolbar>(stream.BaseStream, '
               'out var toolbarBuilder);\n'
               '            return new Toolbar(toolbarBuilder);\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=156,
          lineno=64,
          tokens=24,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Write',
          body='public void Write(string path)\n'
               '        {\n'
               '            using (var stream = new StreamWriter(path))\n'
               '                Write(stream);\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=157,
          lineno=70,
          tokens=87,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Write',
          body='private void Write(StreamWriter stream)\n'
               '        {\n'
               '            var builder = new MyObjectBuilder_Toolbar\n'
               '            {\n'
               '                ToolbarType = type\n'
               '            };\n'
               '\n'
               '            foreach (var slot in slots)\n'
               '            {\n'
               '                builder.Slots.Add(new '
               'MyObjectBuilder_Toolbar.Slot\n'
               '                {\n'
               '                    Index = slot.Index,\n'
               '                    Data = slot.Builder\n'
               '                });\n'
               '            }\n'
               '\n'
               '            '
               'MyObjectBuilderSerializer.SerializeXML(stream.BaseStream, '
               'builder);\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=158,
          lineno=89,
          tokens=26,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='WriteJson',
          body='public void WriteJson(string path)\n'
               '        {\n'
               '            using (var stream = new StreamWriter(path))\n'
               '                WriteJson(stream);\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=159,
          lineno=95,
          tokens=224,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='WriteJson',
          body='private void WriteJson(StreamWriter stream)\n'
               '        {\n'
               '            var d = new JsonData();\n'
               '            d["ToolbarType"] = type.ToString();\n'
               '\n'
               '            var ss = new JsonData();\n'
               '            ss.SetJsonType(JsonType.Array);\n'
               '            d["Slots"] = ss;\n'
               '\n'
               '            foreach (var slot in slots)\n'
               '            {\n'
               '                var s = new JsonData();\n'
               '                s["Index"] = slot.Index;\n'
               '                s["Page"] = slot.Page;\n'
               '                s["Number"] = slot.Number;\n'
               '                s["IsEmpty"] = slot.IsEmpty;\n'
               '\n'
               '                if (slot.Builder == null)\n'
               '                {\n'
               '                    s["Type"] = "";\n'
               '                    s["Name"] = "";\n'
               '                }\n'
               '                else\n'
               '                {\n'
               '                    s["Type"] = slot.Builder.GetType().Name;\n'
               '                    switch (slot.Builder)\n'
               '                    {\n'
               '                        case '
               'MyObjectBuilder_ToolbarItemDefinition itemBuilder:\n'
               '                            s["Name"] = '
               'itemBuilder.DefinitionId.ToString();\n'
               '                            break;\n'
               '\n'
               '                        case '
               'MyObjectBuilder_ToolbarItemTerminalGroup groupBuilder:\n'
               '                            s["Name"] = '
               'groupBuilder.GroupName;\n'
               '                            break;\n'
               '\n'
               '                        case '
               'MyObjectBuilder_ToolbarItemTerminalBlock blockBuilder:\n'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=160,
          lineno=131,
          tokens=101,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='WriteJson',
          body='                            if '
               '(MyEntities.TryGetEntityById(blockBuilder.BlockEntityId, out '
               'var block))\n'
               '                                s["Name"] = '
               'block.DisplayNameText;\n'
               '                            else\n'
               '                                s["Name"] = "?";\n'
               '                            break;\n'
               '\n'
               '                        default:\n'
               '                            s["Name"] = "??";\n'
               '                            break;\n'
               '                    }\n'
               '                }\n'
               '\n'
               '                ss.Add(s);\n'
               '            }\n'
               '\n'
               '            var writer = new JsonWriter\n'
               '            {\n'
               '                PrettyPrint = true,\n'
               '            };\n'
               '            d.ToJson(writer);\n'
               '            stream.Write(writer.ToString());\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=161,
          lineno=154,
          tokens=47,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Set',
          body='public void Set(MyToolbar toolbar)\n'
               '        {\n'
               '            var count = Math.Min(slots.Count, '
               'toolbar.ItemCount);\n'
               '            for (var index = 0; index < count; index++)\n'
               '                slots[index].Set(toolbar);\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=162,
          lineno=161,
          tokens=47,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Merge',
          body='public void Merge(MyToolbar toolbar)\n'
               '        {\n'
               '            var count = Math.Min(slots.Count, '
               'toolbar.ItemCount);\n'
               '            for (var index = 0; index < count; index++)\n'
               '                slots[index].Merge(toolbar);\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=163,
          lineno=168,
          tokens=148,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Dissociate',
          body='public void Dissociate(MyToolbar currentToolbar)\n'
               '        {\n'
               '            if (!(currentToolbar.Owner is MyTerminalBlock))\n'
               '                return;\n'
               '\n'
               '            var utf8 = Encoding.UTF8;\n'
               '            var sha1 = SHA1.Create();\n'
               '            foreach (var slot in slots)\n'
               '            {\n'
               '                switch (slot.Builder)\n'
               '                {\n'
               '                    case '
               'MyObjectBuilder_ToolbarItemTerminalBlock blockBuilder:\n'
               '                        if '
               '(MyEntities.TryGetEntityById(blockBuilder.BlockEntityId, out '
               'var block))\n'
               '                            blockBuilder.BlockEntityId = '
               'CalculateDisplayNameTextChecksum(utf8, sha1, block);\n'
               '                        break;\n'
               '\n'
               '                    case '
               'MyObjectBuilder_ToolbarItemTerminalGroup groupBuilder:\n'
               '                        groupBuilder.BlockEntityId = 0;\n'
               '                        break;\n'
               '                }\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=164,
          lineno=191,
          tokens=227,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Associate',
          body='public void Associate(MyToolbar currentToolbar)\n'
               '        {\n'
               '            if (!(currentToolbar.Owner is MyTerminalBlock '
               'terminalBlock))\n'
               '                return;\n'
               '\n'
               '            var physicalGroup = '
               'MyCubeGridGroups.Static.Physical.GetGroup(terminalBlock.CubeGrid);\n'
               '            if (physicalGroup == null)\n'
               '                return;\n'
               '\n'
               '            var blockSlots = new Dictionary<long, '
               'List<Slot>>();\n'
               '            foreach (var slot in slots)\n'
               '            {\n'
               '                switch (slot.Builder)\n'
               '                {\n'
               '                    case '
               'MyObjectBuilder_ToolbarItemTerminalBlock blockBuilder:\n'
               '                        if '
               '(blockSlots.TryGetValue(blockBuilder.BlockEntityId, out var '
               'blockSlotList))\n'
               '                            blockSlotList.Add(slot);\n'
               '                        else\n'
               '                            '
               'blockSlots[blockBuilder.BlockEntityId] = new List<Slot> { slot '
               '};\n'
               '                        break;\n'
               '                }\n'
               '            }\n'
               '\n'
               '            var utf8 = Encoding.UTF8;\n'
               '            var sha1 = SHA1.Create();\n'
               '            foreach (var physicalNode in physicalGroup.Nodes)\n'
               '            {\n'
               '                var grid = physicalNode.NodeData;\n'
               '                foreach (var block in '
               'grid.GetFatBlocks<MyTerminalBlock>())\n'
               '                {\n'
               '                    var checksum = '
               'CalculateDisplayNameTextChecksum(utf8, sha1, block);\n'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=165,
          lineno=222,
          tokens=108,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='Associate',
          body='                    if (blockSlots.TryGetValue(checksum, out '
               'var blockSlotList))\n'
               '                    {\n'
               '                        foreach (var slot in blockSlotList)\n'
               '                        {\n'
               '                            if (slot.Builder is '
               'MyObjectBuilder_ToolbarItemTerminalBlock blockBuilder)\n'
               '                                blockBuilder.BlockEntityId = '
               'block.EntityId;\n'
               '                        }\n'
               '                    }\n'
               '                }\n'
               '            }\n'
               '\n'
               '            foreach (var slot in slots)\n'
               '            {\n'
               '                if (slot.Builder is '
               'MyObjectBuilder_ToolbarItemTerminalGroup groupBuilder)\n'
               '                    groupBuilder.BlockEntityId = '
               'terminalBlock.EntityId;\n'
               '            }\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=166,
          lineno=240,
          tokens=68,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='CalculateDisplayNameTextChecksum',
          body='[MethodImpl(MethodImplOptions.AggressiveInlining)]\n'
               '        private static long '
               'CalculateDisplayNameTextChecksum(Encoding encoding, '
               'HashAlgorithm hashAlgorithm, MyEntity block)\n'
               '        {\n'
               '            var sha1Hash = '
               'hashAlgorithm.ComputeHash(encoding.GetBytes(block.DisplayNameText));\n'
               '            var checksum = '
               '-Math.Abs(BitConverter.ToInt64(sha1Hash, 0));\n'
               '            return checksum;\n'
               '        }'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=167,
          lineno=20,
          tokens=4,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='MyToolbarType',
          body='MyToolbarType type'),
 Fragment(document_cs='94bfd66a4b0d1ca3caa49f76d1347c3810b8dce718dd78033baf9ee9166a10da',
          id=168,
          lineno=1,
          tokens=269,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Toolbar\n'
               '  Methods: Associate CalculateDisplayNameTextChecksum Clear '
               'Dissociate Merge Read Set Toolbar Write WriteJson\n'
               '  Variables: MyToolbarType\n'
               '  Usages: Abs Add AggressiveInlining Array BaseStream '
               'BitConverter BlockEntityId Builder '
               'CalculateDisplayNameTextChecksum Clear Collections Common '
               'CompilerServices ComputeHash Count Create Cryptography Cube '
               'CubeGrid Data DefinitionId DeserializeXML Dictionary '
               'DisplayNameText Encoding Entities Entity EntityId Game Generic '
               'GetBytes GetFatBlocks GetGroup GetItemAtIndex GetType '
               'GroupName HashAlgorithm Helpers IO Index IsEmpty ItemCount '
               'JsonData JsonType JsonWriter List LitJson Logic Math Merge '
               'MethodImpl MethodImplOptions Min MyCubeGridGroups MyEntities '
               'MyEntity MyObjectBuilderSerializer MyObjectBuilder_Toolbar '
               'MyObjectBuilder_ToolbarItemDefinition '
               'MyObjectBuilder_ToolbarItemTerminalBlock '
               'MyObjectBuilder_ToolbarItemTerminalGroup MyTerminalBlock '
               'MyToolbar Name NodeData Nodes Number ObjectBuilders Owner Page '
               'Physical PrettyPrint Read Runtime SHA1 Sandbox Screens '
               'Security SerializeXML Set SetJsonType Slot Slots Static '
               'StreamReader StreamWriter System Text ToInt64 ToJson ToString '
               'Toolbar ToolbarManager ToolbarType TryGetEntityById '
               'TryGetValue UTF8 VRage Write WriteJson block blockBuilder '
               'blockSlotList blockSlots builder checksum count currentToolbar '
               'd encoding grid groupBuilder hashAlgorithm index itemBuilder '
               'path physicalGroup physicalNode s sha1 sha1Hash slot slots ss '
               'stream terminalBlock toolbar toolbarBuilder type utf8 writer\n'),
 Fragment(document_cs='9e1554ffe12bc7517d277fbb77e889a175d5a083c3f8b237ae0649b7165c7c7a',
          id=169,
          lineno=1,
          tokens=22,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='.idea\n'
               'Bin64\n'
               'ToolbarManager.sln.DotSettings.user\n'
               '/packages\n'
               '**/bin\n'
               '**/obj'),
 Fragment(document_cs='9e1554ffe12bc7517d277fbb77e889a175d5a083c3f8b237ae0649b7165c7c7a',
          id=170,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='be34887b8ab241d73be16523cd3af5a805580a90cd9216fe845fba0eb4468571',
          id=171,
          lineno=1,
          tokens=230,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='<component name="ProjectRunConfigurationManager">\n'
               '  <configuration default="false" name="Space Engineers" '
               'type="RunExe" factoryName=".NET Executable">\n'
               '    <option name="EXE_PATH" value="$PROJECT_DIR$/../../Program '
               'Files '
               '(x86)/Steam/steamapps/common/SpaceEngineers/Bin64/SpaceEngineers.exe" '
               '/>\n'
               '    <option name="PROGRAM_PARAMETERS" value="-skipintro '
               '-plugin '
               '&quot;C:\\Users\\fviktor\\AppData\\Roaming\\SpaceEngineers\\Mods\\Plugin '
               'Loader\\RunPluginLoader&quot;" />\n'
               '    <option name="WORKING_DIRECTORY" '
               'value="$PROJECT_DIR$/../../Program Files '
               '(x86)/Steam/steamapps/common/SpaceEngineers/Bin64" />\n'
               '    <option name="PASS_PARENT_ENVS" value="1" />\n'
               '    <option name="USE_EXTERNAL_CONSOLE" value="0" />\n'
               '    <option name="USE_MONO" value="0" />\n'
               '    <option name="RUNTIME_ARGUMENTS" value="" />\n'
               '    <option name="RUNTIME_TYPE" value="netfw" />\n'
               '    <method v="2">\n'),
 Fragment(document_cs='be34887b8ab241d73be16523cd3af5a805580a90cd9216fe845fba0eb4468571',
          id=172,
          lineno=12,
          tokens=45,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='      <option name="Build" default="false" '
               'projectName="ToolbarManager" '
               'projectPath="file://$PROJECT_DIR$/ToolbarManager/ToolbarManager.csproj" '
               '/>\n'
               '    </method>\n'
               '  </configuration>\n'
               '</component>'),
 Fragment(document_cs='be34887b8ab241d73be16523cd3af5a805580a90cd9216fe845fba0eb4468571',
          id=173,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='c2336dddeefb94b4987ffd2321bc06eae24c27bb2c06a159d46b6e34701ad94f',
          id=174,
          lineno=8,
          tokens=93,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='MyGuiScreenToolbarConfigBaseExt',
          body='public static class MyGuiScreenToolbarConfigBaseExt\n'
               '    {\n'
               '        private static readonly MethodInfo '
               'AddGridItemToToolbarMethodInfo = '
               'AccessTools.DeclaredMethod(typeof(MyGuiScreenToolbarConfigBase), '
               '"AddGridItemToToolbar");\n'
               '        public static void AddGridItemToToolbar(this '
               'MyGuiScreenToolbarConfigBase obj, MyObjectBuilder_ToolbarItem '
               'toolbarItemBuilder) => '
               'AddGridItemToToolbarMethodInfo.Invoke(obj, new object[] { '
               'toolbarItemBuilder });\n'
               '    }'),
 Fragment(document_cs='c2336dddeefb94b4987ffd2321bc06eae24c27bb2c06a159d46b6e34701ad94f',
          id=175,
          lineno=11,
          tokens=45,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='AddGridItemToToolbar',
          body='public static void AddGridItemToToolbar(this '
               'MyGuiScreenToolbarConfigBase obj, MyObjectBuilder_ToolbarItem '
               'toolbarItemBuilder) => '
               'AddGridItemToToolbarMethodInfo.Invoke(obj, new object[] { '
               'toolbarItemBuilder });'),
 Fragment(document_cs='c2336dddeefb94b4987ffd2321bc06eae24c27bb2c06a159d46b6e34701ad94f',
          id=176,
          lineno=10,
          tokens=28,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='MethodInfo',
          body='MethodInfo AddGridItemToToolbarMethodInfo = '
               'AccessTools.DeclaredMethod(typeof(MyGuiScreenToolbarConfigBase), '
               '"AddGridItemToToolbar")'),
 Fragment(document_cs='c2336dddeefb94b4987ffd2321bc06eae24c27bb2c06a159d46b6e34701ad94f',
          id=177,
          lineno=1,
          tokens=70,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: MyGuiScreenToolbarConfigBaseExt\n'
               '  Methods: AddGridItemToToolbar\n'
               '  Variables: MethodInfo\n'
               '  Usages: AccessTools AddGridItemToToolbarMethodInfo '
               'DeclaredMethod Extensions Game Gui HarmonyLib Invoke '
               'MyGuiScreenToolbarConfigBase MyObjectBuilder_ToolbarItem '
               'Reflection Sandbox System ToolbarManager VRage obj '
               'toolbarItemBuilder\n'),
 Fragment(document_cs='c8b8202e7022975f7cf5aebf3af31aaa452c701d903571f4568e435ba0e52d6a',
          id=178,
          lineno=1,
          tokens=189,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# These are supported funding model platforms\n'
               '\n'
               'github: viktor-ferenczi\n'
               'patreon: semods\n'
               '#open_collective: # Replace with a single Open Collective '
               'username\n'
               '#ko_fi: # Replace with a single Ko-fi username\n'
               '#tidelift: # Replace with a single Tidelift '
               'platform-name/package-name e.g., npm/babel\n'
               '#community_bridge: # Replace with a single Community Bridge '
               'project-name e.g., cloud-foundry\n'
               '#liberapay: # Replace with a single Liberapay username\n'
               '#issuehunt: # Replace with a single IssueHunt username\n'
               '#otechie: # Replace with a single Otechie username\n'
               '#lfx_crowdfunding: # Replace with a single LFX Crowdfunding '
               'project-name e.g., cloud-foundry\n'
               '#custom: # Replace with up to 4 custom sponsorship URLs e.g., '
               "['link1', 'link2']\n"),
 Fragment(document_cs='c8b8202e7022975f7cf5aebf3af31aaa452c701d903571f4568e435ba0e52d6a',
          id=179,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='da9f2e4df613027c35242f353652ead43c29d4bbe458f596e9448de92a6e3b67',
          id=180,
          lineno=17,
          tokens=172,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='MyGuiScreenToolbarConfigBasePatch',
          body='[HarmonyPatch(typeof(MyGuiScreenToolbarConfigBase))]\n'
               '    public static class MyGuiScreenToolbarConfigBasePatch\n'
               '    {\n'
               '        public static event Action OnSaveToolbar;\n'
               '        public static event Action OnLoadToolbar;\n'
               '\n'
               '        [HarmonyPostfix]\n'
               '        '
               '[HarmonyPatch(nameof(MyGuiScreenToolbarConfigBase.RecreateControls))]\n'
               '        private static void '
               'RecreateControlsPostfix(MyGuiScreenToolbarConfigBase '
               '__instance)\n'
               '        {\n'
               '            var toolbarType = '
               'MyToolbarComponent.CurrentToolbar?.ToolbarType;\n'
               '            var enabled = toolbarType != null && toolbarType '
               '!= MyToolbarType.None;\n'
               '        \n'
               '            createSaveButton(__instance, enabled);\n'
               '            createLoadButton(__instance, enabled);\n'
               '        }\n'
               '\n'
               '        private static void '
               'createSaveButton(MyGuiScreenToolbarConfigBase screen, bool '
               'enabled)\n'
               '        {\n'
               '            var button = new MyGuiControlButton\n'
               '            {\n'
               '              '),
 Fragment(document_cs='da9f2e4df613027c35242f353652ead43c29d4bbe458f596e9448de92a6e3b67',
          id=181,
          lineno=38,
          tokens=180,
          depth=2,
          parent_id=None,
          category='class',
          summary=False,
          name='MyGuiScreenToolbarConfigBasePatch',
          body='  Text = "Save",\n'
               '                Name = "SaveToolbarButton",\n'
               '                VisualStyle = '
               'MyGuiControlButtonStyleEnum.Small,\n'
               '                Position = new Vector2(-0.425f, 0.41f)\n'
               '            };\n'
               '            button.ButtonClicked += _ => '
               'OnSaveToolbar?.Invoke();\n'
               '            button.Enabled = enabled;\n'
               '            screen.Elements.Add(button);\n'
               '        }\n'
               '\n'
               '        private static void '
               'createLoadButton(MyGuiScreenToolbarConfigBase screen, bool '
               'enabled)\n'
               '        {\n'
               '            var button = new MyGuiControlButton\n'
               '            {\n'
               '                Text = "Load",\n'
               '                Name = "LoadToolbarButton",\n'
               '                VisualStyle = '
               'MyGuiControlButtonStyleEnum.Small,\n'
               '                Position = new Vector2(-0.425f, 0.46f)\n'
               '            };\n'
               '            button.ButtonClicked += _ => '
               'OnLoadToolbar?.Invoke();\n'
               '            button.Enabled = enabled;\n'
               '            screen.Elements.Add(button);\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='da9f2e4df613027c35242f353652ead43c29d4bbe458f596e9448de92a6e3b67',
          id=182,
          lineno=23,
          tokens=94,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='RecreateControlsPostfix',
          body='[HarmonyPostfix]\n'
               '        '
               '[HarmonyPatch(nameof(MyGuiScreenToolbarConfigBase.RecreateControls))]\n'
               '        private static void '
               'RecreateControlsPostfix(MyGuiScreenToolbarConfigBase '
               '__instance)\n'
               '        {\n'
               '            var toolbarType = '
               'MyToolbarComponent.CurrentToolbar?.ToolbarType;\n'
               '            var enabled = toolbarType != null && toolbarType '
               '!= MyToolbarType.None;\n'
               '        \n'
               '            createSaveButton(__instance, enabled);\n'
               '            createLoadButton(__instance, enabled);\n'
               '        }'),
 Fragment(document_cs='da9f2e4df613027c35242f353652ead43c29d4bbe458f596e9448de92a6e3b67',
          id=183,
          lineno=34,
          tokens=104,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='createSaveButton',
          body='private static void '
               'createSaveButton(MyGuiScreenToolbarConfigBase screen, bool '
               'enabled)\n'
               '        {\n'
               '            var button = new MyGuiControlButton\n'
               '            {\n'
               '                Text = "Save",\n'
               '                Name = "SaveToolbarButton",\n'
               '                VisualStyle = '
               'MyGuiControlButtonStyleEnum.Small,\n'
               '                Position = new Vector2(-0.425f, 0.41f)\n'
               '            };\n'
               '            button.ButtonClicked += _ => '
               'OnSaveToolbar?.Invoke();\n'
               '            button.Enabled = enabled;\n'
               '            screen.Elements.Add(button);\n'
               '        }'),
 Fragment(document_cs='da9f2e4df613027c35242f353652ead43c29d4bbe458f596e9448de92a6e3b67',
          id=184,
          lineno=48,
          tokens=104,
          depth=4,
          parent_id=None,
          category='method',
          summary=False,
          name='createLoadButton',
          body='private static void '
               'createLoadButton(MyGuiScreenToolbarConfigBase screen, bool '
               'enabled)\n'
               '        {\n'
               '            var button = new MyGuiControlButton\n'
               '            {\n'
               '                Text = "Load",\n'
               '                Name = "LoadToolbarButton",\n'
               '                VisualStyle = '
               'MyGuiControlButtonStyleEnum.Small,\n'
               '                Position = new Vector2(-0.425f, 0.46f)\n'
               '            };\n'
               '            button.ButtonClicked += _ => '
               'OnLoadToolbar?.Invoke();\n'
               '            button.Enabled = enabled;\n'
               '            screen.Elements.Add(button);\n'
               '        }'),
 Fragment(document_cs='da9f2e4df613027c35242f353652ead43c29d4bbe458f596e9448de92a6e3b67',
          id=185,
          lineno=20,
          tokens=4,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='Action',
          body='Action OnSaveToolbar'),
 Fragment(document_cs='da9f2e4df613027c35242f353652ead43c29d4bbe458f596e9448de92a6e3b67',
          id=186,
          lineno=21,
          tokens=4,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='Action',
          body='Action OnLoadToolbar'),
 Fragment(document_cs='da9f2e4df613027c35242f353652ead43c29d4bbe458f596e9448de92a6e3b67',
          id=187,
          lineno=1,
          tokens=125,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: MyGuiScreenToolbarConfigBasePatch\n'
               '  Methods: RecreateControlsPostfix createLoadButton '
               'createSaveButton\n'
               '  Variables: Action\n'
               '  Usages: Add ButtonClicked CurrentToolbar Elements Enabled '
               'GUI Game Graphics Gui HarmonyLib HarmonyPatch HarmonyPostfix '
               'Helpers Invoke MyGuiControlButton MyGuiControlButtonStyleEnum '
               'MyGuiScreenToolbarConfigBase MyToolbarComponent MyToolbarType '
               'Name None OnLoadToolbar OnSaveToolbar Patches Position '
               'RecreateControls Sandbox Screens Small System Text '
               'ToolbarManager ToolbarType VRage VRageMath Vector2 VisualStyle '
               '_ __instance button createLoadButton createSaveButton enabled '
               'nameof screen toolbarType\n')]