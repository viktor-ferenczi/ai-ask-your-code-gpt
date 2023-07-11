[Hit(uuid='0',
     path='/app/Console/Kernel.php',
     lineno=8,
     depth=1,
     type='class',
     name='Kernel',
     text='class Kernel extends ConsoleKernel\n'
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
          '}',
     tokens=115,
     score=1.0),
 Hit(uuid='1',
     path='/app/Http/Kernel.php',
     lineno=7,
     depth=1,
     type='class',
     name='Kernel',
     text='class Kernel extends HttpKernel\n'
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
          '        \\Illuminate\\Session\\Middleware\\StartSession::class,\n'
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
          "        'auth' => \\App\\Http\\Middleware\\Authenticate::class,\n"
          "        'auth.basic' => "
          '\\Illuminate\\Auth\\Middleware\\AuthenticateWithBasicAuth::class,\n'
          "        'guest' => "
          '\\App\\Http\\Middleware\\RedirectIfAuthenticated::class,\n'
          '    ];\n'
          '}',
     tokens=193,
     score=0.5)]