[Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=1,
          lineno=7,
          tokens=225,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='GameOfLife',
          body='public class GameOfLife extends JFrame {\n'
               '\n'
               '    JPanel infoPanel;\n'
               '    static JLabel generationLabel;\n'
               '    static JLabel aliveLabel;\n'
               '    static JPanel universePanel;\n'
               '\n'
               '    static boolean paused = false;\n'
               '\n'
               '    static Universe universe = new Universe();\n'
               '    static Evolution evolution = new Evolution();\n'
               '\n'
               '    public GameOfLife() {\n'
               '\n'
               '        super("Game of Life");\n'
               '        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);\n'
               '        setSize(720, 789);\n'
               '        setLocationRelativeTo(null);\n'
               '        setLayout(null);\n'
               '        setVisible(true);\n'
               '\n'
               '        infoPanel = new JPanel();\n'
               '        infoPanel.setBounds(1, 1, 110, 40);\n'
               '        infoPanel.setLayout(new BoxLayout(infoPanel, '
               'BoxLayout.Y_AXIS));\n'
               '        '
               'infoPanel.setBorder(BorderFactory.createEtchedBorder());\n'
               '        add(infoPanel);\n'
               '\n'
               '        generationLabel = new JLabel();\n'
               '        generationLabel.setName("GenerationLabel");\n'
               '        generationLabel.setText(" Generation #0");\n'
               '        generationLabel.setBounds(0, 0, 400, 20);\n'
               '        infoPanel.add(generationLabel);\n'
               '\n'
               '        aliveLabel = new JLabel();\n'
               '        aliveLabel.setName("AliveLabel");\n'
               '        aliveLabel.setText(" Alive: " + GameO'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=2,
          lineno=42,
          tokens=220,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='GameOfLife',
          body='fLife.universe.alive);\n'
               '        aliveLabel.setBounds(0, 20, 400, 20);\n'
               '        infoPanel.add(aliveLabel);\n'
               '\n'
               '        JPanel controlPanel = new JPanel();\n'
               '        controlPanel.setBounds(111, 1, 121, 40);\n'
               '        controlPanel.setLayout(new BoxLayout(controlPanel, '
               'BoxLayout.X_AXIS));\n'
               '        '
               'controlPanel.setBorder(BorderFactory.createEtchedBorder());\n'
               '        add(controlPanel);\n'
               '\n'
               '        JToggleButton pauseButton = new JToggleButton("||");\n'
               '        pauseButton.setName("PlayToggleButton");\n'
               '        ActionListener pauseListener = new PauseListener();\n'
               '        pauseButton.addActionListener(pauseListener);\n'
               '        controlPanel.add(pauseButton);\n'
               '\n'
               '        JButton restartButton = new JButton("Restart");\n'
               '        restartButton.setName("ResetButton");\n'
               '        ActionListener restartListener = new '
               'RestartListener();\n'
               '        restartButton.addActionListener(restartListener);\n'
               '        controlPanel.add(restartButton);\n'
               '\n'
               '        universePanel = new UniversePanel();\n'
               '        add(universePanel);\n'
               '    }\n'
               '\n'
               '    public static void main(String[] args) {\n'
               '\n'
               '        new GameOfLife();\n'
               '        universe.setSize(35);\n'
               '        evolution.setGenerations(500);\n'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=3,
          lineno=73,
          tokens=33,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='GameOfLife',
          body='\n'
               '        while (true) {\n'
               '\n'
               '            if (!evolution.restart) {\n'
               '\n'
               '                universe.create();\n'
               '                evolution.evolve(universe);\n'
               '\n'
               '            }\n'
               '        }\n'
               '    }\n'
               '}'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=4,
          lineno=86,
          tokens=247,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Universe',
          body='class Universe {\n'
               '\n'
               '    int size;\n'
               '    static int genNum;\n'
               '    static int alive;\n'
               '    char[][] field;\n'
               '    Random rand;\n'
               '\n'
               '    public Universe() {}\n'
               '\n'
               '    public int getSize() {\n'
               '\n'
               '        return this.size;\n'
               '\n'
               '    }\n'
               '\n'
               '    public void setSize(int size) {\n'
               '\n'
               '        if (size > 0) {\n'
               '\n'
               '            this.size = size;\n'
               '\n'
               '        } else {\n'
               '\n'
               '            System.out.println("Size must be greater than '
               '0.");\n'
               '\n'
               '        }\n'
               '\n'
               '    }\n'
               '\n'
               '    public void create() {\n'
               '\n'
               '        this.genNum = 0;\n'
               '        this.alive = 0;\n'
               '        this.rand = new Random();\n'
               '\n'
               '        this.field = new char[size][size];\n'
               '\n'
               '        for (int i = 0; i < this.size; i++) {\n'
               '\n'
               '            for (int j = 0; j < this.size; j++) {\n'
               '\n'
               '                if (this.rand.nextBoolean()) {\n'
               '\n'
               "                    this.field[i][j] = 'O';\n"
               '                    alive++;\n'
               '\n'
               '                } else {\n'
               '\n'
               "                    this.field[i][j] = ' ';\n"
               '\n'
               '                }\n'
               '            }\n'
               '        }\n'
               '    }\n'
               '\n'
               '    public void print() {\n'
               '\n'
               '        GameOfLife.aliveLabel.setText(" Alive: " + '
               'GameOfLife.universe.alive);\n'
               '        System.out.println("Alive: " + this.alive);\n'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=5,
          lineno=146,
          tokens=70,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Universe',
          body='\n'
               '        for (int i = 0; i < this.size; i++) {\n'
               '\n'
               '            for (int j = 0; j < this.size; j++) {\n'
               '\n'
               '                System.out.print(j == size - 1 ? '
               'this.field[i][j] + "\\n" : this.field[i][j]);\n'
               '\n'
               '            }\n'
               '        }\n'
               '    }\n'
               '}'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=6,
          lineno=158,
          tokens=222,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Evolution',
          body='class Evolution {\n'
               '\n'
               '    int generations;\n'
               '    char[][] field;\n'
               '    boolean restart = false;\n'
               '\n'
               '    public Evolution() {}\n'
               '\n'
               '    public void evolve(Universe universe) {\n'
               '\n'
               '        this.field = new char[universe.size][universe.size];\n'
               '\n'
               '        if (this.generations == 0) {\n'
               '\n'
               '            System.out.println("Generation 0");\n'
               '            GameOfLife.generationLabel.setText(" Generation '
               '0");\n'
               '\n'
               '            universe.print();\n'
               '            return;\n'
               '\n'
               '        }\n'
               '\n'
               '        for (int g = 1; g <= this.generations; g++) {\n'
               '\n'
               '            if (restart) {\n'
               '\n'
               '                restart = false;\n'
               '                break;\n'
               '\n'
               '            }\n'
               '\n'
               '            try {\n'
               '\n'
               '                while (GameOfLife.paused) {\n'
               '\n'
               '                    Thread.sleep(1000l);\n'
               '\n'
               '                }\n'
               '\n'
               '                Thread.sleep(50l);\n'
               '                if (g < this.generations) {\n'
               '\n'
               '                    new '
               'ProcessBuilder("cmd","/c","cls").inheritIO().start().waitFor();\n'
               '\n'
               '                }\n'
               '            } catch (Exception e) {\n'
               '\n'
               '                e.printStackTrace();\n'
               '\n'
               '            }\n'
               '\n'
               '            universe.alive = 0;\n'
               '\n'
               '            for (int i = 0; i < universe.getSize(); i++) {\n'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=7,
          lineno=212,
          tokens=103,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Evolution',
          body='\n'
               '                for (int j = 0; j < universe.getSize(); j++) '
               '{\n'
               '\n'
               '                    int neighbours = 0;\n'
               '                    int n = i - 1;\n'
               '                    int s = i + 1;\n'
               '                    int w = j - 1;\n'
               '                    int e = j + 1;\n'
               '\n'
               '                    if (i == 0) {\n'
               '\n'
               '                        n = universe.getSize() - 1;\n'
               '\n'
               '                    } else if (i == universe.getSize() - 1) {\n'
               '\n'
               '                        s = 0;\n'
               '\n'
               '                    }\n'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=8,
          lineno=230,
          tokens=203,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Evolution',
          body='\n'
               '                    if (j == 0) {\n'
               '\n'
               '                        w = universe.getSize() - 1;\n'
               '\n'
               '                    } else if (j == universe.getSize() - 1) {\n'
               '\n'
               '                        e = 0;\n'
               '\n'
               '                    }\n'
               '\n'
               "                    neighbours += universe.field[n][w] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[n][j] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[n][e] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[i][w] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[i][e] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[s][w] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[s][j] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[s][e] == 'O' "
               '? 1 : 0;\n'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=9,
          lineno=249,
          tokens=241,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Evolution',
          body='\n'
               "                    if (universe.field[i][j] == 'O') {\n"
               '\n'
               '                        this.field[i][j] = neighbours < 2 || '
               "neighbours > 3 ? ' ' : 'O';\n"
               '\n'
               '                    } else {\n'
               '\n'
               '                        this.field[i][j] = neighbours == 3 ? '
               "'O' : ' ';\n"
               '\n'
               '                    }\n'
               '                }\n'
               '            }\n'
               '\n'
               '            for (int i = 0; i < universe.getSize(); i++) {\n'
               '\n'
               '                for (int j = 0; j < universe.getSize(); j++) '
               '{\n'
               '\n'
               '                    universe.field[i][j] = this.field[i][j];\n'
               '\n'
               "                    if (this.field[i][j] == 'O') {\n"
               '\n'
               '                        universe.alive++;\n'
               '\n'
               '                    }\n'
               '                }\n'
               '            }\n'
               '\n'
               '            universe.genNum = g;\n'
               '            GameOfLife.generationLabel.setText(" Generation #" '
               '+ universe.genNum);\n'
               '            System.out.println("Generation #" + g);\n'
               '            universe.print();\n'
               '            GameOfLife.universePanel.repaint();\n'
               '        }\n'
               '    }\n'
               '\n'
               '    public void setGenerations(int generations) {\n'
               '\n'
               '        if (generations >= 0) {\n'
               '\n'
               '            this.generations = generations;\n'
               '\n'
               '        } else {\n'
               '\n'
               '            System.out.println("Number of generations can\'t '
               'be negative.");\n'
               '\n'
               '        }\n'
               '    }\n'
               '}'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=10,
          lineno=298,
          tokens=204,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='UniversePanel',
          body='class UniversePanel extends JPanel {\n'
               '\n'
               '    public UniversePanel() {\n'
               '\n'
               '        '
               'setBorder(BorderFactory.createLineBorder(Color.black));\n'
               '        setBounds(1, 41, 700, 700);\n'
               '\n'
               '    }\n'
               '\n'
               '    public void paintComponent(Graphics g) {\n'
               '\n'
               '        super.paintComponent(g);\n'
               '\n'
               '        for (int i = 1; i < GameOfLife.universe.getSize(); '
               'i++) {\n'
               '\n'
               '            g.drawLine(20 * i, 0, 20 * i, 900);\n'
               '            g.drawLine(0, 20 * i, 905, 20 * i);\n'
               '\n'
               '        }\n'
               '\n'
               '        for (int i = 0; i < GameOfLife.universe.getSize(); '
               'i++) {\n'
               '\n'
               '            for (int j = 0; j < GameOfLife.universe.getSize(); '
               'j++) {\n'
               '\n'
               "                if (GameOfLife.universe.field[i][j] == 'O') {\n"
               '\n'
               '                    g.fillRect(j * 20, i * 20, 20, 20);\n'
               '\n'
               '                }\n'
               '            }\n'
               '        }\n'
               '    }\n'
               '}'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=11,
          lineno=332,
          tokens=29,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='PauseListener',
          body='class PauseListener implements ActionListener {\n'
               '\n'
               '    public void actionPerformed(ActionEvent e) {\n'
               '\n'
               '        GameOfLife.paused = !GameOfLife.paused;\n'
               '\n'
               '    }\n'
               '}'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=12,
          lineno=341,
          tokens=27,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='RestartListener',
          body='class RestartListener implements ActionListener {\n'
               '\n'
               '    public void actionPerformed(ActionEvent e) {\n'
               '\n'
               '        GameOfLife.evolution.restart = true;\n'
               '\n'
               '    }\n'
               '}'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=13,
          lineno=68,
          tokens=60,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='main',
          body='public static void main(String[] args) {\n'
               '\n'
               '        new GameOfLife();\n'
               '        universe.setSize(35);\n'
               '        evolution.setGenerations(500);\n'
               '\n'
               '        while (true) {\n'
               '\n'
               '            if (!evolution.restart) {\n'
               '\n'
               '                universe.create();\n'
               '                evolution.evolve(universe);\n'
               '\n'
               '            }\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=14,
          lineno=96,
          tokens=12,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='getSize',
          body='public int getSize() {\n\n        return this.size;\n\n    }'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=15,
          lineno=102,
          tokens=43,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='setSize',
          body='public void setSize(int size) {\n'
               '\n'
               '        if (size > 0) {\n'
               '\n'
               '            this.size = size;\n'
               '\n'
               '        } else {\n'
               '\n'
               '            System.out.println("Size must be greater than '
               '0.");\n'
               '\n'
               '        }\n'
               '\n'
               '    }'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=16,
          lineno=116,
          tokens=117,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='create',
          body='public void create() {\n'
               '\n'
               '        this.genNum = 0;\n'
               '        this.alive = 0;\n'
               '        this.rand = new Random();\n'
               '\n'
               '        this.field = new char[size][size];\n'
               '\n'
               '        for (int i = 0; i < this.size; i++) {\n'
               '\n'
               '            for (int j = 0; j < this.size; j++) {\n'
               '\n'
               '                if (this.rand.nextBoolean()) {\n'
               '\n'
               "                    this.field[i][j] = 'O';\n"
               '                    alive++;\n'
               '\n'
               '                } else {\n'
               '\n'
               "                    this.field[i][j] = ' ';\n"
               '\n'
               '                }\n'
               '            }\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=17,
          lineno=142,
          tokens=107,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='print',
          body='public void print() {\n'
               '\n'
               '        GameOfLife.aliveLabel.setText(" Alive: " + '
               'GameOfLife.universe.alive);\n'
               '        System.out.println("Alive: " + this.alive);\n'
               '\n'
               '        for (int i = 0; i < this.size; i++) {\n'
               '\n'
               '            for (int j = 0; j < this.size; j++) {\n'
               '\n'
               '                System.out.print(j == size - 1 ? '
               'this.field[i][j] + "\\n" : this.field[i][j]);\n'
               '\n'
               '            }\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=18,
          lineno=166,
          tokens=198,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='evolve',
          body='public void evolve(Universe universe) {\n'
               '\n'
               '        this.field = new char[universe.size][universe.size];\n'
               '\n'
               '        if (this.generations == 0) {\n'
               '\n'
               '            System.out.println("Generation 0");\n'
               '            GameOfLife.generationLabel.setText(" Generation '
               '0");\n'
               '\n'
               '            universe.print();\n'
               '            return;\n'
               '\n'
               '        }\n'
               '\n'
               '        for (int g = 1; g <= this.generations; g++) {\n'
               '\n'
               '            if (restart) {\n'
               '\n'
               '                restart = false;\n'
               '                break;\n'
               '\n'
               '            }\n'
               '\n'
               '            try {\n'
               '\n'
               '                while (GameOfLife.paused) {\n'
               '\n'
               '                    Thread.sleep(1000l);\n'
               '\n'
               '                }\n'
               '\n'
               '                Thread.sleep(50l);\n'
               '                if (g < this.generations) {\n'
               '\n'
               '                    new '
               'ProcessBuilder("cmd","/c","cls").inheritIO().start().waitFor();\n'
               '\n'
               '                }\n'
               '            } catch (Exception e) {\n'
               '\n'
               '                e.printStackTrace();\n'
               '\n'
               '            }\n'
               '\n'
               '            universe.alive = 0;\n'
               '\n'
               '            for (int i = 0; i < universe.getSize(); i++) {\n'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=19,
          lineno=212,
          tokens=103,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='evolve',
          body='\n'
               '                for (int j = 0; j < universe.getSize(); j++) '
               '{\n'
               '\n'
               '                    int neighbours = 0;\n'
               '                    int n = i - 1;\n'
               '                    int s = i + 1;\n'
               '                    int w = j - 1;\n'
               '                    int e = j + 1;\n'
               '\n'
               '                    if (i == 0) {\n'
               '\n'
               '                        n = universe.getSize() - 1;\n'
               '\n'
               '                    } else if (i == universe.getSize() - 1) {\n'
               '\n'
               '                        s = 0;\n'
               '\n'
               '                    }\n'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=20,
          lineno=230,
          tokens=203,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='evolve',
          body='\n'
               '                    if (j == 0) {\n'
               '\n'
               '                        w = universe.getSize() - 1;\n'
               '\n'
               '                    } else if (j == universe.getSize() - 1) {\n'
               '\n'
               '                        e = 0;\n'
               '\n'
               '                    }\n'
               '\n'
               "                    neighbours += universe.field[n][w] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[n][j] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[n][e] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[i][w] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[i][e] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[s][w] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[s][j] == 'O' "
               '? 1 : 0;\n'
               "                    neighbours += universe.field[s][e] == 'O' "
               '? 1 : 0;\n'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=21,
          lineno=249,
          tokens=192,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='evolve',
          body='\n'
               "                    if (universe.field[i][j] == 'O') {\n"
               '\n'
               '                        this.field[i][j] = neighbours < 2 || '
               "neighbours > 3 ? ' ' : 'O';\n"
               '\n'
               '                    } else {\n'
               '\n'
               '                        this.field[i][j] = neighbours == 3 ? '
               "'O' : ' ';\n"
               '\n'
               '                    }\n'
               '                }\n'
               '            }\n'
               '\n'
               '            for (int i = 0; i < universe.getSize(); i++) {\n'
               '\n'
               '                for (int j = 0; j < universe.getSize(); j++) '
               '{\n'
               '\n'
               '                    universe.field[i][j] = this.field[i][j];\n'
               '\n'
               "                    if (this.field[i][j] == 'O') {\n"
               '\n'
               '                        universe.alive++;\n'
               '\n'
               '                    }\n'
               '                }\n'
               '            }\n'
               '\n'
               '            universe.genNum = g;\n'
               '            GameOfLife.generationLabel.setText(" Generation #" '
               '+ universe.genNum);\n'
               '            System.out.println("Generation #" + g);\n'
               '            universe.print();\n'
               '            GameOfLife.universePanel.repaint();\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=22,
          lineno=284,
          tokens=47,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='setGenerations',
          body='public void setGenerations(int generations) {\n'
               '\n'
               '        if (generations >= 0) {\n'
               '\n'
               '            this.generations = generations;\n'
               '\n'
               '        } else {\n'
               '\n'
               '            System.out.println("Number of generations can\'t '
               'be negative.");\n'
               '\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=23,
          lineno=307,
          tokens=162,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='paintComponent',
          body='public void paintComponent(Graphics g) {\n'
               '\n'
               '        super.paintComponent(g);\n'
               '\n'
               '        for (int i = 1; i < GameOfLife.universe.getSize(); '
               'i++) {\n'
               '\n'
               '            g.drawLine(20 * i, 0, 20 * i, 900);\n'
               '            g.drawLine(0, 20 * i, 905, 20 * i);\n'
               '\n'
               '        }\n'
               '\n'
               '        for (int i = 0; i < GameOfLife.universe.getSize(); '
               'i++) {\n'
               '\n'
               '            for (int j = 0; j < GameOfLife.universe.getSize(); '
               'j++) {\n'
               '\n'
               "                if (GameOfLife.universe.field[i][j] == 'O') {\n"
               '\n'
               '                    g.fillRect(j * 20, i * 20, 20, 20);\n'
               '\n'
               '                }\n'
               '            }\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=24,
          lineno=334,
          tokens=40,
          depth=2,
          parent_id=None,
          category='method',
          summary=False,
          name='actionPerformed',
          body='public void actionPerformed(ActionEvent e) {\n'
               '\n'
               '        GameOfLife.paused = !GameOfLife.paused;\n'
               '\n'
               '    }public void actionPerformed(ActionEvent e) {\n'
               '\n'
               '        GameOfLife.evolution.restart = true;\n'
               '\n'
               '    }'),
 Fragment(document_cs='0f962b05cc6d5707ce2b748eabbb84570dd8d9040dbbcf15e81e29d500235b04',
          id=25,
          lineno=1,
          tokens=114,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Evolution GameOfLife PauseListener RestartListener '
               'Universe UniversePanel\n'
               '  Methods: actionPerformed create evolve getSize main '
               'paintComponent print setGenerations setSize\n'
               '  Usages: BorderFactory Thread add addActionListener alive '
               'aliveLabel controlPanel create createEtchedBorder '
               'createLineBorder drawLine e evolution evolve fillRect g '
               'generationLabel generations getSize i infoPanel inheritIO j n '
               'neighbours nextBoolean paintComponent pauseButton print '
               'printStackTrace println repaint restart restartButton s '
               'setBorder setBounds setDefaultCloseOperation setGenerations '
               'setLayout setLocationRelativeTo setName setSize setText '
               'setVisible size sleep start universe universePanel w waitFor\n'),
 Fragment(document_cs='77a7ebad8ad0f0fa90514c0a5f5f1db1357be1de6c589411b5d1a204d67ddb14',
          id=26,
          lineno=1,
          tokens=66,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# Game of Life\n'
               '\n'
               'My 8th project from Hyperskill.\n'
               '\n'
               "This program provides Conway's Game of Life experience with a "
               'GUI.\n'
               '\n'
               'Features:\n'
               '- window with graphical representation of the grid (35x35) and '
               'the current "universe" state;\n'
               '- generation number and alive cells counters;\n'
               '- pause and restart buttons.\n'),
 Fragment(document_cs='77a7ebad8ad0f0fa90514c0a5f5f1db1357be1de6c589411b5d1a204d67ddb14',
          id=27,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='# Game of Life\n')]