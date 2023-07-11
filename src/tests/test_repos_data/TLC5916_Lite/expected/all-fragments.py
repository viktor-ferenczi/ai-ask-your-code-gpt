[Fragment(document_cs='0a5cdd3edb9cc02fb2ce40df1e29df527f20c5afb3a2f753562fc62edfcd0ec2',
          id=1,
          lineno=1,
          tokens=113,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='name=TLC5916_Lite\n'
               'version=3.0.0\n'
               'author=Daniel Nebert <dpnebert@gmail.com>\n'
               'maintainer=Daniel Nebert <dpnebert@gmail.com>\n'
               'sentence=Works in Normal Mode to turn on/off LEDs, and special '
               'mode for current gain and open circuit detection.\n'
               'paragraph=Can be used with more than one TLC5916.\n'
               'category=Device Control\n'
               'url=https://github.com/dpnebert/TLC5916_Lite\n'
               'architectures=avr\n'
               'includes=TLC5916_Lite.h\n'),
 Fragment(document_cs='0a5cdd3edb9cc02fb2ce40df1e29df527f20c5afb3a2f753562fc62edfcd0ec2',
          id=2,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=3,
          lineno=17,
          tokens=135,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::TLC5916_Lite',
          body='TLC5916_Lite::TLC5916_Lite(uint8_t sdi, uint8_t clk, uint8_t '
               'oe, uint8_t le, uint8_t sdo) {\n'
               '  SDI = sdi;\n'
               '  CLK = clk;\n'
               '  OE = oe;\n'
               '  LE = le;\n'
               '  SDO = sdo;\n'
               '  \n'
               '  pinMode(SDI, OUTPUT);\n'
               '  pinMode(CLK, OUTPUT);\n'
               '  pinMode(LE, OUTPUT);\n'
               '  pinMode(OE, OUTPUT);\n'
               '  pinMode(SDO, INPUT);\n'
               '\n'
               '  digitalWrite(SDI, LOW);\n'
               '  digitalWrite(CLK, LOW);\n'
               '  digitalWrite(LE, LOW);\n'
               '  digitalWrite(OE, HIGH);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=4,
          lineno=36,
          tokens=42,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::transmit',
          body='void TLC5916_Lite::transmit(uint8_t p, uint8_t c, bool l) {\n'
               '\tsendBits(p, 0, 0, c);\n'
               '\tif(l) pulseLatch();\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=5,
          lineno=41,
          tokens=20,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::enableOutput',
          body='void TLC5916_Lite::enableOutput() {\n'
               '\tdigitalWrite(OE, LOW);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=6,
          lineno=44,
          tokens=20,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::disableOutput',
          body='void TLC5916_Lite::disableOutput() {\n'
               '\tdigitalWrite(OE, HIGH);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=7,
          lineno=48,
          tokens=59,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::allOn',
          body='void TLC5916_Lite::allOn(uint8_t n) {\n'
               '\tfor(int i = 0; i < n - 1; i++) {\n'
               '\t\ttransmit(ALL_ON, PACKET_FULL, false);\n'
               '\t}\t\n'
               '\ttransmit(ALL_ON, PACKET_FULL, true);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=8,
          lineno=54,
          tokens=60,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::allOff',
          body='void TLC5916_Lite::allOff(uint8_t n) {\n'
               '\t\n'
               '\tfor(int i = 0; i < n - 1; i++) {\n'
               '\t\ttransmit(ALL_OFF, PACKET_FULL, false);\n'
               '\t}\t\n'
               '\ttransmit(ALL_OFF, PACKET_FULL, true);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=9,
          lineno=62,
          tokens=31,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::switchToSpecialMode',
          body='void TLC5916_Lite::switchToSpecialMode() {\n'
               '\tsendBits(DATA_NULL, STSM_OE, STSM_LE, PACKET_MODE);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=10,
          lineno=66,
          tokens=32,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::switchToNormalMode',
          body='void TLC5916_Lite::switchToNormalMode() {\t\n'
               '\tsendBits(DATA_NULL, STNM_OE, STNM_LE, PACKET_MODE);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=11,
          lineno=70,
          tokens=32,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::writeConfiguration',
          body='void TLC5916_Lite::writeConfiguration(uint8_t c) {\n'
               '\tsendBits(c, WCC_OE, WCC_LE, PACKET_FULL);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=12,
          lineno=74,
          tokens=133,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::readErrorCodeStatus',
          body='uint8_t TLC5916_Lite::readErrorCodeStatus() {\t\n'
               '\tuint8_t reading = 0;\t\n'
               '\tgenerateErrorCodeStatus();\n'
               '\tdigitalWrite(CLK, HIGH);\n'
               '\tdisableOutput();\n'
               '\tif( digitalRead(SDO) ) {\n'
               '\t\treading++;\n'
               '\t}\n'
               '\tdigitalWrite(CLK, LOW);  \n'
               '\tfor(uint8_t i = 0; i < 7; i++) {\t\t\n'
               '    reading = reading << 1;    \n'
               '    digitalWrite(CLK, HIGH);    \n'
               '\t\tif(  digitalRead(SDO) ) {\n'
               '\t\t\treading++;\n'
               '\t\t}\n'
               '\t\tdigitalWrite(CLK, LOW);\n'
               '\t}\n'
               '\treturn reading;\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=13,
          lineno=101,
          tokens=137,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::sendBits',
          body='void TLC5916_Lite::sendBits(uint8_t d, uint8_t o, uint8_t l, '
               'uint8_t c) {\n'
               '  uint8_t bitMask = 1;\n'
               '  for(uint8_t i = 0; i < c; i++) {\n'
               '  \n'
               '    digitalWrite(SDI, (d & bitMask) > 0);\n'
               '    digitalWrite(OE, (o & bitMask) > 0);\n'
               '    digitalWrite(LE, (l & bitMask) > 0);\n'
               '    bitMask = bitMask << 1;\n'
               '    digitalWrite(CLK, HIGH);\n'
               '    digitalWrite(CLK, LOW);\n'
               '  }\n'
               '  digitalWrite(SDI, LOW);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=14,
          lineno=115,
          tokens=26,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::pulseLatch',
          body='void TLC5916_Lite::pulseLatch() {\n'
               '  digitalWrite(LE, HIGH);\n'
               '  digitalWrite(LE, LOW);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=15,
          lineno=120,
          tokens=20,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::latchHigh',
          body='void TLC5916_Lite::latchHigh() {\n  digitalWrite(LE, HIGH);\n}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=16,
          lineno=123,
          tokens=20,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::latchLow',
          body='void TLC5916_Lite::latchLow() {\n  digitalWrite(LE, LOW);\n}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=17,
          lineno=126,
          tokens=28,
          depth=0,
          parent_id=None,
          category='method',
          summary=False,
          name='TLC5916_Lite::generateErrorCodeStatus',
          body='void TLC5916_Lite::generateErrorCodeStatus() {\n'
               '  sendBits(0, 1, 0, 8);\n'
               '}'),
 Fragment(document_cs='1d6303e189d6ca9516aae0c12331b790babd75ace5071dbd6bd1725a8146928a',
          id=18,
          lineno=1,
          tokens=179,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Methods: TLC5916_Lite::TLC5916_Lite TLC5916_Lite::allOff '
               'TLC5916_Lite::allOn TLC5916_Lite::disableOutput '
               'TLC5916_Lite::enableOutput '
               'TLC5916_Lite::generateErrorCodeStatus TLC5916_Lite::latchHigh '
               'TLC5916_Lite::latchLow TLC5916_Lite::pulseLatch '
               'TLC5916_Lite::readErrorCodeStatus TLC5916_Lite::sendBits '
               'TLC5916_Lite::switchToNormalMode '
               'TLC5916_Lite::switchToSpecialMode TLC5916_Lite::transmit '
               'TLC5916_Lite::writeConfiguration\n'
               '  Usages: TLC5916_Lite allOff allOn disableOutput enableOutput '
               'generateErrorCodeStatus latchHigh latchLow pulseLatch '
               'readErrorCodeStatus sendBits switchToNormalMode '
               'switchToSpecialMode transmit writeConfiguration\n'),
 Fragment(document_cs='2273e1af9c071aa2d65c3e8d7fb24a47defe11b026b588a1849889bcfaeb7d4a',
          id=19,
          lineno=26,
          tokens=2,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='setup',
          body='setup()'),
 Fragment(document_cs='2273e1af9c071aa2d65c3e8d7fb24a47defe11b026b588a1849889bcfaeb7d4a',
          id=20,
          lineno=26,
          tokens=40,
          depth=0,
          parent_id=None,
          category='function',
          summary=False,
          name='setup',
          body='void setup() {\n'
               '\n'
               '  count = 0;\n'
               '    \n'
               '  tlc.switchToNormalMode();\n'
               '  tlc.allOn(1);\n'
               '  tlc.enableOutput();\n'
               '  delay(3000);\n'
               '}'),
 Fragment(document_cs='2273e1af9c071aa2d65c3e8d7fb24a47defe11b026b588a1849889bcfaeb7d4a',
          id=21,
          lineno=36,
          tokens=24,
          depth=0,
          parent_id=None,
          category='function',
          summary=False,
          name='loop',
          body='void loop() {\n'
               '  tlc.transmit(count++, 8, true);\n'
               '  delay(500);\n'
               '}loop()'),
 Fragment(document_cs='2273e1af9c071aa2d65c3e8d7fb24a47defe11b026b588a1849889bcfaeb7d4a',
          id=22,
          lineno=16,
          tokens=6,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='SDI',
          body='#define SDI       5'),
 Fragment(document_cs='2273e1af9c071aa2d65c3e8d7fb24a47defe11b026b588a1849889bcfaeb7d4a',
          id=23,
          lineno=17,
          tokens=5,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='CLK',
          body='#define CLK       4'),
 Fragment(document_cs='2273e1af9c071aa2d65c3e8d7fb24a47defe11b026b588a1849889bcfaeb7d4a',
          id=24,
          lineno=18,
          tokens=5,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='LE',
          body='#define LE        3'),
 Fragment(document_cs='2273e1af9c071aa2d65c3e8d7fb24a47defe11b026b588a1849889bcfaeb7d4a',
          id=25,
          lineno=19,
          tokens=6,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='SDO',
          body='#define SDO       9'),
 Fragment(document_cs='2273e1af9c071aa2d65c3e8d7fb24a47defe11b026b588a1849889bcfaeb7d4a',
          id=26,
          lineno=20,
          tokens=5,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='OE',
          body='#define OE        8'),
 Fragment(document_cs='2273e1af9c071aa2d65c3e8d7fb24a47defe11b026b588a1849889bcfaeb7d4a',
          id=27,
          lineno=24,
          tokens=5,
          depth=0,
          parent_id=None,
          category='variable',
          summary=False,
          name='count',
          body='uint8_t count;'),
 Fragment(document_cs='2273e1af9c071aa2d65c3e8d7fb24a47defe11b026b588a1849889bcfaeb7d4a',
          id=28,
          lineno=1,
          tokens=22,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Macros: CLK LE OE SDI SDO\n'
               '  Functions: loop setup\n'
               '  Variables: count\n'),
 Fragment(document_cs='38b0047186510690f2a7eb163e2d67129e6eb41a6cd6b65d44a4a613134ee20f',
          id=29,
          lineno=21,
          tokens=11,
          depth=0,
          parent_id=None,
          category='function',
          summary=False,
          name='setup',
          body='void setup() {\n  brightness = 255;\n}'),
 Fragment(document_cs='38b0047186510690f2a7eb163e2d67129e6eb41a6cd6b65d44a4a613134ee20f',
          id=30,
          lineno=21,
          tokens=2,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='setup',
          body='setup()'),
 Fragment(document_cs='38b0047186510690f2a7eb163e2d67129e6eb41a6cd6b65d44a4a613134ee20f',
          id=31,
          lineno=25,
          tokens=78,
          depth=0,
          parent_id=None,
          category='function',
          summary=False,
          name='loop',
          body='void loop() {\n'
               '  tlc.switchToSpecialMode();\n'
               '  tlc.writeConfiguration(brightness);\n'
               '  if(brightness == 255) {\n'
               '    brightness = 0;\n'
               '  } else {\n'
               '    brightness = 255;\n'
               '  }\n'
               '  tlc.switchToNormalMode();\n'
               '  tlc.allOn(1);\n'
               '  tlc.enableOutput();\n'
               '  delay(1000);\n'
               '}loop()'),
 Fragment(document_cs='38b0047186510690f2a7eb163e2d67129e6eb41a6cd6b65d44a4a613134ee20f',
          id=32,
          lineno=13,
          tokens=6,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='SDI',
          body='#define SDI       5'),
 Fragment(document_cs='38b0047186510690f2a7eb163e2d67129e6eb41a6cd6b65d44a4a613134ee20f',
          id=33,
          lineno=14,
          tokens=5,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='CLK',
          body='#define CLK       4'),
 Fragment(document_cs='38b0047186510690f2a7eb163e2d67129e6eb41a6cd6b65d44a4a613134ee20f',
          id=34,
          lineno=15,
          tokens=5,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='LE',
          body='#define LE        3'),
 Fragment(document_cs='38b0047186510690f2a7eb163e2d67129e6eb41a6cd6b65d44a4a613134ee20f',
          id=35,
          lineno=16,
          tokens=6,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='SDO',
          body='#define SDO       9'),
 Fragment(document_cs='38b0047186510690f2a7eb163e2d67129e6eb41a6cd6b65d44a4a613134ee20f',
          id=36,
          lineno=17,
          tokens=5,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='OE',
          body='#define OE        8'),
 Fragment(document_cs='38b0047186510690f2a7eb163e2d67129e6eb41a6cd6b65d44a4a613134ee20f',
          id=37,
          lineno=20,
          tokens=5,
          depth=0,
          parent_id=None,
          category='variable',
          summary=False,
          name='brightness',
          body='uint8_t brightness;'),
 Fragment(document_cs='38b0047186510690f2a7eb163e2d67129e6eb41a6cd6b65d44a4a613134ee20f',
          id=38,
          lineno=1,
          tokens=22,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Macros: CLK LE OE SDI SDO\n'
               '  Functions: loop setup\n'
               '  Variables: brightness\n'),
 Fragment(document_cs='4491fafd913deca663e0273f99a953ebff86034e43155e75d8e701f6bb1f8f22',
          id=39,
          lineno=21,
          tokens=17,
          depth=0,
          parent_id=None,
          category='function',
          summary=False,
          name='setup',
          body='void setup() {\n  Serial.begin(115200);\n  while(!Serial);\n}'),
 Fragment(document_cs='4491fafd913deca663e0273f99a953ebff86034e43155e75d8e701f6bb1f8f22',
          id=40,
          lineno=21,
          tokens=2,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='setup',
          body='setup()'),
 Fragment(document_cs='4491fafd913deca663e0273f99a953ebff86034e43155e75d8e701f6bb1f8f22',
          id=41,
          lineno=26,
          tokens=62,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='loop',
          body='loop()void loop() {\n'
               '  tlc.switchToSpecialMode();\n'
               '  uint8_t reading = tlc.readErrorCodeStatus();\n'
               '\n'
               '  Serial.println(reading);\n'
               '\n'
               '  tlc.switchToNormalMode();    \n'
               '  tlc.enableOutput();\n'
               '  tlc.allOn(1);\n'
               '  \n'
               '  delay(10);\n'
               '}'),
 Fragment(document_cs='4491fafd913deca663e0273f99a953ebff86034e43155e75d8e701f6bb1f8f22',
          id=42,
          lineno=13,
          tokens=6,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='SDI',
          body='#define SDI       5'),
 Fragment(document_cs='4491fafd913deca663e0273f99a953ebff86034e43155e75d8e701f6bb1f8f22',
          id=43,
          lineno=14,
          tokens=5,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='CLK',
          body='#define CLK       4'),
 Fragment(document_cs='4491fafd913deca663e0273f99a953ebff86034e43155e75d8e701f6bb1f8f22',
          id=44,
          lineno=15,
          tokens=5,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='LE',
          body='#define LE        3'),
 Fragment(document_cs='4491fafd913deca663e0273f99a953ebff86034e43155e75d8e701f6bb1f8f22',
          id=45,
          lineno=16,
          tokens=6,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='SDO',
          body='#define SDO       9'),
 Fragment(document_cs='4491fafd913deca663e0273f99a953ebff86034e43155e75d8e701f6bb1f8f22',
          id=46,
          lineno=17,
          tokens=5,
          depth=0,
          parent_id=None,
          category='macro',
          summary=False,
          name='OE',
          body='#define OE        8'),
 Fragment(document_cs='4491fafd913deca663e0273f99a953ebff86034e43155e75d8e701f6bb1f8f22',
          id=47,
          lineno=1,
          tokens=17,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Macros: CLK LE OE SDI SDO\n  Functions: loop setup\n'),
 Fragment(document_cs='6febd96f3ffe447c306d03e10ed9217b4ffc50640146a72785f71543fd73a1e6',
          id=48,
          lineno=1,
          tokens=68,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='TLC5916_Lite\tKEYWORD1\n'
               'transmit\tKEYWORD2\n'
               'enableOutput\tKEYWORD3\n'
               'disableOutput\tKEYWORD4\n'
               'allOn\tKEYWORD5\n'
               'allOff\tKEYWORD6\n'
               'switchToSpecialMode\tKEYWORD7\n'
               'switchToNormalMode\tKEYWORD8\n'
               'writeConfiguration\tKEYWORD9\n'
               'readErrorCodeStatus\tKEYWORD10'),
 Fragment(document_cs='6febd96f3ffe447c306d03e10ed9217b4ffc50640146a72785f71543fd73a1e6',
          id=49,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=50,
          lineno=34,
          tokens=217,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='TLC5916_Lite',
          body='class TLC5916_Lite\n'
               '{\n'
               '  public:\n'
               '    TLC5916_Lite(uint8_t sdi, uint8_t clk, uint8_t oe, uint8_t '
               'le, uint8_t sdo);\n'
               '    void transmit(uint8_t p, uint8_t c, bool l);\n'
               '    void enableOutput();\n'
               '    void disableOutput();\n'
               '    void allOn(uint8_t n);\n'
               '    void allOff(uint8_t n);\n'
               '    \n'
               '    void switchToSpecialMode();\n'
               '    void switchToNormalMode();\n'
               '    \n'
               '    void writeConfiguration(uint8_t c);\n'
               '    uint8_t readErrorCodeStatus();\n'
               '    \n'
               '  private:\n'
               '    uint8_t readBits();\n'
               '    void sendBits(uint8_t d, uint8_t o, uint8_t l, uint8_t '
               'c);\n'
               '    void pulseLatch();\n'
               '    void latchHigh();\n'
               '    void latchLow();\n'
               '    void generateErrorCodeStatus();\n'
               '\n'
               '    uint8_t SDI;\n'
               '    uint8_t CLK;\n'
               '    uint8_t OE;\n'
               '    uint8_t LE; \n'
               '    uint8_t SDO;   \n'
               '  protected:\n'
               '    \n'
               '  \n'
               '}'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=51,
          lineno=58,
          tokens=6,
          depth=3,
          parent_id=None,
          category='field',
          summary=False,
          name='SDI',
          body='uint8_t SDI;'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=52,
          lineno=59,
          tokens=5,
          depth=3,
          parent_id=None,
          category='field',
          summary=False,
          name='CLK',
          body='uint8_t CLK;'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=53,
          lineno=60,
          tokens=5,
          depth=3,
          parent_id=None,
          category='field',
          summary=False,
          name='OE',
          body='uint8_t OE;'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=54,
          lineno=61,
          tokens=5,
          depth=3,
          parent_id=None,
          category='field',
          summary=False,
          name='LE',
          body='uint8_t LE;'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=55,
          lineno=62,
          tokens=6,
          depth=3,
          parent_id=None,
          category='field',
          summary=False,
          name='SDO',
          body='uint8_t SDO;'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=56,
          lineno=37,
          tokens=33,
          depth=4,
          parent_id=None,
          category='function',
          summary=False,
          name='TLC5916_Lite',
          body='TLC5916_Lite(uint8_t sdi, uint8_t clk, uint8_t oe, uint8_t le, '
               'uint8_t sdo)'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=57,
          lineno=12,
          tokens=8,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='TLC5916_LITE_H_',
          body='#define TLC5916_LITE_H_'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=58,
          lineno=14,
          tokens=6,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='ALL_ON',
          body='#define ALL_ON      255'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=59,
          lineno=15,
          tokens=6,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='ALL_OFF',
          body='#define ALL_OFF     0'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=60,
          lineno=17,
          tokens=8,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='STSM_OE',
          body='#define STSM_OE     29'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=61,
          lineno=18,
          tokens=7,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='STSM_LE',
          body='#define STSM_LE     8'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=62,
          lineno=20,
          tokens=8,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='STNM_OE',
          body='#define STNM_OE     29'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=63,
          lineno=21,
          tokens=7,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='STNM_LE',
          body='#define STNM_LE     0'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=64,
          lineno=23,
          tokens=8,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='WCC_OE',
          body='#define WCC_OE      255'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=65,
          lineno=24,
          tokens=7,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='WCC_LE',
          body='#define WCC_LE      128'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=66,
          lineno=25,
          tokens=8,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='WCC_FULL_BRIGHT',
          body='#define WCC_FULL_BRIGHT 255'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=67,
          lineno=27,
          tokens=6,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='DATA_NULL',
          body='#define DATA_NULL   0'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=68,
          lineno=29,
          tokens=6,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='PACKET_FULL',
          body='#define PACKET_FULL   8'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=69,
          lineno=30,
          tokens=6,
          depth=1,
          parent_id=None,
          category='macro',
          summary=False,
          name='PACKET_MODE',
          body='#define PACKET_MODE   5'),
 Fragment(document_cs='921f83947a134a1d4919069c271438089eb0728bf56b9b263fab5c48014a1cab',
          id=70,
          lineno=1,
          tokens=76,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: TLC5916_Lite\n'
               '  Macros: ALL_OFF ALL_ON DATA_NULL PACKET_FULL PACKET_MODE '
               'STNM_LE STNM_OE STSM_LE STSM_OE TLC5916_LITE_H_ '
               'WCC_FULL_BRIGHT WCC_LE WCC_OE\n'
               '  Functions: TLC5916_Lite\n'
               '  Fields: CLK LE OE SDI SDO\n'),
 Fragment(document_cs='a338b32e84315aa0de5dd9afd4bd1a9c35cf463aa29dc1071518ea02dd6cf15f',
          id=71,
          lineno=1,
          tokens=85,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# TLC5916_Lite\n'
               '<p>\n'
               '  For documentation, visit: \n'
               '  <a '
               'href="https://github.com/dpnebert/TLC5916_Lite/blob/main/extras/TCL5916%20Lite%20Arduino%20Library%20Rev%202.0.0.pdf">TCL5916 '
               'Lite Arduino Library Rev 2.0.0.pdf</a>  \n'
               '</p>\n'),
 Fragment(document_cs='a338b32e84315aa0de5dd9afd4bd1a9c35cf463aa29dc1071518ea02dd6cf15f',
          id=72,
          lineno=1,
          tokens=7,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='# TLC5916_Lite\n'),
 Fragment(document_cs='a3502544916a6f59f24b774e8af6f7731d5adaae2b6ea69c6867a9ff886f3e09',
          id=73,
          lineno=1,
          tokens=64,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='on: [push, pull_request]\n'
               'jobs:\n'
               '  lint:\n'
               '    runs-on: ubuntu-latest\n'
               '    steps:\n'
               '      - uses: actions/checkout@v2\n'
               '      - uses: arduino/arduino-lint-action@v1\n'
               '        with:\n'
               '          library-manager: update\n'
               '          compliance: strict\n'),
 Fragment(document_cs='a3502544916a6f59f24b774e8af6f7731d5adaae2b6ea69c6867a9ff886f3e09',
          id=74,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='ae162e2b23a02b1da5ad3c5c4a79541acd43839013a136203485a4d2c2cd449e',
          id=75,
          lineno=1,
          tokens=220,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='MIT License\n'
               '\n'
               'Copyright (c) 2021 dpnebert\n'
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
 Fragment(document_cs='ae162e2b23a02b1da5ad3c5c4a79541acd43839013a136203485a4d2c2cd449e',
          id=76,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='')]