[Fragment(document_cs='0016f76490775633602914e96aa936588f08c6f4ca25102c3f53141abc0ebb1b',
          id=1,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='00fedd6c09e1926625e7b77bf67014a6f1dcb5125ac5ae27133d8af05ec762e7',
          id=2,
          lineno=6,
          tokens=162,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='NewUserColumns',
          body='class NewUserColumns extends Migration\n'
               '{\n'
               '    /**\n'
               '     * Run the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function up()\n'
               '    {\n'
               "        Schema::table('users', function (Blueprint $table) {\n"
               "            $table->string('title');\n"
               "            $table->string('bio');\n"
               "            $table->string('link');\n"
               "            $table->string('twitter');\n"
               "            $table->string('facebook');\n"
               "            $table->string('linkedin');\n"
               '        });\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Reverse the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function down()\n'
               '    {\n'
               "        Schema::table('users', function (Blueprint $table) {\n"
               '            '
               "$table->dropColumn(['title','bio','link','twitter','facebook','linkedin']);\n"
               '        });\n'
               '    }\n'
               '}'),
 Fragment(document_cs='00fedd6c09e1926625e7b77bf67014a6f1dcb5125ac5ae27133d8af05ec762e7',
          id=3,
          lineno=13,
          tokens=72,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '    {\n'
               "        Schema::table('users', function (Blueprint $table) {\n"
               "            $table->string('title');\n"
               "            $table->string('bio');\n"
               "            $table->string('link');\n"
               "            $table->string('twitter');\n"
               "            $table->string('facebook');\n"
               "            $table->string('linkedin');\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='00fedd6c09e1926625e7b77bf67014a6f1dcb5125ac5ae27133d8af05ec762e7',
          id=4,
          lineno=30,
          tokens=43,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '    {\n'
               "        Schema::table('users', function (Blueprint $table) {\n"
               '            '
               "$table->dropColumn(['title','bio','link','twitter','facebook','linkedin']);\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='00fedd6c09e1926625e7b77bf67014a6f1dcb5125ac5ae27133d8af05ec762e7',
          id=5,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: NewUserColumns\n'
               '  Usages: table\n'),
 Fragment(document_cs='018a94996eeb3b7aa32a6c273be30b424e004751b6b2a10837d9dfb5715dc799',
          id=6,
          lineno=13,
          tokens=131,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='TasksController',
          body='class TasksController extends BaseController {\n'
               '\n'
               '    // Return all tasks that are not completed for the given '
               'user\n'
               '    public function getAllUserOpenTasks(){\n'
               '        $tasks = '
               "Task::where('user_id',Auth::id())->where('state', '!=', "
               "'complete')->get();\n"
               "        return $this->setStatusCode(200)->makeResponse('Tasks "
               "retrieved successfully',$tasks->toArray());\n"
               '    }\n'
               '\n'
               '    // Insert a new task into the database\n'
               '    public function storeTask($client_id, $project_id){\n'
               '        if (!Input::all()) {\n'
               "            return $this->setStatusCode(406)->makeResponse('No "
               "information provided to create task');\n"
               '        }\n'),
 Fragment(document_cs='018a94996eeb3b7aa32a6c273be30b424e004751b6b2a10837d9dfb5715dc799',
          id=7,
          lineno=26,
          tokens=159,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='TasksController',
          body='\n'
               "        if (!Input::get('name')) {\n"
               '            return '
               "$this->setStatusCode(406)->makeResponse('The name seems to be "
               "empty');\n"
               '        }\n'
               '\n'
               "        Input::merge(array('user_id' => Auth::id(), "
               "'client_id' => $client_id, 'project_id' => $project_id));\n"
               '\n'
               '        Task::create(Input::all());\n'
               '        $id = \\DB::getPdo()->lastInsertId();\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('Task "
               "created successfully', Task::find($id));\n"
               '    }\n'
               '\n'
               '    // Update the given task\n'
               '    public function updateTask($id){\n'
               '        if (!Task::find($id)) {\n'
               '            return '
               "$this->setStatusCode(400)->makeResponse('Could not find the "
               "task');\n"
               '        }\n'),
 Fragment(document_cs='018a94996eeb3b7aa32a6c273be30b424e004751b6b2a10837d9dfb5715dc799',
          id=8,
          lineno=44,
          tokens=159,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='TasksController',
          body='\n'
               '        if ( Input::get(\'name\') === "") {\n'
               '            return '
               "$this->setStatusCode(406)->makeResponse('The task needs a "
               "name');\n"
               '        }\n'
               '\n'
               '        $input = Input::all();\n'
               "        unset($input['_method']);\n"
               '\n'
               '        Task::find($id)->update($input);\n'
               "        return $this->setStatusCode(200)->makeResponse('The "
               "task has been updated');\n"
               '    }\n'
               '\n'
               '    // Remove the given task from the database\n'
               '    public function removeTask($id){\n'
               '        if (!Task::find($id)) {\n'
               '            return '
               "$this->setStatusCode(400)->makeResponse('Could not find the "
               "task');\n"
               '        }\n'
               '\n'
               '        Task::find($id)->delete();\n'
               "        return $this->setStatusCode(200)->makeResponse('Task "
               "deleted successfully');\n"
               '    }\n'
               '\n'
               '}'),
 Fragment(document_cs='018a94996eeb3b7aa32a6c273be30b424e004751b6b2a10837d9dfb5715dc799',
          id=9,
          lineno=16,
          tokens=57,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='getAllUserOpenTasks',
          body='public function getAllUserOpenTasks(){\n'
               '        $tasks = '
               "Task::where('user_id',Auth::id())->where('state', '!=', "
               "'complete')->get();\n"
               "        return $this->setStatusCode(200)->makeResponse('Tasks "
               "retrieved successfully',$tasks->toArray());\n"
               '    }'),
 Fragment(document_cs='018a94996eeb3b7aa32a6c273be30b424e004751b6b2a10837d9dfb5715dc799',
          id=10,
          lineno=22,
          tokens=154,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='storeTask',
          body='public function storeTask($client_id, $project_id){\n'
               '        if (!Input::all()) {\n'
               "            return $this->setStatusCode(406)->makeResponse('No "
               "information provided to create task');\n"
               '        }\n'
               '\n'
               "        if (!Input::get('name')) {\n"
               '            return '
               "$this->setStatusCode(406)->makeResponse('The name seems to be "
               "empty');\n"
               '        }\n'
               '\n'
               "        Input::merge(array('user_id' => Auth::id(), "
               "'client_id' => $client_id, 'project_id' => $project_id));\n"
               '\n'
               '        Task::create(Input::all());\n'
               '        $id = \\DB::getPdo()->lastInsertId();\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('Task "
               "created successfully', Task::find($id));\n"
               '    }'),
 Fragment(document_cs='018a94996eeb3b7aa32a6c273be30b424e004751b6b2a10837d9dfb5715dc799',
          id=11,
          lineno=40,
          tokens=118,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='updateTask',
          body='public function updateTask($id){\n'
               '        if (!Task::find($id)) {\n'
               '            return '
               "$this->setStatusCode(400)->makeResponse('Could not find the "
               "task');\n"
               '        }\n'
               '\n'
               '        if ( Input::get(\'name\') === "") {\n'
               '            return '
               "$this->setStatusCode(406)->makeResponse('The task needs a "
               "name');\n"
               '        }\n'
               '\n'
               '        $input = Input::all();\n'
               "        unset($input['_method']);\n"
               '\n'
               '        Task::find($id)->update($input);\n'
               "        return $this->setStatusCode(200)->makeResponse('The "
               "task has been updated');\n"
               '    }'),
 Fragment(document_cs='018a94996eeb3b7aa32a6c273be30b424e004751b6b2a10837d9dfb5715dc799',
          id=12,
          lineno=57,
          tokens=66,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='removeTask',
          body='public function removeTask($id){\n'
               '        if (!Task::find($id)) {\n'
               '            return '
               "$this->setStatusCode(400)->makeResponse('Could not find the "
               "task');\n"
               '        }\n'
               '\n'
               '        Task::find($id)->delete();\n'
               "        return $this->setStatusCode(200)->makeResponse('Task "
               "deleted successfully');\n"
               '    }'),
 Fragment(document_cs='018a94996eeb3b7aa32a6c273be30b424e004751b6b2a10837d9dfb5715dc799',
          id=13,
          lineno=1,
          tokens=32,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: getAllUserOpenTasks removeTask storeTask '
               'updateTask\n'
               '  Classes: TasksController\n'
               '  Usages: client_id input project_id tasks this\n'),
 Fragment(document_cs='01b4125abf717af7d4297bf61d1ad1aff6a631ed106245b19612304c61da7eae',
          id=14,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='027d116f2e2bfd4b1a9b50e496d41fd1ded5ca6e2bf9f94ce8fec290a52d88fe',
          id=15,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='029545c9b755a61d3007edcf33124f5fae06afd491eb7acd2c1f8382018f7678',
          id=16,
          lineno=7,
          tokens=46,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='VerifyCsrfToken',
          body='class VerifyCsrfToken extends BaseVerifier\n'
               '{\n'
               '    /**\n'
               '     * The URIs that should be excluded from CSRF '
               'verification.\n'
               '     *\n'
               '     * @var array\n'
               '     */\n'
               '    protected $except = [\n'
               '        //\n'
               '    ];\n'
               '}'),
 Fragment(document_cs='029545c9b755a61d3007edcf33124f5fae06afd491eb7acd2c1f8382018f7678',
          id=17,
          lineno=1,
          tokens=14,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: VerifyCsrfToken\n  Usages: except\n'),
 Fragment(document_cs='051a8dbec6e97a2334367710957d4db3e0201da44d3cdaaaa6c6619ab5e0154d',
          id=18,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='055d9871df01573858a6698b545aa1b6e96c5b12156603bbc4d87f21dee16e55',
          id=19,
          lineno=1,
          tokens=51,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='/bootstrap/compiled.php\n'
               '/vendor\n'
               '/public/uploads/files/*\n'
               'composer.phar\n'
               'composer.lock\n'
               '.env.*.php\n'
               '.env.php\n'
               '.DS_Store\n'
               'Thumbs.db\n'
               '.idea\n'
               '/public/uploads/files/*\n'
               '/vendor\n'
               '/node_modules\n'
               'Homestead.yaml\n'
               '.env\n'),
 Fragment(document_cs='055d9871df01573858a6698b545aa1b6e96c5b12156603bbc4d87f21dee16e55',
          id=20,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='0b00ef2806fcb0c3f6089bf257192e0335e2d1b270aae74dbd1291d232669844',
          id=21,
          lineno=6,
          tokens=121,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CreatePasswordResetsTable',
          body='class CreatePasswordResetsTable extends Migration\n'
               '{\n'
               '    /**\n'
               '     * Run the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function up()\n'
               '    {\n'
               "        Schema::create('password_resets', function (Blueprint "
               '$table) {\n'
               "            $table->string('email')->index();\n"
               "            $table->string('token')->index();\n"
               "            $table->timestamp('created_at');\n"
               '        });\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Reverse the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function down()\n'
               '    {\n'
               "        Schema::drop('password_resets');\n"
               '    }\n'
               '}'),
 Fragment(document_cs='0b00ef2806fcb0c3f6089bf257192e0335e2d1b270aae74dbd1291d232669844',
          id=22,
          lineno=13,
          tokens=55,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '    {\n'
               "        Schema::create('password_resets', function (Blueprint "
               '$table) {\n'
               "            $table->string('email')->index();\n"
               "            $table->string('token')->index();\n"
               "            $table->timestamp('created_at');\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='0b00ef2806fcb0c3f6089bf257192e0335e2d1b270aae74dbd1291d232669844',
          id=23,
          lineno=27,
          tokens=17,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '    {\n'
               "        Schema::drop('password_resets');\n"
               '    }'),
 Fragment(document_cs='0b00ef2806fcb0c3f6089bf257192e0335e2d1b270aae74dbd1291d232669844',
          id=24,
          lineno=1,
          tokens=21,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: CreatePasswordResetsTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='0bebfa7882e392a820aeb58254887beaadb37cd540b9982fe4c1ee10dbaf33e8',
          id=25,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='0d1270e8a4b63e1b33b97a70089050a09599491b97078522182e2dd07c5629da',
          id=26,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='0e01006feee460e5543c74a490fd03e2ba9ddbbcec349fd2685c1bb452a406a9',
          id=27,
          lineno=1,
          tokens=24,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='suites:\n'
               '    main:\n'
               '        namespace: App\n'
               '        psr4_prefix: App\n'
               '        src_path: app'),
 Fragment(document_cs='0e01006feee460e5543c74a490fd03e2ba9ddbbcec349fd2685c1bb452a406a9',
          id=28,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='1012397b20028c69c34f85a0d37438929001cd18099cd13558191520602dbfea',
          id=29,
          lineno=6,
          tokens=166,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CreateCredentialsTable',
          body='class CreateCredentialsTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::create('credentials', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->integer('user_id');\n"
               "\t\t\t$table->integer('project_id');\t\t\t\n"
               "\t\t\t$table->boolean('type');\n"
               "\t\t\t$table->string('name');\n"
               "\t\t\t$table->string('hostname');\n"
               "\t\t\t$table->string('username');\n"
               "\t\t\t$table->string('password');\n"
               "\t\t\t$table->integer('port');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::drop('credentials');\n"
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='1012397b20028c69c34f85a0d37438929001cd18099cd13558191520602dbfea',
          id=30,
          lineno=13,
          tokens=107,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::create('credentials', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->integer('user_id');\n"
               "\t\t\t$table->integer('project_id');\t\t\t\n"
               "\t\t\t$table->boolean('type');\n"
               "\t\t\t$table->string('name');\n"
               "\t\t\t$table->string('hostname');\n"
               "\t\t\t$table->string('username');\n"
               "\t\t\t$table->string('password');\n"
               "\t\t\t$table->integer('port');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='1012397b20028c69c34f85a0d37438929001cd18099cd13558191520602dbfea',
          id=31,
          lineno=36,
          tokens=15,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '\t{\n'
               "\t\tSchema::drop('credentials');\n"
               '\t}'),
 Fragment(document_cs='1012397b20028c69c34f85a0d37438929001cd18099cd13558191520602dbfea',
          id=32,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: CreateCredentialsTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='11dc58f367654bffcd23cf1e9faa9a6b9f7561b8bc646353cd3235e79d37758b',
          id=33,
          lineno=7,
          tokens=139,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='TasksTableSeeder',
          body='class TasksTableSeeder extends Seeder {\n'
               '\n'
               '\tpublic function run()\n'
               '\t{\n'
               '\t\t$faker = Faker::create();\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=0;');\n"
               '\n'
               "\t\tDB::table('tasks')->truncate();\n"
               "\t\tDB::table('tasks')->insert(\n"
               '\t\t    array(\n'
               "\t\t    \t'user_id' \t\t\t=>\t1,\n"
               "\t\t    \t'project_id' \t\t=>\t1,\n"
               '\t\t    \t\'name\'\t\t\t\t=>\t"First Task",\n'
               '\t\t    \t\'state\' \t\t\t=> \t"incomplete",\n'
               "\t\t    \t'weight'\t\t\t=>\t2,\n"
               '\t\t    \t)\n'
               '\t\t);\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=1;');\n"
               '\t}\n'
               '}'),
 Fragment(document_cs='11dc58f367654bffcd23cf1e9faa9a6b9f7561b8bc646353cd3235e79d37758b',
          id=34,
          lineno=9,
          tokens=131,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='run',
          body='public function run()\n'
               '\t{\n'
               '\t\t$faker = Faker::create();\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=0;');\n"
               '\n'
               "\t\tDB::table('tasks')->truncate();\n"
               "\t\tDB::table('tasks')->insert(\n"
               '\t\t    array(\n'
               "\t\t    \t'user_id' \t\t\t=>\t1,\n"
               "\t\t    \t'project_id' \t\t=>\t1,\n"
               '\t\t    \t\'name\'\t\t\t\t=>\t"First Task",\n'
               '\t\t    \t\'state\' \t\t\t=> \t"incomplete",\n'
               "\t\t    \t'weight'\t\t\t=>\t2,\n"
               '\t\t    \t)\n'
               '\t\t);\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=1;');\n"
               '\t}'),
 Fragment(document_cs='11dc58f367654bffcd23cf1e9faa9a6b9f7561b8bc646353cd3235e79d37758b',
          id=35,
          lineno=1,
          tokens=18,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: run\n'
               '  Classes: TasksTableSeeder\n'
               '  Usages: faker\n'),
 Fragment(document_cs='161cbb7b719906f095c8eb4e6db24f6114e09241dc874e90714cf91820d69367',
          id=36,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='1f7c1beef30b08b475daed1942d679b855ae38fa16a49e894ab6b9eddd08f3bd',
          id=37,
          lineno=7,
          tokens=54,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ExampleTest',
          body='class ExampleTest extends TestCase\n'
               '{\n'
               '    /**\n'
               '     * A basic functional test example.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function testBasicExample()\n'
               '    {\n'
               "        $this->visit('/')\n"
               "             ->see('Laravel 5');\n"
               '    }\n'
               '}'),
 Fragment(document_cs='1f7c1beef30b08b475daed1942d679b855ae38fa16a49e894ab6b9eddd08f3bd',
          id=38,
          lineno=14,
          tokens=25,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='testBasicExample',
          body='public function testBasicExample()\n'
               '    {\n'
               "        $this->visit('/')\n"
               "             ->see('Laravel 5');\n"
               '    }'),
 Fragment(document_cs='1f7c1beef30b08b475daed1942d679b855ae38fa16a49e894ab6b9eddd08f3bd',
          id=39,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: testBasicExample\n'
               '  Classes: ExampleTest\n'
               '  Usages: this\n'),
 Fragment(document_cs='22fab6c4cacb4114439e03dbe91814cbeed4896b20505b7b3645250b2ee2efd3',
          id=40,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='240a3e0d37d2e86b614063f5347eb02d4f99ca6c254de6b82871ff8d95532a7d',
          id=41,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='*\n!.gitignore\n'),
 Fragment(document_cs='240a3e0d37d2e86b614063f5347eb02d4f99ca6c254de6b82871ff8d95532a7d',
          id=42,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='*\n!.gitignore\n'),
 Fragment(document_cs='240a3e0d37d2e86b614063f5347eb02d4f99ca6c254de6b82871ff8d95532a7d',
          id=43,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='*\n!.gitignore\n'),
 Fragment(document_cs='240a3e0d37d2e86b614063f5347eb02d4f99ca6c254de6b82871ff8d95532a7d',
          id=44,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='*\n!.gitignore\n'),
 Fragment(document_cs='240a3e0d37d2e86b614063f5347eb02d4f99ca6c254de6b82871ff8d95532a7d',
          id=45,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='240a3e0d37d2e86b614063f5347eb02d4f99ca6c254de6b82871ff8d95532a7d',
          id=46,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='240a3e0d37d2e86b614063f5347eb02d4f99ca6c254de6b82871ff8d95532a7d',
          id=47,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='240a3e0d37d2e86b614063f5347eb02d4f99ca6c254de6b82871ff8d95532a7d',
          id=48,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='2662c7137a61279df7d5f0cc4df9c832eb809b75f212a6b810182da70aaee304',
          id=49,
          lineno=11,
          tokens=141,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AuthController',
          body='class AuthController extends Controller\n'
               '{\n'
               '    /*\n'
               '    '
               '|--------------------------------------------------------------------------\n'
               '    | Registration & Login Controller\n'
               '    '
               '|--------------------------------------------------------------------------\n'
               '    |\n'
               '    | This controller handles the registration of new users, '
               'as well as the\n'
               '    | authentication of existing users. By default, this '
               'controller uses\n'
               "    | a simple trait to add these behaviors. Why don't you "
               'explore it?\n'
               '    |\n'
               '    */\n'
               '\n'
               '    use AuthenticatesAndRegistersUsers, ThrottlesLogins;\n'
               '\n'
               '    /**\n'
               '     * Create a new authentication controller instance.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function __construct()\n'
               '    {\n'
               "        $this->middleware('guest', ['except' => "
               "'getLogout']);\n"
               '    }\n'
               '\n'
               '    /**\n'
               '     * Get a v'),
 Fragment(document_cs='2662c7137a61279df7d5f0cc4df9c832eb809b75f212a6b810182da70aaee304',
          id=50,
          lineno=37,
          tokens=182,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AuthController',
          body='alidator for an incoming registration request.\n'
               '     *\n'
               '     * @param  array  $data\n'
               '     * @return \\Illuminate\\Contracts\\Validation\\Validator\n'
               '     */\n'
               '    protected function validator(array $data)\n'
               '    {\n'
               '        return Validator::make($data, [\n'
               "            'name' => 'required|max:255',\n"
               "            'email' => 'required|email|max:255|unique:users',\n"
               "            'password' => 'required|confirmed|min:6',\n"
               '        ]);\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Create a new user instance after a valid registration.\n'
               '     *\n'
               '     * @param  array  $data\n'
               '     * @return User\n'
               '     */\n'
               '    protected function create(array $data)\n'
               '    {\n'
               '        return User::create([\n'
               "            'name' => $data['name'],\n"
               "            'email' => $data['email'],\n"
               "            'password' => bcrypt($data['password']),\n"
               '        ]);\n'
               '    }\n'
               '}'),
 Fragment(document_cs='2662c7137a61279df7d5f0cc4df9c832eb809b75f212a6b810182da70aaee304',
          id=51,
          lineno=31,
          tokens=25,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='__construct',
          body='public function __construct()\n'
               '    {\n'
               "        $this->middleware('guest', ['except' => "
               "'getLogout']);\n"
               '    }'),
 Fragment(document_cs='2662c7137a61279df7d5f0cc4df9c832eb809b75f212a6b810182da70aaee304',
          id=52,
          lineno=42,
          tokens=62,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='validator',
          body='protected function validator(array $data)\n'
               '    {\n'
               '        return Validator::make($data, [\n'
               "            'name' => 'required|max:255',\n"
               "            'email' => 'required|email|max:255|unique:users',\n"
               "            'password' => 'required|confirmed|min:6',\n"
               '        ]);\n'
               '    }'),
 Fragment(document_cs='2662c7137a61279df7d5f0cc4df9c832eb809b75f212a6b810182da70aaee304',
          id=53,
          lineno=57,
          tokens=50,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='create',
          body='protected function create(array $data)\n'
               '    {\n'
               '        return User::create([\n'
               "            'name' => $data['name'],\n"
               "            'email' => $data['email'],\n"
               "            'password' => bcrypt($data['password']),\n"
               '        ]);\n'
               '    }'),
 Fragment(document_cs='2662c7137a61279df7d5f0cc4df9c832eb809b75f212a6b810182da70aaee304',
          id=54,
          lineno=1,
          tokens=21,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: __construct create validator\n'
               '  Classes: AuthController\n'
               '  Usages: data this\n'),
 Fragment(document_cs='26bc87560b566881623f3869e573943d1663ea05fedb4001543519d6ca6e8264',
          id=55,
          lineno=1,
          tokens=9,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Usages: app kernel request response\n'),
 Fragment(document_cs='26d2ca555a07e068a966c5790425576592457e5efe43da5dad4d699953a300e2',
          id=56,
          lineno=7,
          tokens=94,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Client',
          body='class Client extends Model {\n'
               '\n'
               "\tprotected $table = 'clients';\n"
               "\tprotected $hidden = ['created_at','updated_at'];\n"
               '\tprotected $fillable = [\n'
               "\t\t'user_id',\n"
               "\t\t'name',\n"
               "\t\t'phone_number',\n"
               "\t\t'point_of_contact',\n"
               "\t\t'email'\n"
               '\t];\n'
               '\n'
               '\t/**\n'
               '\t * Return the related projects for a given client\n'
               '\t */\n'
               '\tpublic function projects() {\n'
               "        return $this->hasMany('App\\Project', 'client_id');\n"
               '    }\n'
               '}'),
 Fragment(document_cs='26d2ca555a07e068a966c5790425576592457e5efe43da5dad4d699953a300e2',
          id=57,
          lineno=22,
          tokens=22,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='projects',
          body='public function projects() {\n'
               "        return $this->hasMany('App\\Project', 'client_id');\n"
               '    }'),
 Fragment(document_cs='26d2ca555a07e068a966c5790425576592457e5efe43da5dad4d699953a300e2',
          id=58,
          lineno=1,
          tokens=20,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: projects\n'
               '  Classes: Client\n'
               '  Usages: fillable hidden table this\n'),
 Fragment(document_cs='28f42b5608f2877ed1172eb79ca0bdc29445ac4928db64f5674effb6fa4109cd',
          id=59,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='29eba26feb29dd81ee149272c468123b72c19186a9c842fbb6a3da3af49b266b',
          id=60,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='2c23c154eae3d588bda9282857204967a84468fd1f3bc6321faee55b8c8b78dd',
          id=61,
          lineno=7,
          tokens=11,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Request',
          body='abstract class Request extends FormRequest\n{\n    //\n}'),
 Fragment(document_cs='2c23c154eae3d588bda9282857204967a84468fd1f3bc6321faee55b8c8b78dd',
          id=62,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Request\n'),
 Fragment(document_cs='2c9cef3de27f76ac0ba46a87128a2c1892f78dc1748c3017caae84c058a90ec8',
          id=63,
          lineno=6,
          tokens=119,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AddPhoneNumberToClientsTable',
          body='class AddPhoneNumberToClientsTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->string('phone_number',20);\n"
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->dropColumn(['phone_number']);\n"
               '\t\t});\n'
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='2c9cef3de27f76ac0ba46a87128a2c1892f78dc1748c3017caae84c058a90ec8',
          id=64,
          lineno=13,
          tokens=37,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->string('phone_number',20);\n"
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='2c9cef3de27f76ac0ba46a87128a2c1892f78dc1748c3017caae84c058a90ec8',
          id=65,
          lineno=27,
          tokens=36,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->dropColumn(['phone_number']);\n"
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='2c9cef3de27f76ac0ba46a87128a2c1892f78dc1748c3017caae84c058a90ec8',
          id=66,
          lineno=1,
          tokens=21,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: AddPhoneNumberToClientsTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='2d0db41e7083bc4d94e42d85d59fd4d5e46911fe852c87d336513f73a08d4ec7',
          id=67,
          lineno=12,
          tokens=154,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='FilesController',
          body='class FilesController extends BaseController {\n'
               '\n'
               '    /**\n'
               '     * Upload the file and store\n'
               '     * the file path in the DB.\n'
               '     */\n'
               '\tpublic function store()\n'
               '\t{\n'
               '        // Rules\n'
               "        $rules\t= array('name' => 'required', 'file' => "
               "'required|max:20000');\n"
               "        $messages = array('max' => 'Please make sure the file "
               "size is not larger then 20MB');\n"
               '\n'
               '        // Create validation\n'
               '        $validator = Validator::make( Input::all(), $rules, '
               '$messages);\n'
               '\n'
               '        if ( $validator->fails() ) {\n'
               '            return '
               'Redirect::back()->withErrors($validator)->withInput();\n'
               '        }\n'
               '\n'
               '        $directory = "uploads/files/";\n'
               '\n'
               "        // Before anything let's make sure a file was "
               'uploaded\n'),
 Fragment(document_cs='2d0db41e7083bc4d94e42d85d59fd4d5e46911fe852c87d336513f73a08d4ec7',
          id=68,
          lineno=34,
          tokens=226,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='FilesController',
          body="        if ( Input::hasFile('file') && "
               "Request::file('file')->isValid() )\n"
               '        {\n'
               '\n'
               "            $current_file = Input::file('file');\n"
               "            $filename = Auth::id() .'_'. "
               '$current_file->getClientOriginalName();\n'
               '            $current_file->move($directory, $filename);\n'
               '\n'
               '            $file = new Upload;\n'
               '            $file->user_id = Auth::id();\n'
               "            $file->project_id = Input::get('project_id');\n"
               "            $file->name = Input::get('name');\n"
               '            $file->path = $directory.$filename;\n'
               '            $file->save();\n'
               '\n'
               '            return Redirect::back();\n'
               '        }\n'
               '\n'
               '        $upload = new Upload;\n'
               '        $upload->user_id = Auth::id();\n'
               "        $upload->project_id = Input::get('project_id');\n"
               "        $upload->name = Input::get('name');\n"
               '        $upload->path = $directory.$filename;\n'
               '        $upload->save();\n'
               '\n'
               '        return Redirect::back();\n'
               '\t}\n'
               '\n'
               '    /**\n'
               '     * Delete the given file\n'
               '     */\n'
               '\tpublic function destroy($id)\n'
               '\t{\n'
               '\t\t//\n'
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='2d0db41e7083bc4d94e42d85d59fd4d5e46911fe852c87d336513f73a08d4ec7',
          id=69,
          lineno=18,
          tokens=127,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='store',
          body='public function store()\n'
               '\t{\n'
               '        // Rules\n'
               "        $rules\t= array('name' => 'required', 'file' => "
               "'required|max:20000');\n"
               "        $messages = array('max' => 'Please make sure the file "
               "size is not larger then 20MB');\n"
               '\n'
               '        // Create validation\n'
               '        $validator = Validator::make( Input::all(), $rules, '
               '$messages);\n'
               '\n'
               '        if ( $validator->fails() ) {\n'
               '            return '
               'Redirect::back()->withErrors($validator)->withInput();\n'
               '        }\n'
               '\n'
               '        $directory = "uploads/files/";\n'
               '\n'
               "        // Before anything let's make sure a file was "
               'uploaded\n'),
 Fragment(document_cs='2d0db41e7083bc4d94e42d85d59fd4d5e46911fe852c87d336513f73a08d4ec7',
          id=70,
          lineno=34,
          tokens=201,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='store',
          body="        if ( Input::hasFile('file') && "
               "Request::file('file')->isValid() )\n"
               '        {\n'
               '\n'
               "            $current_file = Input::file('file');\n"
               "            $filename = Auth::id() .'_'. "
               '$current_file->getClientOriginalName();\n'
               '            $current_file->move($directory, $filename);\n'
               '\n'
               '            $file = new Upload;\n'
               '            $file->user_id = Auth::id();\n'
               "            $file->project_id = Input::get('project_id');\n"
               "            $file->name = Input::get('name');\n"
               '            $file->path = $directory.$filename;\n'
               '            $file->save();\n'
               '\n'
               '            return Redirect::back();\n'
               '        }\n'
               '\n'
               '        $upload = new Upload;\n'
               '        $upload->user_id = Auth::id();\n'
               "        $upload->project_id = Input::get('project_id');\n"
               "        $upload->name = Input::get('name');\n"
               '        $upload->path = $directory.$filename;\n'
               '        $upload->save();\n'
               '\n'
               '        return Redirect::back();\n'
               '\t}'),
 Fragment(document_cs='2d0db41e7083bc4d94e42d85d59fd4d5e46911fe852c87d336513f73a08d4ec7',
          id=71,
          lineno=64,
          tokens=13,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='destroy',
          body='public function destroy($id)\n\t{\n\t\t//\n\t}'),
 Fragment(document_cs='2d0db41e7083bc4d94e42d85d59fd4d5e46911fe852c87d336513f73a08d4ec7',
          id=72,
          lineno=1,
          tokens=26,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: destroy store\n'
               '  Classes: FilesController\n'
               '  Usages: current_file directory file filename messages rules '
               'upload validator\n'),
 Fragment(document_cs='2e078f3757c32004de3bab1e14ee91772f19b0488fa3634111c9c16fe987aadd',
          id=73,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='31e7b360931ebfd43b2260b83e2043a60f318e10a42e898f1e55af14427c0bef',
          id=74,
          lineno=6,
          tokens=134,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ProjectsTableSeeder',
          body='class ProjectsTableSeeder extends Seeder {\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Run the database seeds.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function run()\n'
               '\t{\n'
               '\t\t$faker = Faker::create();\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=0;');\n"
               '\n'
               "\t\tDB::table('projects')->truncate();\n"
               '\n'
               "\t\tDB::table('projects')->insert(\n"
               '\t\t    array(\n'
               '\t\t    \t\'name\' \t\t\t\t=>\t"First Project",\n'
               "\t\t    \t'user_id' \t\t\t=> \t1,\n"
               "\t\t    \t'client_id'\t\t\t=>\t1,\n"
               '\t\t    \t)\n'
               '\t\t);\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=1;');\n"
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='31e7b360931ebfd43b2260b83e2043a60f318e10a42e898f1e55af14427c0bef',
          id=75,
          lineno=14,
          tokens=107,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='run',
          body='public function run()\n'
               '\t{\n'
               '\t\t$faker = Faker::create();\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=0;');\n"
               '\n'
               "\t\tDB::table('projects')->truncate();\n"
               '\n'
               "\t\tDB::table('projects')->insert(\n"
               '\t\t    array(\n'
               '\t\t    \t\'name\' \t\t\t\t=>\t"First Project",\n'
               "\t\t    \t'user_id' \t\t\t=> \t1,\n"
               "\t\t    \t'client_id'\t\t\t=>\t1,\n"
               '\t\t    \t)\n'
               '\t\t);\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=1;');\n"
               '\t}'),
 Fragment(document_cs='31e7b360931ebfd43b2260b83e2043a60f318e10a42e898f1e55af14427c0bef',
          id=76,
          lineno=1,
          tokens=18,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: run\n'
               '  Classes: ProjectsTableSeeder\n'
               '  Usages: faker\n'),
 Fragment(document_cs='325506e2901fc53d252cd7b2d1e9a858c67477e444b529f172df9c443d7b8591',
          id=77,
          lineno=8,
          tokens=115,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Kernel',
          body='class Kernel extends ConsoleKernel\n'
               '{\n'
               '    /**\n'
               '     * The Artisan commands provided by your application.\n'
               '     *\n'
               '     * @var array\n'
               '     */\n'
               '    protected $commands = [\n'
               '        \\App\\Console\\Commands\\Inspire::class,\n'
               '    ];\n'
               '\n'
               '    /**\n'
               "     * Define the application's command schedule.\n"
               '     *\n'
               '     * @param  \\Illuminate\\Console\\Scheduling\\Schedule  '
               '$schedule\n'
               '     * @return void\n'
               '     */\n'
               '    protected function schedule(Schedule $schedule)\n'
               '    {\n'
               "        $schedule->command('inspire')\n"
               '                 ->hourly();\n'
               '    }\n'
               '}'),
 Fragment(document_cs='325506e2901fc53d252cd7b2d1e9a858c67477e444b529f172df9c443d7b8591',
          id=78,
          lineno=25,
          tokens=26,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='schedule',
          body='protected function schedule(Schedule $schedule)\n'
               '    {\n'
               "        $schedule->command('inspire')\n"
               '                 ->hourly();\n'
               '    }'),
 Fragment(document_cs='325506e2901fc53d252cd7b2d1e9a858c67477e444b529f172df9c443d7b8591',
          id=79,
          lineno=1,
          tokens=16,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: schedule\n  Classes: Kernel\n  Usages: commands\n'),
 Fragment(document_cs='32696dab91b91895375a1e2034b98038677b717d704286aea4a0d7edf987b717',
          id=80,
          lineno=6,
          tokens=115,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AddEmailToClientsTable',
          body='class AddEmailToClientsTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->string('email');\n"
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->dropColumn(['email']);\n"
               '\t\t});\n'
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='32696dab91b91895375a1e2034b98038677b717d704286aea4a0d7edf987b717',
          id=81,
          lineno=13,
          tokens=34,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->string('email');\n"
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='32696dab91b91895375a1e2034b98038677b717d704286aea4a0d7edf987b717',
          id=82,
          lineno=27,
          tokens=35,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->dropColumn(['email']);\n"
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='32696dab91b91895375a1e2034b98038677b717d704286aea4a0d7edf987b717',
          id=83,
          lineno=1,
          tokens=21,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: AddEmailToClientsTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='328d2aa8515665fe6a27f00df587e37bfb463294a28aa0e89cde4208adee5ae5',
          id=84,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='33dd69945be20795b2c2e9fad4f740af55391c796e0059d1de231c7b0993e995',
          id=85,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='34730c07b8c18848e19ad87db8e98b72288dfbb89ddfed3c7449d53e3e5deb58',
          id=86,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='3643baa236598d7875f85063cb6445558e193cdcae55f0af43a7e9fdad42c780',
          id=87,
          lineno=7,
          tokens=139,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='UsersTableSeeder',
          body='class UsersTableSeeder extends Seeder {\n'
               '\n'
               '\tpublic function run()\n'
               '\t{\n'
               '\t\t$faker = Faker::create();\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=0;');\n"
               '\n'
               "\t\tDB::table('users')->truncate();\n"
               "\t\tDB::table('users')->insert(\n"
               '\t\t    array(\n'
               "\t\t    \t'full_name' \t\t=>\t$faker->name,\n"
               "\t\t    \t'email' \t\t\t=> \t'test@ribbbon.com',\n"
               "\t\t    \t'password'\t\t\t=>\tHash::make('secret'),\n"
               "\t\t    \t'tasks_created' \t=> \t1,\n"
               '\t\t    \t)\n'
               '\t\t);\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=1;');\n"
               '\t}\n'
               '}'),
 Fragment(document_cs='3643baa236598d7875f85063cb6445558e193cdcae55f0af43a7e9fdad42c780',
          id=88,
          lineno=9,
          tokens=131,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='run',
          body='public function run()\n'
               '\t{\n'
               '\t\t$faker = Faker::create();\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=0;');\n"
               '\n'
               "\t\tDB::table('users')->truncate();\n"
               "\t\tDB::table('users')->insert(\n"
               '\t\t    array(\n'
               "\t\t    \t'full_name' \t\t=>\t$faker->name,\n"
               "\t\t    \t'email' \t\t\t=> \t'test@ribbbon.com',\n"
               "\t\t    \t'password'\t\t\t=>\tHash::make('secret'),\n"
               "\t\t    \t'tasks_created' \t=> \t1,\n"
               '\t\t    \t)\n'
               '\t\t);\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=1;');\n"
               '\t}'),
 Fragment(document_cs='3643baa236598d7875f85063cb6445558e193cdcae55f0af43a7e9fdad42c780',
          id=89,
          lineno=1,
          tokens=18,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: run\n'
               '  Classes: UsersTableSeeder\n'
               '  Usages: faker\n'),
 Fragment(document_cs='38d0f07e1eaca26029aa7a0850a75e0d43d2b6dfe89ee9b51f4ee24ba99d2d8e',
          id=90,
          lineno=6,
          tokens=162,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CreateUsersTable',
          body='class CreateUsersTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::create('users', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->string('full_name');\n"
               "\t\t\t$table->string('email')->unique();\n"
               "\t\t\t$table->string('password', 60);\n"
               "\t\t\t$table->string('avatar');\n"
               "\t\t\t$table->integer('tasks_created');\n"
               "\t\t\t$table->integer('tasks_completed');\n"
               '\t\t\t$table->rememberToken();\n'
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::drop('users');\n"
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='38d0f07e1eaca26029aa7a0850a75e0d43d2b6dfe89ee9b51f4ee24ba99d2d8e',
          id=91,
          lineno=13,
          tokens=103,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::create('users', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->string('full_name');\n"
               "\t\t\t$table->string('email')->unique();\n"
               "\t\t\t$table->string('password', 60);\n"
               "\t\t\t$table->string('avatar');\n"
               "\t\t\t$table->integer('tasks_created');\n"
               "\t\t\t$table->integer('tasks_completed');\n"
               '\t\t\t$table->rememberToken();\n'
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='38d0f07e1eaca26029aa7a0850a75e0d43d2b6dfe89ee9b51f4ee24ba99d2d8e',
          id=92,
          lineno=35,
          tokens=15,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body="public function down()\n\t{\n\t\tSchema::drop('users');\n\t}"),
 Fragment(document_cs='38d0f07e1eaca26029aa7a0850a75e0d43d2b6dfe89ee9b51f4ee24ba99d2d8e',
          id=93,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: CreateUsersTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='394d3409643283ec1fd6ee6f548de8ca386ef6309152ced5a2e4e8fbb130380a',
          id=94,
          lineno=6,
          tokens=2,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='openModule',
          body='openModule'),
 Fragment(document_cs='394d3409643283ec1fd6ee6f548de8ca386ef6309152ced5a2e4e8fbb130380a',
          id=95,
          lineno=17,
          tokens=2,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='closeModule',
          body='closeModule'),
 Fragment(document_cs='394d3409643283ec1fd6ee6f548de8ca386ef6309152ced5a2e4e8fbb130380a',
          id=96,
          lineno=6,
          tokens=81,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='openModule',
          body='openModule = function(){\n'
               "\tvar module = $('div#module');\n"
               '    var top = $(document).scrollTop();\n'
               '\tmodule.height( $(document).height() );\n'
               '\tmodule.width( $(document).width() );\n'
               '\tmodule.fadeIn();\n'
               "    $('.module-form').css('margin-top', top);\n"
               "    $('#close').css('margin-top', top + 20);\n"
               "    $('body').addClass('stop-scrolling');\n"
               '}'),
 Fragment(document_cs='394d3409643283ec1fd6ee6f548de8ca386ef6309152ced5a2e4e8fbb130380a',
          id=97,
          lineno=7,
          tokens=7,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='module',
          body="module = $('div#module')"),
 Fragment(document_cs='394d3409643283ec1fd6ee6f548de8ca386ef6309152ced5a2e4e8fbb130380a',
          id=98,
          lineno=8,
          tokens=7,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='top',
          body='top = $(document).scrollTop()'),
 Fragment(document_cs='394d3409643283ec1fd6ee6f548de8ca386ef6309152ced5a2e4e8fbb130380a',
          id=99,
          lineno=17,
          tokens=45,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='closeModule',
          body='closeModule = function(){\n'
               "\tvar module \t\t= $('div#module');\n"
               "\tvar moduleForm \t= $('.module-form');\n"
               '\tmodule.fadeOut();\n'
               '\tmoduleForm.fadeOut();\n'
               "    $('body').removeClass('stop-scrolling');\n"
               '}'),
 Fragment(document_cs='394d3409643283ec1fd6ee6f548de8ca386ef6309152ced5a2e4e8fbb130380a',
          id=100,
          lineno=18,
          tokens=9,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='module',
          body="module \t\t= $('div#module')"),
 Fragment(document_cs='394d3409643283ec1fd6ee6f548de8ca386ef6309152ced5a2e4e8fbb130380a',
          id=101,
          lineno=19,
          tokens=9,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='moduleForm',
          body="moduleForm \t= $('.module-form')"),
 Fragment(document_cs='394d3409643283ec1fd6ee6f548de8ca386ef6309152ced5a2e4e8fbb130380a',
          id=102,
          lineno=1,
          tokens=26,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: closeModule openModule\n'
               '  Variables: closeModule module moduleForm openModule top\n'
               '  Usages: document\n'),
 Fragment(document_cs='3a3afb1490aacbb1f34de90662a1d87190105c32afb446e9cc39cd8024ad1970',
          id=103,
          lineno=6,
          tokens=145,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AddUrlsToProjectsTable',
          body='class AddUrlsToProjectsTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::table('projects', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->string('production');\n"
               "\t\t\t$table->string('stage');\n"
               "\t\t\t$table->string('dev');\n"
               "\t\t\t$table->string('github');\n"
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::table('projects', function(Blueprint $table)\n"
               '\t\t{\n'
               '\t\t\t'
               "$table->dropColumn(['production','stage','dev','github']);\n"
               '\t\t});\n'
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='3a3afb1490aacbb1f34de90662a1d87190105c32afb446e9cc39cd8024ad1970',
          id=104,
          lineno=13,
          tokens=58,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::table('projects', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->string('production');\n"
               "\t\t\t$table->string('stage');\n"
               "\t\t\t$table->string('dev');\n"
               "\t\t\t$table->string('github');\n"
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='3a3afb1490aacbb1f34de90662a1d87190105c32afb446e9cc39cd8024ad1970',
          id=105,
          lineno=29,
          tokens=41,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '\t{\n'
               "\t\tSchema::table('projects', function(Blueprint $table)\n"
               '\t\t{\n'
               '\t\t\t'
               "$table->dropColumn(['production','stage','dev','github']);\n"
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='3a3afb1490aacbb1f34de90662a1d87190105c32afb446e9cc39cd8024ad1970',
          id=106,
          lineno=1,
          tokens=21,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: AddUrlsToProjectsTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='3ad4b42e6c3b9435a6f30f5e1ec4f96ffa98c7f5d0ba79af588a47c845bcb85d',
          id=107,
          lineno=6,
          tokens=133,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CreateProjectsTable',
          body='class CreateProjectsTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::create('projects', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->integer('user_id');\n"
               "\t\t\t$table->integer('client_id');\n"
               "\t\t\t$table->string('name');\n"
               "\t\t\t$table->text('description');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::drop('projects');\n"
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='3ad4b42e6c3b9435a6f30f5e1ec4f96ffa98c7f5d0ba79af588a47c845bcb85d',
          id=108,
          lineno=13,
          tokens=74,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::create('projects', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->integer('user_id');\n"
               "\t\t\t$table->integer('client_id');\n"
               "\t\t\t$table->string('name');\n"
               "\t\t\t$table->text('description');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='3ad4b42e6c3b9435a6f30f5e1ec4f96ffa98c7f5d0ba79af588a47c845bcb85d',
          id=109,
          lineno=32,
          tokens=15,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '\t{\n'
               "\t\tSchema::drop('projects');\n"
               '\t}'),
 Fragment(document_cs='3ad4b42e6c3b9435a6f30f5e1ec4f96ffa98c7f5d0ba79af588a47c845bcb85d',
          id=110,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: CreateProjectsTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=111,
          lineno=1,
          tokens=207,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// DEFAULT COLORS\n'
               '$background-color: #f2f4f3;\n'
               '$color-primary-light: #26b2ad;\n'
               '$color-primary-dark: #3e3e3e;\n'
               '$color-primary-dark-two: #333545;\n'
               '$color-mint: #e1f2f1;\n'
               '$color-badge: #10e1c2;\n'
               '$color-panel-heading: #d3dddf;\n'
               '$color-default-grey: #ebefef;\n'
               '$color-default-text: #444;\n'
               '\n'
               '// GLOBALS\n'
               'html,body{\n'
               "\tfont-family: 'Open Sans', sans-serif;;\n"
               '\tfont-size: 14px;\n'
               '\theight: 100%;\n'
               '\tcolor: $color-default-text;\n'
               '\tbackground-color: $background-color;\n'
               '}\n'
               '\n'
               'h1,h2,h3,h4,h5,h6{\n'
               "\tfont-family: 'Open Sans light', sans-serif;\n"
               '\tfont-weight: 300;\n'
               '}\n'
               '\n'
               'a{\n'
               '  color: $color-primary-light\n'
               '}\n'
               'a:hover{\n'
               '  text-decoration: none;\n'
               '  color: $color-primary-dark;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=112,
          lineno=33,
          tokens=223,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '// Inputs\n'
               'input.form-control{\n'
               '    padding: 10px 12px;\n'
               '\theight: auto;\n'
               '}\n'
               'input.form-control:focus,\n'
               'textarea.form-control:focus{\n'
               '\tbox-shadow: none;\n'
               '\tborder-color: $color-primary-light;\n'
               '}\n'
               '\n'
               'img{\n'
               '  max-width: 100%;\n'
               '}\n'
               '\n'
               '.label-default{\n'
               '  font-size: 1em;\n'
               '}\n'
               '\n'
               '// Helpers\n'
               '.color-primary{color: $color-primary-light}\n'
               '.color-badge{color: $color-badge}\n'
               '\n'
               '.no-padding-left{padding-left: 0}\n'
               '.no-padding-right{padding-right: 0}\n'
               '.no-side-padding{padding-left: 0; padding-right: 0}\n'
               '\n'
               '.show-on-hover{display: none}\n'
               '\n'
               '// Messages\n'
               '.status-msg{\n'
               '  padding: 10px;\n'
               '  display:block;\n'
               '  text-align: center;\n'
               '  margin-bottom: 5px;\n'
               '  color: #fff;\n'
               '}\n'
               '.status-msg.error-msg{background-color: rgb(239, 130, 130)};\n'
               '.status-msg.success-msg{background-color: #48D0BE};\n'
               '\n'
               '.noScroll{\n'
               '  overflow-y:hidden;\n'
               '}\n'
               '\n'
               '.dim{\n'
               '\topacity: .5;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=113,
          lineno=81,
          tokens=59,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '.circle{\n'
               '  border-radius: 100%;\n'
               '}\n'
               '// Weight\n'
               '.weight{\n'
               '\tbackground-color: $color-badge; \n'
               '\tcolor: #4f4055;\n'
               '\tpadding: 2px 8px;\n'
               '    border-radius: 15px;\t\n'
               '    font-size: 14px;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=114,
          lineno=93,
          tokens=244,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '// Panel\n'
               '.panel{\n'
               '\tbox-shadow: none;\n'
               '\t-webkit-box-shadow: none;\n'
               '\t-moz-box-shadow: none;\n'
               '}\n'
               '.panel .panel-heading{\n'
               '\tbackground-color: $color-panel-heading;\n'
               '\tcolor: rgba(100,100,100,.8);\n'
               '\tfont-size: 1.3em; \n'
               '\tpadding: 15px;\n'
               '}\n'
               '.panel.panel-list .panel-body{\n'
               '\tpadding: 0;\n'
               '}\n'
               '.panel.panel-list a{\n'
               '\tdisplay: block;\n'
               '\tpadding: 8px 25px;\n'
               '\tborder-left: 4px solid #fff;\n'
               '\ttransition-duration: .2s;\n'
               '\tcolor: #333;\n'
               '\tfont-size: 1em;\n'
               '\tborder-bottom: 1px solid #e0e9e8;\n'
               '}\n'
               '.panel.panel-list a:hover{\n'
               '\tborder-left-color: $color-primary-light;\n'
               '\tbackground-color: #fafafa;\n'
               '\ttext-decoration: none;\n'
               '}\n'
               '.panel.panel-list a.with-number{\n'
               '  padding-left: 10px;\n'
               '}\n'
               '.panel.panel-list a.with-number .dim{\n'
               '  font-size: .7em;\n'
               '}\n'
               '.panel.panel-list .panel-body p{\n'
               '\tmargin-bottom: 0;\n'
               '\tpadding: 10px;\n'
               '}\n'
               '\n'
               '// SIDE NAV SECTION\n'
               '$side-nav-padding: 20px;\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=115,
          lineno=136,
          tokens=213,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='.side-nav{\n'
               '\tposition: fixed;\n'
               '\ttop: 0;\n'
               '\tleft: 0;\n'
               '\twidth: 250px;\n'
               '\theight: 100%;\n'
               '\tbackground-color: $color-primary-dark;\n'
               '\tcolor: rgba(150,150,150,.2);\n'
               '}\n'
               '.side-nav a{\t\n'
               '\tcolor: rgba(150,150,150,.6);\t\n'
               '\ttransition-duration: .2s;\t\n'
               '}\n'
               '.side-nav a:hover{\n'
               '\tcolor: #fff;\n'
               '\ttext-decoration: none;\n'
               '}\n'
               '.side-nav .logo-section{\n'
               '\tdisplay: block;\n'
               '\tpadding: 10px 25px;\t\n'
               "\tfont-family: 'Pacifico', cursive;\t\n"
               '\tfont-size: 1.5em;\t\n'
               '\ttext-align: left;\t\n'
               '\tbackground-color: $color-primary-light;\t\n'
               '}\n'
               '.side-nav .logo-section p{color: #fff; margin-bottom: 0}\n'
               '.side-nav .logo-section p:hover{text-decoration: none}\n'
               '.side-nav .user-section{padding: 25px; text-align: center;}\n'
               '.side-nav .user-section p{color: #fff; text-align: '),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=116,
          lineno=164,
          tokens=211,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='center;}\n'
               '.side-nav .user-section img{\n'
               '\twidth: 40px;\n'
               '    height: 40px;\n'
               '    border-radius: 100%;\n'
               '    display: block;\n'
               '    margin: 0 auto;\t\n'
               '}\n'
               '.side-nav .search input{\n'
               '\tborder-radius: 0;\n'
               '    border: none;\n'
               '    background-color: rgba(150,150,150,.2);\n'
               '    padding: 10px 20px;\n'
               '    color: #fff;\n'
               '}\n'
               '.side-nav .search input:focus{\n'
               '\t-moz-box-shadow: none;\n'
               '\t-webkit-box-shadow: none;\n'
               '\tbox-shadow: none;\n'
               '}\n'
               '.side-nav .menu h3{\n'
               '\tfont-size: 1.2em;\n'
               '\tpadding-left: $side-nav-padding;\n'
               '\tpadding-right: $side-nav-padding;\n'
               '\tcolor: rgba(150,150,150,.6);\n'
               '}\n'
               '.side-nav .menu a{\n'
               '\tdisplay: block;\n'
               '\tfont-size: .95em;\n'
               '\tbox-sizing: border-box;\t\n'
               '\tpadding: 6px 16px;\n'
               '\tborder-left: 4px solid $color-primary-dark;\t\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=117,
          lineno=196,
          tokens=215,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='}\n'
               '.side-nav .menu a:hover,\n'
               '.side-nav .menu a.active{\n'
               '\tborder-left: 4px solid $color-primary-light;\n'
               '\tcolor: #fff;\t\n'
               '}\n'
               '.side-nav .menu a:last-child{margin-top: 20px;}\n'
               '.side-nav .line{\n'
               '    padding-left: $side-nav-padding;\n'
               '    padding-right: $side-nav-padding;\t\n'
               '}\n'
               '.side-nav .menu a i{\n'
               '\tdisplay: inline-block;\n'
               '\twidth: 20px;\n'
               '\tfont-size: 1.3em;\n'
               '\tpadding-right: 10px;\n'
               '}\n'
               '.side-nav .menu a:last-child i{\n'
               '\tposition: relative;\n'
               '\ttop: 1px;\n'
               '}\n'
               '.side-nav .line hr{\n'
               '\tborder-top: none;\n'
               '    height: 2px;\n'
               '    background-color: rgba(150,150,150,.1);\n'
               '    margin-top: 40px;\n'
               '}\n'
               '.side-nav .footer{\n'
               '\tpadding-left: $side-nav-padding;\n'
               '\tpadding-right: $side-nav-padding;\n'
               '}\n'
               '.side-nav .footer {text-align: center}\n'
               '.side-nav .footer p{font-size: .8em}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=118,
          lineno=229,
          tokens=236,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '// Buttons\n'
               '.btn{\n'
               '\tpadding: 10px 20px;\n'
               '\tborder: none;\n'
               '\ttransition-duration: .2s;\n'
               '\t-webkit-box-shadow: 0 1px 1px rgba(0,0,0,.3);\n'
               '\t-moz-box-shadow: 0 1px 1px rgba(0,0,0,.3);\n'
               '\tbox-shadow: 0 1px 1px rgba(0,0,0,.3);\n'
               '}\n'
               '.btn:hover{\n'
               '\topacity: .95;\n'
               '}\n'
               '.btn:focus,\n'
               '.btn:active{\n'
               '  outline: none;\n'
               '  border: none;\n'
               '}\n'
               '.btn.btn-wide{\n'
               '  width: 100%;\n'
               '}\n'
               '.btn-default{\n'
               '  background-color: $color-default-grey;\n'
               '}\n'
               '.btn.btn-primary{\n'
               '\tbackground-color: $color-primary-light;\n'
               '}\n'
               '.btn.btn-primary.btn-line{\n'
               '  color: $color-primary-light;\n'
               '  border: 1px solid $color-primary-light;\n'
               '  background: transparent;\n'
               '  box-shadow: none;\n'
               '}\n'
               '.btn.btn-primary.btn-line:hover{\n'
               '  background-color: $color-primary-light;\n'
               '  color: #fff;\n'
               '}\n'
               '.btn-special{\n'
               '  background-color :#f81280;\n'
               '  '),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=119,
          lineno=268,
          tokens=228,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='color: #fff;\n'
               '  font-size: 1.5em;\n'
               '  font-weight: lighter;\n'
               '  letter-spacing: 1px;\n'
               '  padding: 20px 130px;\n'
               '  margin-top: 40px;\n'
               '}\n'
               '.btn-special:hover{\n'
               '\tbackground-color: #d11264;\n'
               '\tcolor: #fff;\n'
               '}\n'
               '// Pop Up Form\n'
               '.popup-form{\n'
               '\tposition: fixed;\n'
               '\tbottom: 0;\n'
               '\tright: 20px;\n'
               '\twidth: 400px;\n'
               '\tmax-width: 400px;\n'
               '\tbackground-color: #fff;\n'
               '\tbox-shadow: 0 2px 10px rgba(50,50,50,.4);\n'
               '\t-webkit-box-shadow: 0 2px 10px rgba(50,50,50,.4);\n'
               '\t-moz-box-shadow: 0 2px 10px rgba(50,50,50,.4);\n'
               '\tdisplay: none;\n'
               '}\n'
               '.popup-form header{\n'
               '\tpadding: 10px;\n'
               '\tbackground: $color-primary-dark;\n'
               '\tcolor: #fff;\n'
               '}\n'
               '.popup-form header p{\n'
               '\tmargin-bottom: 0;\n'
               '}\n'
               '.popup-form header .actions i{\n'
               '\tcolor: '),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=120,
          lineno=301,
          tokens=179,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#fff;\t\n'
               '\ttransition-duration: .2s;\n'
               '\topacity: .8;\n'
               '}\n'
               '.popup-form header .actions i:hover{\n'
               '\topacity: 1;\n'
               '\tcursor: pointer;\n'
               '}\n'
               '.popup-form header .actions i:nth-child(1){\n'
               '\tmargin-right: 10px;\n'
               '}\n'
               '.popup-form.minimized{\n'
               '\ttransition-duration: .3s;\n'
               '\theight: 40px !important;\n'
               '}\n'
               '.popup-form section{\n'
               '\tpadding: 10px;\n'
               '    padding-bottom: 60px;\n'
               '}\n'
               '.popup-form footer{\n'
               '\twidth: 100%;\n'
               '\tpadding: 10px;\n'
               '\tposition: absolute;\n'
               '\tbottom: 0;\n'
               '\tbackground-color: #f2f4f3;\n'
               '}\n'
               '.popup-form.minimized footer{\n'
               '\tposition: static;\n'
               '}\n'
               '.popup-form .form-control{\n'
               '  margin-bottom: 10px;\n'
               '}\n'
               '.popup-form.new-task,\n'
               '.popup-form.update-task{\n'
               '  height: 450px;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=121,
          lineno=337,
          tokens=221,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '// Mega Menu\n'
               '.mega-menu .links{\n'
               '\tfloat: left;\n'
               '\twidth: 30%;\n'
               '\tposition: relative;\n'
               '\tleft: 1px;\n'
               '}\n'
               '.mega-menu .links a{\n'
               '\tdisplay: block;\n'
               '\tpadding: 15px;\n'
               '\tfont-size: 1.2em;\n'
               '\ttext-decoration: none;\n'
               '\tcolor: #999c9b;\n'
               '\tborder-left: 4px solid transparent;\n'
               '}\n'
               '.mega-menu .links a.active,\n'
               '.mega-menu .links a:hover,\n'
               '.mega-menu .links a:first-child{\n'
               '\tborder-left-color: $color-primary-light;\n'
               '\tcolor: $color-default-text;\n'
               '}\n'
               '.mega-menu .links a.active,\n'
               '.mega-menu .links a:first-child{\n'
               '\t//border-top: 1px solid #cdcdd4;\n'
               '\tborder-bottom: 1px solid #cdcdd4;\t\n'
               '\t//font-weight: bold;\n'
               '\tbackground-color: #fff;\n'
               '}\n'
               '.mega-menu .links a.inactive{\n'
               '\tborder-top: none;\n'
               '\tborder-bottom: none;\t\n'
               '\tborder-left: 4px solid transparent;\n'
               '\tcolor: #999c9b;\n'
               '\tfont-weight: '),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=122,
          lineno=371,
          tokens=222,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='normal;\n'
               '\tbackground-color: transparent;\t\n'
               '}\n'
               '.mega-menu .links a.inactive:hover{\n'
               '\tborder-left-color: $color-primary-light;\n'
               '\tcolor: $color-default-text;\t\n'
               '}\n'
               '.mega-menu .content{\n'
               '\tfloat: left;\n'
               '\twidth: 70%;\n'
               '\tpadding: 10px;\n'
               '\tbackground-color: #fff;\n'
               '\t//border: 1px solid #cdcdd4;\n'
               '\tmin-height: 500px;\n'
               '}\n'
               '.mega-menu .content .item{\n'
               '\tdisplay: none;\n'
               '}\n'
               '.mega-menu .content .item:first-child{\n'
               '\tdisplay: block;\n'
               '}\n'
               '.mega-menu .content header{\n'
               '    line-height: .8;\n'
               '}\n'
               '.mega-menu .content header h2{\n'
               '    height: 40px;\n'
               '\tmargin-top: 5px;\n'
               '    margin-bottom: 15px;\n'
               '\ttransition-duration: .2s;\n'
               '    line-height: 2;\n'
               '}\n'
               '.mega-menu .content header i{\n'
               '\tcolor: #333;\n'
               '}\n'
               '.mega-menu .content header i:hover{\n'
               '\topacity: .9;\n'
               '\tcursor: pointer;\n'
               '}\n'
               '.mega-menu .content header p{\n'
               '\tfont-style: italic;\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=123,
          lineno=411,
          tokens=235,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='}\n'
               '.mega-menu .content header .client-update-form{\n'
               '\tdisplay: none;\n'
               '}\n'
               '.mega-menu .content header .client-update-form input{\n'
               '  border: 1px solid rgba(50,50,50,.2);\n'
               '  padding: 21px 10px;\n'
               '  background-color: transparent;\n'
               '  color: #fff;\n'
               '  margin-top: 5px;\n'
               '}\n'
               '.mega-menu .content header .client-update-form input:focus{\n'
               '  border-color: #fff;\n'
               '}\n'
               '.mega-menu .content .panel{\n'
               '    margin-top: 10px;\n'
               '    box-shadow: none;\n'
               '    border: none;\t\n'
               '}\n'
               '.mega-menu.mega-menu-tab .links{\n'
               '\tfloat: none;\n'
               '\twidth: auto;\n'
               '    min-height: 56px;\n'
               '    position: relative;\n'
               '    z-index: 2;\n'
               '}\n'
               '.mega-menu.mega-menu-tab .links a{\n'
               '\tfloat: left;\n'
               '    border-left: 1px solid transparent;\n'
               '    border-bottom: none;\n'
               '}\n'
               '.mega-menu .links a.inactive:hover{\n'
               '  border-left-color: transparent;\n'
               '}\n'
               '.mega-menu.mega-menu-tab .content{\n'
               '  float: none;\n'
               '  width: '),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=124,
          lineno=447,
          tokens=88,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='auto;\n'
               '  position: relative;\n'
               '  top: -3px;\n'
               '  left: 1px;\n'
               '  z-index: 1;\n'
               '  background-color: #fff;\n'
               '}\n'
               '\n'
               '.client.page-title-section{\n'
               '\theight: 70px;\n'
               '}\n'
               '\n'
               '.task-list-row,\n'
               '.task-list-row .col-md-4,\n'
               '.mega-menu.mega-menu-tab .content .item{\n'
               '  height: 100%;\n'
               '  min-height: 500px;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=125,
          lineno=465,
          tokens=237,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '.task-list{\n'
               '  padding: 15px 0;\n'
               '  margin-bottom: 0;\n'
               '  border-radius: 5px;\n'
               '  max-height: 500px;\n'
               '  min-height: 500px;\n'
               '  overflow-y: auto;\n'
               '  list-style: none;\n'
               '  background-color: #fff;\n'
               '}\n'
               '.task-list .title{\n'
               '  text-align: center;\n'
               '  padding-bottom: 10px;\n'
               '  border-bottom: 1px solid rgba(250,250,250,.2);\n'
               '  color: #ccc;\n'
               '}\n'
               '.task-list li{\n'
               '  padding: 10px;\n'
               '  transition-duration: .2s;\n'
               '  background-color: #F2F4F3;\n'
               '  color: #777;\n'
               '  margin-top: 5px;\n'
               '}\n'
               '.task-list li:hover{opacity: .9; cursor: pointer}\n'
               '.task-list li .show-on-hover{opacity: 0;}\n'
               '.task-list li:hover .show-on-hover{opacity: 1; display: '
               'inline-block}\n'
               '.task-list li span{transition-duration: .2s;}\n'
               '.task-list li span:hover{opacity: .7;}\n'
               '.task-list li span:first-child{margin-right: 5px}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=126,
          lineno=495,
          tokens=210,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '.task-list.backlog li{\n'
               '  margin-bottom: 20px;\n'
               '}\n'
               '.task-list.backlog li:nth-child(2),\n'
               '.task-list.backlog li:nth-child(3),\n'
               '.task-list.backlog li:nth-child(4){\n'
               '  margin-top: 0;\n'
               '}\n'
               '\n'
               '.priority-circle{\n'
               '  display: inline-block;\n'
               '  width: 13px;\n'
               '  height: 13px;\n'
               '  border-radius: 100%;\n'
               '}\n'
               '.priority-low{background-color: #00BCD4}\n'
               '.priority-normal{background-color: #2196F3}\n'
               '.priority-medium{background-color: #e167ff}\n'
               '.priority-high{background-color: #FF9800}\n'
               '.priority-highest{background-color: #ff4559}\n'
               '// SHEET AND PROMPT\n'
               '#sheet{\n'
               '  position: absolute;\n'
               '  top: 0;\n'
               '  left: 0;\n'
               '  z-index: 100;\n'
               '  width: 100%;\n'
               '  height: 100%;\n'
               '  background-color: $color-primary-dark;\n'
               '  opacity: .9;\n'
               '  display: none;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=127,
          lineno=528,
          tokens=217,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '#pop-up-prompt{\n'
               '  position: absolute;\n'
               '  left: 0;\n'
               '  right: 0;\n'
               '  z-index: 150;\n'
               '  width: 100%;\n'
               '  min-height: 400px;\n'
               '  margin: 0 auto;\n'
               '  color: #fff;\n'
               '  display: none;\n'
               '  text-align: center;\n'
               '}\n'
               '#pop-up-prompt h4{\n'
               '  margin-top: 30px;\n'
               '}\n'
               '#pop-up-prompt section{\n'
               '  margin-top: 40px;\n'
               '}\n'
               '#pop-up-prompt section .btn{\n'
               '  display: block;\n'
               '  border-top: 1px solid rgba(250,250,250,.2);\n'
               '  border-radius: 0;\n'
               '  color: rgba(250,250,250,.2);\n'
               '}\n'
               '#pop-up-prompt section .btn:last-child{\n'
               '  border-bottom: 1px solid rgba(250,250,250,.2);\n'
               '}\n'
               '#pop-up-prompt section .btn:hover{\n'
               '  color: #fff;\n'
               '  background-color: rgba(250,250,250,.1);\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=128,
          lineno=560,
          tokens=234,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '// CONTENT AREA\n'
               '.content-area{\n'
               '    padding: 20px;    \t\n'
               '    margin-left: 260px;\n'
               '\tmin-height: 100%;    \n'
               '    border-top: 5px solid $color-primary-light;\n'
               '}\n'
               '\n'
               '.page-title-section > h1{\n'
               '\theight: 50px;\n'
               '}\n'
               '.page-title-section .btn.btn-primary{\n'
               '\tmargin-top: 10px;\n'
               '\tmargin-left: 10px;\n'
               '}\n'
               '.page-title-section:hover .show-on-hover{\n'
               '\tdisplay: inline-block;\n'
               '}\n'
               '\n'
               '.page-title-section .label{\n'
               '  margin-left: 5px;\n'
               '}\n'
               '\n'
               '// SETTINGS\n'
               '.settings-container section{\n'
               '  overflow: auto;\n'
               '}\n'
               '\n'
               '.settings-container .left-side{\n'
               '  background-color: $color-primary-dark;\n'
               '  padding: 10px 20px;\n'
               '  height: 600px;\n'
               '}\n'
               '\n'
               '.settings-container .left-side .info{\n'
               '  float: left;\n'
               '  padding: 10px 0 10px 10px;\n'
               '}\n'
               '\n'
               '.settings-container .left-side .info p{\n'
               '  margin-bottom: 0;\n'
               '}\n'
               '\n'
               '.settings-container .left-side .info p.name{\n'
               '  color: #fff;\n'
               '}\n'
               '\n'
               '.settings-container .left-side a{\n'
               '  float: left;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=129,
          lineno=611,
          tokens=242,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '.settings-container .left-side .bio{\n'
               '  color: #fff;\n'
               '  font-size: 1.1em;\n'
               '  line-height: 2;\n'
               '  text-align: center;\n'
               '}\n'
               '\n'
               '.settings-container .left-side hr{\n'
               '  border-top: none;\n'
               '  height: 2px;\n'
               '  background-color: rgba(150,150,150,.1);\n'
               '}\n'
               '\n'
               '.settings-container .left-side .links a{\n'
               '  float: none;\n'
               '  color: rgba(150, 150, 150, 0.6);\n'
               '  transition-duration: .2s;\n'
               '}\n'
               '\n'
               '.settings-container .left-side .links a:hover{\n'
               '  color: #fff;\n'
               '}\n'
               '\n'
               '.settings-container .left-side .links span{\n'
               '  display: inline-block;\n'
               '  width: 13px;\n'
               '}\n'
               '\n'
               '.settings-container .right-side{\n'
               '  padding-left: 5px;\n'
               '}\n'
               '\n'
               '.settings-container .right-side .mega-menu{\n'
               '  padding-top: 50px;\n'
               '}\n'
               '.progress{\n'
               '  background-color: #CECECE;\n'
               '  border-radius: 0;\n'
               '}\n'
               '.progress-bar{\n'
               '  background-color: $color-primary-light;\n'
               '  -webkit-box-shadow: none;\n'
               '  -moz-box-shadow: none;\n'
               '  box-shadow: none;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=130,
          lineno=657,
          tokens=92,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '.table .progress{\n'
               '  margin-bottom: 0;\n'
               '}\n'
               '\n'
               '.credential-form .form-group.type-0{\n'
               '  display: none;\n'
               '}\n'
               '\n'
               '// Table\n'
               '.table>thead>tr>th, \n'
               '.table>tbody>tr>th, \n'
               '.table>tfoot>tr>th, \n'
               '.table>thead>tr>td, \n'
               '.table>tbody>tr>td, \n'
               '.table>tfoot>tr>td{\n'
               '  border-top: none;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=131,
          lineno=675,
          tokens=210,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '// Login and register\n'
               '.special-form{\n'
               '\tmax-width: 500px;\n'
               '\tmargin: 5% auto 0;\n'
               '\tbackground-color: #393d4e;\n'
               '\tpadding: 10px;\n'
               '\tborder-radius: 10px;\n'
               '\tbox-shadow: 0 3px 5px rgba(50,50,50,.2);\n'
               '\tcolor: #fff;\n'
               '}\n'
               '.special-form img{\n'
               '  max-width: 100%;\n'
               '  width: 150px;\n'
               '  display: block;\n'
               '  margin: 0 auto;\n'
               '}\n'
               '.special-form hr{\n'
               '\topacity: .1;\n'
               '}\n'
               '.special-form input{\n'
               '  padding: 15px 25px;\n'
               '}\n'
               '.special-form .btn{\n'
               '  padding: 20px;\n'
               '}\n'
               '.special-form a:hover{\n'
               '\tcolor: $color-primary-light;\n'
               '\ttext-decoration: underline;\n'
               '}\n'
               '\n'
               '// Home page\n'
               '.hug{width: 100%}\n'
               '\n'
               '.hug-header{\n'
               '  background-color: #fff;\n'
               '}\n'
               '\n'
               '.hug-header img{\n'
               '  max-width: 125px;\n'
               '  padding: 10px 0;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=132,
          lineno=717,
          tokens=242,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '.hug-header .btn{\n'
               '  font-size: 1.2em;\n'
               '  margin-top: 35px;\n'
               '  min-width: 130px;\n'
               '}\n'
               '.hug-header .btn.register{\n'
               '  margin-right: 20px;\n'
               '}\n'
               '\n'
               '.hug-hero .left-side,\n'
               '.hug-hero .right-side{\n'
               '  width: 50%;\n'
               '  float: left;\n'
               '}\n'
               '\n'
               '.hug-hero{\n'
               '  background: url("/assets/img/hero_screen.png") no-repeat;\n'
               '  background-size: cover;\n'
               '  min-height: 730px;\n'
               '  padding-top: 150px;\n'
               '}\n'
               '.hug-hero .left-side h1{\n'
               "  font-family: 'parmapetitregular';\n"
               '  font-size: 7em;\n'
               '  text-transform: uppercase;\n'
               '  color: $color-primary-light;\n'
               '  line-height: .9;\n'
               '}\n'
               '\n'
               '.mascot{\n'
               '  max-width: 475px;\n'
               '}\n'
               '\n'
               '.hug-skyline{\n'
               '  background-color: $color-mint;\n'
               '  height: 350px;\n'
               '}\n'
               '.hug-skyline .skyline{\n'
               '  height: 350px;\n'
               '  background: url("/assets/img/skyline.png") no-repeat;\n'
               '  background-size: cover; ;\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=133,
          lineno=759,
          tokens=236,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='}\n'
               '.hug-features{\n'
               '  background-color: #393d4d;\n'
               '  padding: 50px 0 150px;\n'
               '  margin-top: -1px;\n'
               '}\n'
               '.hug-features h2{\n'
               '  color: #fff;\n'
               "  font-family: 'Lobster', cursive;\n"
               '  font-size: 3em;\n'
               '  margin-bottom: 50px;\n'
               '  text-transform: capitalize;\n'
               '  letter-spacing: 2px;\n'
               '}\n'
               '.hug-features i{\n'
               '  font-size: 6em;\n'
               '  color: $color-primary-light;\n'
               '}\n'
               '.hug-features h3{\n'
               '  margin-top: 0;\n'
               '  color: $color-primary-light;\n'
               '  text-transform: uppercase;\n'
               '  font-size: 1.4em;\n'
               '  letter-spacing: 1px;\n'
               '}\n'
               '.hug-features h3 .new{\n'
               '  color: #ffde00;\n'
               '}\n'
               '.hug-features p{\n'
               '  color: #fff;\n'
               '  line-height: 2;\n'
               '  letter-spacing: .2px;\n'
               '}\n'
               '.hug-features .feature.centered{\n'
               '  text-align: center;\n'
               '  float: none;\n'
               '  margin: 0 auto;\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=134,
          lineno=796,
          tokens=185,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='}\n'
               '.hug-info{\n'
               '  color: $color-primary-light;\n'
               '  padding-bottom: 290px;\n'
               '  position: relative;\n'
               '  background-color: #fff;\n'
               '  background-image: url("/assets/img/oval_bg.png");\n'
               '  background-repeat: no-repeat;\n'
               '  background-position: right 0 bottom 0;\n'
               '  background-size: contain;\n'
               '}\n'
               '.hug-info h2{\n'
               "  font-family: 'Lobster', cursive;\n"
               '  font-size: 7em;\n'
               '  text-transform: capitalize;\n'
               '  margin-top: -90px;\n'
               '}\n'
               '.hug-info h3{\n'
               '  font-size: 3em;\n'
               '}\n'
               '.hug-info .row img{\n'
               '  max-width: 100px;\n'
               '  margin: 20px;\n'
               '}\n'
               '.hug-info .arrow{\n'
               '  position: relative;\n'
               '  top: -60px;\n'
               '  max-width: 120px;\n'
               '  margin-bottom: 50px;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=135,
          lineno=826,
          tokens=128,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '.hug-ui{\n'
               '  background-color: #26b2ad;\n'
               '  color: #fff;\n'
               '}\n'
               '.hug-ui .text-bucket{\n'
               '  width: 60%;\n'
               '  margin: 0 auto;\n'
               '  padding-bottom: 50px;\n'
               '}\n'
               '.hug-ui h2{\n'
               '  font-size: 5em;\n'
               "  font-family: 'Lobster', cursive;\n"
               '  text-transform: capitalize;\n'
               '}\n'
               '.hug-ui h3{\n'
               '  font-size: 2.5em;\n'
               '}\n'
               '.hug-ui img{\n'
               '  border-top-right-radius: 10px;\n'
               '  border-top-left-radius: 10px;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=136,
          lineno=848,
          tokens=181,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '.hug-exit{\n'
               '  background-color: $color-primary-dark;\n'
               '  color: #fff;\n'
               '  text-align: center;\n'
               '  position: relative;\n'
               '}\n'
               '.hug-exit .img{\n'
               '  position: relative;\n'
               '  top: -150px;\n'
               '  max-width: 100%;\n'
               '  padding-bottom: 600px;\n'
               '  background-image: url("/assets/img/fantastic.png");\n'
               '  background-repeat: no-repeat;\n'
               '  background-size: 100%;\n'
               '}\n'
               '.hug-exit .img h2{\n'
               '  max-width: 50%;\n'
               '  display: block;\n'
               '  margin: 0 auto;\n'
               '  font-weight: bold;\n'
               '  text-transform: uppercase;\n'
               '  font-weight: lighter;\n'
               '  line-height: 1.3;\n'
               '}\n'
               '.hug-exit .img h2,\n'
               '.hug-exit .img a{\n'
               '  position: relative;\n'
               '  top: 400px;\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=137,
          lineno=878,
          tokens=242,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '.hug-footer{\n'
               '  background-color: $color-primary-dark;\n'
               '  color: rgba(200,200,200,.5);\n'
               '}\n'
               '.hug-footer hr{\n'
               '  border: none;\n'
               '  height: 1px;\n'
               '  margin-bottom: 10px;\n'
               '  background-color: rgba(200,200,200,.5);;\n'
               '}\n'
               '.hug-footer h3{\n'
               '  font-size: 1.5em;\n'
               '}\n'
               '.hug-footer hr.special{\n'
               '  background-color: $color-primary-light;\n'
               '}\n'
               '.hug-footer a{\n'
               '  color: $color-primary-light;\n'
               '}\n'
               '.hug-footer a:hover{\n'
               '  color: #fff;\n'
               '}\n'
               '.hug-footer .last-line{\n'
               '  padding: 50px 0;\n'
               '}\n'
               '\n'
               '.project-list-container{\n'
               '\tpadding: 10px;\n'
               '\tbackground-color: #fff;\n'
               '\tborder-radius: 4px;\n'
               '}\n'
               '\n'
               '// MEDIA QUERIES\n'
               '@media screen and (max-width: 991px) {\n'
               '  .hug-hero{\n'
               '    min-height: 530px;\n'
               '  }\n'
               '  .hug-hero .right-side{\n'
               '    display: none;\n'
               '  }\n'
               '  .hug-hero .left-side{\n'
               '    width: 100%;\n'
               '    text-align: center;\n'
               '  }\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=138,
          lineno=923,
          tokens=160,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  .hug-features{\n'
               '    text-align: center;\n'
               '  }\n'
               '\n'
               '  .hug-ui .text-bucket{\n'
               '    width: 100%;\n'
               '  }\n'
               '\n'
               '  .hug-exit .img{\n'
               '    background-image: none;\n'
               '    position: static;\n'
               '    padding-top: 50px;\n'
               '    padding-bottom: 100px;\n'
               '  }\n'
               '  .hug-exit .img h2, .hug-exit .img a{\n'
               '    position: static;\n'
               '    max-width: 100%;\n'
               '  }\n'
               '\n'
               '  .hug-footer{\n'
               '    text-align: center;\n'
               '    margin-top: -1px;\n'
               '  }\n'
               '}\n'
               '\n'
               '@media screen and (max-width: 770px) {\n'
               '  .hug-hero h1{\n'
               '    font-size: 7em;\n'
               '  }\n'
               '}\n'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=139,
          lineno=954,
          tokens=134,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '@media screen and (max-width: 600px) {\n'
               '  .hug-header .pull-left{\n'
               '      float: none !important;\n'
               '  }\n'
               '  .hug-header img{\n'
               '\t  display: block;\n'
               '\t  margin: 0 auto;\n'
               '  }\n'
               '  .hug-header .btn.register{\n'
               '    margin-right: 0;\n'
               '  }\n'
               '  .hug-header .btn{\n'
               '    width: 40%;\n'
               '    margin: 10px 6.6%;\n'
               '  }\n'
               '\n'
               '  .hug-hero h1{\n'
               '    font-size: 4em !important;\n'
               '  }\n'
               '\n'
               '  .btn-special{\n'
               '    padding: 20px 20%;\n'
               '  }\n'
               '}'),
 Fragment(document_cs='3cbae63abeda5a1776c2bd460f72d7a92d48761fdd3b213c15aaa5078312ab98',
          id=140,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='3e567ac417549c2329f802d4655110e38b218044d1b8fcff4fe24a2c6902d83b',
          id=141,
          lineno=8,
          tokens=166,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='RedirectIfAuthenticated',
          body='class RedirectIfAuthenticated\n'
               '{\n'
               '    /**\n'
               '     * The Guard implementation.\n'
               '     *\n'
               '     * @var Guard\n'
               '     */\n'
               '    protected $auth;\n'
               '\n'
               '    /**\n'
               '     * Create a new filter instance.\n'
               '     *\n'
               '     * @param  Guard  $auth\n'
               '     * @return void\n'
               '     */\n'
               '    public function __construct(Guard $auth)\n'
               '    {\n'
               '        $this->auth = $auth;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Handle an incoming request.\n'
               '     *\n'
               '     * @param  \\Illuminate\\Http\\Request  $request\n'
               '     * @param  \\Closure  $next\n'
               '     * @return mixed\n'
               '     */\n'
               '    public function handle($request, Closure $next)\n'
               '    {\n'
               '        if ($this->auth->check()) {\n'
               "            return redirect('/home');\n"
               '        }\n'
               '\n'
               '        return $next($request);\n'
               '    }\n'
               '}'),
 Fragment(document_cs='3e567ac417549c2329f802d4655110e38b218044d1b8fcff4fe24a2c6902d83b',
          id=142,
          lineno=23,
          tokens=22,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='__construct',
          body='public function __construct(Guard $auth)\n'
               '    {\n'
               '        $this->auth = $auth;\n'
               '    }'),
 Fragment(document_cs='3e567ac417549c2329f802d4655110e38b218044d1b8fcff4fe24a2c6902d83b',
          id=143,
          lineno=35,
          tokens=39,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='handle',
          body='public function handle($request, Closure $next)\n'
               '    {\n'
               '        if ($this->auth->check()) {\n'
               "            return redirect('/home');\n"
               '        }\n'
               '\n'
               '        return $next($request);\n'
               '    }'),
 Fragment(document_cs='3e567ac417549c2329f802d4655110e38b218044d1b8fcff4fe24a2c6902d83b',
          id=144,
          lineno=1,
          tokens=23,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: __construct handle\n'
               '  Classes: RedirectIfAuthenticated\n'
               '  Usages: auth next request this\n'),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=145,
          lineno=9,
          tokens=170,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Project',
          body='class Project extends Model {\n'
               '\tprotected $fillable = [\n'
               "\t\t\t'user_id',\n"
               "\t\t\t'client_id',\n"
               "\t\t\t'name',\n"
               "\t\t\t'description',\n"
               "\t\t\t'production',\n"
               "\t\t\t'stage',\n"
               "\t\t\t'dev',\n"
               "\t\t\t'github'\n"
               '\t\t];\n'
               '\tprotected $hidden = [\n'
               "\t\t\t'created_at',\n"
               "\t\t\t'updated_at'\n"
               '\t];\n'
               '\n'
               '\tpublic function tasks(){\n'
               "\t\treturn $this->hasMany('App\\Task', 'project_id');\n"
               '\t}\n'
               '\n'
               '\tpublic function credentials(){\n'
               "\t\treturn $this->hasMany('App\\Credential', 'project_id');\n"
               '\t}\n'
               '\n'
               '\tpublic function members(){\n'
               "\t\treturn $this->belongsToMany('App\\User');\n"
               '\t}\n'
               '\n'
               '    public function client(){\n'
               "        return $this->belongsTo('App\\Client');\n"
               '    }\n'
               '\n'
               '    public function uploads(){\n'
               "        return $this->hasMany('App\\Upload', 'project_id');\n"
               ' '),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=146,
          lineno=43,
          tokens=187,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Project',
          body='   }\n'
               '\n'
               '\t/**\n'
               '\t * Checks if teh currently Auth user\n'
               '\t * is the owner of the project.\n'
               '\t *\n'
               '\t * @return bool\n'
               '\t */\n'
               '\tpublic function isOwner(){\n'
               '\t\tif($this->user_id != Auth::id()){\n'
               '\t\t\treturn false;\n'
               '\t\t}\n'
               '\n'
               '\t\treturn true;\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Checks if the current Auth user\n'
               '\t * is a member of a given project.\n'
               '\t *\n'
               '\t * @return bool\n'
               '\t */\n'
               '\tpublic function isMember(){\n'
               '\n'
               '\t\t$s = '
               "DB::table('project_user')->whereProjectId($this->id)->whereUserId(Auth::id())->get();\n"
               '\t\tif(count($s) == 0){\n'
               '\t\t\treturn false;\n'
               '\t\t}\n'
               '\n'
               '\t\treturn true;\n'
               '\t}\n'
               '\n'
               '\t// Get the toal weight of the given project\n'
               '\tpublic function totalWeight(){\n'
               '\t\treturn '
               "$this->tasks()->where('state','!=','complete')->sum('weight');\n"
               '\t}\n'
               '}'),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=147,
          lineno=25,
          tokens=21,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='tasks',
          body='public function tasks(){\n'
               "\t\treturn $this->hasMany('App\\Task', 'project_id');\n"
               '\t}'),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=148,
          lineno=29,
          tokens=21,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='credentials',
          body='public function credentials(){\n'
               "\t\treturn $this->hasMany('App\\Credential', 'project_id');\n"
               '\t}'),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=149,
          lineno=33,
          tokens=17,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='members',
          body='public function members(){\n'
               "\t\treturn $this->belongsToMany('App\\User');\n"
               '\t}'),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=150,
          lineno=37,
          tokens=16,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='client',
          body='public function client(){\n'
               "        return $this->belongsTo('App\\Client');\n"
               '    }'),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=151,
          lineno=41,
          tokens=21,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='uploads',
          body='public function uploads(){\n'
               "        return $this->hasMany('App\\Upload', 'project_id');\n"
               '    }'),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=152,
          lineno=51,
          tokens=30,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='isOwner',
          body='public function isOwner(){\n'
               '\t\tif($this->user_id != Auth::id()){\n'
               '\t\t\treturn false;\n'
               '\t\t}\n'
               '\n'
               '\t\treturn true;\n'
               '\t}'),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=153,
          lineno=66,
          tokens=55,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='isMember',
          body='public function isMember(){\n'
               '\n'
               '\t\t$s = '
               "DB::table('project_user')->whereProjectId($this->id)->whereUserId(Auth::id())->get();\n"
               '\t\tif(count($s) == 0){\n'
               '\t\t\treturn false;\n'
               '\t\t}\n'
               '\n'
               '\t\treturn true;\n'
               '\t}'),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=154,
          lineno=77,
          tokens=26,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='totalWeight',
          body='public function totalWeight(){\n'
               '\t\treturn '
               "$this->tasks()->where('state','!=','complete')->sum('weight');\n"
               '\t}'),
 Fragment(document_cs='3e8ffdf8cc896e0d036be514c3b17c3e7c931101792ce8691b8b891809aaec2a',
          id=155,
          lineno=1,
          tokens=29,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: client credentials isMember isOwner members tasks '
               'totalWeight uploads\n'
               '  Classes: Project\n'
               '  Usages: fillable hidden this\n'),
 Fragment(document_cs='45765038c81bfbb93a7606a90f5b08881be705cb00d7890ee2194db000e2cafc',
          id=156,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='46dbcff7e256aadf758991f2bc689b635d44b877a9f54b6e449f93e012274cd9',
          id=157,
          lineno=8,
          tokens=190,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Authenticate',
          body='class Authenticate\n'
               '{\n'
               '    /**\n'
               '     * The Guard implementation.\n'
               '     *\n'
               '     * @var Guard\n'
               '     */\n'
               '    protected $auth;\n'
               '\n'
               '    /**\n'
               '     * Create a new filter instance.\n'
               '     *\n'
               '     * @param  Guard  $auth\n'
               '     * @return void\n'
               '     */\n'
               '    public function __construct(Guard $auth)\n'
               '    {\n'
               '        $this->auth = $auth;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Handle an incoming request.\n'
               '     *\n'
               '     * @param  \\Illuminate\\Http\\Request  $request\n'
               '     * @param  \\Closure  $next\n'
               '     * @return mixed\n'
               '     */\n'
               '    public function handle($request, Closure $next)\n'
               '    {\n'
               '        if ($this->auth->guest()) {\n'
               '            if ($request->ajax()) {\n'
               "                return response('Unauthorized.', 401);\n"
               '            } else {\n'
               "                return redirect()->guest('auth/login');\n"
               '            }\n'
               '        }\n'
               '\n'
               '        return $next($request);\n'
               '    }\n'
               '}'),
 Fragment(document_cs='46dbcff7e256aadf758991f2bc689b635d44b877a9f54b6e449f93e012274cd9',
          id=158,
          lineno=23,
          tokens=22,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='__construct',
          body='public function __construct(Guard $auth)\n'
               '    {\n'
               '        $this->auth = $auth;\n'
               '    }'),
 Fragment(document_cs='46dbcff7e256aadf758991f2bc689b635d44b877a9f54b6e449f93e012274cd9',
          id=159,
          lineno=35,
          tokens=65,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='handle',
          body='public function handle($request, Closure $next)\n'
               '    {\n'
               '        if ($this->auth->guest()) {\n'
               '            if ($request->ajax()) {\n'
               "                return response('Unauthorized.', 401);\n"
               '            } else {\n'
               "                return redirect()->guest('auth/login');\n"
               '            }\n'
               '        }\n'
               '\n'
               '        return $next($request);\n'
               '    }'),
 Fragment(document_cs='46dbcff7e256aadf758991f2bc689b635d44b877a9f54b6e449f93e012274cd9',
          id=160,
          lineno=1,
          tokens=21,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: __construct handle\n'
               '  Classes: Authenticate\n'
               '  Usages: auth next request this\n'),
 Fragment(document_cs='475591be8ee3bb2d99d4dd875bdc4acad4894de84a35cd858488469f5eccaee9',
          id=161,
          lineno=1,
          tokens=7,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Usages: compiledPath\n'),
 Fragment(document_cs='4a1fe24095a87783bb3fd337dd3b1f883230f8ccaf9299d52473b4fb7cf92ffa',
          id=162,
          lineno=14,
          tokens=199,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Helpers',
          body='class Helpers {\n'
               '\n'
               '\t// Return the image logo path\n'
               '\tstatic public function logoUrl(){\n'
               "\t\treturn asset('assets/img/logo.png');\n"
               '\t}\n'
               '\n'
               '\t// Checks if the given user is the owner of the project\n'
               '\tstatic function isOwner($project_id, $user_id = null) {\n'
               '\n'
               '\t\tif($user_id == null){\n'
               '\t\t\t$user_id = Auth::id();\n'
               '\t\t}\n'
               '\n'
               '\t\t$s = '
               'Project::whereId($project_id)->whereUserId($user_id)->get();\n'
               '\n'
               '\t\tif(count($s) == 0){\n'
               '\t\t\treturn false;\n'
               '\t\t}\n'
               '\n'
               '\t\treturn true;\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/*******************************\n'
               '\t\t\tMAIL FUNCTIONS\n'
               '\t********************************/\n'
               '\n'
               '\t// Send the welcome email to the user\n'
               '\tstatic function sendWelcomeMail() {\n'
               '\t\t$data = [\n'
               "\t\t\t\t'to' \t=> Auth::user()->email,\n"
               "\t\t\t\t'name' \t=> Auth::user()->full_name\n"
               '\t\t];\n'
               '\n'
               "\t\tMail::send('emails.welcome', [ 'name' =>"),
 Fragment(document_cs='4a1fe24095a87783bb3fd337dd3b1f883230f8ccaf9299d52473b4fb7cf92ffa',
          id=163,
          lineno=49,
          tokens=197,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Helpers',
          body=" $data['name'] ] , function($message) use ($data){\n"
               "\t\t\t$message->from(getenv('MAIL_FROM'), "
               "getenv('MAIL_FROM_NAME'));\n"
               "\t        $message->to($data['to'], $data['name'] "
               ")->subject('Welcome to Ribbbon');\n"
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\t/** Sends password changed email **/\n'
               '\n'
               '\t/** Sends account deletion email **/\n'
               '\n'
               '\t// Send project invite email\n'
               '\tstatic function sendProjectInviteMail($email, $project_name, '
               '$project_url) {\n'
               "\t\t$data = [ 'to' => $email ];\n"
               '\n'
               "\t\tMail::send('emails.projectInvite', [ 'project_url' => "
               "$project_url, 'project_name' => $project_name ] , "
               'function($message) use ($data) {\n'
               "\t\t\t$message->from(getenv('MAIL_FROM'), "
               "getenv('MAIL_FROM_NAME'));\n"
               "\t\t\t$message->to($data['to'], '')->subject('You have been "
               "invited to a new project');\n"
               '\t\t});\n'
               '\t}\n'
               '}'),
 Fragment(document_cs='4a1fe24095a87783bb3fd337dd3b1f883230f8ccaf9299d52473b4fb7cf92ffa',
          id=164,
          lineno=17,
          tokens=17,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='logoUrl',
          body='static public function logoUrl(){\n'
               "\t\treturn asset('assets/img/logo.png');\n"
               '\t}'),
 Fragment(document_cs='4a1fe24095a87783bb3fd337dd3b1f883230f8ccaf9299d52473b4fb7cf92ffa',
          id=165,
          lineno=22,
          tokens=78,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='isOwner',
          body='static function isOwner($project_id, $user_id = null) {\n'
               '\n'
               '\t\tif($user_id == null){\n'
               '\t\t\t$user_id = Auth::id();\n'
               '\t\t}\n'
               '\n'
               '\t\t$s = '
               'Project::whereId($project_id)->whereUserId($user_id)->get();\n'
               '\n'
               '\t\tif(count($s) == 0){\n'
               '\t\t\treturn false;\n'
               '\t\t}\n'
               '\n'
               '\t\treturn true;\n'
               '\t}'),
 Fragment(document_cs='4a1fe24095a87783bb3fd337dd3b1f883230f8ccaf9299d52473b4fb7cf92ffa',
          id=166,
          lineno=43,
          tokens=119,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='sendWelcomeMail',
          body='static function sendWelcomeMail() {\n'
               '\t\t$data = [\n'
               "\t\t\t\t'to' \t=> Auth::user()->email,\n"
               "\t\t\t\t'name' \t=> Auth::user()->full_name\n"
               '\t\t];\n'
               '\n'
               "\t\tMail::send('emails.welcome', [ 'name' => $data['name'] ] , "
               'function($message) use ($data){\n'
               "\t\t\t$message->from(getenv('MAIL_FROM'), "
               "getenv('MAIL_FROM_NAME'));\n"
               "\t        $message->to($data['to'], $data['name'] "
               ")->subject('Welcome to Ribbbon');\n"
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='4a1fe24095a87783bb3fd337dd3b1f883230f8ccaf9299d52473b4fb7cf92ffa',
          id=167,
          lineno=60,
          tokens=114,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='sendProjectInviteMail',
          body='static function sendProjectInviteMail($email, $project_name, '
               '$project_url) {\n'
               "\t\t$data = [ 'to' => $email ];\n"
               '\n'
               "\t\tMail::send('emails.projectInvite', [ 'project_url' => "
               "$project_url, 'project_name' => $project_name ] , "
               'function($message) use ($data) {\n'
               "\t\t\t$message->from(getenv('MAIL_FROM'), "
               "getenv('MAIL_FROM_NAME'));\n"
               "\t\t\t$message->to($data['to'], '')->subject('You have been "
               "invited to a new project');\n"
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='4a1fe24095a87783bb3fd337dd3b1f883230f8ccaf9299d52473b4fb7cf92ffa',
          id=168,
          lineno=1,
          tokens=36,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: isOwner logoUrl sendProjectInviteMail '
               'sendWelcomeMail\n'
               '  Classes: Helpers\n'
               '  Usages: data email message project_id project_name '
               'project_url user_id\n'),
 Fragment(document_cs='4c40a6787934b3b0076c6665473686ce74b80867dc0b215601bb419f8656f663',
          id=169,
          lineno=6,
          tokens=170,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CreateProjectUserTable',
          body='class CreateProjectUserTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::create('project_user', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->integer('project_id')->unsigned()->index();\n"
               '\t\t\t'
               "$table->foreign('project_id')->references('id')->on('projects')->onDelete('cascade');\n"
               "\t\t\t$table->integer('user_id')->unsigned()->index();\n"
               '\t\t\t'
               "$table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::drop('project_user');\n"
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='4c40a6787934b3b0076c6665473686ce74b80867dc0b215601bb419f8656f663',
          id=170,
          lineno=13,
          tokens=109,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::create('project_user', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->integer('project_id')->unsigned()->index();\n"
               '\t\t\t'
               "$table->foreign('project_id')->references('id')->on('projects')->onDelete('cascade');\n"
               "\t\t\t$table->integer('user_id')->unsigned()->index();\n"
               '\t\t\t'
               "$table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='4c40a6787934b3b0076c6665473686ce74b80867dc0b215601bb419f8656f663',
          id=171,
          lineno=32,
          tokens=16,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '\t{\n'
               "\t\tSchema::drop('project_user');\n"
               '\t}'),
 Fragment(document_cs='4c40a6787934b3b0076c6665473686ce74b80867dc0b215601bb419f8656f663',
          id=172,
          lineno=1,
          tokens=20,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: CreateProjectUserTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='4ca4fccde97862f16f87238df62642feb46df020e1364127f660906b0537e7f5',
          id=173,
          lineno=8,
          tokens=114,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Inspire',
          body='class Inspire extends Command\n'
               '{\n'
               '    /**\n'
               '     * The name and signature of the console command.\n'
               '     *\n'
               '     * @var string\n'
               '     */\n'
               "    protected $signature = 'inspire';\n"
               '\n'
               '    /**\n'
               '     * The console command description.\n'
               '     *\n'
               '     * @var string\n'
               '     */\n'
               "    protected $description = 'Display an inspiring quote';\n"
               '\n'
               '    /**\n'
               '     * Execute the console command.\n'
               '     *\n'
               '     * @return mixed\n'
               '     */\n'
               '    public function handle()\n'
               '    {\n'
               '        $this->comment(PHP_EOL.Inspiring::quote().PHP_EOL);\n'
               '    }\n'
               '}'),
 Fragment(document_cs='4ca4fccde97862f16f87238df62642feb46df020e1364127f660906b0537e7f5',
          id=174,
          lineno=29,
          tokens=24,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='handle',
          body='public function handle()\n'
               '    {\n'
               '        $this->comment(PHP_EOL.Inspiring::quote().PHP_EOL);\n'
               '    }'),
 Fragment(document_cs='4ca4fccde97862f16f87238df62642feb46df020e1364127f660906b0537e7f5',
          id=175,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: handle\n'
               '  Classes: Inspire\n'
               '  Usages: description signature this\n'),
 Fragment(document_cs='4d3db4616d5f6df5f1f48f2f87df9f80d8584cdf495c6a23f8a5c0f98bc4d12c',
          id=176,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='4d77082eb4834e289174c72834c9f1f643a9f16c505774e22b4813dcec28e94e',
          id=177,
          lineno=6,
          tokens=113,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='DropWishColumn',
          body='class DropWishColumn extends Migration\n'
               '{\n'
               '    /**\n'
               '     * Run the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function up()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->dropColumn(['wish']);\n"
               '        });\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Reverse the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function down()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->string('wish');\n"
               '        });\n'
               '    }\n'
               '}'),
 Fragment(document_cs='4d77082eb4834e289174c72834c9f1f643a9f16c505774e22b4813dcec28e94e',
          id=178,
          lineno=13,
          tokens=33,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->dropColumn(['wish']);\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='4d77082eb4834e289174c72834c9f1f643a9f16c505774e22b4813dcec28e94e',
          id=179,
          lineno=25,
          tokens=32,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->string('wish');\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='4d77082eb4834e289174c72834c9f1f643a9f16c505774e22b4813dcec28e94e',
          id=180,
          lineno=1,
          tokens=20,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: DropWishColumn\n'
               '  Usages: table\n'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=181,
          lineno=15,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='a:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=182,
          lineno=19,
          tokens=6,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='form-control',
          body='input.form-controlinput.form-control'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=183,
          lineno=23,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='focus',
          body='input.form-control:focus'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=184,
          lineno=24,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='form-control',
          body='textarea.form-control'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=185,
          lineno=24,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='focus',
          body='textarea.form-control:focus'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=186,
          lineno=31,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='label-default',
          body='.label-default'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=187,
          lineno=34,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='color-primary',
          body='.color-primary'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=188,
          lineno=37,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='color-badge',
          body='.color-badge'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=189,
          lineno=40,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='no-padding-left',
          body='.no-padding-left'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=190,
          lineno=43,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='no-padding-right',
          body='.no-padding-right'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=191,
          lineno=46,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='no-side-padding',
          body='.no-side-padding'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=192,
          lineno=50,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='show-on-hover',
          body='.show-on-hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=193,
          lineno=53,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='status-msg',
          body='.status-msg.status-msg'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=194,
          lineno=60,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='error-msg',
          body='.status-msg.error-msg'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=195,
          lineno=63,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='status-msg',
          body='.status-msg'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=196,
          lineno=63,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='success-msg',
          body='.status-msg.success-msg'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=197,
          lineno=66,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='noScroll',
          body='.noScroll'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=198,
          lineno=69,
          tokens=1,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='dim',
          body='.dim'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=199,
          lineno=72,
          tokens=1,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='circle',
          body='.circle'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=200,
          lineno=75,
          tokens=1,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='weight',
          body='.weight'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=201,
          lineno=82,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='panel',
          body='.panel.panel'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=202,
          lineno=87,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='panel-heading',
          body='.panel-heading'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=203,
          lineno=93,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='panel',
          body='.panel'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=204,
          lineno=93,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='panel-list',
          body='.panel.panel-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=205,
          lineno=93,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='panel-body',
          body='.panel-body'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=206,
          lineno=96,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='panel',
          body='.panel'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=207,
          lineno=96,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='panel-list',
          body='.panel.panel-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=208,
          lineno=105,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='panel',
          body='.panel'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=209,
          lineno=105,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='panel-list',
          body='.panel.panel-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=210,
          lineno=105,
          tokens=5,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.panel.panel-list a:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=211,
          lineno=110,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='panel',
          body='.panel'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=212,
          lineno=110,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='panel-list',
          body='.panel.panel-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=213,
          lineno=110,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='with-number',
          body='a.with-number'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=214,
          lineno=113,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='panel',
          body='.panel'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=215,
          lineno=113,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='panel-list',
          body='.panel.panel-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=216,
          lineno=113,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='with-number',
          body='a.with-number'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=217,
          lineno=113,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='dim',
          body='.dim'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=218,
          lineno=116,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='panel',
          body='.panel'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=219,
          lineno=116,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='panel-list',
          body='.panel.panel-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=220,
          lineno=116,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='panel-body',
          body='.panel-body'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=221,
          lineno=120,
          tokens=6,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav.side-nav.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=222,
          lineno=133,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.side-nav a:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=223,
          lineno=137,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=224,
          lineno=137,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='logo-section',
          body='.logo-section'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=225,
          lineno=145,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=226,
          lineno=145,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='logo-section',
          body='.logo-section'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=227,
          lineno=149,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=228,
          lineno=149,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='logo-section',
          body='.logo-section'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=229,
          lineno=149,
          tokens=7,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.side-nav .logo-section p:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=230,
          lineno=152,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=231,
          lineno=152,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='user-section',
          body='.user-section'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=232,
          lineno=156,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=233,
          lineno=156,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='user-section',
          body='.user-section'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=234,
          lineno=160,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=235,
          lineno=160,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='user-section',
          body='.user-section'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=236,
          lineno=167,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=237,
          lineno=167,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='search',
          body='.search'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=238,
          lineno=174,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=239,
          lineno=174,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='search',
          body='.search'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=240,
          lineno=174,
          tokens=6,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='focus',
          body='.side-nav .search input:focus'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=241,
          lineno=179,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=242,
          lineno=179,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='menu',
          body='.menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=243,
          lineno=185,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=244,
          lineno=185,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='menu',
          body='.menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=245,
          lineno=192,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=246,
          lineno=192,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='menu',
          body='.menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=247,
          lineno=192,
          tokens=6,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.side-nav .menu a:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=248,
          lineno=193,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=249,
          lineno=193,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='menu',
          body='.menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=250,
          lineno=193,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='active',
          body='a.active'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=251,
          lineno=197,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=252,
          lineno=197,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='menu',
          body='.menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=253,
          lineno=197,
          tokens=7,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='last-child',
          body='.side-nav .menu a:last-child'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=254,
          lineno=200,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=255,
          lineno=200,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='line',
          body='.line'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=256,
          lineno=204,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=257,
          lineno=204,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='menu',
          body='.menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=258,
          lineno=210,
          tokens=2,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=259,
          lineno=210,
          tokens=1,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='menu',
          body='.menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=260,
          lineno=210,
          tokens=7,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='last-child',
          body='.side-nav .menu a:last-child'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=261,
          lineno=214,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=262,
          lineno=214,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='line',
          body='.line'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=263,
          lineno=220,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=264,
          lineno=220,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='footer',
          body='.footer'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=265,
          lineno=224,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=266,
          lineno=224,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='footer',
          body='.footer'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=267,
          lineno=227,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='side-nav',
          body='.side-nav'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=268,
          lineno=227,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='footer',
          body='.footer'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=269,
          lineno=230,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=270,
          lineno=238,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.btn:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=271,
          lineno=241,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=272,
          lineno=241,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='focus',
          body='.btn:focus'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=273,
          lineno=242,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=274,
          lineno=242,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='active',
          body='.btn:active'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=275,
          lineno=246,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=276,
          lineno=246,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='btn-wide',
          body='.btn.btn-wide'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=277,
          lineno=249,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='btn-default',
          body='.btn-default'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=278,
          lineno=252,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=279,
          lineno=252,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='btn-primary',
          body='.btn.btn-primary'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=280,
          lineno=255,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=281,
          lineno=255,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='btn-primary',
          body='.btn.btn-primary'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=282,
          lineno=255,
          tokens=5,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='btn-line',
          body='.btn.btn-primary.btn-line'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=283,
          lineno=261,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=284,
          lineno=261,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='btn-primary',
          body='.btn.btn-primary'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=285,
          lineno=261,
          tokens=5,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='btn-line',
          body='.btn.btn-primary.btn-line'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=286,
          lineno=261,
          tokens=6,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.btn.btn-primary.btn-line:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=287,
          lineno=265,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='btn-special',
          body='.btn-special.btn-special'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=288,
          lineno=274,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.btn-special:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=289,
          lineno=278,
          tokens=8,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='popup-form',
          body='.popup-form.popup-form.popup-form.popup-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=290,
          lineno=298,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='actions',
          body='.actions'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=291,
          lineno=303,
          tokens=2,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='popup-form',
          body='.popup-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=292,
          lineno=303,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='actions',
          body='.actions'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=293,
          lineno=303,
          tokens=7,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.popup-form header .actions i:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=294,
          lineno=307,
          tokens=2,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='popup-form',
          body='.popup-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=295,
          lineno=307,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='actions',
          body='.actions'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=296,
          lineno=307,
          tokens=11,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='nth-child',
          body='.popup-form header .actions i:nth-child(1)'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=297,
          lineno=310,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='popup-form',
          body='.popup-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=298,
          lineno=310,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='minimized',
          body='.popup-form.minimized'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=299,
          lineno=314,
          tokens=6,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='popup-form',
          body='.popup-form.popup-form.popup-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=300,
          lineno=325,
          tokens=4,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='minimized',
          body='.popup-form.minimized'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=301,
          lineno=328,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='popup-form',
          body='.popup-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=302,
          lineno=328,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='form-control',
          body='.form-control'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=303,
          lineno=331,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='popup-form',
          body='.popup-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=304,
          lineno=331,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='new-task',
          body='.popup-form.new-task'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=305,
          lineno=332,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='popup-form',
          body='.popup-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=306,
          lineno=332,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='update-task',
          body='.popup-form.update-task'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=307,
          lineno=335,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=308,
          lineno=335,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=309,
          lineno=341,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=310,
          lineno=341,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=311,
          lineno=349,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=312,
          lineno=349,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=313,
          lineno=349,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='active',
          body='a.active'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=314,
          lineno=350,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=315,
          lineno=350,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=316,
          lineno=350,
          tokens=7,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.mega-menu .links a:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=317,
          lineno=351,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=318,
          lineno=351,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=319,
          lineno=351,
          tokens=8,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='first-child',
          body='.mega-menu .links a:first-child'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=320,
          lineno=355,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=321,
          lineno=355,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=322,
          lineno=355,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='active',
          body='a.active'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=323,
          lineno=356,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=324,
          lineno=356,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=325,
          lineno=356,
          tokens=8,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='first-child',
          body='.mega-menu .links a:first-child'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=326,
          lineno=360,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=327,
          lineno=360,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=328,
          lineno=360,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='inactive',
          body='a.inactive'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=329,
          lineno=368,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=330,
          lineno=368,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=331,
          lineno=368,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='inactive',
          body='a.inactive'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=332,
          lineno=368,
          tokens=9,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.mega-menu .links a.inactive:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=333,
          lineno=372,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=334,
          lineno=372,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=335,
          lineno=379,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=336,
          lineno=379,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=337,
          lineno=379,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='item',
          body='.item'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=338,
          lineno=382,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=339,
          lineno=382,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=340,
          lineno=382,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='item',
          body='.item'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=341,
          lineno=382,
          tokens=9,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='first-child',
          body='.mega-menu .content .item:first-child'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=342,
          lineno=385,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=343,
          lineno=385,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=344,
          lineno=388,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=345,
          lineno=388,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=346,
          lineno=395,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=347,
          lineno=395,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=348,
          lineno=398,
          tokens=3,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=349,
          lineno=398,
          tokens=1,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=350,
          lineno=398,
          tokens=8,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.mega-menu .content header i:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=351,
          lineno=402,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=352,
          lineno=402,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=353,
          lineno=405,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=354,
          lineno=405,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=355,
          lineno=405,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='client-update-form',
          body='.client-update-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=356,
          lineno=408,
          tokens=3,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=357,
          lineno=408,
          tokens=1,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=358,
          lineno=408,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='client-update-form',
          body='.client-update-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=359,
          lineno=415,
          tokens=3,
          depth=8,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=360,
          lineno=415,
          tokens=1,
          depth=8,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=361,
          lineno=415,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='client-update-form',
          body='.client-update-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=362,
          lineno=415,
          tokens=12,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='focus',
          body='.mega-menu .content header .client-update-form input:focus'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=363,
          lineno=418,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=364,
          lineno=418,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=365,
          lineno=418,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='panel',
          body='.panel'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=366,
          lineno=423,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=367,
          lineno=423,
          tokens=7,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu-tab',
          body='.mega-menu.mega-menu-tab'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=368,
          lineno=423,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=369,
          lineno=430,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=370,
          lineno=430,
          tokens=7,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu-tab',
          body='.mega-menu.mega-menu-tab'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=371,
          lineno=430,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=372,
          lineno=435,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=373,
          lineno=435,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=374,
          lineno=435,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='inactive',
          body='a.inactive'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=375,
          lineno=435,
          tokens=9,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.mega-menu .links a.inactive:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=376,
          lineno=438,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=377,
          lineno=438,
          tokens=7,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu-tab',
          body='.mega-menu.mega-menu-tab'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=378,
          lineno=438,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=379,
          lineno=447,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='client',
          body='.client'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=380,
          lineno=447,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='page-title-section',
          body='.client.page-title-section'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=381,
          lineno=450,
          tokens=6,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list-row',
          body='.task-list-row.task-list-row'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=382,
          lineno=451,
          tokens=4,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='col-md-4',
          body='.col-md-4'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=383,
          lineno=452,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=384,
          lineno=452,
          tokens=7,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu-tab',
          body='.mega-menu.mega-menu-tab'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=385,
          lineno=452,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='content',
          body='.content'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=386,
          lineno=452,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='item',
          body='.item'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=387,
          lineno=456,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list',
          body='.task-list.task-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=388,
          lineno=466,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='title',
          body='.title'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=389,
          lineno=472,
          tokens=4,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list',
          body='.task-list.task-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=390,
          lineno=479,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.task-list li:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=391,
          lineno=483,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list',
          body='.task-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=392,
          lineno=483,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='show-on-hover',
          body='.show-on-hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=393,
          lineno=486,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list',
          body='.task-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=394,
          lineno=486,
          tokens=4,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.task-list li:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=395,
          lineno=486,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='show-on-hover',
          body='.show-on-hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=396,
          lineno=490,
          tokens=4,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list',
          body='.task-list.task-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=397,
          lineno=493,
          tokens=5,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.task-list li span:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=398,
          lineno=496,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list',
          body='.task-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=399,
          lineno=496,
          tokens=6,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='first-child',
          body='.task-list li span:first-child'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=400,
          lineno=499,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list',
          body='.task-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=401,
          lineno=499,
          tokens=4,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='backlog',
          body='.task-list.backlog'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=402,
          lineno=502,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list',
          body='.task-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=403,
          lineno=502,
          tokens=4,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='backlog',
          body='.task-list.backlog'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=404,
          lineno=502,
          tokens=10,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='nth-child',
          body='.task-list.backlog li:nth-child(2)'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=405,
          lineno=503,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list',
          body='.task-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=406,
          lineno=503,
          tokens=4,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='backlog',
          body='.task-list.backlog'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=407,
          lineno=503,
          tokens=10,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='nth-child',
          body='.task-list.backlog li:nth-child(3)'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=408,
          lineno=504,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='task-list',
          body='.task-list'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=409,
          lineno=504,
          tokens=4,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='backlog',
          body='.task-list.backlog'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=410,
          lineno=504,
          tokens=10,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='nth-child',
          body='.task-list.backlog li:nth-child(4)'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=411,
          lineno=507,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='priority-circle',
          body='.priority-circle'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=412,
          lineno=513,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='priority-low',
          body='.priority-low'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=413,
          lineno=516,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='priority-normal',
          body='.priority-normal'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=414,
          lineno=519,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='priority-medium',
          body='.priority-medium'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=415,
          lineno=522,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='priority-high',
          body='.priority-high'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=416,
          lineno=525,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='priority-highest',
          body='.priority-highest'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=417,
          lineno=557,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=418,
          lineno=563,
          tokens=10,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='last-child',
          body='#pop-up-prompt section .btn:last-child'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=419,
          lineno=566,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=420,
          lineno=566,
          tokens=9,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='#pop-up-prompt section .btn:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=421,
          lineno=570,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='content-area',
          body='.content-area'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=422,
          lineno=576,
          tokens=6,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='page-title-section',
          body='.page-title-section.page-title-section'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=423,
          lineno=579,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=424,
          lineno=579,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='btn-primary',
          body='.btn.btn-primary'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=425,
          lineno=583,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='page-title-section',
          body='.page-title-section'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=426,
          lineno=583,
          tokens=4,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.page-title-section:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=427,
          lineno=583,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='show-on-hover',
          body='.show-on-hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=428,
          lineno=586,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='page-title-section',
          body='.page-title-section'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=429,
          lineno=586,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='label',
          body='.label'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=430,
          lineno=589,
          tokens=4,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=431,
          lineno=592,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=432,
          lineno=597,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=433,
          lineno=597,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=434,
          lineno=597,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='info',
          body='.info'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=435,
          lineno=601,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=436,
          lineno=601,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=437,
          lineno=601,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='info',
          body='.info'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=438,
          lineno=604,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=439,
          lineno=604,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=440,
          lineno=604,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='info',
          body='.info'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=441,
          lineno=604,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='name',
          body='p.name'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=442,
          lineno=607,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=443,
          lineno=607,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=444,
          lineno=610,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=445,
          lineno=610,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=446,
          lineno=610,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='bio',
          body='.bio'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=447,
          lineno=616,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=448,
          lineno=616,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=449,
          lineno=621,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=450,
          lineno=621,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=451,
          lineno=621,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=452,
          lineno=626,
          tokens=2,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=453,
          lineno=626,
          tokens=2,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=454,
          lineno=626,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=455,
          lineno=626,
          tokens=9,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.settings-container .left-side .links a:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=456,
          lineno=629,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=457,
          lineno=629,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=458,
          lineno=629,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='links',
          body='.links'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=459,
          lineno=633,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=460,
          lineno=633,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='right-side',
          body='.right-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=461,
          lineno=636,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='settings-container',
          body='.settings-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=462,
          lineno=636,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='right-side',
          body='.right-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=463,
          lineno=636,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='mega-menu',
          body='.mega-menu'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=464,
          lineno=639,
          tokens=1,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='progress',
          body='.progress'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=465,
          lineno=643,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='progress-bar',
          body='.progress-bar'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=466,
          lineno=649,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='table',
          body='.table'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=467,
          lineno=649,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='progress',
          body='.progress'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=468,
          lineno=652,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='credential-form',
          body='.credential-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=469,
          lineno=652,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='form-group',
          body='.form-group'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=470,
          lineno=652,
          tokens=5,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='type-0',
          body='.form-group.type-0'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=471,
          lineno=655,
          tokens=6,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='table',
          body='.table.table.table.table.table.table'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=472,
          lineno=663,
          tokens=10,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='special-form',
          body='.special-form.special-form.special-form.special-form.special-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=473,
          lineno=684,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=474,
          lineno=687,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='special-form',
          body='.special-form'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=475,
          lineno=687,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.special-form a:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=476,
          lineno=691,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hug',
          body='.hug'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=477,
          lineno=694,
          tokens=9,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-header',
          body='.hug-header.hug-header.hug-header'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=478,
          lineno=701,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=479,
          lineno=706,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-header',
          body='.hug-header'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=480,
          lineno=706,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=481,
          lineno=706,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='register',
          body='.btn.register'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=482,
          lineno=709,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-hero',
          body='.hug-hero'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=483,
          lineno=709,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=484,
          lineno=710,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-hero',
          body='.hug-hero'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=485,
          lineno=710,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='right-side',
          body='.right-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=486,
          lineno=714,
          tokens=6,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-hero',
          body='.hug-hero.hug-hero'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=487,
          lineno=720,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=488,
          lineno=727,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='mascot',
          body='.mascot'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=489,
          lineno=730,
          tokens=10,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-skyline',
          body='.hug-skyline.hug-skyline'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=490,
          lineno=734,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='skyline',
          body='.skyline'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=491,
          lineno=739,
          tokens=20,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-features',
          body='.hug-features.hug-features.hug-features.hug-features.hug-features'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=492,
          lineno=763,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='new',
          body='.new'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=493,
          lineno=766,
          tokens=8,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-features',
          body='.hug-features.hug-features'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=494,
          lineno=771,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='feature',
          body='.feature'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=495,
          lineno=771,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='centered',
          body='.feature.centered'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=496,
          lineno=776,
          tokens=12,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-info',
          body='.hug-info.hug-info.hug-info.hug-info'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=497,
          lineno=795,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='row',
          body='.row'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=498,
          lineno=799,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-info',
          body='.hug-info'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=499,
          lineno=799,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='arrow',
          body='.arrow'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=500,
          lineno=805,
          tokens=6,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-ui',
          body='.hug-ui.hug-ui'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=501,
          lineno=809,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='text-bucket',
          body='.text-bucket'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=502,
          lineno=814,
          tokens=9,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-ui',
          body='.hug-ui.hug-ui.hug-ui'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=503,
          lineno=826,
          tokens=8,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-exit',
          body='.hug-exit.hug-exit'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=504,
          lineno=832,
          tokens=1,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='img',
          body='.img'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=505,
          lineno=841,
          tokens=4,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-exit',
          body='.hug-exit'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=506,
          lineno=841,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='img',
          body='.img'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=507,
          lineno=850,
          tokens=4,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-exit',
          body='.hug-exit'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=508,
          lineno=850,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='img',
          body='.img'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=509,
          lineno=851,
          tokens=4,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-exit',
          body='.hug-exit'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=510,
          lineno=851,
          tokens=1,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='img',
          body='.img'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=511,
          lineno=855,
          tokens=12,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-footer',
          body='.hug-footer.hug-footer.hug-footer.hug-footer'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=512,
          lineno=868,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='special',
          body='hr.special'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=513,
          lineno=871,
          tokens=6,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-footer',
          body='.hug-footer.hug-footer'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=514,
          lineno=874,
          tokens=5,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hover',
          body='.hug-footer a:hover'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=515,
          lineno=877,
          tokens=3,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-footer',
          body='.hug-footer'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=516,
          lineno=877,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='last-line',
          body='.last-line'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=517,
          lineno=880,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='project-list-container',
          body='.project-list-container'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=518,
          lineno=886,
          tokens=6,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-hero',
          body='.hug-hero.hug-hero'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=519,
          lineno=889,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='right-side',
          body='.right-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=520,
          lineno=892,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-hero',
          body='.hug-hero'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=521,
          lineno=892,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='left-side',
          body='.left-side'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=522,
          lineno=896,
          tokens=4,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-features',
          body='.hug-features'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=523,
          lineno=899,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-ui',
          body='.hug-ui'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=524,
          lineno=899,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='text-bucket',
          body='.text-bucket'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=525,
          lineno=902,
          tokens=4,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-exit',
          body='.hug-exit'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=526,
          lineno=902,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='img',
          body='.img'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=527,
          lineno=908,
          tokens=4,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-exit',
          body='.hug-exit'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=528,
          lineno=908,
          tokens=1,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='img',
          body='.img'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=529,
          lineno=908,
          tokens=4,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-exit',
          body='.hug-exit'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=530,
          lineno=908,
          tokens=1,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='img',
          body='.img'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=531,
          lineno=912,
          tokens=3,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-footer',
          body='.hug-footer'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=532,
          lineno=916,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-hero',
          body='.hug-hero'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=533,
          lineno=919,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-header',
          body='.hug-header'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=534,
          lineno=919,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='pull-left',
          body='.pull-left'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=535,
          lineno=922,
          tokens=6,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-header',
          body='.hug-header.hug-header'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=536,
          lineno=926,
          tokens=1,
          depth=7,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=537,
          lineno=926,
          tokens=2,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='register',
          body='.btn.register'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=538,
          lineno=929,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-header',
          body='.hug-header'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=539,
          lineno=929,
          tokens=1,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='btn',
          body='.btn'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=540,
          lineno=933,
          tokens=3,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='hug-hero',
          body='.hug-hero'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=541,
          lineno=936,
          tokens=2,
          depth=5,
          parent_id=None,
          category='class',
          summary=False,
          name='btn-special',
          body='.btn-special'),
 Fragment(document_cs='4ef53eaf8070a8e33bd5090da18ce69bc7e26331938011e291ca3ab666fff2fd',
          id=542,
          lineno=1,
          tokens=8,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body="  Classes: {' '.join(classes)}\n"),
 Fragment(document_cs='5040c18d00811c7cecc9d22ec511d890e6b67c4034372b2d53a7265072c03574',
          id=543,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='547ae041e49475ff19df872e1d9dba0ba35e5f749ceb02220f1dfce736a1acaa',
          id=544,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='567071d9d574f6f418e5f2198e131160647ab79fc3bd275da64c5a8a52d953f8',
          id=545,
          lineno=12,
          tokens=225,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CredentialsController',
          body='class CredentialsController extends BaseController {\n'
               '\n'
               '\t// Get all credentials for the given project\n'
               '\tpublic function getProjectCredentials($id){\n'
               "\t\tif( count(Credential::where('project_id',$id)->get()) === "
               '0 ){\n'
               "\t\t\tif (!Input::get('password')) {\n"
               "\t\t\t\treturn $this->setStatusCode(404)->makeResponse('No "
               "credentials found for this project');\n"
               '\t\t\t}\n'
               '\t\t}\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Found "
               "credentials for this project', "
               "Credential::where('project_id',$id)->get() );\n"
               '\t}\n'
               '\n'
               '\t// Insert a new credential into the database\n'
               '\tpublic function storeCredential(){\n'
               '\t\tif (!Input::all()) {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('No "
               "information provided to create credential');\n"
               '\t\t}\n'
               '\n'
               "\t\tif (!Input::get('name')) {\n"
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The name "
               "seems to be empty');\n"
               '\t\t}\n'
               '\n'
               "\t\tif (!Input::get('username')) {\n"
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "username seems to be empty');\n"
               '\t\t}\n'),
 Fragment(document_cs='567071d9d574f6f418e5f2198e131160647ab79fc3bd275da64c5a8a52d953f8',
          id=546,
          lineno=38,
          tokens=231,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CredentialsController',
          body='\n'
               "\t\tif (!Input::get('user_id')) {\n"
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('No user "
               "id is being passed');\n"
               '\t\t}\n'
               '\n'
               "\t\tif (!Input::get('project_id')) {\n"
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('No "
               "project id is being passed');\n"
               '\t\t}\n'
               '\n'
               "\t\tif (!Input::get('password')) {\n"
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "password seems to be empty');\n"
               '\t\t}\n'
               '\n'
               '\t\tCredential::create(Input::all());\n'
               '\t\t$id = \\DB::getPdo()->lastInsertId();\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Credential "
               "created successfully', Credential::find($id));\n"
               '\t}\n'
               '\n'
               '\t// Update the given credential\n'
               '\tpublic function updateCredential($id){\n'
               '\t\tif (!Credential::find($id)) {\n'
               "\t\t\treturn $this->setStatusCode(400)->makeResponse('Could "
               "not find the credential');\n"
               '\t\t}\n'
               '\n'
               '\t\tif ( Input::get(\'name\') === "") {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "credential needs a name');\n"
               '\t\t}\n'),
 Fragment(document_cs='567071d9d574f6f418e5f2198e131160647ab79fc3bd275da64c5a8a52d953f8',
          id=547,
          lineno=66,
          tokens=196,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CredentialsController',
          body='\n'
               '\t\tif ( Input::get(\'username\') === "") {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "credential needs a username');\n"
               '\t\t}\n'
               '\n'
               '\t\tif ( Input::get(\'password\') === "") {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "credential needs a password');\n"
               '\t\t}\n'
               '\n'
               '\t\t$input = Input::all();\n'
               "\t\tunset($input['_method']);\n"
               '\n'
               '\t\tCredential::find($id)->update($input);\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('The "
               "credential has been updated');\n"
               '\t}\n'
               '\n'
               '\t// Remove the given credential from the database\n'
               '\tpublic function removeCredential($id){\n'
               '\t\tif (!Credential::find($id)) {\n'
               "\t\t\treturn $this->setStatusCode(400)->makeResponse('Could "
               "not find the credentials');\n"
               '\t\t}\n'
               '\n'
               '\t\tCredential::find($id)->delete();\n'
               '\t\treturn '
               "$this->setStatusCode(200)->makeResponse('Credentials deleted "
               "successfully');\n"
               '\t}\n'
               '}'),
 Fragment(document_cs='567071d9d574f6f418e5f2198e131160647ab79fc3bd275da64c5a8a52d953f8',
          id=548,
          lineno=15,
          tokens=97,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='getProjectCredentials',
          body='public function getProjectCredentials($id){\n'
               "\t\tif( count(Credential::where('project_id',$id)->get()) === "
               '0 ){\n'
               "\t\t\tif (!Input::get('password')) {\n"
               "\t\t\t\treturn $this->setStatusCode(404)->makeResponse('No "
               "credentials found for this project');\n"
               '\t\t\t}\n'
               '\t\t}\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Found "
               "credentials for this project', "
               "Credential::where('project_id',$id)->get() );\n"
               '\t}'),
 Fragment(document_cs='567071d9d574f6f418e5f2198e131160647ab79fc3bd275da64c5a8a52d953f8',
          id=549,
          lineno=26,
          tokens=170,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='storeCredential',
          body='public function storeCredential(){\n'
               '\t\tif (!Input::all()) {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('No "
               "information provided to create credential');\n"
               '\t\t}\n'
               '\n'
               "\t\tif (!Input::get('name')) {\n"
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The name "
               "seems to be empty');\n"
               '\t\t}\n'
               '\n'
               "\t\tif (!Input::get('username')) {\n"
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "username seems to be empty');\n"
               '\t\t}\n'
               '\n'
               "\t\tif (!Input::get('user_id')) {\n"
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('No user "
               "id is being passed');\n"
               '\t\t}\n'
               '\n'
               "\t\tif (!Input::get('project_id')) {\n"
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('No "
               "project id is being passed');\n"
               '\t\t}\n'),
 Fragment(document_cs='567071d9d574f6f418e5f2198e131160647ab79fc3bd275da64c5a8a52d953f8',
          id=550,
          lineno=46,
          tokens=83,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='storeCredential',
          body='\n'
               "\t\tif (!Input::get('password')) {\n"
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "password seems to be empty');\n"
               '\t\t}\n'
               '\n'
               '\t\tCredential::create(Input::all());\n'
               '\t\t$id = \\DB::getPdo()->lastInsertId();\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Credential "
               "created successfully', Credential::find($id));\n"
               '\t}'),
 Fragment(document_cs='567071d9d574f6f418e5f2198e131160647ab79fc3bd275da64c5a8a52d953f8',
          id=551,
          lineno=58,
          tokens=189,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='updateCredential',
          body='public function updateCredential($id){\n'
               '\t\tif (!Credential::find($id)) {\n'
               "\t\t\treturn $this->setStatusCode(400)->makeResponse('Could "
               "not find the credential');\n"
               '\t\t}\n'
               '\n'
               '\t\tif ( Input::get(\'name\') === "") {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "credential needs a name');\n"
               '\t\t}\n'
               '\n'
               '\t\tif ( Input::get(\'username\') === "") {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "credential needs a username');\n"
               '\t\t}\n'
               '\n'
               '\t\tif ( Input::get(\'password\') === "") {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "credential needs a password');\n"
               '\t\t}\n'
               '\n'
               '\t\t$input = Input::all();\n'
               "\t\tunset($input['_method']);\n"
               '\n'
               '\t\tCredential::find($id)->update($input);\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('The "
               "credential has been updated');\n"
               '\t}'),
 Fragment(document_cs='567071d9d574f6f418e5f2198e131160647ab79fc3bd275da64c5a8a52d953f8',
          id=552,
          lineno=83,
          tokens=68,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='removeCredential',
          body='public function removeCredential($id){\n'
               '\t\tif (!Credential::find($id)) {\n'
               "\t\t\treturn $this->setStatusCode(400)->makeResponse('Could "
               "not find the credentials');\n"
               '\t\t}\n'
               '\n'
               '\t\tCredential::find($id)->delete();\n'
               '\t\treturn '
               "$this->setStatusCode(200)->makeResponse('Credentials deleted "
               "successfully');\n"
               '\t}'),
 Fragment(document_cs='567071d9d574f6f418e5f2198e131160647ab79fc3bd275da64c5a8a52d953f8',
          id=553,
          lineno=1,
          tokens=26,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: getProjectCredentials removeCredential '
               'storeCredential updateCredential\n'
               '  Classes: CredentialsController\n'
               '  Usages: input this\n'),
 Fragment(document_cs='56a46c3a226b4436acf3e5c857a1b33a92c24186fc4d8c04583d2c5613e59a19',
          id=554,
          lineno=6,
          tokens=179,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CreateFilesTable',
          body='class CreateFilesTable extends Migration {\n'
               '\n'
               '    /**\n'
               '     * Run the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function up()\n'
               '    {\n'
               "        Schema::create('uploads', function(Blueprint $table)\n"
               '        {\n'
               "            $table->increments('id');\n"
               "            $table->integer('user_id')->unsigned();\n"
               "            $table->integer('project_id')->unsigned();\n"
               "            $table->string('name');\n"
               "            $table->string('path');\n"
               '            $table->timestamps();\n'
               '\n'
               '            '
               "$table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');\n"
               '            '
               "$table->foreign('project_id')->references('id')->on('projects')->onDelete('cascade');\n"
               '        });\n'
               '    }\n'
               '\n'
               '\n'
               '    /**\n'
               '     * Reverse the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function down()\n'
               '    {\n'
               "        Schema::drop('uploads');\n"
               '    }\n'
               '\n'
               '}'),
 Fragment(document_cs='56a46c3a226b4436acf3e5c857a1b33a92c24186fc4d8c04583d2c5613e59a19',
          id=555,
          lineno=13,
          tokens=118,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '    {\n'
               "        Schema::create('uploads', function(Blueprint $table)\n"
               '        {\n'
               "            $table->increments('id');\n"
               "            $table->integer('user_id')->unsigned();\n"
               "            $table->integer('project_id')->unsigned();\n"
               "            $table->string('name');\n"
               "            $table->string('path');\n"
               '            $table->timestamps();\n'
               '\n'
               '            '
               "$table->foreign('user_id')->references('id')->on('users')->onDelete('cascade');\n"
               '            '
               "$table->foreign('project_id')->references('id')->on('projects')->onDelete('cascade');\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='56a46c3a226b4436acf3e5c857a1b33a92c24186fc4d8c04583d2c5613e59a19',
          id=556,
          lineno=35,
          tokens=15,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '    {\n'
               "        Schema::drop('uploads');\n"
               '    }'),
 Fragment(document_cs='56a46c3a226b4436acf3e5c857a1b33a92c24186fc4d8c04583d2c5613e59a19',
          id=557,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: CreateFilesTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='5ac9483a9eea703984ef4adfb2f2309d67f2d8368ab6d5de467edc9603dfe3b0',
          id=558,
          lineno=7,
          tokens=68,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AppServiceProvider',
          body='class AppServiceProvider extends ServiceProvider\n'
               '{\n'
               '    /**\n'
               '     * Bootstrap any application services.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function boot()\n'
               '    {\n'
               '        //\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Register any application services.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function register()\n'
               '    {\n'
               '        //\n'
               '    }\n'
               '}'),
 Fragment(document_cs='5ac9483a9eea703984ef4adfb2f2309d67f2d8368ab6d5de467edc9603dfe3b0',
          id=559,
          lineno=14,
          tokens=10,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='boot',
          body='public function boot()\n    {\n        //\n    }'),
 Fragment(document_cs='5ac9483a9eea703984ef4adfb2f2309d67f2d8368ab6d5de467edc9603dfe3b0',
          id=560,
          lineno=24,
          tokens=10,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='register',
          body='public function register()\n    {\n        //\n    }'),
 Fragment(document_cs='5ac9483a9eea703984ef4adfb2f2309d67f2d8368ab6d5de467edc9603dfe3b0',
          id=561,
          lineno=1,
          tokens=12,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: boot register\n  Classes: AppServiceProvider\n'),
 Fragment(document_cs='5b06eb920fc4b63311ba839597e6fc1482cd7c9bb82878852a08f963968e7f9e',
          id=562,
          lineno=6,
          tokens=121,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AddPointOfContactToClientsTable',
          body='class AddPointOfContactToClientsTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->string('point_of_contact');\n"
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->dropColumn(['point_of_contact']);\n"
               '\t\t});\n'
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='5b06eb920fc4b63311ba839597e6fc1482cd7c9bb82878852a08f963968e7f9e',
          id=563,
          lineno=13,
          tokens=36,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->string('point_of_contact');\n"
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='5b06eb920fc4b63311ba839597e6fc1482cd7c9bb82878852a08f963968e7f9e',
          id=564,
          lineno=27,
          tokens=37,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '\t{\n'
               "\t\tSchema::table('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->dropColumn(['point_of_contact']);\n"
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='5b06eb920fc4b63311ba839597e6fc1482cd7c9bb82878852a08f963968e7f9e',
          id=565,
          lineno=1,
          tokens=23,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: AddPointOfContactToClientsTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='5b4cd9784a5f4742e16a13465f9886d00d7aba944dcf0ce9c00966f25304be21',
          id=566,
          lineno=6,
          tokens=115,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CreateBetaTable',
          body='class CreateBetaTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::create('beta', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->string('email');\n"
               "\t\t\t$table->boolean('status');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::drop('beta');\n"
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='5b4cd9784a5f4742e16a13465f9886d00d7aba944dcf0ce9c00966f25304be21',
          id=567,
          lineno=13,
          tokens=56,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::create('beta', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->string('email');\n"
               "\t\t\t$table->boolean('status');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='5b4cd9784a5f4742e16a13465f9886d00d7aba944dcf0ce9c00966f25304be21',
          id=568,
          lineno=29,
          tokens=15,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body="public function down()\n\t{\n\t\tSchema::drop('beta');\n\t}"),
 Fragment(document_cs='5b4cd9784a5f4742e16a13465f9886d00d7aba944dcf0ce9c00966f25304be21',
          id=569,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: CreateBetaTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='5c0dbb5d795864320e15bd9ada2309037566a2aa8de2bc228ea811515c70cac5',
          id=570,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='5c89a8a9c5af258d02d0bfd3582c75963bea53baa1f5f5132662b80020a63452',
          id=571,
          lineno=1,
          tokens=4,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='*\n!.gitignore'),
 Fragment(document_cs='5c89a8a9c5af258d02d0bfd3582c75963bea53baa1f5f5132662b80020a63452',
          id=572,
          lineno=1,
          tokens=4,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='*\n!.gitignore'),
 Fragment(document_cs='5c89a8a9c5af258d02d0bfd3582c75963bea53baa1f5f5132662b80020a63452',
          id=573,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='5c89a8a9c5af258d02d0bfd3582c75963bea53baa1f5f5132662b80020a63452',
          id=574,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='66c6189eaa34abfadb561b2fa2ce296282551df0ec3cc8f0c67806d846a6ecc5',
          id=575,
          lineno=7,
          tokens=193,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Kernel',
          body='class Kernel extends HttpKernel\n'
               '{\n'
               '    /**\n'
               "     * The application's global HTTP middleware stack.\n"
               '     *\n'
               '     * @var array\n'
               '     */\n'
               '    protected $middleware = [\n'
               '        '
               '\\Illuminate\\Foundation\\Http\\Middleware\\CheckForMaintenanceMode::class,\n'
               '        \\App\\Http\\Middleware\\EncryptCookies::class,\n'
               '        '
               '\\Illuminate\\Cookie\\Middleware\\AddQueuedCookiesToResponse::class,\n'
               '        '
               '\\Illuminate\\Session\\Middleware\\StartSession::class,\n'
               '        '
               '\\Illuminate\\View\\Middleware\\ShareErrorsFromSession::class,\n'
               '        // \\App\\Http\\Middleware\\VerifyCsrfToken::class,\n'
               '    ];\n'
               '\n'
               '    /**\n'
               "     * The application's route middleware.\n"
               '     *\n'
               '     * @var array\n'
               '     */\n'
               '    protected $routeMiddleware = [\n'
               "        'auth' => "
               '\\App\\Http\\Middleware\\Authenticate::class,\n'
               "        'auth.basic' => "
               '\\Illuminate\\Auth\\Middleware\\AuthenticateWithBasicAuth::class,\n'
               "        'guest' => "
               '\\App\\Http\\Middleware\\RedirectIfAuthenticated::class,\n'
               '    ];\n'
               '}'),
 Fragment(document_cs='66c6189eaa34abfadb561b2fa2ce296282551df0ec3cc8f0c67806d846a6ecc5',
          id=576,
          lineno=1,
          tokens=13,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Kernel\n  Usages: middleware routeMiddleware\n'),
 Fragment(document_cs='67dbcf1fb37baf000a8fc8fd04b5ae97459543bc8549f573778508e9cab83160',
          id=577,
          lineno=7,
          tokens=80,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Job',
          body='abstract class Job\n'
               '{\n'
               '    /*\n'
               '    '
               '|--------------------------------------------------------------------------\n'
               '    | Queueable Jobs\n'
               '    '
               '|--------------------------------------------------------------------------\n'
               '    |\n'
               '    | This job base class provides a central location to place '
               'any logic that\n'
               '    | is shared across all of your jobs. The trait included '
               'with the class\n'
               '    | provides access to the "queueOn" and "delay" queue '
               'helper methods.\n'
               '    |\n'
               '    */\n'
               '\n'
               '    use Queueable;\n'
               '}'),
 Fragment(document_cs='67dbcf1fb37baf000a8fc8fd04b5ae97459543bc8549f573778508e9cab83160',
          id=578,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Job\n'),
 Fragment(document_cs='69f1ac97f5315d65f519ea9d3b76311e064b85c441f371f14bd8f372319c64f2',
          id=579,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='6aa1e6114c6d0789b419701c7a97601bb6896d3b93aa0a09d558097e83850fa4',
          id=580,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='6ecc117707142a2f9de731d057659c031e1965f7d074bb01057712f740fafcde',
          id=581,
          lineno=1,
          tokens=12,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='# AskYourCode\n### The intelligent rubber ducky!\n'),
 Fragment(document_cs='6eff78320e52269d33282e6ab613e2c6b2704ada8e22486e3bdb1b2b8a05de2e',
          id=582,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='706dbe797bacc090a0d02b4578546afa937bd4543db525a50ee0a2743bb4d21a',
          id=583,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='720c1d870f59209ac775f75d3c148b9d31ca199502cd7a44fc0e34c38b5d364c',
          id=584,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='76dd668e3d779a79e2449c19eff0589204d02f8c820bbef9d45320e8a2a7118c',
          id=585,
          lineno=7,
          tokens=59,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Credential',
          body='class Credential extends Model {\n'
               '\tprotected $fillable = [\n'
               "        'user_id',\n"
               "        'project_id',\n"
               "        'name',\n"
               "        'type',\n"
               "        'hostname',\n"
               "        'username',\n"
               "        'password',\n"
               "        'port'\n"
               '    ];\n'
               '\n'
               "    protected $hidden = ['created_at','updated_at'];\n"
               '}'),
 Fragment(document_cs='76dd668e3d779a79e2449c19eff0589204d02f8c820bbef9d45320e8a2a7118c',
          id=586,
          lineno=1,
          tokens=13,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Credential\n  Usages: fillable hidden\n'),
 Fragment(document_cs='7cb8bf6e54de76b01d779e55d490410ffad65bc5edd682e09316e9b05169720c',
          id=587,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='7d43713003d8a90f6af943187cd2748dd5c34d2a2dd81f297a20fa6301e93649',
          id=588,
          lineno=6,
          tokens=130,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AddDescriptionAndWishColumnsToTasks',
          body='class AddDescriptionAndWishColumnsToTasks extends Migration\n'
               '{\n'
               '    /**\n'
               '     * Run the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function up()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->string('description');            \n"
               "            $table->boolean('wish');\n"
               '        });\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Reverse the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function down()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->dropColumn(array('description', 'wish'));\n"
               '        });\n'
               '    }\n'
               '}'),
 Fragment(document_cs='7d43713003d8a90f6af943187cd2748dd5c34d2a2dd81f297a20fa6301e93649',
          id=589,
          lineno=13,
          tokens=41,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->string('description');            \n"
               "            $table->boolean('wish');\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='7d43713003d8a90f6af943187cd2748dd5c34d2a2dd81f297a20fa6301e93649',
          id=590,
          lineno=26,
          tokens=37,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->dropColumn(array('description', 'wish'));\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='7d43713003d8a90f6af943187cd2748dd5c34d2a2dd81f297a20fa6301e93649',
          id=591,
          lineno=1,
          tokens=24,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: AddDescriptionAndWishColumnsToTasks\n'
               '  Usages: table\n'),
 Fragment(document_cs='7e50d90a58983c0326fc7a895455ad1490290c1c3827f67bcfe1f7ae81316af5',
          id=592,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='7f99dce936aebdb18f5d8f03390a21a53708fb2893f2e81193b203bdca94a637',
          id=593,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='806b27e5e231318eb91a128fe95f418193516e9c760692c984e033604049d57b',
          id=594,
          lineno=1,
          tokens=6,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Usages: counter\n'),
 Fragment(document_cs='81a6cbb3e29cefea44b1d25f2c7ab24e90d9b5d75a5386758ebf41465ef48a4e',
          id=595,
          lineno=1,
          tokens=38,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='hud',
          body='hud = new Vue({\n'
               "    el: '#hud',\n"
               '    data: {\n'
               '        clients: 0,\n'
               '        projects: [],\n'
               '        sharedProjects: [],\n'
               '        tasks: 0\n'
               '    },\n'),
 Fragment(document_cs='81a6cbb3e29cefea44b1d25f2c7ab24e90d9b5d75a5386758ebf41465ef48a4e',
          id=596,
          lineno=9,
          tokens=244,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='hud',
          body='    ready: function () {\n'
               '        this.getClients();\n'
               '        this.getProjects();\n'
               '        this.getSharedProjects();\n'
               '        this.getTasks();\n'
               '    },\n'
               '    computed: {},\n'
               '    methods: {\n'
               '        getClients: function(){\n'
               '            $.get( window.baseurl + "/api/clients/true", '
               'function( results ) {\n'
               '                hud.clients = results.data.length;\n'
               '            }).fail(function(e){\n'
               '                console.log( "error "+ e );\n'
               '            });\n'
               '        },\n'
               '        getProjects: function(){\n'
               '            $.get( window.baseurl + "/api/projects", function( '
               'results ) {\n'
               '                hud.projects = results.data;\n'
               '            }).fail(function(e){\n'
               '                console.log( "error "+ e );\n'
               '            });\n'
               '        },\n'
               '        getSharedProjects: function(){\n'
               '            $.get( window.baseurl + "/api/projects/shared", '
               'function( results ) {\n'
               '                hud.sharedProjects = results.data;\n'
               '            }).fail(function(e){\n'
               '                console.log( "error "+ e );\n'
               '            });\n'
               '        },\n'
               '        getTasks: function(){\n'
               '            $.get( window.baseurl + "/api/tasks", function( '
               'results ) {\n'
               '                hud.tasks = results.data.length;\n'
               '            }).fail(function(e){\n'
               '                console.log( "error "+ e );\n'
               '            });\n'
               '        },\n'
               '    }\n'
               '})'),
 Fragment(document_cs='81a6cbb3e29cefea44b1d25f2c7ab24e90d9b5d75a5386758ebf41465ef48a4e',
          id=597,
          lineno=1,
          tokens=14,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: hud\n  Usages: Vue console results window\n'),
 Fragment(document_cs='8287c7a8948349d802237f6bb43dae76379faa32eeec3aad0be3ebe6d0590185',
          id=598,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='834f350959f49b6059604a739dd901bba8df312f0c4e125353b72e590d7bb9cd',
          id=599,
          lineno=7,
          tokens=19,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Beta',
          body='class Beta extends Model {\n'
               '\tprotected $fillable = [];\n'
               "\tprotected $table = 'beta';\n"
               '\n'
               '\t\n'
               '}'),
 Fragment(document_cs='834f350959f49b6059604a739dd901bba8df312f0c4e125353b72e590d7bb9cd',
          id=600,
          lineno=1,
          tokens=13,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Beta\n  Usages: fillable table\n'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=601,
          lineno=18,
          tokens=182,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='UsersController',
          body='class UsersController extends BaseController {\n'
               '\n'
               '\t// Go to user settings page\n'
               '\tpublic function index()\n'
               '\t{\n'
               "\t\treturn View::make('ins/settings')->with('pTitle', "
               'Auth::user()->full_name);\n'
               '\t}\n'
               '\n'
               '\t// Logout the user\n'
               '\tpublic function logout(){\n'
               '\t\tAuth::logout();\n'
               "\t\treturn Redirect::to('/');\n"
               '\t}\n'
               '\n'
               '\t// Login the user\n'
               '\tpublic function login()\n'
               '\t{\t\t\t\t\n'
               "\t\t$email \t\t=\tInput::get('email');\n"
               "\t\t$password\t=\tInput::get('password');\n"
               '\n'
               '\t\t// lets validate the users input\n'
               '\t\t$validator = Validator::make(\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'email' \t=>\t$email,\n"
               "\t\t\t\t\t'password' \t=> \t$password\n"
               '\t\t\t),\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'email'\t\t=> \t'required|email',\n"
               "\t\t\t\t\t'password'\t=>\t'required'\n"
               '\t\t\t)\n'
               '\t\t);\n'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=602,
          lineno=49,
          tokens=115,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='UsersController',
          body='\n'
               '\t\tif ($validator->fails()){\n'
               '\t\t    return '
               'Redirect::back()->withErrors($validator)->withInput();\n'
               '\t\t}else{\n'
               "\t\t\tif( Auth::attempt(array('email' => $email, 'password' => "
               '$password)) ){\t\t\t\t\n'
               "\t\t\t\treturn Redirect::to('hud');\n"
               '\t\t\t}else{\t\t\t\t\n'
               "\t\t\t\t$validator->getMessageBag()->add('input', 'Incorrect "
               "email or password');\n"
               '\t\t\t\treturn '
               'Redirect::back()->withErrors($validator)->withInput();;\n'
               '\t\t\t}\t\t\t\n'
               '\t\t}\n'
               '\t}\t\n'
               '\n'
               '\t// Register the user and start a new session\n'
               '\tpublic'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=603,
          lineno=63,
          tokens=232,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='UsersController',
          body=' function register()\n'
               '\t{\t\n'
               "\t\t$fullName\t=\tInput::get('fullName');\n"
               "\t\t$email \t\t=\tInput::get('email');\n"
               "\t\t$password\t=\tInput::get('password');\t\n"
               '\n'
               '\t\t// lets validate the users input\n'
               '\t\t$validator = Validator::make(\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'fullName' \t=> \t$fullName,\n"
               "\t\t\t\t\t'email' \t=>\t$email,\n"
               "\t\t\t\t\t'password' \t=> \t$password\n"
               '\t\t\t),\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'fullName' \t=> \t'required',\n"
               "\t\t\t\t\t'email'\t\t=> \t'required|email|unique:users',\n"
               "\t\t\t\t\t'password'\t=>\t'required|min:8'\n"
               '\t\t\t)\n'
               '\t\t);\n'
               '\n'
               '\t\tif ($validator->fails()){\n'
               '\t\t    return '
               'Redirect::back()->withErrors($validator)->withInput();\n'
               '\t\t}\n'
               '\n'
               '\t\t$user \t\t\t\t=\tnew User;\n'
               '\t\t$user->full_name \t=\t$fullName;\n'
               '\t\t$user->email \t\t=\t$email;\n'
               '\t\t$user->password \t=\tHash::make($password);\n'
               '\n'
               '\t\t$user->save();\t\n'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=604,
          lineno=93,
          tokens=129,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='UsersController',
          body='\n'
               "\t\tif ( Auth::attempt(array('email' => $email, 'password' => "
               '$password)) ) {\n'
               '\t\t\tHelpers::sendWelcomeMail();\n'
               "\t\t\treturn Redirect::to('hud');\n"
               '\t\t}\n'
               '\n'
               '\t\treturn Redirect::back()->withErrors($validator);\n'
               '\t}\t\n'
               '\n'
               '\t// Reset the user password\n'
               '\tpublic function resetPassword($id)\n'
               '\t{\t\t\n'
               '\t\t// ----------------------------------------\n'
               '\t\t$user = User::find(Auth::id());\n'
               '\t\t$created = $user->tasks_created;\n'
               '\t\t$completed = $user->tasks_completed;\n'
               '\n'
               '\t\tif ($created == "") {\n'
               '\t\t\t$created = 0;\n'
               '\t\t}\n'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=605,
          lineno=113,
          tokens=178,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='UsersController',
          body='\n'
               '\t\tif ($completed == "") {\n'
               '\t\t\t$completed = 0;\n'
               '\t\t}\n'
               '\t\t// ----------------------------------------\n'
               '\n'
               "\t\t$current_pwd\t=\tInput::get('current_pwd');\n"
               "\t\t$new_pwd\t\t=\tInput::get('new_pwd');\n"
               '\n'
               '\t\t// lets validate the users input\n'
               '\t\t$validator = Validator::make(\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'current_pwd' \t=>\t$current_pwd,\n"
               "\t\t\t\t\t'new_pwd' \t\t=> \t$new_pwd\n"
               '\t\t\t),\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'current_pwd'\t=> \t'required',\n"
               "\t\t\t\t\t'new_pwd'\t\t=>\t'required'\n"
               '\t\t\t)\n'
               '\t\t);\n'
               '\n'
               '\t\tif ($validator->fails()){\n'
               '\t\t    return '
               "Redirect::back()->withErrors($validator)->with('user', "
               "$user)->with('created', $created)->with('completed', "
               '$completed);\n'
               '\t\t}\n'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=606,
          lineno=137,
          tokens=203,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='UsersController',
          body='\n'
               "\t\tif ( !Auth::validate(array('email' => $user->email, "
               "'password' => $current_pwd)) ) {\n"
               "\t\t\t$validator->getMessageBag()->add('password', 'That "
               "password is incorrect');\n"
               '\t\t\treturn '
               "Redirect::back()->withErrors($validator)->with('user', "
               "$user)->with('created', $created)->with('completed', "
               '$completed);\t\n'
               '\t\t}\n'
               '\n'
               '\t\t// Store the new password and redirect;\n'
               '\t\t$user->password = Hash::make($new_pwd);\n'
               '\t\t$user->save();\n'
               '\n'
               '\t\treturn Redirect::back()\n'
               "\t\t\t\t\t\t\t\t->with('user', $user)\n"
               "\t\t\t\t\t\t\t\t->with('created', $created)->with('completed', "
               '$completed)\n'
               '\t\t\t\t\t\t\t\t->with(\'success\', "Your password has been '
               'updated!");\n'
               '\n'
               '\t}\n'
               '\n'
               '    // Get the current user\n'
               '    public function getUser(){\n'
               '        $user = User::find(Auth::id());\n'
               '        return $user;\n'
               '    }\n'
               '    // Update the given user\n'
               '    public function updateUser($id){\n'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=607,
          lineno=161,
          tokens=241,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='UsersController',
          body="        if (strlen(trim(Input::get('email'))) === 0) {\n"
               '            return '
               "$this->setStatusCode(200)->makeResponse('You need to provide "
               "an email.');\n"
               '        }\n'
               '\n'
               "        if( strlen(trim(Input::get('full_name'))) === 0 ){\n"
               '            return '
               "$this->setStatusCode(200)->makeResponse('You have a name, "
               "no?');\n"
               '        }\n'
               '\n'
               '        if (!User::find(Auth::id())) {\n'
               '            return '
               "$this->setStatusCode(404)->makeResponse('User not found');\n"
               '        }\n'
               '\n'
               '        $input = Input::all();\n'
               "        unset($input['_method']);\n"
               '\n'
               '        User::find(Auth::id())->update($input);\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('Your "
               "changes have been saved');\n"
               '    }\n'
               '\n'
               '    // Delete the users account\n'
               '    public function deleteUser()\n'
               '    {\n'
               "        Task::where('user_id', Auth::id())->delete();\n"
               "        Credential::where('user_id', Auth::id())->delete();\n"
               "        Project::where('user_id', Auth::id())->delete();\n"
               "        Client::where('user_id', Auth::id())->delete();\n"
               "        User::where('id', Auth::id())->delete();\n"
               '    }\n'
               '\n'
               '}'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=608,
          lineno=21,
          tokens=29,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='index',
          body='public function index()\n'
               '\t{\n'
               "\t\treturn View::make('ins/settings')->with('pTitle', "
               'Auth::user()->full_name);\n'
               '\t}'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=609,
          lineno=27,
          tokens=18,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='logout',
          body='public function logout(){\n'
               '\t\tAuth::logout();\n'
               "\t\treturn Redirect::to('/');\n"
               '\t}'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=610,
          lineno=33,
          tokens=211,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='login',
          body='public function login()\n'
               '\t{\t\t\t\t\n'
               "\t\t$email \t\t=\tInput::get('email');\n"
               "\t\t$password\t=\tInput::get('password');\n"
               '\n'
               '\t\t// lets validate the users input\n'
               '\t\t$validator = Validator::make(\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'email' \t=>\t$email,\n"
               "\t\t\t\t\t'password' \t=> \t$password\n"
               '\t\t\t),\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'email'\t\t=> \t'required|email',\n"
               "\t\t\t\t\t'password'\t=>\t'required'\n"
               '\t\t\t)\n'
               '\t\t);\n'
               '\n'
               '\t\tif ($validator->fails()){\n'
               '\t\t    return '
               'Redirect::back()->withErrors($validator)->withInput();\n'
               '\t\t}else{\n'
               "\t\t\tif( Auth::attempt(array('email' => $email, 'password' => "
               '$password)) ){\t\t\t\t\n'
               "\t\t\t\treturn Redirect::to('hud');\n"
               '\t\t\t}else{\t\t\t\t\n'
               "\t\t\t\t$validator->getMessageBag()->add('input', 'Incorrect "
               "email or password');\n"
               '\t\t\t\treturn '
               'Redirect::back()->withErrors($validator)->withInput();;\n'
               '\t\t\t}\t\t\t\n'
               '\t\t}\n'
               '\t}'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=611,
          lineno=63,
          tokens=233,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='register',
          body='public function register()\n'
               '\t{\t\n'
               "\t\t$fullName\t=\tInput::get('fullName');\n"
               "\t\t$email \t\t=\tInput::get('email');\n"
               "\t\t$password\t=\tInput::get('password');\t\n"
               '\n'
               '\t\t// lets validate the users input\n'
               '\t\t$validator = Validator::make(\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'fullName' \t=> \t$fullName,\n"
               "\t\t\t\t\t'email' \t=>\t$email,\n"
               "\t\t\t\t\t'password' \t=> \t$password\n"
               '\t\t\t),\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'fullName' \t=> \t'required',\n"
               "\t\t\t\t\t'email'\t\t=> \t'required|email|unique:users',\n"
               "\t\t\t\t\t'password'\t=>\t'required|min:8'\n"
               '\t\t\t)\n'
               '\t\t);\n'
               '\n'
               '\t\tif ($validator->fails()){\n'
               '\t\t    return '
               'Redirect::back()->withErrors($validator)->withInput();\n'
               '\t\t}\n'
               '\n'
               '\t\t$user \t\t\t\t=\tnew User;\n'
               '\t\t$user->full_name \t=\t$fullName;\n'
               '\t\t$user->email \t\t=\t$email;\n'
               '\t\t$user->password \t=\tHash::make($password);\n'
               '\n'
               '\t\t$user->save();\t\n'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=612,
          lineno=93,
          tokens=55,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='register',
          body='\n'
               "\t\tif ( Auth::attempt(array('email' => $email, 'password' => "
               '$password)) ) {\n'
               '\t\t\tHelpers::sendWelcomeMail();\n'
               "\t\t\treturn Redirect::to('hud');\n"
               '\t\t}\n'
               '\n'
               '\t\treturn Redirect::back()->withErrors($validator);\n'
               '\t}'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=613,
          lineno=103,
          tokens=243,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='resetPassword',
          body='public function resetPassword($id)\n'
               '\t{\t\t\n'
               '\t\t// ----------------------------------------\n'
               '\t\t$user = User::find(Auth::id());\n'
               '\t\t$created = $user->tasks_created;\n'
               '\t\t$completed = $user->tasks_completed;\n'
               '\n'
               '\t\tif ($created == "") {\n'
               '\t\t\t$created = 0;\n'
               '\t\t}\n'
               '\n'
               '\t\tif ($completed == "") {\n'
               '\t\t\t$completed = 0;\n'
               '\t\t}\n'
               '\t\t// ----------------------------------------\n'
               '\n'
               "\t\t$current_pwd\t=\tInput::get('current_pwd');\n"
               "\t\t$new_pwd\t\t=\tInput::get('new_pwd');\n"
               '\n'
               '\t\t// lets validate the users input\n'
               '\t\t$validator = Validator::make(\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'current_pwd' \t=>\t$current_pwd,\n"
               "\t\t\t\t\t'new_pwd' \t\t=> \t$new_pwd\n"
               '\t\t\t),\n'
               '\t\t\tarray(\n'
               "\t\t\t\t\t'current_pwd'\t=> \t'required',\n"
               "\t\t\t\t\t'new_pwd'\t\t=>\t'required'\n"
               '\t\t\t)\n'
               '\t\t);\n'
               '\n'
               '\t\tif ($validator->fails()){\n'
               '\t\t    return '
               "Redirect::back()->withErrors($validator)->with('user', "
               "$user)->with('created', $created)->with('completed', "
               '$completed);\n'
               '\t\t}\n'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=614,
          lineno=137,
          tokens=159,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='resetPassword',
          body='\n'
               "\t\tif ( !Auth::validate(array('email' => $user->email, "
               "'password' => $current_pwd)) ) {\n"
               "\t\t\t$validator->getMessageBag()->add('password', 'That "
               "password is incorrect');\n"
               '\t\t\treturn '
               "Redirect::back()->withErrors($validator)->with('user', "
               "$user)->with('created', $created)->with('completed', "
               '$completed);\t\n'
               '\t\t}\n'
               '\n'
               '\t\t// Store the new password and redirect;\n'
               '\t\t$user->password = Hash::make($new_pwd);\n'
               '\t\t$user->save();\n'
               '\n'
               '\t\treturn Redirect::back()\n'
               "\t\t\t\t\t\t\t\t->with('user', $user)\n"
               "\t\t\t\t\t\t\t\t->with('created', $created)->with('completed', "
               '$completed)\n'
               '\t\t\t\t\t\t\t\t->with(\'success\', "Your password has been '
               'updated!");\n'
               '\n'
               '\t}'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=615,
          lineno=155,
          tokens=22,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='getUser',
          body='public function getUser(){\n'
               '        $user = User::find(Auth::id());\n'
               '        return $user;\n'
               '    }'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=616,
          lineno=160,
          tokens=161,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='updateUser',
          body='public function updateUser($id){\n'
               "        if (strlen(trim(Input::get('email'))) === 0) {\n"
               '            return '
               "$this->setStatusCode(200)->makeResponse('You need to provide "
               "an email.');\n"
               '        }\n'
               '\n'
               "        if( strlen(trim(Input::get('full_name'))) === 0 ){\n"
               '            return '
               "$this->setStatusCode(200)->makeResponse('You have a name, "
               "no?');\n"
               '        }\n'
               '\n'
               '        if (!User::find(Auth::id())) {\n'
               '            return '
               "$this->setStatusCode(404)->makeResponse('User not found');\n"
               '        }\n'
               '\n'
               '        $input = Input::all();\n'
               "        unset($input['_method']);\n"
               '\n'
               '        User::find(Auth::id())->update($input);\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('Your "
               "changes have been saved');\n"
               '    }'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=617,
          lineno=182,
          tokens=77,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='deleteUser',
          body='public function deleteUser()\n'
               '    {\n'
               "        Task::where('user_id', Auth::id())->delete();\n"
               "        Credential::where('user_id', Auth::id())->delete();\n"
               "        Project::where('user_id', Auth::id())->delete();\n"
               "        Client::where('user_id', Auth::id())->delete();\n"
               "        User::where('id', Auth::id())->delete();\n"
               '    }'),
 Fragment(document_cs='8450d906ba5af2da1aba67b03e56863feb30e6701849128725800600cdce0fbd',
          id=618,
          lineno=1,
          tokens=36,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: deleteUser getUser index login logout register '
               'resetPassword updateUser\n'
               '  Classes: UsersController\n'
               '  Usages: completed created current_pwd email fullName input '
               'new_pwd password this user validator\n'),
 Fragment(document_cs='8486013f307863823b8f2558df6847c71999a6728f2a5942ecf102b203440ef1',
          id=619,
          lineno=8,
          tokens=153,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ClientsTableSeeder',
          body='class ClientsTableSeeder extends Seeder {\n'
               '\n'
               '\tpublic function run()\n'
               '\t{\n'
               '\t\t$faker = Faker::create();\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=0;');\n"
               '\n'
               "\t\tDB::table('clients')->truncate();\n"
               "\t\tDB::table('clients')->insert(\n"
               '\t\t    array(\n'
               "\t\t    \t'name' \t\t\t\t=>\t$faker->name,\n"
               "\t\t    \t'user_id' \t\t\t=> \t1,\n"
               '\t\t    \t\'phone_number\'\t\t=>\t"1-55-555-555",\n'
               "\t\t    \t'point_of_contact' \t=> \t$faker->name,\n"
               '\t\t    \t\'email\'\t\t\t\t=>\t"test@test.com",\n'
               '\t\t    \t)\n'
               '\t\t);\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=1;');\n"
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='8486013f307863823b8f2558df6847c71999a6728f2a5942ecf102b203440ef1',
          id=620,
          lineno=10,
          tokens=145,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='run',
          body='public function run()\n'
               '\t{\n'
               '\t\t$faker = Faker::create();\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=0;');\n"
               '\n'
               "\t\tDB::table('clients')->truncate();\n"
               "\t\tDB::table('clients')->insert(\n"
               '\t\t    array(\n'
               "\t\t    \t'name' \t\t\t\t=>\t$faker->name,\n"
               "\t\t    \t'user_id' \t\t\t=> \t1,\n"
               '\t\t    \t\'phone_number\'\t\t=>\t"1-55-555-555",\n'
               "\t\t    \t'point_of_contact' \t=> \t$faker->name,\n"
               '\t\t    \t\'email\'\t\t\t\t=>\t"test@test.com",\n'
               '\t\t    \t)\n'
               '\t\t);\n'
               '\n'
               "\t\tDB::statement('SET FOREIGN_KEY_CHECKS=1;');\n"
               '\t}'),
 Fragment(document_cs='8486013f307863823b8f2558df6847c71999a6728f2a5942ecf102b203440ef1',
          id=621,
          lineno=1,
          tokens=18,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: run\n'
               '  Classes: ClientsTableSeeder\n'
               '  Usages: faker\n'),
 Fragment(document_cs='848f8a80f1d914e209be7fab69cb6017cf28babb2a7fc4b8170b74e51c9dda85',
          id=622,
          lineno=1,
          tokens=183,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='userObj',
          body='userObj = new Vue({\n'
               "    el: '#user',\n"
               '    data: {\n'
               '        user: {},\n'
               '        delete_text: null,\n'
               '        msg: {error: null, success: null},\n'
               '    },\n'
               '\n'
               '    ready: function(){\n'
               '        this.getUser();\n'
               '    },\n'
               '\n'
               '    methods: {\n'
               '        getUser: function(){\n'
               '            $.get( window.baseurl + "/api/user", function( '
               'result ) {\n'
               '                userObj.user = result;\n'
               '            });\n'
               '        },\n'
               '        update: function(event){\n'
               '            if(event !== undefined) {\n'
               '                event.preventDefault();\n'
               '            }\n'
               '\n'
               '            var data = this.user;\n'
               '\n'
               '            $.ajax({\n'
               '                type: "POST",\n'
               '                url: window.baseurl + "/api/user/"+data.id,\n'
               '                data: data,\n'
               '                success: function(result){\n'
               '                    if(result.message != "Your changes have '
               'been saved"){\n'
               '                        userObj.msg.error = result.message;\n'
               '                        userObj.msg.success = null;\n'
               '                        return false;\n'
               '           '),
 Fragment(document_cs='848f8a80f1d914e209be7fab69cb6017cf28babb2a7fc4b8170b74e51c9dda85',
          id=623,
          lineno=24,
          tokens=4,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='data',
          body='data = this.user'),
 Fragment(document_cs='848f8a80f1d914e209be7fab69cb6017cf28babb2a7fc4b8170b74e51c9dda85',
          id=624,
          lineno=35,
          tokens=150,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='userObj',
          body='         }\n'
               '                    userObj.msg.success = result.message;\n'
               '                    userObj.msg.error = null\n'
               '                },\n'
               '                error: function(e){\n'
               '                    // do nothing\n'
               '                }\n'
               '            });\n'
               '        },\n'
               '        delete: function(){\n'
               '            showSheet();\n'
               '            makePrompt("Are you sure you want to delete your '
               'account","This action is irreversible","No now", "Yes");\n'
               '\n'
               '            $("#cancel-btn").click(function(){\n'
               '                closePrompt();\n'
               '            });\n'
               '\n'
               '            $("#confirm-btn").click(function(){\n'
               '                $.ajax({\n'
               '                    type: "DELETE",\n'
               '                    url: window.baseurl + "/api/user/",\n'
               '                    success: function(result){\n'
               '                        document.location.href="/";\n'
               '                    },\n'
               '                    error: function(e){\n'
               '                        closePrompt();\n'
               '                    }\n'
               '                });\n'
               '            });\n'
               '        }\n'
               '    }\n'
               '\n'
               '})'),
 Fragment(document_cs='848f8a80f1d914e209be7fab69cb6017cf28babb2a7fc4b8170b74e51c9dda85',
          id=625,
          lineno=1,
          tokens=23,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: data userObj\n'
               '  Usages: Vue closePrompt document event makePrompt result '
               'showSheet window\n'),
 Fragment(document_cs='84d9a33bcfdea8b3055de361455540b702e3303fada8be3430af724ea1bf5b16',
          id=626,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='8bcacb08f8360f32c3c6d9b29fffdfa31b8f0d6e65d002a68a34d6d4fae90d27',
          id=627,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='8e49942f299e08f19ceccc1c7efcee40268a8628a6c636a5b3f90981fabaf8ba',
          id=628,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='8f033a2afa170fae8ad73bdac039942438c089694d3f93588f560feabafd2ab5',
          id=629,
          lineno=9,
          tokens=196,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Handler',
          body='class Handler extends ExceptionHandler\n'
               '{\n'
               '    /**\n'
               '     * A list of the exception types that should not be '
               'reported.\n'
               '     *\n'
               '     * @var array\n'
               '     */\n'
               '    protected $dontReport = [\n'
               '        HttpException::class,\n'
               '    ];\n'
               '\n'
               '    /**\n'
               '     * Report or log an exception.\n'
               '     *\n'
               '     * This is a great spot to send exceptions to Sentry, '
               'Bugsnag, etc.\n'
               '     *\n'
               '     * @param  \\Exception  $e\n'
               '     * @return void\n'
               '     */\n'
               '    public function report(Exception $e)\n'
               '    {\n'
               '        return parent::report($e);\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Render an exception into an HTTP response.\n'
               '     *\n'
               '     * @param  \\Illuminate\\Http\\Request  $request\n'
               '     * @param  \\Exception  $e\n'
               '     * @return \\Illuminate\\Http\\Response\n'
               '     */\n'
               '    public function render($request, Exception $e)\n'
               '    {\n'
               '        return parent::render($request, $e);\n'
               '    }\n'
               '}'),
 Fragment(document_cs='8f033a2afa170fae8ad73bdac039942438c089694d3f93588f560feabafd2ab5',
          id=630,
          lineno=28,
          tokens=19,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='report',
          body='public function report(Exception $e)\n'
               '    {\n'
               '        return parent::report($e);\n'
               '    }'),
 Fragment(document_cs='8f033a2afa170fae8ad73bdac039942438c089694d3f93588f560feabafd2ab5',
          id=631,
          lineno=40,
          tokens=25,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='render',
          body='public function render($request, Exception $e)\n'
               '    {\n'
               '        return parent::render($request, $e);\n'
               '    }'),
 Fragment(document_cs='8f033a2afa170fae8ad73bdac039942438c089694d3f93588f560feabafd2ab5',
          id=632,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: render report\n'
               '  Classes: Handler\n'
               '  Usages: dontReport request\n'),
 Fragment(document_cs='90ace4e94f4893f5925b2bd509d514614b863714032bc4cbfb1505dee10b1d43',
          id=633,
          lineno=8,
          tokens=118,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='EventServiceProvider',
          body='class EventServiceProvider extends ServiceProvider\n'
               '{\n'
               '    /**\n'
               '     * The event listener mappings for the application.\n'
               '     *\n'
               '     * @var array\n'
               '     */\n'
               '    protected $listen = [\n'
               "        'App\\Events\\SomeEvent' => [\n"
               "            'App\\Listeners\\EventListener',\n"
               '        ],\n'
               '    ];\n'
               '\n'
               '    /**\n'
               '     * Register any other events for your application.\n'
               '     *\n'
               '     * @param  \\Illuminate\\Contracts\\Events\\Dispatcher  '
               '$events\n'
               '     * @return void\n'
               '     */\n'
               '    public function boot(DispatcherContract $events)\n'
               '    {\n'
               '        parent::boot($events);\n'
               '\n'
               '        //\n'
               '    }\n'
               '}'),
 Fragment(document_cs='90ace4e94f4893f5925b2bd509d514614b863714032bc4cbfb1505dee10b1d43',
          id=634,
          lineno=27,
          tokens=22,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='boot',
          body='public function boot(DispatcherContract $events)\n'
               '    {\n'
               '        parent::boot($events);\n'
               '\n'
               '        //\n'
               '    }'),
 Fragment(document_cs='90ace4e94f4893f5925b2bd509d514614b863714032bc4cbfb1505dee10b1d43',
          id=635,
          lineno=1,
          tokens=18,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: boot\n'
               '  Classes: EventServiceProvider\n'
               '  Usages: events listen\n'),
 Fragment(document_cs='92c524dceadbe8c910e5ffdbf33a7508afdd6f8be7dedaf0876d2e5c05f73173',
          id=636,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='92ee63b62c114fdd5215bf83be657c35e8d31ce2054c76210a94ca57ad9112d8',
          id=637,
          lineno=1,
          tokens=113,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='<IfModule mod_rewrite.c>\n'
               '    <IfModule mod_negotiation.c>\n'
               '        Options -MultiViews\n'
               '    </IfModule>\n'
               '\n'
               '    RewriteEngine On\n'
               '\n'
               '    # Redirect Trailing Slashes If Not A Folder...\n'
               '    RewriteCond %{REQUEST_FILENAME} !-d\n'
               '    RewriteRule ^(.*)/$ /$1 [L,R=301]\n'
               '\n'
               '    # Handle Front Controller...\n'
               '    RewriteCond %{REQUEST_FILENAME} !-d\n'
               '    RewriteCond %{REQUEST_FILENAME} !-f\n'
               '    RewriteRule ^ index.php [L]\n'
               '</IfModule>\n'),
 Fragment(document_cs='92ee63b62c114fdd5215bf83be657c35e8d31ce2054c76210a94ca57ad9112d8',
          id=638,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='95cfcad5856c825b4ac29210c8950f77c4db01099e1c5e62cc8e2885638995c8',
          id=639,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='970c1ef1665a4131b7454f45c4621c233aa51a7c78adb5021889d8524efb865e',
          id=640,
          lineno=1,
          tokens=11,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='elixir',
          body="elixir = require('laravel-elixir')"),
 Fragment(document_cs='970c1ef1665a4131b7454f45c4621c233aa51a7c78adb5021889d8524efb865e',
          id=641,
          lineno=1,
          tokens=14,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: elixir\n  Usages: mix require\n'),
 Fragment(document_cs='97e3b39e30d7ad61e82b45ce047519ea3ffe40b1b4d405cdeed12f8591ed0a4e',
          id=642,
          lineno=13,
          tokens=246,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='RouteServiceProvider',
          body='class RouteServiceProvider extends ServiceProvider\n'
               '{\n'
               '    /**\n'
               '     * This namespace is applied to the controller routes in '
               'your routes file.\n'
               '     *\n'
               "     * In addition, it is set as the URL generator's root "
               'namespace.\n'
               '     *\n'
               '     * @var string\n'
               '     */\n'
               "    protected $namespace = 'App\\Http\\Controllers';\n"
               '\n'
               '    /**\n'
               '     * Define your route model bindings, pattern filters, '
               'etc.\n'
               '     *\n'
               '     * @param  \\Illuminate\\Routing\\Router  $router\n'
               '     * @return void\n'
               '     */\n'
               '    public function boot(Router $router)\n'
               '    {\n'
               "        $router->filter('auth', function()\n"
               '        {\n'
               '        \tif (Auth::guest())\n'
               '        \t{\n'
               '        \t\tif (Request::ajax())\n'
               '        \t\t{\n'
               "        \t\t\treturn Response::make('Unauthorized', 401);\n"
               '        \t\t}\n'
               '        \t\telse\n'
               '        \t\t{\n'
               "        \t\t\treturn Redirect::guest('/');\n"
               '        \t\t}\n'
               '        \t}\n'
               '        });\n'
               '\n'
               "        $router->filter('auth.basic', function()\n"
               '        {\n'
               '        \treturn Auth::basic();\n'
               '        });\n'
               '\n'
               "        $router->filter('guest', function()\n"
               '        {\n'
               "        \tif (Auth::check()) return Redirect::to('/');\n"
               '        });\n'
               '\n'
               "        $router->filter('admin', function()\n"
               '        {\n'
               '        \tif (Auth::check())\n'
               '        \t{\n'),
 Fragment(document_cs='97e3b39e30d7ad61e82b45ce047519ea3ffe40b1b4d405cdeed12f8591ed0a4e',
          id=643,
          lineno=61,
          tokens=131,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='RouteServiceProvider',
          body='        \t\tif (Auth::user()->email != "ceesco53@gmail.com")\n'
               '        \t\t{\n'
               "        \t\t\treturn Redirect::to('/');\n"
               '        \t\t}\n'
               '        \t}else{\n'
               "        \t\treturn Redirect::to('/');\n"
               '        \t}\n'
               '        });\n'
               '\n'
               '        parent::boot($router);\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Define the routes for the application.\n'
               '     *\n'
               '     * @param  \\Illuminate\\Routing\\Router  $router\n'
               '     * @return void\n'
               '     */\n'
               '    public function map(Router $router)\n'
               '    {\n'
               "        $router->group(['namespace' => $this->namespace], "
               'function ($router) {\n'
               "            require app_path('Http/routes.php');\n"
               '        });\n'
               '    }\n'
               '}'),
 Fragment(document_cs='97e3b39e30d7ad61e82b45ce047519ea3ffe40b1b4d405cdeed12f8591ed0a4e',
          id=644,
          lineno=30,
          tokens=197,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='boot',
          body='public function boot(Router $router)\n'
               '    {\n'
               "        $router->filter('auth', function()\n"
               '        {\n'
               '        \tif (Auth::guest())\n'
               '        \t{\n'
               '        \t\tif (Request::ajax())\n'
               '        \t\t{\n'
               "        \t\t\treturn Response::make('Unauthorized', 401);\n"
               '        \t\t}\n'
               '        \t\telse\n'
               '        \t\t{\n'
               "        \t\t\treturn Redirect::guest('/');\n"
               '        \t\t}\n'
               '        \t}\n'
               '        });\n'
               '\n'
               "        $router->filter('auth.basic', function()\n"
               '        {\n'
               '        \treturn Auth::basic();\n'
               '        });\n'
               '\n'
               "        $router->filter('guest', function()\n"
               '        {\n'
               "        \tif (Auth::check()) return Redirect::to('/');\n"
               '        });\n'
               '\n'
               "        $router->filter('admin', function()\n"
               '        {\n'
               '        \tif (Auth::check())\n'
               '        \t{\n'
               '        \t\tif (Auth::user()->email != "ceesco53@gmail.com")\n'
               '        \t\t{\n'
               "        \t\t\treturn Redirect::to('/');\n"
               '        \t\t}\n'
               '        \t}else{\n'
               "        \t\treturn Redirect::to('/');\n"
               '        \t}\n'
               '        });\n'
               '\n'
               '        parent::boot($router);\n'
               '    }'),
 Fragment(document_cs='97e3b39e30d7ad61e82b45ce047519ea3ffe40b1b4d405cdeed12f8591ed0a4e',
          id=645,
          lineno=79,
          tokens=42,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='map',
          body='public function map(Router $router)\n'
               '    {\n'
               "        $router->group(['namespace' => $this->namespace], "
               'function ($router) {\n'
               "            require app_path('Http/routes.php');\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='97e3b39e30d7ad61e82b45ce047519ea3ffe40b1b4d405cdeed12f8591ed0a4e',
          id=646,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: boot map\n'
               '  Classes: RouteServiceProvider\n'
               '  Usages: namespace router this\n'),
 Fragment(document_cs='99dfe2afcf157ea435460a80a00de062d193d0ae14bd9e8c68335b3925707ffe',
          id=647,
          lineno=1,
          tokens=14,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// @import '
               '"node_modules/bootstrap-sass/assets/stylesheets/bootstrap";\n'
               '\n'),
 Fragment(document_cs='99dfe2afcf157ea435460a80a00de062d193d0ae14bd9e8c68335b3925707ffe',
          id=648,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='99f140f6ba62efbda2470bdbd7afb1f1c9541457fa1662d2f6540f9b5b3ac231',
          id=649,
          lineno=1,
          tokens=203,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#!/usr/bin/env php\n'
               '<?php\n'
               '\n'
               '/*\n'
               '|--------------------------------------------------------------------------\n'
               '| Register The Auto Loader\n'
               '|--------------------------------------------------------------------------\n'
               '|\n'
               '| Composer provides a convenient, automatically generated '
               'class loader\n'
               "| for our application. We just need to utilize it! We'll "
               'require it\n'
               '| into the script here so that we do not have to worry about '
               'the\n'
               '| loading of any our classes "manually". Feels great to '
               'relax.\n'
               '|\n'
               '*/\n'
               '\n'
               "require __DIR__.'/bootstrap/autoload.php';\n"
               '\n'
               "$app = require_once __DIR__.'/bootstrap/app.php';\n"
               '\n'
               '/*\n'
               '|--------------------------------------------------------------------------\n'
               '| Run The Artisan Application\n'
               '|--------------------------------------------------------------------------\n'
               '|\n'
               '| When we run the console application, the current CLI command '
               'will be\n'
               '| executed in this console and the response sent back to a '
               'terminal\n'
               '| or another output device for the developers. Here goes '
               'nothing!\n'
               '|\n'
               '*/\n'
               '\n'
               '$kernel = '
               '$app->make(Illuminate\\Contracts\\Console\\Kernel::class);\n'
               '\n'
               '$status = $kernel->handle(\n'
               '    $input = new '
               'Symfony\\Component\\Console\\Input\\ArgvInput,\n'
               '    new Symfony\\Component\\Console\\Output\\ConsoleOutput\n'
               ');\n'),
 Fragment(document_cs='99f140f6ba62efbda2470bdbd7afb1f1c9541457fa1662d2f6540f9b5b3ac231',
          id=650,
          lineno=37,
          tokens=74,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '/*\n'
               '|--------------------------------------------------------------------------\n'
               '| Shutdown The Application\n'
               '|--------------------------------------------------------------------------\n'
               '|\n'
               '| Once Artisan has finished running. We will fire off the '
               'shutdown events\n'
               '| so that any final work may be done by the application before '
               'we shut\n'
               '| down the process. This is the last thing to happen to the '
               'request.\n'
               '|\n'
               '*/\n'
               '\n'
               '$kernel->terminate($input, $status);\n'
               '\n'
               'exit($status);\n'),
 Fragment(document_cs='99f140f6ba62efbda2470bdbd7afb1f1c9541457fa1662d2f6540f9b5b3ac231',
          id=651,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='9c8ff53a87d45150f45dd32740f8de9c295d7cc81d76a4671b971063f46e07df',
          id=652,
          lineno=6,
          tokens=1,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='megaMenuInit',
          body='function'),
 Fragment(document_cs='9c8ff53a87d45150f45dd32740f8de9c295d7cc81d76a4671b971063f46e07df',
          id=653,
          lineno=36,
          tokens=1,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='showSheet',
          body='function'),
 Fragment(document_cs='9c8ff53a87d45150f45dd32740f8de9c295d7cc81d76a4671b971063f46e07df',
          id=654,
          lineno=41,
          tokens=1,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='makePrompt',
          body='function'),
 Fragment(document_cs='9c8ff53a87d45150f45dd32740f8de9c295d7cc81d76a4671b971063f46e07df',
          id=655,
          lineno=52,
          tokens=1,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='closePrompt',
          body='function'),
 Fragment(document_cs='9c8ff53a87d45150f45dd32740f8de9c295d7cc81d76a4671b971063f46e07df',
          id=656,
          lineno=13,
          tokens=12,
          depth=8,
          parent_id=None,
          category='variable',
          summary=False,
          name='id',
          body='id = "#" + $(this).attr("data-id")'),
 Fragment(document_cs='9c8ff53a87d45150f45dd32740f8de9c295d7cc81d76a4671b971063f46e07df',
          id=657,
          lineno=42,
          tokens=12,
          depth=3,
          parent_id=None,
          category='variable',
          summary=False,
          name='newMarginTop',
          body='newMarginTop = $(document).scrollTop() + 100'),
 Fragment(document_cs='9c8ff53a87d45150f45dd32740f8de9c295d7cc81d76a4671b971063f46e07df',
          id=658,
          lineno=1,
          tokens=33,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: closePrompt makePrompt megaMenuInit showSheet\n'
               '  Variables: newMarginTop\n'
               '  Usages: cancelTxt confirmTxt document event msg title\n'),
 Fragment(document_cs='9ecb47cf9e345bed2e95780f56eec3761073aa7a7961dd6705dd8fb8e5194ae0',
          id=659,
          lineno=7,
          tokens=45,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='EncryptCookies',
          body='class EncryptCookies extends BaseEncrypter\n'
               '{\n'
               '    /**\n'
               '     * The names of the cookies that should not be encrypted.\n'
               '     *\n'
               '     * @var array\n'
               '     */\n'
               '    protected $except = [\n'
               '        //\n'
               '    ];\n'
               '}'),
 Fragment(document_cs='9ecb47cf9e345bed2e95780f56eec3761073aa7a7961dd6705dd8fb8e5194ae0',
          id=660,
          lineno=1,
          tokens=12,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: EncryptCookies\n  Usages: except\n'),
 Fragment(document_cs='a08e69c07e5a23e56f4343b878c27636d17c34734a996d10b392439542f912b7',
          id=661,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='a246a0ba35c2aed4de261cf7e91f4d563c3f81523f23011afdb583a81f2b67ee',
          id=662,
          lineno=6,
          tokens=114,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AddPriorityColumnToTasks',
          body='class AddPriorityColumnToTasks extends Migration\n'
               '{\n'
               '    /**\n'
               '     * Run the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function up()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->string('priority');\n"
               '        });\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Reverse the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function down()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->dropColumn('priority');\n"
               '        });\n'
               '    }\n'
               '}'),
 Fragment(document_cs='a246a0ba35c2aed4de261cf7e91f4d563c3f81523f23011afdb583a81f2b67ee',
          id=663,
          lineno=13,
          tokens=32,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->string('priority');\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='a246a0ba35c2aed4de261cf7e91f4d563c3f81523f23011afdb583a81f2b67ee',
          id=664,
          lineno=25,
          tokens=33,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->dropColumn('priority');\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='a246a0ba35c2aed4de261cf7e91f4d563c3f81523f23011afdb583a81f2b67ee',
          id=665,
          lineno=1,
          tokens=21,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: AddPriorityColumnToTasks\n'
               '  Usages: table\n'),
 Fragment(document_cs='a25d59a614086be9b7ee608c6c39492c7b83c2e6dfb4953eace4acc723822025',
          id=666,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='a5ae3804057c2e55f674d441eec9c3b4f76bb55ec457587622f22c3c1703d1b7',
          id=667,
          lineno=1,
          tokens=3,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='*.sqlite\n'),
 Fragment(document_cs='a5ae3804057c2e55f674d441eec9c3b4f76bb55ec457587622f22c3c1703d1b7',
          id=668,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='a64b78cd838229e72653445fb78467b47aea20ce69f443f23bee475cb83fc47f',
          id=669,
          lineno=6,
          tokens=115,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AddExtraTaskColumns',
          body='class AddExtraTaskColumns extends Migration\n'
               '{\n'
               '    /**\n'
               '     * Run the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function up()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->string('due_date');\n"
               '        });\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Reverse the migrations.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function down()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->dropColumn(['due_date']);\n"
               '        });\n'
               '    }\n'
               '}'),
 Fragment(document_cs='a64b78cd838229e72653445fb78467b47aea20ce69f443f23bee475cb83fc47f',
          id=670,
          lineno=13,
          tokens=33,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->string('due_date');\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='a64b78cd838229e72653445fb78467b47aea20ce69f443f23bee475cb83fc47f',
          id=671,
          lineno=25,
          tokens=34,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body='public function down()\n'
               '    {\n'
               "        Schema::table('tasks', function (Blueprint $table) {\n"
               "            $table->dropColumn(['due_date']);\n"
               '        });\n'
               '    }'),
 Fragment(document_cs='a64b78cd838229e72653445fb78467b47aea20ce69f443f23bee475cb83fc47f',
          id=672,
          lineno=1,
          tokens=20,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: AddExtraTaskColumns\n'
               '  Usages: table\n'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=673,
          lineno=1,
          tokens=135,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='client',
          body='client = new Vue({\n'
               "  el: '#client',\n"
               '  data: {\n'
               '    clients: [],\n'
               '    client: null,\n'
               '    currentClient: null,\n'
               '    newProjectClientId: {name: null, project_id: null},\n'
               '    newProject: {name: null, project_id: null},\n'
               '    tempClientIndex: null,\n'
               '    lastRequest: false,\n'
               '    msg: {success: null, error: null}\n'
               '  },\n'
               '\n'
               '  ready: function(){\n'
               '  \tthis.getClients();\n'
               '  },\n'
               '\n'
               '  methods: {\n'
               '  \tgetClients: function(){\n'
               '        $.get( window.baseurl + "/api/clients/true", function( '
               'results ) {\n'
               '            client.clients = results.data;\n'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=674,
          lineno=22,
          tokens=241,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='client',
          body='            Vue.nextTick(function () {\n'
               '                megaMenuInit();\n'
               '            })\n'
               '        }).fail(function(e){\n'
               '            console.log( e );\n'
               '        });\n'
               '  \t},\n'
               '    showCreateForm: function(){\n'
               '          this.msg.success = null;\n'
               '          this.msg.error = null;\n'
               '          $(".new-client").show();\n'
               '          $(".new-client .first").focus();\n'
               '      },\n'
               '  \tcreate: function(new_client, update){\n'
               '\n'
               '\t\tupdate = update || false;\n'
               '\n'
               '\t\t$.ajax({\n'
               "\t\t  type: 'POST',\n"
               '\t\t  url: window.baseurl + "/api/clients",\n'
               '\t\t  data: new_client,\n'
               '\t\t  error: function(e) {\n'
               '\t\t    var response = jQuery.parseJSON(e.responseText);\n'
               '\t\t  \t$(\'.new-client .status-msg\').text("")\n'
               "\t\t  \t\t\t\t\t\t\t\t.removeClass('success-msg')\n"
               '\t\t  \t\t\t\t\t\t\t\t.addClass("error-msg")\n'
               '\t\t  \t\t\t\t\t\t\t\t.text(response.message);\t\t\t    \n'
               '\t\t  \treturn false;\n'
               '\t\t  },\n'
               '\n'
               '\t\t  success: function(result){\t\t\t  \t\t  \t\n'
               '\t\t  \t$(\'.new-client .status-msg\').text("")\n'
               '\t\t  \t\t\t\t\t\t\t\t'
               ".removeClass('remove-msg')\t\t  \t\t\t\t\t\t\t\t\n"
               '\t\t  \t\t\t\t\t\t\t\t.addClass("success-msg")\n'
               '\t\t  \t\t\t\t\t\t\t\t.text(result.message);\n'
               '\t\t\t\t\t\t\n'
               '\t\t\tif (update == true){\n'
               '                result.data.projects = [];\n'
               '\t\t  \t\tclient.clients.push(result.data);\n'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=675,
          lineno=44,
          tokens=8,
          depth=18,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body='response = jQuery.parseJSON(e.responseText)'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=676,
          lineno=61,
          tokens=221,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='client',
          body='\t\t\t\tVue.nextTick(function () {\n'
               '\t\t\t\t\tmegaMenuInit();\n'
               '\t\t\t\t})\t\t  \t\t\n'
               '\t\t  \t}\n'
               '\n'
               '\t\t  \tnew_client.name = null;\n'
               '\t\t  \tnew_client.phone_number = null;\n'
               '\t\t  \tnew_client.point_of_contact = null;\n'
               '\t\t  \tnew_client.email = null;\n'
               '            '
               "$('.popup-form.new-client').find('input[type=text],textarea,select').filter(':visible:first').focus();\n"
               '          }\n'
               '\t\t}); \n'
               '  \t},\n'
               '\tstartClientEditMode: function(clientIndex){\n'
               '        this.msg.success = null;\n'
               '        this.msg.error = null;\n'
               '        this.currentClient = this.clients[clientIndex];\n'
               '        this.currentClient.position = clientIndex;\n'
               '\n'
               '        $(".popup-form.update-client").show();\n'
               '        '
               '$(".popup-form.update-client").find(\'input[type=text],textarea,select\').filter(\':visible:first\').focus();\n'
               '    },\n'
               '    updateClient: function(){\n'
               '\n'
               '        var data = this.currentClient;\n'
               '        var id = data.id;\n'
               '        data._method = "put";\n'
               '\n'
               '        $.ajax({\n'
               '            type: "POST",\n'
               '            url: window.baseurl + "/api/clients/"+id,\n'
               '            data: data,\n'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=677,
          lineno=85,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='data',
          body='data = this.currentClient'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=678,
          lineno=86,
          tokens=4,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='id',
          body='id = data.id'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=679,
          lineno=93,
          tokens=178,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='client',
          body='            success: function(e){\n'
               '                console.log(e);\n'
               '                client.msg.success = e.message;\n'
               '                client.msg.error = null;\n'
               '            },\n'
               '            error: function(e){\n'
               '                var response = '
               'jQuery.parseJSON(e.responseText);\n'
               '                client.msg.success = null;\n'
               '                client.msg.error = response.message;\n'
               '            }\n'
               '        });\n'
               '    },\n'
               '    deleteClient: function(currentClient, clientIndex){\n'
               '        this.currentClient = currentClient;\n'
               '\n'
               '        showSheet();\n'
               '        makePrompt(\n'
               '            "Are you sure you want to delete the client: '
               '"+currentClient.name+"?",\n'
               '            "By deleting this client you will loose all data '
               'associated with any project under this client",\n'
               '            "Not now", "Yes");\n'
               '\n'
               '        $("#cancel-btn").click(function(){\n'
               '            closePrompt();\n'
               '        });\n'
               '\n'
               '        $("#confirm-btn").click(function(){\n'
               '            $.ajax({\n'
               '                type: "POST",\n'
               '                url: window.baseurl + "/api'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=680,
          lineno=99,
          tokens=8,
          depth=18,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body='response = jQuery.parseJSON(e.responseText)'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=681,
          lineno=121,
          tokens=171,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='client',
          body='/clients/"+currentClient.id,\n'
               '                data: {_method: "delete"},\n'
               '                success: function(){\n'
               '                    client.clients.splice(clientIndex);\n'
               '                    client.currentClient = null;\n'
               '\n'
               '                    $(".mega-menu .links '
               'a").removeClass("active").addClass("inactive");\n'
               '                    $(".mega-menu .links '
               'a:first-child").removeClass("inactive").addClass("active");\n'
               '                    $(".mega-menu .content .item").hide();\n'
               '                    var id = "#" + $(".mega-menu .content '
               'div:first-child").show();\n'
               '\n'
               '                    closePrompt();\n'
               '                },\n'
               '                error: function(){\n'
               '                    client.currentClient = null;\n'
               '                    closePrompt();\n'
               '                }\n'
               '            });\n'
               '        });\n'
               '    },\n'
               '    showNewProjectForm: function(clientId, clientIndex){\n'
               '\n'
               '        this.msg.success = null;\n'
               '        this.msg.error = null;\n'
               '        this.newProject.client_id = clientId;\n'
               '        this.tempClientIndex = clientInd'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=682,
          lineno=130,
          tokens=15,
          depth=23,
          parent_id=None,
          category='variable',
          summary=False,
          name='id',
          body='id = "#" + $(".mega-menu .content div:first-child").show()'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=683,
          lineno=146,
          tokens=189,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='client',
          body='ex;\n'
               '\n'
               '        $(".popup-form.new-project").show();\n'
               '        $(".popup-form.new-project .first").focus();\n'
               '    },\n'
               '  \tcreateProject: function(){\n'
               '\n'
               '\t\t $.ajax({\n'
               "\t\t   type: 'POST',\n"
               '\t\t   url: window.baseurl + "/api/projects",\n'
               '\t\t   data: client.newProject,\n'
               '\t\t   error: function(e) {\n'
               '               var response = '
               'jQuery.parseJSON(e.responseText);\n'
               '               client.msg.success = null;\n'
               '               client.msg.error = response.message;\n'
               '\t\t   },\n'
               '\t\t    success: function(result){\n'
               '                console.log(client.clients);\n'
               '                console.log(result);\n'
               '                '
               'client.clients[client.tempClientIndex].projects.push(result.data);\n'
               '                client.msg.success = result.message;\n'
               '                client.msg.error = null;\n'
               '\n'
               '                client.newProject.name = null;\n'
               '                client.newProject.project_id = null;\n'
               '                '
               "$('.popup-form.new-project').find('input[type=text],textarea,select').filter(':visible:first').focus();\n"
               '            }\n'
               '\t\t });\n'
               '  \t}\n'
               '  }\n'
               '\n'
               '})'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=684,
          lineno=158,
          tokens=8,
          depth=18,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body='response = jQuery.parseJSON(e.responseText)'),
 Fragment(document_cs='a779859b5dfefc34ca8ce37e087337c9df8edd24ba4b968692f9e4532231eb5c',
          id=685,
          lineno=1,
          tokens=35,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: client data response\n'
               '  Usages: Vue clientId clientIndex closePrompt console '
               'currentClient jQuery makePrompt megaMenuInit new_client result '
               'results showSheet update window\n'),
 Fragment(document_cs='a7ff4b516dd788a9b584cfbdcafda2ccd2cf248b281c106fc4b5bbd4a72bfc5a',
          id=686,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=687,
          lineno=1,
          tokens=152,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='{\n'
               '"version": 3,\n'
               '"mappings": '
               '"AAYA,UAAS;EACR,WAAW,EAAE,uBAAuB;EACpC,SAAS,EAAE,IAAI;EACf,MAAM,EAAE,IAAI;EACZ,KAAK,EAPe,IAAI;EAQxB,gBAAgB,EAhBE,OAAO;;AAmB1B,sBAAiB;EAChB,WAAW,EAAE,6BAA6B;EAC1C,WAAW,EAAE,GAAG;;AAGjB,CAAC;EACC,KAAK,EAxBe,OAAO;;'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=688,
          lineno=3,
          tokens=140,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AA0B7B,OAAO;EACL,eAAe,EAAE,IAAI;EACrB,KAAK,EA3Bc,OAAO;;AA+B5B,kBAAkB;EACd,OAAO,EAAE,SAAS;EACrB,MAAM,EAAE,IAAI;;AAEb;2BAC2B;EAC1B,UAAU,EAAE,IAAI;EAChB,YAAY,EAvCS,OAAO;;AA0C7B,GAAG;EACD,SAAS,EAAE,IAAI;;AAGjB,cAAc;E'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=689,
          lineno=3,
          tokens=132,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='ACZ,SAAS,EAAE,GAAG;;AAIhB,cAAc;EAAC,KAAK,EAnDE,OAAO;;AAoD7B,YAAY;EAAC,KAAK,EAhDJ,OAAO;;AAkDrB,gBAAgB;EAAC,YAAY,EAAE,CAAC;;AAChC,iBAAiB;EAAC,aAAa,EAAE,CAAC;;AAClC,gBAAgB;EAAC,YAAY,EAAE,CAAC;EAAE,aAAa,EAAE,CAAC;;A'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=690,
          lineno=3,
          tokens=135,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AElD,cAAc;EAAC,OAAO,EAAE,IAAI;;AAG5B,WAAW;EACT,OAAO,EAAE,IAAI;EACb,OAAO,EAAC,KAAK;EACb,UAAU,EAAE,MAAM;EAClB,aAAa,EAAE,GAAG;EAClB,KAAK,EAAE,IAAI;;AAEb,qBAAqB;EAAC,gBAAgB,EAAE,OAAkB;;AAC1D,uBAAuB;EAAC,gBAAgB,EAAE,O'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=691,
          lineno=3,
          tokens=137,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAO;;AAEjD,SAAS;EACP,UAAU,EAAC,MAAM;;AAGnB,IAAI;EACH,OAAO,EAAE,EAAE;;AAGZ,OAAO;EACL,aAAa,EAAE,IAAI;;AAGrB,OAAO;EACN,gBAAgB,EAhFH,OAAO;EAiFpB,KAAK,EAAE,OAAO;EACd,OAAO,EAAE,OAAO;EACb,aAAa,EAAE,IAAI;EACnB,SAAS,EAAE'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=692,
          lineno=3,
          tokens=138,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=',IAAI;;AAInB,MAAM;EACL,UAAU,EAAE,IAAI;EAChB,kBAAkB,EAAE,IAAI;EACxB,eAAe,EAAE,IAAI;;AAEtB,qBAAqB;EACpB,gBAAgB,EA7FK,OAAO;EA8F5B,KAAK,EAAE,wBAAoB;EAC3B,SAAS,EAAE,KAAK;EAChB,OAAO,EAAE,IAAI;;AAEd,6BAA6B;EAC5B,OAAO,EA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=693,
          lineno=3,
          tokens=140,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AE,CAAC;;AAEX,mBAAmB;EAClB,OAAO,EAAE,KAAK;EACd,OAAO,EAAE,QAAQ;EACjB,WAAW,EAAE,cAAc;EAC3B,mBAAmB,EAAE,GAAG;EACxB,KAAK,EAAE,IAAI;EACX,SAAS,EAAE,GAAG;EACd,aAAa,EAAE,iBAAiB;;AAEjC,yBAAyB;EACxB,iBAAiB,EApHI,OAAO;EAqH5'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=694,
          lineno=3,
          tokens=137,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='B,gBAAgB,EAAE,OAAO;EACzB,eAAe,EAAE,IAAI;;AAEtB,+BAA+B;EAC7B,YAAY,EAAE,IAAI;;AAEpB,oCAAoC;EAClC,SAAS,EAAE,IAAI;;AAEjB,+BAA+B;EAC9B,aAAa,EAAE,CAAC;EAChB,OAAO,EAAE,IAAI;;AAKd,SAAS;EACR,QAAQ,EAAE,KAAK;EACf,GAAG,EAAE,'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=695,
          lineno=3,
          tokens=141,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='CAAC;EACN,IAAI,EAAE,CAAC;EACP,KAAK,EAAE,KAAK;EACZ,MAAM,EAAE,IAAI;EACZ,gBAAgB,EA1II,OAAO;EA2I3B,KAAK,EAAE,wBAAoB;;AAE5B,WAAW;EACV,KAAK,EAAE,wBAAoB;EAC3B,mBAAmB,EAAE,GAAG;;AAEzB,iBAAiB;EAChB,KAAK,EAAE,IAAI;EACX,eA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=696,
          lineno=3,
          tokens=139,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Ae,EAAE,IAAI;;AAEtB,uBAAuB;EACtB,OAAO,EAAE,KAAK;EACd,OAAO,EAAE,SAAS;EAClB,WAAW,EAAE,mBAAmB;EAChC,SAAS,EAAE,KAAK;EAChB,UAAU,EAAE,IAAI;EAChB,gBAAgB,EA5JK,OAAO;;AA8J7B,yBAAyB;EAAC,KAAK,EAAE,IAAI;EAAE,aAAa,EAAE,CAAC;'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=697,
          lineno=3,
          tokens=135,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=';AACvD,+BAA+B;EAAC,eAAe,EAAE,IAAI;;AACrD,uBAAuB;EAAC,OAAO,EAAE,IAAI;EAAE,UAAU,EAAE,MAAM;;AACzD,yBAAyB;EAAC,KAAK,EAAE,IAAI;EAAE,UAAU,EAAE,MAAM;;AACzD,2BAA2B;EAC1B,KAAK,EAAE,IAAI;EACR,MAAM,EAAE,IAAI;EACZ,aAAa,EAAE'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=698,
          lineno=3,
          tokens=142,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=',IAAI;EACnB,OAAO,EAAE,KAAK;EACd,MAAM,EAAE,MAAM;;AAElB,uBAAuB;EACtB,aAAa,EAAE,CAAC;EACb,MAAM,EAAE,IAAI;EACZ,gBAAgB,EAAE,wBAAoB;EACtC,OAAO,EAAE,SAAS;EAClB,KAAK,EAAE,IAAI;;AAEf,6BAA6B;EAC5B,eAAe,EAAE,IAAI;EACrB,kBAA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=699,
          lineno=3,
          tokens=134,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='kB,EAAE,IAAI;EACxB,UAAU,EAAE,IAAI;;AAEjB,kBAAkB;EACjB,SAAS,EAAE,KAAK;EAChB,YAAY,EAnDM,IAAI;EAoDtB,aAAa,EApDK,IAAI;EAqDtB,KAAK,EAAE,wBAAoB;;AAE5B,iBAAiB;EAChB,OAAO,EAAE,KAAK;EACd,SAAS,EAAE,KAAK;EAChB,UAAU,EAAE,UA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=700,
          lineno=3,
          tokens=140,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AU;EACtB,OAAO,EAAE,QAAQ;EACjB,WAAW,EAAE,iBAA6B;;AAE3C;wBACwB;EACvB,WAAW,EAAE,iBAA8B;EAC3C,KAAK,EAAE,IAAI;;AAEZ,4BAA4B;EAAC,UAAU,EAAE,IAAI;;AAC7C,eAAe;EACX,YAAY,EArEG,IAAI;EAsEnB,aAAa,EAtEE,IAAI;;AAwEvB,mBAAmB;EAC'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=701,
          lineno=3,
          tokens=139,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='lB,OAAO,EAAE,YAAY;EACrB,KAAK,EAAE,IAAI;EACX,SAAS,EAAE,KAAK;EAChB,aAAa,EAAE,IAAI;;AAEpB,8BAA8B;EAC7B,QAAQ,EAAE,QAAQ;EAClB,GAAG,EAAE,GAAG;;AAET,kBAAkB;EACjB,UAAU,EAAE,IAAI;EACb,MAAM,EAAE,GAAG;EACX,gBAAgB,EAAE,wBAAo'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=702,
          lineno=3,
          tokens=137,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='B;EACtC,UAAU,EAAE,IAAI;;AAEpB,iBAAiB;EAChB,YAAY,EAzFM,IAAI;EA0FtB,aAAa,EA1FK,IAAI;;AA4FvB,iBAAkB;EAAC,UAAU,EAAE,MAAM;;AACrC,mBAAmB;EAAC,SAAS,EAAE,IAAI;;AAGnC,IAAI;EACH,OAAO,EAAE,SAAS;EAClB,MAAM,EAAE,IAAI;EACZ,mBA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=703,
          lineno=3,
          tokens=137,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AmB,EAAE,GAAG;EACxB,kBAAkB,EAAE,4BAAwB;EAC5C,eAAe,EAAE,4BAAwB;EACzC,UAAU,EAAE,4BAAwB;;AAErC,UAAU;EACT,OAAO,EAAE,GAAG;;AAEb;WACW;EACT,OAAO,EAAE,IAAI;EACb,MAAM,EAAE,IAAI;;AAEd,aAAa;EACX,KAAK,EAAE,IAAI;;AAEb,YAAY;E'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=704,
          lineno=3,
          tokens=145,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='ACV,gBAAgB,EAlPG,OAAO;;AAoP5B,gBAAgB;EACf,gBAAgB,EA3PK,OAAO;;AA6P7B,yBAAyB;EACvB,KAAK,EA9Pe,OAAO;EA+P3B,MAAM,EAAE,iBAA8B;EACtC,UAAU,EAAE,WAAW;EACvB,UAAU,EAAE,IAAI;;AAElB,+BAA+B;EAC7B,gBAAgB,EApQI,OAAO;EAqQ3B,KAAK'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=705,
          lineno=3,
          tokens=138,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=',EAAE,IAAI;;AAEb,YAAY;EACV,gBAAgB,EAAE,OAAO;EACzB,KAAK,EAAE,IAAI;EACX,SAAS,EAAE,KAAK;EAChB,WAAW,EAAE,OAAO;EACpB,cAAc,EAAE,GAAG;EACnB,OAAO,EAAE,UAAU;EACnB,UAAU,EAAE,IAAI;;AAElB,kBAAkB;EACjB,gBAAgB,EAAE,OAAO;EACzB'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=706,
          lineno=3,
          tokens=134,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=',KAAK,EAAE,IAAI;;AAGZ,WAAW;EACV,QAAQ,EAAE,KAAK;EACf,MAAM,EAAE,CAAC;EACT,KAAK,EAAE,IAAI;EACX,KAAK,EAAE,KAAK;EACZ,SAAS,EAAE,KAAK;EAChB,gBAAgB,EAAE,IAAI;EACtB,UAAU,EAAE,gCAA4B;EACxC,kBAAkB,EAAE,gCAA4B;EAChD,eAAe,EAA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=707,
          lineno=3,
          tokens=139,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='E,gCAA4B;EAC7C,OAAO,EAAE,IAAI;;AAEd,kBAAkB;EACjB,OAAO,EAAE,IAAI;EACb,UAAU,EAlSU,OAAO;EAmS3B,KAAK,EAAE,IAAI;;AAEZ,oBAAoB;EACnB,aAAa,EAAE,CAAC;;AAEjB,6BAA6B;EAC5B,KAAK,EAAE,IAAI;EACX,mBAAmB,EAAE,GAAG;EACxB,OAAO,EA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=708,
          lineno=3,
          tokens=138,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AE,EAAE;;AAEZ,mCAAmC;EAClC,OAAO,EAAE,CAAC;EACV,MAAM,EAAE,OAAO;;AAEhB,0CAA0C;EACzC,YAAY,EAAE,IAAI;;AAEnB,qBAAqB;EACpB,mBAAmB,EAAE,GAAG;EACxB,MAAM,EAAE,eAAe;;AAExB,mBAAmB;EAClB,OAAO,EAAE,IAAI;EACV,cAAc,EAAE,IAAI;;A'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=709,
          lineno=3,
          tokens=143,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AExB,kBAAkB;EACjB,KAAK,EAAE,IAAI;EACX,OAAO,EAAE,IAAI;EACb,QAAQ,EAAE,QAAQ;EAClB,MAAM,EAAE,CAAC;EACT,gBAAgB,EAAE,OAAO;;AAE1B,4BAA4B;EAC3B,QAAQ,EAAE,MAAM;;AAEjB,yBAAyB;EACvB,aAAa,EAAE,IAAI;;AAErB;uBACuB;EACrB,MAAM,E'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=710,
          lineno=3,
          tokens=137,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAE,KAAK;;AAIf,iBAAiB;EAChB,KAAK,EAAE,IAAI;EACX,KAAK,EAAE,GAAG;EACV,QAAQ,EAAE,QAAQ;EAClB,IAAI,EAAE,GAAG;;AAEV,mBAAmB;EAClB,OAAO,EAAE,KAAK;EACd,OAAO,EAAE,IAAI;EACb,SAAS,EAAE,KAAK;EAChB,eAAe,EAAE,IAAI;EACrB,KAAK,EA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=711,
          lineno=3,
          tokens=143,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AE,OAAO;EACd,WAAW,EAAE,qBAAqB;;AAEnC;;+BAE+B;EAC9B,iBAAiB,EAjWI,OAAO;EAkW5B,KAAK,EA3Ve,IAAI;;AA6VzB;+BAC+B;EAE9B,aAAa,EAAE,iBAAiB;EAEhC,gBAAgB,EAAE,IAAI;;AAEvB,4BAA4B;EAC3B,UAAU,EAAE,IAAI;EAChB,aAAa,EAAE,IAAI;EA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=712,
          lineno=3,
          tokens=144,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='CnB,WAAW,EAAE,qBAAqB;EAClC,KAAK,EAAE,OAAO;EACd,WAAW,EAAE,MAAM;EACnB,gBAAgB,EAAE,WAAW;;AAE9B,kCAAkC;EACjC,iBAAiB,EApXI,OAAO;EAqX5B,KAAK,EA9We,IAAI;;AAgXzB,mBAAmB;EAClB,KAAK,EAAE,IAAI;EACX,KAAK,EAAE,GAAG;EACV,OAAO,'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=713,
          lineno=3,
          tokens=139,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='EAAE,IAAI;EACb,gBAAgB,EAAE,IAAI;EAEtB,UAAU,EAAE,KAAK;;AAElB,yBAAyB;EACxB,OAAO,EAAE,IAAI;;AAEd,qCAAqC;EACpC,OAAO,EAAE,KAAK;;AAEf,0BAA0B;EACtB,WAAW,EAAE,EAAE;;AAEnB,6BAA6B;EACzB,MAAM,EAAE,IAAI;EACf,UAAU,EAAE,GAAG;'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=714,
          lineno=3,
          tokens=142,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='EACZ,aAAa,EAAE,IAAI;EACtB,mBAAmB,EAAE,GAAG;EACrB,WAAW,EAAE,CAAC;;AAElB,4BAA4B;EAC3B,KAAK,EAAE,IAAI;;AAEZ,kCAAkC;EACjC,OAAO,EAAE,EAAE;EACX,MAAM,EAAE,OAAO;;AAEhB,4BAA4B;EAC3B,UAAU,EAAE,MAAM;;AAEnB,8CAA8C;EAC7C,OAAO'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=715,
          lineno=3,
          tokens=141,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=',EAAE,IAAI;;AAEd,oDAAoD;EAClD,MAAM,EAAE,+BAA2B;EACnC,OAAO,EAAE,SAAS;EAClB,gBAAgB,EAAE,WAAW;EAC7B,KAAK,EAAE,IAAI;EACX,UAAU,EAAE,GAAG;;AAEjB,0DAA0D;EACxD,YAAY,EAAE,IAAI;;AAEpB,0BAA0B;EACtB,UAAU,EAAE,IAAI;EAChB,UAA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=716,
          lineno=3,
          tokens=137,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='U,EAAE,IAAI;EAChB,MAAM,EAAE,IAAI;;AAEhB,+BAA+B;EAC9B,KAAK,EAAE,IAAI;EACX,KAAK,EAAE,IAAI;EACR,UAAU,EAAE,IAAI;EAChB,QAAQ,EAAE,QAAQ;EAClB,OAAO,EAAE,CAAC;;AAEd,iCAAiC;EAChC,KAAK,EAAE,IAAI;EACR,WAAW,EAAE,qBAAqB;EAClC,'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=717,
          lineno=3,
          tokens=135,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='aAAa,EAAE,IAAI;;AAEvB,kCAAkC;EAChC,iBAAiB,EAAE,WAAW;;AAEhC,iCAAiC;EAC/B,KAAK,EAAE,IAAI;EACX,KAAK,EAAE,IAAI;EACX,QAAQ,EAAE,QAAQ;EAClB,GAAG,EAAE,IAAI;EACT,IAAI,EAAE,GAAG;EACT,OAAO,EAAE,CAAC;EACV,gBAAgB,EAAE,IAAI;;A'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=718,
          lineno=3,
          tokens=140,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AGxB,0BAA0B;EACzB,MAAM,EAAE,IAAI;;AAGb;;uCAEuC;EACrC,MAAM,EAAE,IAAI;EACZ,UAAU,EAAE,KAAK;;AAGnB,UAAU;EACR,OAAO,EAAE,MAAM;EACf,aAAa,EAAE,CAAC;EAChB,aAAa,EAAE,GAAG;EAClB,UAAU,EAAE,KAAK;EACjB,UAAU,EAAE,KAAK;EACjB,UAA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=719,
          lineno=3,
          tokens=137,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='U,EAAE,IAAI;EAChB,UAAU,EAAE,IAAI;EAChB,gBAAgB,EAAE,IAAI;;AAExB,iBAAiB;EACf,UAAU,EAAE,MAAM;EAClB,cAAc,EAAE,IAAI;EACpB,aAAa,EAAE,kCAA8B;EAC7C,KAAK,EAAE,IAAI;;AAEb,aAAa;EACX,OAAO,EAAE,IAAI;EACb,mBAAmB,EAAE,GAAG;EAC'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=720,
          lineno=3,
          tokens=135,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='xB,gBAAgB,EAAE,OAAO;EACzB,KAAK,EAAE,IAAI;EACX,UAAU,EAAE,GAAG;;AAEjB,mBAAmB;EAAC,OAAO,EAAE,EAAE;EAAE,MAAM,EAAE,OAAO;;AAChD,4BAA4B;EAAC,OAAO,EAAE,CAAC;;AACvC,kCAAkC;EAAC,OAAO,EAAE,CAAC;EAAE,OAAO,EAAE,YAAY;;AACpE,kB'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=721,
          lineno=3,
          tokens=136,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAkB;EAAC,mBAAmB,EAAE,GAAG;;AAC3C,wBAAwB;EAAC,OAAO,EAAE,EAAE;;AACpC,8BAA8B;EAAC,YAAY,EAAE,GAAG;;AAEhD,qBAAqB;EACnB,aAAa,EAAE,IAAI;;AAErB;;kCAEkC;EAChC,UAAU,EAAE,CAAC;;AAGf,gBAAgB;EACd,OAAO,EAAE,YAAY;EACrB,KAAK,E'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=722,
          lineno=3,
          tokens=133,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAE,IAAI;EACX,MAAM,EAAE,IAAI;EACZ,aAAa,EAAE,IAAI;;AAErB,aAAa;EAAC,gBAAgB,EAAE,OAAO;;AACvC,gBAAgB;EAAC,gBAAgB,EAAE,OAAO;;AAC1C,gBAAgB;EAAC,gBAAgB,EAAE,OAAO;;AAC1C,cAAc;EAAC,gBAAgB,EAAE,OAAO;;AACxC,iBAAiB;EAAC,gBAA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=723,
          lineno=3,
          tokens=139,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='gB,EAAE,OAAO;;AAE3C,MAAM;EACJ,QAAQ,EAAE,QAAQ;EAClB,GAAG,EAAE,CAAC;EACN,IAAI,EAAE,CAAC;EACP,OAAO,EAAE,GAAG;EACZ,KAAK,EAAE,IAAI;EACX,MAAM,EAAE,IAAI;EACZ,gBAAgB,EAxgBG,OAAO;EAygB1B,OAAO,EAAE,EAAE;EACX,OAAO,EAAE,IAA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=724,
          lineno=3,
          tokens=138,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='I;;AAGf,cAAc;EACZ,QAAQ,EAAE,QAAQ;EAClB,IAAI,EAAE,CAAC;EACP,KAAK,EAAE,CAAC;EACR,OAAO,EAAE,GAAG;EACZ,KAAK,EAAE,IAAI;EACX,UAAU,EAAE,KAAK;EACjB,MAAM,EAAE,MAAM;EACd,KAAK,EAAE,IAAI;EACX,OAAO,EAAE,IAAI;EACb,UAAU,EAAE,MA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=725,
          lineno=3,
          tokens=138,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AM;;AAEpB,iBAAiB;EACf,UAAU,EAAE,IAAI;;AAElB,sBAAsB;EACpB,UAAU,EAAE,IAAI;;AAElB,2BAA2B;EACzB,OAAO,EAAE,KAAK;EACd,UAAU,EAAE,kCAA8B;EAC1C,aAAa,EAAE,CAAC;EAChB,KAAK,EAAE,wBAAoB;;AAE7B,sCAAsC;EACpC,aAAa,EAAE,kCAA8B;;A'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=726,
          lineno=3,
          tokens=137,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AE/C,iCAAiC;EAC/B,KAAK,EAAE,IAAI;EACX,gBAAgB,EAAE,wBAAoB;;AAIxC,aAAa;EACT,OAAO,EAAE,IAAI;EACb,WAAW,EAAE,KAAK;EACrB,UAAU,EAAE,IAAI;EACb,UAAU,EAAE,iBAA8B;;AAG9C,wBAAwB;EACvB,MAAM,EAAE,IAAI;;AAEb,oCAAoC;EACnC,UAAU,E'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=727,
          lineno=3,
          tokens=142,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAE,IAAI;EAChB,WAAW,EAAE,IAAI;;AAElB,wCAAwC;EACvC,OAAO,EAAE,YAAY;;AAGtB,0BAA0B;EACxB,WAAW,EAAE,GAAG;;AAIlB,2BAA2B;EACzB,QAAQ,EAAE,IAAI;;AAGhB,8BAA8B;EAC5B,gBAAgB,EA1kBG,OAAO;EA2kB1B,OAAO,EAAE,SAAS;EAClB,MAAM,EAA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=728,
          lineno=3,
          tokens=140,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='E,KAAK;;AAGf,oCAAoC;EAClC,KAAK,EAAE,IAAI;EACX,OAAO,EAAE,gBAAgB;;AAG3B,sCAAsC;EACpC,aAAa,EAAE,CAAC;;AAGlB,2CAA2C;EACzC,KAAK,EAAE,IAAI;;AAGb,gCAAgC;EAC9B,KAAK,EAAE,IAAI;;AAGb,mCAAmC;EACjC,KAAK,EAAE,IAAI;EACX,SAAS,E'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=729,
          lineno=3,
          tokens=135,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAE,KAAK;EAChB,WAAW,EAAE,CAAC;EACd,UAAU,EAAE,MAAM;;AAGpB,iCAAiC;EAC/B,UAAU,EAAE,IAAI;EAChB,MAAM,EAAE,GAAG;EACX,gBAAgB,EAAE,wBAAoB;;AAGxC,uCAAuC;EACrC,KAAK,EAAE,IAAI;EACX,KAAK,EAAE,wBAAwB;EAC/B,mBAAmB,EAAE,GAAG;;'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=730,
          lineno=3,
          tokens=139,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAG1B,6CAA6C;EAC3C,KAAK,EAAE,IAAI;;AAGb,0CAA0C;EACxC,OAAO,EAAE,YAAY;EACrB,KAAK,EAAE,IAAI;;AAGb,+BAA+B;EAC7B,YAAY,EAAE,GAAG;;AAGnB,0CAA0C;EACxC,WAAW,EAAE,IAAI;;AAEnB,SAAS;EACP,gBAAgB,EAAE,OAAO;EACzB,aAAa,EAAE,CAAC'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=731,
          lineno=3,
          tokens=136,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=';;AAElB,aAAa;EACX,gBAAgB,EAzoBI,OAAO;EA0oB3B,kBAAkB,EAAE,IAAI;EACxB,eAAe,EAAE,IAAI;EACrB,UAAU,EAAE,IAAI;;AAGlB,gBAAgB;EACd,aAAa,EAAE,CAAC;;AAGlB,mCAAmC;EACjC,OAAO,EAAE,IAAI;;AAIf;;;;;wBAKkB;EAChB,UAAU,EAAE,IAAI;'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=732,
          lineno=3,
          tokens=139,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=';AAIlB,aAAa;EACZ,SAAS,EAAE,KAAK;EAChB,MAAM,EAAE,SAAS;EACjB,gBAAgB,EAAE,OAAO;EACzB,OAAO,EAAE,IAAI;EACb,aAAa,EAAE,IAAI;EACnB,UAAU,EAAE,+BAA2B;EACvC,KAAK,EAAE,IAAI;;AAEZ,iBAAiB;EACf,SAAS,EAAE,IAAI;EACf,KAAK,EAAE,KAA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=733,
          lineno=3,
          tokens=140,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='K;EACZ,OAAO,EAAE,KAAK;EACd,MAAM,EAAE,MAAM;;AAEhB,gBAAgB;EACf,OAAO,EAAE,EAAE;;AAEZ,mBAAmB;EACjB,OAAO,EAAE,SAAS;;AAEpB,kBAAkB;EAChB,OAAO,EAAE,IAAI;;AAEf,qBAAqB;EACpB,KAAK,EA3rBgB,OAAO;EA4rB5B,eAAe,EAAE,SAAS;;AAI3B,'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=734,
          lineno=3,
          tokens=135,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='IAAI;EAAC,KAAK,EAAE,IAAI;;AAEhB,WAAW;EACT,gBAAgB,EAAE,IAAI;;AAGxB,eAAe;EACb,SAAS,EAAE,KAAK;EAChB,OAAO,EAAE,MAAM;;AAGjB,gBAAgB;EACd,SAAS,EAAE,KAAK;EAChB,UAAU,EAAE,IAAI;EAChB,SAAS,EAAE,KAAK;;AAElB,yBAAyB;EACvB,YAAY'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=735,
          lineno=3,
          tokens=138,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=',EAAE,IAAI;;AAGpB;qBACqB;EACnB,KAAK,EAAE,GAAG;EACV,KAAK,EAAE,IAAI;;AAGb,SAAS;EACP,UAAU,EAAE,4CAA4C;EACxD,eAAe,EAAE,KAAK;EACtB,UAAU,EAAE,KAAK;EACjB,WAAW,EAAE,KAAK;;AAEpB,uBAAuB;EACrB,WAAW,EAAE,mBAAmB;EAChC,SAAS,E'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=736,
          lineno=3,
          tokens=139,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAE,GAAG;EACd,cAAc,EAAE,SAAS;EACzB,KAAK,EApuBe,OAAO;EAquB3B,WAAW,EAAE,EAAE;;AAGjB,OAAO;EACL,SAAS,EAAE,KAAK;;AAGlB,YAAY;EACV,gBAAgB,EA1uBL,OAAO;EA2uBlB,MAAM,EAAE,KAAK;;AAEf,qBAAqB;EACnB,MAAM,EAAE,KAAK;EACb,UAAU,EA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=737,
          lineno=3,
          tokens=137,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AE,wCAAwC;EACpD,eAAe,EAAE,KAAK;;AAExB,aAAa;EACX,gBAAgB,EAAE,OAAO;EACzB,OAAO,EAAE,YAAY;EACrB,UAAU,EAAE,IAAI;;AAElB,gBAAgB;EACd,KAAK,EAAE,IAAI;EACX,WAAW,EAAE,kBAAkB;EAC/B,SAAS,EAAE,GAAG;EACd,aAAa,EAAE,IAAI;EACnB,c'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=738,
          lineno=3,
          tokens=139,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAc,EAAE,UAAU;EAC1B,cAAc,EAAE,GAAG;;AAErB,eAAe;EACb,SAAS,EAAE,GAAG;EACd,KAAK,EApwBe,OAAO;;AAswB7B,gBAAgB;EACd,UAAU,EAAE,CAAC;EACb,KAAK,EAxwBe,OAAO;EAywB3B,cAAc,EAAE,SAAS;EACzB,SAAS,EAAE,KAAK;EAChB,cAAc,EAAE,GAAG;'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=739,
          lineno=3,
          tokens=138,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=';AAErB,qBAAqB;EACnB,KAAK,EAAE,OAAO;;AAEhB,eAAe;EACb,KAAK,EAAE,IAAI;EACX,WAAW,EAAE,CAAC;EACd,cAAc,EAAE,IAAI;;AAEtB,+BAA+B;EAC7B,UAAU,EAAE,MAAM;EAClB,KAAK,EAAE,IAAI;EACX,MAAM,EAAE,MAAM;;AAEhB,SAAS;EACP,KAAK,EA3xBe'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=740,
          lineno=3,
          tokens=144,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=',OAAO;EA4xB3B,cAAc,EAAE,KAAK;EACrB,QAAQ,EAAE,QAAQ;EAClB,gBAAgB,EAAE,IAAI;EACtB,gBAAgB,EAAE,8BAA8B;EAChD,iBAAiB,EAAE,SAAS;EAC5B,mBAAmB,EAAE,gBAAgB;EACrC,eAAe,EAAE,OAAO;;AAE1B,YAAY;EACV,WAAW,EAAE,kBAAkB;EAC/B,SAAS,'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=741,
          lineno=3,
          tokens=136,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='EAAE,GAAG;EACd,cAAc,EAAE,UAAU;EAC1B,UAAU,EAAE,KAAK;;AAEnB,YAAY;EACV,SAAS,EAAE,GAAG;;AAEhB,kBAAkB;EAChB,SAAS,EAAE,KAAK;EAChB,MAAM,EAAE,IAAI;;AAEd,gBAAgB;EACd,QAAQ,EAAE,QAAQ;EAClB,GAAG,EAAE,KAAK;EACV,SAAS,EAAE,KAAK'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=742,
          lineno=3,
          tokens=136,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=';EAChB,aAAa,EAAE,IAAI;;AAGrB,OAAO;EACL,gBAAgB,EAAE,OAAO;EACzB,KAAK,EAAE,IAAI;;AAEb,oBAAoB;EAClB,KAAK,EAAE,GAAG;EACV,MAAM,EAAE,MAAM;EACd,cAAc,EAAE,IAAI;;AAEtB,UAAU;EACR,SAAS,EAAE,GAAG;EACd,WAAW,EAAE,kBAAkB;EAC/B,c'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=743,
          lineno=3,
          tokens=136,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAc,EAAE,UAAU;;AAE5B,UAAU;EACR,SAAS,EAAE,KAAK;;AAElB,WAAW;EACT,uBAAuB,EAAE,IAAI;EAC7B,sBAAsB,EAAE,IAAI;;AAG9B,SAAS;EACP,gBAAgB,EA90BG,OAAO;EA+0B1B,KAAK,EAAE,IAAI;EACX,UAAU,EAAE,MAAM;EAClB,QAAQ,EAAE,QAAQ;;AAEpB,c'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=744,
          lineno=3,
          tokens=141,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AAc;EACZ,QAAQ,EAAE,QAAQ;EAClB,GAAG,EAAE,MAAM;EACX,SAAS,EAAE,IAAI;EACf,cAAc,EAAE,KAAK;EACrB,gBAAgB,EAAE,gCAAgC;EAClD,iBAAiB,EAAE,SAAS;EAC5B,eAAe,EAAE,IAAI;;AAEvB,iBAAiB;EACf,SAAS,EAAE,GAAG;EACd,OAAO,EAAE,KAAK;EACd'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=745,
          lineno=3,
          tokens=138,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=',MAAM,EAAE,MAAM;EACd,WAAW,EAAE,IAAI;EACjB,cAAc,EAAE,SAAS;EACzB,WAAW,EAAE,OAAO;EACpB,WAAW,EAAE,GAAG;;AAElB;gBACgB;EACd,QAAQ,EAAE,QAAQ;EAClB,GAAG,EAAE,KAAK;;AAGZ,WAAW;EACT,gBAAgB,EA52BG,OAAO;EA62B1B,KAAK,EAAE,wBAA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=746,
          lineno=3,
          tokens=139,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='oB;;AAE7B,cAAc;EACZ,MAAM,EAAE,IAAI;EACZ,MAAM,EAAE,GAAG;EACX,aAAa,EAAE,IAAI;EACnB,gBAAgB,EAAE,wBAAoB;;AAExC,cAAc;EACZ,SAAS,EAAE,KAAK;;AAElB,sBAAsB;EACpB,gBAAgB,EA13BI,OAAO;;AA43B7B,aAAa;EACX,KAAK,EA73Be,OAAO;;AA+3'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=747,
          lineno=3,
          tokens=140,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='B7B,mBAAmB;EACjB,KAAK,EAAE,IAAI;;AAEb,sBAAsB;EACpB,OAAO,EAAE,MAAM;;AAGjB,uBAAuB;EACtB,OAAO,EAAE,IAAI;EACb,gBAAgB,EAAE,IAAI;EACtB,aAAa,EAAE,GAAG;;AAInB,oCAAqC;EACnC,SAAS;IACP,UAAU,EAAE,KAAK;;EAEnB,qBAAqB;IACnB,OA'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=748,
          lineno=3,
          tokens=140,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AO,EAAE,IAAI;;EAEf,oBAAoB;IAClB,KAAK,EAAE,IAAI;IACX,UAAU,EAAE,MAAM;;EAGpB,aAAa;IACX,UAAU,EAAE,MAAM;;EAGpB,oBAAoB;IAClB,KAAK,EAAE,IAAI;;EAGb,cAAc;IACZ,gBAAgB,EAAE,IAAI;IACtB,QAAQ,EAAE,MAAM;IAChB,WAAW,EAAE,IAAI;IAC'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=749,
          lineno=3,
          tokens=138,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='jB,cAAc,EAAE,KAAK;;EAEvB,mCAAmC;IACjC,QAAQ,EAAE,MAAM;IAChB,SAAS,EAAE,IAAI;;EAGjB,WAAW;IACT,UAAU,EAAE,MAAM;IAClB,UAAU,EAAE,IAAI;AAIpB,oCAAqC;EACnC,YAAY;IACV,SAAS,EAAE,GAAG;AAIlB,oCAAqC;EACnC,sBAAsB;IAClB,KAAK,EAAE'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=750,
          lineno=3,
          tokens=158,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body=',eAAe;;EAE1B,eAAe;IACd,OAAO,EAAE,KAAK;IACd,MAAM,EAAE,MAAM;;EAEf,yBAAyB;IACvB,YAAY,EAAE,CAAC;;EAEjB,gBAAgB;IACd,KAAK,EAAE,GAAG;IACV,MAAM,EAAE,SAAS;;EAGnB,YAAY;IACV,SAAS,EAAE,cAAc;;EAG3B,YAAY;IACV,OAAO,EAAE,QAAQ",\n'
               '"sources": ["style.scss"],\n'
               '"names": [],\n'
               '"file": "style.css"\n'
               '}'),
 Fragment(document_cs='a917345572dfe4ad78bd3d669d9684844bd3685dbec74826e5f93ecbc266420e',
          id=751,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='aad4961b5ff22caa6cffa48c0ba48076ceea26c1f841fd807adfa8b2019ce23d',
          id=752,
          lineno=1,
          tokens=134,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='APP_ENV=local\n'
               'APP_DEBUG=true\n'
               'APP_KEY=BzwPijlvDCehuNVPwQejf3z41YHCvJ9y\n'
               '\n'
               'DB_HOST=localhost\n'
               'DB_DATABASE=DB\n'
               'DB_USERNAME=root\n'
               'DB_PASSWORD=root\n'
               '\n'
               'CACHE_DRIVER=file\n'
               'SESSION_DRIVER=file\n'
               'QUEUE_DRIVER=sync\n'
               '\n'
               'MAIL_DRIVER=smtp\n'
               'MAIL_HOST=mailtrap.io\n'
               'MAIL_PORT=2525\n'
               'MAIL_USERNAME=null\n'
               'MAIL_PASSWORD=null\n'
               'MAIL_ENCRYPTION=null\n'
               '\n'
               'MAIL_FROM=someone@yourdomain.com\n'
               'MAIL_FROM_NAME="Project Administrator"\n'
               '\n'
               'ADMIN_EMAIL=youremail@youremail.com\n'
               '\n'
               'GOOGLE_UA=\n'
               'USERVOICE_URL=\n'),
 Fragment(document_cs='aad4961b5ff22caa6cffa48c0ba48076ceea26c1f841fd807adfa8b2019ce23d',
          id=753,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='ad16862c0526a180ba294c4bcfdc013466dafe7d37ebb9a38053854cde604d20',
          id=754,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='afcba53425cab66aa75fd8d50df60bf748fcb34aab7c2a566e7d35c4e3168f56',
          id=755,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='b05b0d9f8e9ef182ea6ca96850cde2ccc58e458fdb1bd8d821a5e2d50be9d94a',
          id=756,
          lineno=5,
          tokens=156,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='DatabaseSeeder',
          body='class DatabaseSeeder extends Seeder {\n'
               '\n'
               '\t/**\n'
               '\t * Run the database seeds.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function run()\n'
               '\t{\n'
               '\t\tEloquent::unguard();\n'
               '\n'
               "\t\t$this->call('UsersTableSeeder');\n"
               "\t\t$this->command->info('Users table seeded!');\n"
               '\n'
               "\t\t$this->call('ClientsTableSeeder');\n"
               "\t\t$this->command->info('Clients table seeded!');\n"
               '\n'
               "\t\t$this->call('ProjectsTableSeeder');\n"
               "\t\t$this->command->info('Projects table seeded!');\n"
               '\n'
               "\t\t$this->call('TasksTableSeeder');\n"
               "\t\t$this->command->info('Tasks table seeded!');\n"
               '\n'
               "\t\t$this->command->info('Test Account: EMAIL: "
               "test@ribbbon.com PASSWORD: secret');\n"
               '\n'
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='b05b0d9f8e9ef182ea6ca96850cde2ccc58e458fdb1bd8d821a5e2d50be9d94a',
          id=757,
          lineno=12,
          tokens=130,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='run',
          body='public function run()\n'
               '\t{\n'
               '\t\tEloquent::unguard();\n'
               '\n'
               "\t\t$this->call('UsersTableSeeder');\n"
               "\t\t$this->command->info('Users table seeded!');\n"
               '\n'
               "\t\t$this->call('ClientsTableSeeder');\n"
               "\t\t$this->command->info('Clients table seeded!');\n"
               '\n'
               "\t\t$this->call('ProjectsTableSeeder');\n"
               "\t\t$this->command->info('Projects table seeded!');\n"
               '\n'
               "\t\t$this->call('TasksTableSeeder');\n"
               "\t\t$this->command->info('Tasks table seeded!');\n"
               '\n'
               "\t\t$this->command->info('Test Account: EMAIL: "
               "test@ribbbon.com PASSWORD: secret');\n"
               '\n'
               '\t}'),
 Fragment(document_cs='b05b0d9f8e9ef182ea6ca96850cde2ccc58e458fdb1bd8d821a5e2d50be9d94a',
          id=758,
          lineno=1,
          tokens=17,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: run\n  Classes: DatabaseSeeder\n  Usages: this\n'),
 Fragment(document_cs='b3dfa15369cf5f11cf96cdb2449a88ae77600ade786d9ad0536b04b9e81a42cb',
          id=759,
          lineno=5,
          tokens=8,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Event',
          body='abstract class Event\n{\n    //\n}'),
 Fragment(document_cs='b3dfa15369cf5f11cf96cdb2449a88ae77600ade786d9ad0536b04b9e81a42cb',
          id=760,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Event\n'),
 Fragment(document_cs='b3f86d8c97beb62b13e3ce76e1e36c9c5283f265607115d6bee41b49193f45dd',
          id=761,
          lineno=6,
          tokens=116,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CreateClientsTable',
          body='class CreateClientsTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::create('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->integer('user_id');\n"
               "\t\t\t$table->string('name');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::drop('clients');\n"
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='b3f86d8c97beb62b13e3ce76e1e36c9c5283f265607115d6bee41b49193f45dd',
          id=762,
          lineno=13,
          tokens=57,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::create('clients', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->integer('user_id');\n"
               "\t\t\t$table->string('name');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='b3f86d8c97beb62b13e3ce76e1e36c9c5283f265607115d6bee41b49193f45dd',
          id=763,
          lineno=30,
          tokens=15,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body="public function down()\n\t{\n\t\tSchema::drop('clients');\n\t}"),
 Fragment(document_cs='b3f86d8c97beb62b13e3ce76e1e36c9c5283f265607115d6bee41b49193f45dd',
          id=764,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: CreateClientsTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='bb926d03878886ac776168739f2582c8fb97a55508f9c1f4efecc7a1682b1941',
          id=765,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='bbc46819c8699b1b5a2ded5c4538c83e751b67e3a90afc12580bcf55b125ef51',
          id=766,
          lineno=16,
          tokens=6,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ApiController',
          body='class ApiController extends BaseController {\n\n}'),
 Fragment(document_cs='bbc46819c8699b1b5a2ded5c4538c83e751b67e3a90afc12580bcf55b125ef51',
          id=767,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: ApiController\n'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=768,
          lineno=17,
          tokens=49,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ProjectsController',
          body='class ProjectsController extends BaseController {\n'
               '\n'
               '\t// Returns the given project view\n'
               '\tpublic function show($id)\n'
               '\t{   \t\n'
               '\t\t$project \t\t=\tProject::find($id);\n'
               '\n'
               '        // Must be refactored as a filter\n'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=769,
          lineno=25,
          tokens=227,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ProjectsController',
          body='\t\tif ( $project->isOwner() == false && $project->isMember() '
               '== false ) {\n'
               "\t\t\treturn Redirect::to('/hud');\n"
               '\t\t}\n'
               '\n'
               "\t\treturn  View::make('ins/projects/show')->with('pTitle', "
               '$project->name);\n'
               '\t}\n'
               '\n'
               '\t// Get all user projects\n'
               '\tpublic function getAllUserProjects(){\n'
               "\t\t$projects = Project::where('user_id',Auth::id())->get();\n"
               '\n'
               '\t\tif($projects) {\n'
               '\t\t\tforeach ($projects as $project) {\n'
               '\t\t\t\t$completedWeight = '
               "Project::find($project->id)->tasks()->where('state','=','complete')->sum('weight');\n"
               '\t\t\t\t$totalWeight = '
               "Project::find($project->id)->tasks()->sum('weight');\n"
               '\n'
               '\t\t\t\t$project["completedWeight"] = $completedWeight;\n'
               '\t\t\t\t$project["totalWeight"] = $totalWeight;\n'
               '\t\t\t}\n'
               '\t\t}\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Projects "
               "retrieved successfully',$projects->toArray());\n"
               '\t}\n'
               '\n'
               '    // Get all projects that the Auth user is a member of\n'
               '\tpublic function getAllMemberProjects(){\n'
               '        $sharedProjects '),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=770,
          lineno=51,
          tokens=191,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ProjectsController',
          body="= Projectuser::where('user_id', "
               "Auth::id())->select('project_id')->get();\n"
               '        $project_ids = [];\n'
               '\n'
               '        foreach($sharedProjects as $project){\n'
               '            $project_ids[] = $project->project_id;\n'
               '        }\n'
               '\n'
               "        $sharedProjects = Project::whereIn('id', "
               '$project_ids)->get();\n'
               '\n'
               '        if($sharedProjects) {\n'
               '            foreach ($sharedProjects as $project) {\n'
               '                $completedWeight = '
               "Project::find($project->id)->tasks()->where('state','=','complete')->sum('weight');\n"
               '                $totalWeight = '
               "Project::find($project->id)->tasks()->sum('weight');\n"
               '\n'
               '                $project["completedWeight"] = '
               '$completedWeight;\n'
               '                $project["totalWeight"] = $totalWeight;\n'
               '            }\n'
               '        }\n'
               '        return '
               "$this->setStatusCode(200)->makeResponse('Projects retrieved "
               "successfully',$sharedProjects);\n"
               '    }\n'
               '\n'
               '\t//\tReturn the given project\n'
               '\tpublic function getProject($id){\n'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=771,
          lineno=74,
          tokens=240,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ProjectsController',
          body='\t\tif (!Project::find($id)) {\n'
               "\t\t\treturn $this->setStatusCode(404)->makeResponse('The "
               "project was not found');\n"
               '\t\t}\n'
               '\n'
               '\t\t$project = Project::find($id);\n'
               "\t\t$project->tasks = Task::where('project_id', $id)->get();\n"
               "\t\t$project->credentials = Credential::where('project_id', "
               '$id)->get();\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Project "
               "was successfully found', $project);\n"
               '\t}\n'
               '\n'
               '\t// Insert the given project into the database\n'
               '\tpublic function storeProject(){\n'
               "\t\tif (!Input::all() || strlen(trim(Input::get('name'))) == "
               '0) {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('No "
               "information provided to create project');\n"
               '\t\t}\n'
               '\n'
               "\t\tInput::merge(array('user_id' => Auth::id()));\n"
               '\t\tProject::create(Input::all());\n'
               '\t\t$id = \\DB::getPdo()->lastInsertId();\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Project "
               "created successfully', Project::find($id));\n"
               '\t}\n'
               '\n'
               '\t// Update the given project\n'
               '\tpublic function updateProject($id){\n'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=772,
          lineno=100,
          tokens=226,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ProjectsController',
          body='\t\tif ( Input::get(\'name\') === "") {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "project needs a name');\n"
               '\t\t}\n'
               '\n'
               '\t\tif (!Project::find($id)) {\n'
               "\t\t\treturn $this->setStatusCode(404)->makeResponse('Project "
               "not found');\n"
               '\t\t}\n'
               '\n'
               '\t\t$input = Input::all();\n'
               "\t\tunset($input['_method']);\n"
               '\n'
               '\t\tProject::find($id)->update($input);\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('The "
               "project has been updated');\n"
               '\t}\n'
               '\n'
               '    public function getOwner($id){\n'
               "        $owner_id = Project::whereId($id)->pluck('user_id');\n"
               '        $owner = User::whereId($owner_id)->get();\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('ok.', "
               '$owner[0]);\n'
               '    }\n'
               '\n'
               '    public function getMembers($id){\n'
               "        $members_id = Projectuser::where('project_id', "
               "$id)->lists('user_id');\n"
               '        $members = [];\n'
               '\n'
               '        foreach($members_id as $id){\n'
               '            $member = User::whereId($i'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=773,
          lineno=127,
          tokens=173,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ProjectsController',
          body='d)->get();\n'
               '            array_push($members, $member[0]);\n'
               '        }\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('ok.', "
               '$members);\n'
               '    }\n'
               '    // Invites a user to the given project.\n'
               '\tpublic function invite($project_id, $email){\n'
               '        if(trim(strlen($email)) == 0){\n'
               '            return '
               "$this->setStatusCode(406)->makeResponse('The email field is "
               "required!');\n"
               '        }\n'
               '\n'
               '        if(!filter_var($email, FILTER_VALIDATE_EMAIL)) {\n'
               '            return '
               "$this->setStatusCode(406)->makeResponse('Please enter a valid "
               "email!');\n"
               '        }\n'
               '\n'
               '        $project_name\t= '
               "Project::find($project_id)->pluck('name');\n"
               '        $owner_id\t    = '
               "Project::find($project_id)->pluck('user_id');\n"
               "        $project_url \t= url() . '/projects/'.$project"),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=774,
          lineno=145,
          tokens=189,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ProjectsController',
          body='_id;\n'
               '        $invited_user   = User::whereEmail($email)->get();\n'
               '\n'
               '        if( count($invited_user) == 0 ){\n'
               '            return '
               "$this->setStatusCode(406)->makeResponse('That user does not "
               "have an account.');\n"
               '        }\n'
               '        $invited_user = $invited_user[0];\n'
               '\n'
               '        if( '
               'count(Projectuser::whereUserId($invited_user->id)->whereProjectId($project_id)->get()) '
               '!= 0 ){\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('A user "
               "with that email has already been invited.');\n"
               '\t\t}\n'
               '\n'
               '        if(Auth::id() != $owner_id){\n'
               '            return '
               "$this->setStatusCode(406)->makeResponse('Only the project "
               "owner can invite a user.');\n"
               '        }\n'
               '\t\t// Save the relationship between user and project.\n'
               '\t\t$pu\t\t\t\t= \tnew Projectuser();\n'
               '\t\t$pu->project_id\t='),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=775,
          lineno=162,
          tokens=198,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ProjectsController',
          body='\t$project_id;\n'
               '\t\t$pu->user_id\t=\t$invited_user->id;\n'
               '\t\t$pu->save();\n'
               '\n'
               '\t\tHelpers::sendProjectInviteMail($email, $project_name, '
               '$project_url);\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('A new "
               "member has been added to this project.', $invited_user);\n"
               '\t}\n'
               '\n'
               '    // Removes a member from a given project\n'
               '\tpublic function removeMember($project_id, $member_id){\n'
               '\t\tif( '
               'count(Projectuser::whereUserId($member_id)->whereProjectId($project_id)->get()) '
               '== 0 ){\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('That "
               "user is not in this project.');\n"
               '\t\t}\n'
               '\n'
               '\t\t$project = Project::find($project_id);\n'
               '\t\t$project->members()->detach($member_id);\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Member has "
               "been removed from this project.');\n"
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=776,
          lineno=20,
          tokens=91,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='show',
          body='public function show($id)\n'
               '\t{   \t\n'
               '\t\t$project \t\t=\tProject::find($id);\n'
               '\n'
               '        // Must be refactored as a filter\n'
               '\t\tif ( $project->isOwner() == false && $project->isMember() '
               '== false ) {\n'
               "\t\t\treturn Redirect::to('/hud');\n"
               '\t\t}\n'
               '\n'
               "\t\treturn  View::make('ins/projects/show')->with('pTitle', "
               '$project->name);\n'
               '\t}'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=777,
          lineno=33,
          tokens=139,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='getAllUserProjects',
          body='public function getAllUserProjects(){\n'
               "\t\t$projects = Project::where('user_id',Auth::id())->get();\n"
               '\n'
               '\t\tif($projects) {\n'
               '\t\t\tforeach ($projects as $project) {\n'
               '\t\t\t\t$completedWeight = '
               "Project::find($project->id)->tasks()->where('state','=','complete')->sum('weight');\n"
               '\t\t\t\t$totalWeight = '
               "Project::find($project->id)->tasks()->sum('weight');\n"
               '\n'
               '\t\t\t\t$project["completedWeight"] = $completedWeight;\n'
               '\t\t\t\t$project["totalWeight"] = $totalWeight;\n'
               '\t\t\t}\n'
               '\t\t}\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Projects "
               "retrieved successfully',$projects->toArray());\n"
               '\t}'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=778,
          lineno=50,
          tokens=187,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='getAllMemberProjects',
          body='public function getAllMemberProjects(){\n'
               "        $sharedProjects = Projectuser::where('user_id', "
               "Auth::id())->select('project_id')->get();\n"
               '        $project_ids = [];\n'
               '\n'
               '        foreach($sharedProjects as $project){\n'
               '            $project_ids[] = $project->project_id;\n'
               '        }\n'
               '\n'
               "        $sharedProjects = Project::whereIn('id', "
               '$project_ids)->get();\n'
               '\n'
               '        if($sharedProjects) {\n'
               '            foreach ($sharedProjects as $project) {\n'
               '                $completedWeight = '
               "Project::find($project->id)->tasks()->where('state','=','complete')->sum('weight');\n"
               '                $totalWeight = '
               "Project::find($project->id)->tasks()->sum('weight');\n"
               '\n'
               '                $project["completedWeight"] = '
               '$completedWeight;\n'
               '                $project["totalWeight"] = $totalWeight;\n'
               '            }\n'
               '        }\n'
               '        return '
               "$this->setStatusCode(200)->makeResponse('Projects retrieved "
               "successfully',$sharedProjects);\n"
               '    }'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=779,
          lineno=73,
          tokens=111,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='getProject',
          body='public function getProject($id){\n'
               '\t\tif (!Project::find($id)) {\n'
               "\t\t\treturn $this->setStatusCode(404)->makeResponse('The "
               "project was not found');\n"
               '\t\t}\n'
               '\n'
               '\t\t$project = Project::find($id);\n'
               "\t\t$project->tasks = Task::where('project_id', $id)->get();\n"
               "\t\t$project->credentials = Credential::where('project_id', "
               '$id)->get();\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Project "
               "was successfully found', $project);\n"
               '\t}'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=780,
          lineno=86,
          tokens=112,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='storeProject',
          body='public function storeProject(){\n'
               "\t\tif (!Input::all() || strlen(trim(Input::get('name'))) == "
               '0) {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('No "
               "information provided to create project');\n"
               '\t\t}\n'
               '\n'
               "\t\tInput::merge(array('user_id' => Auth::id()));\n"
               '\t\tProject::create(Input::all());\n'
               '\t\t$id = \\DB::getPdo()->lastInsertId();\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Project "
               "created successfully', Project::find($id));\n"
               '\t}'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=781,
          lineno=99,
          tokens=119,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='updateProject',
          body='public function updateProject($id){\n'
               '\t\tif ( Input::get(\'name\') === "") {\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('The "
               "project needs a name');\n"
               '\t\t}\n'
               '\n'
               '\t\tif (!Project::find($id)) {\n'
               "\t\t\treturn $this->setStatusCode(404)->makeResponse('Project "
               "not found');\n"
               '\t\t}\n'
               '\n'
               '\t\t$input = Input::all();\n'
               "\t\tunset($input['_method']);\n"
               '\n'
               '\t\tProject::find($id)->update($input);\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('The "
               "project has been updated');\n"
               '\t}'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=782,
          lineno=115,
          tokens=60,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='getOwner',
          body='public function getOwner($id){\n'
               "        $owner_id = Project::whereId($id)->pluck('user_id');\n"
               '        $owner = User::whereId($owner_id)->get();\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('ok.', "
               '$owner[0]);\n'
               '    }'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=783,
          lineno=122,
          tokens=88,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='getMembers',
          body='public function getMembers($id){\n'
               "        $members_id = Projectuser::where('project_id', "
               "$id)->lists('user_id');\n"
               '        $members = [];\n'
               '\n'
               '        foreach($members_id as $id){\n'
               '            $member = User::whereId($id)->get();\n'
               '            array_push($members, $member[0]);\n'
               '        }\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('ok.', "
               '$members);\n'
               '    }'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=784,
          lineno=134,
          tokens=180,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='invite',
          body='public function invite($project_id, $email){\n'
               '        if(trim(strlen($email)) == 0){\n'
               '            return '
               "$this->setStatusCode(406)->makeResponse('The email field is "
               "required!');\n"
               '        }\n'
               '\n'
               '        if(!filter_var($email, FILTER_VALIDATE_EMAIL)) {\n'
               '            return '
               "$this->setStatusCode(406)->makeResponse('Please enter a valid "
               "email!');\n"
               '        }\n'
               '\n'
               '        $project_name\t= '
               "Project::find($project_id)->pluck('name');\n"
               '        $owner_id\t    = '
               "Project::find($project_id)->pluck('user_id');\n"
               "        $project_url \t= url() . '/projects/'.$project_id;\n"
               '        $invited_user   = User::whereEmail($email)->get();\n'
               '\n'
               '        if( count($invited_user) == 0 ){\n'
               '            return '
               "$this->setStatusCode(406)->makeResponse('That user does not "
               "have an account.');\n"
               '        }\n'
               '       '),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=785,
          lineno=151,
          tokens=212,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='invite',
          body=' $invited_user = $invited_user[0];\n'
               '\n'
               '        if( '
               'count(Projectuser::whereUserId($invited_user->id)->whereProjectId($project_id)->get()) '
               '!= 0 ){\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('A user "
               "with that email has already been invited.');\n"
               '\t\t}\n'
               '\n'
               '        if(Auth::id() != $owner_id){\n'
               '            return '
               "$this->setStatusCode(406)->makeResponse('Only the project "
               "owner can invite a user.');\n"
               '        }\n'
               '\t\t// Save the relationship between user and project.\n'
               '\t\t$pu\t\t\t\t= \tnew Projectuser();\n'
               '\t\t$pu->project_id\t=\t$project_id;\n'
               '\t\t$pu->user_id\t=\t$invited_user->id;\n'
               '\t\t$pu->save();\n'
               '\n'
               '\t\tHelpers::sendProjectInviteMail($email, $project_name, '
               '$project_url);\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('A new "
               "member has been added to this project.', $invited_user);\n"
               '\t}'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=786,
          lineno=171,
          tokens=109,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='removeMember',
          body='public function removeMember($project_id, $member_id){\n'
               '\t\tif( '
               'count(Projectuser::whereUserId($member_id)->whereProjectId($project_id)->get()) '
               '== 0 ){\n'
               "\t\t\treturn $this->setStatusCode(406)->makeResponse('That "
               "user is not in this project.');\n"
               '\t\t}\n'
               '\n'
               '\t\t$project = Project::find($project_id);\n'
               '\t\t$project->members()->detach($member_id);\n'
               '\n'
               "\t\treturn $this->setStatusCode(200)->makeResponse('Member has "
               "been removed from this project.');\n"
               '\t}'),
 Fragment(document_cs='bfbf6e54ec1d655a75cc078e24d75e9a0bc589b105c9b8d306f3460b1db67522',
          id=787,
          lineno=1,
          tokens=65,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: getAllMemberProjects getAllUserProjects '
               'getMembers getOwner getProject invite removeMember show '
               'storeProject updateProject\n'
               '  Classes: ProjectsController\n'
               '  Usages: completedWeight email input invited_user member '
               'member_id members members_id owner owner_id project project_id '
               'project_ids project_name project_url projects sharedProjects '
               'this totalWeight\n'),
 Fragment(document_cs='c457a110ceaa430bdfaa5bd0167403f390d3cc72fff227ea227e43b702db66d0',
          id=788,
          lineno=1,
          tokens=184,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# Ribbbon\n'
               '\n'
               '_V 2.2_\n'
               '\n'
               '\n'
               '[Ribbbon.com](http://ribbbon.com)\n'
               '\n'
               'Ribbbon is a project management system built on Laravel 5.1.* '
               '& Vue.js :)\n'
               '\n'
               '# Features\n'
               '  - User / account creation\n'
               '  - Client creation\n'
               '  - Project creation\n'
               '  - Task creation \n'
               '  - Assigning weights to tasks\n'
               '  - Project sharing\n'
               '  - Api Driven\n'
               '\n'
               '# Get involved\n'
               '  - Clone or fork the project. \n'
               '  - Create feature branches off develop branch.\n'
               '  - Once your changes are ready create a pull request into the '
               'master branch.\n'
               '   \n'
               '# Installation\n'
               ' - Clone the repo\n'
               ' - Copy .env.example to .env\n'
               ' - Set values in .env file\n'
               ' - Run composer install\n'
               ' - Run php artisan key:generate\n'
               ' - Run php artisan migrate\n'
               ' - Run php artisan db:seed\n'
               ' - Start developing!\n'
               '\n'
               '\n'),
 Fragment(document_cs='c457a110ceaa430bdfaa5bd0167403f390d3cc72fff227ea227e43b702db66d0',
          id=789,
          lineno=1,
          tokens=15,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='# Ribbbon\n# Features\n# Get involved\n# Installation\n'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=790,
          lineno=13,
          tokens=172,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='User',
          body='class User extends Model implements AuthenticatableContract, '
               'CanResetPasswordContract\n'
               '{\n'
               '    use Authenticatable, CanResetPassword;\n'
               '\n'
               '    /**\n'
               '     * The database table used by the model.\n'
               '     *\n'
               '     * @var string\n'
               '     */\n'
               "    protected $table = 'users';\n"
               '\n'
               '\n'
               '    /**\n'
               '     * The attributes that are mass assignable.\n'
               '     *\n'
               '     * @var array\n'
               '     */\n'
               '    protected $fillable = [\n'
               "        'full_name',\n"
               "        'email',\n"
               "        'password',\n"
               "        'title',\n"
               "        'bio',\n"
               "        'link',\n"
               "        'twitter',\n"
               "        'facebook',\n"
               "        'linkedin'\n"
               '    ];\n'
               '\n'
               '    /**\n'
               "     * The attributes excluded from the model's JSON form.\n"
               '     *\n'
               '     * @var array\n'
               '     */\n'
               "    protected $hidden = ['password', "
               "'remember_token','created_at','updated_at'];\n"
               '\n'
               '\n'
               '    /**\n'
               '     * Return the related clie'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=791,
          lineno=51,
          tokens=183,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='User',
          body='nts for a given user\n'
               '     */\n'
               '    public function clients(){\n'
               "        return $this->hasMany('App\\Client','user_id');\n"
               '    }\n'
               '\n'
               '    /**\n'
               '     * Return the related projects for a given user\n'
               '     */\n'
               '    public function projects(){\n'
               "        return $this->hasMany('App\\Project','user_id');\n"
               '    }   \n'
               '\n'
               '    /**\n'
               '     * Return the related tasks for a given user\n'
               '     */\n'
               '    public function tasks(){\n'
               "        return $this->hasMany('App\\Task','user_id');\n"
               '    }\n'
               '\n'
               '    public function inProjects(){\n'
               "        return $this->belongsToMany('App\\Project');\n"
               '    }\n'
               '\n'
               '    /**\n'
               '     * Get the total weight of a user\n'
               '     * @param  [int] $id [the id of the user]\n'
               '     * @return [int]     [the total weight of all the '
               'incomplete tasks a user has]\n'
               '     */\n'
               '    public static function weight($id = null){\n'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=792,
          lineno=81,
          tokens=166,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='User',
          body='        if ($id == null) {\n'
               '            $result = '
               "DB::table('tasks')->where('user_id',Auth::id())->whereState('incomplete')->sum('weight');\n"
               '        }else{\n'
               '            $result = '
               "DB::table('tasks')->where('user_id',$id)->whereState('incomplete')->sum('weight');\n"
               '        }\n'
               '        return $result;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * Get either a Gravatar URL or complete image tag for a '
               'specified email address.\n'
               '     *\n'
               '     * @param string $email The email address\n'
               '     * @param string $s Size in pixels, defaults to 80px [ 1 - '
               '2048 ]\n'
               '     * @param string $d Default imageset to use [ 404 | mm | '
               'identicon | monsterid | wavatar ]\n'
               '     * @param s'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=793,
          lineno=95,
          tokens=242,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='User',
          body='tring $r Maximum rating (inclusive) [ g | pg | r | x ]\n'
               '     * @param boole $img True to return a complete IMG tag '
               'False for just the URL\n'
               '     * @param array $atts Optional, additional key/value '
               'attributes to include in the IMG tag\n'
               '     * @return String containing either just a URL or a '
               'complete image tag\n'
               '     * @source http://gravatar.com/site/implement/images/php/\n'
               '     */\n'
               '    public static function get_gravatar( $email, $s = 80, $d = '
               "'mm', $r = 'g', $img = false, $atts = array() ) {\n"
               "        $url = 'http://www.gravatar.com/avatar/';\n"
               '        $url .= md5( strtolower( trim( $email ) ) );\n'
               '        $url .= "?s=$s&d=$d&r=$r";\n'
               '        if ( $img ) {\n'
               '            $url = \'<img src="\' . $url . \'"\';\n'
               '            foreach ( $atts as $key => $val )\n'
               '                $url .= \' \' . $key . \'="\' . $val . \'"\';\n'
               "            $url .= ' />';\n"
               '        }\n'
               '        return $url;\n'
               '    }\n'
               '\n'
               '}'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=794,
          lineno=53,
          tokens=19,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='clients',
          body='public function clients(){\n'
               "        return $this->hasMany('App\\Client','user_id');\n"
               '    }'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=795,
          lineno=60,
          tokens=20,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='projects',
          body='public function projects(){\n'
               "        return $this->hasMany('App\\Project','user_id');\n"
               '    }'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=796,
          lineno=67,
          tokens=20,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='tasks',
          body='public function tasks(){\n'
               "        return $this->hasMany('App\\Task','user_id');\n"
               '    }'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=797,
          lineno=71,
          tokens=19,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='inProjects',
          body='public function inProjects(){\n'
               "        return $this->belongsToMany('App\\Project');\n"
               '    }'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=798,
          lineno=80,
          tokens=86,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='weight',
          body='public static function weight($id = null){\n'
               '        if ($id == null) {\n'
               '            $result = '
               "DB::table('tasks')->where('user_id',Auth::id())->whereState('incomplete')->sum('weight');\n"
               '        }else{\n'
               '            $result = '
               "DB::table('tasks')->where('user_id',$id)->whereState('incomplete')->sum('weight');\n"
               '        }\n'
               '        return $result;\n'
               '    }'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=799,
          lineno=101,
          tokens=149,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='get_gravatar',
          body='public static function get_gravatar( $email, $s = 80, $d = '
               "'mm', $r = 'g', $img = false, $atts = array() ) {\n"
               "        $url = 'http://www.gravatar.com/avatar/';\n"
               '        $url .= md5( strtolower( trim( $email ) ) );\n'
               '        $url .= "?s=$s&d=$d&r=$r";\n'
               '        if ( $img ) {\n'
               '            $url = \'<img src="\' . $url . \'"\';\n'
               '            foreach ( $atts as $key => $val )\n'
               '                $url .= \' \' . $key . \'="\' . $val . \'"\';\n'
               "            $url .= ' />';\n"
               '        }\n'
               '        return $url;\n'
               '    }'),
 Fragment(document_cs='c737a60f554d002553c8cb69aa26716ae2f6c1d44d3e30c4fd84cd4e2fc64cb6',
          id=800,
          lineno=1,
          tokens=36,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: clients get_gravatar inProjects projects tasks '
               'weight\n'
               '  Classes: User\n'
               '  Usages: atts email fillable hidden img key result table this '
               'url val\n'),
 Fragment(document_cs='c73acac55dd8e955eab6842fa21d52b3094199f6ec39bdac1f3532357ebd24e6',
          id=801,
          lineno=1,
          tokens=6,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Usages: app\n'),
 Fragment(document_cs='c905bb3740fbef9356dab5fd9854557526664c159c79c791a336e639d90ee57a',
          id=802,
          lineno=6,
          tokens=187,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='BaseController',
          body='class BaseController extends Controller {\n'
               '\tprivate $statusCode = 200;\n'
               '\n'
               '    // Set the status code\n'
               '\tpublic function setStatusCode($statusCode)\n'
               '\t{\n'
               '\t\t$this->statusCode = $statusCode;\n'
               '\n'
               '\t\treturn $this;\n'
               '\t}\n'
               '\n'
               '    // Return the response status code\n'
               '    public function getStatusCode()\n'
               '    {\n'
               '        return $this->statusCode;\n'
               '    }\n'
               '\n'
               '    // Construct the entire response and return it\n'
               '    public function makeResponse($message, $data = null)\n'
               '    {\n'
               '        return Response::json([\n'
               "            'status_code' => $this->getStatusCode(),\n"
               "            'message' => $message,\n"
               "            'data' => $data\n"
               '        ], $this->getStatusCode());\n'
               '    }\n'
               '\n'
               '    // Setup the layout used by the controller.\n'
               '\tprotected function setupLayout()\n'
               '\t{\n'
               '\t\tif ( ! is_null($this->layout))\n'
               '\t\t{\n'
               '\t\t\t$this->layout = View::make($this->layout);\n'
               '\t\t}\n'
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='c905bb3740fbef9356dab5fd9854557526664c159c79c791a336e639d90ee57a',
          id=803,
          lineno=10,
          tokens=25,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='setStatusCode',
          body='public function setStatusCode($statusCode)\n'
               '\t{\n'
               '\t\t$this->statusCode = $statusCode;\n'
               '\n'
               '\t\treturn $this;\n'
               '\t}'),
 Fragment(document_cs='c905bb3740fbef9356dab5fd9854557526664c159c79c791a336e639d90ee57a',
          id=804,
          lineno=18,
          tokens=16,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='getStatusCode',
          body='public function getStatusCode()\n'
               '    {\n'
               '        return $this->statusCode;\n'
               '    }'),
 Fragment(document_cs='c905bb3740fbef9356dab5fd9854557526664c159c79c791a336e639d90ee57a',
          id=805,
          lineno=24,
          tokens=56,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='makeResponse',
          body='public function makeResponse($message, $data = null)\n'
               '    {\n'
               '        return Response::json([\n'
               "            'status_code' => $this->getStatusCode(),\n"
               "            'message' => $message,\n"
               "            'data' => $data\n"
               '        ], $this->getStatusCode());\n'
               '    }'),
 Fragment(document_cs='c905bb3740fbef9356dab5fd9854557526664c159c79c791a336e639d90ee57a',
          id=806,
          lineno=34,
          tokens=40,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='setupLayout',
          body='protected function setupLayout()\n'
               '\t{\n'
               '\t\tif ( ! is_null($this->layout))\n'
               '\t\t{\n'
               '\t\t\t$this->layout = View::make($this->layout);\n'
               '\t\t}\n'
               '\t}'),
 Fragment(document_cs='c905bb3740fbef9356dab5fd9854557526664c159c79c791a336e639d90ee57a',
          id=807,
          lineno=1,
          tokens=26,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: getStatusCode makeResponse setStatusCode '
               'setupLayout\n'
               '  Classes: BaseController\n'
               '  Usages: data message statusCode this\n'),
 Fragment(document_cs='cb0ba65f1cd3f35aeda2dc83a7b447b832fce06d069d41f6c2860070ef208ba2',
          id=808,
          lineno=7,
          tokens=54,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CredentialsTableSeeder',
          body='class CredentialsTableSeeder extends Seeder {\n'
               '\n'
               '\tpublic function run()\n'
               '\t{\n'
               '\t\t$faker = Faker::create();\n'
               '\n'
               '\t\tforeach(range(1, 10) as $index)\n'
               '\t\t{\n'
               '\t\t\tCredential::create([\n'
               '\n'
               '\t\t\t]);\n'
               '\t\t}\n'
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='cb0ba65f1cd3f35aeda2dc83a7b447b832fce06d069d41f6c2860070ef208ba2',
          id=809,
          lineno=9,
          tokens=46,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='run',
          body='public function run()\n'
               '\t{\n'
               '\t\t$faker = Faker::create();\n'
               '\n'
               '\t\tforeach(range(1, 10) as $index)\n'
               '\t\t{\n'
               '\t\t\tCredential::create([\n'
               '\n'
               '\t\t\t]);\n'
               '\t\t}\n'
               '\t}'),
 Fragment(document_cs='cb0ba65f1cd3f35aeda2dc83a7b447b832fce06d069d41f6c2860070ef208ba2',
          id=810,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: run\n'
               '  Classes: CredentialsTableSeeder\n'
               '  Usages: faker index\n'),
 Fragment(document_cs='cd2f979fb3f16ca661a51a09b7abf8d828988026615f2027ce1175139d422096',
          id=811,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=812,
          lineno=1,
          tokens=241,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='project = new Vue({\n'
               "    el: '#project',\n"
               '    data: {\n'
               '        project: { id: null, name : null, weight : null, '
               'production : null, dev : null, github: null, description: '
               'null},\n'
               '        newProject: {name: null, project_id: null},\n'
               '        newTask: {name: null, weight: null, state: null, '
               'priority: null, description: null},\n'
               '        currentTask: {name: null, weight: null, state: null, '
               'priority: null, description: null},\n'
               '        newCredential: {type: null, name: null, hostname: '
               'null, username: null, password: null, port: null},\n'
               '        currentCredential: {type: null, name: null, hostname: '
               'null, username: null, password: null, port: null},\n'
               '        msg: {success: null, error: null},\n'
               '        owner: {id: null},\n'
               '        members: [],\n'
               '        invited: {email: null}\n'
               '    },\n'
               '    ready: function(){\n'
               '        this.setupProject();\n'
               '    },\n'
               '    computed: {\n'
               '        projectWeight: function(){\n'
               '            var tasks = this.project.tasks;\n'
               '            var remainingWeight = 0;\n'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=813,
          lineno=20,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='tasks',
          body='tasks = this.project.tasks'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=814,
          lineno=21,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='remainingWeight',
          body='remainingWeight = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=815,
          lineno=22,
          tokens=208,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='\n'
               '            for (var i = 0; i < tasks.length; i++){\n'
               '                if( tasks[i].state != "complete" ){\n'
               '                    remainingWeight = remainingWeight + '
               'Number(tasks[i].weight);\n'
               '                }\n'
               '            }\n'
               '\n'
               '            return remainingWeight;\n'
               '        },\n'
               '        numTasks: function(){\n'
               '            var tasks = this.project.tasks;\n'
               '            var finalNum = 0;\n'
               '\n'
               '            for (var i = 0; i < tasks.length; i++){\n'
               '                if( tasks[i].state != "backlog" ){\n'
               '                    finalNum++;\n'
               '                }\n'
               '            }\n'
               '\n'
               '            return finalNum;\n'
               '        },\n'
               '        numProgressTasks: function(){\n'
               '            var tasks = this.project.tasks;\n'
               '            var finalNum = 0;\n'
               '\n'
               '            for (var i = 0; i < tasks.length; i++){\n'
               '                if( tasks[i].state == "progress" ){\n'
               '                    finalNum++;\n'
               '                }\n'
               '            }\n'
               '\n'
               '            return finalNum;\n'
               '        },\n'
               '        numTestingTasks: function(){\n'
               '            var tasks = this.project.tasks;\n'
               '            var finalNum = 0;\n'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=816,
          lineno=23,
          tokens=4,
          depth=12,
          parent_id=None,
          category='variable',
          summary=False,
          name='i',
          body='i = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=817,
          lineno=32,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='tasks',
          body='tasks = this.project.tasks'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=818,
          lineno=33,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='finalNum',
          body='finalNum = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=819,
          lineno=35,
          tokens=4,
          depth=12,
          parent_id=None,
          category='variable',
          summary=False,
          name='i',
          body='i = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=820,
          lineno=44,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='tasks',
          body='tasks = this.project.tasks'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=821,
          lineno=45,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='finalNum',
          body='finalNum = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=822,
          lineno=47,
          tokens=4,
          depth=12,
          parent_id=None,
          category='variable',
          summary=False,
          name='i',
          body='i = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=823,
          lineno=56,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='tasks',
          body='tasks = this.project.tasks'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=824,
          lineno=57,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='finalNum',
          body='finalNum = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=825,
          lineno=58,
          tokens=223,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='\n'
               '            for (var i = 0; i < tasks.length; i++){\n'
               '                if( tasks[i].state == "testing" ){\n'
               '                    finalNum++;\n'
               '                }\n'
               '            }\n'
               '\n'
               '            return finalNum;\n'
               '        },\n'
               '        numCompleteTasks: function(){\n'
               '            var tasks = this.project.tasks;\n'
               '            var finalNum = 0;\n'
               '\n'
               '            for (var i = 0; i < tasks.length; i++){\n'
               '                if( tasks[i].state == "complete" ){\n'
               '                    finalNum++;\n'
               '                }\n'
               '            }\n'
               '\n'
               '            return finalNum;\n'
               '        },\n'
               '        numBacklogTasks: function(){\n'
               '            var tasks = this.project.tasks;\n'
               '            var finalNum = 0;\n'
               '\n'
               '            for (var i = 0; i < tasks.length; i++){\n'
               '                if( tasks[i].state == "backlog" ){\n'
               '                    finalNum++;\n'
               '                }\n'
               '            }\n'
               '\n'
               '            return finalNum;\n'
               '        },\n'
               '        numCredentials: function(){\n'
               '            return this.project.credentials.length;\n'
               '        },\n'
               '        projectProgress: function(){\n'
               '            var tasks = this.project.tasks;\n'
               '            var totalWeight = 0;\n'
               '            var completedWeight = 0;\n'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=826,
          lineno=59,
          tokens=4,
          depth=12,
          parent_id=None,
          category='variable',
          summary=False,
          name='i',
          body='i = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=827,
          lineno=68,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='tasks',
          body='tasks = this.project.tasks'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=828,
          lineno=69,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='finalNum',
          body='finalNum = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=829,
          lineno=71,
          tokens=4,
          depth=12,
          parent_id=None,
          category='variable',
          summary=False,
          name='i',
          body='i = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=830,
          lineno=80,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='tasks',
          body='tasks = this.project.tasks'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=831,
          lineno=81,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='finalNum',
          body='finalNum = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=832,
          lineno=83,
          tokens=4,
          depth=12,
          parent_id=None,
          category='variable',
          summary=False,
          name='i',
          body='i = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=833,
          lineno=95,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='tasks',
          body='tasks = this.project.tasks'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=834,
          lineno=96,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='totalWeight',
          body='totalWeight = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=835,
          lineno=97,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='completedWeight',
          body='completedWeight = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=836,
          lineno=98,
          tokens=145,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='\n'
               '            for (var i = 0; i < tasks.length; i++){\n'
               '                totalWeight = totalWeight + '
               'Number(tasks[i].weight);\n'
               '\n'
               '                if( tasks[i].state == "complete" ){\n'
               '                    completedWeight = completedWeight + '
               'Number(tasks[i].weight);\n'
               '                }\n'
               '            }\n'
               '            return  (completedWeight / totalWeight) * 100;\n'
               '        }\n'
               '    },\n'
               '    methods: {\n'
               '        setupProject: function(){\n'
               '            this.getOwner();\n'
               '            this.getMembers();\n'
               '            var url = window.location.href,\n'
               "                project_id  = url.split('/').splice(-1);\n"
               '\n'
               '            $.get( window.baseurl + '
               '"/api/projects/"+project_id, function( results ) {\n'
               '                project.project = results.data;\n'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=837,
          lineno=99,
          tokens=4,
          depth=12,
          parent_id=None,
          category='variable',
          summary=False,
          name='i',
          body='i = 0'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=838,
          lineno=113,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='url',
          body='url = window.location.href'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=839,
          lineno=114,
          tokens=12,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='project_id',
          body="project_id  = url.split('/').splice(-1)"),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=840,
          lineno=118,
          tokens=249,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='                Vue.nextTick(function () {\n'
               '                    megaMenuInit();\n'
               '                })\n'
               '            }).fail(function(e){\n'
               '                console.log( "error "+ e );\n'
               '            });\n'
               '        },\n'
               '        startProjectEditMode: function(){\n'
               '            this.msg.success = null;\n'
               '            this.msg.error = null;\n'
               '            $(".popup-form.update-project").show();\n'
               '            $(".popup-form.update-project .first").focus();\n'
               '        },\n'
               '        updateProject: function(){\n'
               '\n'
               '            var updatedProject = this.project;\n'
               '\n'
               '            delete updatedProject.tasks;\n'
               '            delete updatedProject.credentials;\n'
               '\n'
               '            updatedProject._method = "put";\n'
               '\n'
               '            $.ajax({\n'
               "                type: 'POST',\n"
               '                url: window.baseurl + "/api/projects/"+ '
               'updatedProject.id,\n'
               '                data: updatedProject,\n'
               '                error: function(e) {\n'
               '                    var response = '
               'jQuery.parseJSON(e.responseText);\n'
               '\n'
               '                    project.msg.success = null;\n'
               '                    project.msg.error = response.message;\n'
               '\n'
               '                    return false;\n'
               '                },\n'
               '                success: function(result){\n'
               '                    project.msg.success = result.message;\n'
               '                    project.msg.error = null;\n'
               '                }\n'
               '            });\n'
               '        },\n'
               '        deleteTask: function(taskId){\n'
               '            showSheet();\n'
               '            makePrompt("Are you sure you want to delete this '
               'task?","","No now", "Yes");\n'
               '\n'
               '            $("#cancel-btn").click(function(){\n'
               '       '),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=841,
          lineno=133,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='updatedProject',
          body='updatedProject = this.project'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=842,
          lineno=145,
          tokens=24,
          depth=18,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body='response = jQuery.parseJSON(e.responseText)response = '
               'jQuery.parseJSON(e.responseText)response = '
               'jQuery.parseJSON(e.responseText)'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=843,
          lineno=163,
          tokens=242,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='         closePrompt();\n'
               '            });\n'
               '\n'
               '            $("#confirm-btn").click(function(){\n'
               '                $.ajax({\n'
               '                    type: "POST",\n'
               '                    url: window.baseurl + '
               '"/api/tasks/"+taskId,\n'
               '                    data: {_method: "delete"},\n'
               '                    success: function(){\n'
               '                        $(".task-"+taskId).hide();\n'
               '                        closePrompt();\n'
               '                    },\n'
               '                    error: function(e){\n'
               '                        closePrompt();\n'
               '                    }\n'
               '                });\n'
               '            });\n'
               '        },\n'
               '        showTaskCreateForm: function(){\n'
               '            this.msg.success = null;\n'
               '            this.msg.error = null;\n'
               '            $(".popup-form.new-task").show();\n'
               '            $(".popup-form.new-task .first").focus();\n'
               '        },\n'
               '        createTask: function(client_id, project_id){\n'
               '\n'
               '\n'
               '            $.ajax({\n'
               "                type: 'POST',\n"
               '                url: window.baseurl + "/api/tasks/"+ client_id '
               '+"/"+ project_id,\n'
               '                data: project.newTask,\n'
               '                error: function(e) {\n'
               '                    var response = '
               'jQuery.parseJSON(e.responseText);\n'
               '\n'
               '                    project.msg.success = null;\n'
               '                    project.msg.error = response.message;\n'
               '\n'
               '                    return false;\n'
               '                },\n'
               '\n'
               '                success: function(result){\n'
               '                    project.msg.success = result.message;\n'
               '                    project.msg.error = null;\n'
               '\n'
               '                    project.project.tasks.push(result.data);\n'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=844,
          lineno=208,
          tokens=206,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='                    Vue.nextTick(function () {\n'
               '                        megaMenuInit();\n'
               '                    });\n'
               '\n'
               '                    project.newTask.name = null;\n'
               '                    project.newTask.description = null;\n'
               '\n'
               "                    $('.popup-form.new-task select "
               'option:first-child\').attr("selected", "selected");\n'
               '                    '
               "$('.popup-form.new-task').find('input[type=text],textarea,select').filter(':visible:first').focus();\n"
               '                }\n'
               '            });\n'
               '        },\n'
               '        editMode: function(task){\n'
               '            this.msg.success = null;\n'
               '            this.msg.error = null;\n'
               '            this.currentTask = task;\n'
               '            $(".popup-form.update-task").show();\n'
               '            $(".popup-form.update-task .first").focus();\n'
               '        },\n'
               '        updateTask: function(taskId){\n'
               '\n'
               '\n'
               '            this.currentTask._method = "put";\n'
               '\n'
               '            $.ajax({\n'
               "                type: 'POST',\n"
               '                url: window.baseurl + "/api/tasks/"+ taskId,\n'
               '                data: project.currentTask,\n'
               '                error: function(e) {\n'
               '                    var response = '
               'jQuery.parseJSON(e.responseText);\n'
               '\n'
               '                    project.msg.success = null;\n'
               '                    project.msg.error ='),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=845,
          lineno=240,
          tokens=180,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body=' response.message;\n'
               '\n'
               '                    return false;\n'
               '                },\n'
               '                success: function(result){\n'
               '                    project.msg.success = result.message;\n'
               '                    project.msg.error = null;\n'
               '                }\n'
               '            });\n'
               '        },\n'
               '        createCredential: function(user_id, project_id){\n'
               '\n'
               '\n'
               '            var credential = this.newCredential;\n'
               '            credential.user_id = user_id;\n'
               '            credential.project_id = project_id;\n'
               '\n'
               '            $.ajax({\n'
               "                type: 'POST',\n"
               '                url: window.baseurl + "/api/credentials",\n'
               '                data: credential,\n'
               '                error: function(e) {\n'
               '                    var response = '
               'jQuery.parseJSON(e.responseText);\n'
               '\n'
               '                    project.msg.success = null;\n'
               '                    project.msg.error = response.message;\n'
               '\n'
               '                    return false;\n'
               '                },\n'
               '                success: function(result){\n'
               '                    project.msg.success = result.message;\n'
               '                    project.msg.error = null;\n'
               '\n'
               '                    '
               'project.project.credentials.push(result.data);\n'
               '\n'
               '                    project.newCredential.name = null;\n'
               '                    project.newCredent'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=846,
          lineno=253,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='credential',
          body='credential = this.newCredential'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=847,
          lineno=262,
          tokens=16,
          depth=18,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body='response = jQuery.parseJSON(e.responseText)response = '
               'jQuery.parseJSON(e.responseText)'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=848,
          lineno=276,
          tokens=185,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='ial.username = null;\n'
               '                    project.newCredential.hostname = null;\n'
               '                    project.newCredential.password = null;\n'
               '                    project.newCredential.port = null;\n'
               '                }\n'
               '            });\n'
               '        },\n'
               '        deleteCredential: function(credential){\n'
               '            showSheet();\n'
               '            makePrompt("Are you sure you want to delete this '
               'credential?","","No now", "Yes");\n'
               '\n'
               '            $("#cancel-btn").click(function(){\n'
               '                closePrompt();\n'
               '            });\n'
               '\n'
               '            $("#confirm-btn").click(function(){\n'
               '                $.ajax({\n'
               '                    type: "POST",\n'
               '                    url: window.baseurl + '
               '"/api/credentials/"+credential.id,\n'
               '                    data: {_method: "delete"},\n'
               '                    success: function(){\n'
               '                        '
               'project.project.credentials.$remove(credential);\n'
               '                        closePrompt();\n'
               '                    },\n'
               '                    error: function(e){\n'
               '                        closePrompt();\n'
               '                    }\n'
               '                });\n'
               '            });\n'
               '        },\n'
               '        editCredential: function(credential){\n'
               '            this.msg.success = null;\n'
               '            this.msg.error = null;\n'
               '      '),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=849,
          lineno=309,
          tokens=203,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='      this.currentCredential = credential ;\n'
               '            $(".popup-form.update-credential").show();\n'
               '            $(".popup-form.update-credential '
               '.first").focus();\n'
               '        },\n'
               '        updateCredential: function(credentialId){\n'
               '\n'
               '            this.currentCredential._method = "put";\n'
               '\n'
               '            $.ajax({\n'
               "                type: 'POST',\n"
               '                url: window.baseurl + "/api/credentials/"+ '
               'credentialId,\n'
               '                data: project.currentCredential,\n'
               '                error: function(e) {\n'
               '                    var response = '
               'jQuery.parseJSON(e.responseText);\n'
               '\n'
               '                    project.msg.success = null;\n'
               '                    project.msg.error = response.message;\n'
               '\n'
               '                    return false;\n'
               '                },\n'
               '                success: function(result){\n'
               '                    project.msg.success = result.message;\n'
               '                    project.msg.error = null;\n'
               '                }\n'
               '            });\n'
               '        },\n'
               '        getOwner: function(){\n'
               '            var url = window.location.href,\n'
               "                project_id  = url.split('/').splice(-1);\n"
               '\n'
               '            $.get( window.baseurl + '
               '"/api/projects/"+project_id+"/owner", function( results ) {\n'
               '                project.owner = results.data;\n'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=850,
          lineno=336,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='url',
          body='url = window.location.href'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=851,
          lineno=337,
          tokens=12,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='project_id',
          body="project_id  = url.split('/').splice(-1)"),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=852,
          lineno=341,
          tokens=250,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='                Vue.nextTick(function () {\n'
               '                    megaMenuInit();\n'
               '                })\n'
               '            }).fail(function(e){\n'
               '                console.log( "error "+ e );\n'
               '            });\n'
               '        },\n'
               '        getMembers: function(){\n'
               '            var url = window.location.href,\n'
               "                project_id  = url.split('/').splice(-1);\n"
               '\n'
               '            $.get( window.baseurl + '
               '"/api/projects/"+project_id+"/members", function( results ) {\n'
               '                project.members = results.data;\n'
               '                console.log(project.members);\n'
               '                Vue.nextTick(function () {\n'
               '                    megaMenuInit();\n'
               '                })\n'
               '            }).fail(function(e){\n'
               '                console.log( "error "+ e );\n'
               '            });\n'
               '        },\n'
               '        inviteUser: function(project_id){\n'
               '            if(this.invited.email == ""){\n'
               '                this.invited.email = "";\n'
               '            }\n'
               '\n'
               '            $.ajax({\n'
               "                type: 'POST',\n"
               '                url: window.baseurl + "/api/projects/"+ '
               'project_id +"/"+this.invited.email+"/invite",\n'
               '                data: project.currentCredential,\n'
               '                error: function(e) {\n'
               '                    var response = '
               'jQuery.parseJSON(e.responseText);\n'
               '\n'
               '                    project.msg.success = null;\n'
               '                    project.msg.error = response.message;\n'
               '\n'
               '                    return false;\n'
               '                },\n'
               '                success: function(result){\n'
               '                    project.members.push(result.data);\n'
               '                    project.msg.success = re'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=853,
          lineno=349,
          tokens=5,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='url',
          body='url = window.location.href'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=854,
          lineno=350,
          tokens=12,
          depth=11,
          parent_id=None,
          category='variable',
          summary=False,
          name='project_id',
          body="project_id  = url.split('/').splice(-1)"),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=855,
          lineno=372,
          tokens=8,
          depth=18,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body='response = jQuery.parseJSON(e.responseText)'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=856,
          lineno=381,
          tokens=154,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body='sult.message;\n'
               '                    project.msg.error = null;\n'
               '                }\n'
               '            });\n'
               '        },\n'
               '        removeMember: function(project_id, member){\n'
               '            showSheet();\n'
               '            makePrompt("Are you sure you want to remove this '
               'member from this project?","","Not now", "Yes");\n'
               '\n'
               '            $("#cancel-btn").click(function(){\n'
               '                closePrompt();\n'
               '            });\n'
               '\n'
               '            $("#confirm-btn").click(function(){\n'
               '                $.ajax({\n'
               '                    type: "POST",\n'
               '                    url: window.baseurl + '
               '"/api/projects/"+project_id+"/"+member.id+"/remove",\n'
               '                    data: {_method: "delete"},\n'
               '                    success: function(){\n'
               '                        project.members.$remove(member);\n'
               '                        closePrompt();\n'
               '                    },\n'
               '                    error: function(e){\n'
               '                        closePrompt();\n'
               '                    }\n'
               '                });\n'
               '            });\n'
               '        }\n'
               '    }\n'
               '\n'
               '})'),
 Fragment(document_cs='cf1c6ea9d1ebf1bc2931706d094d7f283c9e07d7435d0c988e089c9a8b470bef',
          id=857,
          lineno=1,
          tokens=51,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: completedWeight credential finalNum project '
               'project_id remainingWeight response tasks totalWeight '
               'updatedProject url\n'
               '  Usages: Number Vue client_id closePrompt console '
               'credentialId jQuery makePrompt megaMenuInit member result '
               'results showSheet task taskId user_id window\n'),
 Fragment(document_cs='d03a66c59ff14a2b90e06f70685cecc4b766b6abea5d100d629d56e092173f05',
          id=858,
          lineno=15,
          tokens=85,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ClientsController',
          body='class ClientsController extends BaseController {\n'
               '\n'
               '\t// Go to clients index page\n'
               '\tpublic function index()\n'
               '\t{\t\n'
               '\t\treturn View::make(\'ins/clients/index\')->with("pTitle", '
               '"Clients");\n'
               '\t}\n'
               '\n'
               '    // Get all clients for the given user\n'
               '    public function getAllUserClients($withWeight = false){\n'
               '        $clients = '
               "Client::with('projects')->where('user_id',Auth::id())->get();\n"),
 Fragment(document_cs='d03a66c59ff14a2b90e06f70685cecc4b766b6abea5d100d629d56e092173f05',
          id=859,
          lineno=26,
          tokens=168,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ClientsController',
          body='\n'
               '        if (count($clients) === 0) {\n'
               '            return '
               "$this->setStatusCode(400)->makeResponse('Could not find "
               "clients');\n"
               '        }\n'
               '\n'
               '        // Get each project total weight if needed\n'
               '        if($withWeight == true){\n'
               '            if($clients) {\n'
               '                foreach ($clients as $client) {\n'
               '                    if($client->projects){\n'
               '                        foreach($client->projects as '
               '$project){\n'
               '                            $weight = '
               "Project::find($project->id)->tasks()->where('state','!=','complete')->sum('weight');\n"
               '                            $project["weight"] = $weight;\n'
               '                        }\n'
               '                    }\n'
               '                }\n'
               '            }\n'
               '        }\n'
               '        return '
               "$this->setStatusCode(200)->makeResponse('Clients retrieved "
               "successfully',$clients->toArray());\n"
               '    }\n'
               '\n'
               '    // Insert a new client into the database\n'
               '    public function storeClient(){\n'),
 Fragment(document_cs='d03a66c59ff14a2b90e06f70685cecc4b766b6abea5d100d629d56e092173f05',
          id=860,
          lineno=49,
          tokens=186,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ClientsController',
          body='\n'
               "        if (  strlen(trim(Input::get('name'))) == 0) {\n"
               '            return '
               "$this->setStatusCode(400)->makeResponse('Name field is "
               "required');\n"
               '        }\n'
               '\n'
               "        Input::merge(array('user_id' => Auth::id()));\n"
               '        Client::create(Input::all());\n'
               '        $id = \\DB::getPdo()->lastInsertId();\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('Client "
               "created successfully', Client::find($id));\n"
               '    }\n'
               '\n'
               '    // Update the given client\n'
               '    public function updateClient($id){\n'
               '        if (count(Input::all()) <= 1) {\n'
               "            return $this->setStatusCode(406)->makeResponse('No "
               "information provided to update client');\n"
               '        }\n'
               '\n'
               "        if( strlen(trim(Input::get('name'))) === 0 ){\n"
               '            return '
               "$this->setStatusCode(406)->makeResponse('The client name is "
               "required');\n"
               '        }\n'),
 Fragment(document_cs='d03a66c59ff14a2b90e06f70685cecc4b766b6abea5d100d629d56e092173f05',
          id=861,
          lineno=70,
          tokens=250,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='ClientsController',
          body='\n'
               '        if (!Client::find($id)) {\n'
               '            return '
               "$this->setStatusCode(404)->makeResponse('Client not found');\n"
               '        }\n'
               '\n'
               '        $input = Input::all();\n'
               "        unset($input['_method']);\n"
               '\n'
               '        Client::find($id)->update($input);\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('The "
               "client has been updated');\n"
               '    }\n'
               '\n'
               '    // Remove the given client and all tasks, projects and '
               'credentials attached to it\n'
               '    public function removeClient($id){\n'
               '        if (!Client::find($id)) {\n'
               '            return '
               "$this->setStatusCode(400)->makeResponse('Could not find the "
               "client');\n"
               '        }\n'
               '\n'
               '        $client \t= \tClient::find($id);\n'
               '\n'
               '        // delete all related tasks and credentials\n'
               '        foreach ($client->projects as $p) {\n'
               "            Task::where('project_id', $p->id)->delete();\n"
               "            Credential::where('project_id', "
               '$p->id)->delete();\n'
               '            $p->members()->detach();\n'
               '        }\n'
               '\n'
               '        // delete projects\n'
               '        Project::where("client_id", $id)->delete();\n'
               '        $client->delete();\n'
               "        return $this->setStatusCode(200)->makeResponse('Client "
               "deleted successfully');\n"
               '    }\n'
               '\n'
               '}'),
 Fragment(document_cs='d03a66c59ff14a2b90e06f70685cecc4b766b6abea5d100d629d56e092173f05',
          id=862,
          lineno=18,
          tokens=28,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='index',
          body='public function index()\n'
               '\t{\t\n'
               '\t\treturn View::make(\'ins/clients/index\')->with("pTitle", '
               '"Clients");\n'
               '\t}'),
 Fragment(document_cs='d03a66c59ff14a2b90e06f70685cecc4b766b6abea5d100d629d56e092173f05',
          id=863,
          lineno=24,
          tokens=183,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='getAllUserClients',
          body='public function getAllUserClients($withWeight = false){\n'
               '        $clients = '
               "Client::with('projects')->where('user_id',Auth::id())->get();\n"
               '\n'
               '        if (count($clients) === 0) {\n'
               '            return '
               "$this->setStatusCode(400)->makeResponse('Could not find "
               "clients');\n"
               '        }\n'
               '\n'
               '        // Get each project total weight if needed\n'
               '        if($withWeight == true){\n'
               '            if($clients) {\n'
               '                foreach ($clients as $client) {\n'
               '                    if($client->projects){\n'
               '                        foreach($client->projects as '
               '$project){\n'
               '                            $weight = '
               "Project::find($project->id)->tasks()->where('state','!=','complete')->sum('weight');\n"
               '                            $project["weight"] = $weight;\n'
               '                        }\n'
               '                    }\n'
               '                }\n'
               '            }\n'
               '        }\n'
               '        return '
               "$this->setStatusCode(200)->makeResponse('Clients retrieved "
               "successfully',$clients->toArray());\n"
               '    }'),
 Fragment(document_cs='d03a66c59ff14a2b90e06f70685cecc4b766b6abea5d100d629d56e092173f05',
          id=864,
          lineno=48,
          tokens=104,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='storeClient',
          body='public function storeClient(){\n'
               '\n'
               "        if (  strlen(trim(Input::get('name'))) == 0) {\n"
               '            return '
               "$this->setStatusCode(400)->makeResponse('Name field is "
               "required');\n"
               '        }\n'
               '\n'
               "        Input::merge(array('user_id' => Auth::id()));\n"
               '        Client::create(Input::all());\n'
               '        $id = \\DB::getPdo()->lastInsertId();\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('Client "
               "created successfully', Client::find($id));\n"
               '    }'),
 Fragment(document_cs='d03a66c59ff14a2b90e06f70685cecc4b766b6abea5d100d629d56e092173f05',
          id=865,
          lineno=62,
          tokens=154,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='updateClient',
          body='public function updateClient($id){\n'
               '        if (count(Input::all()) <= 1) {\n'
               "            return $this->setStatusCode(406)->makeResponse('No "
               "information provided to update client');\n"
               '        }\n'
               '\n'
               "        if( strlen(trim(Input::get('name'))) === 0 ){\n"
               '            return '
               "$this->setStatusCode(406)->makeResponse('The client name is "
               "required');\n"
               '        }\n'
               '\n'
               '        if (!Client::find($id)) {\n'
               '            return '
               "$this->setStatusCode(404)->makeResponse('Client not found');\n"
               '        }\n'
               '\n'
               '        $input = Input::all();\n'
               "        unset($input['_method']);\n"
               '\n'
               '        Client::find($id)->update($input);\n'
               '\n'
               "        return $this->setStatusCode(200)->makeResponse('The "
               "client has been updated');\n"
               '    }'),
 Fragment(document_cs='d03a66c59ff14a2b90e06f70685cecc4b766b6abea5d100d629d56e092173f05',
          id=866,
          lineno=84,
          tokens=154,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='removeClient',
          body='public function removeClient($id){\n'
               '        if (!Client::find($id)) {\n'
               '            return '
               "$this->setStatusCode(400)->makeResponse('Could not find the "
               "client');\n"
               '        }\n'
               '\n'
               '        $client \t= \tClient::find($id);\n'
               '\n'
               '        // delete all related tasks and credentials\n'
               '        foreach ($client->projects as $p) {\n'
               "            Task::where('project_id', $p->id)->delete();\n"
               "            Credential::where('project_id', "
               '$p->id)->delete();\n'
               '            $p->members()->detach();\n'
               '        }\n'
               '\n'
               '        // delete projects\n'
               '        Project::where("client_id", $id)->delete();\n'
               '        $client->delete();\n'
               "        return $this->setStatusCode(200)->makeResponse('Client "
               "deleted successfully');\n"
               '    }'),
 Fragment(document_cs='d03a66c59ff14a2b90e06f70685cecc4b766b6abea5d100d629d56e092173f05',
          id=867,
          lineno=1,
          tokens=33,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: getAllUserClients index removeClient storeClient '
               'updateClient\n'
               '  Classes: ClientsController\n'
               '  Usages: client clients input project this weight '
               'withWeight\n'),
 Fragment(document_cs='d8a0ab7eb76f5cc8ef41831a9ddbc6ba6660fb568f15997663cad5cc8efd5950',
          id=868,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='db27227badae8e9a4563279ae007daf0fe9d823ee87fdc6cb0ac31e4b7b9e421',
          id=869,
          lineno=8,
          tokens=113,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='PasswordController',
          body='class PasswordController extends Controller\n'
               '{\n'
               '    /*\n'
               '    '
               '|--------------------------------------------------------------------------\n'
               '    | Password Reset Controller\n'
               '    '
               '|--------------------------------------------------------------------------\n'
               '    |\n'
               '    | This controller is responsible for handling password '
               'reset requests\n'
               "    | and uses a simple trait to include this behavior. You're "
               'free to\n'
               '    | explore this trait and override any methods you wish to '
               'tweak.\n'
               '    |\n'
               '    */\n'
               '\n'
               '    use ResetsPasswords;\n'
               '\n'
               '    /**\n'
               '     * Create a new password controller instance.\n'
               '     *\n'
               '     * @return void\n'
               '     */\n'
               '    public function __construct()\n'
               '    {\n'
               "        $this->middleware('guest');\n"
               '    }\n'
               '}'),
 Fragment(document_cs='db27227badae8e9a4563279ae007daf0fe9d823ee87fdc6cb0ac31e4b7b9e421',
          id=870,
          lineno=28,
          tokens=17,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='__construct',
          body='public function __construct()\n'
               '    {\n'
               "        $this->middleware('guest');\n"
               '    }'),
 Fragment(document_cs='db27227badae8e9a4563279ae007daf0fe9d823ee87fdc6cb0ac31e4b7b9e421',
          id=871,
          lineno=1,
          tokens=18,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: __construct\n'
               '  Classes: PasswordController\n'
               '  Usages: this\n'),
 Fragment(document_cs='ddfbfa4f0a89ce9d1acee750fbe779f59688781f0bf0489865d811a6d241e7f7',
          id=872,
          lineno=7,
          tokens=46,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Upload',
          body='class Upload extends Model {\n'
               '\tprotected $fillable = [];\n'
               '\n'
               '    public function user(){\n'
               "        return $this->belongsTo('App\\User');\n"
               '    }\n'
               '\n'
               '    public function project(){\n'
               "        return $this->belongsTo('App\\Project');\n"
               '    }\n'
               '\n'
               '}'),
 Fragment(document_cs='ddfbfa4f0a89ce9d1acee750fbe779f59688781f0bf0489865d811a6d241e7f7',
          id=873,
          lineno=10,
          tokens=16,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='user',
          body='public function user(){\n'
               "        return $this->belongsTo('App\\User');\n"
               '    }'),
 Fragment(document_cs='ddfbfa4f0a89ce9d1acee750fbe779f59688781f0bf0489865d811a6d241e7f7',
          id=874,
          lineno=14,
          tokens=17,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='project',
          body='public function project(){\n'
               "        return $this->belongsTo('App\\Project');\n"
               '    }'),
 Fragment(document_cs='ddfbfa4f0a89ce9d1acee750fbe779f59688781f0bf0489865d811a6d241e7f7',
          id=875,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: project user\n'
               '  Classes: Upload\n'
               '  Usages: fillable this\n'),
 Fragment(document_cs='de775212fc3aa7a5b457ee660a7e866a4323d7cd08ca44ef1e23576fe3267c03',
          id=876,
          lineno=3,
          tokens=110,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='TestCase',
          body='class TestCase extends '
               'Illuminate\\Foundation\\Testing\\TestCase\n'
               '{\n'
               '    /**\n'
               '     * The base URL to use while testing the application.\n'
               '     *\n'
               '     * @var string\n'
               '     */\n'
               "    protected $baseUrl = 'http://localhost';\n"
               '\n'
               '    /**\n'
               '     * Creates the application.\n'
               '     *\n'
               '     * @return \\Illuminate\\Foundation\\Application\n'
               '     */\n'
               '    public function createApplication()\n'
               '    {\n'
               "        $app = require __DIR__.'/../bootstrap/app.php';\n"
               '\n'
               '        '
               '$app->make(Illuminate\\Contracts\\Console\\Kernel::class)->bootstrap();\n'
               '\n'
               '        return $app;\n'
               '    }\n'
               '}'),
 Fragment(document_cs='de775212fc3aa7a5b457ee660a7e866a4323d7cd08ca44ef1e23576fe3267c03',
          id=877,
          lineno=17,
          tokens=43,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='createApplication',
          body='public function createApplication()\n'
               '    {\n'
               "        $app = require __DIR__.'/../bootstrap/app.php';\n"
               '\n'
               '        '
               '$app->make(Illuminate\\Contracts\\Console\\Kernel::class)->bootstrap();\n'
               '\n'
               '        return $app;\n'
               '    }'),
 Fragment(document_cs='de775212fc3aa7a5b457ee660a7e866a4323d7cd08ca44ef1e23576fe3267c03',
          id=878,
          lineno=1,
          tokens=18,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: createApplication\n'
               '  Classes: TestCase\n'
               '  Usages: app baseUrl\n'),
 Fragment(document_cs='e11f2f6c115abe7487355ccf7de21e489d6b9775b6b284f8509a8eb2684209cb',
          id=879,
          lineno=1,
          tokens=24,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='config.php\n'
               'routes.php\n'
               'compiled.php\n'
               'services.json\n'
               'events.scanned.php\n'
               'routes.scanned.php\n'
               'down\n'),
 Fragment(document_cs='e11f2f6c115abe7487355ccf7de21e489d6b9775b6b284f8509a8eb2684209cb',
          id=880,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='e1c3b7d81e53a5b3da7f1c9d8fef067c26517b3a3635f51fce1cedd2325864be',
          id=881,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='e40b96bd2b64e19c374b195716d40a09e105bf7eada6011e6cf74325fdecd69e',
          id=882,
          lineno=6,
          tokens=141,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='CreateTasksTable',
          body='class CreateTasksTable extends Migration {\n'
               '\n'
               '\t/**\n'
               '\t * Run the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function up()\n'
               '\t{\n'
               "\t\tSchema::create('tasks', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->integer('user_id');\n"
               "\t\t\t$table->integer('project_id');\n"
               "\t\t\t$table->string('name');\n"
               "\t\t\t$table->string('state');\n"
               "\t\t\t$table->string('weight');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}\n'
               '\n'
               '\n'
               '\t/**\n'
               '\t * Reverse the migrations.\n'
               '\t *\n'
               '\t * @return void\n'
               '\t */\n'
               '\tpublic function down()\n'
               '\t{\n'
               "\t\tSchema::drop('tasks');\n"
               '\t}\n'
               '\n'
               '}'),
 Fragment(document_cs='e40b96bd2b64e19c374b195716d40a09e105bf7eada6011e6cf74325fdecd69e',
          id=883,
          lineno=13,
          tokens=82,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='up',
          body='public function up()\n'
               '\t{\n'
               "\t\tSchema::create('tasks', function(Blueprint $table)\n"
               '\t\t{\n'
               "\t\t\t$table->increments('id');\n"
               "\t\t\t$table->integer('user_id');\n"
               "\t\t\t$table->integer('project_id');\n"
               "\t\t\t$table->string('name');\n"
               "\t\t\t$table->string('state');\n"
               "\t\t\t$table->string('weight');\n"
               '\t\t\t$table->timestamps();\n'
               '\t\t});\n'
               '\t}'),
 Fragment(document_cs='e40b96bd2b64e19c374b195716d40a09e105bf7eada6011e6cf74325fdecd69e',
          id=884,
          lineno=33,
          tokens=15,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='down',
          body="public function down()\n\t{\n\t\tSchema::drop('tasks');\n\t}"),
 Fragment(document_cs='e40b96bd2b64e19c374b195716d40a09e105bf7eada6011e6cf74325fdecd69e',
          id=885,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: down up\n'
               '  Classes: CreateTasksTable\n'
               '  Usages: table\n'),
 Fragment(document_cs='e5c4b84484ee4216e9373be99380320c25dd94805f99f0a805846f087636553f',
          id=886,
          lineno=1,
          tokens=6,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='User-agent: *\nDisallow:\n'),
 Fragment(document_cs='e5c4b84484ee4216e9373be99380320c25dd94805f99f0a805846f087636553f',
          id=887,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='e753774a5c6c845d5b43db5e4e133c8b7308c233f036517be1e2ae01cb068790',
          id=888,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='* text=auto\n'),
 Fragment(document_cs='e753774a5c6c845d5b43db5e4e133c8b7308c233f036517be1e2ae01cb068790',
          id=889,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='e93e54786a45490a6dc5cd106ae450a93b778ccd246ff7dfb33eb7c112805b3d',
          id=890,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=891,
          lineno=10,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='animated',
          body='.animated.animated'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=892,
          lineno=17,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='infinite',
          body='.animated.infinite'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=893,
          lineno=22,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='animated',
          body='.animated'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=894,
          lineno=22,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hinge',
          body='.animated.hinge'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=895,
          lineno=87,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounce',
          body='.bounce'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=896,
          lineno=115,
          tokens=1,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='flash',
          body='.flash'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=897,
          lineno=159,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='pulse',
          body='.pulse'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=898,
          lineno=245,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rubberBand',
          body='.rubberBand'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=899,
          lineno=287,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='shake',
          body='.shake'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=900,
          lineno=351,
          tokens=1,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='swing',
          body='.swing'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=901,
          lineno=418,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='tada',
          body='.tada'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=902,
          lineno=506,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='wobble',
          body='.wobble'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=903,
          lineno=597,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounceIn',
          body='.bounceIn'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=904,
          lineno=677,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounceInDown',
          body='.bounceInDown'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=905,
          lineno=755,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounceInLeft',
          body='.bounceInLeft'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=906,
          lineno=833,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounceInRight',
          body='.bounceInRight'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=907,
          lineno=911,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounceInUp',
          body='.bounceInUp'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=908,
          lineno=957,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounceOut',
          body='.bounceOut'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=909,
          lineno=1005,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounceOutDown',
          body='.bounceOutDown'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=910,
          lineno=1040,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounceOutLeft',
          body='.bounceOutLeft'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=911,
          lineno=1075,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounceOutRight',
          body='.bounceOutRight'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=912,
          lineno=1121,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='bounceOutUp',
          body='.bounceOutUp'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=913,
          lineno=1146,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeIn',
          body='.fadeIn'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=914,
          lineno=1181,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeInDown',
          body='.fadeInDown'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=915,
          lineno=1216,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeInDownBig',
          body='.fadeInDownBig'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=916,
          lineno=1251,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeInLeft',
          body='.fadeInLeft'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=917,
          lineno=1286,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeInLeftBig',
          body='.fadeInLeftBig'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=918,
          lineno=1321,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeInRight',
          body='.fadeInRight'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=919,
          lineno=1356,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeInRightBig',
          body='.fadeInRightBig'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=920,
          lineno=1391,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeInUp',
          body='.fadeInUp'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=921,
          lineno=1426,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeInUpBig',
          body='.fadeInUpBig'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=922,
          lineno=1451,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeOut',
          body='.fadeOut'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=923,
          lineno=1481,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeOutDown',
          body='.fadeOutDown'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=924,
          lineno=1511,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeOutDownBig',
          body='.fadeOutDownBig'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=925,
          lineno=1541,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeOutLeft',
          body='.fadeOutLeft'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=926,
          lineno=1571,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeOutLeftBig',
          body='.fadeOutLeftBig'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=927,
          lineno=1601,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeOutRight',
          body='.fadeOutRight'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=928,
          lineno=1631,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeOutRightBig',
          body='.fadeOutRightBig'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=929,
          lineno=1661,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeOutUp',
          body='.fadeOutUp'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=930,
          lineno=1691,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='fadeOutUpBig',
          body='.fadeOutUpBig'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=931,
          lineno=1775,
          tokens=2,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='animated',
          body='.animated'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=932,
          lineno=1775,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='flip',
          body='.animated.flip'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=933,
          lineno=1854,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='flipInX',
          body='.flipInX'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=934,
          lineno=1933,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='flipInY',
          body='.flipInY'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=935,
          lineno=1982,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='flipOutX',
          body='.flipOutX'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=936,
          lineno=2033,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='flipOutY',
          body='.flipOutY'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=937,
          lineno=2099,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='lightSpeedIn',
          body='.lightSpeedIn'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=938,
          lineno=2131,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='lightSpeedOut',
          body='.lightSpeedOut'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=939,
          lineno=2178,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rotateIn',
          body='.rotateIn'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=940,
          lineno=2223,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rotateInDownLeft',
          body='.rotateInDownLeft'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=941,
          lineno=2268,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rotateInDownRight',
          body='.rotateInDownRight'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=942,
          lineno=2313,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rotateInUpLeft',
          body='.rotateInUpLeft'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=943,
          lineno=2358,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rotateInUpRight',
          body='.rotateInUpRight'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=944,
          lineno=2398,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rotateOut',
          body='.rotateOut'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=945,
          lineno=2438,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rotateOutDownLeft',
          body='.rotateOutDownLeft'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=946,
          lineno=2478,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rotateOutDownRight',
          body='.rotateOutDownRight'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=947,
          lineno=2518,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rotateOutUpLeft',
          body='.rotateOutUpLeft'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=948,
          lineno=2558,
          tokens=4,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rotateOutUpRight',
          body='.rotateOutUpRight'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=949,
          lineno=2637,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='hinge',
          body='.hinge'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=950,
          lineno=2674,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rollIn',
          body='.rollIn'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=951,
          lineno=2706,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='rollOut',
          body='.rollOut'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=952,
          lineno=2736,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='zoomIn',
          body='.zoomIn'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=953,
          lineno=2779,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='zoomInDown',
          body='.zoomInDown'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=954,
          lineno=2822,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='zoomInLeft',
          body='.zoomInLeft'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=955,
          lineno=2865,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='zoomInRight',
          body='.zoomInRight'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=956,
          lineno=2908,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='zoomInUp',
          body='.zoomInUp'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=957,
          lineno=2946,
          tokens=2,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='zoomOut',
          body='.zoomOut'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=958,
          lineno=2994,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='zoomOutDown',
          body='.zoomOutDown'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=959,
          lineno=3034,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='zoomOutLeft',
          body='.zoomOutLeft'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=960,
          lineno=3074,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='zoomOutRight',
          body='.zoomOutRight'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=961,
          lineno=3122,
          tokens=3,
          depth=3,
          parent_id=None,
          category='class',
          summary=False,
          name='zoomOutUp',
          body='.zoomOutUp'),
 Fragment(document_cs='e948e5869da246bfe815e9957eb26f2782c0954928aa6b073cc1243e9ad8821e',
          id=962,
          lineno=1,
          tokens=8,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body="  Classes: {' '.join(classes)}\n"),
 Fragment(document_cs='ea034e97bbd489fdbb104cf83f4a551a30c716b784ad6b9194c39fc918e2e588',
          id=963,
          lineno=1,
          tokens=7,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Usages: factory faker\n'),
 Fragment(document_cs='ee0363988a82c4c116c1266edb672d7cb340ee97bd9fa99f6441fb28f687ff4a',
          id=964,
          lineno=13,
          tokens=120,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='HomeController',
          body='class HomeController extends BaseController {\n'
               '\n'
               '\t// Depending if the user is signed in or not, return the '
               'home page \n'
               '\tpublic function index(){\n'
               '\t\tif( Auth::check() ) {\n'
               "\t\t\treturn View::make('ins/hud')->with('pTitle', "
               '"Hud");\n'
               '\t\t}else{\n'
               '\t\t\treturn View::make(\'index\')->with(\'pTitle\', "A '
               'project management system for artisans");\n'
               '\t\t}\n'
               '\t}\n'
               '\n'
               '\t// Search for, clients, projects, and tasks\n'
               '\tpublic function search(){\n'
               '\t\t$q = Input::get("q");\n'
               '\n'
               '        // redirect user back if nothing was typed\n'),
 Fragment(document_cs='ee0363988a82c4c116c1266edb672d7cb340ee97bd9fa99f6441fb28f687ff4a',
          id=965,
          lineno=29,
          tokens=135,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='HomeController',
          body='        if ( empty(trim($q)) ){\n'
               '            return Redirect::back();\n'
               '        }\n'
               '\n'
               "\t\t$clients = Client::where('name', 'like', "
               "'%'.$q.'%')->whereUserId(Auth::id())->get();\n"
               "\t\t$projects = Project::where('name', 'like', "
               "'%'.$q.'%')->whereUserId(Auth::id())->get();\n"
               "\t\t$tasks = Task::where('name', 'like', "
               "'%'.$q.'%')->whereUserId(Auth::id())->get();\n"
               '\t\t$pTitle = "Search Results";\n'
               '\n'
               "\t\treturn View::make('ins/search', "
               "compact('q','clients','projects','tasks','pTitle'));\n"
               '\t}\n'
               '}'),
 Fragment(document_cs='ee0363988a82c4c116c1266edb672d7cb340ee97bd9fa99f6441fb28f687ff4a',
          id=966,
          lineno=16,
          tokens=62,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='index',
          body='public function index(){\n'
               '\t\tif( Auth::check() ) {\n'
               "\t\t\treturn View::make('ins/hud')->with('pTitle', "
               '"Hud");\n'
               '\t\t}else{\n'
               '\t\t\treturn View::make(\'index\')->with(\'pTitle\', "A '
               'project management system for artisans");\n'
               '\t\t}\n'
               '\t}'),
 Fragment(document_cs='ee0363988a82c4c116c1266edb672d7cb340ee97bd9fa99f6441fb28f687ff4a',
          id=967,
          lineno=25,
          tokens=158,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='search',
          body='public function search(){\n'
               '\t\t$q = Input::get("q");\n'
               '\n'
               '        // redirect user back if nothing was typed\n'
               '        if ( empty(trim($q)) ){\n'
               '            return Redirect::back();\n'
               '        }\n'
               '\n'
               "\t\t$clients = Client::where('name', 'like', "
               "'%'.$q.'%')->whereUserId(Auth::id())->get();\n"
               "\t\t$projects = Project::where('name', 'like', "
               "'%'.$q.'%')->whereUserId(Auth::id())->get();\n"
               "\t\t$tasks = Task::where('name', 'like', "
               "'%'.$q.'%')->whereUserId(Auth::id())->get();\n"
               '\t\t$pTitle = "Search Results";\n'
               '\n'
               "\t\treturn View::make('ins/search', "
               "compact('q','clients','projects','tasks','pTitle'));\n"
               '\t}'),
 Fragment(document_cs='ee0363988a82c4c116c1266edb672d7cb340ee97bd9fa99f6441fb28f687ff4a',
          id=968,
          lineno=1,
          tokens=21,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: index search\n'
               '  Classes: HomeController\n'
               '  Usages: clients pTitle projects tasks\n'),
 Fragment(document_cs='eed45adf1a606fa18c44befe1e256a4a562624987550396899ce73adbd82e09c',
          id=969,
          lineno=1,
          tokens=8,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Usages: _SERVER uri\n'),
 Fragment(document_cs='efbd0fdba71eb941d92164b6785ff9921fa014a54a2cec8e7a0fe98e0b61f8bb',
          id=970,
          lineno=7,
          tokens=94,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Task',
          body='class Task extends Model {\n'
               '\tprotected $fillable = [\n'
               "        'name',\n"
               "        'weight',\n"
               "        'user_id',\n"
               "        'project_id',\n"
               "        'state',\n"
               "        'priority',\n"
               "        'description'\n"
               '    ];\n'
               '\n'
               '    protected  $hidden = [\n'
               '        "created_at",\n'
               '        "updated_at",\n'
               '    ];\n'
               '\n'
               '    /**\n'
               '     * Relationship to project\n'
               '     */\n'
               '    public function project(){\n'
               "        return $this->belongsTo('App\\Project', "
               "'project_id');\n"
               '    }\n'
               '}'),
 Fragment(document_cs='efbd0fdba71eb941d92164b6785ff9921fa014a54a2cec8e7a0fe98e0b61f8bb',
          id=971,
          lineno=26,
          tokens=21,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='project',
          body='public function project(){\n'
               "        return $this->belongsTo('App\\Project', "
               "'project_id');\n"
               '    }'),
 Fragment(document_cs='efbd0fdba71eb941d92164b6785ff9921fa014a54a2cec8e7a0fe98e0b61f8bb',
          id=972,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: project\n'
               '  Classes: Task\n'
               '  Usages: fillable hidden this\n'),
 Fragment(document_cs='f21798429d01eaa1459219b1dae02f3471e088ae0c02a92139b819c340c9f751',
          id=973,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='f4bf47fdefb9d091523b1cd5d47f6057a7d4d2cfc48357bab9c71e03a62890f9',
          id=974,
          lineno=13,
          tokens=181,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='AdminController',
          body='class AdminController extends BaseController {\n'
               '\n'
               '    /**\n'
               '     * Takes you to the admin page of the app\n'
               '     * @return mixed\n'
               '     */\n'
               '    public function index(){\n'
               "        if( Auth::user()->email != env('ADMIN_EMAIL') ){\n"
               '            return Redirect::back();\n'
               '        }\n'
               '\n'
               '        $users = User::all();\n'
               '        $n_users = count($users);\n'
               '        $n_tasks = Task::all()->count();\n'
               '        $n_projects = Project::all()->count();\n'
               '        $n_clients = Client::all()->count();\n'
               '\n'
               "        return View::make('admin/index')\n"
               "            ->with('pTitle', 'Admin')\n"
               "            ->with('users', $users)\n"
               "            ->with('n_users', $n_users)\n"
               "            ->with('n_tasks', $n_tasks)\n"
               "            ->with('n_projects', $n_projects)\n"
               "            ->with('n_clients', $n_clients);\n"
               '\n'
               '    }\n'
               '\n'
               '}'),
 Fragment(document_cs='f4bf47fdefb9d091523b1cd5d47f6057a7d4d2cfc48357bab9c71e03a62890f9',
          id=975,
          lineno=19,
          tokens=151,
          depth=3,
          parent_id=None,
          category='function',
          summary=False,
          name='index',
          body='public function index(){\n'
               "        if( Auth::user()->email != env('ADMIN_EMAIL') ){\n"
               '            return Redirect::back();\n'
               '        }\n'
               '\n'
               '        $users = User::all();\n'
               '        $n_users = count($users);\n'
               '        $n_tasks = Task::all()->count();\n'
               '        $n_projects = Project::all()->count();\n'
               '        $n_clients = Client::all()->count();\n'
               '\n'
               "        return View::make('admin/index')\n"
               "            ->with('pTitle', 'Admin')\n"
               "            ->with('users', $users)\n"
               "            ->with('n_users', $n_users)\n"
               "            ->with('n_tasks', $n_tasks)\n"
               "            ->with('n_projects', $n_projects)\n"
               "            ->with('n_clients', $n_clients);\n"
               '\n'
               '    }'),
 Fragment(document_cs='f4bf47fdefb9d091523b1cd5d47f6057a7d4d2cfc48357bab9c71e03a62890f9',
          id=976,
          lineno=1,
          tokens=25,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: index\n'
               '  Classes: AdminController\n'
               '  Usages: n_clients n_projects n_tasks n_users users\n'),
 Fragment(document_cs='f5ea3a5f74623073d515e9ecc3f0c2675af686c9b347ae479905ae3e5ab39c6b',
          id=977,
          lineno=9,
          tokens=17,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Controller',
          body='abstract class Controller extends BaseController\n'
               '{\n'
               '    use DispatchesJobs, ValidatesRequests;\n'
               '}'),
 Fragment(document_cs='f5ea3a5f74623073d515e9ecc3f0c2675af686c9b347ae479905ae3e5ab39c6b',
          id=978,
          lineno=1,
          tokens=5,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Controller\n'),
 Fragment(document_cs='f99b94f6759de8fb8eb453f098a9a7373942239a1c83f940840bb51b7d2ff732',
          id=979,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='f9ee52bc38ef7c17f4d7301c8648ee5012687632b0c2b9fa4b1a8eaa92597225',
          id=980,
          lineno=7,
          tokens=34,
          depth=1,
          parent_id=None,
          category='class',
          summary=False,
          name='Projectuser',
          body='class Projectuser extends Model {\n'
               '\tprotected $fillable = [];\n'
               "\tprotected $hidden = ['id','created_at', 'updated_at'];\n"
               "\tprotected $table = 'project_user';\n"
               '\n'
               '}'),
 Fragment(document_cs='f9ee52bc38ef7c17f4d7301c8648ee5012687632b0c2b9fa4b1a8eaa92597225',
          id=981,
          lineno=1,
          tokens=15,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Projectuser\n  Usages: fillable hidden table\n'),
 Fragment(document_cs='fa700a189e428a2ee2d455b96097fdbc34ebaf445754136a4b59fc70a76f0a93',
          id=982,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='fa93a98550534fc3e0ad7f3097f3475c9c72456201db69bfe3b0829ee5857e58',
          id=983,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='')]