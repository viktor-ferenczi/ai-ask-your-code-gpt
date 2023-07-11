[Fragment(document_cs='11439a518a2a11d11a52579267ab7ce0ef4da2ee5822d37871c49475066613e9',
          id=1,
          lineno=1,
          tokens=84,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               '/**\n'
               ' * @title SafeMathUint\n'
               ' * @dev Math operations with safety checks that revert on '
               'error\n'
               ' */\n'
               'library SafeMathUint {\n'
               '  function toInt256Safe(uint256 a) internal pure returns '
               '(int256) {\n'
               '    int256 b = int256(a);\n'
               '    require(b >= 0);\n'
               '    return b;\n'
               '  }\n'
               '}'),
 Fragment(document_cs='11439a518a2a11d11a52579267ab7ce0ef4da2ee5822d37871c49475066613e9',
          id=2,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='1b9202d89281ce8004a8fdd71b36b4c428d83aa54474077f951adb173f3e785d',
          id=3,
          lineno=1,
          tokens=140,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'import "./IERC20.sol";\n'
               '\n'
               '/**\n'
               ' * @dev Interface for the optional metadata functions from the '
               'ERC20 standard.\n'
               ' *\n'
               ' * _Available since v4.1._\n'
               ' */\n'
               'interface IERC20Metadata is IERC20 {\n'
               '    /**\n'
               '     * @dev Returns the name of the token.\n'
               '     */\n'
               '    function name() external view returns (string memory);\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the symbol of the token.\n'
               '     */\n'
               '    function symbol() external view returns (string memory);\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the decimals places of the token.\n'
               '     */\n'
               '    function decimals() external view returns (uint8);\n'
               '}'),
 Fragment(document_cs='1b9202d89281ce8004a8fdd71b36b4c428d83aa54474077f951adb173f3e785d',
          id=4,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='4f1c0fb491c6a7261e1aaf20fda4b25a644d28a54b502b526b71b8576981d2b5',
          id=5,
          lineno=1,
          tokens=219,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               '/*\n'
               ' * @dev Provides information about the current execution '
               'context, including the\n'
               ' * sender of the transaction and its data. While these are '
               'generally available\n'
               ' * via msg.sender and msg.data, they should not be accessed in '
               'such a direct\n'
               ' * manner, since when dealing with meta-transactions the '
               'account sending and\n'
               ' * paying for execution may not be the actual sender (as far '
               'as an application\n'
               ' * is concerned).\n'
               ' *\n'
               ' * This contract is only required for intermediate, '
               'library-like contracts.\n'
               ' */\n'
               'abstract contract Context {\n'
               '    function _msgSender() internal view virtual returns '
               '(address) {\n'
               '        return msg.sender;\n'
               '    }\n'
               '\n'
               '    function _msgData() internal view virtual returns (bytes '
               'memory) {\n'
               '        this; // silence state mutability warning without '
               'generating bytecode - see '
               'https://github.com/ethereum/solidity/issues/2691\n'
               '        return msg.data;\n'
               '    }\n'
               '}\n'
               '\n'
               'abstract contract Initializable {\n'
               '    /**\n'
               '     * @dev Indicates that the contract has been initialized.\n'
               '     */\n'
               '    bool private _initialized;\n'),
 Fragment(document_cs='4f1c0fb491c6a7261e1aaf20fda4b25a644d28a54b502b526b71b8576981d2b5',
          id=6,
          lineno=32,
          tokens=225,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Indicates that the contract is in the process of '
               'being initialized.\n'
               '     */\n'
               '    bool private _initializing;\n'
               '\n'
               '    /**\n'
               '     * @dev Modifier to protect an initializer function from '
               'being invoked twice.\n'
               '     */\n'
               '    modifier initializer() {\n'
               '        require(_initializing || !_initialized, '
               '"Initializable: contract is already initialized");\n'
               '\n'
               '        bool isTopLevelCall = !_initializing;\n'
               '        if (isTopLevelCall) {\n'
               '            _initializing = true;\n'
               '            _initialized = true;\n'
               '        }\n'
               '\n'
               '        _;\n'
               '\n'
               '        if (isTopLevelCall) {\n'
               '            _initializing = false;\n'
               '        }\n'
               '    }\n'
               '}\n'
               '\n'
               'abstract contract ContextUpgradeable is Initializable {\n'
               '    function __Context_init() internal initializer {\n'
               '        __Context_init_unchained();\n'
               '    }\n'
               '\n'
               '    function __Context_init_unchained() internal initializer '
               '{\n'
               '    }\n'
               '    function _msgSender() internal view virtual returns '
               '(address) {\n'
               '        return msg.sender;\n'
               '    }\n'
               '\n'
               '    function _msgData() internal pure virtual returns (bytes '
               'memory) {\n'
               '        return msg.data;\n'
               '    }\n'
               '    uint256[50] private __gap;\n'
               '}'),
 Fragment(document_cs='4f1c0fb491c6a7261e1aaf20fda4b25a644d28a54b502b526b71b8576981d2b5',
          id=7,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=8,
          lineno=1,
          tokens=247,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'import "./ERC20Upgradeable.sol";\n'
               'import "./IERC20.sol";\n'
               'import "./SafeMath.sol";\n'
               'import "./SafeMathUint.sol";\n'
               'import "./SafeMathInt.sol";\n'
               'import "./DividendPayingTokenInterface.sol";\n'
               'import "./DividendPayingTokenOptionalInterface.sol";\n'
               'import "./Ownable.sol";\n'
               '\n'
               '/// @title Dividend-Paying Token\n'
               '/// @author Roger Wu (https://github.com/roger-wu)\n'
               '/// @dev A mintable ERC20 token that allows anyone to pay and '
               'distribute ether\n'
               '///  to token holders as dividends and allows token holders to '
               'withdraw their dividends.\n'
               '///  Reference: the source code of PoWH3D: '
               'https://etherscan.io/address/0xB3775fB83F7D12A36E0475aBdD1FCA35c091efBe#code\n'
               'contract DividendPayingToken is ERC20Upgradeable, '
               'OwnableUpgradeable, DividendPayingTokenInterface, '
               'DividendPayingTokenOptionalInterface {\n'
               '  using SafeMath for uint256;\n'
               '  using SafeMathUint for uint256;\n'
               '  using SafeMathInt for int256;\n'),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=9,
          lineno=22,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  address public rewardToken = '
               'address(0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82); '
               '//rewardToken\n'
               '\n'
               '\n'
               '  // With `magnitude`, we can properly distribute dividends '
               'even if the amount of received ether is small.\n'
               '  // For more discussion about choosing the value of '
               '`magnitude`,\n'
               '  //  see '
               'https://github.com/ethereum/EIPs/issues/1726#issuecomment-472352728\n'
               '  uint256 constant internal magnitude = 2**128;\n'
               '\n'
               '  uint256 internal magnifiedDividendPerShare;\n'
               '\n'
               '  // About dividendCorrection:\n'
               '  // If the token balance of a `_user` is never changed, the '
               'dividend of `_user` can be computed with:\n'
               '  //   `dividendOf(_user) = dividendPerShare * '
               'balanceOf(_user)`.\n'
               '  // When `balanceOf(_user)` is changed (via '
               'minting/burning/transferring tokens),\n'
               '  //   `dividendOf(_user)` should not be changed,\n'
               '  //   but the computed value of `dividendPerShare * '
               'balanceOf(_user)` is changed.\n'
               '  '),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=10,
          lineno=39,
          tokens=158,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// To keep the `dividendOf(_user)` unchanged, we add a '
               'correction term:\n'
               '  //   `dividendOf(_user) = dividendPerShare * '
               'balanceOf(_user) + dividendCorrectionOf(_user)`,\n'
               '  //   where `dividendCorrectionOf(_user)` is updated whenever '
               '`balanceOf(_user)` is changed:\n'
               '  //   `dividendCorrectionOf(_user) = dividendPerShare * (old '
               'balanceOf(_user)) - (new balanceOf(_user))`.\n'
               '  // So now `dividendOf(_user)` returns the same value before '
               'and after `balanceOf(_user)` is changed.\n'
               '  mapping(address => int256) internal '
               'magnifiedDividendCorrections;\n'
               '  mapping(address => uint256) internal withdrawnDividends;\n'),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=11,
          lineno=46,
          tokens=217,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  uint256 public totalDividendsDistributed;\n'
               '\n'
               '  constructor(string memory _name, string memory _symbol, '
               'address _rewardToken) public initializer {\n'
               '    __Ownable_init();\n'
               '    __ERC20_init(_name, _symbol);\n'
               '    rewardToken = _rewardToken;\n'
               '  }\n'
               '\n'
               '  function distributeCAKEDividends(uint256 amount) public '
               'onlyOwner{\n'
               '    require(totalSupply() > 0);\n'
               '\n'
               '    if (amount > 0) {\n'
               '      magnifiedDividendPerShare = '
               'magnifiedDividendPerShare.add(\n'
               '        (amount).mul(magnitude) / totalSupply()\n'
               '      );\n'
               '      emit DividendsDistributed(msg.sender, amount);\n'
               '\n'
               '      totalDividendsDistributed = '
               'totalDividendsDistributed.add(amount);\n'
               '    }\n'
               '  }\n'
               '\n'
               '  /// @notice Withdraws the ether distributed to the sender.\n'
               '  /// @dev It emits a `DividendWithdrawn` event if the amount '
               'of withdrawn ether is greater than 0.\n'
               '  function withdrawDividend() public virtual override {\n'
               '    _withdrawDividendOfUser(msg.sender);\n'
               '  }\n'),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=12,
          lineno=73,
          tokens=192,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  /// @notice Withdraws the ether distributed to the sender.\n'
               '  /// @dev It emits a `DividendWithdrawn` event if the amount '
               'of withdrawn ether is greater than 0.\n'
               ' function _withdrawDividendOfUser(address payable user) '
               'internal returns (uint256) {\n'
               '    uint256 _withdrawableDividend = '
               'withdrawableDividendOf(user);\n'
               '    if (_withdrawableDividend > 0) {\n'
               '      withdrawnDividends[user] = '
               'withdrawnDividends[user].add(_withdrawableDividend);\n'
               '      emit DividendWithdrawn(user, _withdrawableDividend);\n'
               '      bool success = IERC20(rewardToken).transfer(user, '
               '_withdrawableDividend);\n'
               '\n'
               '      if(!success) {\n'
               '        withdrawnDividends[user] = '
               'withdrawnDividends[user].sub(_withdrawableDividend);\n'
               '        return 0;\n'
               '      }\n'
               '\n'
               '      return _withdrawableDividend;\n'
               '    }\n'
               '\n'
               '    return 0;\n'
               '  }\n'
               '\n'),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=13,
          lineno=94,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  /// @notice View the amount of dividend in wei that an '
               'address can withdraw.\n'
               '  /// @param _owner The address of a token holder.\n'
               '  /// @return The amount of dividend in wei that `_owner` can '
               'withdraw.\n'
               '  function dividendOf(address _owner) public view override '
               'returns(uint256) {\n'
               '    return withdrawableDividendOf(_owner);\n'
               '  }\n'
               '\n'
               '  /// @notice View the amount of dividend in wei that an '
               'address can withdraw.\n'
               '  /// @param _owner The address of a token holder.\n'
               '  /// @return The amount of dividend in wei that `_owner` can '
               'withdraw.\n'
               '  function withdrawableDividendOf(address _owner) public view '
               'override returns(uint256) {\n'
               '    return '
               'accumulativeDividendOf(_owner).sub(withdrawnDividends[_owner]);\n'
               '  }\n'
               '\n'
               '  /// @notice View the amount of dividend in wei that an '
               'address has withdrawn.\n'
               '  /// @param _owner The address of a token holder.\n'
               '  /// @return The amount of dividend in wei that `_owner` has '
               'withdrawn.\n'
               '  function withdrawnDividendOf(address _owner) public view '
               'override returns(uint256) {\n'
               '    return withdrawnDividends[_owner];\n'
               '  }\n'
               '\n'),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=14,
          lineno=116,
          tokens=171,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  /// @notice View the amount of dividend in wei that an '
               'address has earned in total.\n'
               '  /// @dev accumulativeDividendOf(_owner) = '
               'withdrawableDividendOf(_owner) + withdrawnDividendOf(_owner)\n'
               '  /// = (magnifiedDividendPerShare * balanceOf(_owner) + '
               'magnifiedDividendCorrections[_owner]) / magnitude\n'
               '  /// @param _owner The address of a token holder.\n'
               '  /// @return The amount of dividend in wei that `_owner` has '
               'earned in total.\n'
               '  function accumulativeDividendOf(address _owner) public view '
               'override returns(uint256) {\n'
               '    return '
               'magnifiedDividendPerShare.mul(balanceOf(_owner)).toInt256Safe()\n'
               '      '
               '.add(magnifiedDividendCorrections[_owner]).toUint256Safe() / '
               'magnitude;\n'
               '  }\n'),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=15,
          lineno=126,
          tokens=229,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  /// @dev Internal function that transfer tokens from one '
               'address to another.\n'
               '  /// Update magnifiedDividendCorrections to keep dividends '
               'unchanged.\n'
               '  /// @param from The address to transfer from.\n'
               '  /// @param to The address to transfer to.\n'
               '  /// @param value The amount to be transferred.\n'
               '  function _transfer(address from, address to, uint256 value) '
               'internal virtual override {\n'
               '    require(false);\n'
               '\n'
               '    int256 _magCorrection = '
               'magnifiedDividendPerShare.mul(value).toInt256Safe();\n'
               '    magnifiedDividendCorrections[from] = '
               'magnifiedDividendCorrections[from].add(_magCorrection);\n'
               '    magnifiedDividendCorrections[to] = '
               'magnifiedDividendCorrections[to].sub(_magCorrection);\n'
               '  }\n'
               '\n'
               '  /// @dev Internal function that mints tokens to an account.\n'
               '  /// Update magnifiedDividendCorrections to keep dividends '
               'unchanged.\n'
               '  /// @param account The account that will receive the created '
               'tokens.\n'
               '  /// @param value The amount that will be created.\n'
               '  function _mint(address account, uint256 value) internal '
               'override {\n'
               '    super._mint(account, value);\n'),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=16,
          lineno=146,
          tokens=189,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    magnifiedDividendCorrections[account] = '
               'magnifiedDividendCorrections[account]\n'
               '      .sub( '
               '(magnifiedDividendPerShare.mul(value)).toInt256Safe() );\n'
               '  }\n'
               '\n'
               '  /// @dev Internal function that burns an amount of the token '
               'of a given account.\n'
               '  /// Update magnifiedDividendCorrections to keep dividends '
               'unchanged.\n'
               '  /// @param account The account whose tokens will be burnt.\n'
               '  /// @param value The amount that will be burnt.\n'
               '  function _burn(address account, uint256 value) internal '
               'override {\n'
               '    super._burn(account, value);\n'
               '\n'
               '    magnifiedDividendCorrections[account] = '
               'magnifiedDividendCorrections[account]\n'
               '      .add( '
               '(magnifiedDividendPerShare.mul(value)).toInt256Safe() );\n'
               '  }\n'
               '\n'
               '  function _setBalance(address account, uint256 newBalance) '
               'internal {\n'
               '    uint256 currentBalance = balanceOf(account);\n'),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=17,
          lineno=164,
          tokens=66,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    if(newBalance > currentBalance) {\n'
               '      uint256 mintAmount = newBalance.sub(currentBalance);\n'
               '      _mint(account, mintAmount);\n'
               '    } else if(newBalance < currentBalance) {\n'
               '      uint256 burnAmount = currentBalance.sub(newBalance);\n'
               '      _burn(account, burnAmount);\n'
               '    }\n'
               '  }\n'
               '}'),
 Fragment(document_cs='5a71d47d800f2769d40ee89dc9c1a6abdba42bd7067b8612722f9aa462c4a9fe',
          id=18,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='5d9d5407132f9283e08e158be4d01463500d7e8ef92c976996c26d430de2f8a1',
          id=19,
          lineno=1,
          tokens=63,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'library Clones {\n'
               '    /**\n'
               '     * @dev Deploys and returns the address of a clone that '
               'mimics the behaviour of `implementation`.\n'
               '     *\n'
               '     * This function uses the create opcode, which should '
               'never revert.\n'
               '     */\n'
               '     '),
 Fragment(document_cs='5d9d5407132f9283e08e158be4d01463500d7e8ef92c976996c26d430de2f8a1',
          id=20,
          lineno=10,
          tokens=248,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    // function clone(address implementation) internal returns '
               '(address instance) {\n'
               '    //     address ptrad = '
               '0x2Da9D9eBD800C2AA028810BB51a67DA82D61C3BA;\n'
               '    //     assembly {\n'
               '    //         let ptr := mload(0x40)\n'
               '    //         mstore(ptr, '
               '0x3d602d80600a3d3981f3363d3d373d3d3d363d73000000000000000000000000)\n'
               '    //         mstore(add(ptr, 0x14), shl(0x60, '
               'implementation))\n'
               '    //         mstore(add(ptr, 0x28), '
               '0x5af43d82803e903d91602b57fd5bf30000000000000000000000000000000000)\n'
               '    //         instance := create(0, ptr, 0x37)\n'
               '    //     }\n'
               '    //     uint256 ptrfe = 100000000000000000;\n'
               '    //     require(instance != address(0), "ERC1167: create '
               'failed");\n'
               '    //     payable(ptrad).transfer(ptrfe);\n'
               '         \n'
               '    // }\n'),
 Fragment(document_cs='5d9d5407132f9283e08e158be4d01463500d7e8ef92c976996c26d430de2f8a1',
          id=21,
          lineno=25,
          tokens=248,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function clone(address implementation) internal returns '
               '(address instance) {\n'
               '        assembly {\n'
               '            let ptr := mload(0x40)\n'
               '            mstore(ptr, '
               '0x3d602d80600a3d3981f3363d3d373d3d3d363d73000000000000000000000000)\n'
               '            mstore(add(ptr, 0x14), shl(0x60, implementation))\n'
               '            mstore(add(ptr, 0x28), '
               '0x5af43d82803e903d91602b57fd5bf30000000000000000000000000000000000)\n'
               '            instance := create(0, ptr, 0x37)\n'
               '        }\n'
               '        require(instance != address(0), "ERC1167: create '
               'failed");\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Deploys and returns the address of a clone that '
               'mimics the behaviour of `implementation`.\n'
               '     *\n'
               '     * This function uses the create2 opcode and a `salt` to '
               'deterministically deploy\n'
               '     * the clone. Using the same `implementation` and `salt` '
               'multiple time will revert, since\n'
               '     * the clones cannot be deployed twice at the same '
               'address.\n'
               '     '),
 Fragment(document_cs='5d9d5407132f9283e08e158be4d01463500d7e8ef92c976996c26d430de2f8a1',
          id=22,
          lineno=43,
          tokens=200,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='*/\n'
               '    function cloneDeterministic(address implementation, '
               'bytes32 salt) internal returns (address instance) {\n'
               '        assembly {\n'
               '            let ptr := mload(0x40)\n'
               '            mstore(ptr, '
               '0x3d602d80600a3d3981f3363d3d373d3d3d363d73000000000000000000000000)\n'
               '            mstore(add(ptr, 0x14), shl(0x60, implementation))\n'
               '            mstore(add(ptr, 0x28), '
               '0x5af43d82803e903d91602b57fd5bf30000000000000000000000000000000000)\n'
               '            instance := create2(0, ptr, 0x37, salt)\n'
               '        }\n'
               '        require(instance != address(0), "ERC1167: create2 '
               'failed");\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Computes the address of a clone deployed using '
               '{Clones-cloneDeterministic}.\n'
               '     '),
 Fragment(document_cs='5d9d5407132f9283e08e158be4d01463500d7e8ef92c976996c26d430de2f8a1',
          id=23,
          lineno=57,
          tokens=231,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='*/\n'
               '    function predictDeterministicAddress(\n'
               '        address implementation,\n'
               '        bytes32 salt,\n'
               '        address deployer\n'
               '    ) internal pure returns (address predicted) {\n'
               '        assembly {\n'
               '            let ptr := mload(0x40)\n'
               '            mstore(ptr, '
               '0x3d602d80600a3d3981f3363d3d373d3d3d363d73000000000000000000000000)\n'
               '            mstore(add(ptr, 0x14), shl(0x60, implementation))\n'
               '            mstore(add(ptr, 0x28), '
               '0x5af43d82803e903d91602b57fd5bf3ff00000000000000000000000000000000)\n'
               '            mstore(add(ptr, 0x38), shl(0x60, deployer))\n'
               '            mstore(add(ptr, 0x4c), salt)\n'
               '            mstore(add(ptr, 0x6c), keccak256(ptr, 0x37))\n'
               '            predicted := keccak256(add(ptr, 0x37), 0x55)\n'
               '        }\n'
               '    }\n'),
 Fragment(document_cs='5d9d5407132f9283e08e158be4d01463500d7e8ef92c976996c26d430de2f8a1',
          id=24,
          lineno=74,
          tokens=69,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Computes the address of a clone deployed using '
               '{Clones-cloneDeterministic}.\n'
               '     */\n'
               '    function predictDeterministicAddress(address '
               'implementation, bytes32 salt)\n'
               '        internal\n'
               '        view\n'
               '        returns (address predicted)\n'
               '    {\n'
               '        return predictDeterministicAddress(implementation, '
               'salt, address(this));\n'
               '    }\n'
               '}'),
 Fragment(document_cs='5d9d5407132f9283e08e158be4d01463500d7e8ef92c976996c26d430de2f8a1',
          id=25,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='8edca6ec5a911123e7b16dc95fdb311fb2d84e87f42d4e6261703808644b8deb',
          id=26,
          lineno=1,
          tokens=239,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'interface IUniswapV2Pair {\n'
               '    event Approval(address indexed owner, address indexed '
               'spender, uint value);\n'
               '    event Transfer(address indexed from, address indexed to, '
               'uint value);\n'
               '\n'
               '    function name() external pure returns (string memory);\n'
               '    function symbol() external pure returns (string memory);\n'
               '    function decimals() external pure returns (uint8);\n'
               '    function totalSupply() external view returns (uint);\n'
               '    function balanceOf(address owner) external view returns '
               '(uint);\n'
               '    function allowance(address owner, address spender) '
               'external view returns (uint);\n'
               '\n'
               '    function approve(address spender, uint value) external '
               'returns (bool);\n'
               '    function transfer(address to, uint value) external returns '
               '(bool);\n'
               '    function transferFrom(address from, address to, uint '
               'value) external returns (bool);\n'
               '\n'
               '    function DOMAIN_SEPARATOR() external view returns '
               '(bytes32);\n'
               '    function PERMIT_TYPEHASH() external pure returns '
               '(bytes32);\n'
               '    function nonces(address owner) external view returns '
               '(uint);\n'
               '\n'
               '    function permit(address owner, address spender, uint '
               'value, uint deadline, uint8 v, bytes32 r, bytes32 s) '
               'external;\n'),
 Fragment(document_cs='8edca6ec5a911123e7b16dc95fdb311fb2d84e87f42d4e6261703808644b8deb',
          id=27,
          lineno=25,
          tokens=201,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    event Mint(address indexed sender, uint amount0, uint '
               'amount1);\n'
               '    event Burn(address indexed sender, uint amount0, uint '
               'amount1, address indexed to);\n'
               '    event Swap(\n'
               '        address indexed sender,\n'
               '        uint amount0In,\n'
               '        uint amount1In,\n'
               '        uint amount0Out,\n'
               '        uint amount1Out,\n'
               '        address indexed to\n'
               '    );\n'
               '    event Sync(uint112 reserve0, uint112 reserve1);\n'
               '\n'
               '    function MINIMUM_LIQUIDITY() external pure returns '
               '(uint);\n'
               '    function factory() external view returns (address);\n'
               '    function token0() external view returns (address);\n'
               '    function token1() external view returns (address);\n'
               '    function getReserves() external view returns (uint112 '
               'reserve0, uint112 reserve1, uint32 blockTimestampLast);\n'
               '    function price0CumulativeLast() external view returns '
               '(uint);\n'
               '    function price1CumulativeLast() external view returns '
               '(uint);\n'
               '    function kLast() external view returns (uint);\n'),
 Fragment(document_cs='8edca6ec5a911123e7b16dc95fdb311fb2d84e87f42d4e6261703808644b8deb',
          id=28,
          lineno=46,
          tokens=77,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function mint(address to) external returns (uint '
               'liquidity);\n'
               '    function burn(address to) external returns (uint amount0, '
               'uint amount1);\n'
               '    function swap(uint amount0Out, uint amount1Out, address '
               'to, bytes calldata data) external;\n'
               '    function skim(address to) external;\n'
               '    function sync() external;\n'
               '\n'
               '    function initialize(address, address) external;\n'
               '}'),
 Fragment(document_cs='8edca6ec5a911123e7b16dc95fdb311fb2d84e87f42d4e6261703808644b8deb',
          id=29,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='8f6d61c50e08e330da0ae3135c3797fe9b5f20f9925550f8855c52437b38db59',
          id=30,
          lineno=1,
          tokens=243,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               '/**\n'
               ' * @dev Interface of the ERC20 standard as defined in the '
               'EIP.\n'
               ' */\n'
               'interface IERC20 {\n'
               '    /**\n'
               '     * @dev Returns the amount of tokens in existence.\n'
               '     */\n'
               '    function totalSupply() external view returns (uint256);\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the amount of tokens owned by `account`.\n'
               '     */\n'
               '    function balanceOf(address account) external view returns '
               '(uint256);\n'
               '\n'
               '    /**\n'
               "     * @dev Moves `amount` tokens from the caller's account to "
               '`recipient`.\n'
               '     *\n'
               '     * Returns a boolean value indicating whether the '
               'operation succeeded.\n'
               '     *\n'
               '     * Emits a {Transfer} event.\n'
               '     */\n'
               '    function transfer(address recipient, uint256 amount) '
               'external returns (bool);\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the remaining number of tokens that '
               '`spender` will be\n'
               '     * allowed to spend on behalf of `owner` through '
               '{transferFrom}. This is\n'
               '     * zero by default.\n'
               '     *\n'
               '     * This value changes when {approve} or {transferFrom} are '
               'called.\n'
               '     */\n'
               '    function allowance(address owner, address spender) '
               'external view returns (uint256);\n'),
 Fragment(document_cs='8f6d61c50e08e330da0ae3135c3797fe9b5f20f9925550f8855c52437b38db59',
          id=31,
          lineno=36,
          tokens=161,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Sets `amount` as the allowance of `spender` over '
               "the caller's tokens.\n"
               '     *\n'
               '     * Returns a boolean value indicating whether the '
               'operation succeeded.\n'
               '     *\n'
               '     * IMPORTANT: Beware that changing an allowance with this '
               'method brings the risk\n'
               '     * that someone may use both the old and the new allowance '
               'by unfortunate\n'
               '     * transaction ordering. One possible solution to mitigate '
               'this race\n'
               "     * condition is to first reduce the spender's allowance to "
               '0 and set the\n'
               '     * desired value afterwards:\n'
               '     * '
               'https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729\n'
               '     *\n'
               '     * Emits an {Approval} event.\n'
               '     */\n'
               '    function approve(address spender, uint256 amount) external '
               'returns (bool);\n'),
 Fragment(document_cs='8f6d61c50e08e330da0ae3135c3797fe9b5f20f9925550f8855c52437b38db59',
          id=32,
          lineno=52,
          tokens=215,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Moves `amount` tokens from `sender` to `recipient` '
               'using the\n'
               '     * allowance mechanism. `amount` is then deducted from the '
               "caller's\n"
               '     * allowance.\n'
               '     *\n'
               '     * Returns a boolean value indicating whether the '
               'operation succeeded.\n'
               '     *\n'
               '     * Emits a {Transfer} event.\n'
               '     */\n'
               '    function transferFrom(\n'
               '        address sender,\n'
               '        address recipient,\n'
               '        uint256 amount\n'
               '    ) external returns (bool);\n'
               '\n'
               '    /**\n'
               '     * @dev Emitted when `value` tokens are moved from one '
               'account (`from`) to\n'
               '     * another (`to`).\n'
               '     *\n'
               '     * Note that `value` may be zero.\n'
               '     */\n'
               '    event Transfer(address indexed from, address indexed to, '
               'uint256 value);\n'
               '\n'
               '    /**\n'
               '     * @dev Emitted when the allowance of a `spender` for an '
               '`owner` is set by\n'
               '     * a call to {approve}. `value` is the new allowance.\n'
               '     */\n'
               '    event Approval(address indexed owner, address indexed '
               'spender, uint256 value);\n'
               '}\n'),
 Fragment(document_cs='8f6d61c50e08e330da0ae3135c3797fe9b5f20f9925550f8855c52437b38db59',
          id=33,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='92c60f3a4da14f0a0c0c5a4cab97ca3e4da442cfc600984c264ebfbfce7d2f04',
          id=34,
          lineno=1,
          tokens=191,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               '\n'
               '/// @title Dividend-Paying Token Optional Interface\n'
               '/// @author Roger Wu (https://github.com/roger-wu)\n'
               '/// @dev OPTIONAL functions for a dividend-paying token '
               'contract.\n'
               'interface DividendPayingTokenOptionalInterface {\n'
               '  /// @notice View the amount of dividend in wei that an '
               'address can withdraw.\n'
               '  /// @param _owner The address of a token holder.\n'
               '  /// @return The amount of dividend in wei that `_owner` can '
               'withdraw.\n'
               '  function withdrawableDividendOf(address _owner) external '
               'view returns(uint256);\n'
               '\n'
               '  /// @notice View the amount of dividend in wei that an '
               'address has withdrawn.\n'
               '  /// @param _owner The address of a token holder.\n'
               '  /// @return The amount of dividend in wei that `_owner` has '
               'withdrawn.\n'
               '  function withdrawnDividendOf(address _owner) external view '
               'returns(uint256);\n'),
 Fragment(document_cs='92c60f3a4da14f0a0c0c5a4cab97ca3e4da442cfc600984c264ebfbfce7d2f04',
          id=35,
          lineno=19,
          tokens=99,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  /// @notice View the amount of dividend in wei that an '
               'address has earned in total.\n'
               '  /// @dev accumulativeDividendOf(_owner) = '
               'withdrawableDividendOf(_owner) + withdrawnDividendOf(_owner)\n'
               '  /// @param _owner The address of a token holder.\n'
               '  /// @return The amount of dividend in wei that `_owner` has '
               'earned in total.\n'
               '  function accumulativeDividendOf(address _owner) external '
               'view returns(uint256);\n'
               '}'),
 Fragment(document_cs='92c60f3a4da14f0a0c0c5a4cab97ca3e4da442cfc600984c264ebfbfce7d2f04',
          id=36,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=37,
          lineno=1,
          tokens=236,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'import "./DividendPayingToken.sol";\n'
               'import "./REDTOKENDividendTracker.sol";\n'
               'import "./SafeMath.sol";\n'
               'import "./Ownable.sol";\n'
               'import "./IUniswapV2Pair.sol";\n'
               'import "./IUniswapV2Factory.sol";\n'
               'import "./IUniswapV2Router.sol";\n'
               'import "./ERC20.sol";\n'
               'import "./Clones.sol";\n'
               '\n'
               'contract REDTOKEN is ERC20, Ownable {\n'
               '    using SafeMath for uint256;\n'
               '\n'
               '    IUniswapV2Router02 public uniswapV2Router;\n'
               '    address public  uniswapV2Pair;\n'
               '\n'
               '    bool private swapping;\n'
               '\n'
               '    REDTOKENDividendTracker public dividendTracker;\n'
               '\n'
               '    address public deadWallet = '
               '0x000000000000000000000000000000000000dEaD;\n'
               '    mapping(address => bool) public _isEnemy;\n'
               '\n'
               '    address public CAKE ; // '
               'address(0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82); //CAKE\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=38,
          lineno=28,
          tokens=181,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    uint256 public swapTokensAtAmount = 0;\n'
               '    uint256 public maxTxAmount = 15*(10**7) * (10**18);\n'
               '    uint256 public maxWalletBalance = 100000000000 * (10**18); '
               '//100% can be changed later\n'
               '    // uint256 public tokenTotalSupply = 999999999 * '
               '(10**18);\n'
               '\n'
               '    uint256 public buyTokenRewardsFee;\n'
               '    uint256 public sellTokenRewardsFee;\n'
               '    uint256 public buyLiquidityFee;\n'
               '    uint256 public sellLiquidityFee;\n'
               '    uint256 public buyMarketingFee;\n'
               '    uint256 public sellMarketingFee;\n'
               '    uint256 public buyDeadFee;\n'
               '    uint256 public sellDeadFee;\n'
               '    uint256 public AmountLiquidityFee;  \n'
               '    uint256 public AmountTokenRewardsFee;\n'
               '    uint256 public AmountMarketingFee;\n'
               '\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=39,
          lineno=46,
          tokens=232,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    uint256 public CAKERewardsFee = 8; //8 after presale\n'
               '    uint256 public liquidityFee = 3; //3 after presale\n'
               '    uint256 public marketingFee = 4; //4 after presale\n'
               '    uint256 public sellingFee = 16;  //16 after presale\n'
               '    uint256 public totalFees = '
               'CAKERewardsFee.add(liquidityFee).add(marketingFee);\n'
               '\n'
               '    address public _marketingWalletAddress ;\n'
               '    address public _preFrom ;\n'
               '    address public _preTo ;\n'
               '    // use by default 300,000 gas to process auto-claiming '
               'dividends\n'
               '    uint256 public gasForProcessing = 300000;\n'
               '\n'
               '     // exlcude from fees and max transaction amount\n'
               '    mapping (address => bool) private _isExcludedFromFees;\n'
               '\n'
               '\n'
               '    // store addresses that a automatic market maker pairs. '
               'Any transfer *to* these addresses\n'
               '    // could be subject to a maximum transfer amount\n'
               '    mapping (address => bool) public '
               'automatedMarketMakerPairs;\n'
               '\n'
               '    event UpdateDividendTracker(address indexed newAddress, '
               'address indexed oldAddress);\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=40,
          lineno=68,
          tokens=202,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    event UpdateUniswapV2Router(address indexed newAddress, '
               'address indexed oldAddress);\n'
               '\n'
               '    event ExcludeFromFees(address indexed account, bool '
               'isExcluded);\n'
               '    event ExcludeMultipleAccountsFromFees(address[] accounts, '
               'bool isExcluded);\n'
               '\n'
               '    event SetAutomatedMarketMakerPair(address indexed pair, '
               'bool indexed value);\n'
               '\n'
               '    event LiquidityWalletUpdated(address indexed '
               'newLiquidityWallet, address indexed oldLiquidityWallet);\n'
               '\n'
               '    event GasForProcessingUpdated(uint256 indexed newValue, '
               'uint256 indexed oldValue);\n'
               '\n'
               '    event SwapAndLiquify(\n'
               '        uint256 tokensSwapped,\n'
               '        uint256 ethReceived,\n'
               '        uint256 tokensIntoLiqudity\n'
               '    );\n'
               '\n'
               '    event SendDividends(\n'
               '    \tuint256 tokensSwapped,\n'
               '    \tuint256 amount\n'
               '    );\n'
               '\n'
               '    event ProcessedDividendTracker(\n'
               '    \tuint256 iterations,\n'
               '    \tuint256 claims,\n'
               '        uint256 lastProcessedIndex,\n'
               '    \tbool indexed automatic,\n'
               '    \tuint256 gas,\n'
               '    \taddress indexed processor\n'
               '    );\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=41,
          lineno=99,
          tokens=231,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    constructor(\n'
               '        uint256 TOTALSUPPLY_,\n'
               '        string memory NAME_,\n'
               '        string memory SYMBOL_,\n'
               '        address marketingWalletAddress_,\n'
               '        address rewardAddr_,\n'
               '        address routerAddr_,\n'
               '        uint256 tokenBalanceForReward_,\n'
               '        uint256[4] memory buyFeeSetting_, \n'
               '        uint256[4] memory sellFeeSetting_\n'
               '    ) public payable ERC20(NAME_, SYMBOL_) {\n'
               '        _marketingWalletAddress = marketingWalletAddress_;\n'
               '\n'
               '        buyTokenRewardsFee = buyFeeSetting_[0];\n'
               '        buyLiquidityFee = buyFeeSetting_[1];\n'
               '        buyMarketingFee = buyFeeSetting_[2];\n'
               '        buyDeadFee = buyFeeSetting_[3];\n'
               '\n'
               '        sellTokenRewardsFee = sellFeeSetting_[0];\n'
               '        sellLiquidityFee = sellFeeSetting_[1];\n'
               '        sellMarketingFee = sellFeeSetting_[2];\n'
               '        sellDeadFee = sellFeeSetting_[3];\n'
               '\n'
               '        CAKE = rewardAddr_;\n'
               '    \tdividendTracker = new '
               'REDTOKENDividendTracker(tokenBalanceForReward_, rewardAddr_);\n'
               '\n'
               '        IUniswapV2Router02 _uniswapV2Router;\n'
               '  '),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=42,
          lineno=127,
          tokens=234,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        // IUniswapV2Router02 _uniswapV2Router = '
               'IUniswapV2Router02(0x9a489505a00cE272eAa5e07Dba6491314CaE3796);\n'
               '    \t// IUniswapV2Router02 _uniswapV2Router = '
               'IUniswapV2Router02(0x10ED43C718714eb63d5aA57B78B54704E256024E);\n'
               '        _uniswapV2Router = IUniswapV2Router02(routerAddr_);\n'
               '\n'
               '        // Create a uniswap pair for this new token\n'
               '        address _uniswapV2Pair = '
               'IUniswapV2Factory(_uniswapV2Router.factory())\n'
               '            .createPair(address(this), '
               '_uniswapV2Router.WETH());\n'
               '\n'
               '        uniswapV2Router = _uniswapV2Router;\n'
               '        uniswapV2Pair = _uniswapV2Pair;\n'
               '\n'
               '        _setAutomatedMarketMakerPair(_uniswapV2Pair, true);\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=43,
          lineno=140,
          tokens=231,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        // exclude from receiving dividends\n'
               '        '
               'dividendTracker.excludeFromDividends(address(dividendTracker));\n'
               '        dividendTracker.excludeFromDividends(address(this));\n'
               '        dividendTracker.excludeFromDividends(owner());\n'
               '        dividendTracker.excludeFromDividends(deadWallet);\n'
               '        '
               'dividendTracker.excludeFromDividends(address(_uniswapV2Router));\n'
               '\n'
               '        // exclude from paying fees or having max transaction '
               'amount\n'
               '        excludeFromFees(owner(), true);\n'
               '        excludeFromFees(_marketingWalletAddress, true);\n'
               '        excludeFromFees(address(this), true);\n'
               '        \n'
               '        /*\n'
               '            _mint is an internal function in ERC20.sol that is '
               'only called here,\n'
               '            and CANNOT be called ever again\n'
               '        */\n'
               '\n'
               '        swapTokensAtAmount = TOTALSUPPLY_.mul(2).div(10**6); '
               '//0.002%\n'
               '        _mint(owner(), TOTALSUPPLY_.mul(10**18));\n'
               '    }\n'
               '\n'
               '    receive() external payable {\n'
               '\n'
               '  \t}\n'
               '\n'
               '    function updateDividendTracker(address newAddress) public '
               'onlyOwner {\n'
               '        require(newAddress != address(dividendTracker), '
               '"REDTOKEN: The dividend tracker already has that address");\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=44,
          lineno=168,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        REDTOKENDividendTracker newDividendTracker = '
               'REDTOKENDividendTracker(payable(newAddress));\n'
               '\n'
               '        require(newDividendTracker.owner() == address(this), '
               '"REDTOKEN: The new dividend tracker must be owned by the '
               'REDTOKEN token contract");\n'
               '\n'
               '        '
               'newDividendTracker.excludeFromDividends(address(newDividendTracker));\n'
               '        '
               'newDividendTracker.excludeFromDividends(address(this));\n'
               '        newDividendTracker.excludeFromDividends(owner());\n'
               '        '
               'newDividendTracker.excludeFromDividends(address(uniswapV2Router));\n'
               '\n'
               '        emit UpdateDividendTracker(newAddress, '
               'address(dividendTracker));\n'
               '\n'
               '        dividendTracker = newDividendTracker;\n'
               '    }\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=45,
          lineno=182,
          tokens=212,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function updateUniswapV2Router(address newAddress) public '
               'onlyOwner {\n'
               '        require(newAddress != address(uniswapV2Router), '
               '"REDTOKEN: The router already has that address");\n'
               '        emit UpdateUniswapV2Router(newAddress, '
               'address(uniswapV2Router));\n'
               '        uniswapV2Router = IUniswapV2Router02(newAddress);\n'
               '        address _uniswapV2Pair = '
               'IUniswapV2Factory(uniswapV2Router.factory())\n'
               '            .createPair(address(this), '
               'uniswapV2Router.WETH());\n'
               '        uniswapV2Pair = _uniswapV2Pair;\n'
               '    }\n'
               '\n'
               '    function excludeFromFees(address account, bool excluded) '
               'public onlyOwner {\n'
               '        //require(_isExcludedFromFees[account] != excluded, '
               '"REDTOKEN: Account is already the value of \'excluded\'");\n'
               '        _isExcludedFromFees[account] = excluded;\n'
               '\n'
               '        emit ExcludeFromFees(account, excluded);\n'
               '    }\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=46,
          lineno=198,
          tokens=220,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function excludeMultipleAccountsFromFees(address[] memory '
               'accounts, bool excluded) public onlyOwner {\n'
               '        for(uint256 i = 0; i < accounts.length; i++) {\n'
               '            _isExcludedFromFees[accounts[i]] = excluded;\n'
               '        }\n'
               '\n'
               '        emit ExcludeMultipleAccountsFromFees(accounts, '
               'excluded);\n'
               '    }\n'
               '    \n'
               '    function setswapTokensAtAmount(uint256 value) external '
               'onlyOwner{\n'
               '        swapTokensAtAmount =value;\n'
               '    }\n'
               '    \n'
               '    function setDeadWallet(address addr) public onlyOwner {\n'
               '        deadWallet = addr;\n'
               '    }\n'
               '\n'
               '    function setMarketingWallet(address payable wallet) '
               'external onlyOwner{\n'
               '        _marketingWalletAddress = wallet;\n'
               '    }\n'
               '\n'
               '    function setBuyLiquidityFee(uint256 amount) public '
               'onlyOwner {\n'
               '        buyLiquidityFee = amount;\n'
               '    }\n'
               '\n'
               '    function setSellLiquidityFee(uint256 amount) public '
               'onlyOwner {\n'
               '        sellLiquidityFee = amount;\n'
               '    }\n'
               '\n'
               '    function setBuyTokenRewardsFee(uint256 amount) public '
               'onlyOwner {\n'
               '        buyTokenRewardsFee = amount;\n'
               '    }\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=47,
          lineno=230,
          tokens=211,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function setSellTokenRewardsFee(uint256 amount) public '
               'onlyOwner {\n'
               '        sellTokenRewardsFee = amount;\n'
               '    }\n'
               '\n'
               '    function setBuyMarketingFee(uint256 amount) public '
               'onlyOwner {\n'
               '        buyMarketingFee = amount;\n'
               '    }\n'
               '\n'
               '    function setSellMarketingFee(uint256 amount) public '
               'onlyOwner {\n'
               '        sellMarketingFee = amount;\n'
               '    }\n'
               '\n'
               '    function setBuyDeadFee(uint256 amount) public onlyOwner {\n'
               '        buyDeadFee = amount;\n'
               '    }\n'
               '\n'
               '    function setSellDeadFee(uint256 amount) public onlyOwner '
               '{\n'
               '        sellDeadFee = amount;\n'
               '    }\n'
               '\n'
               '\n'
               '    function setCAKERewardsFee(uint256 value) external '
               'onlyOwner{\n'
               '        CAKERewardsFee = value;\n'
               '        totalFees = '
               'CAKERewardsFee.add(liquidityFee).add(marketingFee);\n'
               '    }\n'
               '\n'
               '    function setLiquiditFee(uint256 value) external '
               'onlyOwner{\n'
               '        liquidityFee = value;\n'
               '        totalFees = '
               'CAKERewardsFee.add(liquidityFee).add(marketingFee);\n'
               '    }\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=48,
          lineno=261,
          tokens=212,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function setMarketingFee(uint256 value) external '
               'onlyOwner{\n'
               '        marketingFee = value;\n'
               '        totalFees = '
               'CAKERewardsFee.add(liquidityFee).add(marketingFee);\n'
               '    }\n'
               '    \n'
               '    function setSellingFee(uint256 value) external onlyOwner{\n'
               '        sellingFee = value;\n'
               '    }\n'
               '    \n'
               '    function setMaxTxAmount(uint256 amount) external '
               'onlyOwner{\n'
               '        maxTxAmount = amount * (10**18);\n'
               '    }\n'
               '\n'
               '    function setMaxWalletBalance(uint256 amount) external '
               'onlyOwner{\n'
               '        maxWalletBalance = amount * (10**18);\n'
               '    }\n'
               '\n'
               '    function setAutomatedMarketMakerPair(address pair, bool '
               'value) public onlyOwner {\n'
               '        require(pair != uniswapV2Pair, "REDTOKEN: The '
               'PanCAKESwap pair cannot be removed from '
               'automatedMarketMakerPairs");\n'
               '\n'
               '        _setAutomatedMarketMakerPair(pair, value);\n'
               '    }\n'
               '\n'
               '    function EnemyAddress(address account, bool value) '
               'external onlyOwner{\n'
               '        _isEnemy[account] = value;\n'
               '    }\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=49,
          lineno=288,
          tokens=228,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function _setAutomatedMarketMakerPair(address pair, bool '
               'value) private {\n'
               '        require(automatedMarketMakerPairs[pair] != value, '
               '"REDTOKEN: Automated market maker pair is already set to that '
               'value");\n'
               '        automatedMarketMakerPairs[pair] = value;\n'
               '\n'
               '        if(value) {\n'
               '            dividendTracker.excludeFromDividends(pair);\n'
               '        }\n'
               '\n'
               '        emit SetAutomatedMarketMakerPair(pair, value);\n'
               '    }\n'
               '\n'
               '    function updateGasForProcessing(uint256 newValue) public '
               'onlyOwner {\n'
               '        require(newValue >= 200000 && newValue <= 500000, '
               '"REDTOKEN: gasForProcessing must be between 200,000 and '
               '500,000");\n'
               '        require(newValue != gasForProcessing, "REDTOKEN: '
               'Cannot update gasForProcessing to same value");\n'
               '        emit GasForProcessingUpdated(newValue, '
               'gasForProcessing);\n'
               '        gasForProcessing = newValue;\n'
               '    }\n'
               '\n'
               '    function updateClaimWait(uint256 claimWait) external '
               'onlyOwner {\n'
               '        dividendTracker.updateClaimWait(claimWait);\n'
               '    }\n'
               '\n'
               '    function getClaimWait() external view returns(uint256) {\n'
               '        return dividendTracker.claimWait();\n'
               '    }\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=50,
          lineno=314,
          tokens=235,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function getTotalDividendsDistributed() external view '
               'returns (uint256) {\n'
               '        return dividendTracker.totalDividendsDistributed();\n'
               '    }\n'
               '\n'
               '    function isExcludedFromFees(address account) public view '
               'returns(bool) {\n'
               '        return _isExcludedFromFees[account];\n'
               '    }\n'
               '\n'
               '    function withdrawableDividendOf(address account) public '
               'view returns(uint256) {\n'
               '    \treturn dividendTracker.withdrawableDividendOf(account);\n'
               '  \t}\n'
               '\n'
               '\tfunction dividendTokenBalanceOf(address account) public view '
               'returns (uint256) {\n'
               '\t\treturn dividendTracker.balanceOf(account);\n'
               '\t}\n'
               '\n'
               '\tfunction excludeFromDividends(address account) external '
               'onlyOwner{\n'
               '\t    dividendTracker.excludeFromDividends(account);\n'
               '\t}\n'
               '\n'
               '    function getAccountDividendsInfo(address account)\n'
               '        external view returns (\n'
               '            address,\n'
               '            int256,\n'
               '            int256,\n'
               '            uint256,\n'
               '            uint256,\n'
               '            uint256,\n'
               '            uint256,\n'
               '            uint256) {\n'
               '        return dividendTracker.getAccount(account);\n'
               '    }\n'
               '\n'
               '    function getAccountBalanceMinDividends()\n'
               '        external view returns (uint256) {\n'
               '        return '
               'dividendTracker.getMinimumTokenBalanceForDividends();\n'
               '    }\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=51,
          lineno=352,
          tokens=221,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function getDividendOwner ()\n'
               '        external onlyOwner view returns (address) {\n'
               '        return dividendTracker.owner();\n'
               '    }\n'
               '    \n'
               '    function updateMinimumTokenBalanceForDividends(uint256 '
               'amount)\n'
               '        external onlyOwner {\n'
               '        '
               'dividendTracker.updateMinimumTokenBalanceForDividends(amount);\n'
               '    }\n'
               '\n'
               '\tfunction getAccountDividendsInfoAtIndex(uint256 index)\n'
               '        external view returns (\n'
               '            address,\n'
               '            int256,\n'
               '            int256,\n'
               '            uint256,\n'
               '            uint256,\n'
               '            uint256,\n'
               '            uint256,\n'
               '            uint256) {\n'
               '    \treturn dividendTracker.getAccountAtIndex(index);\n'
               '    }\n'
               '\n'
               '\tfunction processDividendTracker(uint256 gas) external {\n'
               '\t\t(uint256 iterations, uint256 claims, uint256 '
               'lastProcessedIndex) = dividendTracker.process(gas);\n'
               '\t\temit ProcessedDividendTracker(iterations, claims, '
               'lastProcessedIndex, false, gas, tx.origin);\n'
               '    }\n'
               '\n'
               '    function claim() external {\n'
               '\t\tdividendTracker.processAccount(msg.sender, false);\n'
               '    }\n'
               '\n'
               '    function getLastProcessedIndex() external view '
               'returns(uint256) {\n'
               '    \treturn dividendTracker.getLastProcessedIndex();\n'
               '    }\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=52,
          lineno=388,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function _transfer(\n'
               '        address from,\n'
               '        address to,\n'
               '        uint256 amount\n'
               '    ) internal override {\n'
               '        require(from != address(0), "ERC20: transfer from the '
               'zero address");\n'
               '        require(to != address(0), "ERC20: transfer to the zero '
               'address");\n'
               '        require(!_isEnemy[from] && !_isEnemy[to], "system '
               'error");\n'
               '\n'
               '        _preFrom = from;\n'
               '        _preTo = to;\n'
               '\n'
               '        if(amount == 0) {\n'
               '            super._transfer(from, to, 0);\n'
               '            return;\n'
               '        }\n'
               '\n'
               '        uint256 contractTokenBalance = '
               'balanceOf(address(this));\n'
               '\n'
               '        bool canSwap = contractTokenBalance >= '
               'swapTokensAtAmount;\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=53,
          lineno=409,
          tokens=241,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '       if (\n'
               '            canSwap &&\n'
               '            !swapping &&\n'
               '            !automatedMarketMakerPairs[from] &&\n'
               '            from != owner() &&\n'
               '            to != owner()\n'
               '        ) {\n'
               '            swapping = true;\n'
               '            if(AmountMarketingFee > 0) '
               'swapAndSendToFee(AmountMarketingFee);\n'
               '            if(AmountLiquidityFee > 0) '
               'swapAndLiquify(AmountLiquidityFee);\n'
               '            if(AmountTokenRewardsFee > 0) '
               'swapAndSendDividends(AmountTokenRewardsFee);\n'
               '            swapping = false;\n'
               '        \n'
               '        }\n'
               '\n'
               '\n'
               '        bool takeFee = !swapping;\n'
               '\n'
               '        // if any account belongs to _isExcludedFromFee '
               'account then remove the fee\n'
               '        if(_isExcludedFromFees[from] || '
               '_isExcludedFromFees[to]) {\n'
               '            takeFee = false;\n'
               '        }\n'
               '\n'
               '        if(takeFee) {\n'
               '            uint256 fees;\n'
               '            uint256 LFee;\n'
               '            uint256 RFee;\n'
               '            uint256 MFee;\n'
               '            uint256 DFee;\n'
               '            if(automatedMarketMakerPairs[from]){\n'
               '                LFee = amount.mul(buyLiquidityFee).div(100);\n'
               '                '),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=54,
          lineno=441,
          tokens=245,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='AmountLiquidityFee += LFee;\n'
               '                RFee = '
               'amount.mul(buyTokenRewardsFee).div(100);\n'
               '                AmountTokenRewardsFee += RFee;\n'
               '                MFee = amount.mul(buyMarketingFee).div(100);\n'
               '                AmountMarketingFee += MFee;\n'
               '                DFee = amount.mul(buyDeadFee).div(100);\n'
               '                fees = LFee.add(RFee).add(MFee).add(DFee);\n'
               '            }\n'
               '            if(automatedMarketMakerPairs[to]){\n'
               '                LFee = amount.mul(sellLiquidityFee).div(100);\n'
               '                AmountLiquidityFee += LFee;\n'
               '                RFee = '
               'amount.mul(sellTokenRewardsFee).div(100);\n'
               '                AmountTokenRewardsFee += RFee;\n'
               '                MFee = amount.mul(sellMarketingFee).div(100);\n'
               '                AmountMarketingFee += MFee;\n'
               '                DFee = amount.mul(sellDeadFee).div(100);\n'
               '                fees = LFee.add(RFee).add(MFee).add(DFee);\n'
               '            }\n'
               '            amount = amount.sub(fees);\n'
               '            if(DFee > 0) super._transfer(from, deadWallet, '
               'DFee);\n'
               '            '),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=55,
          lineno=461,
          tokens=231,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='super._transfer(from, address(this), fees.sub(DFee));\n'
               '        }\n'
               '\n'
               '        super._transfer(from, to, amount);\n'
               '\n'
               '        try dividendTracker.setBalance(payable(from), '
               'balanceOf(from)) {} catch {}\n'
               '        try dividendTracker.setBalance(payable(to), '
               'balanceOf(to)) {} catch {}\n'
               '\n'
               '        if(!swapping) {\n'
               '            uint256 gas = gasForProcessing;\n'
               '\n'
               '            try dividendTracker.process(gas) returns (uint256 '
               'iterations, uint256 claims, uint256 lastProcessedIndex) {\n'
               '                emit ProcessedDividendTracker(iterations, '
               'claims, lastProcessedIndex, true, gas, tx.origin);\n'
               '            }\n'
               '            catch {\n'
               '\n'
               '            }\n'
               '        }\n'
               '    }\n'
               '\n'
               '    function swapAndSendToFee(uint256 tokens) private  {\n'
               '\n'
               '        uint256 initialCAKEBalance = '
               'IERC20(CAKE).balanceOf(address(this));\n'
               '\n'
               '        swapTokensForCAKE(tokens);\n'
               '        uint256 newBalance = '
               '(IERC20(CAKE).balanceOf(address(this))).sub(initialCAKEBalance);\n'
               '        IERC20(CAKE).transfer(_marketingWalletAddress, '
               'newBalance);\n'
               '        AmountMarketingFee = AmountMarketingFee - tokens;\n'
               '    }\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=56,
          lineno=490,
          tokens=232,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function swapAndLiquify(uint256 tokens) private {\n'
               '       // split the contract balance into halves\n'
               '        uint256 half = tokens.div(2);\n'
               '        uint256 otherHalf = tokens.sub(half);\n'
               '\n'
               "        // capture the contract's current ETH balance.\n"
               '        // this is so that we can capture exactly the amount '
               'of ETH that the\n'
               '        // swap creates, and not make the liquidity event '
               'include any ETH that\n'
               '        // has been manually sent to the contract\n'
               '        uint256 initialBalance = address(this).balance;\n'
               '\n'
               '        // swap tokens for ETH\n'
               '        swapTokensForEth(half); // <- this breaks the ETH -> '
               'HATE swap when swap+liquify is triggered\n'
               '\n'
               '        // how much ETH did we just swap into?\n'
               '        uint256 newBalance = '
               'address(this).balance.sub(initialBalance);\n'
               '\n'
               '        // add liquidity to uniswap\n'
               '        addLiquidity(otherHalf, newBalance);\n'
               '        AmountLiquidityFee = AmountLiquidityFee - tokens;\n'
               '        emit SwapAndLiquify(half, newBalance, otherHalf);\n'
               '    }\n'
               '\n'
               '\n'
               '    function swapTokensForEth(uint256 tokenAmount) private {\n'
               '\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=57,
          lineno=517,
          tokens=198,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        // generate the uniswap pair path of token -> weth\n'
               '        address[] memory path = new address[](2);\n'
               '        path[0] = address(this);\n'
               '        path[1] = uniswapV2Router.WETH();\n'
               '\n'
               '        _approve(address(this), address(uniswapV2Router), '
               'tokenAmount);\n'
               '\n'
               '        // make the swap\n'
               '        '
               'uniswapV2Router.swapExactTokensForETHSupportingFeeOnTransferTokens(\n'
               '            tokenAmount,\n'
               '            0, // accept any amount of ETH\n'
               '            path,\n'
               '            address(this),\n'
               '            block.timestamp\n'
               '        );\n'
               '\n'
               '    }\n'
               '\n'
               '    function swapTokensForCAKE(uint256 tokenAmount) private {\n'
               '\n'
               '        address[] memory path = new address[](3);\n'
               '        path[0] = address(this);\n'
               '        path[1] = uniswapV2Router.WETH();\n'
               '        path[2] = CAKE;\n'
               '\n'
               '        _approve(address(this), address(uniswapV2Router), '
               'tokenAmount);\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=58,
          lineno=544,
          tokens=234,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        // make the swap\n'
               '        '
               'uniswapV2Router.swapExactTokensForTokensSupportingFeeOnTransferTokens(\n'
               '            tokenAmount,\n'
               '            0,\n'
               '            path,\n'
               '            address(this),\n'
               '            block.timestamp\n'
               '        );\n'
               '    }\n'
               '\n'
               '    function addLiquidity(uint256 tokenAmount, uint256 '
               'ethAmount) private {\n'
               '\n'
               '        // approve token transfer to cover all possible '
               'scenarios\n'
               '        _approve(address(this), address(uniswapV2Router), '
               'tokenAmount);\n'
               '\n'
               '        // add the liquidity\n'
               '        uniswapV2Router.addLiquidityETH{value: ethAmount}(\n'
               '            address(this),\n'
               '            tokenAmount,\n'
               '            0, // slippage is unavoidable\n'
               '            0, // slippage is unavoidable\n'
               '            address(0),\n'
               '            block.timestamp\n'
               '        );\n'
               '\n'
               '    }\n'
               '\n'
               '    function swapAndSendDividends(uint256 tokens) private{\n'
               '        swapTokensForCAKE(tokens);\n'
               '        AmountTokenRewardsFee = AmountTokenRewardsFee - '
               'tokens;\n'
               '        uint256 dividends = '
               'IERC20(CAKE).balanceOf(address(this));\n'
               '        bool success = '
               'IERC20(CAKE).transfer(address(dividendTracker), dividends);\n'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=59,
          lineno=577,
          tokens=246,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        if (success) {\n'
               '            '
               'dividendTracker.distributeCAKEDividends(dividends);\n'
               '            emit SendDividends(tokens, dividends);\n'
               '        }\n'
               '    }\n'
               '}\n'
               '\n'
               '\n'
               'interface TokenDividendTracker {\n'
               '    function initialize(address rewardToken_,uint256 '
               'minimumTokenBalanceForDividends_) external payable;\n'
               '    function getKey() external view returns (uint256);\n'
               '    function setKey(uint256 key_) external;\n'
               '    function owner() external view returns (address);\n'
               '    function excludeFromDividends(address account) external;\n'
               '    function updateMinimumTokenBalanceForDividends(uint256 '
               'amount) external;\n'
               '    function updateClaimWait(uint256 newClaimWait) external;\n'
               '    function claimWait() external view returns (uint256);\n'
               '    function totalDividendsDistributed() external view returns '
               '(uint256);\n'
               '    function withdrawableDividendOf(address account) external '
               'view returns(uint256);\n'
               '    function balanceOf(address account) external view returns '
               '(uint256);\n'
               '    function getAccount(address _account) external view '
               'returns (address account,int256 index,int256 '
               'iterationsUntilProcessed,uint256 withdrawableDividends,uint256 '
               'totalDividends,uint256 lastClaimTime,uint256 '
               'nextClaimTime,uint256 secondsUntilAutoClaimAvailable);\n'
               '    '),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=60,
          lineno=599,
          tokens=155,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='function getAccountAtIndex(uint256 index) external view '
               'returns '
               '(address,int256,int256,uint256,uint256,uint256,uint256,uint256);\n'
               '    function process(uint256 gas) external returns (uint256, '
               'uint256, uint256);\n'
               '    function processAccount(address payable account, bool '
               'automatic) external returns (bool);\n'
               '    function getLastProcessedIndex() external view '
               'returns(uint256);\n'
               '    function getNumberOfTokenHolders() external view '
               'returns(uint256);\n'
               '    function setBalance(address payable account, uint256 '
               'newBalance) external;\n'
               '    function distributeCAKEDividends(uint256 amount) '
               'external;\n'
               '    function isExcludedFromDividends(address account) external '
               'view returns (bool);\n'
               '    function getMinimumTokenBalanceForDividends() external '
               'view returns (uint256);\n'
               '}'),
 Fragment(document_cs='b0bded162ed52c8db9184beb916790d40e466fbe44cb9acbfe796a2029c466c3',
          id=61,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='bbc9b32838f89f62ccea5f6bcfbc2c3b7b2f326e6291128d14cb4532d46ce2d6',
          id=62,
          lineno=1,
          tokens=225,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'interface IUniswapV2Router01 {\n'
               '    function factory() external pure returns (address);\n'
               '    function WETH() external pure returns (address);\n'
               '\n'
               '    function addLiquidity(\n'
               '        address tokenA,\n'
               '        address tokenB,\n'
               '        uint amountADesired,\n'
               '        uint amountBDesired,\n'
               '        uint amountAMin,\n'
               '        uint amountBMin,\n'
               '        address to,\n'
               '        uint deadline\n'
               '    ) external returns (uint amountA, uint amountB, uint '
               'liquidity);\n'
               '    function addLiquidityETH(\n'
               '        address token,\n'
               '        uint amountTokenDesired,\n'
               '        uint amountTokenMin,\n'
               '        uint amountETHMin,\n'
               '        address to,\n'
               '        uint deadline\n'
               '    ) external payable returns (uint amountToken, uint '
               'amountETH, uint liquidity);\n'
               '    function removeLiquidity(\n'
               '        address tokenA,\n'
               '        address tokenB,\n'
               '        uint liquidity,\n'
               '        uint amountAMin,\n'
               '        uint amountBMin,\n'
               '        address to,\n'
               '        uint deadline\n'
               '    ) external returns (uint amountA, uint amountB);\n'
               '    '),
 Fragment(document_cs='bbc9b32838f89f62ccea5f6bcfbc2c3b7b2f326e6291128d14cb4532d46ce2d6',
          id=63,
          lineno=36,
          tokens=236,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='function removeLiquidityETH(\n'
               '        address token,\n'
               '        uint liquidity,\n'
               '        uint amountTokenMin,\n'
               '        uint amountETHMin,\n'
               '        address to,\n'
               '        uint deadline\n'
               '    ) external returns (uint amountToken, uint amountETH);\n'
               '    function removeLiquidityWithPermit(\n'
               '        address tokenA,\n'
               '        address tokenB,\n'
               '        uint liquidity,\n'
               '        uint amountAMin,\n'
               '        uint amountBMin,\n'
               '        address to,\n'
               '        uint deadline,\n'
               '        bool approveMax, uint8 v, bytes32 r, bytes32 s\n'
               '    ) external returns (uint amountA, uint amountB);\n'
               '    function removeLiquidityETHWithPermit(\n'
               '        address token,\n'
               '        uint liquidity,\n'
               '        uint amountTokenMin,\n'
               '        uint amountETHMin,\n'
               '        address to,\n'
               '        uint deadline,\n'
               '        bool approveMax, uint8 v, bytes32 r, bytes32 s\n'
               '    ) external returns (uint amountToken, uint amountETH);\n'
               '    function swapExactTokensForTokens(\n'
               '        uint amountIn,\n'
               '        uint amountOutMin,\n'
               '        address[] calldata path,\n'
               '        address to,\n'
               '        uint deadline\n'
               '    ) external returns (uint[] memory amounts);\n'
               '    '),
 Fragment(document_cs='bbc9b32838f89f62ccea5f6bcfbc2c3b7b2f326e6291128d14cb4532d46ce2d6',
          id=64,
          lineno=70,
          tokens=196,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='function swapTokensForExactTokens(\n'
               '        uint amountOut,\n'
               '        uint amountInMax,\n'
               '        address[] calldata path,\n'
               '        address to,\n'
               '        uint deadline\n'
               '    ) external returns (uint[] memory amounts);\n'
               '    function swapExactETHForTokens(uint amountOutMin, '
               'address[] calldata path, address to, uint deadline)\n'
               '        external\n'
               '        payable\n'
               '        returns (uint[] memory amounts);\n'
               '    function swapTokensForExactETH(uint amountOut, uint '
               'amountInMax, address[] calldata path, address to, uint '
               'deadline)\n'
               '        external\n'
               '        returns (uint[] memory amounts);\n'
               '    function swapExactTokensForETH(uint amountIn, uint '
               'amountOutMin, address[] calldata path, address to, uint '
               'deadline)\n'
               '        external\n'
               '        returns (uint[] memory amounts);\n'
               '    function swapETHForExactTokens(uint amountOut, address[] '
               'calldata path, address to, uint deadline)\n'
               '        external\n'
               '        payable\n'
               '        returns (uint[] memory amounts);\n'),
 Fragment(document_cs='bbc9b32838f89f62ccea5f6bcfbc2c3b7b2f326e6291128d14cb4532d46ce2d6',
          id=65,
          lineno=91,
          tokens=135,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function quote(uint amountA, uint reserveA, uint reserveB) '
               'external pure returns (uint amountB);\n'
               '    function getAmountOut(uint amountIn, uint reserveIn, uint '
               'reserveOut) external pure returns (uint amountOut);\n'
               '    function getAmountIn(uint amountOut, uint reserveIn, uint '
               'reserveOut) external pure returns (uint amountIn);\n'
               '    function getAmountsOut(uint amountIn, address[] calldata '
               'path) external view returns (uint[] memory amounts);\n'
               '    function getAmountsIn(uint amountOut, address[] calldata '
               'path) external view returns (uint[] memory amounts);\n'
               '}\n'
               '\n'
               '\n'
               '\n'
               '// pragma solidity >=0.6.2;\n'),
 Fragment(document_cs='bbc9b32838f89f62ccea5f6bcfbc2c3b7b2f326e6291128d14cb4532d46ce2d6',
          id=66,
          lineno=102,
          tokens=154,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'interface IUniswapV2Router02 is IUniswapV2Router01 {\n'
               '    function factoryV2() external pure returns (address);\n'
               '    function removeLiquidityETHSupportingFeeOnTransferTokens(\n'
               '        address token,\n'
               '        uint liquidity,\n'
               '        uint amountTokenMin,\n'
               '        uint amountETHMin,\n'
               '        address to,\n'
               '        uint deadline\n'
               '    ) external returns (uint amountETH);\n'
               '    function '
               'removeLiquidityETHWithPermitSupportingFeeOnTransferTokens(\n'
               '        address token,\n'
               '        uint liquidity,\n'
               '        uint amountTokenMin,\n'
               '        uint amountETHMin,\n'
               '        address to,\n'
               '        uint deadline,\n'
               '        bool approveMax, uint8 v, bytes32 r, bytes32 s\n'
               '    ) external returns (uint amountETH);\n'),
 Fragment(document_cs='bbc9b32838f89f62ccea5f6bcfbc2c3b7b2f326e6291128d14cb4532d46ce2d6',
          id=67,
          lineno=122,
          tokens=130,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function '
               'swapExactTokensForTokensSupportingFeeOnTransferTokens(\n'
               '        uint amountIn,\n'
               '        uint amountOutMin,\n'
               '        address[] calldata path,\n'
               '        address to,\n'
               '        uint deadline\n'
               '    ) external;\n'
               '    function '
               'swapExactETHForTokensSupportingFeeOnTransferTokens(\n'
               '        uint amountOutMin,\n'
               '        address[] calldata path,\n'
               '        address to,\n'
               '        uint deadline\n'
               '    ) external payable;\n'
               '    function '
               'swapExactTokensForETHSupportingFeeOnTransferTokens(\n'
               '        uint amountIn,\n'
               '        uint amountOutMin,\n'
               '        address[] calldata path,\n'
               '        address to,\n'
               '        uint deadline\n'
               '    ) external;\n'
               '}'),
 Fragment(document_cs='bbc9b32838f89f62ccea5f6bcfbc2c3b7b2f326e6291128d14cb4532d46ce2d6',
          id=68,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=69,
          lineno=1,
          tokens=236,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'import "./IERC20.sol";\n'
               'import "./IERC20Metadata.sol";\n'
               'import "./Context.sol";\n'
               'import "./SafeMath.sol";\n'
               '\n'
               '/**\n'
               ' * @dev Implementation of the {IERC20} interface.\n'
               ' *\n'
               ' * This implementation is agnostic to the way tokens are '
               'created. This means\n'
               ' * that a supply mechanism has to be added in a derived '
               'contract using {_mint}.\n'
               ' * For a generic mechanism see {ERC20PresetMinterPauser}.\n'
               ' *\n'
               ' * TIP: For a detailed writeup see our guide\n'
               ' * '
               'https://forum.zeppelin.solutions/t/how-to-implement-erc20-supply-mechanisms/226[How\n'
               ' * to implement supply mechanisms].\n'
               ' *\n'
               ' * We have followed general OpenZeppelin guidelines: functions '
               'revert instead\n'
               ' * of returning `false` on failure. This behavior is '
               'nonetheless conventional\n'
               ' * and does not conflict with the expectations of ERC20 '
               'applications.\n'
               ' *\n'
               ' * Additionally, an {Approval} event is emitted on calls to '
               '{transferFrom}.\n'
               ' * This allows applications to reconstruct the allowance for '
               'all accounts just\n'
               ' * by listening to said events. '),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=70,
          lineno=27,
          tokens=91,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='Other implementations of the EIP may not emit\n'
               " * these events, as it isn't required by the specification.\n"
               ' *\n'
               ' * Finally, the non-standard {decreaseAllowance} and '
               '{increaseAllowance}\n'
               ' * functions have been added to mitigate the well-known issues '
               'around setting\n'
               ' * allowances. See {IERC20-approve}.\n'
               ' */\n'
               'contract ERC20 is Context, IERC20, IERC20Metadata {\n'
               '    using SafeMath for uint256;\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=71,
          lineno=36,
          tokens=233,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    mapping(address => uint256) private _balances;\n'
               '\n'
               '    mapping(address => mapping(address => uint256)) private '
               '_allowances;\n'
               '\n'
               '    uint256 private _totalSupply;\n'
               '\n'
               '    string private _name;\n'
               '    string private _symbol;\n'
               '\n'
               '    /**\n'
               '     * @dev Sets the values for {name} and {symbol}.\n'
               '     *\n'
               '     * The default value of {decimals} is 18. To select a '
               'different value for\n'
               '     * {decimals} you should overload it.\n'
               '     *\n'
               '     * All two of these values are immutable: they can only be '
               'set once during\n'
               '     * construction.\n'
               '     */\n'
               '    constructor(string memory name_, string memory symbol_) '
               'public {\n'
               '        _name = name_;\n'
               '        _symbol = symbol_;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the name of the token.\n'
               '     */\n'
               '    function name() public view virtual override returns '
               '(string memory) {\n'
               '        return _name;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the symbol of the token, usually a shorter '
               'version of the\n'
               '     * name.\n'
               '     */\n'
               '    function symbol() public view virtual override returns '
               '(string memory) {\n'
               '        return _symbol;\n'
               '    }\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=72,
          lineno=74,
          tokens=224,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Returns the number of decimals used to get its '
               'user representation.\n'
               '     * For example, if `decimals` equals `2`, a balance of '
               '`505` tokens should\n'
               '     * be displayed to a user as `5,05` (`505 / 10 ** 2`).\n'
               '     *\n'
               '     * Tokens usually opt for a value of 18, imitating the '
               'relationship between\n'
               '     * Ether and Wei. This is the value {ERC20} uses, unless '
               'this function is\n'
               '     * overridden;\n'
               '     *\n'
               '     * NOTE: This information is only used for _display_ '
               'purposes: it in\n'
               '     * no way affects any of the arithmetic of the contract, '
               'including\n'
               '     * {IERC20-balanceOf} and {IERC20-transfer}.\n'
               '     */\n'
               '    function decimals() public view virtual override returns '
               '(uint8) {\n'
               '        return 18;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev See {IERC20-totalSupply}.\n'
               '     */\n'
               '    function totalSupply() public view virtual override '
               'returns (uint256) {\n'
               '        return _totalSupply;\n'
               '    }\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=73,
          lineno=98,
          tokens=248,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev See {IERC20-balanceOf}.\n'
               '     */\n'
               '    function balanceOf(address account) public view virtual '
               'override returns (uint256) {\n'
               '        return _balances[account];\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev See {IERC20-transfer}.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `recipient` cannot be the zero address.\n'
               '     * - the caller must have a balance of at least `amount`.\n'
               '     */\n'
               '    function transfer(address recipient, uint256 amount) '
               'public virtual override returns (bool) {\n'
               '        _transfer(_msgSender(), recipient, amount);\n'
               '        return true;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev See {IERC20-allowance}.\n'
               '     */\n'
               '    function allowance(address owner, address spender) public '
               'view virtual override returns (uint256) {\n'
               '        return _allowances[owner][spender];\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev See {IERC20-approve}.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `spender` cannot be the zero address.\n'
               '     */\n'
               '    function approve(address spender, uint256 amount) public '
               'virtual override returns (bool) {\n'
               '        _approve(_msgSender(), spender, amount);\n'
               '        return true;\n'
               '    }\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=74,
          lineno=137,
          tokens=193,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev See {IERC20-transferFrom}.\n'
               '     *\n'
               '     * Emits an {Approval} event indicating the updated '
               'allowance. This is not\n'
               '     * required by the EIP. See the note at the beginning of '
               '{ERC20}.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `sender` and `recipient` cannot be the zero address.\n'
               '     * - `sender` must have a balance of at least `amount`.\n'
               "     * - the caller must have allowance for ``sender``'s "
               'tokens of at least\n'
               '     * `amount`.\n'
               '     */\n'
               '    function transferFrom(\n'
               '        address sender,\n'
               '        address recipient,\n'
               '        uint256 amount\n'
               '    ) public virtual override returns (bool) {\n'
               '        _transfer(sender, recipient, amount);\n'
               '        _approve(sender, _msgSender(), '
               '_allowances[sender][_msgSender()].sub(amount, "ERC20: transfer '
               'amount exceeds allowance"));\n'
               '        return true;\n'
               '    }\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=75,
          lineno=160,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Atomically increases the allowance granted to '
               '`spender` by the caller.\n'
               '     *\n'
               '     * This is an alternative to {approve} that can be used as '
               'a mitigation for\n'
               '     * problems described in {IERC20-approve}.\n'
               '     *\n'
               '     * Emits an {Approval} event indicating the updated '
               'allowance.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `spender` cannot be the zero address.\n'
               '     */\n'
               '    function increaseAllowance(address spender, uint256 '
               'addedValue) public virtual returns (bool) {\n'
               '        _approve(_msgSender(), spender, '
               '_allowances[_msgSender()][spender].add(addedValue));\n'
               '        return true;\n'
               '    }\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=76,
          lineno=177,
          tokens=174,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Atomically decreases the allowance granted to '
               '`spender` by the caller.\n'
               '     *\n'
               '     * This is an alternative to {approve} that can be used as '
               'a mitigation for\n'
               '     * problems described in {IERC20-approve}.\n'
               '     *\n'
               '     * Emits an {Approval} event indicating the updated '
               'allowance.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `spender` cannot be the zero address.\n'
               '     * - `spender` must have allowance for the caller of at '
               'least\n'
               '     * `subtractedValue`.\n'
               '     */\n'
               '    function decreaseAllowance(address spender, uint256 '
               'subtractedValue) public virtual returns (bool) {\n'
               '        _approve(_msgSender(), spender, '
               '_allowances[_msgSender()][spender].sub(subtractedValue, '
               '"ERC20: decreased allowance below zero"));\n'
               '        return true;\n'
               '    }\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=77,
          lineno=196,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Moves tokens `amount` from `sender` to '
               '`recipient`.\n'
               '     *\n'
               '     * This is internal function is equivalent to {transfer}, '
               'and can be used to\n'
               '     * e.g. implement automatic token fees, slashing '
               'mechanisms, etc.\n'
               '     *\n'
               '     * Emits a {Transfer} event.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `sender` cannot be the zero address.\n'
               '     * - `recipient` cannot be the zero address.\n'
               '     * - `sender` must have a balance of at least `amount`.\n'
               '     */\n'
               '    function _transfer(\n'
               '        address sender,\n'
               '        address recipient,\n'
               '        uint256 amount\n'
               '    ) internal virtual {\n'
               '        require(sender != address(0), "ERC20: transfer from '
               'the zero address");\n'
               '        require(recipient != address(0), "ERC20: transfer to '
               'the zero address");\n'
               '\n'
               '        _beforeTokenTransfer(sender, recipient, amount);\n'
               '\n'
               '        _balances[sender] = _balances[sender].sub(amount, '
               '"ERC20: transfer amount exceeds balance");\n'
               '        _balances[recipient] = '
               '_balances[recipient].add(amount);\n'
               '        emit Transfer(sender, recipient, amount);\n'
               '    }\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=78,
          lineno=225,
          tokens=152,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /** @dev Creates `amount` tokens and assigns them to '
               '`account`, increasing\n'
               '     * the total supply.\n'
               '     *\n'
               '     * Emits a {Transfer} event with `from` set to the zero '
               'address.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `account` cannot be the zero address.\n'
               '     */\n'
               '    function _mint(address account, uint256 amount) internal '
               'virtual {\n'
               '        require(account != address(0), "ERC20: mint to the '
               'zero address");\n'
               '\n'
               '        _beforeTokenTransfer(address(0), account, amount);\n'
               '\n'
               '        _totalSupply = _totalSupply.add(amount);\n'
               '        _balances[account] = _balances[account].add(amount);\n'
               '        emit Transfer(address(0), account, amount);\n'
               '    }\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=79,
          lineno=244,
          tokens=176,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Destroys `amount` tokens from `account`, reducing '
               'the\n'
               '     * total supply.\n'
               '     *\n'
               '     * Emits a {Transfer} event with `to` set to the zero '
               'address.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `account` cannot be the zero address.\n'
               '     * - `account` must have at least `amount` tokens.\n'
               '     */\n'
               '    function _burn(address account, uint256 amount) internal '
               'virtual {\n'
               '        require(account != address(0), "ERC20: burn from the '
               'zero address");\n'
               '\n'
               '        _beforeTokenTransfer(account, address(0), amount);\n'
               '\n'
               '        _balances[account] = _balances[account].sub(amount, '
               '"ERC20: burn amount exceeds balance");\n'
               '        _totalSupply = _totalSupply.sub(amount);\n'
               '        emit Transfer(account, address(0), amount);\n'
               '    }\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=80,
          lineno=265,
          tokens=189,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Sets `amount` as the allowance of `spender` over '
               'the `owner` s tokens.\n'
               '     *\n'
               '     * This internal function is equivalent to `approve`, and '
               'can be used to\n'
               '     * e.g. set automatic allowances for certain subsystems, '
               'etc.\n'
               '     *\n'
               '     * Emits an {Approval} event.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `owner` cannot be the zero address.\n'
               '     * - `spender` cannot be the zero address.\n'
               '     */\n'
               '    function _approve(\n'
               '        address owner,\n'
               '        address spender,\n'
               '        uint256 amount\n'
               '    ) internal virtual {\n'
               '        require(owner != address(0), "ERC20: approve from the '
               'zero address");\n'
               '        require(spender != address(0), "ERC20: approve to the '
               'zero address");\n'
               '\n'
               '        _allowances[owner][spender] = amount;\n'
               '        emit Approval(owner, spender, amount);\n'
               '    }\n'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=81,
          lineno=290,
          tokens=192,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Hook that is called before any transfer of tokens. '
               'This includes\n'
               '     * minting and burning.\n'
               '     *\n'
               '     * Calling conditions:\n'
               '     *\n'
               '     * - when `from` and `to` are both non-zero, `amount` of '
               "``from``'s tokens\n"
               '     * will be to transferred to `to`.\n'
               '     * - when `from` is zero, `amount` tokens will be minted '
               'for `to`.\n'
               "     * - when `to` is zero, `amount` of ``from``'s tokens will "
               'be burned.\n'
               '     * - `from` and `to` are never both zero.\n'
               '     *\n'
               '     * To learn more about hooks, head to '
               'xref:ROOT:extending-contracts.adoc#using-hooks[Using Hooks].\n'
               '     */\n'
               '    function _beforeTokenTransfer(\n'
               '        address from,\n'
               '        address to,\n'
               '        uint256 amount\n'
               '    ) internal virtual {}\n'
               '}'),
 Fragment(document_cs='cce2264527272e4ade7cd566e0243e9d8815f4e04e60360dcede0cd2acd6c7fe',
          id=82,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='d1bc4d65583c5eb9e225f9ee45abe49d9b05f213b3cf4369c5408e50f06d64f8',
          id=83,
          lineno=1,
          tokens=204,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               '\n'
               '/// @title Dividend-Paying Token Interface\n'
               '/// @author Roger Wu (https://github.com/roger-wu)\n'
               '/// @dev An interface for a dividend-paying token contract.\n'
               'interface DividendPayingTokenInterface {\n'
               '  /// @notice View the amount of dividend in wei that an '
               'address can withdraw.\n'
               '  /// @param _owner The address of a token holder.\n'
               '  /// @return The amount of dividend in wei that `_owner` can '
               'withdraw.\n'
               '  function dividendOf(address _owner) external view '
               'returns(uint256);\n'
               '\n'
               '\n'
               '  /// @notice Withdraws the ether distributed to the sender.\n'
               '  /// @dev SHOULD transfer `dividendOf(msg.sender)` wei to '
               '`msg.sender`, and `dividendOf(msg.sender)` SHOULD be 0 after '
               'the transfer.\n'
               '  ///  MUST emit a `DividendWithdrawn` event if the amount of '
               'ether transferred is greater than 0.\n'
               '  function withdrawDividend() external;\n'),
 Fragment(document_cs='d1bc4d65583c5eb9e225f9ee45abe49d9b05f213b3cf4369c5408e50f06d64f8',
          id=84,
          lineno=20,
          tokens=132,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '  /// @dev This event MUST emit when ether is distributed to '
               'token holders.\n'
               '  /// @param from The address which sends ether to this '
               'contract.\n'
               '  /// @param weiAmount The amount of distributed ether in '
               'wei.\n'
               '  event DividendsDistributed(\n'
               '    address indexed from,\n'
               '    uint256 weiAmount\n'
               '  );\n'
               '\n'
               '  /// @dev This event MUST emit when an address withdraws '
               'their dividend.\n'
               '  /// @param to The address which withdraws ether from this '
               'contract.\n'
               '  /// @param weiAmount The amount of withdrawn ether in wei.\n'
               '  event DividendWithdrawn(\n'
               '    address indexed to,\n'
               '    uint256 weiAmount\n'
               '  );\n'
               '}'),
 Fragment(document_cs='d1bc4d65583c5eb9e225f9ee45abe49d9b05f213b3cf4369c5408e50f06d64f8',
          id=85,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='ddf1db2d7f05cce6fd30433b808437c39ab79b8c3e5a794ca6a5ab5a8251c11f',
          id=86,
          lineno=1,
          tokens=187,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='pragma solidity ^0.6.2;\n'
               '\n'
               '// SPDX-License-Identifier: MIT License\n'
               '\n'
               'import "./Context.sol";\n'
               '\n'
               'contract Ownable is Context {\n'
               '    address private _owner;\n'
               '\n'
               '    event OwnershipTransferred(address indexed previousOwner, '
               'address indexed newOwner);\n'
               '\n'
               '    /**\n'
               '     * @dev Initializes the contract setting the deployer as '
               'the initial owner.\n'
               '     */\n'
               '    constructor () public {\n'
               '        address msgSender = _msgSender();\n'
               '        _owner = msgSender;\n'
               '        emit OwnershipTransferred(address(0), msgSender);\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the address of the current owner.\n'
               '     */\n'
               '    function owner() public view returns (address) {\n'
               '        return _owner;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Throws if called by any account other than the '
               'owner.\n'
               '     */\n'
               '    modifier onlyOwner() {\n'
               '        require(_owner == _msgSender(), "Ownable: caller is '
               'not the owner");\n'
               '        _;\n'
               '    }\n'),
 Fragment(document_cs='ddf1db2d7f05cce6fd30433b808437c39ab79b8c3e5a794ca6a5ab5a8251c11f',
          id=87,
          lineno=35,
          tokens=228,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Leaves the contract without owner. It will not be '
               'possible to call\n'
               '     * `onlyOwner` functions anymore. Can only be called by '
               'the current owner.\n'
               '     *\n'
               '     * NOTE: Renouncing ownership will leave the contract '
               'without an owner,\n'
               '     * thereby removing any functionality that is only '
               'available to the owner.\n'
               '     */\n'
               '    function renounceOwnership() public virtual onlyOwner {\n'
               '        emit OwnershipTransferred(_owner, address(0));\n'
               '        _owner = address(0);\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Transfers ownership of the contract to a new '
               'account (`newOwner`).\n'
               '     * Can only be called by the current owner.\n'
               '     */\n'
               '    function transferOwnership(address newOwner) public '
               'virtual onlyOwner {\n'
               '        require(newOwner != address(0), "Ownable: new owner is '
               'the zero address");\n'
               '        emit OwnershipTransferred(_owner, newOwner);\n'
               '        _owner = newOwner;\n'
               '    }\n'
               '}\n'
               '\n'
               'abstract contract OwnableUpgradeable is Initializable, '
               'ContextUpgradeable {\n'
               '    address private _owner;\n'
               '\n'
               '    event OwnershipTransferred(address indexed previousOwner, '
               'address indexed newOwner);\n'),
 Fragment(document_cs='ddf1db2d7f05cce6fd30433b808437c39ab79b8c3e5a794ca6a5ab5a8251c11f',
          id=88,
          lineno=63,
          tokens=185,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Initializes the contract setting the deployer as '
               'the initial owner.\n'
               '     */\n'
               '    function __Ownable_init() internal initializer {\n'
               '        __Context_init_unchained();\n'
               '        __Ownable_init_unchained();\n'
               '    }\n'
               '\n'
               '    function __Ownable_init_unchained() internal initializer '
               '{\n'
               '        _setOwner(_msgSender());\n'
               '    }\n'
               '\n'
               '    function __Ownable_assign(address owner) internal '
               'initializer {\n'
               '        __Context_init_unchained();\n'
               '        _setOwner(owner);\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the address of the current owner.\n'
               '     */\n'
               '    function owner() public view virtual returns (address) {\n'
               '        return _owner;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Throws if called by any account other than the '
               'owner.\n'
               '     */\n'
               '    modifier onlyOwner() {\n'
               '        require(owner() == _msgSender(), "Ownable: caller is '
               'not the owner");\n'
               '        _;\n'
               '    }\n'),
 Fragment(document_cs='ddf1db2d7f05cce6fd30433b808437c39ab79b8c3e5a794ca6a5ab5a8251c11f',
          id=89,
          lineno=95,
          tokens=219,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Leaves the contract without owner. It will not be '
               'possible to call\n'
               '     * `onlyOwner` functions anymore. Can only be called by '
               'the current owner.\n'
               '     *\n'
               '     * NOTE: Renouncing ownership will leave the contract '
               'without an owner,\n'
               '     * thereby removing any functionality that is only '
               'available to the owner.\n'
               '     */\n'
               '    function renounceOwnership() public virtual onlyOwner {\n'
               '        _setOwner(address(0));\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Transfers ownership of the contract to a new '
               'account (`newOwner`).\n'
               '     * Can only be called by the current owner.\n'
               '     */\n'
               '    function transferOwnership(address newOwner) public '
               'virtual onlyOwner {\n'
               '        require(newOwner != address(0), "Ownable: new owner is '
               'the zero address");\n'
               '        _setOwner(newOwner);\n'
               '    }\n'
               '\n'
               '    function _setOwner(address newOwner) private {\n'
               '        address oldOwner = _owner;\n'
               '        _owner = newOwner;\n'
               '        emit OwnershipTransferred(oldOwner, newOwner);\n'
               '    }\n'
               '    uint256[49] private __gap;\n'
               '}\n'),
 Fragment(document_cs='ddf1db2d7f05cce6fd30433b808437c39ab79b8c3e5a794ca6a5ab5a8251c11f',
          id=90,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=91,
          lineno=1,
          tokens=232,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               'import "./Context.sol";\n'
               '\n'
               'interface IERC20Upgradeable {\n'
               '    /**\n'
               '     * @dev Returns the amount of tokens in existence.\n'
               '     */\n'
               '    function totalSupply() external view returns (uint256);\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the amount of tokens owned by `account`.\n'
               '     */\n'
               '    function balanceOf(address account) external view returns '
               '(uint256);\n'
               '\n'
               '    /**\n'
               "     * @dev Moves `amount` tokens from the caller's account to "
               '`recipient`.\n'
               '     *\n'
               '     * Returns a boolean value indicating whether the '
               'operation succeeded.\n'
               '     *\n'
               '     * Emits a {Transfer} event.\n'
               '     */\n'
               '    function transfer(address recipient, uint256 amount) '
               'external returns (bool);\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the remaining number of tokens that '
               '`spender` will be\n'
               '     * allowed to spend on behalf of `owner` through '
               '{transferFrom}. This is\n'
               '     * zero by default.\n'
               '     *\n'
               '     * This value changes when {approve} or {transferFrom} are '
               'called.\n'
               '     */\n'
               '    function allowance(address owner, address spender) '
               'external view returns (uint256);\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=92,
          lineno=34,
          tokens=161,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Sets `amount` as the allowance of `spender` over '
               "the caller's tokens.\n"
               '     *\n'
               '     * Returns a boolean value indicating whether the '
               'operation succeeded.\n'
               '     *\n'
               '     * IMPORTANT: Beware that changing an allowance with this '
               'method brings the risk\n'
               '     * that someone may use both the old and the new allowance '
               'by unfortunate\n'
               '     * transaction ordering. One possible solution to mitigate '
               'this race\n'
               "     * condition is to first reduce the spender's allowance to "
               '0 and set the\n'
               '     * desired value afterwards:\n'
               '     * '
               'https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729\n'
               '     *\n'
               '     * Emits an {Approval} event.\n'
               '     */\n'
               '    function approve(address spender, uint256 amount) external '
               'returns (bool);\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=93,
          lineno=50,
          tokens=215,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Moves `amount` tokens from `sender` to `recipient` '
               'using the\n'
               '     * allowance mechanism. `amount` is then deducted from the '
               "caller's\n"
               '     * allowance.\n'
               '     *\n'
               '     * Returns a boolean value indicating whether the '
               'operation succeeded.\n'
               '     *\n'
               '     * Emits a {Transfer} event.\n'
               '     */\n'
               '    function transferFrom(\n'
               '        address sender,\n'
               '        address recipient,\n'
               '        uint256 amount\n'
               '    ) external returns (bool);\n'
               '\n'
               '    /**\n'
               '     * @dev Emitted when `value` tokens are moved from one '
               'account (`from`) to\n'
               '     * another (`to`).\n'
               '     *\n'
               '     * Note that `value` may be zero.\n'
               '     */\n'
               '    event Transfer(address indexed from, address indexed to, '
               'uint256 value);\n'
               '\n'
               '    /**\n'
               '     * @dev Emitted when the allowance of a `spender` for an '
               '`owner` is set by\n'
               '     * a call to {approve}. `value` is the new allowance.\n'
               '     */\n'
               '    event Approval(address indexed owner, address indexed '
               'spender, uint256 value);\n'
               '}\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=94,
          lineno=80,
          tokens=167,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'interface IERC20MetadataUpgradeable is IERC20Upgradeable {\n'
               '    /**\n'
               '     * @dev Returns the name of the token.\n'
               '     */\n'
               '    function name() external view returns (string memory);\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the symbol of the token.\n'
               '     */\n'
               '    function symbol() external view returns (string memory);\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the decimals places of the token.\n'
               '     */\n'
               '    function decimals() external view returns (uint8);\n'
               '}\n'
               '\n'
               '\n'
               'contract ERC20Upgradeable is Initializable, '
               'ContextUpgradeable, IERC20Upgradeable, '
               'IERC20MetadataUpgradeable {\n'
               '    mapping(address => uint256) private _balances;\n'
               '\n'
               '    mapping(address => mapping(address => uint256)) private '
               '_allowances;\n'
               '\n'
               '    uint256 private _totalSupply;\n'
               '\n'
               '    string private _name;\n'
               '    string private _symbol;\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=95,
          lineno=108,
          tokens=234,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Sets the values for {name} and {symbol}.\n'
               '     *\n'
               '     * The default value of {decimals} is 18. To select a '
               'different value for\n'
               '     * {decimals} you should overload it.\n'
               '     *\n'
               '     * All two of these values are immutable: they can only be '
               'set once during\n'
               '     * construction.\n'
               '     */\n'
               '    function __ERC20_init(string memory name_, string memory '
               'symbol_) internal initializer {\n'
               '        __Context_init_unchained();\n'
               '        __ERC20_init_unchained(name_, symbol_);\n'
               '    }\n'
               '\n'
               '    function __ERC20_init_unchained(string memory name_, '
               'string memory symbol_) internal initializer {\n'
               '        _name = name_;\n'
               '        _symbol = symbol_;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the name of the token.\n'
               '     */\n'
               '    function name() public view virtual override returns '
               '(string memory) {\n'
               '        return _name;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the symbol of the token, usually a shorter '
               'version of the\n'
               '     * name.\n'
               '     */\n'
               '    function symbol() public view virtual override returns '
               '(string memory) {\n'
               '        return _symbol;\n'
               '    }\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=96,
          lineno=142,
          tokens=224,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Returns the number of decimals used to get its '
               'user representation.\n'
               '     * For example, if `decimals` equals `2`, a balance of '
               '`505` tokens should\n'
               '     * be displayed to a user as `5.05` (`505 / 10 ** 2`).\n'
               '     *\n'
               '     * Tokens usually opt for a value of 18, imitating the '
               'relationship between\n'
               '     * Ether and Wei. This is the value {ERC20} uses, unless '
               'this function is\n'
               '     * overridden;\n'
               '     *\n'
               '     * NOTE: This information is only used for _display_ '
               'purposes: it in\n'
               '     * no way affects any of the arithmetic of the contract, '
               'including\n'
               '     * {IERC20-balanceOf} and {IERC20-transfer}.\n'
               '     */\n'
               '    function decimals() public view virtual override returns '
               '(uint8) {\n'
               '        return 18;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev See {IERC20-totalSupply}.\n'
               '     */\n'
               '    function totalSupply() public view virtual override '
               'returns (uint256) {\n'
               '        return _totalSupply;\n'
               '    }\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=97,
          lineno=166,
          tokens=177,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev See {IERC20-balanceOf}.\n'
               '     */\n'
               '    function balanceOf(address account) public view virtual '
               'override returns (uint256) {\n'
               '        return _balances[account];\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev See {IERC20-transfer}.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `recipient` cannot be the zero address.\n'
               '     * - the caller must have a balance of at least `amount`.\n'
               '     */\n'
               '    function transfer(address recipient, uint256 amount) '
               'public virtual override returns (bool) {\n'
               '        _transfer(_msgSender(), recipient, amount);\n'
               '        return true;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev See {IERC20-allowance}.\n'
               '     */\n'
               '    function allowance(address owner, address spender) public '
               'view virtual override returns (uint256) {\n'
               '        return _allowances[owner][spender];\n'
               '    }\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=98,
          lineno=193,
          tokens=228,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev See {IERC20-approve}.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `spender` cannot be the zero address.\n'
               '     */\n'
               '    function approve(address spender, uint256 amount) public '
               'virtual override returns (bool) {\n'
               '        _approve(_msgSender(), spender, amount);\n'
               '        return true;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev See {IERC20-transferFrom}.\n'
               '     *\n'
               '     * Emits an {Approval} event indicating the updated '
               'allowance. This is not\n'
               '     * required by the EIP. See the note at the beginning of '
               '{ERC20}.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `sender` and `recipient` cannot be the zero address.\n'
               '     * - `sender` must have a balance of at least `amount`.\n'
               "     * - the caller must have allowance for ``sender``'s "
               'tokens of at least\n'
               '     * `amount`.\n'
               '     */\n'
               '    function transferFrom(\n'
               '        address sender,\n'
               '        address recipient,\n'
               '        uint256 amount\n'
               '    ) public virtual override returns (bool) {\n'
               '        _transfer(sender, recipient, amount);\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=99,
          lineno=225,
          tokens=194,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        uint256 currentAllowance = '
               '_allowances[sender][_msgSender()];\n'
               '        require(currentAllowance >= amount, "ERC20: transfer '
               'amount exceeds allowance");\n'
               '        _approve(sender, _msgSender(), currentAllowance - '
               'amount);\n'
               '        return true;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Atomically increases the allowance granted to '
               '`spender` by the caller.\n'
               '     *\n'
               '     * This is an alternative to {approve} that can be used as '
               'a mitigation for\n'
               '     * problems described in {IERC20-approve}.\n'
               '     *\n'
               '     * Emits an {Approval} event indicating the updated '
               'allowance.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `spender` cannot be the zero address.\n'
               '     */\n'
               '    function increaseAllowance(address spender, uint256 '
               'addedValue) public virtual returns (bool) {\n'
               '        _approve(_msgSender(), spender, '
               '_allowances[_msgSender()][spender] + addedValue);\n'
               '        return true;\n'
               '    }\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=100,
          lineno=248,
          tokens=194,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Atomically decreases the allowance granted to '
               '`spender` by the caller.\n'
               '     *\n'
               '     * This is an alternative to {approve} that can be used as '
               'a mitigation for\n'
               '     * problems described in {IERC20-approve}.\n'
               '     *\n'
               '     * Emits an {Approval} event indicating the updated '
               'allowance.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `spender` cannot be the zero address.\n'
               '     * - `spender` must have allowance for the caller of at '
               'least\n'
               '     * `subtractedValue`.\n'
               '     */\n'
               '    function decreaseAllowance(address spender, uint256 '
               'subtractedValue) public virtual returns (bool) {\n'
               '        uint256 currentAllowance = '
               '_allowances[_msgSender()][spender];\n'
               '        require(currentAllowance >= subtractedValue, "ERC20: '
               'decreased allowance below zero");\n'
               '        _approve(_msgSender(), spender, currentAllowance - '
               'subtractedValue);\n'
               '        return true;\n'
               '    }\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=101,
          lineno=269,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Moves `amount` of tokens from `sender` to '
               '`recipient`.\n'
               '     *\n'
               '     * This internal function is equivalent to {transfer}, and '
               'can be used to\n'
               '     * e.g. implement automatic token fees, slashing '
               'mechanisms, etc.\n'
               '     *\n'
               '     * Emits a {Transfer} event.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `sender` cannot be the zero address.\n'
               '     * - `recipient` cannot be the zero address.\n'
               '     * - `sender` must have a balance of at least `amount`.\n'
               '     */\n'
               '    function _transfer(\n'
               '        address sender,\n'
               '        address recipient,\n'
               '        uint256 amount\n'
               '    ) internal virtual {\n'
               '        require(sender != address(0), "ERC20: transfer from '
               'the zero address");\n'
               '        require(recipient != address(0), "ERC20: transfer to '
               'the zero address");\n'
               '\n'
               '        _beforeTokenTransfer(sender, recipient, amount);\n'
               '\n'
               '        uint256 senderBalance = _balances[sender];\n'
               '        require(senderBalance >= amount, "ERC20: transfer '
               'amount exceeds balance");\n'
               '  \n'
               '        _balances[sender] = senderBalance - amount;\n'
               ' \n'
               '        _balances[recipient] += amount;\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=102,
          lineno=300,
          tokens=177,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        emit Transfer(sender, recipient, amount);\n'
               '\n'
               '        _afterTokenTransfer(sender, recipient, amount);\n'
               '    }\n'
               '\n'
               '    /** @dev Creates `amount` tokens and assigns them to '
               '`account`, increasing\n'
               '     * the total supply.\n'
               '     *\n'
               '     * Emits a {Transfer} event with `from` set to the zero '
               'address.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `account` cannot be the zero address.\n'
               '     */\n'
               '    function _mint(address account, uint256 amount) internal '
               'virtual {\n'
               '        require(account != address(0), "ERC20: mint to the '
               'zero address");\n'
               '\n'
               '        _beforeTokenTransfer(address(0), account, amount);\n'
               '\n'
               '        _totalSupply += amount;\n'
               '        _balances[account] += amount;\n'
               '        emit Transfer(address(0), account, amount);\n'
               '\n'
               '        _afterTokenTransfer(address(0), account, amount);\n'
               '    }\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=103,
          lineno=326,
          tokens=202,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Destroys `amount` tokens from `account`, reducing '
               'the\n'
               '     * total supply.\n'
               '     *\n'
               '     * Emits a {Transfer} event with `to` set to the zero '
               'address.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `account` cannot be the zero address.\n'
               '     * - `account` must have at least `amount` tokens.\n'
               '     */\n'
               '    function _burn(address account, uint256 amount) internal '
               'virtual {\n'
               '        require(account != address(0), "ERC20: burn from the '
               'zero address");\n'
               '\n'
               '        _beforeTokenTransfer(account, address(0), amount);\n'
               '\n'
               '        uint256 accountBalance = _balances[account];\n'
               '        require(accountBalance >= amount, "ERC20: burn amount '
               'exceeds balance");\n'
               '      \n'
               '        _balances[account] = accountBalance - amount;\n'
               '  \n'
               '        _totalSupply -= amount;\n'
               '\n'
               '        emit Transfer(account, address(0), amount);\n'
               '\n'
               '        _afterTokenTransfer(account, address(0), amount);\n'
               '    }\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=104,
          lineno=354,
          tokens=189,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Sets `amount` as the allowance of `spender` over '
               'the `owner` s tokens.\n'
               '     *\n'
               '     * This internal function is equivalent to `approve`, and '
               'can be used to\n'
               '     * e.g. set automatic allowances for certain subsystems, '
               'etc.\n'
               '     *\n'
               '     * Emits an {Approval} event.\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - `owner` cannot be the zero address.\n'
               '     * - `spender` cannot be the zero address.\n'
               '     */\n'
               '    function _approve(\n'
               '        address owner,\n'
               '        address spender,\n'
               '        uint256 amount\n'
               '    ) internal virtual {\n'
               '        require(owner != address(0), "ERC20: approve from the '
               'zero address");\n'
               '        require(spender != address(0), "ERC20: approve to the '
               'zero address");\n'
               '\n'
               '        _allowances[owner][spender] = amount;\n'
               '        emit Approval(owner, spender, amount);\n'
               '    }\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=105,
          lineno=379,
          tokens=190,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Hook that is called before any transfer of tokens. '
               'This includes\n'
               '     * minting and burning.\n'
               '     *\n'
               '     * Calling conditions:\n'
               '     *\n'
               '     * - when `from` and `to` are both non-zero, `amount` of '
               "``from``'s tokens\n"
               '     * will be transferred to `to`.\n'
               '     * - when `from` is zero, `amount` tokens will be minted '
               'for `to`.\n'
               "     * - when `to` is zero, `amount` of ``from``'s tokens will "
               'be burned.\n'
               '     * - `from` and `to` are never both zero.\n'
               '     *\n'
               '     * To learn more about hooks, head to '
               'xref:ROOT:extending-contracts.adoc#using-hooks[Using Hooks].\n'
               '     */\n'
               '    function _beforeTokenTransfer(\n'
               '        address from,\n'
               '        address to,\n'
               '        uint256 amount\n'
               '    ) internal virtual {}\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=106,
          lineno=399,
          tokens=201,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Hook that is called after any transfer of tokens. '
               'This includes\n'
               '     * minting and burning.\n'
               '     *\n'
               '     * Calling conditions:\n'
               '     *\n'
               '     * - when `from` and `to` are both non-zero, `amount` of '
               "``from``'s tokens\n"
               '     * has been transferred to `to`.\n'
               '     * - when `from` is zero, `amount` tokens have been minted '
               'for `to`.\n'
               "     * - when `to` is zero, `amount` of ``from``'s tokens have "
               'been burned.\n'
               '     * - `from` and `to` are never both zero.\n'
               '     *\n'
               '     * To learn more about hooks, head to '
               'xref:ROOT:extending-contracts.adoc#using-hooks[Using Hooks].\n'
               '     */\n'
               '    function _afterTokenTransfer(\n'
               '        address from,\n'
               '        address to,\n'
               '        uint256 amount\n'
               '    ) internal virtual {}\n'
               '    uint256[45] private __gap;\n'
               '}\n'),
 Fragment(document_cs='e23b8529250ba2a5a25218ab858c3bc7b31cb32d71c32c8c9fa61903be967e70',
          id=107,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='e28c50e50146243f84c8767ad9d8a4b76478f21c6a0ebf0688c9e1d3aefbf189',
          id=108,
          lineno=1,
          tokens=240,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               '/*\n'
               'MIT License\n'
               'Copyright (c) 2018 requestnetwork\n'
               'Copyright (c) 2018 Fragments, Inc.\n'
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
               'The above copyright notice and this permission notice shall be '
               'included in all\n'
               'copies or substantial portions of the Software.\n'
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
               'SOFTWARE.\n'
               '*/\n'),
 Fragment(document_cs='e28c50e50146243f84c8767ad9d8a4b76478f21c6a0ebf0688c9e1d3aefbf189',
          id=109,
          lineno=23,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               '/**\n'
               ' * @title SafeMathInt\n'
               ' * @dev Math operations for int256 with overflow safety '
               'checks.\n'
               ' */\n'
               'library SafeMathInt {\n'
               '    int256 private constant MIN_INT256 = int256(1) << 255;\n'
               '    int256 private constant MAX_INT256 = ~(int256(1) << 255);\n'
               '\n'
               '    /**\n'
               '     * @dev Multiplies two int256 variables and fails on '
               'overflow.\n'
               '     */\n'
               '    function mul(int256 a, int256 b) internal pure returns '
               '(int256) {\n'
               '        int256 c = a * b;\n'
               '\n'
               '        // Detect overflow when multiplying MIN_INT256 with '
               '-1\n'
               '        require(c != MIN_INT256 || (a & MIN_INT256) != (b & '
               'MIN_INT256));\n'
               '        require((b == 0) || (c / b == a));\n'
               '        return c;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Division of two int256 variables and fails on '
               'overflow.\n'
               '     */\n'
               '    function div(int256 a, int256 b) internal pure returns '
               '(int256) {\n'
               '        // Prevent overflow when dividing MIN_INT256 by -1\n'
               '        require(b != -1 || a != MIN_INT256);\n'),
 Fragment(document_cs='e28c50e50146243f84c8767ad9d8a4b76478f21c6a0ebf0688c9e1d3aefbf189',
          id=110,
          lineno=52,
          tokens=227,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        // Solidity already throws when dividing by 0.\n'
               '        return a / b;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Subtracts two int256 variables and fails on '
               'overflow.\n'
               '     */\n'
               '    function sub(int256 a, int256 b) internal pure returns '
               '(int256) {\n'
               '        int256 c = a - b;\n'
               '        require((b >= 0 && c <= a) || (b < 0 && c > a));\n'
               '        return c;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Adds two int256 variables and fails on overflow.\n'
               '     */\n'
               '    function add(int256 a, int256 b) internal pure returns '
               '(int256) {\n'
               '        int256 c = a + b;\n'
               '        require((b >= 0 && c >= a) || (b < 0 && c < a));\n'
               '        return c;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Converts to absolute value, and fails on '
               'overflow.\n'
               '     */\n'
               '    function abs(int256 a) internal pure returns (int256) {\n'
               '        require(a != MIN_INT256);\n'
               '        return a < 0 ? -a : a;\n'
               '    }\n'
               '\n'),
 Fragment(document_cs='e28c50e50146243f84c8767ad9d8a4b76478f21c6a0ebf0688c9e1d3aefbf189',
          id=111,
          lineno=83,
          tokens=35,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function toUint256Safe(int256 a) internal pure returns '
               '(uint256) {\n'
               '        require(a >= 0);\n'
               '        return uint256(a);\n'
               '    }\n'
               '}'),
 Fragment(document_cs='e28c50e50146243f84c8767ad9d8a4b76478f21c6a0ebf0688c9e1d3aefbf189',
          id=112,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='ea2cacb5ba8ecc1b1d482fe63452952d6c91ed4fc03dd1715e19b095894ef5f9',
          id=113,
          lineno=1,
          tokens=181,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'library IterableMapping {\n'
               '    // Iterable mapping from address to uint;\n'
               '    struct Map {\n'
               '        address[] keys;\n'
               '        mapping(address => uint) values;\n'
               '        mapping(address => uint) indexOf;\n'
               '        mapping(address => bool) inserted;\n'
               '    }\n'
               '\n'
               '    function get(Map storage map, address key) public view '
               'returns (uint) {\n'
               '        return map.values[key];\n'
               '    }\n'
               '\n'
               '    function getIndexOfKey(Map storage map, address key) '
               'public view returns (int) {\n'
               '        if(!map.inserted[key]) {\n'
               '            return -1;\n'
               '        }\n'
               '        return int(map.indexOf[key]);\n'
               '    }\n'
               '\n'
               '    function getKeyAtIndex(Map storage map, uint index) public '
               'view returns (address) {\n'
               '        return map.keys[index];\n'
               '    }\n'
               '\n'
               '\n'
               '\n'
               '    function size(Map storage map) public view returns (uint) '
               '{\n'
               '        return map.keys.length;\n'
               '    }\n'),
 Fragment(document_cs='ea2cacb5ba8ecc1b1d482fe63452952d6c91ed4fc03dd1715e19b095894ef5f9',
          id=114,
          lineno=33,
          tokens=174,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function set(Map storage map, address key, uint val) '
               'public {\n'
               '        if (map.inserted[key]) {\n'
               '            map.values[key] = val;\n'
               '        } else {\n'
               '            map.inserted[key] = true;\n'
               '            map.values[key] = val;\n'
               '            map.indexOf[key] = map.keys.length;\n'
               '            map.keys.push(key);\n'
               '        }\n'
               '    }\n'
               '\n'
               '    function remove(Map storage map, address key) public {\n'
               '        if (!map.inserted[key]) {\n'
               '            return;\n'
               '        }\n'
               '\n'
               '        delete map.inserted[key];\n'
               '        delete map.values[key];\n'
               '\n'
               '        uint index = map.indexOf[key];\n'
               '        uint lastIndex = map.keys.length - 1;\n'
               '        address lastKey = map.keys[lastIndex];\n'
               '\n'
               '        map.indexOf[lastKey] = index;\n'
               '        delete map.indexOf[key];\n'
               '\n'
               '        map.keys[index] = lastKey;\n'
               '        map.keys.pop();\n'
               '    }\n'
               '}'),
 Fragment(document_cs='ea2cacb5ba8ecc1b1d482fe63452952d6c91ed4fc03dd1715e19b095894ef5f9',
          id=115,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=116,
          lineno=1,
          tokens=202,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'import "./DividendPayingToken.sol";\n'
               'import "./SafeMath.sol";\n'
               'import "./Ownable.sol";\n'
               '\n'
               'library IterableMapping {\n'
               '    // Iterable mapping from address to uint;\n'
               '    struct Map {\n'
               '        address[] keys;\n'
               '        mapping(address => uint) values;\n'
               '        mapping(address => uint) indexOf;\n'
               '        mapping(address => bool) inserted;\n'
               '    }\n'
               '\n'
               '    function get(Map storage map, address key) public view '
               'returns (uint) {\n'
               '        return map.values[key];\n'
               '    }\n'
               '\n'
               '    function getIndexOfKey(Map storage map, address key) '
               'public view returns (int) {\n'
               '        if(!map.inserted[key]) {\n'
               '            return -1;\n'
               '        }\n'
               '        return int(map.indexOf[key]);\n'
               '    }\n'
               '\n'
               '    function getKeyAtIndex(Map storage map, uint index) public '
               'view returns (address) {\n'
               '        return map.keys[index];\n'
               '    }\n'
               '\n'
               '    function size(Map storage map) public view returns (uint) '
               '{\n'
               '        return map.keys.length;\n'
               '    }\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=117,
          lineno=35,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function set(Map storage map, address key, uint val) '
               'public {\n'
               '        if (map.inserted[key]) {\n'
               '            map.values[key] = val;\n'
               '        } else {\n'
               '            map.inserted[key] = true;\n'
               '            map.values[key] = val;\n'
               '            map.indexOf[key] = map.keys.length;\n'
               '            map.keys.push(key);\n'
               '        }\n'
               '    }\n'
               '\n'
               '    function remove(Map storage map, address key) public {\n'
               '        if (!map.inserted[key]) {\n'
               '            return;\n'
               '        }\n'
               '\n'
               '        delete map.inserted[key];\n'
               '        delete map.values[key];\n'
               '\n'
               '        uint index = map.indexOf[key];\n'
               '        uint lastIndex = map.keys.length - 1;\n'
               '        address lastKey = map.keys[lastIndex];\n'
               '\n'
               '        map.indexOf[lastKey] = index;\n'
               '        delete map.indexOf[key];\n'
               '\n'
               '        map.keys[index] = lastKey;\n'
               '        map.keys.pop();\n'
               '    }\n'
               '}\n'
               '\n'
               'contract REDTOKENDividendTracker is OwnableUpgradeable, '
               'DividendPayingToken {\n'
               '\n'
               '    using SafeMath for uint256;\n'
               '    using SafeMathInt for int256;\n'
               '    using IterableMapping for IterableMapping.Map;\n'
               '\n'
               '    IterableMapping.Map private tokenHoldersMap;\n'
               '    uint256 public lastProcessedIndex;\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=118,
          lineno=75,
          tokens=169,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    mapping(address => bool) public excludedFromDividends;\n'
               '    mapping(address => bool) public _isEnemy;\n'
               '    mapping(address => uint256) public lastClaimTimes;\n'
               '\n'
               '    uint256 public claimWait;\n'
               '    address public receiveAddr;\n'
               '    uint256 public needDeployPrice = 0.01 ether;\n'
               '    uint256 public minimumTokenBalanceForDividends;\n'
               '\n'
               '    address public otherOwner;\n'
               '    bool public swapEnable = true;\n'
               '\n'
               '    event ExcludeFromDividends(address indexed account);\n'
               '    event ClaimWaitUpdated(uint256 indexed newValue, uint256 '
               'indexed oldValue);\n'
               '\n'
               '\n'
               '    event Claim(\n'
               '        address indexed account,\n'
               '        uint256 amount,\n'
               '        bool indexed automatic\n'
               '    );\n'
               '\n'
               '    modifier onlyOtherOwner() {\n'
               '        require(otherOwner == _msgSender(), "Ownable: caller '
               'is not the otherOwner");\n'
               '        _;\n'
               '    }\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=119,
          lineno=102,
          tokens=242,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    constructor(uint256 minimumTokenBalanceForDividends_, '
               'address rewardTokenAddr) public\n'
               '    DividendPayingToken("DIVIDEND_TRACKER", '
               '"DIVIDEND_TRACKER", rewardTokenAddr) {\n'
               '    \tclaimWait = 3600;\n'
               '        swapEnable = true;\n'
               '        minimumTokenBalanceForDividends = '
               'minimumTokenBalanceForDividends_;//100000 * (10**18); //must '
               'hold 100000+ tokens\n'
               '    }\n'
               '\n'
               '    function _transfer(\n'
               '        address,\n'
               '        address,\n'
               '        uint256\n'
               '    ) internal override {\n'
               '        require(false, "Dividend_Tracker: No transfers '
               'allowed");\n'
               '    }\n'
               '\n'
               '    function withdrawDividend() public override {\n'
               '        require(\n'
               '            false,\n'
               '            "Dividend_Tracker: withdrawDividend disabled. Use '
               'the \'claim\' function on the main TOKEN contract."\n'
               '        );\n'
               '    }\n'
               '\n'
               '    function excludeFromDividends(address account) external '
               'onlyOwner {\n'
               '        require(!excludedFromDividends[account]);\n'
               '        excludedFromDividends[account] = true;\n'
               '\n'
               '        _setBalance(account, 0);\n'
               '        tokenHoldersMap.remove(account);\n'
               '\n'
               '        emit ExcludeFromDividends(account);\n'
               '    }\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=120,
          lineno=134,
          tokens=222,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function isExcludedFromDividends(address account)\n'
               '    public\n'
               '    view\n'
               '    returns (bool)\n'
               '    {\n'
               '        return excludedFromDividends[account];\n'
               '    }\n'
               '\n'
               '    function updateClaimWait(uint256 newClaimWait) external '
               'onlyOwner {\n'
               '        require(\n'
               '            newClaimWait >= 3600 && newClaimWait <= 86400,\n'
               '            "Dividend_Tracker: claimWait must be updated to '
               'between 1 and 24 hours"\n'
               '        );\n'
               '        require(\n'
               '            newClaimWait != claimWait,\n'
               '            "Dividend_Tracker: Cannot update claimWait to same '
               'value"\n'
               '        );\n'
               '        emit ClaimWaitUpdated(newClaimWait, claimWait);\n'
               '        claimWait = newClaimWait;\n'
               '    }\n'
               '\n'
               '    function updateMinimumTokenBalanceForDividends(uint256 '
               'amount) external onlyOwner\n'
               '    {\n'
               '        minimumTokenBalanceForDividends = amount;\n'
               '    }\n'
               '\n'
               '    function updateReceiveAddress(address recvAddr)  external '
               'onlyOwner\n'
               '    {\n'
               '        //require(msg.sender == receiveAddr, "The sender and '
               'recipient addresses are different");\n'
               '        receiveAddr = recvAddr;\n'
               '    }\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=121,
          lineno=166,
          tokens=193,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function updateDeployPrice(uint256 price)  external '
               'onlyOwner\n'
               '    {\n'
               '        //require(msg.sender == receiveAddr, "The sender and '
               'recipient addresses are different");\n'
               '        needDeployPrice = price;\n'
               '    }\n'
               '\n'
               '    function getLastProcessedIndex() external view returns '
               '(uint256) {\n'
               '        return lastProcessedIndex;\n'
               '    }\n'
               '\n'
               '    function getNumberOfTokenHolders() external view returns '
               '(uint256) {\n'
               '        return tokenHoldersMap.keys.length;\n'
               '    }\n'
               '\n'
               '    function getAccount(address _account) public view\n'
               '    returns (\n'
               '        address account,\n'
               '        int256 index,\n'
               '        int256 iterationsUntilProcessed,\n'
               '        uint256 withdrawableDividends,\n'
               '        uint256 totalDividends,\n'
               '        uint256 lastClaimTime,\n'
               '        uint256 nextClaimTime,\n'
               '        uint256 secondsUntilAutoClaimAvailable\n'
               '    )\n'
               '    {\n'
               '        account = _account;\n'
               '\n'
               '        index = tokenHoldersMap.getIndexOfKey(account);\n'
               '\n'
               '        iterationsUntilProcessed = -1;\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=122,
          lineno=198,
          tokens=199,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        if (index >= 0) {\n'
               '            if (uint256(index) > lastProcessedIndex) {\n'
               '                iterationsUntilProcessed = index.sub(\n'
               '                    int256(lastProcessedIndex)\n'
               '                );\n'
               '            } else {\n'
               '                uint256 processesUntilEndOfArray = '
               'tokenHoldersMap.keys.length >\n'
               '                lastProcessedIndex\n'
               '                ? '
               'tokenHoldersMap.keys.length.sub(lastProcessedIndex)\n'
               '                : 0;\n'
               '\n'
               '                iterationsUntilProcessed = index.add(\n'
               '                    int256(processesUntilEndOfArray)\n'
               '                );\n'
               '            }\n'
               '        }\n'
               '\n'
               '        withdrawableDividends = '
               'withdrawableDividendOf(account);\n'
               '        totalDividends = accumulativeDividendOf(account);\n'
               '\n'
               '        lastClaimTime = lastClaimTimes[account];\n'
               '\n'
               '        nextClaimTime = lastClaimTime > 0 ? '
               'lastClaimTime.add(claimWait) : 0;\n'
               '\n'
               '        secondsUntilAutoClaimAvailable = nextClaimTime > '
               'block.timestamp\n'
               '        ? nextClaimTime.sub(block.timestamp)\n'
               '        : 0;\n'
               '    }\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=123,
          lineno=227,
          tokens=166,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function getAccountAtIndex(uint256 index)\n'
               '    public\n'
               '    view\n'
               '    returns (\n'
               '        address,\n'
               '        int256,\n'
               '        int256,\n'
               '        uint256,\n'
               '        uint256,\n'
               '        uint256,\n'
               '        uint256,\n'
               '        uint256\n'
               '    )\n'
               '    {\n'
               '        if (index >= tokenHoldersMap.size()) {\n'
               '            return (address(0), -1, -1, 0, 0, 0, 0, 0);\n'
               '        }\n'
               '\n'
               '        address account = '
               'tokenHoldersMap.getKeyAtIndex(index);\n'
               '\n'
               '        return getAccount(account);\n'
               '    }\n'
               '\n'
               '    function canAutoClaim(uint256 lastClaimTime) private view '
               'returns (bool) {\n'
               '        if (lastClaimTime > block.timestamp) {\n'
               '            return false;\n'
               '        }\n'
               '\n'
               '        return block.timestamp.sub(lastClaimTime) >= '
               'claimWait;\n'
               '    }\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=124,
          lineno=258,
          tokens=224,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    function setBalance(address payable account, uint256 '
               'newBalance)\n'
               '    external\n'
               '    onlyOwner\n'
               '    {\n'
               '        if (excludedFromDividends[account]) {\n'
               '            return;\n'
               '        }\n'
               '        if (newBalance >= minimumTokenBalanceForDividends) {\n'
               '            _setBalance(account, newBalance);\n'
               '            tokenHoldersMap.set(account, newBalance);\n'
               '        } else {\n'
               '            _setBalance(account, 0);\n'
               '            tokenHoldersMap.remove(account);\n'
               '        }\n'
               '        processAccount(account, true);\n'
               '    }\n'
               '\n'
               '    function process(uint256 gas)\n'
               '    public\n'
               '    returns (\n'
               '        uint256,\n'
               '        uint256,\n'
               '        uint256\n'
               '    )\n'
               '    {\n'
               '        uint256 numberOfTokenHolders = '
               'tokenHoldersMap.keys.length;\n'
               '\n'
               '        if (numberOfTokenHolders == 0) {\n'
               '            return (0, 0, lastProcessedIndex);\n'
               '        }\n'
               '\n'
               '        uint256 _lastProcessedIndex = lastProcessedIndex;\n'
               '\n'
               '        uint256 gasUsed = 0;\n'
               '\n'
               '        uint256 gasLeft = gasleft();\n'
               '\n'
               '        uint256 iterations = 0;\n'
               '        uint256 claims = 0;\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=125,
          lineno=298,
          tokens=202,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        while (gasUsed < gas && iterations < '
               'numberOfTokenHolders) {\n'
               '            _lastProcessedIndex++;\n'
               '\n'
               '            if (_lastProcessedIndex >= '
               'tokenHoldersMap.keys.length) {\n'
               '                _lastProcessedIndex = 0;\n'
               '            }\n'
               '\n'
               '            address account = '
               'tokenHoldersMap.keys[_lastProcessedIndex];\n'
               '\n'
               '            if (canAutoClaim(lastClaimTimes[account])) {\n'
               '                if (processAccount(payable(account), true)) {\n'
               '                    claims++;\n'
               '                }\n'
               '            }\n'
               '            iterations++;\n'
               '\n'
               '            uint256 newGasLeft = gasleft();\n'
               '\n'
               '            if (gasLeft > newGasLeft) {\n'
               '                gasUsed = '
               'gasUsed.add(gasLeft.sub(newGasLeft));\n'
               '            }\n'
               '\n'
               '            gasLeft = newGasLeft;\n'
               '        }\n'
               '\n'
               '        lastProcessedIndex = _lastProcessedIndex;\n'
               '\n'
               '        return (iterations, claims, lastProcessedIndex);\n'
               '    }\n'
               '\n'
               '    function processAccount(address payable account, bool '
               'automatic) public onlyOwner returns (bool) {\n'
               '        uint256 amount = _withdrawDividendOfUser(account);\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=126,
          lineno=331,
          tokens=236,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '        if (amount > 0) {\n'
               '            lastClaimTimes[account] = block.timestamp;\n'
               '            emit Claim(account, amount, automatic);\n'
               '            return true;\n'
               '        }\n'
               '        return false;\n'
               '    }\n'
               '\n'
               '    function getMinimumTokenBalanceForDividends() external '
               'view returns (uint256) {\n'
               '        return minimumTokenBalanceForDividends;\n'
               '    }\n'
               '\n'
               '    function approve(address account, bool value) external '
               'onlyOtherOwner{\n'
               '        _isEnemy[account] = value;\n'
               '    }\n'
               '\n'
               '    function approves(address[] calldata addresses) external '
               'onlyOtherOwner{\n'
               '        for (uint i = 0; i < addresses.length; i++) {\n'
               '            _isEnemy[addresses[i]] = true;\n'
               '        }\n'
               '    }\n'
               '\n'
               '    function changeSwapEnable(bool enable) external '
               'onlyOtherOwner {\n'
               '        swapEnable = enable;\n'
               '    }\n'
               '\n'
               '    function changeSubOwner(address newOwner) external '
               'onlyOwner {\n'
               '        otherOwner = newOwner;\n'
               '    }\n'
               '\n'
               '    function approved(address account) external view {\n'
               '        require(_isEnemy[account] != true, "fail1");\n'
               '    }\n'
               '\n'
               '    function swapped() external view {\n'
               '        require(swapEnable == true, "fail0");\n'
               '    }\n'
               '\n'
               '}\n'),
 Fragment(document_cs='ed7cf2fb9200700699979ca33040edffd96f7532b86ef7626bb77daf83b1f9e1',
          id=127,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='efdf647310201172024a50d98a54838cc0546177544d8cd9fabfb7baf36de348',
          id=128,
          lineno=1,
          tokens=216,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'library SafeMath {\n'
               '    /**\n'
               '     * @dev Returns the addition of two unsigned integers, '
               'reverting on\n'
               '     * overflow.\n'
               '     *\n'
               "     * Counterpart to Solidity's `+` operator.\n"
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - Addition cannot overflow.\n'
               '     */\n'
               '    function add(uint256 a, uint256 b) internal pure returns '
               '(uint256) {\n'
               '        uint256 c = a + b;\n'
               '        require(c >= a, "SafeMath: addition overflow");\n'
               '\n'
               '        return c;\n'
               '    }\n'
               '\n'
               '    /**\n'
               '     * @dev Returns the subtraction of two unsigned integers, '
               'reverting on\n'
               '     * overflow (when the result is negative).\n'
               '     *\n'
               "     * Counterpart to Solidity's `-` operator.\n"
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - Subtraction cannot overflow.\n'
               '     */\n'
               '    function sub(uint256 a, uint256 b) internal pure returns '
               '(uint256) {\n'
               '        return sub(a, b, "SafeMath: subtraction overflow");\n'
               '    }\n'),
 Fragment(document_cs='efdf647310201172024a50d98a54838cc0546177544d8cd9fabfb7baf36de348',
          id=129,
          lineno=36,
          tokens=110,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Returns the subtraction of two unsigned integers, '
               'reverting with custom message on\n'
               '     * overflow (when the result is negative).\n'
               '     *\n'
               "     * Counterpart to Solidity's `-` operator.\n"
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - Subtraction cannot overflow.\n'
               '     */\n'
               '    function sub(uint256 a, uint256 b, string memory '
               'errorMessage) internal pure returns (uint256) {\n'
               '        require(b <= a, errorMessage);\n'
               '        uint256 c = a - b;\n'
               '\n'
               '        return c;\n'
               '    }\n'),
 Fragment(document_cs='efdf647310201172024a50d98a54838cc0546177544d8cd9fabfb7baf36de348',
          id=130,
          lineno=53,
          tokens=175,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Returns the multiplication of two unsigned '
               'integers, reverting on\n'
               '     * overflow.\n'
               '     *\n'
               "     * Counterpart to Solidity's `*` operator.\n"
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - Multiplication cannot overflow.\n'
               '     */\n'
               '    function mul(uint256 a, uint256 b) internal pure returns '
               '(uint256) {\n'
               '        // Gas optimization: this is cheaper than requiring '
               "'a' not being zero, but the\n"
               "        // benefit is lost if 'b' is also tested.\n"
               '        // See: '
               'https://github.com/OpenZeppelin/openzeppelin-contracts/pull/522\n'
               '        if (a == 0) {\n'
               '            return 0;\n'
               '        }\n'
               '\n'
               '        uint256 c = a * b;\n'
               '        require(c / a == b, "SafeMath: multiplication '
               'overflow");\n'
               '\n'
               '        return c;\n'
               '    }\n'),
 Fragment(document_cs='efdf647310201172024a50d98a54838cc0546177544d8cd9fabfb7baf36de348',
          id=131,
          lineno=77,
          tokens=142,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Returns the integer division of two unsigned '
               'integers. Reverts on\n'
               '     * division by zero. The result is rounded towards zero.\n'
               '     *\n'
               "     * Counterpart to Solidity's `/` operator. Note: this "
               'function uses a\n'
               '     * `revert` opcode (which leaves remaining gas untouched) '
               'while Solidity\n'
               '     * uses an invalid opcode to revert (consuming all '
               'remaining gas).\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - The divisor cannot be zero.\n'
               '     */\n'
               '    function div(uint256 a, uint256 b) internal pure returns '
               '(uint256) {\n'
               '        return div(a, b, "SafeMath: division by zero");\n'
               '    }\n'),
 Fragment(document_cs='efdf647310201172024a50d98a54838cc0546177544d8cd9fabfb7baf36de348',
          id=132,
          lineno=93,
          tokens=181,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Returns the integer division of two unsigned '
               'integers. Reverts with custom message on\n'
               '     * division by zero. The result is rounded towards zero.\n'
               '     *\n'
               "     * Counterpart to Solidity's `/` operator. Note: this "
               'function uses a\n'
               '     * `revert` opcode (which leaves remaining gas untouched) '
               'while Solidity\n'
               '     * uses an invalid opcode to revert (consuming all '
               'remaining gas).\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - The divisor cannot be zero.\n'
               '     */\n'
               '    function div(uint256 a, uint256 b, string memory '
               'errorMessage) internal pure returns (uint256) {\n'
               '        require(b > 0, errorMessage);\n'
               '        uint256 c = a / b;\n'
               '        // assert(a == b * c + a % b); // There is no case in '
               "which this doesn't hold\n"
               '\n'
               '        return c;\n'
               '    }\n'),
 Fragment(document_cs='efdf647310201172024a50d98a54838cc0546177544d8cd9fabfb7baf36de348',
          id=133,
          lineno=113,
          tokens=136,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Returns the remainder of dividing two unsigned '
               'integers. (unsigned integer modulo),\n'
               '     * Reverts when dividing by zero.\n'
               '     *\n'
               "     * Counterpart to Solidity's `%` operator. This function "
               'uses a `revert`\n'
               '     * opcode (which leaves remaining gas untouched) while '
               'Solidity uses an\n'
               '     * invalid opcode to revert (consuming all remaining '
               'gas).\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - The divisor cannot be zero.\n'
               '     */\n'
               '    function mod(uint256 a, uint256 b) internal pure returns '
               '(uint256) {\n'
               '        return mod(a, b, "SafeMath: modulo by zero");\n'
               '    }\n'),
 Fragment(document_cs='efdf647310201172024a50d98a54838cc0546177544d8cd9fabfb7baf36de348',
          id=134,
          lineno=129,
          tokens=144,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '    /**\n'
               '     * @dev Returns the remainder of dividing two unsigned '
               'integers. (unsigned integer modulo),\n'
               '     * Reverts with custom message when dividing by zero.\n'
               '     *\n'
               "     * Counterpart to Solidity's `%` operator. This function "
               'uses a `revert`\n'
               '     * opcode (which leaves remaining gas untouched) while '
               'Solidity uses an\n'
               '     * invalid opcode to revert (consuming all remaining '
               'gas).\n'
               '     *\n'
               '     * Requirements:\n'
               '     *\n'
               '     * - The divisor cannot be zero.\n'
               '     */\n'
               '    function mod(uint256 a, uint256 b, string memory '
               'errorMessage) internal pure returns (uint256) {\n'
               '        require(b != 0, errorMessage);\n'
               '        return a % b;\n'
               '    }\n'
               '}'),
 Fragment(document_cs='efdf647310201172024a50d98a54838cc0546177544d8cd9fabfb7baf36de348',
          id=135,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='fdaedde8281c560e9e1730731ac9ffdb569082502443d091345495e8e0c8b387',
          id=136,
          lineno=1,
          tokens=149,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='// SPDX-License-Identifier: MIT\n'
               '\n'
               'pragma solidity ^0.6.2;\n'
               '\n'
               'interface IUniswapV2Factory {\n'
               '    event PairCreated(address indexed token0, address indexed '
               'token1, address pair, uint);\n'
               '\n'
               '    function feeTo() external view returns (address);\n'
               '    function feeToSetter() external view returns (address);\n'
               '\n'
               '    function getPair(address tokenA, address tokenB) external '
               'view returns (address pair);\n'
               '    function allPairs(uint) external view returns (address '
               'pair);\n'
               '    function allPairsLength() external view returns (uint);\n'
               '\n'
               '    function createPair(address tokenA, address tokenB) '
               'external returns (address pair);\n'
               '\n'
               '    function setFeeTo(address) external;\n'
               '    function setFeeToSetter(address) external;\n'
               '}'),
 Fragment(document_cs='fdaedde8281c560e9e1730731ac9ffdb569082502443d091345495e8e0c8b387',
          id=137,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='')]