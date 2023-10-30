[Fragment(document_cs='04e64709b061d51fc79e555ed95a4ab21e36ce306dc8ea6b3f080254ea25ca4e',
          id=1,
          lineno=1,
          tokens=237,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='#########################\n'
               '# .gitignore file for Xcode4 and Xcode5 Source projects\n'
               '#\n'
               '# Apple bugs, waiting for Apple to fix/respond:\n'
               '#\n'
               '#    15564624 - what does the xccheckout file in Xcode5 do? '
               "Where's the documentation?\n"
               '#\n'
               '# Version 2.1\n'
               '# For latest version, see: '
               'http://stackoverflow.com/questions/49478/git-ignore-file-for-xcode-projects\n'
               '#\n'
               '# 2013 updates:\n'
               '# - fixed the broken "save personal Schemes"\n'
               '# - added line-by-line explanations for EVERYTHING (some were '
               'missing)\n'
               '#\n'
               '# NB: if you are storing "built" products, this WILL NOT '
               'WORK,\n'
               '# and you should use a different .gitignore (or none at all)\n'
               '# This file is for SOURCE projects, where there are many '
               'extra\n'
               '# files that we want to exclude\n'
               '#\n'
               '#########################\n'
               '\n'
               '#####\n'
               '# OS X temporary files that should never be committed\n'
               '#\n'
               '# c.f. http://www.westwind.com/reference/os-x/invisibles.html\n'
               '\n'
               '.DS_Store\n'
               '\n'
               '# c.f. http://www.westwind.com/reference/os-x/invisibles.html\n'
               '\n'
               '.Trashes\n'),
 Fragment(document_cs='04e64709b061d51fc79e555ed95a4ab21e36ce306dc8ea6b3f080254ea25ca4e',
          id=2,
          lineno=32,
          tokens=212,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '# c.f. http://www.westwind.com/reference/os-x/invisibles.html\n'
               '\n'
               '*.swp\n'
               '\n'
               '# *.lock - this is used and abused by many editors for many '
               'different things.\n'
               '#    For the main ones I use (e.g. Eclipse), it should be '
               'excluded \n'
               '#    from source-control, but YMMV\n'
               '\n'
               '*.lock\n'
               '\n'
               '#\n'
               '# profile - REMOVED temporarily (on double-checking, this '
               "seems incorrect; I can't find it in OS X docs?)\n"
               '#profile\n'
               '\n'
               '\n'
               '####\n'
               '# Xcode temporary files that should never be committed\n'
               '# \n'
               '# NB: NIB/XIB files still exist even on Storyboard projects, '
               'so we want this...\n'
               '\n'
               '*~.nib\n'
               '\n'
               '\n'
               '####\n'
               '# Xcode build files -\n'
               '#\n'
               '# NB: slash on the end, so we only remove the FOLDER, not any '
               'files that were badly named "DerivedData"\n'
               '\n'
               'DerivedData/\n'
               '\n'
               '# NB: slash on the end, so we only remove the FOLDER, not any '
               'files that were badly named "build"\n'
               '\n'
               'build/\n'
               '\n'),
 Fragment(document_cs='04e64709b061d51fc79e555ed95a4ab21e36ce306dc8ea6b3f080254ea25ca4e',
          id=3,
          lineno=67,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '#####\n'
               '# Xcode private settings (window sizes, bookmarks, '
               'breakpoints, custom executables, smart groups)\n'
               '#\n'
               '# This is complicated:\n'
               '#\n'
               '# SOMETIMES you need to put this file in version control.\n'
               '# Apple designed it poorly - if you use "custom executables", '
               'they are\n'
               '#  saved in this file.\n'
               '# 99% of projects do NOT use those, so they do NOT want to '
               'version control this file.\n'
               "#  ..but if you're in the 1%, comment out the line "
               '"*.pbxuser"\n'
               '\n'
               '# .pbxuser: '
               'http://lists.apple.com/archives/xcode-users/2004/Jan/msg00193.html\n'
               '\n'
               '*.pbxuser\n'
               '\n'
               '# .mode1v3: '
               'http://lists.apple.com/archives/xcode-users/2007/Oct/msg00465.html\n'
               '\n'
               '*.mode1v3\n'
               '\n'
               '# .mode2v3: '
               'http://lists.apple.com/archives/xcode-users/2007/Oct/msg00465.html\n'
               '\n'
               '*.mode2v3\n'
               '\n'
               '# .perspectivev3: '
               'http://stackoverflow.com/questions/5223297/xcode-projects-what-is-a-perspectivev3-file\n'),
 Fragment(document_cs='04e64709b061d51fc79e555ed95a4ab21e36ce306dc8ea6b3f080254ea25ca4e',
          id=4,
          lineno=92,
          tokens=232,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '*.perspectivev3\n'
               '\n'
               '#    NB: also, whitelist the default ones, some projects need '
               'to use these\n'
               '!default.pbxuser\n'
               '!default.mode1v3\n'
               '!default.mode2v3\n'
               '!default.perspectivev3\n'
               '\n'
               '\n'
               '####\n'
               '# Xcode 4 - semi-personal settings\n'
               '#\n'
               '#\n'
               '# OPTION 1: ---------------------------------\n'
               '#     throw away ALL personal settings (including custom '
               'schemes!\n'
               '#     - unless they are "shared")\n'
               '#\n'
               '# NB: this is exclusive with OPTION 2 below\n'
               'xcuserdata\n'
               '\n'
               '# OPTION 2: ---------------------------------\n'
               '#     get rid of ALL personal settings, but KEEP SOME OF THEM\n'
               '#     - NB: you must manually uncomment the bits you want to '
               'keep\n'
               '#\n'
               '# NB: this *requires* git v1.8.2 or above; you may need to '
               'upgrade to latest OS X,\n'
               '#    or manually install git over the top of the OS X version\n'
               '# NB: this is exclusive with OPTION 1 above\n'
               '#\n'
               '#xcuserdata/**/*\n'
               '\n'
               '#     (requires option 2 above): Personal Schemes\n'
               '#\n'
               '#!xcuserdata/**/xcschemes/*\n'),
 Fragment(document_cs='04e64709b061d51fc79e555ed95a4ab21e36ce306dc8ea6b3f080254ea25ca4e',
          id=5,
          lineno=126,
          tokens=236,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '####\n'
               '# XCode 4 workspaces - more detailed\n'
               '#\n'
               '# Workspaces are important! They are a core feature of Xcode - '
               "don't exclude them :)\n"
               '#\n'
               '# Workspace layout is quite spammy. For reference:\n'
               '#\n'
               '# /(root)/\n'
               '#   /(project-name).xcodeproj/\n'
               '#     project.pbxproj\n'
               '#     /project.xcworkspace/\n'
               '#       contents.xcworkspacedata\n'
               '#       /xcuserdata/\n'
               '#         /(your name)/xcuserdatad/\n'
               '#           UserInterfaceState.xcuserstate\n'
               '#     /xcsshareddata/\n'
               '#       /xcschemes/\n'
               '#         (shared scheme name).xcscheme\n'
               '#     /xcuserdata/\n'
               '#       /(your name)/xcuserdatad/\n'
               '#         (private scheme).xcscheme\n'
               '#         xcschememanagement.plist\n'
               '#\n'
               '#\n'
               '\n'
               '####\n'
               '# Xcode 4 - Deprecated classes\n'
               '#\n'
               '# Allegedly, if you manually "deprecate" your classes, they '
               'get moved here.\n'
               '#\n'
               '# We\'re using source-control, so this is a "feature" that we '
               'do not want!\n'
               '\n'
               '*.moved-aside\n'),
 Fragment(document_cs='04e64709b061d51fc79e555ed95a4ab21e36ce306dc8ea6b3f080254ea25ca4e',
          id=6,
          lineno=160,
          tokens=87,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '####\n'
               '# Xcode 5 - VCS file\n'
               '# The data in this file not represent state of your project.\n'
               "# If you'll leave this file in git - you will have merge "
               'conflicts during \n'
               "# pull your cahnges to other's repo\n"
               '#\n'
               '*.xccheckout\n'
               '\n'
               '####\n'
               "# UNKNOWN: recommended by others, but I can't discover what "
               'these files are\n'
               '#\n'
               '# ...none. Everything is now explained.'),
 Fragment(document_cs='04e64709b061d51fc79e555ed95a4ab21e36ce306dc8ea6b3f080254ea25ca4e',
          id=7,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=8,
          lineno=11,
          tokens=158,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='SearchResultsViewController',
          body='class SearchResultsViewController: UIViewController, '
               'UITableViewDataSource, UITableViewDelegate, '
               'APIControllerProtocol {\n'
               '    \n'
               '    @IBOutlet var appsTableView : UITableView?\n'
               '    var albums = [Album]()\n'
               '    var api : APIController?\n'
               '    var imageCache = [String : UIImage]()\n'
               '    let kCellIdentifier: String = "SearchResultCell"\n'
               '    \n'
               '    override func viewDidLoad() {\n'
               '        super.viewDidLoad()\n'
               '        api = APIController(delegate: self)\n'
               '        '
               'UIApplication.sharedApplication().networkActivityIndicatorVisible '
               '= true\n'
               '        api!.searchItunesFor("Beatles")\n'
               '    }\n'
               '\n'
               '    override func didReceiveMemoryWarning() {\n'
               '        super.didReceiveMemoryWarning()\n'
               '        // Dispose of any resources that can be recreated.\n'
               '    }\n'
               '    \n'
               '\n'
               '    // MARK: UITableViewDataSource\n'
               '    \n'
               '    func tableView(tableView: UITableView, '
               'numberOfRowsInSection section: Int) -> Int {\n'
               '        return albums.count\n'
               '    }\n'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=9,
          lineno=37,
          tokens=122,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='SearchResultsViewController',
          body='    \n'
               '    func tableView(tableView: UITableView, '
               'cellForRowAtIndexPath indexPath: NSIndexPath) -> '
               'UITableViewCell {\n'
               '        \n'
               '        let cell: UITableViewCell = '
               'tableView.dequeueReusableCellWithIdentifier(kCellIdentifier) '
               'as UITableViewCell\n'
               '        \n'
               '        let album = self.albums[indexPath.row]\n'
               '        cell.textLabel?.text = album.title\n'
               '        cell.imageView?.image = UIImage(named: "Blank52")\n'
               '        \n'
               '        // Get the formatted price string for display in the '
               'subtitle\n'
               '        let formattedPrice = album.price\n'
               '        \n'
               '        // Grab the artworkUrl60 key to get an image URL for '
               "the app's thumbnail\n"
               '        let urlString = album.thumbnailImageURL\n'
               '        \n'
               '        // Check our image cache f'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=10,
          lineno=52,
          tokens=248,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='SearchResultsViewController',
          body='or the existing key. This is just a dictionary of UIImages\n'
               '        //var image: UIImage? = '
               'self.imageCache.valueForKey(urlString) as? UIImage\n'
               '        var image = self.imageCache[urlString]\n'
               '        \n'
               '        \n'
               '        if( image == nil ) {\n'
               '            // If the image does not exist, we need to '
               'download it\n'
               '            var imgURL: NSURL = NSURL(string: urlString)\n'
               '            \n'
               '            // Download an NSData representation of the image '
               'at the URL\n'
               '            let request: NSURLRequest = NSURLRequest(URL: '
               'imgURL)\n'
               '            NSURLConnection.sendAsynchronousRequest(request, '
               'queue: NSOperationQueue.mainQueue(), completionHandler: '
               '{(response: NSURLResponse!,data: NSData!,error: NSError!) -> '
               'Void in\n'
               '                if error == nil {\n'
               '                    image = UIImage(data: data)\n'
               '                    \n'
               '                    // Store the image in to our cache\n'
               '                    self.imageCache[urlString] = image\n'
               '                    dispatch_async(dispatch_get_main_queue(), '
               '{\n'
               '                        if let cellToUpdate = '
               'tableView.cellForRowAtIndexPath(indexPath) {\n'
               '                            cellToUpdate.imageView?.image = '
               'image\n'
               '                        }\n'
               '                    })\n'
               '                }\n'
               '                else {\n'
               '                    println("Error: '
               '\\(error.localizedDescription)")\n'
               '                }\n'
               '            })\n'
               '            \n'
               '        }\n'
               '        else {\n'
               '            dispatch_async(dispatch_get_main_queue(), {\n'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=11,
          lineno=83,
          tokens=45,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='SearchResultsViewController',
          body='                if let cellToUpdate = '
               'tableView.cellForRowAtIndexPath(indexPath) {\n'
               '                    cellToUpdate.imageView?.image = image\n'
               '                }\n'
               '            })\n'
               '        }\n'
               '        \n'
               '        cell.detailTextLabel?.text = formattedPrice\n'
               '        \n'
               '        return cell\n'
               '    }\n'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=12,
          lineno=93,
          tokens=220,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='SearchResultsViewController',
          body='    \n'
               '    func tableView(tableView: UITableView, willDisplayCell '
               'cell: UITableViewCell, forRowAtIndexPath indexPath: '
               'NSIndexPath) {\n'
               '        cell.layer.transform = '
               'CATransform3DMakeScale(0.1,0.1,1)\n'
               '        UIView.animateWithDuration(0.25, animations: {\n'
               '            cell.layer.transform = '
               'CATransform3DMakeScale(1,1,1)\n'
               '        })\n'
               '    }\n'
               '    \n'
               '    \n'
               '    override func prepareForSegue(segue: UIStoryboardSegue, '
               'sender: AnyObject?) {\n'
               '        var detailsViewController: DetailsViewController = '
               'segue.destinationViewController as DetailsViewController\n'
               '        var albumIndex = '
               'appsTableView!.indexPathForSelectedRow()!.row\n'
               '        var selectedAlbum = self.albums[albumIndex]\n'
               '        detailsViewController.album = selectedAlbum\n'
               '    }\n'
               '    \n'
               '    func didReceiveAPIResults(results: NSDictionary) {\n'
               '        var resultsArr: NSArray = results["results"] as '
               'NSArray\n'
               '        dispatch_async(dispatch_get_main_queue(), {\n'
               '            self.albums = Album.albumsWithJSON(resultsArr)\n'
               '            self.appsTableView!.reloadData()\n'
               '            '
               'UIApplication.sharedApplication().networkActivityIndicatorVisible '
               '= false\n'
               '        })\n'
               '    }\n'
               '\n'
               '}'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=13,
          lineno=19,
          tokens=42,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='viewDidLoad',
          body='override func viewDidLoad() {\n'
               '        super.viewDidLoad()\n'
               '        api = APIController(delegate: self)\n'
               '        '
               'UIApplication.sharedApplication().networkActivityIndicatorVisible '
               '= true\n'
               '        api!.searchItunesFor("Beatles")\n'
               '    }'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=14,
          lineno=26,
          tokens=22,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='didReceiveMemoryWarning',
          body='override func didReceiveMemoryWarning() {\n'
               '        super.didReceiveMemoryWarning()\n'
               '        // Dispose of any resources that can be recreated.\n'
               '    }'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=15,
          lineno=34,
          tokens=21,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tableView',
          body='func tableView(tableView: UITableView, numberOfRowsInSection '
               'section: Int) -> Int {\n'
               '        return albums.count\n'
               '    }'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=16,
          lineno=38,
          tokens=121,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tableView',
          body='func tableView(tableView: UITableView, cellForRowAtIndexPath '
               'indexPath: NSIndexPath) -> UITableViewCell {\n'
               '        \n'
               '        let cell: UITableViewCell = '
               'tableView.dequeueReusableCellWithIdentifier(kCellIdentifier) '
               'as UITableViewCell\n'
               '        \n'
               '        let album = self.albums[indexPath.row]\n'
               '        cell.textLabel?.text = album.title\n'
               '        cell.imageView?.image = UIImage(named: "Blank52")\n'
               '        \n'
               '        // Get the formatted price string for display in the '
               'subtitle\n'
               '        let formattedPrice = album.price\n'
               '        \n'
               '        // Grab the artworkUrl60 key to get an image URL for '
               "the app's thumbnail\n"
               '        let urlString = album.thumbnailImageURL\n'
               '        \n'
               '        // Check our image cache for t'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=17,
          lineno=52,
          tokens=247,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tableView',
          body='he existing key. This is just a dictionary of UIImages\n'
               '        //var image: UIImage? = '
               'self.imageCache.valueForKey(urlString) as? UIImage\n'
               '        var image = self.imageCache[urlString]\n'
               '        \n'
               '        \n'
               '        if( image == nil ) {\n'
               '            // If the image does not exist, we need to '
               'download it\n'
               '            var imgURL: NSURL = NSURL(string: urlString)\n'
               '            \n'
               '            // Download an NSData representation of the image '
               'at the URL\n'
               '            let request: NSURLRequest = NSURLRequest(URL: '
               'imgURL)\n'
               '            NSURLConnection.sendAsynchronousRequest(request, '
               'queue: NSOperationQueue.mainQueue(), completionHandler: '
               '{(response: NSURLResponse!,data: NSData!,error: NSError!) -> '
               'Void in\n'
               '                if error == nil {\n'
               '                    image = UIImage(data: data)\n'
               '                    \n'
               '                    // Store the image in to our cache\n'
               '                    self.imageCache[urlString] = image\n'
               '                    dispatch_async(dispatch_get_main_queue(), '
               '{\n'
               '                        if let cellToUpdate = '
               'tableView.cellForRowAtIndexPath(indexPath) {\n'
               '                            cellToUpdate.imageView?.image = '
               'image\n'
               '                        }\n'
               '                    })\n'
               '                }\n'
               '                else {\n'
               '                    println("Error: '
               '\\(error.localizedDescription)")\n'
               '                }\n'
               '            })\n'
               '            \n'
               '        }\n'
               '        else {\n'
               '            dispatch_async(dispatch_get_main_queue(), {\n'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=18,
          lineno=83,
          tokens=45,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tableView',
          body='                if let cellToUpdate = '
               'tableView.cellForRowAtIndexPath(indexPath) {\n'
               '                    cellToUpdate.imageView?.image = image\n'
               '                }\n'
               '            })\n'
               '        }\n'
               '        \n'
               '        cell.detailTextLabel?.text = formattedPrice\n'
               '        \n'
               '        return cell\n'
               '    }'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=19,
          lineno=94,
          tokens=78,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tableView',
          body='func tableView(tableView: UITableView, willDisplayCell cell: '
               'UITableViewCell, forRowAtIndexPath indexPath: NSIndexPath) {\n'
               '        cell.layer.transform = '
               'CATransform3DMakeScale(0.1,0.1,1)\n'
               '        UIView.animateWithDuration(0.25, animations: {\n'
               '            cell.layer.transform = '
               'CATransform3DMakeScale(1,1,1)\n'
               '        })\n'
               '    }'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=20,
          lineno=102,
          tokens=67,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='prepareForSegue',
          body='override func prepareForSegue(segue: UIStoryboardSegue, '
               'sender: AnyObject?) {\n'
               '        var detailsViewController: DetailsViewController = '
               'segue.destinationViewController as DetailsViewController\n'
               '        var albumIndex = '
               'appsTableView!.indexPathForSelectedRow()!.row\n'
               '        var selectedAlbum = self.albums[albumIndex]\n'
               '        detailsViewController.album = selectedAlbum\n'
               '    }'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=21,
          lineno=109,
          tokens=68,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='didReceiveAPIResults',
          body='func didReceiveAPIResults(results: NSDictionary) {\n'
               '        var resultsArr: NSArray = results["results"] as '
               'NSArray\n'
               '        dispatch_async(dispatch_get_main_queue(), {\n'
               '            self.albums = Album.albumsWithJSON(resultsArr)\n'
               '            self.appsTableView!.reloadData()\n'
               '            '
               'UIApplication.sharedApplication().networkActivityIndicatorVisible '
               '= false\n'
               '        })\n'
               '    }'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=22,
          lineno=13,
          tokens=8,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='appsTableView',
          body='@IBOutlet var appsTableView : UITableView?'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=23,
          lineno=14,
          tokens=6,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='albums',
          body='var albums = [Album]()'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=24,
          lineno=15,
          tokens=6,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='api',
          body='var api : APIController?'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=25,
          lineno=16,
          tokens=9,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='imageCache',
          body='var imageCache = [String : UIImage]()'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=26,
          lineno=17,
          tokens=12,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='kCellIdentifier',
          body='let kCellIdentifier: String = "SearchResultCell"'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=27,
          lineno=40,
          tokens=14,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='cell',
          body='let cell: UITableViewCell = '
               'tableView.dequeueReusableCellWithIdentifier(kCellIdentifier) '
               'as UITableViewCell'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=28,
          lineno=42,
          tokens=9,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='album',
          body='let album = self.albums[indexPath.row]'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=29,
          lineno=47,
          tokens=6,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='formattedPrice',
          body='let formattedPrice = album.price'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=30,
          lineno=50,
          tokens=7,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='urlString',
          body='let urlString = album.thumbnailImageURL'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=31,
          lineno=54,
          tokens=9,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='image',
          body='var image = self.imageCache[urlString]'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=32,
          lineno=59,
          tokens=11,
          depth=7,
          parent_id=None,
          category='property',
          summary=False,
          name='imgURL',
          body='var imgURL: NSURL = NSURL(string: urlString)'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=33,
          lineno=62,
          tokens=13,
          depth=7,
          parent_id=None,
          category='property',
          summary=False,
          name='request',
          body='let request: NSURLRequest = NSURLRequest(URL: imgURL)'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=34,
          lineno=103,
          tokens=13,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='detailsViewController',
          body='var detailsViewController: DetailsViewController = '
               'segue.destinationViewController as DetailsViewController'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=35,
          lineno=104,
          tokens=14,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='albumIndex',
          body='var albumIndex = appsTableView!.indexPathForSelectedRow()!.row'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=36,
          lineno=105,
          tokens=11,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='selectedAlbum',
          body='var selectedAlbum = self.albums[albumIndex]'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=37,
          lineno=110,
          tokens=12,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='resultsArr',
          body='var resultsArr: NSArray = results["results"] as NSArray'),
 Fragment(document_cs='15888f39a7be1ce8b7408bc5e23fb7bead75eb1b1f13196f38850143c62b280e',
          id=38,
          lineno=1,
          tokens=60,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: SearchResultsViewController\n'
               '  Functions: didReceiveAPIResults didReceiveMemoryWarning '
               'prepareForSegue tableView viewDidLoad\n'
               '  Properties: album albumIndex albums api appsTableView cell '
               'detailsViewController formattedPrice image imageCache imgURL '
               'kCellIdentifier request resultsArr selectedAlbum urlString\n'
               '  Usages: formattedPrice image selectedAlbum\n'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=39,
          lineno=12,
          tokens=201,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='DetailsViewController',
          body='class DetailsViewController: UIViewController, '
               'APIControllerProtocol, UITableViewDelegate, '
               'UITableViewDataSource {\n'
               '    \n'
               '    var album: Album?\n'
               '    var tracks = [Track]()\n'
               '    \n'
               '    @IBOutlet weak var titleLabel: UILabel!\n'
               '    @IBOutlet weak var albumCover: UIImageView!\n'
               '    @IBOutlet weak var tracksTableView: UITableView!\n'
               '    lazy var api : APIController = APIController(delegate: '
               'self)\n'
               '    var mediaPlayer: MPMoviePlayerController = '
               'MPMoviePlayerController()\n'
               '    \n'
               '    required init(coder aDecoder: NSCoder) {\n'
               '        super.init(coder: aDecoder)\n'
               '    }\n'
               '    \n'
               '    override func viewDidLoad() {\n'
               '        super.viewDidLoad()\n'
               '        titleLabel.text = self.album?.title\n'
               '        albumCover.image = UIImage(data: NSData(contentsOfURL: '
               'NSURL(string: self.album!.largeImageURL)))\n'
               '        \n'
               '        if self.album != nil {\n'
               '            api.lookupAlbum(self.album!.collectionId)\n'
               '        }\n'
               '    }\n'
               '    \n'
               '    // MARK: UITableViewDataSource\n'
               '    func tableView(tableView: UITableView, '
               'numberOfRowsInSection section: Int) -> Int {\n'
               '        return tracks.count\n'
               '    }\n'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=40,
          lineno=41,
          tokens=227,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='DetailsViewController',
          body='\n'
               '    func tableView(tableView: UITableView, '
               'cellForRowAtIndexPath indexPath: NSIndexPath) -> '
               'UITableViewCell {\n'
               '        let cell = '
               'tableView.dequeueReusableCellWithIdentifier("TrackCell") as '
               'TrackCell\n'
               '        let track = tracks[indexPath.row]\n'
               '        cell.titleLabel.text = track.title\n'
               '        cell.playIcon.text = "▶️"\n'
               '        \n'
               '        return cell\n'
               '    }\n'
               '    \n'
               '    func tableView(tableView: UITableView, '
               'didSelectRowAtIndexPath indexPath: NSIndexPath) {\n'
               '        var track = tracks[indexPath.row]\n'
               '        mediaPlayer.stop()\n'
               '        mediaPlayer.contentURL = NSURL(string: '
               'track.previewUrl)\n'
               '        mediaPlayer.play()\n'
               '        if let cell = '
               'tableView.cellForRowAtIndexPath(indexPath) as? TrackCell {\n'
               '            cell.playIcon.text = "◾️"\n'
               '        }\n'
               '    }\n'
               '    \n'
               '    func tableView(tableView: UITableView, willDisplayCell '
               'cell: UITableViewCell, forRowAtIndexPath indexPath: '
               'NSIndexPath) {\n'
               '        cell.layer.transform = '
               'CATransform3DMakeScale(0.1,0.1,1)\n'
               '        UIView.animateWithDuration(0.25, animations: {\n'
               '            cell.layer.transform = '
               'CATransform3DMakeScale(1,1,1)\n'
               '        })\n'
               '    }\n'
               '    \n'
               '    // MARK: APIControllerProtocol\n'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=41,
          lineno=69,
          tokens=68,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='DetailsViewController',
          body='    func didReceiveAPIResults(results: NSDictionary) {\n'
               '        var resultsArr: NSArray = results["results"] as '
               'NSArray\n'
               '        dispatch_async(dispatch_get_main_queue(), {\n'
               '            self.tracks = Track.tracksWithJSON(resultsArr)\n'
               '            self.tracksTableView.reloadData()\n'
               '            '
               'UIApplication.sharedApplication().networkActivityIndicatorVisible '
               '= false\n'
               '        })\n'
               '    }\n'
               '    \n'
               '}'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=42,
          lineno=27,
          tokens=63,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='viewDidLoad',
          body='override func viewDidLoad() {\n'
               '        super.viewDidLoad()\n'
               '        titleLabel.text = self.album?.title\n'
               '        albumCover.image = UIImage(data: NSData(contentsOfURL: '
               'NSURL(string: self.album!.largeImageURL)))\n'
               '        \n'
               '        if self.album != nil {\n'
               '            api.lookupAlbum(self.album!.collectionId)\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=43,
          lineno=38,
          tokens=21,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tableView',
          body='func tableView(tableView: UITableView, numberOfRowsInSection '
               'section: Int) -> Int {\n'
               '        return tracks.count\n'
               '    }'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=44,
          lineno=42,
          tokens=63,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tableView',
          body='func tableView(tableView: UITableView, cellForRowAtIndexPath '
               'indexPath: NSIndexPath) -> UITableViewCell {\n'
               '        let cell = '
               'tableView.dequeueReusableCellWithIdentifier("TrackCell") as '
               'TrackCell\n'
               '        let track = tracks[indexPath.row]\n'
               '        cell.titleLabel.text = track.title\n'
               '        cell.playIcon.text = "▶️"\n'
               '        \n'
               '        return cell\n'
               '    }'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=45,
          lineno=51,
          tokens=71,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tableView',
          body='func tableView(tableView: UITableView, didSelectRowAtIndexPath '
               'indexPath: NSIndexPath) {\n'
               '        var track = tracks[indexPath.row]\n'
               '        mediaPlayer.stop()\n'
               '        mediaPlayer.contentURL = NSURL(string: '
               'track.previewUrl)\n'
               '        mediaPlayer.play()\n'
               '        if let cell = '
               'tableView.cellForRowAtIndexPath(indexPath) as? TrackCell {\n'
               '            cell.playIcon.text = "◾️"\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=46,
          lineno=61,
          tokens=78,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tableView',
          body='func tableView(tableView: UITableView, willDisplayCell cell: '
               'UITableViewCell, forRowAtIndexPath indexPath: NSIndexPath) {\n'
               '        cell.layer.transform = '
               'CATransform3DMakeScale(0.1,0.1,1)\n'
               '        UIView.animateWithDuration(0.25, animations: {\n'
               '            cell.layer.transform = '
               'CATransform3DMakeScale(1,1,1)\n'
               '        })\n'
               '    }'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=47,
          lineno=69,
          tokens=65,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='didReceiveAPIResults',
          body='func didReceiveAPIResults(results: NSDictionary) {\n'
               '        var resultsArr: NSArray = results["results"] as '
               'NSArray\n'
               '        dispatch_async(dispatch_get_main_queue(), {\n'
               '            self.tracks = Track.tracksWithJSON(resultsArr)\n'
               '            self.tracksTableView.reloadData()\n'
               '            '
               'UIApplication.sharedApplication().networkActivityIndicatorVisible '
               '= false\n'
               '        })\n'
               '    }'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=48,
          lineno=14,
          tokens=5,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='album',
          body='var album: Album?'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=49,
          lineno=15,
          tokens=6,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='tracks',
          body='var tracks = [Track]()'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=50,
          lineno=17,
          tokens=8,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='titleLabel',
          body='@IBOutlet weak var titleLabel: UILabel!'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=51,
          lineno=18,
          tokens=9,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='albumCover',
          body='@IBOutlet weak var albumCover: UIImageView!'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=52,
          lineno=19,
          tokens=9,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='tracksTableView',
          body='@IBOutlet weak var tracksTableView: UITableView!'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=53,
          lineno=20,
          tokens=13,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='api',
          body='lazy var api : APIController = APIController(delegate: self)'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=54,
          lineno=21,
          tokens=15,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='mediaPlayer',
          body='var mediaPlayer: MPMoviePlayerController = '
               'MPMoviePlayerController()'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=55,
          lineno=43,
          tokens=13,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='cell',
          body='let cell = '
               'tableView.dequeueReusableCellWithIdentifier("TrackCell") as '
               'TrackCell'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=56,
          lineno=44,
          tokens=7,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='track',
          body='let track = tracks[indexPath.row]'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=57,
          lineno=52,
          tokens=7,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='track',
          body='var track = tracks[indexPath.row]'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=58,
          lineno=70,
          tokens=12,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='resultsArr',
          body='var resultsArr: NSArray = results["results"] as NSArray'),
 Fragment(document_cs='1e437c5cd3a9f31622051e85c7bd36922374575ff58ca1f08dda36ce8a51b0e6',
          id=59,
          lineno=1,
          tokens=33,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: DetailsViewController\n'
               '  Functions: didReceiveAPIResults tableView viewDidLoad\n'
               '  Properties: album albumCover api cell mediaPlayer resultsArr '
               'titleLabel track tracks tracksTableView\n'),
 Fragment(document_cs='1ef5ead2d292a3f4a042b72bc95fbf58526527dd3165d21526e84b321467fa08',
          id=60,
          lineno=11,
          tokens=79,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='TrackCell',
          body='class TrackCell: UITableViewCell {\n'
               '\n'
               '    @IBOutlet weak var playIcon: UILabel!\n'
               '    @IBOutlet weak var titleLabel: UILabel!\n'
               '    \n'
               '    override func awakeFromNib() {\n'
               '        super.awakeFromNib()\n'
               '        // Initialization code\n'
               '    }\n'
               '\n'
               '    override func setSelected(selected: Bool, animated: Bool) '
               '{\n'
               '        super.setSelected(selected, animated: animated)\n'
               '\n'
               '        // Configure the view for the selected state\n'
               '    }\n'
               '\n'
               '}'),
 Fragment(document_cs='1ef5ead2d292a3f4a042b72bc95fbf58526527dd3165d21526e84b321467fa08',
          id=61,
          lineno=16,
          tokens=17,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='awakeFromNib',
          body='override func awakeFromNib() {\n'
               '        super.awakeFromNib()\n'
               '        // Initialization code\n'
               '    }'),
 Fragment(document_cs='1ef5ead2d292a3f4a042b72bc95fbf58526527dd3165d21526e84b321467fa08',
          id=62,
          lineno=21,
          tokens=33,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='setSelected',
          body='override func setSelected(selected: Bool, animated: Bool) {\n'
               '        super.setSelected(selected, animated: animated)\n'
               '\n'
               '        // Configure the view for the selected state\n'
               '    }'),
 Fragment(document_cs='1ef5ead2d292a3f4a042b72bc95fbf58526527dd3165d21526e84b321467fa08',
          id=63,
          lineno=13,
          tokens=9,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='playIcon',
          body='@IBOutlet weak var playIcon: UILabel!'),
 Fragment(document_cs='1ef5ead2d292a3f4a042b72bc95fbf58526527dd3165d21526e84b321467fa08',
          id=64,
          lineno=14,
          tokens=8,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='titleLabel',
          body='@IBOutlet weak var titleLabel: UILabel!'),
 Fragment(document_cs='1ef5ead2d292a3f4a042b72bc95fbf58526527dd3165d21526e84b321467fa08',
          id=65,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: TrackCell\n'
               '  Functions: awakeFromNib setSelected\n'
               '  Properties: playIcon titleLabel\n'),
 Fragment(document_cs='a7673648074a23a9ad44d1f07731e82ee95048f4aa4072c96e3d243483ad06d7',
          id=66,
          lineno=12,
          tokens=152,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='MusicPlayerTests',
          body='class MusicPlayerTests: XCTestCase {\n'
               '    \n'
               '    override func setUp() {\n'
               '        super.setUp()\n'
               '        // Put setup code here. This method is called before '
               'the invocation of each test method in the class.\n'
               '    }\n'
               '    \n'
               '    override func tearDown() {\n'
               '        // Put teardown code here. This method is called after '
               'the invocation of each test method in the class.\n'
               '        super.tearDown()\n'
               '    }\n'
               '    \n'
               '    func testExample() {\n'
               '        // This is an example of a functional test case.\n'
               '        XCTAssert(true, "Pass")\n'
               '    }\n'
               '    \n'
               '    func testPerformanceExample() {\n'
               '        // This is an example of a performance test case.\n'
               '        self.measureBlock() {\n'
               '            // Put the code you want to measure the time of '
               'here.\n'
               '        }\n'
               '    }\n'
               '    \n'
               '}'),
 Fragment(document_cs='a7673648074a23a9ad44d1f07731e82ee95048f4aa4072c96e3d243483ad06d7',
          id=67,
          lineno=14,
          tokens=33,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='setUp',
          body='override func setUp() {\n'
               '        super.setUp()\n'
               '        // Put setup code here. This method is called before '
               'the invocation of each test method in the class.\n'
               '    }'),
 Fragment(document_cs='a7673648074a23a9ad44d1f07731e82ee95048f4aa4072c96e3d243483ad06d7',
          id=68,
          lineno=19,
          tokens=34,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tearDown',
          body='override func tearDown() {\n'
               '        // Put teardown code here. This method is called after '
               'the invocation of each test method in the class.\n'
               '        super.tearDown()\n'
               '    }'),
 Fragment(document_cs='a7673648074a23a9ad44d1f07731e82ee95048f4aa4072c96e3d243483ad06d7',
          id=69,
          lineno=24,
          tokens=26,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='testExample',
          body='func testExample() {\n'
               '        // This is an example of a functional test case.\n'
               '        XCTAssert(true, "Pass")\n'
               '    }'),
 Fragment(document_cs='a7673648074a23a9ad44d1f07731e82ee95048f4aa4072c96e3d243483ad06d7',
          id=70,
          lineno=29,
          tokens=42,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='testPerformanceExample',
          body='func testPerformanceExample() {\n'
               '        // This is an example of a performance test case.\n'
               '        self.measureBlock() {\n'
               '            // Put the code you want to measure the time of '
               'here.\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='a7673648074a23a9ad44d1f07731e82ee95048f4aa4072c96e3d243483ad06d7',
          id=71,
          lineno=1,
          tokens=18,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: MusicPlayerTests\n'
               '  Functions: setUp tearDown testExample '
               'testPerformanceExample\n'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=72,
          lineno=10,
          tokens=69,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Track',
          body='class Track {\n'
               '    \n'
               '    var title: String\n'
               '    var price: String\n'
               '    var previewUrl: String\n'
               '    var tracks = [Track]()\n'
               '    \n'
               '    init(title: String, price: String, previewUrl: String) {\n'
               '        self.title = title\n'
               '        self.price = price\n'
               '        self.previewUrl = previewUrl\n'
               '    }\n'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=73,
          lineno=22,
          tokens=224,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Track',
          body='    \n'
               '    class func tracksWithJSON(allResults: NSArray) -> [Track] '
               '{\n'
               '        \n'
               '        var tracks = [Track]()\n'
               '        \n'
               '        if allResults.count>0 {\n'
               '            for trackInfo in allResults {\n'
               '                // Create the track\n'
               '                if let kind = trackInfo["kind"] as? String {\n'
               '                    if kind=="song" {\n'
               '                        \n'
               '                        var trackPrice = '
               'trackInfo["trackPrice"] as? String\n'
               '                        var trackTitle = '
               'trackInfo["trackName"] as? String\n'
               '                        var trackPreviewUrl = '
               'trackInfo["previewUrl"] as? String\n'
               '                        \n'
               '                        if(trackTitle == nil) {\n'
               '                            trackTitle = "Unknown"\n'
               '                        }\n'
               '                        else if(trackPrice == nil) {\n'
               '                            println("No trackPrice in '
               '\\(trackInfo)")\n'
               '                            trackPrice = "?"\n'
               '                        }\n'
               '                        else if(trackPreviewUrl == nil) {\n'
               '                            trackPreviewUrl = ""\n'
               '                        }\n'
               '                        \n'
               '                        var track = Track(title: trackTitle!, '
               'price: trackPrice!, previewUrl: trackPreviewUrl!)\n'
               '                        tracks.append(track)\n'
               '                        \n'
               '                    }\n'
               '                }\n'
               '            }\n'
               '        }\n'
               '        return tracks\n'
               '    }\n'
               '    \n'
               '}'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=74,
          lineno=23,
          tokens=220,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='tracksWithJSON',
          body='class func tracksWithJSON(allResults: NSArray) -> [Track] {\n'
               '        \n'
               '        var tracks = [Track]()\n'
               '        \n'
               '        if allResults.count>0 {\n'
               '            for trackInfo in allResults {\n'
               '                // Create the track\n'
               '                if let kind = trackInfo["kind"] as? String {\n'
               '                    if kind=="song" {\n'
               '                        \n'
               '                        var trackPrice = '
               'trackInfo["trackPrice"] as? String\n'
               '                        var trackTitle = '
               'trackInfo["trackName"] as? String\n'
               '                        var trackPreviewUrl = '
               'trackInfo["previewUrl"] as? String\n'
               '                        \n'
               '                        if(trackTitle == nil) {\n'
               '                            trackTitle = "Unknown"\n'
               '                        }\n'
               '                        else if(trackPrice == nil) {\n'
               '                            println("No trackPrice in '
               '\\(trackInfo)")\n'
               '                            trackPrice = "?"\n'
               '                        }\n'
               '                        else if(trackPreviewUrl == nil) {\n'
               '                            trackPreviewUrl = ""\n'
               '                        }\n'
               '                        \n'
               '                        var track = Track(title: trackTitle!, '
               'price: trackPrice!, previewUrl: trackPreviewUrl!)\n'
               '                        tracks.append(track)\n'
               '                        \n'
               '                    }\n'
               '                }\n'
               '            }\n'
               '        }\n'
               '        return tracks\n'
               '    }'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=75,
          lineno=12,
          tokens=4,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='title',
          body='var title: String'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=76,
          lineno=13,
          tokens=4,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='price',
          body='var price: String'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=77,
          lineno=14,
          tokens=5,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='previewUrl',
          body='var previewUrl: String'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=78,
          lineno=15,
          tokens=6,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='tracks',
          body='var tracks = [Track]()'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=79,
          lineno=25,
          tokens=6,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='tracks',
          body='var tracks = [Track]()'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=80,
          lineno=33,
          tokens=13,
          depth=13,
          parent_id=None,
          category='property',
          summary=False,
          name='trackPrice',
          body='var trackPrice = trackInfo["trackPrice"] as? String'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=81,
          lineno=34,
          tokens=13,
          depth=13,
          parent_id=None,
          category='property',
          summary=False,
          name='trackTitle',
          body='var trackTitle = trackInfo["trackName"] as? String'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=82,
          lineno=35,
          tokens=14,
          depth=13,
          parent_id=None,
          category='property',
          summary=False,
          name='trackPreviewUrl',
          body='var trackPreviewUrl = trackInfo["previewUrl"] as? String'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=83,
          lineno=48,
          tokens=21,
          depth=13,
          parent_id=None,
          category='property',
          summary=False,
          name='track',
          body='var track = Track(title: trackTitle!, price: trackPrice!, '
               'previewUrl: trackPreviewUrl!)'),
 Fragment(document_cs='abf895ab23d5a5f74f1f6caf237e80276d74a5cf29e66aeebad7cc986c940d18',
          id=84,
          lineno=1,
          tokens=38,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Track\n'
               '  Functions: tracksWithJSON\n'
               '  Properties: previewUrl price title track trackPreviewUrl '
               'trackPrice trackTitle tracks\n'
               '  Usages: previewUrl price title\n'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=85,
          lineno=11,
          tokens=231,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Album',
          body='class Album {\n'
               '    var title: String\n'
               '    var price: String\n'
               '    var thumbnailImageURL: String\n'
               '    var largeImageURL: String\n'
               '    var itemURL: String\n'
               '    var artistURL: String\n'
               '    var collectionId: Int\n'
               '    \n'
               '    init(name: String, price: String, thumbnailImageURL: '
               'String, largeImageURL: String, itemURL: String, artistURL: '
               'String, collectionId: Int)  {\n'
               '        self.title = name\n'
               '        self.price = price\n'
               '        self.thumbnailImageURL = thumbnailImageURL\n'
               '        self.largeImageURL = largeImageURL\n'
               '        self.itemURL = itemURL\n'
               '        self.artistURL = artistURL\n'
               '        self.collectionId = collectionId\n'
               '    }\n'
               '    \n'
               '    class func albumsWithJSON(allResults: NSArray) -> [Album] '
               '{\n'
               '        \n'
               '        // Create an empty array of Albums to append to from '
               'this list\n'
               '        var albums = [Album]()\n'
               '        \n'
               '        // Store the results in our table data array\n'
               '        if allResults.count>0 {\n'
               '            \n'
               '            // Sometimes iTunes returns a collection, not a '
               "track, so we check both for the 'name'\n"),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=86,
          lineno=39,
          tokens=235,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Album',
          body='            for result in allResults {\n'
               '                \n'
               '                var name = result["trackName"] as? String\n'
               '                if name == nil {\n'
               '                    name = result["collectionName"] as? '
               'String\n'
               '                }\n'
               '                \n'
               '                // Sometimes price comes in as formattedPrice, '
               "sometimes as collectionPrice.. and sometimes it's a float "
               'instead of a string. Hooray!\n'
               '                var price = result["formattedPrice"] as? '
               'String\n'
               '                if price == nil {\n'
               '                    price = result["collectionPrice"] as? '
               'String\n'
               '                    if price == nil {\n'
               '                        var priceFloat: Float? = '
               'result["collectionPrice"] as? Float\n'
               '                        var nf: NSNumberFormatter = '
               'NSNumberFormatter()\n'
               '                        nf.maximumFractionDigits = 2\n'
               '                        if priceFloat != nil {\n'
               '                            price = '
               '"$"+nf.stringFromNumber(priceFloat!)\n'
               '                        }\n'
               '                    }\n'
               '                }\n'
               '                \n'
               '                let thumbnailURL = result["artworkUrl60"] as? '
               'String ?? ""\n'
               '                let imageURL = result["artworkUrl100"] as? '
               'String ?? ""\n'
               '                let artistURL = result["artistViewUrl"] as? '
               'String ?? ""\n'
               '                \n'
               '                var itemURL = result["collectionViewUrl"] as? '
               'String\n'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=87,
          lineno=65,
          tokens=102,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='Album',
          body='                if itemURL == nil {\n'
               '                    itemURL = result["trackViewUrl"] as? '
               'String\n'
               '                }\n'
               '                \n'
               '                var collectionId = result["collectionId"] as? '
               'Int\n'
               '                \n'
               '                var newAlbum = Album(name: name!, price: '
               'price!, thumbnailImageURL: thumbnailURL, largeImageURL: '
               'imageURL, itemURL: itemURL!, artistURL: artistURL, '
               'collectionId: collectionId!)\n'
               '                albums.append(newAlbum)\n'
               '                \n'
               '            }\n'
               '        }\n'
               '        return albums\n'
               '    }\n'
               '    \n'
               '}'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=88,
          lineno=30,
          tokens=225,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='albumsWithJSON',
          body='class func albumsWithJSON(allResults: NSArray) -> [Album] {\n'
               '        \n'
               '        // Create an empty array of Albums to append to from '
               'this list\n'
               '        var albums = [Album]()\n'
               '        \n'
               '        // Store the results in our table data array\n'
               '        if allResults.count>0 {\n'
               '            \n'
               '            // Sometimes iTunes returns a collection, not a '
               "track, so we check both for the 'name'\n"
               '            for result in allResults {\n'
               '                \n'
               '                var name = result["trackName"] as? String\n'
               '                if name == nil {\n'
               '                    name = result["collectionName"] as? '
               'String\n'
               '                }\n'
               '                \n'
               '                // Sometimes price comes in as formattedPrice, '
               "sometimes as collectionPrice.. and sometimes it's a float "
               'instead of a string. Hooray!\n'
               '                var price = result["formattedPrice"] as? '
               'String\n'
               '                if price == nil {\n'
               '                    price = result["collectionPrice"] as? '
               'String\n'
               '                    if price == nil {\n'
               '                        var priceFloat: Float? = '
               'result["collectionPrice"] as? Float\n'
               '                        var nf: NSNumberFormatter = '
               'NSNumberFormatter()\n'
               '                        nf.maximumFractionDigits = 2\n'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=89,
          lineno=54,
          tokens=190,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='albumsWithJSON',
          body='                        if priceFloat != nil {\n'
               '                            price = '
               '"$"+nf.stringFromNumber(priceFloat!)\n'
               '                        }\n'
               '                    }\n'
               '                }\n'
               '                \n'
               '                let thumbnailURL = result["artworkUrl60"] as? '
               'String ?? ""\n'
               '                let imageURL = result["artworkUrl100"] as? '
               'String ?? ""\n'
               '                let artistURL = result["artistViewUrl"] as? '
               'String ?? ""\n'
               '                \n'
               '                var itemURL = result["collectionViewUrl"] as? '
               'String\n'
               '                if itemURL == nil {\n'
               '                    itemURL = result["trackViewUrl"] as? '
               'String\n'
               '                }\n'
               '                \n'
               '                var collectionId = result["collectionId"] as? '
               'Int\n'
               '                \n'
               '                var newAlbum = Album(name: name!, price: '
               'price!, thumbnailImageURL: thumbnailURL, largeImageURL: '
               'imageURL, itemURL: itemURL!, artistURL: artistURL, '
               'collectionId: collectionId!)\n'
               '                albums.append(newAlbum)\n'
               '                \n'
               '            }\n'
               '        }\n'
               '        return albums\n'
               '    }'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=90,
          lineno=12,
          tokens=4,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='title',
          body='var title: String'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=91,
          lineno=13,
          tokens=4,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='price',
          body='var price: String'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=92,
          lineno=14,
          tokens=6,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='thumbnailImageURL',
          body='var thumbnailImageURL: String'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=93,
          lineno=15,
          tokens=6,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='largeImageURL',
          body='var largeImageURL: String'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=94,
          lineno=16,
          tokens=5,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='itemURL',
          body='var itemURL: String'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=95,
          lineno=17,
          tokens=20,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='artistURL',
          body='var artistURL: Stringlet artistURL = result["artistViewUrl"] '
               'as? String ?? ""'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=96,
          lineno=18,
          tokens=5,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='collectionId',
          body='var collectionId: Int'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=97,
          lineno=33,
          tokens=6,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='albums',
          body='var albums = [Album]()'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=98,
          lineno=41,
          tokens=11,
          depth=9,
          parent_id=None,
          category='property',
          summary=False,
          name='name',
          body='var name = result["trackName"] as? String'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=99,
          lineno=47,
          tokens=11,
          depth=9,
          parent_id=None,
          category='property',
          summary=False,
          name='price',
          body='var price = result["formattedPrice"] as? String'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=100,
          lineno=51,
          tokens=15,
          depth=13,
          parent_id=None,
          category='property',
          summary=False,
          name='priceFloat',
          body='var priceFloat: Float? = result["collectionPrice"] as? Float'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=101,
          lineno=60,
          tokens=16,
          depth=9,
          parent_id=None,
          category='property',
          summary=False,
          name='thumbnailURL',
          body='let thumbnailURL = result["artworkUrl60"] as? String ?? ""'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=102,
          lineno=61,
          tokens=15,
          depth=9,
          parent_id=None,
          category='property',
          summary=False,
          name='imageURL',
          body='let imageURL = result["artworkUrl100"] as? String ?? ""'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=103,
          lineno=64,
          tokens=12,
          depth=9,
          parent_id=None,
          category='property',
          summary=False,
          name='itemURL',
          body='var itemURL = result["collectionViewUrl"] as? String'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=104,
          lineno=69,
          tokens=12,
          depth=9,
          parent_id=None,
          category='property',
          summary=False,
          name='collectionId',
          body='var collectionId = result["collectionId"] as? Int'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=105,
          lineno=71,
          tokens=44,
          depth=9,
          parent_id=None,
          category='property',
          summary=False,
          name='newAlbum',
          body='var newAlbum = Album(name: name!, price: price!, '
               'thumbnailImageURL: thumbnailURL, largeImageURL: imageURL, '
               'itemURL: itemURL!, artistURL: artistURL, collectionId: '
               'collectionId!)'),
 Fragment(document_cs='b4766ef57ae6f5fb83f7a3c3d8d52504ced39d1acc35193a3fdd6ccf2a46c257',
          id=106,
          lineno=1,
          tokens=58,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: Album\n'
               '  Functions: albumsWithJSON\n'
               '  Properties: albums artistURL collectionId imageURL itemURL '
               'largeImageURL name newAlbum price priceFloat thumbnailImageURL '
               'thumbnailURL title\n'
               '  Usages: artistURL collectionId itemURL largeImageURL name '
               'price thumbnailImageURL\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=107,
          lineno=1,
          tokens=215,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// !$*UTF8*$!\n'
               '{\n'
               '\tarchiveVersion = 1;\n'
               '\tclasses = {\n'
               '\t};\n'
               '\tobjectVersion = 46;\n'
               '\tobjects = {\n'
               '\n'
               '/* Begin PBXBuildFile section */\n'
               '\t\t0270480919C8E08B00FDA1C5 /* AppDelegate.swift in Sources '
               '*/ = {isa = PBXBuildFile; fileRef = 0270480819C8E08B00FDA1C5 '
               '/* AppDelegate.swift */; };\n'
               '\t\t0270480B19C8E08B00FDA1C5 /* '
               'SearchResultsViewController.swift in Sources */ = {isa = '
               'PBXBuildFile; fileRef = 0270480A19C8E08B00FDA1C5 /* '
               'SearchResultsViewController.swift */; };\n'
               '\t\t0270480E19C8E08B00FDA1C5 /* Main.storyboard in Resources '
               '*/ = {isa = PBXBuildFile; fileRef = 0270480C19C8E08B00FDA1C5 '
               '/* Main.storyboard */; };\n'
               '\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=108,
          lineno=13,
          tokens=236,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='0270481019C8E08B00FDA1C5 /* Images.xcassets in Resources */ = '
               '{isa = PBXBuildFile; fileRef = 0270480F19C8E08B00FDA1C5 /* '
               'Images.xcassets */; };\n'
               '\t\t0270481319C8E08B00FDA1C5 /* LaunchScreen.xib in Resources '
               '*/ = {isa = PBXBuildFile; fileRef = 0270481119C8E08B00FDA1C5 '
               '/* LaunchScreen.xib */; };\n'
               '\t\t0270481F19C8E08B00FDA1C5 /* MusicPlayerTests.swift in '
               'Sources */ = {isa = PBXBuildFile; fileRef = '
               '0270481E19C8E08B00FDA1C5 /* MusicPlayerTests.swift */; };\n'
               '\t\t0270482919C8E2E700FDA1C5 /* APIController.swift in Sources '
               '*/ = {isa = PBXBuildFile; fileRef = 0270482819C8E2E700FDA1C5 '
               '/* APIController.swift */; };\n'
               '\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=109,
          lineno=17,
          tokens=223,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='0270482B19C8EC3000FDA1C5 /* Blank52.png in Resources */ = {isa '
               '= PBXBuildFile; fileRef = 0270482A19C8EC3000FDA1C5 /* '
               'Blank52.png */; };\n'
               '\t\t0270482D19C8F35700FDA1C5 /* Album.swift in Sources */ = '
               '{isa = PBXBuildFile; fileRef = 0270482C19C8F35700FDA1C5 /* '
               'Album.swift */; };\n'
               '\t\t0270482F19C8F43500FDA1C5 /* DetailsViewController.swift in '
               'Sources */ = {isa = PBXBuildFile; fileRef = '
               '0270482E19C8F43500FDA1C5 /* DetailsViewController.swift */; '
               '};\n'
               '\t\t0270483119C8F6D000FDA1C5 /* Track.swift in Sources */ = '
               '{isa = PBXBuildFile; fileRef = 0270483019C8F6D000FDA1C5 /* '
               'Track.swift */; };\n'
               '\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=110,
          lineno=21,
          tokens=61,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='0270483519C8F80000FDA1C5 /* TrackCell.swift in Sources */ = '
               '{isa = PBXBuildFile; fileRef = 0270483419C8F80000FDA1C5 /* '
               'TrackCell.swift */; };\n'
               '/* End PBXBuildFile section */\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=111,
          lineno=23,
          tokens=235,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '/* Begin PBXContainerItemProxy section */\n'
               '\t\t0270481919C8E08B00FDA1C5 /* PBXContainerItemProxy */ = {\n'
               '\t\t\tisa = PBXContainerItemProxy;\n'
               '\t\t\tcontainerPortal = 027047FB19C8E08B00FDA1C5 /* Project '
               'object */;\n'
               '\t\t\tproxyType = 1;\n'
               '\t\t\tremoteGlobalIDString = 0270480219C8E08B00FDA1C5;\n'
               '\t\t\tremoteInfo = MusicPlayer;\n'
               '\t\t};\n'
               '/* End PBXContainerItemProxy section */\n'
               '\n'
               '/* Begin PBXFileReference section */\n'
               '\t\t0270480319C8E08B00FDA1C5 /* MusicPlayer.app */ = {isa = '
               'PBXFileReference; explicitFileType = wrapper.application; '
               'includeInIndex = 0; path = MusicPlayer.app; sourceTree = '
               'BUILT_PRODUCTS_DIR; };\n'
               '\t\t0270480719C8E08B00FDA1C5 /* Info.plist */ = {isa = '
               'PBXFileReference; lastKnownFileType = text.plist.xml; path = '
               'Info.plist; sourceTree = "<group>"; };\n'
               '\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=112,
          lineno=37,
          tokens=213,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='0270480819C8E08B00FDA1C5 /* AppDelegate.swift */ = {isa = '
               'PBXFileReference; lastKnownFileType = sourcecode.swift; path = '
               'AppDelegate.swift; sourceTree = "<group>"; };\n'
               '\t\t0270480A19C8E08B00FDA1C5 /* '
               'SearchResultsViewController.swift */ = {isa = '
               'PBXFileReference; lastKnownFileType = sourcecode.swift; path = '
               'SearchResultsViewController.swift; sourceTree = "<group>"; };\n'
               '\t\t0270480D19C8E08B00FDA1C5 /* Base */ = {isa = '
               'PBXFileReference; lastKnownFileType = file.storyboard; name = '
               'Base; path = Base.lproj/Main.storyboard; sourceTree = '
               '"<group>"; };\n'
               '\t\t0270480F19C8E08B00FDA1C5 /* Images.xcassets */ = {isa = '
               'PBXFileReference; lastKnownFileType = folder.assetcatalog; '
               'path = Images.xcassets; sourceTree = "<group>"; };\n'
               '\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=113,
          lineno=41,
          tokens=225,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='0270481219C8E08B00FDA1C5 /* Base */ = {isa = PBXFileReference; '
               'lastKnownFileType = file.xib; name = Base; path = '
               'Base.lproj/LaunchScreen.xib; sourceTree = "<group>"; };\n'
               '\t\t0270481819C8E08B00FDA1C5 /* MusicPlayerTests.xctest */ = '
               '{isa = PBXFileReference; explicitFileType = wrapper.cfbundle; '
               'includeInIndex = 0; path = MusicPlayerTests.xctest; sourceTree '
               '= BUILT_PRODUCTS_DIR; };\n'
               '\t\t0270481D19C8E08B00FDA1C5 /* Info.plist */ = {isa = '
               'PBXFileReference; lastKnownFileType = text.plist.xml; path = '
               'Info.plist; sourceTree = "<group>"; };\n'
               '\t\t0270481E19C8E08B00FDA1C5 /* MusicPlayerTests.swift */ = '
               '{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; '
               'path = MusicPlayerTests.swift; sourceTree = "<group>"; };\n'
               '\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=114,
          lineno=45,
          tokens=218,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='0270482819C8E2E700FDA1C5 /* APIController.swift */ = {isa = '
               'PBXFileReference; fileEncoding = 4; lastKnownFileType = '
               'sourcecode.swift; path = APIController.swift; sourceTree = '
               '"<group>"; };\n'
               '\t\t0270482A19C8EC3000FDA1C5 /* Blank52.png */ = {isa = '
               'PBXFileReference; lastKnownFileType = image.png; path = '
               'Blank52.png; sourceTree = "<group>"; };\n'
               '\t\t0270482C19C8F35700FDA1C5 /* Album.swift */ = {isa = '
               'PBXFileReference; fileEncoding = 4; lastKnownFileType = '
               'sourcecode.swift; path = Album.swift; sourceTree = "<group>"; '
               '};\n'
               '\t\t0270482E19C8F43500FDA1C5 /* DetailsViewController.swift */ '
               '= {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType '
               '= sourcecode.swift; path = DetailsViewController.swift; '
               'sourceTree = "<group>"; };\n'
               '\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=115,
          lineno=49,
          tokens=117,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='0270483019C8F6D000FDA1C5 /* Track.swift */ = {isa = '
               'PBXFileReference; fileEncoding = 4; lastKnownFileType = '
               'sourcecode.swift; path = Track.swift; sourceTree = "<group>"; '
               '};\n'
               '\t\t0270483419C8F80000FDA1C5 /* TrackCell.swift */ = {isa = '
               'PBXFileReference; fileEncoding = 4; lastKnownFileType = '
               'sourcecode.swift; path = TrackCell.swift; sourceTree = '
               '"<group>"; };\n'
               '/* End PBXFileReference section */\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=116,
          lineno=52,
          tokens=249,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '/* Begin PBXFrameworksBuildPhase section */\n'
               '\t\t0270480019C8E08B00FDA1C5 /* Frameworks */ = {\n'
               '\t\t\tisa = PBXFrameworksBuildPhase;\n'
               '\t\t\tbuildActionMask = 2147483647;\n'
               '\t\t\tfiles = (\n'
               '\t\t\t);\n'
               '\t\t\trunOnlyForDeploymentPostprocessing = 0;\n'
               '\t\t};\n'
               '\t\t0270481519C8E08B00FDA1C5 /* Frameworks */ = {\n'
               '\t\t\tisa = PBXFrameworksBuildPhase;\n'
               '\t\t\tbuildActionMask = 2147483647;\n'
               '\t\t\tfiles = (\n'
               '\t\t\t);\n'
               '\t\t\trunOnlyForDeploymentPostprocessing = 0;\n'
               '\t\t};\n'
               '/* End PBXFrameworksBuildPhase section */\n'
               '\n'
               '/* Begin PBXGroup section */\n'
               '\t\t027047FA19C8E08B00FDA1C5 = {\n'
               '\t\t\tisa = PBXGroup;\n'
               '\t\t\tchildren = (\n'
               '\t\t\t\t0270480519C8E08B00FDA1C5 /* MusicPlayer */,\n'
               '\t\t\t\t0270481B19C8E08B00FDA1C5 /* MusicPlayerTests */,\n'
               '\t\t\t\t0270480419C8E08B00FDA1C5 /* Products */,\n'
               '\t\t\t);\n'
               '\t\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=117,
          lineno=78,
          tokens=247,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='sourceTree = "<group>";\n'
               '\t\t};\n'
               '\t\t0270480419C8E08B00FDA1C5 /* Products */ = {\n'
               '\t\t\tisa = PBXGroup;\n'
               '\t\t\tchildren = (\n'
               '\t\t\t\t0270480319C8E08B00FDA1C5 /* MusicPlayer.app */,\n'
               '\t\t\t\t0270481819C8E08B00FDA1C5 /* MusicPlayerTests.xctest '
               '*/,\n'
               '\t\t\t);\n'
               '\t\t\tname = Products;\n'
               '\t\t\tsourceTree = "<group>";\n'
               '\t\t};\n'
               '\t\t0270480519C8E08B00FDA1C5 /* MusicPlayer */ = {\n'
               '\t\t\tisa = PBXGroup;\n'
               '\t\t\tchildren = (\n'
               '\t\t\t\t0270482A19C8EC3000FDA1C5 /* Blank52.png */,\n'
               '\t\t\t\t0270480819C8E08B00FDA1C5 /* AppDelegate.swift */,\n'
               '\t\t\t\t0270480A19C8E08B00FDA1C5 /* '
               'SearchResultsViewController.swift */,\n'
               '\t\t\t\t0270480C19C8E08B00FDA1C5 /* Main.storyboard */,\n'
               '\t\t\t\t0270480F19C8E08B00FDA1C5 /* Images.xcassets */,\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=118,
          lineno=97,
          tokens=148,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\t\t\t\t0270481119C8E08B00FDA1C5 /* LaunchScreen.xib */,\n'
               '\t\t\t\t0270480619C8E08B00FDA1C5 /* Supporting Files */,\n'
               '\t\t\t\t0270482819C8E2E700FDA1C5 /* APIController.swift */,\n'
               '\t\t\t\t0270482C19C8F35700FDA1C5 /* Album.swift */,\n'
               '\t\t\t\t0270482E19C8F43500FDA1C5 /* '
               'DetailsViewController.swift */,\n'
               '\t\t\t\t0270483019C8F6D000FDA1C5 /* Track.swift */,\n'
               '\t\t\t\t0270483419C8F80000FDA1C5 /* TrackCell.swift */,\n'
               '\t\t\t);\n'
               '\t\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=119,
          lineno=105,
          tokens=250,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='path = MusicPlayer;\n'
               '\t\t\tsourceTree = "<group>";\n'
               '\t\t};\n'
               '\t\t0270480619C8E08B00FDA1C5 /* Supporting Files */ = {\n'
               '\t\t\tisa = PBXGroup;\n'
               '\t\t\tchildren = (\n'
               '\t\t\t\t0270480719C8E08B00FDA1C5 /* Info.plist */,\n'
               '\t\t\t);\n'
               '\t\t\tname = "Supporting Files";\n'
               '\t\t\tsourceTree = "<group>";\n'
               '\t\t};\n'
               '\t\t0270481B19C8E08B00FDA1C5 /* MusicPlayerTests */ = {\n'
               '\t\t\tisa = PBXGroup;\n'
               '\t\t\tchildren = (\n'
               '\t\t\t\t0270481E19C8E08B00FDA1C5 /* MusicPlayerTests.swift '
               '*/,\n'
               '\t\t\t\t0270481C19C8E08B00FDA1C5 /* Supporting Files */,\n'
               '\t\t\t);\n'
               '\t\t\tpath = MusicPlayerTests;\n'
               '\t\t\tsourceTree = "<group>";\n'
               '\t\t};\n'
               '\t\t0270481C19C8E08B00FDA1C5 /* Supporting Files */ = {\n'
               '\t\t\tisa = PBXGroup;\n'
               '\t\t\tchildren = (\n'
               '\t\t\t\t0270481D19C8E08B00FDA1C5 /* Info.plist */,\n'
               '\t\t\t);\n'
               '\t\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=120,
          lineno=130,
          tokens=24,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='name = "Supporting Files";\n'
               '\t\t\tsourceTree = "<group>";\n'
               '\t\t};\n'
               '/* End PBXGroup section */\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=121,
          lineno=134,
          tokens=241,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '/* Begin PBXNativeTarget section */\n'
               '\t\t0270480219C8E08B00FDA1C5 /* MusicPlayer */ = {\n'
               '\t\t\tisa = PBXNativeTarget;\n'
               '\t\t\tbuildConfigurationList = 0270482219C8E08B00FDA1C5 /* '
               'Build configuration list for PBXNativeTarget "MusicPlayer" '
               '*/;\n'
               '\t\t\tbuildPhases = (\n'
               '\t\t\t\t027047FF19C8E08B00FDA1C5 /* Sources */,\n'
               '\t\t\t\t0270480019C8E08B00FDA1C5 /* Frameworks */,\n'
               '\t\t\t\t0270480119C8E08B00FDA1C5 /* Resources */,\n'
               '\t\t\t);\n'
               '\t\t\tbuildRules = (\n'
               '\t\t\t);\n'
               '\t\t\tdependencies = (\n'
               '\t\t\t);\n'
               '\t\t\tname = MusicPlayer;\n'
               '\t\t\tproductName = MusicPlayer;\n'
               '\t\t\tproductReference = 0270480319C8E08B00FDA1C5 /* '
               'MusicPlayer.app */;\n'
               '\t\t\tproductType = "com.apple.product-type.application";\n'
               '\t\t};\n'
               '\t\t0270481719C8E08B00FDA1C5 /* MusicPlayerTests */ = {\n'
               '\t\t\tisa = PBXNativeTarget;\n'
               '\t\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=122,
          lineno=155,
          tokens=205,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='buildConfigurationList = 0270482519C8E08B00FDA1C5 /* Build '
               'configuration list for PBXNativeTarget "MusicPlayerTests" */;\n'
               '\t\t\tbuildPhases = (\n'
               '\t\t\t\t0270481419C8E08B00FDA1C5 /* Sources */,\n'
               '\t\t\t\t0270481519C8E08B00FDA1C5 /* Frameworks */,\n'
               '\t\t\t\t0270481619C8E08B00FDA1C5 /* Resources */,\n'
               '\t\t\t);\n'
               '\t\t\tbuildRules = (\n'
               '\t\t\t);\n'
               '\t\t\tdependencies = (\n'
               '\t\t\t\t0270481A19C8E08B00FDA1C5 /* PBXTargetDependency */,\n'
               '\t\t\t);\n'
               '\t\t\tname = MusicPlayerTests;\n'
               '\t\t\tproductName = MusicPlayerTests;\n'
               '\t\t\tproductReference = 0270481819C8E08B00FDA1C5 /* '
               'MusicPlayerTests.xctest */;\n'
               '\t\t\tproductType = '
               '"com.apple.product-type.bundle.unit-test";\n'
               '\t\t};\n'
               '/* End PBXNativeTarget section */\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=123,
          lineno=172,
          tokens=244,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '/* Begin PBXProject section */\n'
               '\t\t027047FB19C8E08B00FDA1C5 /* Project object */ = {\n'
               '\t\t\tisa = PBXProject;\n'
               '\t\t\tattributes = {\n'
               '\t\t\t\tLastUpgradeCheck = 0600;\n'
               '\t\t\t\tORGANIZATIONNAME = "JQ Software LLC";\n'
               '\t\t\t\tTargetAttributes = {\n'
               '\t\t\t\t\t0270480219C8E08B00FDA1C5 = {\n'
               '\t\t\t\t\t\tCreatedOnToolsVersion = 6.0;\n'
               '\t\t\t\t\t};\n'
               '\t\t\t\t\t0270481719C8E08B00FDA1C5 = {\n'
               '\t\t\t\t\t\tCreatedOnToolsVersion = 6.0;\n'
               '\t\t\t\t\t\tTestTargetID = 0270480219C8E08B00FDA1C5;\n'
               '\t\t\t\t\t};\n'
               '\t\t\t\t};\n'
               '\t\t\t};\n'
               '\t\t\tbuildConfigurationList = 027047FE19C8E08B00FDA1C5 /* '
               'Build configuration list for PBXProject "MusicPlayer" */;\n'
               '\t\t\tcompatibilityVersion = "Xcode 3.2";\n'
               '\t\t\tdevelopmentRegion = English;\n'
               '\t\t\thasScannedForEncodings = 0;\n'
               '\t\t\tknownRegions = (\n'
               '\t\t\t\ten,\n'
               '\t\t\t\tBase,\n'
               '\t\t\t);\n'
               '\t\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=124,
          lineno=197,
          tokens=112,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='mainGroup = 027047FA19C8E08B00FDA1C5;\n'
               '\t\t\tproductRefGroup = 0270480419C8E08B00FDA1C5 /* Products '
               '*/;\n'
               '\t\t\tprojectDirPath = "";\n'
               '\t\t\tprojectRoot = "";\n'
               '\t\t\ttargets = (\n'
               '\t\t\t\t0270480219C8E08B00FDA1C5 /* MusicPlayer */,\n'
               '\t\t\t\t0270481719C8E08B00FDA1C5 /* MusicPlayerTests */,\n'
               '\t\t\t);\n'
               '\t\t};\n'
               '/* End PBXProject section */\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=125,
          lineno=207,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '/* Begin PBXResourcesBuildPhase section */\n'
               '\t\t0270480119C8E08B00FDA1C5 /* Resources */ = {\n'
               '\t\t\tisa = PBXResourcesBuildPhase;\n'
               '\t\t\tbuildActionMask = 2147483647;\n'
               '\t\t\tfiles = (\n'
               '\t\t\t\t0270480E19C8E08B00FDA1C5 /* Main.storyboard in '
               'Resources */,\n'
               '\t\t\t\t0270482B19C8EC3000FDA1C5 /* Blank52.png in Resources '
               '*/,\n'
               '\t\t\t\t0270481319C8E08B00FDA1C5 /* LaunchScreen.xib in '
               'Resources */,\n'
               '\t\t\t\t0270481019C8E08B00FDA1C5 /* Images.xcassets in '
               'Resources */,\n'
               '\t\t\t);\n'
               '\t\t\trunOnlyForDeploymentPostprocessing = 0;\n'
               '\t\t};\n'
               '\t\t0270481619C8E08B00FDA1C5 /* Resources */ = {\n'
               '\t\t\tisa = PBXResourcesBuildPhase;\n'
               '\t\t\tbuildActionMask = 2147483647;\n'
               '\t\t\tfiles = (\n'
               '\t\t\t);\n'
               '\t\t\trunOnlyForDeploymentPostprocessing = 0;\n'
               '\t\t};\n'
               '/* End PBXResourcesBuildPhase section */\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=126,
          lineno=228,
          tokens=233,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '/* Begin PBXSourcesBuildPhase section */\n'
               '\t\t027047FF19C8E08B00FDA1C5 /* Sources */ = {\n'
               '\t\t\tisa = PBXSourcesBuildPhase;\n'
               '\t\t\tbuildActionMask = 2147483647;\n'
               '\t\t\tfiles = (\n'
               '\t\t\t\t0270483519C8F80000FDA1C5 /* TrackCell.swift in Sources '
               '*/,\n'
               '\t\t\t\t0270480B19C8E08B00FDA1C5 /* '
               'SearchResultsViewController.swift in Sources */,\n'
               '\t\t\t\t0270480919C8E08B00FDA1C5 /* AppDelegate.swift in '
               'Sources */,\n'
               '\t\t\t\t0270482919C8E2E700FDA1C5 /* APIController.swift in '
               'Sources */,\n'
               '\t\t\t\t0270482D19C8F35700FDA1C5 /* Album.swift in Sources '
               '*/,\n'
               '\t\t\t\t0270482F19C8F43500FDA1C5 /* '
               'DetailsViewController.swift in Sources */,\n'
               '\t\t\t\t0270483119C8F6D000FDA1C5 /* Track.swift in Sources '
               '*/,\n'
               '\t\t\t);\n'
               '\t\t\trunOnlyForDeploymentPostprocessing = 0;\n'
               '\t\t};\n'
               '\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=127,
          lineno=244,
          tokens=196,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='0270481419C8E08B00FDA1C5 /* Sources */ = {\n'
               '\t\t\tisa = PBXSourcesBuildPhase;\n'
               '\t\t\tbuildActionMask = 2147483647;\n'
               '\t\t\tfiles = (\n'
               '\t\t\t\t0270481F19C8E08B00FDA1C5 /* MusicPlayerTests.swift in '
               'Sources */,\n'
               '\t\t\t);\n'
               '\t\t\trunOnlyForDeploymentPostprocessing = 0;\n'
               '\t\t};\n'
               '/* End PBXSourcesBuildPhase section */\n'
               '\n'
               '/* Begin PBXTargetDependency section */\n'
               '\t\t0270481A19C8E08B00FDA1C5 /* PBXTargetDependency */ = {\n'
               '\t\t\tisa = PBXTargetDependency;\n'
               '\t\t\ttarget = 0270480219C8E08B00FDA1C5 /* MusicPlayer */;\n'
               '\t\t\ttargetProxy = 0270481919C8E08B00FDA1C5 /* '
               'PBXContainerItemProxy */;\n'
               '\t\t};\n'
               '/* End PBXTargetDependency section */\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=128,
          lineno=261,
          tokens=250,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '/* Begin PBXVariantGroup section */\n'
               '\t\t0270480C19C8E08B00FDA1C5 /* Main.storyboard */ = {\n'
               '\t\t\tisa = PBXVariantGroup;\n'
               '\t\t\tchildren = (\n'
               '\t\t\t\t0270480D19C8E08B00FDA1C5 /* Base */,\n'
               '\t\t\t);\n'
               '\t\t\tname = Main.storyboard;\n'
               '\t\t\tsourceTree = "<group>";\n'
               '\t\t};\n'
               '\t\t0270481119C8E08B00FDA1C5 /* LaunchScreen.xib */ = {\n'
               '\t\t\tisa = PBXVariantGroup;\n'
               '\t\t\tchildren = (\n'
               '\t\t\t\t0270481219C8E08B00FDA1C5 /* Base */,\n'
               '\t\t\t);\n'
               '\t\t\tname = LaunchScreen.xib;\n'
               '\t\t\tsourceTree = "<group>";\n'
               '\t\t};\n'
               '/* End PBXVariantGroup section */\n'
               '\n'
               '/* Begin XCBuildConfiguration section */\n'
               '\t\t0270482019C8E08B00FDA1C5 /* Debug */ = {\n'
               '\t\t\tisa = XCBuildConfiguration;\n'
               '\t\t\tbuildSettings = {\n'
               '\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;\n'
               '\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++0x";\n'
               '\t\t\t\tCLANG_CXX_LIBRARY = "libc++";\n'
               '\t\t\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=129,
          lineno=288,
          tokens=270,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='CLANG_ENABLE_MODULES = YES;\n'
               '\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;\n'
               '\t\t\t\tCLANG_WARN_BOOL_CONVERSION = YES;\n'
               '\t\t\t\tCLANG_WARN_CONSTANT_CONVERSION = YES;\n'
               '\t\t\t\tCLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;\n'
               '\t\t\t\tCLANG_WARN_EMPTY_BODY = YES;\n'
               '\t\t\t\tCLANG_WARN_ENUM_CONVERSION = YES;\n'
               '\t\t\t\tCLANG_WARN_INT_CONVERSION = YES;\n'
               '\t\t\t\tCLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;\n'
               '\t\t\t\tCLANG_WARN_UNREACHABLE_CODE = YES;\n'
               '\t\t\t\tCLANG_WARN__DUPLICATE_METHOD_MATCH = YES;\n'
               '\t\t\t\t"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "iPhone '
               'Developer";\n'
               '\t\t\t\tCOPY_PHASE_STRIP = NO;\n'
               '\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;\n'
               '\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu99;\n'
               '\t\t\t\tGCC_DYNAMIC_NO_PIC = NO;\n'
               '\t\t\t\tGCC_OPTIMIZATION_LEVEL = 0;\n'
               '\t\t\t\tGCC_PREPROCESSOR_DEFINITIONS = (\n'
               '\t\t\t\t\t"DEBUG=1",\n'
               '\t\t\t\t\t"$(inherited)",\n'
               '\t\t\t\t);\n'
               '\t\t\t\tGCC_SYMBOLS_PRIVATE_EXTERN = NO;\n'
               '\t\t\t\tGCC_WARN_64_TO_32_BIT_CONVERSION = YES;\n'
               '\t\t\t\tGCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;\n'
               '\t\t\t\tGCC_WARN_UNDECLARED_SELECTOR = YES;\n'
               '\t\t\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=130,
          lineno=313,
          tokens=269,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;\n'
               '\t\t\t\tGCC_WARN_UNUSED_FUNCTION = YES;\n'
               '\t\t\t\tGCC_WARN_UNUSED_VARIABLE = YES;\n'
               '\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 8.0;\n'
               '\t\t\t\tMTL_ENABLE_DEBUG_INFO = YES;\n'
               '\t\t\t\tONLY_ACTIVE_ARCH = YES;\n'
               '\t\t\t\tSDKROOT = iphoneos;\n'
               '\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = "-Onone";\n'
               '\t\t\t};\n'
               '\t\t\tname = Debug;\n'
               '\t\t};\n'
               '\t\t0270482119C8E08B00FDA1C5 /* Release */ = {\n'
               '\t\t\tisa = XCBuildConfiguration;\n'
               '\t\t\tbuildSettings = {\n'
               '\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;\n'
               '\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++0x";\n'
               '\t\t\t\tCLANG_CXX_LIBRARY = "libc++";\n'
               '\t\t\t\tCLANG_ENABLE_MODULES = YES;\n'
               '\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;\n'
               '\t\t\t\tCLANG_WARN_BOOL_CONVERSION = YES;\n'
               '\t\t\t\tCLANG_WARN_CONSTANT_CONVERSION = YES;\n'
               '\t\t\t\tCLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;\n'
               '\t\t\t\tCLANG_WARN_EMPTY_BODY = YES;\n'
               '\t\t\t\tCLANG_WARN_ENUM_CONVERSION = YES;\n'
               '\t\t\t\tCLANG_WARN_INT_CONVERSION = YES;\n'
               '\t\t\t\tCLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;\n'
               '\t\t\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=131,
          lineno=339,
          tokens=269,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='CLANG_WARN_UNREACHABLE_CODE = YES;\n'
               '\t\t\t\tCLANG_WARN__DUPLICATE_METHOD_MATCH = YES;\n'
               '\t\t\t\t"CODE_SIGN_IDENTITY[sdk=iphoneos*]" = "iPhone '
               'Developer";\n'
               '\t\t\t\tCOPY_PHASE_STRIP = YES;\n'
               '\t\t\t\tENABLE_NS_ASSERTIONS = NO;\n'
               '\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;\n'
               '\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu99;\n'
               '\t\t\t\tGCC_WARN_64_TO_32_BIT_CONVERSION = YES;\n'
               '\t\t\t\tGCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;\n'
               '\t\t\t\tGCC_WARN_UNDECLARED_SELECTOR = YES;\n'
               '\t\t\t\tGCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;\n'
               '\t\t\t\tGCC_WARN_UNUSED_FUNCTION = YES;\n'
               '\t\t\t\tGCC_WARN_UNUSED_VARIABLE = YES;\n'
               '\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 8.0;\n'
               '\t\t\t\tMTL_ENABLE_DEBUG_INFO = NO;\n'
               '\t\t\t\tSDKROOT = iphoneos;\n'
               '\t\t\t\tVALIDATE_PRODUCT = YES;\n'
               '\t\t\t};\n'
               '\t\t\tname = Release;\n'
               '\t\t};\n'
               '\t\t0270482319C8E08B00FDA1C5 /* Debug */ = {\n'
               '\t\t\tisa = XCBuildConfiguration;\n'
               '\t\t\tbuildSettings = {\n'
               '\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;\n'
               '\t\t\t\tINFOPLIST_FILE = MusicPlayer/Info.plist;\n'
               '\t\t\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=132,
          lineno=364,
          tokens=255,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='LD_RUNPATH_SEARCH_PATHS = "$(inherited) '
               '@executable_path/Frameworks";\n'
               '\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";\n'
               '\t\t\t};\n'
               '\t\t\tname = Debug;\n'
               '\t\t};\n'
               '\t\t0270482419C8E08B00FDA1C5 /* Release */ = {\n'
               '\t\t\tisa = XCBuildConfiguration;\n'
               '\t\t\tbuildSettings = {\n'
               '\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;\n'
               '\t\t\t\tINFOPLIST_FILE = MusicPlayer/Info.plist;\n'
               '\t\t\t\tLD_RUNPATH_SEARCH_PATHS = "$(inherited) '
               '@executable_path/Frameworks";\n'
               '\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";\n'
               '\t\t\t};\n'
               '\t\t\tname = Release;\n'
               '\t\t};\n'
               '\t\t0270482619C8E08B00FDA1C5 /* Debug */ = {\n'
               '\t\t\tisa = XCBuildConfiguration;\n'
               '\t\t\tbuildSettings = {\n'
               '\t\t\t\tBUNDLE_LOADER = "$(TEST_HOST)";\n'
               '\t\t\t\tFRAMEWORK_SEARCH_PATHS = (\n'
               '\t\t\t\t\t"$(SDKROOT)/Developer/Library/Frameworks",\n'
               '\t\t\t\t\t"$(inherited)",\n'
               '\t\t\t\t);\n'
               '\t\t\t\tGCC_PREPROCESSOR_DEFINITIONS = (\n'
               '\t\t\t\t\t"DEBUG=1",\n'
               '\t\t\t\t\t"$(inherited)",\n'
               '\t\t\t\t);\n'
               '\t\t\t\tINFOPLIST_FILE = MusicPlayerTests/Info.plist;\n'
               '\t\t\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=133,
          lineno=392,
          tokens=216,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='LD_RUNPATH_SEARCH_PATHS = "$(inherited) '
               '@executable_path/Frameworks @loader_path/Frameworks";\n'
               '\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";\n'
               '\t\t\t\tTEST_HOST = '
               '"$(BUILT_PRODUCTS_DIR)/MusicPlayer.app/MusicPlayer";\n'
               '\t\t\t};\n'
               '\t\t\tname = Debug;\n'
               '\t\t};\n'
               '\t\t0270482719C8E08B00FDA1C5 /* Release */ = {\n'
               '\t\t\tisa = XCBuildConfiguration;\n'
               '\t\t\tbuildSettings = {\n'
               '\t\t\t\tBUNDLE_LOADER = "$(TEST_HOST)";\n'
               '\t\t\t\tFRAMEWORK_SEARCH_PATHS = (\n'
               '\t\t\t\t\t"$(SDKROOT)/Developer/Library/Frameworks",\n'
               '\t\t\t\t\t"$(inherited)",\n'
               '\t\t\t\t);\n'
               '\t\t\t\tINFOPLIST_FILE = MusicPlayerTests/Info.plist;\n'
               '\t\t\t\tLD_RUNPATH_SEARCH_PATHS = "$(inherited) '
               '@executable_path/Frameworks @loader_path/Frameworks";\n'
               '\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";\n'
               '\t\t\t\tTEST_HOST = '
               '"$(BUILT_PRODUCTS_DIR)/MusicPlayer.app/MusicPlayer";\n'
               '\t\t\t};\n'
               '\t\t\tname = Release;\n'
               '\t\t};\n'
               '/* End XCBuildConfiguration section */\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=134,
          lineno=414,
          tokens=220,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '/* Begin XCConfigurationList section */\n'
               '\t\t027047FE19C8E08B00FDA1C5 /* Build configuration list for '
               'PBXProject "MusicPlayer" */ = {\n'
               '\t\t\tisa = XCConfigurationList;\n'
               '\t\t\tbuildConfigurations = (\n'
               '\t\t\t\t0270482019C8E08B00FDA1C5 /* Debug */,\n'
               '\t\t\t\t0270482119C8E08B00FDA1C5 /* Release */,\n'
               '\t\t\t);\n'
               '\t\t\tdefaultConfigurationIsVisible = 0;\n'
               '\t\t\tdefaultConfigurationName = Release;\n'
               '\t\t};\n'
               '\t\t0270482219C8E08B00FDA1C5 /* Build configuration list for '
               'PBXNativeTarget "MusicPlayer" */ = {\n'
               '\t\t\tisa = XCConfigurationList;\n'
               '\t\t\tbuildConfigurations = (\n'
               '\t\t\t\t0270482319C8E08B00FDA1C5 /* Debug */,\n'
               '\t\t\t\t0270482419C8E08B00FDA1C5 /* Release */,\n'
               '\t\t\t);\n'
               '\t\t\tdefaultConfigurationIsVisible = 0;\n'
               '\t\t\tdefaultConfigurationName = Release;\n'
               '\t\t};\n'
               '\t\t'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=135,
          lineno=434,
          tokens=137,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='0270482519C8E08B00FDA1C5 /* Build configuration list for '
               'PBXNativeTarget "MusicPlayerTests" */ = {\n'
               '\t\t\tisa = XCConfigurationList;\n'
               '\t\t\tbuildConfigurations = (\n'
               '\t\t\t\t0270482619C8E08B00FDA1C5 /* Debug */,\n'
               '\t\t\t\t0270482719C8E08B00FDA1C5 /* Release */,\n'
               '\t\t\t);\n'
               '\t\t\tdefaultConfigurationIsVisible = 0;\n'
               '\t\t\tdefaultConfigurationName = Release;\n'
               '\t\t};\n'
               '/* End XCConfigurationList section */\n'
               '\t};\n'
               '\trootObject = 027047FB19C8E08B00FDA1C5 /* Project object */;\n'
               '}\n'),
 Fragment(document_cs='dbbca263507c57d8aef9b87aa9d58e0f497401f8bb95d731aa5aaacf941a7134',
          id=136,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='dcb3ef8e4696e3b9a215fbeb62194360c0a2aed8e5a64d009650795e471abbf1',
          id=137,
          lineno=11,
          tokens=222,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='AppDelegate',
          body='@UIApplicationMain\n'
               'class AppDelegate: UIResponder, UIApplicationDelegate {\n'
               '\n'
               '    var window: UIWindow?\n'
               '\n'
               '\n'
               '    func application(application: UIApplication, '
               'didFinishLaunchingWithOptions launchOptions: [NSObject: '
               'AnyObject]?) -> Bool {\n'
               '        println("Hello World!")\n'
               '        return true\n'
               '    }\n'
               '\n'
               '    func applicationWillResignActive(application: '
               'UIApplication) {\n'
               '        // Sent when the application is about to move from '
               'active to inactive state. This can occur for certain types of '
               'temporary interruptions (such as an incoming phone call or SMS '
               'message) or when the user quits the application and it begins '
               'the transition to the background state.\n'
               '        // Use this method to pause ongoing tasks, disable '
               'timers, and throttle down OpenGL ES frame rates. Games should '
               'use this method to pause the game.\n'
               '    }\n'
               '\n'
               '    func applicationDidEnterBackground(application: '
               'UIApplication) {\n'
               '        // Use this method to release shared resources, save '
               'user data, invalidate timers, and store enough application '
               'state information to restore your application to its current '
               'state in case it is terminated later.\n'
               '        // If your application supports background execution, '
               'this method is called instead of applicationWillTerminate: '
               'when the user quits.\n'
               '    }\n'),
 Fragment(document_cs='dcb3ef8e4696e3b9a215fbeb62194360c0a2aed8e5a64d009650795e471abbf1',
          id=138,
          lineno=31,
          tokens=126,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='AppDelegate',
          body='\n'
               '    func applicationWillEnterForeground(application: '
               'UIApplication) {\n'
               '        // Called as part of the transition from the '
               'background to the inactive state; here you can undo many of '
               'the changes made on entering the background.\n'
               '    }\n'
               '\n'
               '    func applicationDidBecomeActive(application: '
               'UIApplication) {\n'
               '        // Restart any tasks that were paused (or not yet '
               'started) while the application was inactive. If the '
               'application was previously in the background, optionally '
               'refresh the user interface.\n'
               '    }\n'
               '\n'
               '    func applicationWillTerminate(application: UIApplication) '
               '{\n'
               '        // Called when the application is about to terminate. '
               'Save data if appropriate. See also '
               'applicationDidEnterBackground:.\n'
               '    }\n'
               '\n'
               '\n'
               '}'),
 Fragment(document_cs='dcb3ef8e4696e3b9a215fbeb62194360c0a2aed8e5a64d009650795e471abbf1',
          id=139,
          lineno=17,
          tokens=33,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='application',
          body='func application(application: UIApplication, '
               'didFinishLaunchingWithOptions launchOptions: [NSObject: '
               'AnyObject]?) -> Bool {\n'
               '        println("Hello World!")\n'
               '        return true\n'
               '    }'),
 Fragment(document_cs='dcb3ef8e4696e3b9a215fbeb62194360c0a2aed8e5a64d009650795e471abbf1',
          id=140,
          lineno=22,
          tokens=96,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='applicationWillResignActive',
          body='func applicationWillResignActive(application: UIApplication) '
               '{\n'
               '        // Sent when the application is about to move from '
               'active to inactive state. This can occur for certain types of '
               'temporary interruptions (such as an incoming phone call or SMS '
               'message) or when the user quits the application and it begins '
               'the transition to the background state.\n'
               '        // Use this method to pause ongoing tasks, disable '
               'timers, and throttle down OpenGL ES frame rates. Games should '
               'use this method to pause the game.\n'
               '    }'),
 Fragment(document_cs='dcb3ef8e4696e3b9a215fbeb62194360c0a2aed8e5a64d009650795e471abbf1',
          id=141,
          lineno=27,
          tokens=72,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='applicationDidEnterBackground',
          body='func applicationDidEnterBackground(application: UIApplication) '
               '{\n'
               '        // Use this method to release shared resources, save '
               'user data, invalidate timers, and store enough application '
               'state information to restore your application to its current '
               'state in case it is terminated later.\n'
               '        // If your application supports background execution, '
               'this method is called instead of applicationWillTerminate: '
               'when the user quits.\n'
               '    }'),
 Fragment(document_cs='dcb3ef8e4696e3b9a215fbeb62194360c0a2aed8e5a64d009650795e471abbf1',
          id=142,
          lineno=32,
          tokens=41,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='applicationWillEnterForeground',
          body='func applicationWillEnterForeground(application: '
               'UIApplication) {\n'
               '        // Called as part of the transition from the '
               'background to the inactive state; here you can undo many of '
               'the changes made on entering the background.\n'
               '    }'),
 Fragment(document_cs='dcb3ef8e4696e3b9a215fbeb62194360c0a2aed8e5a64d009650795e471abbf1',
          id=143,
          lineno=36,
          tokens=47,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='applicationDidBecomeActive',
          body='func applicationDidBecomeActive(application: UIApplication) {\n'
               '        // Restart any tasks that were paused (or not yet '
               'started) while the application was inactive. If the '
               'application was previously in the background, optionally '
               'refresh the user interface.\n'
               '    }'),
 Fragment(document_cs='dcb3ef8e4696e3b9a215fbeb62194360c0a2aed8e5a64d009650795e471abbf1',
          id=144,
          lineno=40,
          tokens=33,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='applicationWillTerminate',
          body='func applicationWillTerminate(application: UIApplication) {\n'
               '        // Called when the application is about to terminate. '
               'Save data if appropriate. See also '
               'applicationDidEnterBackground:.\n'
               '    }'),
 Fragment(document_cs='dcb3ef8e4696e3b9a215fbeb62194360c0a2aed8e5a64d009650795e471abbf1',
          id=145,
          lineno=14,
          tokens=5,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='window',
          body='var window: UIWindow?'),
 Fragment(document_cs='dcb3ef8e4696e3b9a215fbeb62194360c0a2aed8e5a64d009650795e471abbf1',
          id=146,
          lineno=1,
          tokens=31,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Classes: AppDelegate\n'
               '  Functions: application applicationDidBecomeActive '
               'applicationDidEnterBackground applicationWillEnterForeground '
               'applicationWillResignActive applicationWillTerminate\n'
               '  Properties: window\n'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=147,
          lineno=15,
          tokens=227,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='APIController',
          body='class APIController {\n'
               '    \n'
               '    var delegate: APIControllerProtocol\n'
               '\n'
               '    init(delegate: APIControllerProtocol) {\n'
               '        self.delegate = delegate\n'
               '    }\n'
               '    \n'
               '    func get(path: String) {\n'
               '        let url = NSURL(string: path)\n'
               '        let session = NSURLSession.sharedSession()\n'
               '        let task = session.dataTaskWithURL(url, '
               'completionHandler: {data, response, error -> Void in\n'
               '            println("Task completed")\n'
               '            if(error != nil) {\n'
               '                // If there is an error in the web request, '
               'print it to the console\n'
               '                println(error.localizedDescription)\n'
               '            }\n'
               '            var err: NSError?\n'
               '            var jsonResult = '
               'NSJSONSerialization.JSONObjectWithData(data, options: '
               'NSJSONReadingOptions.MutableContainers, error: &err) as '
               'NSDictionary\n'
               '            if(err != nil) {\n'
               '                // If there is an error parsing JSON, print it '
               'to the console\n'
               '                println("JSON Error '
               '\\(err!.localizedDescription)")\n'
               '            }\n'
               '            let results: NSArray = jsonResult["results"] as '
               'NSArray\n'
               '            self.delegate.didReceiveAPIResults(jsonResult) // '
               'THIS IS THE NEW LINE!!\n'
               '        })\n'
               '        task.resume()\n'
               '    }\n'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=148,
          lineno=43,
          tokens=176,
          depth=0,
          parent_id=None,
          category='class',
          summary=False,
          name='APIController',
          body='    \n'
               '    func searchItunesFor(searchTerm: String) {\n'
               '        \n'
               '        // The iTunes API wants multiple terms separated by + '
               'symbols, so replace spaces with + signs\n'
               '        let itunesSearchTerm = '
               'searchTerm.stringByReplacingOccurrencesOfString(" ", '
               'withString: "+", options: '
               'NSStringCompareOptions.CaseInsensitiveSearch, range: nil)\n'
               '        \n'
               "        // Now escape anything else that isn't URL-friendly\n"
               '        if let escapedSearchTerm = '
               'itunesSearchTerm.stringByAddingPercentEscapesUsingEncoding(NSUTF8StringEncoding) '
               '{\n'
               '            let urlPath = '
               '"https://itunes.apple.com/search?term=\\(escapedSearchTerm)&media=music&entity=album"\n'
               '            get(urlPath)\n'
               '        }\n'
               '    }\n'
               '    \n'
               '    func lookupAlbum(collectionId: Int) {\n'
               '        '
               'get("https://itunes.apple.com/lookup?id=\\(collectionId)&entity=song")\n'
               '    }\n'
               '    \n'
               '}'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=149,
          lineno=23,
          tokens=195,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='get',
          body='func get(path: String) {\n'
               '        let url = NSURL(string: path)\n'
               '        let session = NSURLSession.sharedSession()\n'
               '        let task = session.dataTaskWithURL(url, '
               'completionHandler: {data, response, error -> Void in\n'
               '            println("Task completed")\n'
               '            if(error != nil) {\n'
               '                // If there is an error in the web request, '
               'print it to the console\n'
               '                println(error.localizedDescription)\n'
               '            }\n'
               '            var err: NSError?\n'
               '            var jsonResult = '
               'NSJSONSerialization.JSONObjectWithData(data, options: '
               'NSJSONReadingOptions.MutableContainers, error: &err) as '
               'NSDictionary\n'
               '            if(err != nil) {\n'
               '                // If there is an error parsing JSON, print it '
               'to the console\n'
               '                println("JSON Error '
               '\\(err!.localizedDescription)")\n'
               '            }\n'
               '            let results: NSArray = jsonResult["results"] as '
               'NSArray\n'
               '            self.delegate.didReceiveAPIResults(jsonResult) // '
               'THIS IS THE NEW LINE!!\n'
               '        })\n'
               '        task.resume()\n'
               '    }'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=150,
          lineno=44,
          tokens=139,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='searchItunesFor',
          body='func searchItunesFor(searchTerm: String) {\n'
               '        \n'
               '        // The iTunes API wants multiple terms separated by + '
               'symbols, so replace spaces with + signs\n'
               '        let itunesSearchTerm = '
               'searchTerm.stringByReplacingOccurrencesOfString(" ", '
               'withString: "+", options: '
               'NSStringCompareOptions.CaseInsensitiveSearch, range: nil)\n'
               '        \n'
               "        // Now escape anything else that isn't URL-friendly\n"
               '        if let escapedSearchTerm = '
               'itunesSearchTerm.stringByAddingPercentEscapesUsingEncoding(NSUTF8StringEncoding) '
               '{\n'
               '            let urlPath = '
               '"https://itunes.apple.com/search?term=\\(escapedSearchTerm)&media=music&entity=album"\n'
               '            get(urlPath)\n'
               '        }\n'
               '    }'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=151,
          lineno=56,
          tokens=31,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='lookupAlbum',
          body='func lookupAlbum(collectionId: Int) {\n'
               '        '
               'get("https://itunes.apple.com/lookup?id=\\(collectionId)&entity=song")\n'
               '    }'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=152,
          lineno=17,
          tokens=6,
          depth=2,
          parent_id=None,
          category='property',
          summary=False,
          name='delegate',
          body='var delegate: APIControllerProtocol'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=153,
          lineno=24,
          tokens=8,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='url',
          body='let url = NSURL(string: path)'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=154,
          lineno=25,
          tokens=8,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='session',
          body='let session = NSURLSession.sharedSession()'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=155,
          lineno=26,
          tokens=163,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='task',
          body='let task = session.dataTaskWithURL(url, completionHandler: '
               '{data, response, error -> Void in\n'
               '            println("Task completed")\n'
               '            if(error != nil) {\n'
               '                // If there is an error in the web request, '
               'print it to the console\n'
               '                println(error.localizedDescription)\n'
               '            }\n'
               '            var err: NSError?\n'
               '            var jsonResult = '
               'NSJSONSerialization.JSONObjectWithData(data, options: '
               'NSJSONReadingOptions.MutableContainers, error: &err) as '
               'NSDictionary\n'
               '            if(err != nil) {\n'
               '                // If there is an error parsing JSON, print it '
               'to the console\n'
               '                println("JSON Error '
               '\\(err!.localizedDescription)")\n'
               '            }\n'
               '            let results: NSArray = jsonResult["results"] as '
               'NSArray\n'
               '            self.delegate.didReceiveAPIResults(jsonResult) // '
               'THIS IS THE NEW LINE!!\n'
               '        })'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=156,
          lineno=32,
          tokens=5,
          depth=12,
          parent_id=None,
          category='property',
          summary=False,
          name='err',
          body='var err: NSError?'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=157,
          lineno=33,
          tokens=27,
          depth=12,
          parent_id=None,
          category='property',
          summary=False,
          name='jsonResult',
          body='var jsonResult = NSJSONSerialization.JSONObjectWithData(data, '
               'options: NSJSONReadingOptions.MutableContainers, error: &err) '
               'as NSDictionary'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=158,
          lineno=38,
          tokens=12,
          depth=12,
          parent_id=None,
          category='property',
          summary=False,
          name='results',
          body='let results: NSArray = jsonResult["results"] as NSArray'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=159,
          lineno=47,
          tokens=32,
          depth=5,
          parent_id=None,
          category='property',
          summary=False,
          name='itunesSearchTerm',
          body='let itunesSearchTerm = '
               'searchTerm.stringByReplacingOccurrencesOfString(" ", '
               'withString: "+", options: '
               'NSStringCompareOptions.CaseInsensitiveSearch, range: nil)'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=160,
          lineno=51,
          tokens=27,
          depth=7,
          parent_id=None,
          category='property',
          summary=False,
          name='urlPath',
          body='let urlPath = '
               '"https://itunes.apple.com/search?term=\\(escapedSearchTerm)&media=music&entity=album"'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=161,
          lineno=11,
          tokens=16,
          depth=0,
          parent_id=None,
          category='protocol',
          summary=False,
          name='APIControllerProtocol',
          body='protocol APIControllerProtocol {\n'
               '    func didReceiveAPIResults(results: NSDictionary)\n'
               '}'),
 Fragment(document_cs='ea823dbfe3450052d5502f024aea879451be13907e6d8aa202399fa99d66aa2b',
          id=162,
          lineno=1,
          tokens=49,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Protocols: APIControllerProtocol\n'
               '  Classes: APIController\n'
               '  Functions: get lookupAlbum searchItunesFor\n'
               '  Properties: delegate err itunesSearchTerm jsonResult results '
               'session task url urlPath\n'
               '  Usages: delegate\n')]