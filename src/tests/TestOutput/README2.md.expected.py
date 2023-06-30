from model.fragment import Fragment

# Parser: MarkdownParser

f0 = Fragment(uuid='TEST-00',
         path='README2.md',
         lineno=1,
         depth=1,
         type='documentation',
         name='',
         text='# C++ Programming\n\n\n')

f1 = Fragment(uuid='TEST-01',
         path='README2.md',
         lineno=4,
         depth=1,
         type='documentation',
         name='',
         text='## Contents\n'
              '- [Tips](#keep-these-tips-in-mind-while-learning-programming)\n'
              '- [Computer Science Basics](#computer-science-basics)\n'
              '- [Learning Resources](#learning-resources)\n'
              '- [Problem Solving](#problem-solving)\n'
              '- [Projects Ideas](#projects-ideas)\n'
              '\n'
              '\n')

f2 = Fragment(uuid='TEST-02',
         path='README2.md',
         lineno=12,
         depth=6,
         type='documentation',
         name='',
         text='## Keep These Tips in Mind While Learning Programming\n```')

f3 = Fragment(uuid='TEST-03',
         path='README2.md',
         lineno=13,
         depth=11,
         type='documentation',
         name='',
         text='\n1. Learn and code every day, consistency is important.')

f4 = Fragment(uuid='TEST-04',
         path='README2.md',
         lineno=14,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '2. Write it down - plan your code before you start coding and understand the input to your program and '
              'the output from your code.')

f5 = Fragment(uuid='TEST-05',
         path='README2.md',
         lineno=15,
         depth=11,
         type='documentation',
         name='',
         text='\n3. Learn to debug your code - look at the code line by line to see how it works.')

f6 = Fragment(uuid='TEST-06',
         path='README2.md',
         lineno=16,
         depth=11,
         type='documentation',
         name='',
         text='\n4. Surround yourself with other people who are learning. Teach each other.')

f7 = Fragment(uuid='TEST-07',
         path='README2.md',
         lineno=17,
         depth=11,
         type='documentation',
         name='',
         text='\n5. Learn taking notes.')

f8 = Fragment(uuid='TEST-08',
         path='README2.md',
         lineno=18,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '6. Build something, anything. For example, simple calculator, or program to save and read data from TXT '
              'files.')

f9 = Fragment(uuid='TEST-09',
         path='README2.md',
         lineno=19,
         depth=11,
         type='documentation',
         name='',
         text='\n7. Focus on 1 thing! Take small steps, but every day, consistency is very important again.')

f10 = Fragment(uuid='TEST-10',
         path='README2.md',
         lineno=20,
         depth=11,
         type='documentation',
         name='',
         text='\n8. Learn to ask GOOD questions to others:')

f11 = Fragment(uuid='TEST-11',
         path='README2.md',
         lineno=21,
         depth=11,
         type='documentation',
         name='',
         text='\n  - G: Give context on what you are trying to do, clearly describing the problem.')

f12 = Fragment(uuid='TEST-12',
         path='README2.md',
         lineno=22,
         depth=11,
         type='documentation',
         name='',
         text='\n  - O: Outline the things you have already tried to fix the issue.')

f13 = Fragment(uuid='TEST-13',
         path='README2.md',
         lineno=23,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '  - O: Offer your best guess as to what the problem might be. It helps the person who is helping you '
              "not only know what you're thinking, but also know that you've thought of something yourself.")

f14 = Fragment(uuid='TEST-14',
         path='README2.md',
         lineno=24,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              "  - D: Demonstrate what's going on. Include the code, the tracing error message, and an explanation of "
              "the steps you followed that resulted in the error. That way, the person helping doesn't have to try to "
              'recreate the problem.')

f15 = Fragment(uuid='TEST-15', path='README2.md', lineno=25, depth=11, type='documentation', name='', text='\n```')

f16 = Fragment(uuid='TEST-16', path='README2.md', lineno=26, depth=11, type='documentation', name='', text='\n')

f17 = Fragment(uuid='TEST-17', path='README2.md', lineno=27, depth=11, type='documentation', name='', text='\n')

f18 = Fragment(uuid='TEST-18', path='README2.md', lineno=28, depth=11, type='documentation', name='', text='\n')

f19 = Fragment(uuid='TEST-19',
         path='README2.md',
         lineno=29,
         depth=11,
         type='documentation',
         name='',
         text='## Computer Science Basics')

f20 = Fragment(uuid='TEST-20',
         path='README2.md',
         lineno=29,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '- [Harvard CS50](https://youtube.com/playlist?list=PLhQjrBD2T383f9scHRNYJkior2VvYjpSL) - Scratch, C, '
              'Arrays, Algorithms, Memory, Data structures, Python, SQL, HTML, CSS, JavaScript, Flask')

f21 = Fragment(uuid='TEST-21',
         path='README2.md',
         lineno=30,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '- `Optional` [Crash Course Computer '
              'Science](https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo)')

f22 = Fragment(uuid='TEST-22',
         path='README2.md',
         lineno=31,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '- [Computer Science for '
              'Everyone](https://www.youtube.com/playlist?list=PLrC-HcVNfULbGKkhJSgfqvqmaFAZvfHes) ')

f23 = Fragment(uuid='TEST-23', path='README2.md', lineno=32, depth=11, type='documentation', name='', text='\n')

f24 = Fragment(uuid='TEST-24', path='README2.md', lineno=33, depth=11, type='documentation', name='', text='\n')

f25 = Fragment(uuid='TEST-25',
         path='README2.md',
         lineno=34,
         depth=11,
         type='documentation',
         name='',
         text='## Learning Resources')

f26 = Fragment(uuid='TEST-26',
         path='README2.md',
         lineno=34,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '- EN [C++ for beginners — '
              'CodeBeauty](https://www.youtube.com/playlist?list=PL43pGnjiVwgQHLPnuH9ch-LhZdwckM8Tq)')

f27 = Fragment(uuid='TEST-27',
         path='README2.md',
         lineno=35,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '- EN [C++ Programming Tutorial — thenewboston](https://www.youtube.com/playlist?list=PLAE85DE8440AA6B83)')

f28 = Fragment(uuid='TEST-28',
         path='README2.md',
         lineno=36,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '- EN [C++ by The '
              'Cherno](https://www.youtube.com/watch?v=18c3MTX0PK0&list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb)')

f29 = Fragment(uuid='TEST-29',
         path='README2.md',
         lineno=37,
         depth=11,
         type='documentation',
         name='',
         text='\n- EN [C++ by freeCodeCamp.org](https://www.youtube.com/watch?v=vLnPwxZdW4Y)')

f30 = Fragment(uuid='TEST-30',
         path='README2.md',
         lineno=38,
         depth=11,
         type='documentation',
         name='',
         text='\n- RU [C++ by Denis Markov](https://www.youtube.com/playlist?list=PLbmlzoDQrXVFC13GjpPrJxl6mzTiX65gs)')

f31 = Fragment(uuid='TEST-31',
         path='README2.md',
         lineno=39,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '- RU [C++ Уроки - Гоша '
              'Дударь](https://www.youtube.com/watch?v=qSHP98i9mDU&list=PL0lO_mIqDDFXNfqIL9PHQM7Wg_kOtDZsW)')

f32 = Fragment(uuid='TEST-32', path='README2.md', lineno=40, depth=11, type='documentation', name='', text='\n- To read:')

f33 = Fragment(uuid='TEST-33',
         path='README2.md',
         lineno=41,
         depth=11,
         type='documentation',
         name='',
         text='\n  - [cplusplus.com](https://cplusplus.com/doc/tutorial/)')

f34 = Fragment(uuid='TEST-34',
         path='README2.md',
         lineno=42,
         depth=11,
         type='documentation',
         name='',
         text='\n  - [w3schools.com](https://www.w3schools.com/cpp/default.asp) ')

f35 = Fragment(uuid='TEST-35',
         path='README2.md',
         lineno=43,
         depth=11,
         type='documentation',
         name='',
         text='\n  - [tutorialspoint.com](https://www.tutorialspoint.com/cplusplus/index.htm)')

f36 = Fragment(uuid='TEST-36',
         path='README2.md',
         lineno=44,
         depth=11,
         type='documentation',
         name='',
         text='\n  - [GeegsForGeeks.org](https://www.geeksforgeeks.org/c-plus-plus/):')

f37 = Fragment(uuid='TEST-37', path='README2.md', lineno=45, depth=11, type='documentation', name='', text='\n')

f38 = Fragment(uuid='TEST-38', path='README2.md', lineno=46, depth=11, type='documentation', name='', text='\n')

f39 = Fragment(uuid='TEST-39',
         path='README2.md',
         lineno=47,
         depth=6,
         type='documentation',
         name='',
         text='## Problem Solving\n```')

f40 = Fragment(uuid='TEST-40',
         path='README2.md',
         lineno=48,
         depth=11,
         type='documentation',
         name='',
         text='\n1. C++ Program to print "Hello, World!"')

f41 = Fragment(uuid='TEST-41',
         path='README2.md',
         lineno=49,
         depth=11,
         type='documentation',
         name='',
         text='\n2. C++ Program to Print an Integer (Entered by the User)')

f42 = Fragment(uuid='TEST-42',
         path='README2.md',
         lineno=50,
         depth=11,
         type='documentation',
         name='',
         text='\n3. C++ Program to Add Two Integers')

f43 = Fragment(uuid='TEST-43',
         path='README2.md',
         lineno=51,
         depth=11,
         type='documentation',
         name='',
         text='\n4. C++ Program to Multiply two Floating Point Numbers')

f44 = Fragment(uuid='TEST-44',
         path='README2.md',
         lineno=52,
         depth=11,
         type='documentation',
         name='',
         text='\n5. C++ Program to Find ASCII Value of a Character')

f45 = Fragment(uuid='TEST-45',
         path='README2.md',
         lineno=53,
         depth=11,
         type='documentation',
         name='',
         text='\n6. C++ Program to Compute Quotient and Remainder')

f46 = Fragment(uuid='TEST-46',
         path='README2.md',
         lineno=54,
         depth=11,
         type='documentation',
         name='',
         text='\n7. C++ Program to Find the Size of int, float, double and char')

f47 = Fragment(uuid='TEST-47',
         path='README2.md',
         lineno=55,
         depth=11,
         type='documentation',
         name='',
         text='\n8. C++ Program to Demonstrate the Working of Keyword long')

f48 = Fragment(uuid='TEST-48',
         path='README2.md',
         lineno=56,
         depth=11,
         type='documentation',
         name='',
         text='\n9. C++ Program to Swap Two Numbers')

f49 = Fragment(uuid='TEST-49',
         path='README2.md',
         lineno=57,
         depth=11,
         type='documentation',
         name='',
         text='\n10. C++ Program to Check Whether a Number is Even or Odd')

f50 = Fragment(uuid='TEST-50',
         path='README2.md',
         lineno=58,
         depth=11,
         type='documentation',
         name='',
         text='\n11. C++ Program to Check Whether a Character is Vowel or Consonant')

f51 = Fragment(uuid='TEST-51',
         path='README2.md',
         lineno=59,
         depth=11,
         type='documentation',
         name='',
         text='\n12. C++ Program to Find the Largest Number Among Three Numbers')

f52 = Fragment(uuid='TEST-52',
         path='README2.md',
         lineno=60,
         depth=11,
         type='documentation',
         name='',
         text='\n13. C++ Program to Find all Roots of a Quadratic equation')

f53 = Fragment(uuid='TEST-53',
         path='README2.md',
         lineno=61,
         depth=11,
         type='documentation',
         name='',
         text='\n14. C++ Program to Check Leap Year')

f54 = Fragment(uuid='TEST-54',
         path='README2.md',
         lineno=62,
         depth=11,
         type='documentation',
         name='',
         text='\n15. C++ Program to Check Whether a Number is Positive or Negative')

f55 = Fragment(uuid='TEST-55',
         path='README2.md',
         lineno=63,
         depth=11,
         type='documentation',
         name='',
         text='\n16. C++ Program to Check Whether a Character is an Alphabet or not')

f56 = Fragment(uuid='TEST-56',
         path='README2.md',
         lineno=64,
         depth=11,
         type='documentation',
         name='',
         text='\n17. C++ Program to Calculate the Sum of Natural Numbers')

f57 = Fragment(uuid='TEST-57',
         path='README2.md',
         lineno=65,
         depth=11,
         type='documentation',
         name='',
         text='\n18. C++ Program to Find Factorial of a Number')

f58 = Fragment(uuid='TEST-58',
         path='README2.md',
         lineno=66,
         depth=11,
         type='documentation',
         name='',
         text='\n19. C++ Program to Generate Multiplication Table')

f59 = Fragment(uuid='TEST-59',
         path='README2.md',
         lineno=67,
         depth=11,
         type='documentation',
         name='',
         text='\n20. C++ Program to Display Fibonacci Sequence')

f60 = Fragment(uuid='TEST-60',
         path='README2.md',
         lineno=68,
         depth=11,
         type='documentation',
         name='',
         text='\n21. C++ Program to Find GCD of two Numbers')

f61 = Fragment(uuid='TEST-61',
         path='README2.md',
         lineno=69,
         depth=11,
         type='documentation',
         name='',
         text='\n22. C++ Program to Find LCM of two Numbers')

f62 = Fragment(uuid='TEST-62',
         path='README2.md',
         lineno=70,
         depth=11,
         type='documentation',
         name='',
         text='\n23. C++ Program to Display Characters from A to Z Using Loop')

f63 = Fragment(uuid='TEST-63',
         path='README2.md',
         lineno=71,
         depth=11,
         type='documentation',
         name='',
         text='\n24. C++ Program to Count Number of Digits in an Integer')

f64 = Fragment(uuid='TEST-64',
         path='README2.md',
         lineno=72,
         depth=11,
         type='documentation',
         name='',
         text='\n25. C++ Program to Reverse a Number')

f65 = Fragment(uuid='TEST-65',
         path='README2.md',
         lineno=73,
         depth=11,
         type='documentation',
         name='',
         text='\n26. C++ Program to Calculate the Power of a Number')

f66 = Fragment(uuid='TEST-66',
         path='README2.md',
         lineno=74,
         depth=11,
         type='documentation',
         name='',
         text='\n27. C++ Program to Check Whether a Number is Palindrome or Not')

f67 = Fragment(uuid='TEST-67',
         path='README2.md',
         lineno=75,
         depth=11,
         type='documentation',
         name='',
         text='\n28. C++ Program to Check Whether a Number is Prime or Not')

f68 = Fragment(uuid='TEST-68',
         path='README2.md',
         lineno=76,
         depth=11,
         type='documentation',
         name='',
         text='\n29. C++ Program to Display Prime Numbers Between Two Intervals')

f69 = Fragment(uuid='TEST-69',
         path='README2.md',
         lineno=77,
         depth=11,
         type='documentation',
         name='',
         text='\n30. C++ Program to Check Armstrong Number')

f70 = Fragment(uuid='TEST-70',
         path='README2.md',
         lineno=78,
         depth=11,
         type='documentation',
         name='',
         text='\n31. C++ Program to Display Armstrong Number Between Two Intervals')

f71 = Fragment(uuid='TEST-71',
         path='README2.md',
         lineno=79,
         depth=11,
         type='documentation',
         name='',
         text='\n32. C++ Program to Display Factors of a Number')

f72 = Fragment(uuid='TEST-72',
         path='README2.md',
         lineno=80,
         depth=11,
         type='documentation',
         name='',
         text='\n33. C++ Programming Code To Create Pyramid and Structure')

f73 = Fragment(uuid='TEST-73',
         path='README2.md',
         lineno=81,
         depth=11,
         type='documentation',
         name='',
         text='\n34. C++ Program to Make a Simple Calculator Using switch...case')

f74 = Fragment(uuid='TEST-74',
         path='README2.md',
         lineno=82,
         depth=11,
         type='documentation',
         name='',
         text='\n35. C++ Program to Display Prime Numbers Between Intervals Using Function')

f75 = Fragment(uuid='TEST-75',
         path='README2.md',
         lineno=83,
         depth=11,
         type='documentation',
         name='',
         text='\n36. C++ Program to Check Prime or Armstrong Number Using User-defined Function')

f76 = Fragment(uuid='TEST-76',
         path='README2.md',
         lineno=84,
         depth=11,
         type='documentation',
         name='',
         text='\n37. C++ Program to Check Whether a Number can be Expressed as Sum of Two Prime Numbers')

f77 = Fragment(uuid='TEST-77',
         path='README2.md',
         lineno=85,
         depth=11,
         type='documentation',
         name='',
         text='\n38. C++ Program to Find the Sum of Natural Numbers using Recursion')

f78 = Fragment(uuid='TEST-78',
         path='README2.md',
         lineno=86,
         depth=11,
         type='documentation',
         name='',
         text='\n39. C++ Program to Find Factorial of a Number Using Recursion')

f79 = Fragment(uuid='TEST-79',
         path='README2.md',
         lineno=87,
         depth=11,
         type='documentation',
         name='',
         text='\n40. C++ Program to Find G.C.D Using Recursion')

f80 = Fragment(uuid='TEST-80',
         path='README2.md',
         lineno=88,
         depth=11,
         type='documentation',
         name='',
         text='\n41. C++ Program to Convert Binary Number to Decimal and vice-versa')

f81 = Fragment(uuid='TEST-81',
         path='README2.md',
         lineno=89,
         depth=11,
         type='documentation',
         name='',
         text='\n42. C++ Program to Convert Octal Number to Decimal and vice-versa')

f82 = Fragment(uuid='TEST-82',
         path='README2.md',
         lineno=90,
         depth=11,
         type='documentation',
         name='',
         text='\n43. C++ Program to Convert Binary Number to Octal and vice-versa')

f83 = Fragment(uuid='TEST-83',
         path='README2.md',
         lineno=91,
         depth=11,
         type='documentation',
         name='',
         text='\n44. C++ Program to Reverse a Sentence Using Recursion')

f84 = Fragment(uuid='TEST-84',
         path='README2.md',
         lineno=92,
         depth=11,
         type='documentation',
         name='',
         text='\n45. C++ Program to calculate the power using recursion')

f85 = Fragment(uuid='TEST-85',
         path='README2.md',
         lineno=93,
         depth=11,
         type='documentation',
         name='',
         text='\n46. C++ Program to Calculate Average Using Arrays')

f86 = Fragment(uuid='TEST-86',
         path='README2.md',
         lineno=94,
         depth=11,
         type='documentation',
         name='',
         text='\n47. C++ Program to Find Largest Element of an Array')

f87 = Fragment(uuid='TEST-87',
         path='README2.md',
         lineno=95,
         depth=11,
         type='documentation',
         name='',
         text='\n48. C++ Program to Calculate Standard Deviation')

f88 = Fragment(uuid='TEST-88',
         path='README2.md',
         lineno=96,
         depth=11,
         type='documentation',
         name='',
         text='\n49. C++ Program to Add Two Matrix Using Multi-dimensional Arrays')

f89 = Fragment(uuid='TEST-89',
         path='README2.md',
         lineno=97,
         depth=11,
         type='documentation',
         name='',
         text='\n50. C++ Program to Multiply to Matrix Using Multi-dimensional Arrays')

f90 = Fragment(uuid='TEST-90',
         path='README2.md',
         lineno=98,
         depth=11,
         type='documentation',
         name='',
         text='\n51. C++ Program to Find Transpose of a Matrix')

f91 = Fragment(uuid='TEST-91',
         path='README2.md',
         lineno=99,
         depth=11,
         type='documentation',
         name='',
         text='\n52. C++ Program to Multiply two Matrices by Passing Matrix to a Function')

f92 = Fragment(uuid='TEST-92',
         path='README2.md',
         lineno=100,
         depth=11,
         type='documentation',
         name='',
         text='\n53. C++ Program to Access Elements of an Array Using Pointer')

f93 = Fragment(uuid='TEST-93',
         path='README2.md',
         lineno=101,
         depth=11,
         type='documentation',
         name='',
         text='\n54. C++ Program Swap Numbers in Cyclic Order Using Call by Reference')

f94 = Fragment(uuid='TEST-94',
         path='README2.md',
         lineno=102,
         depth=11,
         type='documentation',
         name='',
         text='\n55. C++ Program to Find Largest Number Using Dynamic Memory Allocation')

f95 = Fragment(uuid='TEST-95',
         path='README2.md',
         lineno=103,
         depth=11,
         type='documentation',
         name='',
         text='\n56. C++ Program to Find the Frequency of Characters in a String')

f96 = Fragment(uuid='TEST-96',
         path='README2.md',
         lineno=104,
         depth=11,
         type='documentation',
         name='',
         text='\n57. C++ Program to count the number of vowels, consonants and so on')

f97 = Fragment(uuid='TEST-97',
         path='README2.md',
         lineno=105,
         depth=11,
         type='documentation',
         name='',
         text='\n58. C++ Program to Remove all Characters in a String Except Alphabet')

f98 = Fragment(uuid='TEST-98',
         path='README2.md',
         lineno=106,
         depth=11,
         type='documentation',
         name='',
         text='\n59. C++ Program to Find the Length of a String')

f99 = Fragment(uuid='TEST-99',
         path='README2.md',
         lineno=107,
         depth=11,
         type='documentation',
         name='',
         text='\n60. C++ Program to Concatenate Two Strings')

f100 = Fragment(uuid='TEST-100',
         path='README2.md',
         lineno=108,
         depth=11,
         type='documentation',
         name='',
         text='\n61. C++ Program to Copy String Without Using strcpy()')

f101 = Fragment(uuid='TEST-101',
         path='README2.md',
         lineno=109,
         depth=11,
         type='documentation',
         name='',
         text='\n62. C++ Program to Sort Elements in Lexicographical Order (Dictionary Order)')

f102 = Fragment(uuid='TEST-102',
         path='README2.md',
         lineno=110,
         depth=11,
         type='documentation',
         name='',
         text='\n63. C++ Program to Store Information(name, roll and marks) of a Student Using Structure')

f103 = Fragment(uuid='TEST-103',
         path='README2.md',
         lineno=111,
         depth=11,
         type='documentation',
         name='',
         text='\n64. C++ Program to Add Two Distances (in inch-feet) System Using Structures')

f104 = Fragment(uuid='TEST-104',
         path='README2.md',
         lineno=112,
         depth=11,
         type='documentation',
         name='',
         text='\n65. C++ Program to Add Two Complex Numbers by Passing Structure to a Function')

f105 = Fragment(uuid='TEST-105',
         path='README2.md',
         lineno=113,
         depth=11,
         type='documentation',
         name='',
         text='\n66. C++ Program to Calculate Difference Between Two Time Periods')

f106 = Fragment(uuid='TEST-106',
         path='README2.md',
         lineno=114,
         depth=11,
         type='documentation',
         name='',
         text='\n67. C++ Program to Store Information of Students Using Structure')

f107 = Fragment(uuid='TEST-107',
         path='README2.md',
         lineno=115,
         depth=11,
         type='documentation',
         name='',
         text='\n68. C++ Program to Store Information Using Structures with Dynamically Memory Allocation')

f108 = Fragment(uuid='TEST-108',
         path='README2.md',
         lineno=116,
         depth=11,
         type='documentation',
         name='',
         text='\n69. C++ Program to Write a Sentence to a File')

f109 = Fragment(uuid='TEST-109',
         path='README2.md',
         lineno=117,
         depth=11,
         type='documentation',
         name='',
         text='\n70. C++ Program to Read a Line From a File and Display it')

f110 = Fragment(uuid='TEST-110',
         path='README2.md',
         lineno=118,
         depth=11,
         type='documentation',
         name='',
         text='\n71. C++ Program to Display its own Source Code as Output')

f111 = Fragment(uuid='TEST-111',
         path='README2.md',
         lineno=119,
         depth=11,
         type='documentation',
         name='',
         text='\n72. C++ Programming Code To Create Pyramid and Pattern')

f112 = Fragment(uuid='TEST-112', path='README2.md', lineno=120, depth=11, type='documentation', name='', text='\n```')

f113 = Fragment(uuid='TEST-113', path='README2.md', lineno=121, depth=11, type='documentation', name='', text='\n')

f114 = Fragment(uuid='TEST-114', path='README2.md', lineno=122, depth=11, type='documentation', name='', text='\n')

f115 = Fragment(uuid='TEST-115',
         path='README2.md',
         lineno=123,
         depth=6,
         type='documentation',
         name='',
         text='## Projects Ideas\n```')

f116 = Fragment(uuid='TEST-116',
         path='README2.md',
         lineno=124,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '1. Banking system with all banking facilities like – deposit, withdrawal, foreign exchange to any '
              'currency, availability of loans for purchasing vehicles, apartments, houses, setting up business, '
              'education loan, management of ATMs and all other features.')

f117 = Fragment(uuid='TEST-117',
         path='README2.md',
         lineno=125,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '2. Airline flight reservation system (online booking of tickets in different flights for different '
              'destinations all over the world, cancellation of tickets, clear display of cancellation amount, refund '
              'of amount after cancellation, showing  availability of all flights, showing flights timings for all 7 '
              'days of a week, seats availability, seat selection for travelers by giving the complete layout of the '
              'seating arrangement inside the flights, food availability/non-availability inside the flights, change '
              'of travel dates and amount charged.)')

f118 = Fragment(uuid='TEST-118',
         path='README2.md',
         lineno=126,
         depth=11,
         type='documentation',
         name='',
         text='\n3. Taxi/cab sharing')

f119 = Fragment(uuid='TEST-119',
         path='README2.md',
         lineno=127,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '4. University education portal (providing all information about under-graduate, post graduate and '
              'doctoral programs offered, facilities available, location & map, fee structure in all the universities)')

f120 = Fragment(uuid='TEST-120',
         path='README2.md',
         lineno=128,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '5. Online exam management system (with total security of identifying the students during exam, '
              'monitoring the students’ activities during the exam, selection of different questions for each student, '
              'development of a large question bank containing hundreds of questions in each subject considering all '
              'courses taught at the university)')

f121 = Fragment(uuid='TEST-121',
         path='README2.md',
         lineno=129,
         depth=11,
         type='documentation',
         name='',
         text='\n6. Library management system')

f122 = Fragment(uuid='TEST-122',
         path='README2.md',
         lineno=130,
         depth=11,
         type='documentation',
         name='',
         text='\n7. E-content management system ')

f123 = Fragment(uuid='TEST-123',
         path='README2.md',
         lineno=131,
         depth=11,
         type='documentation',
         name='',
         text='\n8. Plagiarism checker & file management system')

f124 = Fragment(uuid='TEST-124',
         path='README2.md',
         lineno=132,
         depth=11,
         type='documentation',
         name='',
         text='\n9. Hotel reservation & management portal')

f125 = Fragment(uuid='TEST-125',
         path='README2.md',
         lineno=133,
         depth=11,
         type='documentation',
         name='',
         text='\n10. Restaurant management')

f126 = Fragment(uuid='TEST-126',
         path='README2.md',
         lineno=134,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '11. Healthcare consulting system (doctors with different specializations for consultation, hospitals '
              'with all facilities for treating different diseases & abroad - one stop portal for all consultations '
              'and treatments)')

f127 = Fragment(uuid='TEST-127',
         path='README2.md',
         lineno=135,
         depth=11,
         type='documentation',
         name='',
         text='\n12. Electronic health record management system with builtin security ')

f128 = Fragment(uuid='TEST-128',
         path='README2.md',
         lineno=136,
         depth=11,
         type='documentation',
         name='',
         text='\n13. Pharmacy - medical store management ')

f129 = Fragment(uuid='TEST-129',
         path='README2.md',
         lineno=137,
         depth=11,
         type='documentation',
         name='',
         text='\n14. Blood bank system')

f130 = Fragment(uuid='TEST-130',
         path='README2.md',
         lineno=138,
         depth=11,
         type='documentation',
         name='',
         text='\n15. Online shopping and delivery system (like amazon)')

f131 = Fragment(uuid='TEST-131',
         path='README2.md',
         lineno=139,
         depth=11,
         type='documentation',
         name='',
         text='\n16. Online car shopping ')

f132 = Fragment(uuid='TEST-132',
         path='README2.md',
         lineno=140,
         depth=11,
         type='documentation',
         name='',
         text='\n17. Tourism portal')

f133 = Fragment(uuid='TEST-133',
         path='README2.md',
         lineno=141,
         depth=11,
         type='documentation',
         name='',
         text='\n18. World tourism portal')

f134 = Fragment(uuid='TEST-134',
         path='README2.md',
         lineno=142,
         depth=11,
         type='documentation',
         name='',
         text='\n19. Higher education abroad portal')

f135 = Fragment(uuid='TEST-135',
         path='README2.md',
         lineno=143,
         depth=11,
         type='documentation',
         name='',
         text='\n20. Job search/recruitment portal')

f136 = Fragment(uuid='TEST-136',
         path='README2.md',
         lineno=144,
         depth=11,
         type='documentation',
         name='',
         text='\n21. Company resource management system')

f137 = Fragment(uuid='TEST-137',
         path='README2.md',
         lineno=145,
         depth=11,
         type='documentation',
         name='',
         text='\n22. Attendance monitoring system with fingerprints verification')

f138 = Fragment(uuid='TEST-138',
         path='README2.md',
         lineno=146,
         depth=11,
         type='documentation',
         name='',
         text='\n23. Face recognition - based attendance checking system')

f139 = Fragment(uuid='TEST-139',
         path='README2.md',
         lineno=147,
         depth=11,
         type='documentation',
         name='',
         text='\n24. Aircraft communication and monitoring system')

f140 = Fragment(uuid='TEST-140',
         path='README2.md',
         lineno=148,
         depth=11,
         type='documentation',
         name='',
         text='\n25. Ticket booking management system for concert ceremonies')

f141 = Fragment(uuid='TEST-141',
         path='README2.md',
         lineno=149,
         depth=11,
         type='documentation',
         name='',
         text='\n26. All store stock management (inventory control)')

f142 = Fragment(uuid='TEST-142',
         path='README2.md',
         lineno=150,
         depth=11,
         type='documentation',
         name='',
         text='\n27. Multiplayer gaming applications')

f143 = Fragment(uuid='TEST-143',
         path='README2.md',
         lineno=151,
         depth=11,
         type='documentation',
         name='',
         text='\n28. City traffic monitoring and control system')

f144 = Fragment(uuid='TEST-144',
         path='README2.md',
         lineno=152,
         depth=11,
         type='documentation',
         name='',
         text='\n29. Police traffic violation reporting & control system')

f145 = Fragment(uuid='TEST-145',
         path='README2.md',
         lineno=153,
         depth=11,
         type='documentation',
         name='',
         text='\n30. The marriage function hall booking & food/music arrangement system')

f146 = Fragment(uuid='TEST-146',
         path='README2.md',
         lineno=154,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '31. Any vehicle (car, bus, heavy vehicles for parties, functions, family picnics, long distance travel) '
              'booking portal')

f147 = Fragment(uuid='TEST-147',
         path='README2.md',
         lineno=155,
         depth=11,
         type='documentation',
         name='',
         text='\n32. Teacher assisted program writing environment for students')

f148 = Fragment(uuid='TEST-148',
         path='README2.md',
         lineno=156,
         depth=11,
         type='documentation',
         name='',
         text='\n33. Doctors reservation system for patients')

f149 = Fragment(uuid='TEST-149',
         path='README2.md',
         lineno=157,
         depth=11,
         type='documentation',
         name='',
         text='\n34. Bus reservation & tracking system')

f150 = Fragment(uuid='TEST-150',
         path='README2.md',
         lineno=158,
         depth=11,
         type='documentation',
         name='',
         text='\n35. Railway booking and train tracking system')

f151 = Fragment(uuid='TEST-151',
         path='README2.md',
         lineno=159,
         depth=11,
         type='documentation',
         name='',
         text='\n36. Warehouse management system')

f152 = Fragment(uuid='TEST-152',
         path='README2.md',
         lineno=160,
         depth=11,
         type='documentation',
         name='',
         text='\n37. Courier tracking, cargo and freight transportation')

f153 = Fragment(uuid='TEST-153',
         path='README2.md',
         lineno=161,
         depth=11,
         type='documentation',
         name='',
         text='\n38. Online code testing system')

f154 = Fragment(uuid='TEST-154',
         path='README2.md',
         lineno=162,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '39. Online quiz system (with total security of identifying the students during the quiz, monitoring the '
              'students’ activities during the quiz, selection of different quiz questions for each student, '
              'development of a large quiz question bank containing hundreds of quiz questions in each subject '
              'considering all courses taught at the university)')

f155 = Fragment(uuid='TEST-155',
         path='README2.md',
         lineno=163,
         depth=11,
         type='documentation',
         name='',
         text='\n40. Land/house/apartment rental & purchase portal')

f156 = Fragment(uuid='TEST-156',
         path='README2.md',
         lineno=164,
         depth=11,
         type='documentation',
         name='',
         text='\n41. Housecleaning, plumbing, electricity service & maintenance system')

f157 = Fragment(uuid='TEST-157',
         path='README2.md',
         lineno=165,
         depth=11,
         type='documentation',
         name='',
         text='\n42. Human organ transplantation management system')

f158 = Fragment(uuid='TEST-158',
         path='README2.md',
         lineno=166,
         depth=11,
         type='documentation',
         name='',
         text='\n43. Covid-19 tracking, testing, treatment & hospital management system')

f159 = Fragment(uuid='TEST-159',
         path='README2.md',
         lineno=167,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '44. Cryptocurrency trading portal (exchange) allowing trading of all crypto coins using security, '
              'confidentiality and authentication')

f160 = Fragment(uuid='TEST-160',
         path='README2.md',
         lineno=168,
         depth=11,
         type='documentation',
         name='',
         text='\n45. Parking management system')

f161 = Fragment(uuid='TEST-161',
         path='README2.md',
         lineno=169,
         depth=11,
         type='documentation',
         name='',
         text='\n'
              '46. Online food delivery system (linked to all restaurants in different districts in different regions '
              'in some country)')

f162 = Fragment(uuid='TEST-162', path='README2.md', lineno=170, depth=11, type='documentation', name='', text='\n```')

f163 = Fragment(uuid='TEST-163', path='README2.md', lineno=171, depth=11, type='documentation', name='', text='\n')

f164 = Fragment(uuid='TEST-164',
         path='README2.md',
         lineno=1,
         depth=0,
         type='summary',
         name='',
         text='# C++ Programming\n'
              '## Contents\n'
              '## Keep These Tips in Mind While Learning Programming\n'
              '## Computer Science Basics\n'
              '## Learning Resources\n'
              '## Problem Solving\n'
              '## Projects Ideas\n')

