[Fragment(document_cs='00c3fae2dadce6fed7bf368f08da0e6d7f586816c2f2ef6fd5fe00cdcedc6776',
          id=1,
          lineno=1,
          tokens=41,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { chatHrefConstructor, cn } from '@/lib/utils'import "
               "Image from 'next/image'import { FC } from 'react'import { "
               "toast, type Toast } from 'react-hot-toast'"),
 Fragment(document_cs='00c3fae2dadce6fed7bf368f08da0e6d7f586816c2f2ef6fd5fe00cdcedc6776',
          id=2,
          lineno=6,
          tokens=42,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='UnseenChatToastProps',
          body='interface UnseenChatToastProps {\n'
               '  t: Toast\n'
               '  sessionId: string\n'
               '  senderId: string\n'
               '  senderImg: string\n'
               '  senderName: string\n'
               '  senderMessage: string\n'
               '}'),
 Fragment(document_cs='00c3fae2dadce6fed7bf368f08da0e6d7f586816c2f2ef6fd5fe00cdcedc6776',
          id=3,
          lineno=15,
          tokens=201,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='UnseenChatToast',
          body='UnseenChatToast: FC<UnseenChatToastProps> = ({\n'
               '  t,\n'
               '  senderId,\n'
               '  sessionId,\n'
               '  senderImg,\n'
               '  senderName,\n'
               '  senderMessage,\n'
               '}) => {\n'
               '  return (\n'
               '    <div\n'
               '      className={cn(\n'
               "        'max-w-md w-full bg-white shadow-lg rounded-lg "
               "pointer-events-auto flex ring-1 ring-black ring-opacity-5',\n"
               "        { 'animate-enter': t.visible, 'animate-leave': "
               '!t.visible }\n'
               '      )}>\n'
               '      <a\n'
               '        onClick={() => toast.dismiss(t.id)}\n'
               '        '
               'href={`/dashboard/chat/${chatHrefConstructor(sessionId, '
               'senderId)}`}\n'
               "        className='flex-1 w-0 p-4'>\n"
               "        <div className='flex items-start'>\n"
               "          <div className='flex-shrink-0 pt-0.5'>\n"
               "            <div className='relative h-10 w-10'>\n"
               '              <Image\n'
               '                fill\n'
               "                referrerPolicy='no-referrer'\n"
               "                className='rounded-"),
 Fragment(document_cs='00c3fae2dadce6fed7bf368f08da0e6d7f586816c2f2ef6fd5fe00cdcedc6776',
          id=4,
          lineno=39,
          tokens=187,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='UnseenChatToast',
          body="full'\n"
               '                src={senderImg}\n'
               '                alt={`${senderName} profile picture`}\n'
               '              />\n'
               '            </div>\n'
               '          </div>\n'
               '\n'
               "          <div className='ml-3 flex-1'>\n"
               "            <p className='text-sm font-medium "
               "text-gray-900'>{senderName}</p>\n"
               "            <p className='mt-1 text-sm "
               "text-gray-500'>{senderMessage}</p>\n"
               '          </div>\n'
               '        </div>\n'
               '      </a>\n'
               '\n'
               "      <div className='flex border-l border-gray-200'>\n"
               '        <button\n'
               '          onClick={() => toast.dismiss(t.id)}\n'
               "          className='w-full border border-transparent "
               'rounded-none rounded-r-lg p-4 flex items-center justify-center '
               'text-sm font-medium text-indigo-600 hover:text-indigo-500 '
               "focus:outline-none focus:ring-2 focus:ring-indigo-500'>\n"
               '          Close\n'
               '        </button>\n'
               '      </div>\n'
               '    </div>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='00c3fae2dadce6fed7bf368f08da0e6d7f586816c2f2ef6fd5fe00cdcedc6776',
          id=5,
          lineno=1,
          tokens=46,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: UnseenChatToastProps\n'
               '  Variables: UnseenChatToast\n'
               '  Usages: FC Image Toast alt chatHrefConstructor className div '
               'fill href onClick referrerPolicy senderId senderImg senderName '
               'sessionId src toast\n'),
 Fragment(document_cs='088e8bc3620b98e99ade0a8fc7511a94f6bc497753734ce7819776c7c080e0d0',
          id=6,
          lineno=3,
          tokens=54,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { pusherClient } from '@/lib/pusher'import { "
               "toPusherKey } from '@/lib/utils'import { User } from "
               "'lucide-react'import Link from 'next/link'import { FC, "
               "useEffect, useState } from 'react'"),
 Fragment(document_cs='088e8bc3620b98e99ade0a8fc7511a94f6bc497753734ce7819776c7c080e0d0',
          id=7,
          lineno=10,
          tokens=22,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='FriendRequestSidebarOptionsProps',
          body='interface FriendRequestSidebarOptionsProps {\n'
               '  sessionId: string\n'
               '  initialUnseenRequestCount: number\n'
               '}'),
 Fragment(document_cs='088e8bc3620b98e99ade0a8fc7511a94f6bc497753734ce7819776c7c080e0d0',
          id=8,
          lineno=15,
          tokens=219,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='FriendRequestSidebarOptions',
          body='FriendRequestSidebarOptions: '
               'FC<FriendRequestSidebarOptionsProps> = ({\n'
               '  sessionId,\n'
               '  initialUnseenRequestCount,\n'
               '}) => {\n'
               '  const [unseenRequestCount, setUnseenRequestCount] = '
               'useState<number>(\n'
               '    initialUnseenRequestCount\n'
               '  )\n'
               '\n'
               '  useEffect(() => {\n'
               '    pusherClient.subscribe(\n'
               '      '
               'toPusherKey(`user:${sessionId}:incoming_friend_requests`)\n'
               '    )\n'
               '    '
               'pusherClient.subscribe(toPusherKey(`user:${sessionId}:friends`))\n'
               '\n'
               '    const friendRequestHandler = () => {\n'
               '      setUnseenRequestCount((prev) => prev + 1)\n'
               '    }\n'
               '\n'
               '    const addedFriendHandler = () => {\n'
               '      setUnseenRequestCount((prev) => prev - 1)\n'
               '    }\n'
               '\n'
               "    pusherClient.bind('incoming_friend_requests', "
               'friendRequestHandler)\n'
               "    pusherClient.bind('new_friend', addedFriendHandler)\n"
               '\n'
               '    return () => {\n'
               '      pusherClient.unsubscribe(\n'
               '        '
               'toPusherKey(`user:${sessionId}:incoming_friend_requests`)\n'
               '      )\n'
               '      pusherClient.unsubscribe(toPusherKey(`user:${sessionId}:'),
 Fragment(document_cs='088e8bc3620b98e99ade0a8fc7511a94f6bc497753734ce7819776c7c080e0d0',
          id=9,
          lineno=29,
          tokens=24,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='friendRequestHandler',
          body='friendRequestHandler = () => {\n'
               '      setUnseenRequestCount((prev) => prev + 1)\n'
               '    }'),
 Fragment(document_cs='088e8bc3620b98e99ade0a8fc7511a94f6bc497753734ce7819776c7c080e0d0',
          id=10,
          lineno=33,
          tokens=24,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='addedFriendHandler',
          body='addedFriendHandler = () => {\n'
               '      setUnseenRequestCount((prev) => prev - 1)\n'
               '    }'),
 Fragment(document_cs='088e8bc3620b98e99ade0a8fc7511a94f6bc497753734ce7819776c7c080e0d0',
          id=11,
          lineno=44,
          tokens=237,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='FriendRequestSidebarOptions',
          body='friends`))\n'
               '\n'
               "      pusherClient.unbind('new_friend', addedFriendHandler)\n"
               "      pusherClient.unbind('incoming_friend_requests', "
               'friendRequestHandler)\n'
               '    }\n'
               '  }, [sessionId])\n'
               '\n'
               '  return (\n'
               '    <Link\n'
               "      href='/dashboard/requests'\n"
               "      className='text-gray-700 hover:text-indigo-600 "
               'hover:bg-gray-50 group flex items-center gap-x-3 rounded-md '
               "p-2 text-sm leading-6 font-semibold'>\n"
               "      <div className='text-gray-400 border-gray-200 "
               'group-hover:border-indigo-600 group-hover:text-indigo-600 flex '
               'h-6 w-6 shrink-0 items-center justify-center rounded-lg border '
               "text-[0.625rem] font-medium bg-white'>\n"
               "        <User className='h-4 w-4' />\n"
               '      </div>\n'
               "      <p className='truncate'>Friend requests</p>\n"
               '\n'
               '      {unseenRequestCount > 0 ? (\n'
               "        <div className='rounded-full w-5 h-5 text-xs flex "
               "justify-center items-center text-white bg-indigo-600'>\n"
               '          {unseenRequestCount}\n'
               '        </div>\n'
               '      ) : null}\n'
               '    </Link>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='088e8bc3620b98e99ade0a8fc7511a94f6bc497753734ce7819776c7c080e0d0',
          id=12,
          lineno=1,
          tokens=60,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: FriendRequestSidebarOptionsProps\n'
               '  Variables: FriendRequestSidebarOptions addedFriendHandler '
               'friendRequestHandler\n'
               '  Usages: FC Friend Link User className div href '
               'initialUnseenRequestCount prev pusherClient requests sessionId '
               'setUnseenRequestCount toPusherKey unseenRequestCount useEffect '
               'useState\n'),
 Fragment(document_cs='13b2cde811bfb63155cdb4015858b4272563524574289594da412325726e4769',
          id=13,
          lineno=3,
          tokens=57,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { Loader2, LogOut } from 'lucide-react'import { signOut "
               "} from 'next-auth/react'import { ButtonHTMLAttributes, FC, "
               "useState } from 'react'import { toast } from "
               "'react-hot-toast'import Button from './ui/Button'"),
 Fragment(document_cs='13b2cde811bfb63155cdb4015858b4272563524574289594da412325726e4769',
          id=14,
          lineno=9,
          tokens=14,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='SignOutButtonProps',
          body='interface SignOutButtonProps extends '
               'ButtonHTMLAttributes<HTMLButtonElement> {}'),
 Fragment(document_cs='13b2cde811bfb63155cdb4015858b4272563524574289594da412325726e4769',
          id=15,
          lineno=1,
          tokens=43,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: SignOutButtonProps\n'
               '  Usages: Button ButtonHTMLAttributes FC HTMLButtonElement '
               'Loader2 LogOut SignOutButton className error isSigningOut '
               'onClick props setIsSigningOut signOut toast useState variant\n'),
 Fragment(document_cs='1589a15e55fbebc6519c95d91d8f0a090618f20dc78e479858b9c27552484961',
          id=16,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='1e25e4d7f16abc08fc4d3823732f9991b7b6fa5c7018f4e75ac755153f287502',
          id=17,
          lineno=1,
          tokens=10,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body='import { Icon } from "@/components/Icons"'),
 Fragment(document_cs='1e25e4d7f16abc08fc4d3823732f9991b7b6fa5c7018f4e75ac755153f287502',
          id=18,
          lineno=3,
          tokens=25,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='SidebarOption',
          body='interface SidebarOption {\n'
               '  id: number\n'
               '  name: string\n'
               '  href: string\n'
               '  Icon: Icon\n'
               '}'),
 Fragment(document_cs='1e25e4d7f16abc08fc4d3823732f9991b7b6fa5c7018f4e75ac755153f287502',
          id=19,
          lineno=1,
          tokens=12,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: SidebarOption\n  Usages: Icon\n'),
 Fragment(document_cs='2107cbcf9e771d83babc938d59d6b89a50435945408f3ae8475a5d0aa016270e',
          id=20,
          lineno=1,
          tokens=96,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body='import { getFriendsByUserId } from '
               "'@/helpers/get-friends-by-user-id'import { fetchRedis } from "
               "'@/helpers/redis'import { authOptions } from "
               "'@/lib/auth'import { chatHrefConstructor } from "
               "'@/lib/utils'import { ChevronRight } from 'lucide-react'import "
               "{ getServerSession } from 'next-auth'import Image from "
               "'next/image'import Link from 'next/link'import { notFound } "
               "from 'next/navigation'"),
 Fragment(document_cs='2107cbcf9e771d83babc938d59d6b89a50435945408f3ae8475a5d0aa016270e',
          id=21,
          lineno=13,
          tokens=9,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='session',
          body='session = await getServerSession(authOptions)'),
 Fragment(document_cs='2107cbcf9e771d83babc938d59d6b89a50435945408f3ae8475a5d0aa016270e',
          id=22,
          lineno=16,
          tokens=11,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='friends',
          body='friends = await getFriendsByUserId(session.user.id)'),
 Fragment(document_cs='2107cbcf9e771d83babc938d59d6b89a50435945408f3ae8475a5d0aa016270e',
          id=23,
          lineno=18,
          tokens=98,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='friendsWithLastMessage',
          body='friendsWithLastMessage = await Promise.all(\n'
               '    friends.map(async (friend) => {\n'
               '      const [lastMessageRaw] = (await fetchRedis(\n'
               "        'zrange',\n"
               '        `chat:${chatHrefConstructor(session.user.id, '
               'friend.id)}:messages`,\n'
               '        -1,\n'
               '        -1\n'
               '      )) as string[]\n'
               '\n'
               '      const lastMessage = JSON.parse(lastMessageRaw) as '
               'Message\n'
               '\n'
               '      return {\n'
               '        ...friend,\n'
               '        lastMessage,\n'
               '      }\n'
               '    })\n'
               '  )'),
 Fragment(document_cs='2107cbcf9e771d83babc938d59d6b89a50435945408f3ae8475a5d0aa016270e',
          id=24,
          lineno=27,
          tokens=11,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='lastMessage',
          body='lastMessage = JSON.parse(lastMessageRaw) as Message'),
 Fragment(document_cs='2107cbcf9e771d83babc938d59d6b89a50435945408f3ae8475a5d0aa016270e',
          id=25,
          lineno=1,
          tokens=63,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: friends friendsWithLastMessage lastMessage '
               'session\n'
               '  Usages: ChevronRight Image JSON Link Message Nothing Promise '
               'Recent authOptions chatHrefConstructor chats className default '
               'div fetchRedis fill friend getFriendsByUserId getServerSession '
               'here href image key lastMessageRaw name notFound page picture '
               'profile show span src text\n'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=26,
          lineno=1,
          tokens=15,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import Pusher from 'pusher';import fetch from 'node-fetch';"),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=27,
          lineno=4,
          tokens=9,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='appId',
          body='appId = process.env.PUSHER_APP_ID'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=28,
          lineno=5,
          tokens=9,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='key',
          body='key = process.env.PUSHER_APPKEY'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=29,
          lineno=6,
          tokens=9,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='secret',
          body='secret = process.env.PUSHER_APP_SECRET'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=30,
          lineno=7,
          tokens=9,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='cluster',
          body='cluster = process.env.PUSHER_APP_CLUSTER'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=31,
          lineno=8,
          tokens=15,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='upstashRedisRestUrl',
          body='upstashRedisRestUrl = process.env.UPSTASH_REDIS_REST_URL'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=32,
          lineno=14,
          tokens=26,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='pusher',
          body='pusher = new Pusher({\n'
               '  appId,\n'
               '  key,\n'
               '  secret,\n'
               '  cluster,\n'
               '  useTLS: true,\n'
               '})'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=33,
          lineno=22,
          tokens=117,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='redis',
          body='redis = {\n'
               '  get: async (key: string) => {\n'
               '    const response = await '
               'fetch(`${upstashRedisRestUrl}/get/${key}`);\n'
               '    const data = await response.json();\n'
               '    return data.value;\n'
               '  },\n'
               '  set: async (key: string, value: string) => {\n'
               '    await fetch(`${upstashRedisRestUrl}/set/${key}`, {\n'
               "      method: 'POST',\n"
               "      headers: { 'Content-Type': 'application/json' },\n"
               '      body: JSON.stringify({ value }),\n'
               '    });\n'
               '  },\n'
               '  // Add other Redis operations as needed...\n'
               '}'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=34,
          lineno=24,
          tokens=16,
          depth=7,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body='response = await fetch(`${upstashRedisRestUrl}/get/${key}`)'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=35,
          lineno=25,
          tokens=6,
          depth=7,
          parent_id=None,
          category='variable',
          summary=False,
          name='data',
          body='data = await response.json()'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=36,
          lineno=38,
          tokens=12,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='chatHelper',
          body='chatHelper = {\n  pusher,\n  redis,\n}'),
 Fragment(document_cs='22ad7e8a3c3a40adb84fd42bcf8a64fce8c41a48bb76b42fc58e72a25ed2b259',
          id=37,
          lineno=1,
          tokens=32,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: appId chatHelper cluster data key pusher redis '
               'response secret upstashRedisRestUrl\n'
               '  Usages: Error JSON Pusher fetch process value\n'),
 Fragment(document_cs='2608df8df4f0b01124702410a9db147dc40a761246dc3b26535b225f738ebf3f',
          id=38,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='27016e7851f7cd7b3a53f49521bce3b1975ebf8b01f756380af4daf374d8e69c',
          id=39,
          lineno=7,
          tokens=4,
          depth=8,
          parent_id=None,
          category='class',
          summary=False,
          name='px-6',
          body=':px-6'),
 Fragment(document_cs='27016e7851f7cd7b3a53f49521bce3b1975ebf8b01f756380af4daf374d8e69c',
          id=40,
          lineno=7,
          tokens=9,
          depth=6,
          parent_id=None,
          category='class',
          summary=False,
          name='px-8',
          body=':px-6 lg:px-8'),
 Fragment(document_cs='27016e7851f7cd7b3a53f49521bce3b1975ebf8b01f756380af4daf374d8e69c',
          id=41,
          lineno=11,
          tokens=5,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='scrollbar-w-2',
          body='.scrollbar-w-2'),
 Fragment(document_cs='27016e7851f7cd7b3a53f49521bce3b1975ebf8b01f756380af4daf374d8e69c',
          id=42,
          lineno=16,
          tokens=6,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='scrollbar-track-blue-lighter',
          body='.scrollbar-track-blue-lighter'),
 Fragment(document_cs='27016e7851f7cd7b3a53f49521bce3b1975ebf8b01f756380af4daf374d8e69c',
          id=43,
          lineno=22,
          tokens=4,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='scrollbar-thumb-blue',
          body='.scrollbar-thumb-blue'),
 Fragment(document_cs='27016e7851f7cd7b3a53f49521bce3b1975ebf8b01f756380af4daf374d8e69c',
          id=44,
          lineno=28,
          tokens=4,
          depth=4,
          parent_id=None,
          category='class',
          summary=False,
          name='scrollbar-thumb-rounded',
          body='.scrollbar-thumb-rounded'),
 Fragment(document_cs='27016e7851f7cd7b3a53f49521bce3b1975ebf8b01f756380af4daf374d8e69c',
          id=45,
          lineno=1,
          tokens=8,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body="  Classes: {' '.join(classes)}\n"),
 Fragment(document_cs='2f12cd20f94987df71e4f6ce1bc1e1bc273651125f29d2d49836b1e9a3db021b',
          id=46,
          lineno=1,
          tokens=9,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { z } from 'zod'"),
 Fragment(document_cs='2f12cd20f94987df71e4f6ce1bc1e1bc273651125f29d2d49836b1e9a3db021b',
          id=47,
          lineno=3,
          tokens=16,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='addFriendValidator',
          body='addFriendValidator = z.object({\n'
               '  email: z.string().email(),\n'
               '})'),
 Fragment(document_cs='2f12cd20f94987df71e4f6ce1bc1e1bc273651125f29d2d49836b1e9a3db021b',
          id=48,
          lineno=1,
          tokens=7,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: addFriendValidator\n'),
 Fragment(document_cs='3363c98950477c82f0a9e786e9a62527328ffc430950786175638bc1922d6971',
          id=49,
          lineno=3,
          tokens=19,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import Button from '@/components/ui/Button'import { signOut } "
               "from 'next-auth/react'"),
 Fragment(document_cs='3363c98950477c82f0a9e786e9a62527328ffc430950786175638bc1922d6971',
          id=50,
          lineno=6,
          tokens=21,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='Home',
          body='function Home() {\n'
               '  return <button onClick={() => signOut()}>Sign out</button>\n'
               '}'),
 Fragment(document_cs='3363c98950477c82f0a9e786e9a62527328ffc430950786175638bc1922d6971',
          id=51,
          lineno=1,
          tokens=17,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: Home\n'
               '  Usages: Button Sign button onClick out signOut\n'),
 Fragment(document_cs='45dac4fd5e264734b0365b2325294b8f1e2c13f089a0a9ed9d78b17f0e032bf4',
          id=52,
          lineno=1,
          tokens=11,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { Redis } from '@upstash/redis';"),
 Fragment(document_cs='45dac4fd5e264734b0365b2325294b8f1e2c13f089a0a9ed9d78b17f0e032bf4',
          id=53,
          lineno=3,
          tokens=13,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='redisRestUrl',
          body='redisRestUrl = process.env.UPSTASH_REDIS_REST_URL'),
 Fragment(document_cs='45dac4fd5e264734b0365b2325294b8f1e2c13f089a0a9ed9d78b17f0e032bf4',
          id=54,
          lineno=4,
          tokens=13,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='redisRestToken',
          body='redisRestToken = process.env.UPSTASH_REDIS_REST_TOKEN'),
 Fragment(document_cs='45dac4fd5e264734b0365b2325294b8f1e2c13f089a0a9ed9d78b17f0e032bf4',
          id=55,
          lineno=10,
          tokens=18,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='config',
          body='config = {\n  url: redisRestUrl,\n  token: redisRestToken,\n}'),
 Fragment(document_cs='45dac4fd5e264734b0365b2325294b8f1e2c13f089a0a9ed9d78b17f0e032bf4',
          id=56,
          lineno=15,
          tokens=6,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='db',
          body='db = new Redis(config)'),
 Fragment(document_cs='45dac4fd5e264734b0365b2325294b8f1e2c13f089a0a9ed9d78b17f0e032bf4',
          id=57,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: config redisRestToken redisRestUrl\n'
               '  Usages: Error Redis process\n'),
 Fragment(document_cs='48e21b90d49ced2c5aa826a10acfce163dee72173ea8d98ec07eae6641f87e9a',
          id=58,
          lineno=1,
          tokens=13,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import Providers from '@/components/Providers'import "
               "'./globals.css'"),
 Fragment(document_cs='48e21b90d49ced2c5aa826a10acfce163dee72173ea8d98ec07eae6641f87e9a',
          id=59,
          lineno=10,
          tokens=50,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='RootLayout',
          body='function RootLayout({\n'
               '  children,\n'
               '}: {\n'
               '  children: React.ReactNode\n'
               '}) {\n'
               '  return (\n'
               "    <html lang='en'>\n"
               '      <body>\n'
               '        <Providers>{children}</Providers>\n'
               '      </body>\n'
               '    </html>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='48e21b90d49ced2c5aa826a10acfce163dee72173ea8d98ec07eae6641f87e9a',
          id=60,
          lineno=5,
          tokens=34,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='metadata',
          body='metadata = {\n'
               "  title: 'Macro Integrations Portal | Home',\n"
               "  description: 'Welcome to Macro Integrations Artifical "
               "Intelligence Assistant (MI-AI)',\n"
               '}'),
 Fragment(document_cs='48e21b90d49ced2c5aa826a10acfce163dee72173ea8d98ec07eae6641f87e9a',
          id=61,
          lineno=1,
          tokens=23,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: RootLayout\n'
               '  Variables: metadata\n'
               '  Usages: Providers React ReactNode body html lang\n'),
 Fragment(document_cs='4a2caf16567cb33e3e732b8ea1bdee1955c1c24614a390a1e556c31f9fbff68e',
          id=62,
          lineno=1,
          tokens=7,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Usages: module require\n'),
 Fragment(document_cs='52666cc11c423d2d669ae17389d08ca42f88002d6b9f21728c94c862a2d6c940',
          id=63,
          lineno=3,
          tokens=138,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { Transition, Dialog } from '@headlessui/react'import { "
               "Menu, X } from 'lucide-react'import Image from "
               "'next/image'import Link from 'next/link'import { FC, Fragment, "
               "useEffect, useState } from 'react'import { Icons } from "
               "'./Icons'import SignOutButton from './SignOutButton'import "
               "Button, { buttonVariants } from './ui/Button'import "
               'FriendRequestSidebarOptions from '
               "'./FriendRequestSidebarOptions'import SidebarChatList from "
               "'./SidebarChatList'import { Session } from 'next-auth'import { "
               "SidebarOption } from '@/types/typings'import { usePathname } "
               "from 'next/navigation'"),
 Fragment(document_cs='52666cc11c423d2d669ae17389d08ca42f88002d6b9f21728c94c862a2d6c940',
          id=64,
          lineno=17,
          tokens=31,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='MobileChatLayoutProps',
          body='interface MobileChatLayoutProps {\n'
               '  friends: User[]\n'
               '  session: Session\n'
               '  sidebarOptions: SidebarOption[]\n'
               '  unseenRequestCount: number\n'
               '}'),
 Fragment(document_cs='52666cc11c423d2d669ae17389d08ca42f88002d6b9f21728c94c862a2d6c940',
          id=65,
          lineno=24,
          tokens=180,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='MobileChatLayout',
          body='MobileChatLayout: FC<MobileChatLayoutProps> = ({ friends, '
               'session, sidebarOptions, unseenRequestCount }) => {\n'
               '  const [open, setOpen] = useState<boolean>(false)\n'
               '\n'
               '  const pathname = usePathname()\n'
               '\n'
               '  useEffect(() => {\n'
               '    setOpen(false)\n'
               '  }, [pathname])\n'
               '\n'
               '  return (\n'
               "    <div className='fixed bg-zinc-50 border-b border-zinc-200 "
               "top-0 inset-x-0 py-2 px-4'>\n"
               "      <div className='w-full flex justify-between "
               "items-center'>\n"
               '        <Link\n'
               "          href='/dashboard'\n"
               "          className={buttonVariants({ variant: 'ghost' })}>\n"
               "          <Icons.Logo className='h-6 w-auto text-indigo-600' "
               '/>\n'
               '        </Link>\n'
               '        <Button onClick={() => setOpen(true)} '
               "className='gap-4'>\n"
               "          Menu <Menu className='h-6 w"),
 Fragment(document_cs='52666cc11c423d2d669ae17389d08ca42f88002d6b9f21728c94c862a2d6c940',
          id=66,
          lineno=27,
          tokens=6,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='pathname',
          body='pathname = usePathname()'),
 Fragment(document_cs='52666cc11c423d2d669ae17389d08ca42f88002d6b9f21728c94c862a2d6c940',
          id=67,
          lineno=42,
          tokens=151,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='MobileChatLayout',
          body="-6' />\n"
               '        </Button>\n'
               '      </div>\n'
               '      <Transition.Root show={open} as={Fragment}>\n'
               "        <Dialog as='div' className='relative z-10' "
               'onClose={setOpen}>\n'
               "          <div className='fixed inset-0' />\n"
               '\n'
               "          <div className='fixed inset-0 overflow-hidden'>\n"
               "            <div className='absolute inset-0 "
               "overflow-hidden'>\n"
               "              <div className='pointer-events-none fixed "
               "inset-y-0 left-0 flex max-w-full pr-10'>\n"
               '                <Transition.Child\n'
               '                  as={Fragment}\n'
               "                  enter='transform transition ease-in-out "
               "duration-500 sm:duration-700'\n"
               "                  enterFrom='-translate-x-full'\n"
               "                  enterTo='translate-x-0'\n"
               "                  leave='transform tran"),
 Fragment(document_cs='52666cc11c423d2d669ae17389d08ca42f88002d6b9f21728c94c862a2d6c940',
          id=68,
          lineno=57,
          tokens=133,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='MobileChatLayout',
          body="sition ease-in-out duration-500 sm:duration-700'\n"
               "                  leaveFrom='translate-x-0'\n"
               "                  leaveTo='-translate-x-full'>\n"
               "                  <Dialog.Panel className='pointer-events-auto "
               "w-screen max-w-md'>\n"
               "                    <div className='flex h-full flex-col "
               "overflow-hidden bg-white py-6 shadow-xl'>\n"
               "                      <div className='px-4 sm:px-6'>\n"
               "                        <div className='flex items-start "
               "justify-between'>\n"
               "                          <Dialog.Title className='text-base "
               "font-semibold leading-6 text-gray-900'>\n"
               '                            Dashboard\n'
               '                          </Dialog.Title>\n'
               "                          <div className='ml-3 flex h-7 "
               "items-center'>\n"
               '  '),
 Fragment(document_cs='52666cc11c423d2d669ae17389d08ca42f88002d6b9f21728c94c862a2d6c940',
          id=69,
          lineno=68,
          tokens=128,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='MobileChatLayout',
          body='                          <button\n'
               "                              type='button'\n"
               "                              className='rounded-md bg-white "
               'text-gray-400 hover:text-gray-500 focus:outline-none '
               "focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2'\n"
               '                              onClick={() => setOpen(false)}>\n'
               "                              <span className='sr-only'>Close "
               'panel</span>\n'
               "                              <X className='h-6 w-6' "
               "aria-hidden='true' />\n"
               '                            </button>\n'
               '                          </div>\n'
               '                        </div>\n'
               '                      </div>\n'
               "                      <div className='relative mt-6 flex-1 "
               "px-4 sm:px-6'>\n"
               '                        {/* Content */}'),
 Fragment(document_cs='52666cc11c423d2d669ae17389d08ca42f88002d6b9f21728c94c862a2d6c940',
          id=70,
          lineno=104,
          tokens=7,
          depth=16,
          parent_id=None,
          category='variable',
          summary=False,
          name='Icon',
          body='Icon = Icons[option.Icon]'),
 Fragment(document_cs='52666cc11c423d2d669ae17389d08ca42f88002d6b9f21728c94c862a2d6c940',
          id=71,
          lineno=1,
          tokens=120,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: MobileChatLayoutProps\n'
               '  Variables: Icon MobileChatLayout pathname\n'
               '  Usages: Button Child Close Dashboard Dialog FC Fragment '
               'FriendRequestSidebarOptions Icons Image Link Menu Overview '
               'Panel Root Session SidebarChatList SidebarOption SignOutButton '
               'Title Transition User X Your absolute alt aria button '
               'buttonVariants chats className default div duration ease '
               'enterTo events fill fixed flex friends full hidden href '
               'initialUnseenRequestCount inset key leave leaveFrom leaveTo '
               'left max name nav none onClick open option out overflow panel '
               'pointer profile referrerPolicy relative role sessionId setOpen '
               'span src transform transition translate type useEffect '
               'usePathname useState\n'),
 Fragment(document_cs='551bd3b3357f01180de96a24b44916868c868963e40133b05a1a1234b3548444',
          id=72,
          lineno=1,
          tokens=24,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { NextApiRequest, NextApiResponse } from 'next'import { "
               "fetchRedis } from '@/helpers/redis';"),
 Fragment(document_cs='551bd3b3357f01180de96a24b44916868c868963e40133b05a1a1234b3548444',
          id=73,
          lineno=4,
          tokens=123,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='handler',
          body='async function handler(req: NextApiRequest, res: '
               'NextApiResponse) {\n'
               "  if (req.method === 'POST') {\n"
               '    const { projectCode } = req.body\n'
               '\n'
               '    // Check if the project code is valid\n'
               "    const isValid = await fetchRedis('sismember', "
               "'projectCodes', projectCode)\n"
               '\n'
               '    if (isValid) {\n'
               '      res.status(200).json({ isValid: true })\n'
               '    } else {\n'
               '      res.status(400).json({ isValid: false })\n'
               '    }\n'
               '  } else {\n'
               "    res.status(405).json({ message: 'Method not allowed' })\n"
               '  }\n'
               '}'),
 Fragment(document_cs='551bd3b3357f01180de96a24b44916868c868963e40133b05a1a1234b3548444',
          id=74,
          lineno=9,
          tokens=17,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='isValid',
          body="isValid = await fetchRedis('sismember', 'projectCodes', "
               'projectCode)'),
 Fragment(document_cs='551bd3b3357f01180de96a24b44916868c868963e40133b05a1a1234b3548444',
          id=75,
          lineno=1,
          tokens=26,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: handler\n'
               '  Variables: isValid\n'
               '  Usages: NextApiRequest NextApiResponse fetchRedis '
               'projectCode req res\n'),
 Fragment(document_cs='5ba94b86e1220a94d7104ea23410d9fbb180aa93c6a92f6fe73d0e73d31c53dd',
          id=76,
          lineno=1,
          tokens=22,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='IncomingFriendRequest',
          body='interface IncomingFriendRequest {\n'
               '  senderId: string\n'
               '  senderEmail: string | null | undefined\n'
               '}'),
 Fragment(document_cs='5ba94b86e1220a94d7104ea23410d9fbb180aa93c6a92f6fe73d0e73d31c53dd',
          id=77,
          lineno=1,
          tokens=7,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: IncomingFriendRequest\n'),
 Fragment(document_cs='5df8db75a40c2b83837edfe079d81403d13d20cc4916d3665b5f8f8226880fb6',
          id=78,
          lineno=1,
          tokens=7,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import fetch from 'node-fetch';"),
 Fragment(document_cs='5df8db75a40c2b83837edfe079d81403d13d20cc4916d3665b5f8f8226880fb6',
          id=79,
          lineno=8,
          tokens=104,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='fetchRedis',
          body='async function fetchRedis(\n'
               '  command: Command,\n'
               '  ...args: (string | number)[]\n'
               ') {\n'
               '  const commandUrl = '
               "`${upstashRedisRestUrl}/${command}/${args.join('/')}`;\n"
               '\n'
               '  const response = await fetch(commandUrl, {\n'
               '    headers: {\n'
               '      Authorization: `Bearer ${authToken}`,\n'
               '    },\n'
               '  });\n'
               '\n'
               '  if (!response.ok) {\n'
               '    throw new Error(`Error executing Redis command: '
               '${response.statusText}`);\n'
               '  }\n'
               '\n'
               '  const data = await response.json();\n'
               '  return data.result;\n'
               '}'),
 Fragment(document_cs='5df8db75a40c2b83837edfe079d81403d13d20cc4916d3665b5f8f8226880fb6',
          id=80,
          lineno=3,
          tokens=15,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='upstashRedisRestUrl',
          body='upstashRedisRestUrl = process.env.UPSTASH_REDIS_REST_URL'),
 Fragment(document_cs='5df8db75a40c2b83837edfe079d81403d13d20cc4916d3665b5f8f8226880fb6',
          id=81,
          lineno=4,
          tokens=12,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='authToken',
          body='authToken = process.env.UPSTASH_REDIS_REST_TOKEN'),
 Fragment(document_cs='5df8db75a40c2b83837edfe079d81403d13d20cc4916d3665b5f8f8226880fb6',
          id=82,
          lineno=12,
          tokens=16,
          depth=4,
          parent_id=None,
          category='variable',
          summary=False,
          name='commandUrl',
          body='commandUrl = '
               "`${upstashRedisRestUrl}/${command}/${args.join('/')}`"),
 Fragment(document_cs='5df8db75a40c2b83837edfe079d81403d13d20cc4916d3665b5f8f8226880fb6',
          id=83,
          lineno=14,
          tokens=25,
          depth=4,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body='response = await fetch(commandUrl, {\n'
               '    headers: {\n'
               '      Authorization: `Bearer ${authToken}`,\n'
               '    },\n'
               '  })'),
 Fragment(document_cs='5df8db75a40c2b83837edfe079d81403d13d20cc4916d3665b5f8f8226880fb6',
          id=84,
          lineno=24,
          tokens=6,
          depth=4,
          parent_id=None,
          category='variable',
          summary=False,
          name='data',
          body='data = await response.json()'),
 Fragment(document_cs='5df8db75a40c2b83837edfe079d81403d13d20cc4916d3665b5f8f8226880fb6',
          id=85,
          lineno=1,
          tokens=31,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: fetchRedis\n'
               '  Variables: authToken commandUrl data response '
               'upstashRedisRestUrl\n'
               '  Usages: Command Error args command fetch process\n'),
 Fragment(document_cs='64b997c42c2994f87f5131ca21b34f8c9d564426547f8584421a2d30f1772271',
          id=86,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='64f38c15f08eed2decd551c77be21d21c5bfd27e5687da22770d6d2622b2c536',
          id=87,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='68864de0900429a3c95e88ac89dc036982130b440e266a3d5e569cc398c7d455',
          id=88,
          lineno=1,
          tokens=118,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# See https://help.github.com/articles/ignoring-files/ for '
               'more about ignoring files.\n'
               '\n'
               '# dependencies\n'
               '/node_modules\n'
               '/.pnp\n'
               '.pnp.js\n'
               '\n'
               '# testing\n'
               '/coverage\n'
               '\n'
               '# next.js\n'
               '/.next/\n'
               '/out/\n'
               '\n'
               '# production\n'
               '/build\n'
               '\n'
               '# misc\n'
               '.DS_Store\n'
               '*.pem\n'
               '\n'
               '# debug\n'
               'npm-debug.log*\n'
               'yarn-debug.log*\n'
               'yarn-error.log*\n'
               '.pnpm-debug.log*\n'
               '\n'
               '# local env files\n'
               '.env*.local\n'
               '\n'
               '# vercel\n'
               '.vercel\n'
               '\n'
               '# typescript\n'
               '*.tsbuildinfo\n'
               'next-env.d.ts\n'
               '.env\n'),
 Fragment(document_cs='68864de0900429a3c95e88ac89dc036982130b440e266a3d5e569cc398c7d455',
          id=89,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='68d9ec0c2e3e3a2d247684802800bf0fca144a80b36160cef7d15a3461eecf9e',
          id=90,
          lineno=1,
          tokens=11,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { fetchRedis } from '../helpers/redis';"),
 Fragment(document_cs='68d9ec0c2e3e3a2d247684802800bf0fca144a80b36160cef7d15a3461eecf9e',
          id=91,
          lineno=3,
          tokens=50,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='verifyProjectCode',
          body='async function verifyProjectCode(projectCode: string): '
               'Promise<boolean> {\n'
               '  // Check if the project code exists in your Redis database\n'
               "  const project = await fetchRedis('get', "
               '`project:${projectCode}`);\n'
               '  return project !== null;\n'
               '}'),
 Fragment(document_cs='68d9ec0c2e3e3a2d247684802800bf0fca144a80b36160cef7d15a3461eecf9e',
          id=92,
          lineno=5,
          tokens=15,
          depth=4,
          parent_id=None,
          category='variable',
          summary=False,
          name='project',
          body="project = await fetchRedis('get', `project:${projectCode}`)"),
 Fragment(document_cs='68d9ec0c2e3e3a2d247684802800bf0fca144a80b36160cef7d15a3461eecf9e',
          id=93,
          lineno=1,
          tokens=22,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: verifyProjectCode\n'
               '  Variables: project\n'
               '  Usages: Promise fetchRedis projectCode\n'),
 Fragment(document_cs='68e41f41e084395db2481464485c5726d782cb51e25728e9093982c09e635134',
          id=94,
          lineno=3,
          tokens=27,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body='import type { NextApiRequest, NextApiResponse } from '
               "'next';import smartsheetHelper from "
               "'../../../helpers/smartsheetHelper';"),
 Fragment(document_cs='68e41f41e084395db2481464485c5726d782cb51e25728e9093982c09e635134',
          id=95,
          lineno=6,
          tokens=185,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='handler',
          body='async function handler(\n'
               '  req: NextApiRequest,\n'
               '  res: NextApiResponse\n'
               ') {\n'
               "  if (req.method === 'POST') {\n"
               '    const { siteNumber } = req.body;\n'
               '    try {\n'
               '      const rows = await '
               'smartsheetHelper.getRowsBySite(siteNumber);\n'
               '      if (rows.length === 0) {\n'
               "        res.status(404).json({ message: 'No rows found for "
               "this site number.' });\n"
               '        return;\n'
               '      }\n'
               '      for (const row of rows) {\n'
               '        await smartsheetHelper.checkOut(row);\n'
               '      }\n'
               "      res.status(200).json({ message: 'Successfully checked "
               "out.' });\n"
               '    } catch (error) {\n'
               '      res.status(500).json({ message: `Error checking out: '
               '${(error as any).message}` });\n'
               '    }\n'
               '  } else {\n'
               "    res.status(405).json({ message: 'Method not allowed.' });\n"
               '  }\n'
               '}'),
 Fragment(document_cs='68e41f41e084395db2481464485c5726d782cb51e25728e9093982c09e635134',
          id=96,
          lineno=13,
          tokens=14,
          depth=8,
          parent_id=None,
          category='variable',
          summary=False,
          name='rows',
          body='rows = await smartsheetHelper.getRowsBySite(siteNumber)'),
 Fragment(document_cs='68e41f41e084395db2481464485c5726d782cb51e25728e9093982c09e635134',
          id=97,
          lineno=1,
          tokens=30,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: handler\n'
               '  Variables: rows\n'
               '  Usages: NextApiRequest NextApiResponse error req res row '
               'siteNumber smartsheetHelper\n'),
 Fragment(document_cs='6e5a42c6bd76ef8f1082e0eb6020d53fa4c1c74ee146f9aea1a4030b729f4ca5',
          id=98,
          lineno=3,
          tokens=52,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import Button from '@/components/ui/Button'import { FC } from "
               "'react'import { signIn } from 'next-auth/react'import { toast "
               "} from 'react-hot-toast'import { useForm } from "
               "'react-hook-form'import React from 'react'"),
 Fragment(document_cs='6e5a42c6bd76ef8f1082e0eb6020d53fa4c1c74ee146f9aea1a4030b729f4ca5',
          id=99,
          lineno=18,
          tokens=64,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='loginWithSmartsheet',
          body='async function loginWithSmartsheet() {\n'
               '    setIsLoading(true)\n'
               '    try {\n'
               "      await signIn('smartsheet')\n"
               '    } catch (error) {\n'
               '      // display error message to user\n'
               "      toast.error('Something went wrong with your login.')\n"
               '    } finally {\n'
               '      setIsLoading(false)\n'
               '    }\n'
               '  }'),
 Fragment(document_cs='6e5a42c6bd76ef8f1082e0eb6020d53fa4c1c74ee146f9aea1a4030b729f4ca5',
          id=100,
          lineno=30,
          tokens=154,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='onSubmit',
          body='onSubmit = async (data: FormData) => {\n'
               '    setIsLoading(true)\n'
               '\n'
               '    // Call the API endpoint to validate the project code\n'
               "    const response = await fetch('/api/projectCodes', {\n"
               "      method: 'POST',\n"
               '      headers: {\n'
               "        'Content-Type': 'application/json',\n"
               '      },\n'
               '      body: JSON.stringify({ projectCode: data.projectCode '
               '}),\n'
               '    })\n'
               '\n'
               '    if (response.ok) {\n'
               '      // If the project code is valid, sign in the user as a '
               'technician\n'
               "      await signIn('credentials', { callbackUrl: '/', "
               'projectCode: data.projectCode })\n'
               '    } else {\n'
               '      // If the project code is not valid, display an error '
               'message\n'
               "      toast.error('Invalid project code.')\n"
               '    }\n'
               '\n'
               '    setIsLoading(false)\n'
               '  }'),
 Fragment(document_cs='6e5a42c6bd76ef8f1082e0eb6020d53fa4c1c74ee146f9aea1a4030b729f4ca5',
          id=101,
          lineno=34,
          tokens=46,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body="response = await fetch('/api/projectCodes', {\n"
               "      method: 'POST',\n"
               '      headers: {\n'
               "        'Content-Type': 'application/json',\n"
               '      },\n'
               '      body: JSON.stringify({ projectCode: data.projectCode '
               '}),\n'
               '    })'),
 Fragment(document_cs='6e5a42c6bd76ef8f1082e0eb6020d53fa4c1c74ee146f9aea1a4030b729f4ca5',
          id=102,
          lineno=1,
          tokens=65,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: loginWithSmartsheet\n'
               '  Variables: onSubmit response\n'
               '  Usages: Button FC FormData JSON Login Page React Sign '
               'Smartsheet Technician account aria className data default div '
               'error fetch fill focusable form hidden icon input isLoading '
               'logo null path prefix register required role setIsLoading '
               'signIn svg toast type useForm viewBox xmlns your\n'),
 Fragment(document_cs='6e746b599555ccd6f9e5eea9747b505ed2f80ab718feafbb7b6cf0088aaf3bab',
          id=103,
          lineno=1,
          tokens=16,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { LucideProps, UserPlus } from 'lucide-react'"),
 Fragment(document_cs='6e746b599555ccd6f9e5eea9747b505ed2f80ab718feafbb7b6cf0088aaf3bab',
          id=104,
          lineno=3,
          tokens=144,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='Icons',
          body='Icons = {\n'
               '  Logo: (props: LucideProps) => (\n'
               "    <svg {...props} viewBox='0 0 2000 2000'>\n"
               '      <path\n'
               "        fill='currentColor'\n"
               "        d='m1976.678 "
               '964.142-1921.534-852.468c-14.802-6.571-32.107-3.37-43.577 '
               '8.046-11.477 11.413-14.763 28.703-8.28 43.532l365.839 '
               '836.751-365.839 836.749c-6.483 14.831-3.197 32.'),
 Fragment(document_cs='6e746b599555ccd6f9e5eea9747b505ed2f80ab718feafbb7b6cf0088aaf3bab',
          id=105,
          lineno=8,
          tokens=173,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='Icons',
          body='119 8.28 43.532 7.508 7.467 17.511 11.417 27.677 11.417 5.37 0 '
               '10.785-1.103 15.9-3.371l1921.533-852.466c14.18-6.292 '
               '23.322-20.349 '
               '23.322-35.861.001-15.514-9.141-29.571-23.321-35.861zm-1861.042-739.791 '
               '1664.615 738.489h-1341.737zm321.069 816.954h1334.219l-1655.287 '
               "734.35z'\n"
               '      />\n'
               '    </svg>\n'
               '  ),\n'
               '  UserPlus\n'
               '}'),
 Fragment(document_cs='6e746b599555ccd6f9e5eea9747b505ed2f80ab718feafbb7b6cf0088aaf3bab',
          id=106,
          lineno=1,
          tokens=21,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: Icons\n'
               '  Usages: Icon LucideProps UserPlus fill path props svg '
               'viewBox\n'),
 Fragment(document_cs='7b22ec63994eefadc433ba859790f1d6a932e9f7d49d2136b2a2b1ae94d038fb',
          id=107,
          lineno=1,
          tokens=47,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body='import type { NextApiRequest, NextApiResponse } from '
               "'next';import { getRowsBySite, getCellByColumnId } from "
               "'../../helpers/smartsheetHelper';import { sendChatSupport } "
               "from '../../helpers/chatHelper';"),
 Fragment(document_cs='7b22ec63994eefadc433ba859790f1d6a932e9f7d49d2136b2a2b1ae94d038fb',
          id=108,
          lineno=5,
          tokens=57,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='requestSupport',
          body='async function requestSupport(req: NextApiRequest, res: '
               'NextApiResponse) {\n'
               "  if (req.method === 'POST') {\n"
               '    const { siteNumber, name, phoneNumber, issue } = '
               'req.body;\n'
               '\n'
               '    try {\n'
               '      const rows = await getRowsBySite(siteNumber);\n'),
 Fragment(document_cs='7b22ec63994eefadc433ba859790f1d6a932e9f7d49d2136b2a2b1ae94d038fb',
          id=109,
          lineno=11,
          tokens=220,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='requestSupport',
          body='      for (const row of rows) {\n'
               '        const projectManagerCell = getCellByColumnId(row, '
               "'Project Manager');\n"
               '        const projectManager = '
               'projectManagerCell.display_value;\n'
               "        const chatId = '123'; // This should be the actual ID "
               'of the chat\n'
               '        const message = `Hello, a user has requested '
               'assistance. Here is the message they have asked me to provide: '
               '\\n\\nName: ${name}\\nPhone Number: ${phoneNumber}\\nIssue: '
               '${issue}\\n\\nWhen you are ready to assist this user please '
               '[Click Here](https://yourwebsite.com/chat/${chatId}) to join '
               'the chat with the user.`;\n'
               '        await sendChatSupport(projectManager, message);\n'
               '      }\n'
               '\n'
               "      res.status(200).json({ status: 'success' });\n"
               '    } catch (error) {\n'
               "      res.status(500).json({ status: 'error', message: "
               'error.message });\n'
               '    }\n'
               '  } else {\n'
               "    res.setHeader('Allow', ['POST']);\n"
               '    res.status(405).end(`Method ${req.method} Not Allowed`);\n'
               '  }\n'
               '}'),
 Fragment(document_cs='7b22ec63994eefadc433ba859790f1d6a932e9f7d49d2136b2a2b1ae94d038fb',
          id=110,
          lineno=10,
          tokens=10,
          depth=8,
          parent_id=None,
          category='variable',
          summary=False,
          name='rows',
          body='rows = await getRowsBySite(siteNumber)'),
 Fragment(document_cs='7b22ec63994eefadc433ba859790f1d6a932e9f7d49d2136b2a2b1ae94d038fb',
          id=111,
          lineno=12,
          tokens=15,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='projectManagerCell',
          body="projectManagerCell = getCellByColumnId(row, 'Project Manager')"),
 Fragment(document_cs='7b22ec63994eefadc433ba859790f1d6a932e9f7d49d2136b2a2b1ae94d038fb',
          id=112,
          lineno=13,
          tokens=8,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='projectManager',
          body='projectManager = projectManagerCell.display_value'),
 Fragment(document_cs='7b22ec63994eefadc433ba859790f1d6a932e9f7d49d2136b2a2b1ae94d038fb',
          id=113,
          lineno=14,
          tokens=6,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='chatId',
          body="chatId = '123'"),
 Fragment(document_cs='7b22ec63994eefadc433ba859790f1d6a932e9f7d49d2136b2a2b1ae94d038fb',
          id=114,
          lineno=15,
          tokens=76,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='message',
          body='message = `Hello, a user has requested assistance. Here is the '
               'message they have asked me to provide: \\n\\nName: '
               '${name}\\nPhone Number: ${phoneNumber}\\nIssue: '
               '${issue}\\n\\nWhen you are ready to assist this user please '
               '[Click Here](https://yourwebsite.com/chat/${chatId}) to join '
               'the chat with the user.`'),
 Fragment(document_cs='7b22ec63994eefadc433ba859790f1d6a932e9f7d49d2136b2a2b1ae94d038fb',
          id=115,
          lineno=1,
          tokens=50,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: requestSupport\n'
               '  Variables: chatId message projectManager projectManagerCell '
               'rows\n'
               '  Usages: NextApiRequest NextApiResponse error '
               'getCellByColumnId getRowsBySite issue name phoneNumber req res '
               'row sendChatSupport siteNumber\n'),
 Fragment(document_cs='7de61c6cdc9104e906e674b02c349aaf78f3e7931dd2ddd2c493fb7bf4829ab9',
          id=116,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='884ac670e71ec67a96c88e822f18b2d684406eaac027b67398ba37236bf3b6c1',
          id=117,
          lineno=2,
          tokens=33,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='nextConfig',
          body='nextConfig = {\n'
               '  experimental: {\n'
               '    appDir: true,\n'
               '  },\n'
               '  images: {\n'
               "    domains: ['lh3.googleusercontent.com']\n"
               '  }\n'
               '}'),
 Fragment(document_cs='884ac670e71ec67a96c88e822f18b2d684406eaac027b67398ba37236bf3b6c1',
          id=118,
          lineno=1,
          tokens=12,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: nextConfig\n  Usages: module\n'),
 Fragment(document_cs='8a43c96dc5d3bfa4856f8981b2803055a85068031551c908771fac87c3a48a25',
          id=119,
          lineno=1,
          tokens=24,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='User',
          body='interface User {\n'
               '  name: string\n'
               '  email: string\n'
               '  image: string\n'
               '  id: string\n'
               '}'),
 Fragment(document_cs='8a43c96dc5d3bfa4856f8981b2803055a85068031551c908771fac87c3a48a25',
          id=120,
          lineno=8,
          tokens=14,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='Chat',
          body='interface Chat {\n  id: string\n  messages: Message[]\n}'),
 Fragment(document_cs='8a43c96dc5d3bfa4856f8981b2803055a85068031551c908771fac87c3a48a25',
          id=121,
          lineno=13,
          tokens=31,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='Message',
          body='interface Message {\n'
               '  id: string\n'
               '  senderId: string\n'
               '  receiverId: string\n'
               '  text: string\n'
               '  timestamp: number\n'
               '}'),
 Fragment(document_cs='8a43c96dc5d3bfa4856f8981b2803055a85068031551c908771fac87c3a48a25',
          id=122,
          lineno=21,
          tokens=22,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='FriendRequest',
          body='interface FriendRequest {\n'
               '  id: string\n'
               '  senderId: string\n'
               '  receiverId: string\n'
               '}'),
 Fragment(document_cs='8a43c96dc5d3bfa4856f8981b2803055a85068031551c908771fac87c3a48a25',
          id=123,
          lineno=1,
          tokens=9,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: Chat FriendRequest Message User\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=124,
          lineno=1,
          tokens=153,
          depth=0,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='# THIS IS AN AUTOGENERATED FILE. DO NOT EDIT THIS FILE '
               'DIRECTLY.\n'
               '# yarn lockfile v1\n'
               '\n'
               '\n'
               '"@aashutoshrathi/word-wrap@^1.2.3":\n'
               '  version "1.2.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/@aashutoshrathi/word-wrap/-/word-wrap-1.2.6.tgz"\n'
               '  integrity '
               'sha512-1Yjs2SvM8TflER/OD3cOjhWWOZb58A2t7wpE2S9XfBYTiIl+XFhQG2bjy4Pu1I+EAlCNUzRDYDdFwFYUKvXcIA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=125,
          lineno=9,
          tokens=117,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@alloc/quick-lru@^5.2.0":\n'
               '  version "5.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz"\n'
               '  integrity '
               'sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=126,
          lineno=14,
          tokens=218,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@auth0/nextjs-auth0@^2.6.3":\n'
               '  version "2.6.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/@auth0/nextjs-auth0/-/nextjs-auth0-2.6.3.tgz"\n'
               '  integrity '
               'sha512-UCr3G8psBgfbN2w82VSkgMCDNV7Ywi3o6YcFhMiIkaNRnqudTks3cqYluuFchaK+HGDu9iWiachBVvuMuv2UTg==\n'
               '  dependencies:\n'
               '    "@panva/hkdf" "^1.0.2"\n'
               '    cookie "^0.5.0"\n'
               '    debug "^4.3.4"\n'
               '    http-errors "^1.8.1"\n'
               '    joi "^17.6.0"\n'
               '    jose "^4.9.2"\n'
               '    openid-client "^5.2.1"\n'
               '    tslib "^2.4.0"\n'
               '    url-join "^4.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=127,
          lineno=29,
          tokens=150,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@babel/runtime@^7.20.13", "@babel/runtime@^7.20.7", '
               '"@babel/runtime@^7.21.0":\n'
               '  version "7.22.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/@babel/runtime/-/runtime-7.22.6.tgz"\n'
               '  integrity '
               'sha512-wDb5pWm4WDdF6LFUde3Jl8WzPA+3ZbxYqkC6xAXuD3irdEHN1k0NfTRrJD8ZD378SJ61miMLCqIOXYhd8x+AJQ==\n'
               '  dependencies:\n'
               '    regenerator-runtime "^0.13.11"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=128,
          lineno=36,
          tokens=139,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@eslint-community/eslint-utils@^4.2.0":\n'
               '  version "4.4.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.4.0.tgz"\n'
               '  integrity '
               'sha512-1/sA4dwrzBAyeUoQ6oxahHKmrZvsnLCg4RfxW3ZFGGmQkSNQPFNLV9CUEFQP1x9EYXHTo5p6xdhZM1Ne9p/AfA==\n'
               '  dependencies:\n'
               '    eslint-visitor-keys "^3.3.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=129,
          lineno=43,
          tokens=124,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@eslint-community/regexpp@^4.4.0":\n'
               '  version "4.5.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.5.1.tgz"\n'
               '  integrity '
               'sha512-Z5ba73P98O1KUYCCJTUeVpja9RcGoMdncZ6T49FCUl2lN38JtCJ+3WgIDBv0AuY4WChU5PmtJmOCTlN6FZTFKQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=130,
          lineno=48,
          tokens=219,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@eslint/eslintrc@^2.0.2":\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@eslint/eslintrc/-/eslintrc-2.1.0.tgz"\n'
               '  integrity '
               'sha512-Lj7DECXqIVCqnqjjHMPna4vn6GJcMgul/wuS0je9OZ9gsL0zzDpKPVtcG1HaDVc+9y+qgXneTeUMbCqXJNpH1A==\n'
               '  dependencies:\n'
               '    ajv "^6.12.4"\n'
               '    debug "^4.3.2"\n'
               '    espree "^9.6.0"\n'
               '    globals "^13.19.0"\n'
               '    ignore "^5.2.0"\n'
               '    import-fresh "^3.2.1"\n'
               '    js-yaml "^4.1.0"\n'
               '    minimatch "^3.1.2"\n'
               '    strip-json-comments "^3.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=131,
          lineno=63,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@eslint/js@8.37.0":\n'
               '  version "8.37.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@eslint/js/-/js-8.37.0.tgz"\n'
               '  integrity '
               'sha512-x5vzdtOOGgFVDCUs81QRB2+liax8rFg3+7hqM+QhBG0/G3F1ZsoYl97UrqgHgQ9KKT7G6c4V+aTUCgu/n22v1A==\n'
               '\n'
               '"@hapi/hoek@^9.0.0":\n'
               '  version "9.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@hapi/hoek/-/hoek-9.3.0.tgz"\n'
               '  integrity '
               'sha512-/c6rf4UJlmHlC9b5BaNvzAcFv7HZ2QHaV0D4/HNlBdvFnvQq8RI4kYdhyPCl7Xj+oWvTWQ8ujhqS53LIgAe6KQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=132,
          lineno=73,
          tokens=138,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@hapi/topo@^5.0.0":\n'
               '  version "5.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@hapi/topo/-/topo-5.1.0.tgz"\n'
               '  integrity '
               'sha512-foQZKJig7Ob0BMAYBfcJk8d77QtOe7Wo4ox7ff1lQYoNNAb6jwcY1ncdoy2e9wQZzvNy7ODZCYJkK8kzmcAnAg==\n'
               '  dependencies:\n'
               '    "@hapi/hoek" "^9.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=133,
          lineno=80,
          tokens=246,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@headlessui/react@^1.7.13":\n'
               '  version "1.7.15"\n'
               '  resolved '
               '"https://registry.npmjs.org/@headlessui/react/-/react-1.7.15.tgz"\n'
               '  integrity '
               'sha512-OTO0XtoRQ6JPB1cKNFYBZv2Q0JMqMGNhYP1CjPvcJvjz8YGokz8oAj89HIYZGN0gZzn/4kk9iUpmMF4Q21Gsqw==\n'
               '  dependencies:\n'
               '    client-only "^0.0.1"\n'
               '\n'
               '"@hookform/resolvers@^3.0.0":\n'
               '  version "3.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/@hookform/resolvers/-/resolvers-3.1.1.tgz"\n'
               '  integrity '
               'sha512-tS16bAUkqjITNSvbJuO1x7MXbn7Oe8ZziDTJdA9mMvsoYthnOOiznOTGBYwbdlYBgU+tgpI/BtTU3paRbCuSlg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=134,
          lineno=92,
          tokens=159,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@humanwhocodes/config-array@^0.11.8":\n'
               '  version "0.11.10"\n'
               '  resolved '
               '"https://registry.npmjs.org/@humanwhocodes/config-array/-/config-array-0.11.10.tgz"\n'
               '  integrity '
               'sha512-KVVjQmNUepDVGXNuoRRdmmEjruj0KfiGSbS8LVc12LMsWDQzRXJ0qdhN8L8uUigKpfEHRhlaQFY0ib1tnUbNeQ==\n'
               '  dependencies:\n'
               '    "@humanwhocodes/object-schema" "^1.2.1"\n'
               '    debug "^4.1.1"\n'
               '    minimatch "^3.0.5"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=135,
          lineno=101,
          tokens=127,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@humanwhocodes/module-importer@^1.0.1":\n'
               '  version "1.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/@humanwhocodes/module-importer/-/module-importer-1.0.1.tgz"\n'
               '  integrity '
               'sha512-bxveV4V8v5Yb4ncFTT3rPSgZBOpCkjfK0y4oVVVJwIuDVBRMDXrPyXRL988i5ap9m9bnyEEjWfm5WkBmtffLfA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=136,
          lineno=106,
          tokens=127,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@humanwhocodes/object-schema@^1.2.1":\n'
               '  version "1.2.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/@humanwhocodes/object-schema/-/object-schema-1.2.1.tgz"\n'
               '  integrity '
               'sha512-ZnQMnLV4e7hDlUvw8H+U8ASL02SS2Gn6+9Ac3wGGLIe7+je2AeAOxPY+izIPJDfFDb7eDjev0Us8MO1iFRN8hA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=137,
          lineno=111,
          tokens=125,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@ioredis/commands@^1.1.1":\n'
               '  version "1.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@ioredis/commands/-/commands-1.2.0.tgz"\n'
               '  integrity '
               'sha512-Sx1pU8EM64o2BrqNpEO1CNLtKQwyhuXuqyfH7oGKCk+1a33d2r5saW8zNwm3j6BTExtjrv2BxTgzzkMwts6vGg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=138,
          lineno=116,
          tokens=183,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@jridgewell/gen-mapping@^0.3.2":\n'
               '  version "0.3.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.3.tgz"\n'
               '  integrity '
               'sha512-HLhSWOLRi875zjjMG/r+Nv0oCW8umGb0BgEhyX3dDX3egwZtB8PqLnjz3yedt8R5StBrzcg4aBpnh8UA9D1BoQ==\n'
               '  dependencies:\n'
               '    "@jridgewell/set-array" "^1.0.1"\n'
               '    "@jridgewell/sourcemap-codec" "^1.4.10"\n'
               '    "@jridgewell/trace-mapping" "^0.3.9"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=139,
          lineno=125,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@jridgewell/resolve-uri@3.1.0":\n'
               '  version "3.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.0.tgz"\n'
               '  integrity '
               'sha512-F2msla3tad+Mfht5cJq7LSXcdudKTWCVYUgw6pLFOOHSTtZlj6SWNYAp+AhuqLmWdBO2X5hPrLcu8cVP8fy28w==\n'
               '\n'
               '"@jridgewell/set-array@^1.0.1":\n'
               '  version "1.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/@jridgewell/set-array/-/set-array-1.1.2.tgz"\n'
               '  integrity '
               'sha512-xnkseuNADM0gt2bs+BvhO0p78Mk762YnZdsuzFV018NoG1Sj1SCQvpSqa7XUaTam5vAGasABV9qXASMKnFMwMw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=140,
          lineno=135,
          tokens=134,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@jridgewell/sourcemap-codec@^1.4.10":\n'
               '  version "1.4.15"\n'
               '  resolved '
               '"https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.4.15.tgz"\n'
               '  integrity '
               'sha512-eF2rxCRulEKXHTRiDrDy6erMYWqNw4LPdQ8UQA4huuxaQsVeRPFl2oM8oDGxMFhJUWZf9McpLtJasDDZb/Bpeg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=141,
          lineno=140,
          tokens=128,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@jridgewell/sourcemap-codec@1.4.14":\n'
               '  version "1.4.14"\n'
               '  resolved '
               '"https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.4.14.tgz"\n'
               '  integrity '
               'sha512-XPSJHWmi394fuUuzDnGz1wiKqWfo1yXecHQMRf2l6hztTO+nPru658AyDngaBe7isIxEkRsPR3FZh+s7iVa4Uw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=142,
          lineno=145,
          tokens=165,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@jridgewell/trace-mapping@^0.3.9":\n'
               '  version "0.3.18"\n'
               '  resolved '
               '"https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.18.tgz"\n'
               '  integrity '
               'sha512-w+niJYzMHdd7USdiH2U6869nqhD2nbfZXND5Yp93qIbEmnDNk7PD48o+YchRVpzMU7M6jVCbenTR7PA1FLQ9pA==\n'
               '  dependencies:\n'
               '    "@jridgewell/resolve-uri" "3.1.0"\n'
               '    "@jridgewell/sourcemap-codec" "1.4.14"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=143,
          lineno=153,
          tokens=143,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@next-auth/upstash-redis-adapter@^3.0.4":\n'
               '  version "3.0.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/@next-auth/upstash-redis-adapter/-/upstash-redis-adapter-3.0.4.tgz"\n'
               '  integrity '
               'sha512-az9hFemtnSry7YAaVvxPEwGZSbnK8xiRLX/C5bDsM1ibQWSx6aIp7QY3Kk4NSdqU6LONkXnjndKKhrUnwEmfFw==\n'
               '  dependencies:\n'
               '    uuid "^8.3.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=144,
          lineno=160,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@next/env@13.2.4":\n'
               '  version "13.2.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/@next/env/-/env-13.2.4.tgz"\n'
               '  integrity '
               'sha512-+Mq3TtpkeeKFZanPturjcXt+KHfKYnLlX6jMLyCrmpq6OOs4i1GqBOAauSkii9QeKCMTYzGppar21JU57b/GEA==\n'
               '\n'
               '"@next/eslint-plugin-next@13.2.4":\n'
               '  version "13.2.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/@next/eslint-plugin-next/-/eslint-plugin-next-13.2.4.tgz"\n'
               '  integrity '
               'sha512-ck1lI+7r1mMJpqLNa3LJ5pxCfOB1lfJncKmRJeJxcJqcngaFwylreLP7da6Rrjr6u2gVRTfmnkSkjc80IiQCwQ==\n'
               '  dependencies:\n'
               '    glob "7.1.7"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=145,
          lineno=172,
          tokens=134,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@next/swc-win32-x64-msvc@13.2.4":\n'
               '  version "13.2.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/@next/swc-win32-x64-msvc/-/swc-win32-x64-msvc-13.2.4.tgz"\n'
               '  integrity '
               'sha512-0MffFmyv7tBLlji01qc0IaPP/LVExzvj7/R5x1Jph1bTAIj4Vu81yFQWHHQAP6r4ff9Ukj1mBK6MDNVXm7Tcvw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=146,
          lineno=177,
          tokens=152,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@nodelib/fs.scandir@2.1.5":\n'
               '  version "2.1.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz"\n'
               '  integrity '
               'sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==\n'
               '  dependencies:\n'
               '    "@nodelib/fs.stat" "2.0.5"\n'
               '    run-parallel "^1.1.9"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=147,
          lineno=185,
          tokens=131,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@nodelib/fs.stat@^2.0.2", "@nodelib/fs.stat@2.0.5":\n'
               '  version "2.0.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz"\n'
               '  integrity '
               'sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=148,
          lineno=190,
          tokens=161,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@nodelib/fs.walk@^1.2.3", "@nodelib/fs.walk@^1.2.8":\n'
               '  version "1.2.8"\n'
               '  resolved '
               '"https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz"\n'
               '  integrity '
               'sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==\n'
               '  dependencies:\n'
               '    "@nodelib/fs.scandir" "2.1.5"\n'
               '    fastq "^1.6.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=149,
          lineno=198,
          tokens=122,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@panva/hkdf@^1.0.2":\n'
               '  version "1.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/@panva/hkdf/-/hkdf-1.1.1.tgz"\n'
               '  integrity '
               'sha512-dhPeilub1NuIG0X5Kvhh9lH4iW3ZsHlnzwgwbOlgwQ2wG1IqFzsgHqmKPk3WzsdWAeaxKJxgM0+W433RmN45GA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=150,
          lineno=203,
          tokens=177,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@pkgr/utils@^2.3.1":\n'
               '  version "2.4.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/@pkgr/utils/-/utils-2.4.2.tgz"\n'
               '  integrity '
               'sha512-POgTXhjrTfbTV63DiFXav4lBHiICLKKwDeaKn9Nphwj7WH6m0hMMCaJkMyRWjgtPFyRKRVoMXXjczsTQRDEhYw==\n'
               '  dependencies:\n'
               '    cross-spawn "^7.0.3"\n'
               '    fast-glob "^3.3.0"\n'
               '    is-glob "^4.0.3"\n'
               '    open "^9.1.0"\n'
               '    picocolors "^1.0.0"\n'
               '    tslib "^2.6.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=151,
          lineno=215,
          tokens=124,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@rushstack/eslint-patch@^1.1.3":\n'
               '  version "1.3.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/@rushstack/eslint-patch/-/eslint-patch-1.3.2.tgz"\n'
               '  integrity '
               'sha512-V+MvGwaHH03hYhY+k6Ef/xKd6RYlc4q8WBx+2ANmipHJcKuktNcI/NgEsJgdSUF6Lw32njT6OnrRsKYCdgHjYw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=152,
          lineno=220,
          tokens=247,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@sideway/address@^4.1.3":\n'
               '  version "4.1.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/@sideway/address/-/address-4.1.4.tgz"\n'
               '  integrity '
               'sha512-7vwq+rOHVWjyXxVlR76Agnvhy8I9rpzjosTESvmhNeXOXdZZB15Fl+TI9x1SiHZH5Jv2wTGduSxFDIaq0m3DUw==\n'
               '  dependencies:\n'
               '    "@hapi/hoek" "^9.0.0"\n'
               '\n'
               '"@sideway/formula@^3.0.1":\n'
               '  version "3.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/@sideway/formula/-/formula-3.0.1.tgz"\n'
               '  integrity '
               'sha512-/poHZJJVjx3L+zVD6g9KgHfYnb443oi7wLu/XKojDviHy6HOEOA6z1Trk5aR1dGcmPenJEgb2sK2I80LeS3MIg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=153,
          lineno=232,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@sideway/pinpoint@^2.0.0":\n'
               '  version "2.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@sideway/pinpoint/-/pinpoint-2.0.0.tgz"\n'
               '  integrity '
               'sha512-RNiOoTPkptFtSVzQevY/yWtZwf/RxyVnPy/OcA9HBM3MlGDnBEYL5B41H0MTn0Uec8Hi+2qUtTfG2WWZBmMejQ==\n'
               '\n'
               '"@sqltools/formatter@^1.2.5":\n'
               '  version "1.2.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/@sqltools/formatter/-/formatter-1.2.5.tgz"\n'
               '  integrity '
               'sha512-Uy0+khmZqUrUGm5dmMqVlnvufZRSK0FbYzVgp0UMstm+F5+W2/jnEEQyc9vo1ZR/E5ZI/B1WjjoTqBqwJL6Krw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=154,
          lineno=242,
          tokens=127,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@swc/helpers@0.4.14":\n'
               '  version "0.4.14"\n'
               '  resolved '
               '"https://registry.npmjs.org/@swc/helpers/-/helpers-0.4.14.tgz"\n'
               '  integrity '
               'sha512-4C7nX/dvpzB7za4Ql9K81xK3HPxCpHMgwTZVyf+9JQ6VUbn9jjZVN7/Nkdz/Ugzs2CSjqnL/UPXroiVBVHUWUw==\n'
               '  dependencies:\n'
               '    tslib "^2.4.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=155,
          lineno=249,
          tokens=134,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@tailwindcss/forms@^0.5.3":\n'
               '  version "0.5.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/@tailwindcss/forms/-/forms-0.5.3.tgz"\n'
               '  integrity '
               'sha512-y5mb86JUoiUgBjY/o6FJSFZSEttfb3Q5gllE4xoKjAAD+vBrnIhE4dViwUuow3va8mpH4s9jyUbUbrRGoRdc2Q==\n'
               '  dependencies:\n'
               '    mini-svg-data-uri "^1.2.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=156,
          lineno=256,
          tokens=241,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@types/json5@^0.0.29":\n'
               '  version "0.0.29"\n'
               '  resolved '
               '"https://registry.npmjs.org/@types/json5/-/json5-0.0.29.tgz"\n'
               '  integrity '
               'sha512-dRLjCWHYg4oaA77cxO64oO+7JwCwnIzkZPdrrC71jQmQtlhM556pwKo5bUzqvZndkVbeFLIIi+9TC40JNF5hNQ==\n'
               '\n'
               '"@types/next@^9.0.0":\n'
               '  version "9.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@types/next/-/next-9.0.0.tgz"\n'
               '  integrity '
               'sha512-gnBXM8rP1mnCgT1uE2z8SnpFTKRWReJlhbZLZkOLq/CH1ifvTNwjIVtXvsywTy1dwVklf+y/MB0Eh6FOa94yrg==\n'
               '  dependencies:\n'
               '    next "*"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=157,
          lineno=268,
          tokens=135,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@types/node-fetch@^2.5.7":\n'
               '  version "2.6.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/@types/node-fetch/-/node-fetch-2.6.4.tgz"\n'
               '  integrity '
               'sha512-1ZX9fcN4Rvkvgv4E6PAY5WXUFWFcRWxZa3EW83UjycOB9ljJCedb2CupIP4RZMEwF/M3eTcCihbBRgwtGbg5Rg==\n'
               '  dependencies:\n'
               '    "@types/node" "*"\n'
               '    form-data "^3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=158,
          lineno=276,
          tokens=233,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@types/node@*", "@types/node@18.15.11":\n'
               '  version "18.15.11"\n'
               '  resolved '
               '"https://registry.npmjs.org/@types/node/-/node-18.15.11.tgz"\n'
               '  integrity '
               'sha512-E5Kwq2n4SbMzQOn6wnmBjuK9ouqlURrcZDVfbo9ftDDTFt3nk7ZKK4GMOzoYgnpQJKcxwQw+lGaBvvlMo0qN/Q==\n'
               '\n'
               '"@types/prop-types@*":\n'
               '  version "15.7.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/@types/prop-types/-/prop-types-15.7.5.tgz"\n'
               '  integrity '
               'sha512-JCB8C6SnDoQf0cNycqd/35A7MjcnK+ZTqE7judS6o7utxUCg6imJg3QK2qzHKszlTjcj2cn+NwMB2i96ubpj7w==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=159,
          lineno=286,
          tokens=126,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@types/react-dom@18.0.11":\n'
               '  version "18.0.11"\n'
               '  resolved '
               '"https://registry.npmjs.org/@types/react-dom/-/react-dom-18.0.11.tgz"\n'
               '  integrity '
               'sha512-O38bPbI2CWtgw/OoQoY+BRelw7uysmXbWvw3nLWO21H1HSh+GOlqPuXshJfjmpNlKiiSDG9cc1JZAaMmVdcTlw==\n'
               '  dependencies:\n'
               '    "@types/react" "*"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=160,
          lineno=293,
          tokens=144,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@types/react@*", "@types/react@18.0.31":\n'
               '  version "18.0.31"\n'
               '  resolved '
               '"https://registry.npmjs.org/@types/react/-/react-18.0.31.tgz"\n'
               '  integrity '
               'sha512-EEG67of7DsvRDU6BLLI0p+k1GojDLz9+lZsnCpCRTa/lOokvyPBvp8S5x+A24hME3yyQuIipcP70KJ6H7Qupww==\n'
               '  dependencies:\n'
               '    "@types/prop-types" "*"\n'
               '    "@types/scheduler" "*"\n'
               '    csstype "^3.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=161,
          lineno=302,
          tokens=115,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@types/scheduler@*":\n'
               '  version "0.16.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/@types/scheduler/-/scheduler-0.16.3.tgz"\n'
               '  integrity '
               'sha512-5cJ8CB4yAx7BH1oMvdU0Jh9lrEXyPkar6F9G/ERswkCuvP4KQZfZkSjcMbAICCpQTN4OuZn8tz0HiKv9TGZgrQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=162,
          lineno=307,
          tokens=173,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@typescript-eslint/parser@^5.42.0":\n'
               '  version "5.61.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@typescript-eslint/parser/-/parser-5.61.0.tgz"\n'
               '  integrity '
               'sha512-yGr4Sgyh8uO6fSi9hw3jAFXNBHbCtKKFMdX2IkT3ZqpKmtAq3lHS4ixB/COFuAIJpwl9/AqF7j72ZDWYKmIfvg==\n'
               '  dependencies:\n'
               '    "@typescript-eslint/scope-manager" "5.61.0"\n'
               '    "@typescript-eslint/types" "5.61.0"\n'
               '    "@typescript-eslint/typescript-estree" "5.61.0"\n'
               '    debug "^4.3.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=163,
          lineno=317,
          tokens=150,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@typescript-eslint/scope-manager@5.61.0":\n'
               '  version "5.61.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@typescript-eslint/scope-manager/-/scope-manager-5.61.0.tgz"\n'
               '  integrity '
               'sha512-W8VoMjoSg7f7nqAROEmTt6LoBpn81AegP7uKhhW5KzYlehs8VV0ZW0fIDVbcZRcaP3aPSW+JZFua+ysQN+m/Nw==\n'
               '  dependencies:\n'
               '    "@typescript-eslint/types" "5.61.0"\n'
               '    "@typescript-eslint/visitor-keys" "5.61.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=164,
          lineno=325,
          tokens=115,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@typescript-eslint/types@5.61.0":\n'
               '  version "5.61.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@typescript-eslint/types/-/types-5.61.0.tgz"\n'
               '  integrity '
               'sha512-ldyueo58KjngXpzloHUog/h9REmHl59G1b3a5Sng1GfBo14BkS3ZbMEb3693gnP1k//97lh7bKsp6/V/0v1veQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=165,
          lineno=330,
          tokens=204,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@typescript-eslint/typescript-estree@5.61.0":\n'
               '  version "5.61.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@typescript-eslint/typescript-estree/-/typescript-estree-5.61.0.tgz"\n'
               '  integrity '
               'sha512-Fud90PxONnnLZ36oR5ClJBLTLfU4pIWBmnvGwTbEa2cXIqj70AEDEmOmpkFComjBZ/037ueKrOdHuYmSFVD7Rw==\n'
               '  dependencies:\n'
               '    "@typescript-eslint/types" "5.61.0"\n'
               '    "@typescript-eslint/visitor-keys" "5.61.0"\n'
               '    debug "^4.3.4"\n'
               '    globby "^11.1.0"\n'
               '    is-glob "^4.0.3"\n'
               '    semver "^7.3.7"\n'
               '    tsutils "^3.21.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=166,
          lineno=343,
          tokens=147,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@typescript-eslint/visitor-keys@5.61.0":\n'
               '  version "5.61.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@typescript-eslint/visitor-keys/-/visitor-keys-5.61.0.tgz"\n'
               '  integrity '
               'sha512-50XQ5VdbWrX06mQXhy93WywSFZZGsv3EOjq+lqp6WC2t+j3mb6A9xYVdrRxafvK88vg9k9u+CT4l6D8PEatjKg==\n'
               '  dependencies:\n'
               '    "@typescript-eslint/types" "5.61.0"\n'
               '    eslint-visitor-keys "^3.3.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=167,
          lineno=351,
          tokens=145,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"@upstash/redis@^1.0.1", "@upstash/redis@^1.22.0":\n'
               '  version "1.22.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/@upstash/redis/-/redis-1.22.0.tgz"\n'
               '  integrity '
               'sha512-sXoJDoEqqik0HbrNE7yRWckOySEFsoBxfRdCgOqkc0w6py19ZZG50SpGkDDEUXSnBqP8VgGYXhWAiBpqxrt5oA==\n'
               '  dependencies:\n'
               '    isomorphic-fetch "^3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=168,
          lineno=358,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'abort-controller@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/abort-controller/-/abort-controller-3.0.0.tgz"\n'
               '  integrity '
               'sha512-h8lQ8tacZYnR3vNQTgibj+tODHI5/+l06Au2Pcriv/Gmet0eaj4TwWH41sO9wnHDiQsEj19q0drzdWdeAHtweg==\n'
               '  dependencies:\n'
               '    event-target-shim "^5.0.0"\n'
               '\n'
               'acorn-jsx@^5.3.2:\n'
               '  version "5.3.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/acorn-jsx/-/acorn-jsx-5.3.2.tgz"\n'
               '  integrity '
               'sha512-rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=169,
          lineno=370,
          tokens=139,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"acorn@^6.0.0 || ^7.0.0 || ^8.0.0", acorn@^8.9.0:\n'
               '  version "8.10.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/acorn/-/acorn-8.10.0.tgz"\n'
               '  integrity '
               'sha512-F0SAmZ8iUtS//m8DmCTA0jlh6TDKkHQyK6xc6V4KDTyZKA9dnvX9/3sRTVQrWm79glUAZbnmmNcdYwUIHWVybw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=170,
          lineno=375,
          tokens=181,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'ajv@^6.10.0, ajv@^6.12.3, ajv@^6.12.4:\n'
               '  version "6.12.6"\n'
               '  resolved "https://registry.npmjs.org/ajv/-/ajv-6.12.6.tgz"\n'
               '  integrity '
               'sha512-j3fVLgvTo527anyYyJOGTYJbG+vnnQYvE0m5mmkc1TK+nxAppkCLMIL0aZ4dblVCNoGShhm+kzE4ZUykBoMg4g==\n'
               '  dependencies:\n'
               '    fast-deep-equal "^3.1.1"\n'
               '    fast-json-stable-stringify "^2.0.0"\n'
               '    json-schema-traverse "^0.4.1"\n'
               '    uri-js "^4.2.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=171,
          lineno=385,
          tokens=117,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'ansi-regex@^5.0.1:\n'
               '  version "5.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz"\n'
               '  integrity '
               'sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=172,
          lineno=390,
          tokens=142,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'ansi-styles@^4.0.0, ansi-styles@^4.1.0:\n'
               '  version "4.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz"\n'
               '  integrity '
               'sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==\n'
               '  dependencies:\n'
               '    color-convert "^2.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=173,
          lineno=397,
          tokens=119,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'any-promise@^1.0.0:\n'
               '  version "1.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/any-promise/-/any-promise-1.3.0.tgz"\n'
               '  integrity '
               'sha512-7UvmKalWRt1wgjL1RrGxoSJW/0QZFIegpeGvZG9kjp8vrRu55XTHbwnqq2GpXm9uLbcuhxm3IqX9OB4MZR1b2A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=174,
          lineno=402,
          tokens=140,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'anymatch@~3.1.2:\n'
               '  version "3.1.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz"\n'
               '  integrity '
               'sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==\n'
               '  dependencies:\n'
               '    normalize-path "^3.0.0"\n'
               '    picomatch "^2.0.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=175,
          lineno=410,
          tokens=231,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'app-root-path@^3.1.0:\n'
               '  version "3.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/app-root-path/-/app-root-path-3.1.0.tgz"\n'
               '  integrity '
               'sha512-biN3PwB2gUtjaYy/isrU3aNWI5w+fAfvHkSvCKeQGxhmYpwKFUxudR3Yya+KqVRHBmEDYh+/lTozYCFbmzX4nA==\n'
               '\n'
               'arg@^5.0.2:\n'
               '  version "5.0.2"\n'
               '  resolved "https://registry.npmjs.org/arg/-/arg-5.0.2.tgz"\n'
               '  integrity '
               'sha512-PYjyFOLKQ9y57JvQ6QLo8dAgNqswh8M1RMJYdQduT6xbWSgK36P/Z/v+p888pM69jMMfS8Xd8F6I1kQ/I9HUGg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=176,
          lineno=420,
          tokens=236,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'argparse@^2.0.1:\n'
               '  version "2.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/argparse/-/argparse-2.0.1.tgz"\n'
               '  integrity '
               'sha512-8+9WqebbFzpX9OR+Wa6O29asIogeRMzcGtAINdpMHHyAg10f05aSFVBbcEqGf/PXw1EjAZ+q2/bEBg3DvurK3Q==\n'
               '\n'
               'aria-query@^5.1.3:\n'
               '  version "5.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/aria-query/-/aria-query-5.3.0.tgz"\n'
               '  integrity '
               'sha512-b0P0sZPKtyu8HkeRAfCq0IfURZK+SuwMjY1UXGBU27wpAiTwQAIlq56IbIO+ytk/JjS1fMR14ee5WBBfKi5J6A==\n'
               '  dependencies:\n'
               '    dequal "^2.0.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=177,
          lineno=432,
          tokens=135,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'array-buffer-byte-length@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/array-buffer-byte-length/-/array-buffer-byte-length-1.0.0.tgz"\n'
               '  integrity '
               'sha512-LPuwb2P+NrQw3XhxGc36+XSvuBPopovXYTR9Ew++Du9Yb/bx5AzBfrIsBoj0EZUifjQU+sHL21sseZ3jerWO/A==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    is-array-buffer "^3.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=178,
          lineno=440,
          tokens=167,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'array-includes@^3.1.6:\n'
               '  version "3.1.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/array-includes/-/array-includes-3.1.6.tgz"\n'
               '  integrity '
               'sha512-sgTbLvL6cNnw24FnbaDyjmvddQ2ML8arZsgaJhoABMoplz/4QRhtrYS+alr1BUM1Bwp6dhx8vVCBSLG+StwOFw==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'
               '    get-intrinsic "^1.1.3"\n'
               '    is-string "^1.0.7"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=179,
          lineno=451,
          tokens=117,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'array-union@^2.1.0:\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/array-union/-/array-union-2.1.0.tgz"\n'
               '  integrity '
               'sha512-HGyxoOTYUyCM6stUe6EJgnd4EoewAI7zMdfqO+kGjnlZmBDz/cR5pf8r/cR4Wq60sL/p0IkcjUEEPwS3GFrIyw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=180,
          lineno=456,
          tokens=163,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'array.prototype.flat@^1.3.1:\n'
               '  version "1.3.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/array.prototype.flat/-/array.prototype.flat-1.3.1.tgz"\n'
               '  integrity '
               'sha512-roTU0KWIOmJ4DRLmwKd19Otg0/mT3qPNt0Qb3GWW8iObuZXxrjB/pzn0R3hqpRSWg4HCwqx+0vwOnWnvlOyeIA==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'
               '    es-shim-unscopables "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=181,
          lineno=466,
          tokens=164,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'array.prototype.flatmap@^1.3.1:\n'
               '  version "1.3.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/array.prototype.flatmap/-/array.prototype.flatmap-1.3.1.tgz"\n'
               '  integrity '
               'sha512-8UGn9O1FDVvMNB0UlLv4voxRMze7+FpHyF5mSMRjWHUMlpoDViniy05870VlxhfgTnLbpuwTzvD76MTtWxB/mQ==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'
               '    es-shim-unscopables "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=182,
          lineno=476,
          tokens=183,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'array.prototype.tosorted@^1.1.1:\n'
               '  version "1.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/array.prototype.tosorted/-/array.prototype.tosorted-1.1.1.tgz"\n'
               '  integrity '
               'sha512-pZYPXPRl2PqWcsUs6LOMn+1f1532nEoPTYowBtqLwAW+W8vSVhkIGnmOX1t/UQjD6YGI0vcD2B1U7ZFGQH9jnQ==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'
               '    es-shim-unscopables "^1.0.0"\n'
               '    get-intrinsic "^1.1.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=183,
          lineno=487,
          tokens=125,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'asn1@~0.2.3:\n'
               '  version "0.2.6"\n'
               '  resolved "https://registry.npmjs.org/asn1/-/asn1-0.2.6.tgz"\n'
               '  integrity '
               'sha512-ix/FxPn0MDjeyJ7i/yoHGFt/EX6LyNbxSEhPPXODPL+KB0VPk86UYfL0lMdy+KCnv+fmvIzySwaK5COwqVbWTQ==\n'
               '  dependencies:\n'
               '    safer-buffer "~2.1.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=184,
          lineno=494,
          tokens=242,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'assert-plus@^1.0.0, assert-plus@1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/assert-plus/-/assert-plus-1.0.0.tgz"\n'
               '  integrity '
               'sha512-NfJ4UzBCcQGLDlQq7nHxH+tv3kyZ0hHQqF5BO6J7tNJeP5do1llPr8dZ8zHonfhAu0PHAdMkSo+8o0wxg9lZWw==\n'
               '\n'
               'ast-types-flow@^0.0.7:\n'
               '  version "0.0.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/ast-types-flow/-/ast-types-flow-0.0.7.tgz"\n'
               '  integrity '
               'sha512-eBvWn1lvIApYMhzQMsu9ciLfkBY499mFZlNqG+/9WR7PVlroQw0vG30cOQQbaKz3sCEc44TAOu2ykzqXSNnwag==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=185,
          lineno=504,
          tokens=235,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'async@^2.6.4:\n'
               '  version "2.6.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/async/-/async-2.6.4.tgz"\n'
               '  integrity '
               'sha512-mzo5dfJYwAn29PeiJ0zvwTo04zj8HDJj0Mn8TD7sno7q12prdbnasKJHhkm2c1LgrhlJ0teaea8860oxi51mGA==\n'
               '  dependencies:\n'
               '    lodash "^4.17.14"\n'
               '\n'
               'asynckit@^0.4.0:\n'
               '  version "0.4.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/asynckit/-/asynckit-0.4.0.tgz"\n'
               '  integrity '
               'sha512-Oei9OH4tRh0YqU3GxhX79dM/mwVgvbZJaSNaRk+bshkj0S5cfHcgYakreBjrHwatXKbz+IoIdYLxrKim2MjW0Q==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=186,
          lineno=516,
          tokens=186,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'autoprefixer@^10.4.14:\n'
               '  version "10.4.14"\n'
               '  resolved '
               '"https://registry.npmjs.org/autoprefixer/-/autoprefixer-10.4.14.tgz"\n'
               '  integrity '
               'sha512-FQzyfOsTlwVzjHxKEqRIAdJx9niO6VCBCoEwax/VLSoQF29ggECcPuBqUMZ+u8jCZOPSy8b8/8KnuFbp0SaFZQ==\n'
               '  dependencies:\n'
               '    browserslist "^4.21.5"\n'
               '    caniuse-lite "^1.0.30001464"\n'
               '    fraction.js "^4.2.0"\n'
               '    normalize-range "^0.1.2"\n'
               '    picocolors "^1.0.0"\n'
               '    postcss-value-parser "^4.2.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=187,
          lineno=528,
          tokens=232,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'available-typed-arrays@^1.0.5:\n'
               '  version "1.0.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/available-typed-arrays/-/available-typed-arrays-1.0.5.tgz"\n'
               '  integrity '
               'sha512-DMD0KiN46eipeziST1LPP/STfDU0sufISXmjSgvVsoU2tqxctQeASejWcfNtxYKqETM1UxQ8sp2OrSBWpHY6sw==\n'
               '\n'
               'aws-sign2@~0.7.0:\n'
               '  version "0.7.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/aws-sign2/-/aws-sign2-0.7.0.tgz"\n'
               '  integrity '
               'sha512-08kcGqnYf/YmjoRhfxyu+CLxBjUtHLXLXX/vUfx9l2LYzG3c1m61nrpyFUZI6zeS+Li/wWMMidD9KgrqtGq3mA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=188,
          lineno=538,
          tokens=226,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'aws4@^1.8.0:\n'
               '  version "1.12.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/aws4/-/aws4-1.12.0.tgz"\n'
               '  integrity '
               'sha512-NmWvPnx0F1SfrQbYwOi7OeaNGokp9XhzNioJ/CSBs8Qa4vxug81mhJEAVZwxXuBmYB5KDRfMq/F3RR0BIU7sWg==\n'
               '\n'
               'axe-core@^4.6.2:\n'
               '  version "4.7.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/axe-core/-/axe-core-4.7.2.tgz"\n'
               '  integrity '
               'sha512-zIURGIS1E1Q4pcrMjp+nnEh+16G56eG/MUllJH8yEvw7asDo7Ac9uhC9KIH5jzpITueEZolfYglnCGIuSBz39g==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=189,
          lineno=548,
          tokens=139,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'axios@^1.3.4:\n'
               '  version "1.4.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/axios/-/axios-1.4.0.tgz"\n'
               '  integrity '
               'sha512-S4XCWMEmzvo64T9GfvQDOXgYRDJ/wsSZc7Jvdgx5u1sd0JwsuPLqb3SYmusag+edF6ziyMensPVqLTSc1PiSEA==\n'
               '  dependencies:\n'
               '    follow-redirects "^1.15.0"\n'
               '    form-data "^4.0.0"\n'
               '    proxy-from-env "^1.1.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=190,
          lineno=557,
          tokens=246,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'axobject-query@^3.1.1:\n'
               '  version "3.2.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/axobject-query/-/axobject-query-3.2.1.tgz"\n'
               '  integrity '
               'sha512-jsyHu61e6N4Vbz/v18DHwWYKK0bSWLqn47eeDSKPB7m8tqMHF9YJ+mhIk2lVteyZrY8tnSj/jHOv4YiTCuCJgg==\n'
               '  dependencies:\n'
               '    dequal "^2.0.3"\n'
               '\n'
               'balanced-match@^1.0.0:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz"\n'
               '  integrity '
               'sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=191,
          lineno=569,
          tokens=248,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'base64-js@^1.3.1:\n'
               '  version "1.5.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz"\n'
               '  integrity '
               'sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==\n'
               '\n'
               'bcrypt-pbkdf@^1.0.0:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/bcrypt-pbkdf/-/bcrypt-pbkdf-1.0.2.tgz"\n'
               '  integrity '
               'sha512-qeFIXtP4MSoi6NLqO12WfqARWWuCKi2Rn/9hJLEmtB5yTNr9DqFWkJRCf2qShWzPeAMRnOgCrq0sg/KLv5ES9w==\n'
               '  dependencies:\n'
               '    tweetnacl "^0.14.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=192,
          lineno=581,
          tokens=227,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'big-integer@^1.6.44:\n'
               '  version "1.6.51"\n'
               '  resolved '
               '"https://registry.npmjs.org/big-integer/-/big-integer-1.6.51.tgz"\n'
               '  integrity '
               'sha512-GPEid2Y9QU1Exl1rpO9B2IPJGHPSupF5GnVIP0blYvNOMer2bTvSWs1jGOUg04hTmu67nmLsQ9TBo1puaotBHg==\n'
               '\n'
               'binary-extensions@^2.0.0:\n'
               '  version "2.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.2.0.tgz"\n'
               '  integrity '
               'sha512-jDctJ/IVQbZoJykoeHbhXpOlNBqGNcwXJKJog42E5HDPUwQTSdjCHdihjj0DlnheQ7blbT6dHOafNAiS8ooQKA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=193,
          lineno=591,
          tokens=241,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'bluebird@^3.5.0:\n'
               '  version "3.7.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/bluebird/-/bluebird-3.7.2.tgz"\n'
               '  integrity '
               'sha512-XpNj6GDQzdfW+r2Wnn7xiSAd7TM3jzkxGXBGTtWKuSXv1xUV+azxAm8jdWZN06QTQk+2N2XB9jRDkvbmQmcRtg==\n'
               '\n'
               'bplist-parser@^0.2.0:\n'
               '  version "0.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/bplist-parser/-/bplist-parser-0.2.0.tgz"\n'
               '  integrity '
               'sha512-z0M+byMThzQmD9NILRniCUXYsYpjwnlO8N5uCFaCqIOpqRsJCrQL9NK3JsD67CN5a08nF5oIL2bD6loTdHOuKw==\n'
               '  dependencies:\n'
               '    big-integer "^1.6.44"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=194,
          lineno=603,
          tokens=134,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'brace-expansion@^1.1.7:\n'
               '  version "1.1.11"\n'
               '  resolved '
               '"https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.11.tgz"\n'
               '  integrity '
               'sha512-iCuPHDFgrHX7H2vEI/5xpz07zSHB00TpugqhmYtVmMO6518mCuRMoOYFldEBl0g187ufozdaHgWKcYFb61qGiA==\n'
               '  dependencies:\n'
               '    balanced-match "^1.0.0"\n'
               '    concat-map "0.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=195,
          lineno=611,
          tokens=128,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'brace-expansion@^2.0.1:\n'
               '  version "2.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/brace-expansion/-/brace-expansion-2.0.1.tgz"\n'
               '  integrity '
               'sha512-XnAIvQ8eM+kC6aULx6wuQiwVsnzsi9d3WxzV3FpWTGA19F621kwdbsAcFKXgKUHZWsy+mY6iL1sHTxWEFCytDA==\n'
               '  dependencies:\n'
               '    balanced-match "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=196,
          lineno=618,
          tokens=140,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'braces@^3.0.2, braces@~3.0.2:\n'
               '  version "3.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/braces/-/braces-3.0.2.tgz"\n'
               '  integrity '
               'sha512-b8um+L1RzM3WDSzvhm6gIz1yfTbBt6YTlcEKAvsmqCZZFw46z626lVj9j1yEPW33H5H+lBQpZMP1k8l+78Ha0A==\n'
               '  dependencies:\n'
               '    fill-range "^7.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=197,
          lineno=625,
          tokens=176,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'browserslist@^4.21.5, "browserslist@>= 4.21.0":\n'
               '  version "4.21.9"\n'
               '  resolved '
               '"https://registry.npmjs.org/browserslist/-/browserslist-4.21.9.tgz"\n'
               '  integrity '
               'sha512-M0MFoZzbUrRU4KNfCrDLnvyE7gub+peetoTid3TBIqtunaDJyXlwhakT+/VkvSXcfIzFfK/nkCs4nmyTmxdNSg==\n'
               '  dependencies:\n'
               '    caniuse-lite "^1.0.30001503"\n'
               '    electron-to-chromium "^1.4.431"\n'
               '    node-releases "^2.0.12"\n'
               '    update-browserslist-db "^1.0.11"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=198,
          lineno=635,
          tokens=130,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'buffer@^6.0.3:\n'
               '  version "6.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/buffer/-/buffer-6.0.3.tgz"\n'
               '  integrity '
               'sha512-FTiCpNxtwiZZHEZbcbTIcZjERVICn9yq/pDFkTl95/AxzD1naBctN7YO68riM/gLSDY7sdrMby8hofADYuuqOA==\n'
               '  dependencies:\n'
               '    base64-js "^1.3.1"\n'
               '    ieee754 "^1.2.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=199,
          lineno=643,
          tokens=129,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'bundle-name@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/bundle-name/-/bundle-name-3.0.0.tgz"\n'
               '  integrity '
               'sha512-PKA4BeSvBpQKQ8iPOGCSiell+N8P+Tf1DlwqmYhpe2gAhKPHn8EYOxVT+ShuGmhg8lN8XiSlS80yiExKXrURlw==\n'
               '  dependencies:\n'
               '    run-applescript "^5.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=200,
          lineno=650,
          tokens=147,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'call-bind@^1.0.0, call-bind@^1.0.2:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/call-bind/-/call-bind-1.0.2.tgz"\n'
               '  integrity '
               'sha512-7O+FbCihrB5WGbFYesctwmTKae6rOiIzmz1icreWJ+0aA7LJfuqhEso2T9ncpcFtzMQtzXf2QGGueWJGTYsqrA==\n'
               '  dependencies:\n'
               '    function-bind "^1.1.1"\n'
               '    get-intrinsic "^1.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=201,
          lineno=658,
          tokens=224,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'callsites@^3.0.0:\n'
               '  version "3.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/callsites/-/callsites-3.1.0.tgz"\n'
               '  integrity '
               'sha512-P8BjAsXvZS+VIDUI11hHCQEv74YT67YUi5JJFNWIqL235sBmjX4+qx9Muvls5ivyNENctx46xQLQ3aTuE7ssaQ==\n'
               '\n'
               'camelcase-css@^2.0.1:\n'
               '  version "2.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/camelcase-css/-/camelcase-css-2.0.1.tgz"\n'
               '  integrity '
               'sha512-QOSvevhslijgYwRx6Rv7zKdMF8lbRmx+uQGx2+vDc+KI/eBnsy9kit5aj23AgGu3pa4t9AgwbnXWqS+iOY+2aA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=202,
          lineno=668,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'caniuse-lite@^1.0.30001406, caniuse-lite@^1.0.30001464, '
               'caniuse-lite@^1.0.30001503:\n'
               '  version "1.0.30001513"\n'
               '  resolved '
               '"https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001513.tgz"\n'
               '  integrity '
               'sha512-pnjGJo7SOOjAGytZZ203Em95MRM8Cr6jhCXNF/FAXTpCTRTECnqQWLpiTRqrFtdYcth8hf4WECUpkezuYsMVww==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=203,
          lineno=673,
          tokens=115,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'caseless@~0.12.0:\n'
               '  version "0.12.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/caseless/-/caseless-0.12.0.tgz"\n'
               '  integrity '
               'sha512-4tYFyifaFfGacoiObjJegolkwSU4xQNGbVgUiNYVUxbQ2x2lUsFvY4hVgVzGiIe6WLOPqycWXA40l+PWsxthUw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=204,
          lineno=678,
          tokens=142,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'chalk@^4.0.0, chalk@^4.1.2:\n'
               '  version "4.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/chalk/-/chalk-4.1.2.tgz"\n'
               '  integrity '
               'sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==\n'
               '  dependencies:\n'
               '    ansi-styles "^4.1.0"\n'
               '    supports-color "^7.1.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=205,
          lineno=686,
          tokens=209,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'chokidar@^3.5.3:\n'
               '  version "3.5.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/chokidar/-/chokidar-3.5.3.tgz"\n'
               '  integrity '
               'sha512-Dr3sfKRP6oTcjf2JmUmFJfeVMvXBdegxB0iVQ5eb2V10uFJUCAS8OByZdVAyVb8xXNz3GjjTgj9kLWsZTqE6kw==\n'
               '  dependencies:\n'
               '    anymatch "~3.1.2"\n'
               '    braces "~3.0.2"\n'
               '    glob-parent "~5.1.2"\n'
               '    is-binary-path "~2.1.0"\n'
               '    is-glob "~4.0.1"\n'
               '    normalize-path "~3.0.0"\n'
               '    readdirp "~3.6.0"\n'
               '  optionalDependencies:\n'
               '    fsevents "~2.3.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=206,
          lineno=701,
          tokens=115,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'class-variance-authority@^0.4.0:\n'
               '  version "0.4.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/class-variance-authority/-/class-variance-authority-0.4.0.tgz"\n'
               '  integrity '
               'sha512-74enNN8O9ZNieycac/y8FxqgyzZhZbxmCitAtAeUrLPlxjSd5zA7LfpprmxEcOmQBnaGs5hYhiSGnJ0mqrtBLQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=207,
          lineno=706,
          tokens=181,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'cli-highlight@^2.1.11:\n'
               '  version "2.1.11"\n'
               '  resolved '
               '"https://registry.npmjs.org/cli-highlight/-/cli-highlight-2.1.11.tgz"\n'
               '  integrity '
               'sha512-9KDcoEVwyUXrjcJNvHD0NFc/hiwe/WPVYIleQh2O1N2Zro5gWJZ/K+3DGn8w8P/F6FxOgzyC5bxDyHIgCSPhGg==\n'
               '  dependencies:\n'
               '    chalk "^4.0.0"\n'
               '    highlight.js "^10.7.1"\n'
               '    mz "^2.4.0"\n'
               '    parse5 "^5.1.1"\n'
               '    parse5-htmlparser2-tree-adapter "^6.0.0"\n'
               '    yargs "^16.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=208,
          lineno=718,
          tokens=123,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'client-only@^0.0.1, client-only@0.0.1:\n'
               '  version "0.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/client-only/-/client-only-0.0.1.tgz"\n'
               '  integrity '
               'sha512-IV3Ou0jSMzZrd3pZ48nLkT9DA7Ag1pnPzaiQhpW7c3RbcqqzvzzVu+L8gfqMp/8IM2MQtSiqaCxrrcfu8I8rMA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=209,
          lineno=723,
          tokens=146,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'cliui@^7.0.2:\n'
               '  version "7.0.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/cliui/-/cliui-7.0.4.tgz"\n'
               '  integrity '
               'sha512-OcRE68cOsVMXp1Yvonl/fzkQOyjLSu/8bhPDfQt0e0/Eb283TKP20Fs2MqoPsr9SwA595rRCA+QMzYc9nBP+JQ==\n'
               '  dependencies:\n'
               '    string-width "^4.2.0"\n'
               '    strip-ansi "^6.0.0"\n'
               '    wrap-ansi "^7.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=210,
          lineno=732,
          tokens=249,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'cliui@^8.0.1:\n'
               '  version "8.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/cliui/-/cliui-8.0.1.tgz"\n'
               '  integrity '
               'sha512-BSeNnyus75C4//NQ9gQt1/csTXyo/8Sb+afLAkzAptFuMsod9HFokGNudZpi/oQV73hnVK+sR+5PVRMd+Dr7YQ==\n'
               '  dependencies:\n'
               '    string-width "^4.2.0"\n'
               '    strip-ansi "^6.0.1"\n'
               '    wrap-ansi "^7.0.0"\n'
               '\n'
               'clsx@^1.2.1:\n'
               '  version "1.2.1"\n'
               '  resolved "https://registry.npmjs.org/clsx/-/clsx-1.2.1.tgz"\n'
               '  integrity '
               'sha512-EcR6r5a8bj6pu3ycsa/E/cKVGuTgZJZdsyUYHOksG/UHIiKfjxzRxYJpyVBwYaQeOvghal9fcc4PidlgzugAQg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=211,
          lineno=746,
          tokens=237,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'cluster-key-slot@^1.1.0:\n'
               '  version "1.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/cluster-key-slot/-/cluster-key-slot-1.1.2.tgz"\n'
               '  integrity '
               'sha512-RMr0FhtfXemyinomL4hrWcYJxmX6deFdCxpJzhDttxgO1+bcCnkk+9drydLVDmAMG7NE6aN/fl4F7ucU/90gAA==\n'
               '\n'
               'color-convert@^2.0.1:\n'
               '  version "2.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz"\n'
               '  integrity '
               'sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==\n'
               '  dependencies:\n'
               '    color-name "~1.1.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=212,
          lineno=758,
          tokens=224,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'color-name@~1.1.4:\n'
               '  version "1.1.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz"\n'
               '  integrity '
               'sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==\n'
               '\n'
               'colors@1.0.x:\n'
               '  version "1.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/colors/-/colors-1.0.3.tgz"\n'
               '  integrity '
               'sha512-pFGrxThWcWQ2MsAz6RtgeWe4NK2kUE1WfsrvvlctdII745EW9I0yflqhe7++M5LEc7bV2c/9/5zc8sFcpL0Drw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=213,
          lineno=768,
          tokens=145,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'combined-stream@^1.0.6, combined-stream@^1.0.8, '
               'combined-stream@~1.0.6:\n'
               '  version "1.0.8"\n'
               '  resolved '
               '"https://registry.npmjs.org/combined-stream/-/combined-stream-1.0.8.tgz"\n'
               '  integrity '
               'sha512-FQN4MRfuJeHf7cBbBMJFXhKSDq+2kAArBlmRBvcvFE5BB1HZKXtSFASDhdlz9zOYwxh8lDdnvmMOe/+5cdoEdg==\n'
               '  dependencies:\n'
               '    delayed-stream "~1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=214,
          lineno=775,
          tokens=229,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'commander@^4.0.0:\n'
               '  version "4.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/commander/-/commander-4.1.1.tgz"\n'
               '  integrity '
               'sha512-NOKm8xhkzAjzFx8B2v5OAHT+u5pRQc2UCa2Vq9jYL/31o2wi9mxBA7LIFs3sV5VSC49z6pEhfbMULvShKj26WA==\n'
               '\n'
               'concat-map@0.0.1:\n'
               '  version "0.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/concat-map/-/concat-map-0.0.1.tgz"\n'
               '  integrity '
               'sha512-/Srv4dswyQNBfohGpz9o6Yb3Gz3SrUDqBH5rTuhGR7ahtlbYKnVxw2bCFMRljaA7EXHaXZ8wsHdodFvbkhKmqg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=215,
          lineno=785,
          tokens=226,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'cookie@^0.5.0:\n'
               '  version "0.5.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/cookie/-/cookie-0.5.0.tgz"\n'
               '  integrity '
               'sha512-YZ3GUyn/o8gfKJlnlX7g7xq4gyO6OSuhGPKaaGssGB2qgDUS0gPgtTvoyZLTt9Ab6dC4hfc9dV5arkvc/OCmrw==\n'
               '\n'
               'core-util-is@1.0.2:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/core-util-is/-/core-util-is-1.0.2.tgz"\n'
               '  integrity '
               'sha512-3lqz5YjWTYnW6dlDa5TLaTCcShfar1e40rmcJVwCBJC6mWlFuj0eCHIElmG1g5kyuJ/GD+8Wn4FFCcz4gJPfaQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=216,
          lineno=795,
          tokens=160,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'cross-spawn@^7.0.2, cross-spawn@^7.0.3:\n'
               '  version "7.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.3.tgz"\n'
               '  integrity '
               'sha512-iRDPJKUPVEND7dHPO8rkbOnPpyDygcDFtWjpeWNCgy8WP2rXcxXL8TskReQl6OrB2G7+UJrags1q15Fudc7G6w==\n'
               '  dependencies:\n'
               '    path-key "^3.1.0"\n'
               '    shebang-command "^2.0.0"\n'
               '    which "^2.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=217,
          lineno=804,
          tokens=233,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'cssesc@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz"\n'
               '  integrity '
               'sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg==\n'
               '\n'
               'csstype@^3.0.10, csstype@^3.0.2:\n'
               '  version "3.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/csstype/-/csstype-3.1.2.tgz"\n'
               '  integrity '
               'sha512-I7K1Uu0MBPzaFKg4nI5Q7Vs2t+3gWWW648spaF+Rg7pI9ds18Ugn+lvg4SHczUdKlHI5LWBXyqfS8+DufyBsgQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=218,
          lineno=814,
          tokens=237,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'cycle@1.0.x:\n'
               '  version "1.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/cycle/-/cycle-1.0.3.tgz"\n'
               '  integrity '
               'sha512-TVF6svNzeQCOpjCqsy0/CSy8VgObG3wXusJ73xW2GbG5rGx7lC8zxDSURicsXI2UsGdi2L0QNRCi745/wUDvsA==\n'
               '\n'
               'damerau-levenshtein@^1.0.8:\n'
               '  version "1.0.8"\n'
               '  resolved '
               '"https://registry.npmjs.org/damerau-levenshtein/-/damerau-levenshtein-1.0.8.tgz"\n'
               '  integrity '
               'sha512-sdQSFB7+llfUcQHUQO3+B8ERRj0Oa4w9POWMI/puGtuf7gFywGmkaLCElnudfTiKZV+NvHqL0ifzdrI8Ro7ESA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=219,
          lineno=824,
          tokens=128,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'dashdash@^1.12.0:\n'
               '  version "1.14.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/dashdash/-/dashdash-1.14.1.tgz"\n'
               '  integrity '
               'sha512-jRFi8UDGo6j+odZiEpjazZaWqEal3w/basFjQHQEwVtZJGDpxbH1MeYluwCS8Xq5wmLJooDlMgvVarmWfGM44g==\n'
               '  dependencies:\n'
               '    assert-plus "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=220,
          lineno=831,
          tokens=249,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'date-fns@^2.29.3:\n'
               '  version "2.30.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/date-fns/-/date-fns-2.30.0.tgz"\n'
               '  integrity '
               'sha512-fnULvOpxnC5/Vg3NCiWelDsLiUc9bRwAPs/+LfTLNvetFCtCTN+yQz15C/fs4AwX1R9K5GLtLfn8QW+dWisaAw==\n'
               '  dependencies:\n'
               '    "@babel/runtime" "^7.21.0"\n'
               '\n'
               'debug@^3.2.7:\n'
               '  version "3.2.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/debug/-/debug-3.2.7.tgz"\n'
               '  integrity '
               'sha512-CFjzYYAi4ThfiQvizrFQevTTXHtnCqWfe7x1AhgEscTz6ZbLbfoLRLPugTQyBth6f8ZERVUSyWHFD/7Wu4t1XQ==\n'
               '  dependencies:\n'
               '    ms "^2.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=221,
          lineno=845,
          tokens=136,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'debug@^4.1.1, debug@^4.3.2, debug@^4.3.4:\n'
               '  version "4.3.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/debug/-/debug-4.3.4.tgz"\n'
               '  integrity '
               'sha512-PRWFHuSU3eDtQJPvnNY7Jcket1j0t5OuOsFzPPzsekD52Zl8qUfFIPEiswXqIvHWGVHOgX+7G/vCNNhehwxfkQ==\n'
               '  dependencies:\n'
               '    ms "2.1.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=222,
          lineno=852,
          tokens=115,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'deep-is@^0.1.3:\n'
               '  version "0.1.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/deep-is/-/deep-is-0.1.4.tgz"\n'
               '  integrity '
               'sha512-oIPzksmTg4/MriiaYGO+okXDT7ztn/w3Eptv/+gSIdMdKsJo0u4CfYNFJPy+4SKMuCqGw2wxnA+URMg3t8a/bQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=223,
          lineno=857,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'default-browser-id@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/default-browser-id/-/default-browser-id-3.0.0.tgz"\n'
               '  integrity '
               'sha512-OZ1y3y0SqSICtE8DE4S8YOE9UZOJ8wO16fKWVP5J1Qz42kV9jcnMVFrEE/noXb/ss3Q4pZIH79kxofzyNNtUNA==\n'
               '  dependencies:\n'
               '    bplist-parser "^0.2.0"\n'
               '    untildify "^4.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=224,
          lineno=865,
          tokens=154,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'default-browser@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/default-browser/-/default-browser-4.0.0.tgz"\n'
               '  integrity '
               'sha512-wX5pXO1+BrhMkSbROFsyxUm0i/cJEScyNhA4PPxc41ICuv05ZZB/MX28s8aZx6xjmatvebIapF6hLEKEcpneUA==\n'
               '  dependencies:\n'
               '    bundle-name "^3.0.0"\n'
               '    default-browser-id "^3.0.0"\n'
               '    execa "^7.1.1"\n'
               '    titleize "^3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=225,
          lineno=875,
          tokens=121,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'define-lazy-prop@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/define-lazy-prop/-/define-lazy-prop-3.0.0.tgz"\n'
               '  integrity '
               'sha512-N+MeXYoqr3pOgn8xfyRPREN7gHakLYjhsHhWGT3fWAiL4IkAt0iDw14QiiEm2bE30c5XX5q0FtAA3CK5f9/BUg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=226,
          lineno=880,
          tokens=158,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'define-properties@^1.1.3, define-properties@^1.1.4, '
               'define-properties@^1.2.0:\n'
               '  version "1.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/define-properties/-/define-properties-1.2.0.tgz"\n'
               '  integrity '
               'sha512-xvqAVKGfT1+UAvPwKTVw/njhdQ8ZhXK4lI0bCIuCMrp2up9nPnaDftrLtmpTazqd1o+UY4zgzU+avtMbDP+ldA==\n'
               '  dependencies:\n'
               '    has-property-descriptors "^1.0.0"\n'
               '    object-keys "^1.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=227,
          lineno=888,
          tokens=234,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'delayed-stream@~1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/delayed-stream/-/delayed-stream-1.0.0.tgz"\n'
               '  integrity '
               'sha512-ZySD7Nf91aLB0RxL4KGrKHBXl7Eds1DAmEdcoVawXnLD7SDhpNgtuII2aAkg7a7QS41jxPSZ17p4VdGnMHk3MQ==\n'
               '\n'
               'denque@^2.1.0:\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/denque/-/denque-2.1.0.tgz"\n'
               '  integrity '
               'sha512-HVQE3AAb/pxF8fQAoiqpvg9i3evqug3hoiwakOyZAwJm+6vZehbkYXZ0l4JxS+I3QxM97v5aaRNhj8v5oBhekw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=228,
          lineno=898,
          tokens=226,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'depd@~1.1.2:\n'
               '  version "1.1.2"\n'
               '  resolved "https://registry.npmjs.org/depd/-/depd-1.1.2.tgz"\n'
               '  integrity '
               'sha512-7emPTl6Dpo6JRXOXjLRxck+FlLRX5847cLKEn00PLAgc3g2hTZZgr+e4c2v6QpSmLeFP3n5yUo7ft6avBK/5jQ==\n'
               '\n'
               'dequal@^2.0.3:\n'
               '  version "2.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/dequal/-/dequal-2.0.3.tgz"\n'
               '  integrity '
               'sha512-0je+qPKHEMohvfRTCEo3CrPG6cAzAYgmzKyxRiYSSDkS6eGJdyVJm7WaYA5ECaAD9wLB2T4EEeymA5aFVcYXCA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=229,
          lineno=908,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'didyoumean@^1.2.2:\n'
               '  version "1.2.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/didyoumean/-/didyoumean-1.2.2.tgz"\n'
               '  integrity '
               'sha512-gxtyfqMg7GKyhQmb056K7M3xszy/myH8w+B4RT+QXBQsvAOdc3XymqDDPHx1BgPgsdAA5SIifona89YtRATDzw==\n'
               '\n'
               'dir-glob@^3.0.1:\n'
               '  version "3.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/dir-glob/-/dir-glob-3.0.1.tgz"\n'
               '  integrity '
               'sha512-WkrWp9GR4KXfKGYzOLmTuGVi1UWFfws377n9cc55/tb6DuqyF6pcQ5AbiHEshaDpY9v6oaSr2XCDidGmMwdzIA==\n'
               '  dependencies:\n'
               '    path-type "^4.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=230,
          lineno=920,
          tokens=235,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'dlv@^1.1.3:\n'
               '  version "1.1.3"\n'
               '  resolved "https://registry.npmjs.org/dlv/-/dlv-1.1.3.tgz"\n'
               '  integrity '
               'sha512-+HlytyjlPKnIG8XuRG8WvmBP8xs8P71y+SKKS6ZXWoEgLuePxtDoUEiH7WkdePWrQ5JBpE6aoVqfZfJUQkjXwA==\n'
               '\n'
               'doctrine@^2.1.0:\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/doctrine/-/doctrine-2.1.0.tgz"\n'
               '  integrity '
               'sha512-35mSku4ZXK0vfCuHEDAwt55dg2jNajHZ1odvF+8SSr82EsZY4QmXfuWso8oEd8zRhVObSN18aM0CjSdoBX7zIw==\n'
               '  dependencies:\n'
               '    esutils "^2.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=231,
          lineno=932,
          tokens=237,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'doctrine@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/doctrine/-/doctrine-3.0.0.tgz"\n'
               '  integrity '
               'sha512-yS+Q5i3hBf7GBkd4KG8a7eBNNWNGLTaEwwYWUijIYM7zrlYDM0BFXHjjPWlWZ1Rg7UaddZeIDmi9jF3HmqiQ2w==\n'
               '  dependencies:\n'
               '    esutils "^2.0.2"\n'
               '\n'
               'dotenv@^16.0.3:\n'
               '  version "16.3.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/dotenv/-/dotenv-16.3.1.tgz"\n'
               '  integrity '
               'sha512-IPzF4w4/Rd94bA9imS68tZBaYyBWSCE47V1RGuMrB94iyTOIEwRmVL2x/4An+6mETpLrKJ5hQkB8W4kFAadeIQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=232,
          lineno=944,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'ecc-jsbn@~0.1.1:\n'
               '  version "0.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/ecc-jsbn/-/ecc-jsbn-0.1.2.tgz"\n'
               '  integrity '
               'sha512-eh9O+hwRHNbG4BLTjEl3nw044CkGm5X6LoaCf7LPp7UU8Qrt47JYNi6nPX8xjW97TKGKm1ouctg0QSpZe9qrnw==\n'
               '  dependencies:\n'
               '    jsbn "~0.1.0"\n'
               '    safer-buffer "^2.1.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=233,
          lineno=952,
          tokens=237,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'electron-to-chromium@^1.4.431:\n'
               '  version "1.4.454"\n'
               '  resolved '
               '"https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.4.454.tgz"\n'
               '  integrity '
               'sha512-pmf1rbAStw8UEQ0sr2cdJtWl48ZMuPD9Sto8HVQOq9vx9j2WgDEN6lYoaqFvqEHYOmGA9oRGn7LqWI9ta0YugQ==\n'
               '\n'
               'emoji-regex@^8.0.0:\n'
               '  version "8.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz"\n'
               '  integrity '
               'sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=234,
          lineno=962,
          tokens=114,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'emoji-regex@^9.2.2:\n'
               '  version "9.2.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/emoji-regex/-/emoji-regex-9.2.2.tgz"\n'
               '  integrity '
               'sha512-L18DaJsXSUk2+42pv8mLs5jJT2hqFkFE4j21wOmgbUqsZ2hL72NsUU785g9RXgo3s0ZNgVl42TiHp3ZtOv/Vyg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=235,
          lineno=967,
          tokens=138,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'encoding@^0.1.0, encoding@^0.1.13:\n'
               '  version "0.1.13"\n'
               '  resolved '
               '"https://registry.npmjs.org/encoding/-/encoding-0.1.13.tgz"\n'
               '  integrity '
               'sha512-ETBauow1T35Y/WZMkio9jiM0Z5xjHHmJ4XmjZOq1l/dXz3lr2sRn87nJy20RupqSh1F2m3HHPSp8ShIPQJrJ3A==\n'
               '  dependencies:\n'
               '    iconv-lite "^0.6.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=236,
          lineno=974,
          tokens=169,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'enhanced-resolve@^5.12.0:\n'
               '  version "5.15.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/enhanced-resolve/-/enhanced-resolve-5.15.0.tgz"\n'
               '  integrity '
               'sha512-LXYT42KJ7lpIKECr2mAXIaMldcNCh/7E0KBKOu4KSfkHmP+mZmSs+8V5gBAqisWBy0OO4W5Oyys0GO1Y8KtdKg==\n'
               '  dependencies:\n'
               '    graceful-fs "^4.2.4"\n'
               '    tapable "^2.2.0"\n'
               '\n'
               'es-abstract@^1.19.0, es-abstract@^1.20.4:\n'
               '  '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=237,
          lineno=984,
          tokens=241,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='version "1.21.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/es-abstract/-/es-abstract-1.21.2.tgz"\n'
               '  integrity '
               'sha512-y/B5POM2iBnIxCiernH1G7rC9qQoM77lLIMQLuob0zhp8C56Po81+2Nj0WFKnd0pNReDTnkYryc+zhOzpEIROg==\n'
               '  dependencies:\n'
               '    array-buffer-byte-length "^1.0.0"\n'
               '    available-typed-arrays "^1.0.5"\n'
               '    call-bind "^1.0.2"\n'
               '    es-set-tostringtag "^2.0.1"\n'
               '    es-to-primitive "^1.2.1"\n'
               '    function.prototype.name "^1.1.5"\n'
               '    get-intrinsic "^1.2.0"\n'
               '    get-symbol-description "^1.0.0"\n'
               '    globalthis "^1.0.3"\n'
               '    gopd "^1.0.1"\n'
               '    has "^1.0.3"\n'
               '    has-property-descriptors "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=238,
          lineno=1000,
          tokens=246,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='    has-proto "^1.0.1"\n'
               '    has-symbols "^1.0.3"\n'
               '    internal-slot "^1.0.5"\n'
               '    is-array-buffer "^3.0.2"\n'
               '    is-callable "^1.2.7"\n'
               '    is-negative-zero "^2.0.2"\n'
               '    is-regex "^1.1.4"\n'
               '    is-shared-array-buffer "^1.0.2"\n'
               '    is-string "^1.0.7"\n'
               '    is-typed-array "^1.1.10"\n'
               '    is-weakref "^1.0.2"\n'
               '    object-inspect "^1.12.3"\n'
               '    object-keys "^1.1.1"\n'
               '    object.assign "^4.1.4"\n'
               '    regexp.prototype.flags "^1.4.3"\n'
               '    safe-regex-test "^1.0.0"\n'
               '    string.prototype.trim "^1.2.7"\n'
               '    string.prototype.trimend "^1.0.6"\n'
               '    string.prototype.trimstart "^1.0.6"\n'
               '    typed-array-length "^1.0.4"\n'
               '    unbox-primitive "^1.0.2"\n'
               '    which-typed-array "^1.1.9"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=239,
          lineno=1022,
          tokens=156,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'es-set-tostringtag@^2.0.1:\n'
               '  version "2.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/es-set-tostringtag/-/es-set-tostringtag-2.0.1.tgz"\n'
               '  integrity '
               'sha512-g3OMbtlwY3QewlqAiMLI47KywjWZoEytKr8pf6iTC8uJq5bIAH52Z9pnQ8pVL6whrCto53JZDuUIsifGeLorTg==\n'
               '  dependencies:\n'
               '    get-intrinsic "^1.1.3"\n'
               '    has "^1.0.3"\n'
               '    has-tostringtag "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=240,
          lineno=1031,
          tokens=139,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'es-shim-unscopables@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/es-shim-unscopables/-/es-shim-unscopables-1.0.0.tgz"\n'
               '  integrity '
               'sha512-Jm6GPcCdC30eMLbZ2x8z2WuRwAws3zTBBKuusffYVUrNj/GVSUAZ+xKMaUpfNDR5IbyNA5LJbaecoUVbmUcB1w==\n'
               '  dependencies:\n'
               '    has "^1.0.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=241,
          lineno=1038,
          tokens=158,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'es-to-primitive@^1.2.1:\n'
               '  version "1.2.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/es-to-primitive/-/es-to-primitive-1.2.1.tgz"\n'
               '  integrity '
               'sha512-QCOllgZJtaUo9miYBcLChTUaHNjJF3PYs1VidD7AwiEj1kYxKeQTctLAezAOH5ZKRH0g2IgPn6KwB4IT8iRpvA==\n'
               '  dependencies:\n'
               '    is-callable "^1.1.4"\n'
               '    is-date-object "^1.0.1"\n'
               '    is-symbol "^1.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=242,
          lineno=1047,
          tokens=234,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'escalade@^3.1.1:\n'
               '  version "3.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/escalade/-/escalade-3.1.1.tgz"\n'
               '  integrity '
               'sha512-k0er2gUkLf8O0zKJiAhmkTnJlTvINGv7ygDNPbeIsX/TJjGJZHuh9B2UxbsaEkmlEo9MfhrSzmhIlhRlI2GXnw==\n'
               '\n'
               'escape-string-regexp@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-4.0.0.tgz"\n'
               '  integrity '
               'sha512-TtpcNJ3XAzx3Gq8sWRzJaVajRs0uVxA2YAkdb1jm2YkPz4G6egUFAyA3n5vtEIZefPk5Wa4UXbKuS5fKkJWdgA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=243,
          lineno=1057,
          tokens=236,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'eslint-config-next@13.2.4:\n'
               '  version "13.2.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint-config-next/-/eslint-config-next-13.2.4.tgz"\n'
               '  integrity '
               'sha512-lunIBhsoeqw6/Lfkd6zPt25w1bn0znLA/JCL+au1HoEpSb4/PpsOYsYtgV/q+YPsoKIOzFyU5xnb04iZnXjUvg==\n'
               '  dependencies:\n'
               '    "@next/eslint-plugin-next" "13.2.4"\n'
               '    "@rushstack/eslint-patch" "^1.1.3"\n'
               '    "@typescript-eslint/parser" "^5.42.0"\n'
               '    eslint-import-resolver-node "^0.3.6"\n'
               '    eslint-import-resolver-typescript "^3.5.2"\n'
               '    eslint-plugin-import "^2.26.0"\n'
               '    eslint-plugin-jsx-a11y "^6.5.1"\n'
               '    eslint-plugin-react "^7.31.7"\n'
               '    eslint-plugin-react-hooks "^4.5.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=244,
          lineno=1072,
          tokens=163,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'eslint-import-resolver-node@^0.3.6, '
               'eslint-import-resolver-node@^0.3.7:\n'
               '  version "0.3.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint-import-resolver-node/-/eslint-import-resolver-node-0.3.7.tgz"\n'
               '  integrity '
               'sha512-gozW2blMLJCeFpBwugLTGyvVjNoeo1knonXAcatC6bjPBZitotxdWf7Gimr25N4c0AAOo4eOUfaG82IJPDpqCA==\n'
               '  dependencies:\n'
               '    debug "^3.2.7"\n'
               '    is-core-module "^2.11.0"\n'
               '    resolve "^1.22.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=245,
          lineno=1081,
          tokens=215,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'eslint-import-resolver-typescript@^3.5.2:\n'
               '  version "3.5.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint-import-resolver-typescript/-/eslint-import-resolver-typescript-3.5.5.tgz"\n'
               '  integrity '
               'sha512-TdJqPHs2lW5J9Zpe17DZNQuDnox4xo2o+0tE7Pggain9Rbc19ik8kFtXdxZ250FVx2kF4vlt2RSf4qlUpG7bhw==\n'
               '  dependencies:\n'
               '    debug "^4.3.4"\n'
               '    enhanced-resolve "^5.12.0"\n'
               '    eslint-module-utils "^2.7.4"\n'
               '    get-tsconfig "^4.5.0"\n'
               '    globby "^13.1.3"\n'
               '    is-core-module "^2.11.0"\n'
               '    is-glob "^4.0.3"\n'
               '    synckit "^0.8.5"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=246,
          lineno=1095,
          tokens=147,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'eslint-module-utils@^2.7.4:\n'
               '  version "2.8.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint-module-utils/-/eslint-module-utils-2.8.0.tgz"\n'
               '  integrity '
               'sha512-aWajIYfsqCKRDgUfjEXNN/JlrzauMuSEy5sbd7WXbtW3EH6A6MpwEh42c7qD+MqQo9QMJ6fWLAeIJynx0g6OAw==\n'
               '  dependencies:\n'
               '    debug "^3.2.7"\n'
               '\n'
               'eslint-plugin-import@*, eslint-plugin-import@^2.26.0:\n'
               '  '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=247,
          lineno=1104,
          tokens=108,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='version "2.27.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint-plugin-import/-/eslint-plugin-import-2.27.5.tgz"\n'
               '  integrity '
               'sha512-LmEt3GVofgiGuiE+ORpnvP+kAm3h6MLZJ4Q5HCyHADofsb4VzXFsRiWj3c0OFiV+3DWFh0qg3v9gcPlfc3zRow==\n'
               '  dependencies:\n'
               '    '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=248,
          lineno=1108,
          tokens=157,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='array-includes "^3.1.6"\n'
               '    array.prototype.flat "^1.3.1"\n'
               '    array.prototype.flatmap "^1.3.1"\n'
               '    debug "^3.2.7"\n'
               '    doctrine "^2.1.0"\n'
               '    eslint-import-resolver-node "^0.3.7"\n'
               '    eslint-module-utils "^2.7.4"\n'
               '    has "^1.0.3"\n'
               '    is-core-module "^2.11.0"\n'
               '    is-glob "^4.0.3"\n'
               '    minimatch "^3.1.2"\n'
               '    object.values "^1.1.6"\n'
               '    resolve "^1.22.1"\n'
               '    semver "^6.3.0"\n'
               '    tsconfig-paths "^3.14.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=249,
          lineno=1123,
          tokens=131,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'eslint-plugin-jsx-a11y@^6.5.1:\n'
               '  version "6.7.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint-plugin-jsx-a11y/-/eslint-plugin-jsx-a11y-6.7.1.tgz"\n'
               '  integrity '
               'sha512-63Bog4iIethyo8smBklORknVjB0T2dwB8Mr/hIC+fBS0uyHdYYpzM/Ed+YC8VxTjlXHEWFOdmgwcDn1U2L9VCA==\n'
               '  dependencies:\n'
               '    '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=250,
          lineno=1129,
          tokens=175,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"@babel/runtime" "^7.20.7"\n'
               '    aria-query "^5.1.3"\n'
               '    array-includes "^3.1.6"\n'
               '    array.prototype.flatmap "^1.3.1"\n'
               '    ast-types-flow "^0.0.7"\n'
               '    axe-core "^4.6.2"\n'
               '    axobject-query "^3.1.1"\n'
               '    damerau-levenshtein "^1.0.8"\n'
               '    emoji-regex "^9.2.2"\n'
               '    has "^1.0.3"\n'
               '    jsx-ast-utils "^3.3.3"\n'
               '    language-tags "=1.0.5"\n'
               '    minimatch "^3.1.2"\n'
               '    object.entries "^1.1.6"\n'
               '    object.fromentries "^2.0.6"\n'
               '    semver "^6.3.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=251,
          lineno=1145,
          tokens=241,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'eslint-plugin-react-hooks@^4.5.0:\n'
               '  version "4.6.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint-plugin-react-hooks/-/eslint-plugin-react-hooks-4.6.0.tgz"\n'
               '  integrity '
               'sha512-oFc7Itz9Qxh2x4gNHStv3BqJq54ExXmfC+a1NjAta66IAN87Wu0R/QArgIS9qKzX3dXKPI9H5crl9QchNMY9+g==\n'
               '\n'
               'eslint-plugin-react@^7.31.7:\n'
               '  version "7.32.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint-plugin-react/-/eslint-plugin-react-7.32.2.tgz"\n'
               '  integrity '
               'sha512-t2fBMa+XzonrrNkyVirzKlvn5RXzzPwRHtMvLAtVZrt8oxgnTQaYbU6SXTOO1mwQgp1y5+toMSKInnzGr0Knqg==\n'
               '  dependencies:\n'
               '    '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=252,
          lineno=1156,
          tokens=169,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='array-includes "^3.1.6"\n'
               '    array.prototype.flatmap "^1.3.1"\n'
               '    array.prototype.tosorted "^1.1.1"\n'
               '    doctrine "^2.1.0"\n'
               '    estraverse "^5.3.0"\n'
               '    jsx-ast-utils "^2.4.1 || ^3.0.0"\n'
               '    minimatch "^3.1.2"\n'
               '    object.entries "^1.1.6"\n'
               '    object.fromentries "^2.0.6"\n'
               '    object.hasown "^1.1.2"\n'
               '    object.values "^1.1.6"\n'
               '    prop-types "^15.8.1"\n'
               '    resolve "^2.0.0-next.4"\n'
               '    semver "^6.3.0"\n'
               '    string.prototype.matchall "^4.0.8"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=253,
          lineno=1171,
          tokens=138,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'eslint-scope@^7.1.1:\n'
               '  version "7.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint-scope/-/eslint-scope-7.2.0.tgz"\n'
               '  integrity '
               'sha512-DYj5deGlHBfMt15J7rdtyKNq/Nqlv5KfU4iodrQ019XESsRnwXH9KAE0y3cwtUHDo2ob7CypAnCqefh6vioWRw==\n'
               '  dependencies:\n'
               '    esrecurse "^4.3.0"\n'
               '    estraverse "^5.2.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=254,
          lineno=1179,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'eslint-visitor-keys@^3.3.0, eslint-visitor-keys@^3.4.0, '
               'eslint-visitor-keys@^3.4.1:\n'
               '  version "3.4.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-3.4.1.tgz"\n'
               '  integrity '
               'sha512-pZnmmLwYzf+kWaM/Qgrvpen51upAktaaiI01nsJD/Yr3lMOdNtq0cxkrrg16w64VtisN6okbs7Q8AfGqj4c9fA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=255,
          lineno=1184,
          tokens=174,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'eslint@*, "eslint@^2 || ^3 || ^4 || ^5 || ^6 || ^7.2.0 || ^8", '
               '"eslint@^3 || ^4 || ^5 || ^6 || ^7 || ^8", "eslint@^3.0.0 || '
               '^4.0.0 || ^5.0.0 || ^6.0.0 || ^7.0.0 || ^8.0.0-0", '
               '"eslint@^6.0.0 || ^7.0.0 || ^8.0.0", "eslint@^6.0.0 || ^7.0.0 '
               '|| >=8.0.0", "eslint@^7.23.0 || ^8.0.0", eslint@8.37.0:\n'
               '  '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=256,
          lineno=1186,
          tokens=250,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='version "8.37.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/eslint/-/eslint-8.37.0.tgz"\n'
               '  integrity '
               'sha512-NU3Ps9nI05GUoVMxcZx1J8CNR6xOvUT4jAUMH5+z8lpp3aEdPVCImKw6PWG4PY+Vfkpr+jvMpxs/qoE7wq0sPw==\n'
               '  dependencies:\n'
               '    "@eslint-community/eslint-utils" "^4.2.0"\n'
               '    "@eslint-community/regexpp" "^4.4.0"\n'
               '    "@eslint/eslintrc" "^2.0.2"\n'
               '    "@eslint/js" "8.37.0"\n'
               '    "@humanwhocodes/config-array" "^0.11.8"\n'
               '    "@humanwhocodes/module-importer" "^1.0.1"\n'
               '    "@nodelib/fs.walk" "^1.2.8"\n'
               '    ajv "^6.10.0"\n'
               '    chalk "^4.0.0"\n'
               '    cross-spawn "^7.0.2"\n'
               '    debug "^4.3.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=257,
          lineno=1201,
          tokens=242,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='    doctrine "^3.0.0"\n'
               '    escape-string-regexp "^4.0.0"\n'
               '    eslint-scope "^7.1.1"\n'
               '    eslint-visitor-keys "^3.4.0"\n'
               '    espree "^9.5.1"\n'
               '    esquery "^1.4.2"\n'
               '    esutils "^2.0.2"\n'
               '    fast-deep-equal "^3.1.3"\n'
               '    file-entry-cache "^6.0.1"\n'
               '    find-up "^5.0.0"\n'
               '    glob-parent "^6.0.2"\n'
               '    globals "^13.19.0"\n'
               '    grapheme-splitter "^1.0.4"\n'
               '    ignore "^5.2.0"\n'
               '    import-fresh "^3.0.0"\n'
               '    imurmurhash "^0.1.4"\n'
               '    is-glob "^4.0.0"\n'
               '    is-path-inside "^3.0.3"\n'
               '    js-sdsl "^4.1.4"\n'
               '    js-yaml "^4.1.0"\n'
               '    json-stable-stringify-without-jsonify "^1.0.1"\n'
               '    levn "^0.4.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=258,
          lineno=1223,
          tokens=236,
          depth=3,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='    lodash.merge "^4.6.2"\n'
               '    minimatch "^3.1.2"\n'
               '    natural-compare "^1.4.0"\n'
               '    optionator "^0.9.1"\n'
               '    strip-ansi "^6.0.1"\n'
               '    strip-json-comments "^3.1.0"\n'
               '    text-table "^0.2.0"\n'
               '\n'
               'espree@^9.5.1, espree@^9.6.0:\n'
               '  version "9.6.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/espree/-/espree-9.6.0.tgz"\n'
               '  integrity '
               'sha512-1FH/IiruXZ84tpUlm0aCUEwMl2Ho5ilqVh0VvQXw+byAz/4SAciyHLlfmL5WYqsvD38oymdUwBss0LtK8m4s/A==\n'
               '  dependencies:\n'
               '    acorn "^8.9.0"\n'
               '    acorn-jsx "^5.3.2"\n'
               '    eslint-visitor-keys "^3.4.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=259,
          lineno=1239,
          tokens=126,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'esquery@^1.4.2:\n'
               '  version "1.5.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/esquery/-/esquery-1.5.0.tgz"\n'
               '  integrity '
               'sha512-YQLXUplAwJgCydQ78IMJywZCceoqk1oH01OERdSAJc/7U2AylwjhSCLDEtqwg811idIS/9fIU5GjG73IgjKMVg==\n'
               '  dependencies:\n'
               '    estraverse "^5.1.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=260,
          lineno=1246,
          tokens=129,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'esrecurse@^4.3.0:\n'
               '  version "4.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/esrecurse/-/esrecurse-4.3.0.tgz"\n'
               '  integrity '
               'sha512-KmfKL3b6G+RXvP8N1vr3Tq1kL/oCFgn2NYXEtqP8/L3pKapUA4G8cFVaoF3SU323CD4XypR/ffioHmkti6/Tag==\n'
               '  dependencies:\n'
               '    estraverse "^5.2.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=261,
          lineno=1253,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'estraverse@^5.1.0, estraverse@^5.2.0, estraverse@^5.3.0:\n'
               '  version "5.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz"\n'
               '  integrity '
               'sha512-MMdARuVEQziNTeJD8DgMqmhwR11BRQ/cBP+pLtYdSTnf3MIO8fFeiINEbX36ZdNlfU/7A9f3gUw49B3oQsvwBA==\n'
               '\n'
               'esutils@^2.0.2:\n'
               '  version "2.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz"\n'
               '  integrity '
               'sha512-kVscqXk4OCp68SZ0dkgEKVi6/8ij300KBWTJq32P/dYeWTSwK41WyTxalN1eRmA5Z9UU/LX9D7FWSmV9SAYx6g==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=262,
          lineno=1263,
          tokens=119,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'event-target-shim@^5.0.0:\n'
               '  version "5.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/event-target-shim/-/event-target-shim-5.0.1.tgz"\n'
               '  integrity '
               'sha512-i/2XbnSz/uxRCU6+NdVJgKWDTM427+MqYbkQzD321DuCQJUqOuJKIA0IM2+W2xtYHdKOmZ4dR6fExsd4SXL+WQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=263,
          lineno=1268,
          tokens=209,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'execa@^5.0.0:\n'
               '  version "5.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/execa/-/execa-5.1.1.tgz"\n'
               '  integrity '
               'sha512-8uSpZZocAZRBAPIEINJj3Lo9HyGitllczc27Eh5YYojjMFMn8yHMDMaUHE2Jqfq05D/wucwI4JGURyXt1vchyg==\n'
               '  dependencies:\n'
               '    cross-spawn "^7.0.3"\n'
               '    get-stream "^6.0.0"\n'
               '    human-signals "^2.1.0"\n'
               '    is-stream "^2.0.0"\n'
               '    merge-stream "^2.0.0"\n'
               '    npm-run-path "^4.0.1"\n'
               '    onetime "^5.1.2"\n'
               '    signal-exit "^3.0.3"\n'
               '    strip-final-newline "^2.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=264,
          lineno=1283,
          tokens=213,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'execa@^7.1.1:\n'
               '  version "7.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/execa/-/execa-7.1.1.tgz"\n'
               '  integrity '
               'sha512-wH0eMf/UXckdUYnO21+HDztteVv05rq2GXksxT4fCGeHkBhw1DROXh40wcjMcRqDOWE7iPJ4n3M7e2+YFP+76Q==\n'
               '  dependencies:\n'
               '    cross-spawn "^7.0.3"\n'
               '    get-stream "^6.0.1"\n'
               '    human-signals "^4.3.0"\n'
               '    is-stream "^3.0.0"\n'
               '    merge-stream "^2.0.0"\n'
               '    npm-run-path "^5.1.0"\n'
               '    onetime "^6.0.0"\n'
               '    signal-exit "^3.0.7"\n'
               '    strip-final-newline "^3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=265,
          lineno=1298,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'extend@^3.0.2, extend@~3.0.2:\n'
               '  version "3.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/extend/-/extend-3.0.2.tgz"\n'
               '  integrity '
               'sha512-fjquC59cD7CyW6urNXK0FBufkZcoiGG80wTuPujX590cB5Ttln20E2UB4S/WARVqhXffZl2LNgS+gQdPIIim/g==\n'
               '\n'
               'extsprintf@^1.2.0, extsprintf@1.3.0:\n'
               '  version "1.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/extsprintf/-/extsprintf-1.3.0.tgz"\n'
               '  integrity '
               'sha512-11Ndz7Nv+mvAC1j0ktTa7fAb0vLyGGX+rMHNBYQviQDGU0Hw7lhctJANqbPhu9nV9/izT/IntTgZ7Im/9LJs9g==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=266,
          lineno=1308,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'eyes@0.1.x:\n'
               '  version "0.1.8"\n'
               '  resolved "https://registry.npmjs.org/eyes/-/eyes-0.1.8.tgz"\n'
               '  integrity '
               'sha512-GipyPsXO1anza0AOZdy69Im7hGFCNB7Y/NGjDlZGJ3GJJLtwNSb2vrzYrTYJRrRloVx7pl+bhUaTB8yiccPvFQ==\n'
               '\n'
               'fast-deep-equal@^3.1.1, fast-deep-equal@^3.1.3:\n'
               '  version "3.1.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz"\n'
               '  integrity '
               'sha512-f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=267,
          lineno=1318,
          tokens=198,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'fast-glob@^3.2.12, fast-glob@^3.2.9, fast-glob@^3.3.0:\n'
               '  version "3.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.0.tgz"\n'
               '  integrity '
               'sha512-ChDuvbOypPuNjO8yIDf36x7BlZX1smcUMTTcyoIjycexOxd6DFsKsg21qVBzEmr3G7fUKIRy2/psii+CIUt7FA==\n'
               '  dependencies:\n'
               '    "@nodelib/fs.stat" "^2.0.2"\n'
               '    "@nodelib/fs.walk" "^1.2.3"\n'
               '    glob-parent "^5.1.2"\n'
               '    merge2 "^1.3.0"\n'
               '    micromatch "^4.0.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=268,
          lineno=1329,
          tokens=244,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'fast-json-stable-stringify@^2.0.0:\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz"\n'
               '  integrity '
               'sha512-lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw==\n'
               '\n'
               'fast-levenshtein@^2.0.6:\n'
               '  version "2.0.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/fast-levenshtein/-/fast-levenshtein-2.0.6.tgz"\n'
               '  integrity '
               'sha512-DCXu6Ifhqcks7TZKY3Hxp3y6qphY5SJZmrWMDrKcERSOXWQdMhU9Ig/PYrzyw/ul9jOIyh0N4M0tbC5hodg8dw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=269,
          lineno=1339,
          tokens=249,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'fastq@^1.6.0:\n'
               '  version "1.15.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/fastq/-/fastq-1.15.0.tgz"\n'
               '  integrity '
               'sha512-wBrocU2LCXXa+lWBt8RoIRD89Fi8OdABODa/kEnyeyjS5aZO5/GNvI5sEINADqP/h8M29UHTHUb53sUu5Ihqdw==\n'
               '  dependencies:\n'
               '    reusify "^1.0.4"\n'
               '\n'
               'file-entry-cache@^6.0.1:\n'
               '  version "6.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/file-entry-cache/-/file-entry-cache-6.0.1.tgz"\n'
               '  integrity '
               'sha512-7Gps/XWymbLk2QLYK4NzpMOrYjMhdIxXuIvy2QBsLE6ljuodKvdkWs/cpyJJ3CVIVpH0Oi1Hvg1ovbMzLdFBBg==\n'
               '  dependencies:\n'
               '    flat-cache "^3.0.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=270,
          lineno=1353,
          tokens=132,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'fill-range@^7.0.1:\n'
               '  version "7.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/fill-range/-/fill-range-7.0.1.tgz"\n'
               '  integrity '
               'sha512-qOo9F+dMUmC2Lcb4BbVvnKJxTPjCm+RRpe4gDuGrzkL7mEVl/djYSu2OdQ2Pa302N4oqkSg9ir6jaLWJ2USVpQ==\n'
               '  dependencies:\n'
               '    to-regex-range "^5.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=271,
          lineno=1360,
          tokens=136,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'find-up@^5.0.0:\n'
               '  version "5.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/find-up/-/find-up-5.0.0.tgz"\n'
               '  integrity '
               'sha512-78/PXT1wlLLDgTzDs7sjq9hzz0vXD+zn+7wypEe4fXQxCmdmqfGsEPQxmiCSQI3ajFV91bVSsvNtrJRiW6nGng==\n'
               '  dependencies:\n'
               '    locate-path "^6.0.0"\n'
               '    path-exists "^4.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=272,
          lineno=1368,
          tokens=143,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'flat-cache@^3.0.4:\n'
               '  version "3.0.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/flat-cache/-/flat-cache-3.0.4.tgz"\n'
               '  integrity '
               'sha512-dm9s5Pw7Jc0GvMYbshN6zchCA9RgQlzzEZX3vylR9IqFfS8XciblUXOKfW6SiuJ0e13eDYZoZV5wdrev7P3Nwg==\n'
               '  dependencies:\n'
               '    flatted "^3.1.0"\n'
               '    rimraf "^3.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=273,
          lineno=1376,
          tokens=232,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'flatted@^3.1.0:\n'
               '  version "3.2.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/flatted/-/flatted-3.2.7.tgz"\n'
               '  integrity '
               'sha512-5nqDSxl8nn5BSNxyR3n4I6eDmbolI6WT+QqR547RwxQapgjQBmtktdP+HTBb/a/zLsbzERTONyUB5pefh5TtjQ==\n'
               '\n'
               'follow-redirects@^1.15.0:\n'
               '  version "1.15.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/follow-redirects/-/follow-redirects-1.15.2.tgz"\n'
               '  integrity '
               'sha512-VQLG33o04KaQ8uYi2tVNbdrWp1QWxNNea+nmIB4EVM28v0hmP17z7aG1+wAkNzVq4KeXTq3221ye5qTJP91JwA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=274,
          lineno=1386,
          tokens=136,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'for-each@^0.3.3:\n'
               '  version "0.3.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/for-each/-/for-each-0.3.3.tgz"\n'
               '  integrity '
               'sha512-jqYfLp7mo9vIyQf8ykW2v7A+2N4QjeCeI5+Dz9XraiO1ign81wjiH7Fb9vSOWvQfNtmSa4H2RoQTrrXivdUZmw==\n'
               '  dependencies:\n'
               '    is-callable "^1.1.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=275,
          lineno=1393,
          tokens=115,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'forever-agent@~0.6.1:\n'
               '  version "0.6.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/forever-agent/-/forever-agent-0.6.1.tgz"\n'
               '  integrity '
               'sha512-j0KLYPhm6zeac4lz3oJ3o65qvgQCcPubiyotZrXqEaG4hNagNYO8qdlUrX5vwqv9ohqeT/Z3j6+yW067yWWdUw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=276,
          lineno=1398,
          tokens=150,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'form-data@^3.0.0:\n'
               '  version "3.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/form-data/-/form-data-3.0.1.tgz"\n'
               '  integrity '
               'sha512-RHkBKtLWUVwd7SqRIvCZMEvAMoGUp0XU+seQiZejj0COz3RI3hWP4sCv3gZWWLjJTd7rGwcsF5eKZGii0r/hbg==\n'
               '  dependencies:\n'
               '    asynckit "^0.4.0"\n'
               '    combined-stream "^1.0.8"\n'
               '    mime-types "^2.1.12"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=277,
          lineno=1407,
          tokens=142,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'form-data@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/form-data/-/form-data-4.0.0.tgz"\n'
               '  integrity '
               'sha512-ETEklSGi5t0QMZuiXoA/Q6vcnxcLQP5vdugSpuAyi6SVGi2clPPp+xgEhuMaHC+zGgn31Kd235W35f7Hykkaww==\n'
               '  dependencies:\n'
               '    asynckit "^0.4.0"\n'
               '    combined-stream "^1.0.8"\n'
               '    mime-types "^2.1.12"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=278,
          lineno=1416,
          tokens=152,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'form-data@~2.3.2:\n'
               '  version "2.3.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/form-data/-/form-data-2.3.3.tgz"\n'
               '  integrity '
               'sha512-1lLKB2Mu3aGP1Q/2eCOx0fNbRMe7XdwktwOruhfqqd0rIJWwN4Dh+E3hrPSlDCXnSR7UtZ1N38rVXm+6+MEhJQ==\n'
               '  dependencies:\n'
               '    asynckit "^0.4.0"\n'
               '    combined-stream "^1.0.6"\n'
               '    mime-types "^2.1.12"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=279,
          lineno=1425,
          tokens=229,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'fraction.js@^4.2.0:\n'
               '  version "4.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/fraction.js/-/fraction.js-4.2.0.tgz"\n'
               '  integrity '
               'sha512-MhLuK+2gUcnZe8ZHlaaINnQLl0xRIGRfcGk2yl8xoQAfHrSsL3rYu6FCmBdkdbhc9EPlwyGHewaRsvwRMJtAlA==\n'
               '\n'
               'fs.realpath@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/fs.realpath/-/fs.realpath-1.0.0.tgz"\n'
               '  integrity '
               'sha512-OO0pH2lK6a0hZnAdau5ItzHPI6pUlvI7jMVnxUQRtw4owF2wk8lOSabtGDCTP4Ggrg2MbGnWO9X8K1t4+fGMDw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=280,
          lineno=1435,
          tokens=109,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'function-bind@^1.1.1:\n'
               '  version "1.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/function-bind/-/function-bind-1.1.1.tgz"\n'
               '  integrity '
               'sha512-yIovAzMX49sF8Yl58fSCWJ5svSLuaibPxXQJFLmBObTuCr0Mf1KiPopGM9NiFjiYBCbfaa2Fh6breQ6ANVTI0A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=281,
          lineno=1440,
          tokens=158,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'function.prototype.name@^1.1.5:\n'
               '  version "1.1.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/function.prototype.name/-/function.prototype.name-1.1.5.tgz"\n'
               '  integrity '
               'sha512-uN7m/BzVKQnCUF/iW8jYea67v++2u7m5UgENbHRtdDVclOUP+FMPlCNdmk0h/ysGyo2tavMJEDqJAkJdRa1vMA==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.3"\n'
               '    es-abstract "^1.19.0"\n'
               '    functions-have-names "^1.2.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=282,
          lineno=1450,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'functions-have-names@^1.2.2, functions-have-names@^1.2.3:\n'
               '  version "1.2.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/functions-have-names/-/functions-have-names-1.2.3.tgz"\n'
               '  integrity '
               'sha512-xckBUXyTIqT97tq2x2AMb+g163b5JFysYk0x4qxNFwbfQkmNZoiRHb6sPzI9/QV33WeuvVYBUIiD4NzNIyqaRQ==\n'
               '\n'
               'get-caller-file@^2.0.5:\n'
               '  version "2.0.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/get-caller-file/-/get-caller-file-2.0.5.tgz"\n'
               '  integrity '
               'sha512-DyFP3BM/3YHTQOCUL/w0OZHR0lpKeGrxotcHWcqNEdnltqFwXVfhEBQ94eIo34AfQpo0rGki4cyIiftY06h2Fg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=283,
          lineno=1460,
          tokens=196,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'get-intrinsic@^1.0.2, get-intrinsic@^1.1.1, '
               'get-intrinsic@^1.1.3, get-intrinsic@^1.2.0:\n'
               '  version "1.2.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/get-intrinsic/-/get-intrinsic-1.2.1.tgz"\n'
               '  integrity '
               'sha512-2DcsyfABl+gVHEfCOaTrWgyt+tb6MSEGmKq+kI5HwLbIYgjgmMcV8KQ41uaKz1xxUcn9tJtgFbQUEVcEbd0FYw==\n'
               '  dependencies:\n'
               '    function-bind "^1.1.1"\n'
               '    has "^1.0.3"\n'
               '    has-proto "^1.0.1"\n'
               '    has-symbols "^1.0.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=284,
          lineno=1470,
          tokens=121,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'get-stream@^6.0.0, get-stream@^6.0.1:\n'
               '  version "6.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/get-stream/-/get-stream-6.0.1.tgz"\n'
               '  integrity '
               'sha512-ts6Wi+2j3jQjqi70w5AlN8DFnkSwC+MqmxEzdEALB2qXZYV3X/b1CTfgPLGJNMeAWxdPfU8FO1ms3NUfaHCPYg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=285,
          lineno=1475,
          tokens=142,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'get-symbol-description@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/get-symbol-description/-/get-symbol-description-1.0.0.tgz"\n'
               '  integrity '
               'sha512-2EmdH1YvIQiZpltCNgkuiUnyukzxM/R6NDJX31Ke3BG1Nq5b0S2PhX59UKi9vZpPDQVdqn+1IcaAwnzTT5vCjw==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    get-intrinsic "^1.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=286,
          lineno=1483,
          tokens=132,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'get-tsconfig@^4.5.0:\n'
               '  version "4.6.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/get-tsconfig/-/get-tsconfig-4.6.2.tgz"\n'
               '  integrity '
               'sha512-E5XrT4CbbXcXWy+1jChlZmrmCwd5KGx502kDCXJJ7y898TtWW9FwoG5HfOLVRKmlmDGkWN2HM9Ho+/Y8F0sJDg==\n'
               '  dependencies:\n'
               '    resolve-pkg-maps "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=287,
          lineno=1490,
          tokens=129,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'getpass@^0.1.1:\n'
               '  version "0.1.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/getpass/-/getpass-0.1.7.tgz"\n'
               '  integrity '
               'sha512-0fzj9JxOLfJ+XGLhR8ze3unN0KZCgZwiSSDz168VERjK8Wl8kVSdcu2kspd4s4wtAa1y/qrVRiAA0WclVsu0ng==\n'
               '  dependencies:\n'
               '    assert-plus "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=288,
          lineno=1497,
          tokens=131,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'glob-parent@^5.1.2:\n'
               '  version "5.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz"\n'
               '  integrity '
               'sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==\n'
               '  dependencies:\n'
               '    is-glob "^4.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=289,
          lineno=1504,
          tokens=131,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'glob-parent@^6.0.2:\n'
               '  version "6.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz"\n'
               '  integrity '
               'sha512-XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==\n'
               '  dependencies:\n'
               '    is-glob "^4.0.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=290,
          lineno=1511,
          tokens=131,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'glob-parent@~5.1.2:\n'
               '  version "5.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz"\n'
               '  integrity '
               'sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==\n'
               '  dependencies:\n'
               '    is-glob "^4.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=291,
          lineno=1518,
          tokens=176,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'glob@^7.1.3, glob@7.1.7:\n'
               '  version "7.1.7"\n'
               '  resolved "https://registry.npmjs.org/glob/-/glob-7.1.7.tgz"\n'
               '  integrity '
               'sha512-OvD9ENzPLbegENnYP5UUfJIirTg4+XwMWGaQfQTY0JenxNvvIKP3U3/tAQSPIu/lHxXYSZmpXlUHeqAIdKzBLQ==\n'
               '  dependencies:\n'
               '    fs.realpath "^1.0.0"\n'
               '    inflight "^1.0.4"\n'
               '    inherits "2"\n'
               '    minimatch "^3.0.4"\n'
               '    once "^1.3.0"\n'
               '    path-is-absolute "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=292,
          lineno=1530,
          tokens=156,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'glob@^8.1.0:\n'
               '  version "8.1.0"\n'
               '  resolved "https://registry.npmjs.org/glob/-/glob-8.1.0.tgz"\n'
               '  integrity '
               'sha512-r8hpEjiQEYlF2QU0df3dS+nxxSIreXQS1qRhMJM0Q5NDdR386C7jb7Hwwod8Fgiuex+k0GFjgft18yvxm5XoCQ==\n'
               '  dependencies:\n'
               '    fs.realpath "^1.0.0"\n'
               '    inflight "^1.0.4"\n'
               '    inherits "2"\n'
               '    minimatch "^5.0.1"\n'
               '    once "^1.3.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=293,
          lineno=1541,
          tokens=166,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'glob@7.1.6:\n'
               '  version "7.1.6"\n'
               '  resolved "https://registry.npmjs.org/glob/-/glob-7.1.6.tgz"\n'
               '  integrity '
               'sha512-LwaxwyZ72Lk7vZINtNNrywX0ZuLyStrdDtabefZKAY5ZGJhVtgdznluResxNmPitE0SAO+O26sWTHeKSI2wMBA==\n'
               '  dependencies:\n'
               '    fs.realpath "^1.0.0"\n'
               '    inflight "^1.0.4"\n'
               '    inherits "2"\n'
               '    minimatch "^3.0.4"\n'
               '    once "^1.3.0"\n'
               '    path-is-absolute "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=294,
          lineno=1553,
          tokens=249,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'globals@^13.19.0:\n'
               '  version "13.20.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/globals/-/globals-13.20.0.tgz"\n'
               '  integrity '
               'sha512-Qg5QtVkCy/kv3FUSlu4ukeZDVf9ee0iXLAUYX13gbR17bnejFTzr4iS9bY7kwCf1NztRNm1t91fjOiyx4CSwPQ==\n'
               '  dependencies:\n'
               '    type-fest "^0.20.2"\n'
               '\n'
               'globalthis@^1.0.3:\n'
               '  version "1.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/globalthis/-/globalthis-1.0.3.tgz"\n'
               '  integrity '
               'sha512-sFdI5LyBiNTHjRd7cGPWapiHWMOXKyuBNX/cWJ3NfzrZQVa8GI/8cofCl74AOVqq9W5kNmguTIzJ/1s2gyI9wA==\n'
               '  dependencies:\n'
               '    define-properties "^1.1.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=295,
          lineno=1567,
          tokens=178,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'globby@^11.1.0:\n'
               '  version "11.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/globby/-/globby-11.1.0.tgz"\n'
               '  integrity '
               'sha512-jhIXaOzy1sb8IyocaruWSn1TjmnBVs8Ayhcy83rmxNJ8q2uWKCAj3CnJY+KpGSXCueAPc0i05kVvVKtP1t9S3g==\n'
               '  dependencies:\n'
               '    array-union "^2.1.0"\n'
               '    dir-glob "^3.0.1"\n'
               '    fast-glob "^3.2.9"\n'
               '    ignore "^5.2.0"\n'
               '    merge2 "^1.4.1"\n'
               '    slash "^3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=296,
          lineno=1579,
          tokens=164,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'globby@^13.1.3:\n'
               '  version "13.2.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/globby/-/globby-13.2.2.tgz"\n'
               '  integrity '
               'sha512-Y1zNGV+pzQdh7H39l9zgB4PJqjRNqydvdYCDG4HFXM4XuvSaQQlEc91IU1yALL8gUTDomgBAfz3XJdmUS+oo0w==\n'
               '  dependencies:\n'
               '    dir-glob "^3.0.1"\n'
               '    fast-glob "^3.3.0"\n'
               '    ignore "^5.2.4"\n'
               '    merge2 "^1.4.1"\n'
               '    slash "^4.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=297,
          lineno=1590,
          tokens=244,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'goober@^2.1.10:\n'
               '  version "2.1.13"\n'
               '  resolved '
               '"https://registry.npmjs.org/goober/-/goober-2.1.13.tgz"\n'
               '  integrity '
               'sha512-jFj3BQeleOoy7t93E9rZ2de+ScC4lQICLwiAQmKMg9F6roKGaLSHoCDYKkWlSafg138jejvq/mTdvmnwDQgqoQ==\n'
               '\n'
               'gopd@^1.0.1:\n'
               '  version "1.0.1"\n'
               '  resolved "https://registry.npmjs.org/gopd/-/gopd-1.0.1.tgz"\n'
               '  integrity '
               'sha512-d65bNlIadxvpb/A2abVdlqKqV563juRnZ1Wtk6s1sIR8uNsXR70xqIzVqxVf1eTqDunwT2MkczEeaezCKTZhwA==\n'
               '  dependencies:\n'
               '    get-intrinsic "^1.1.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=298,
          lineno=1602,
          tokens=239,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'graceful-fs@^4.2.4:\n'
               '  version "4.2.11"\n'
               '  resolved '
               '"https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz"\n'
               '  integrity '
               'sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ==\n'
               '\n'
               'grapheme-splitter@^1.0.4:\n'
               '  version "1.0.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/grapheme-splitter/-/grapheme-splitter-1.0.4.tgz"\n'
               '  integrity '
               'sha512-bzh50DW9kTPM00T8y4o8vQg89Di9oLJVLW/KaOGIXJWP/iqCN6WKYkbNOF04vFLJhwcpYUh9ydh/+5vpOqV4YQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=299,
          lineno=1612,
          tokens=250,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'har-schema@^2.0.0:\n'
               '  version "2.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/har-schema/-/har-schema-2.0.0.tgz"\n'
               '  integrity '
               'sha512-Oqluz6zhGX8cyRaTQlFMPw80bSJVG2x/cFb8ZPhUILGgHka9SsokCCOQgpveePerqidZOrT14ipqfJb7ILcW5Q==\n'
               '\n'
               'har-validator@~5.1.3:\n'
               '  version "5.1.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/har-validator/-/har-validator-5.1.5.tgz"\n'
               '  integrity '
               'sha512-nmT2T0lljbxdQZfspsno9hgrG3Uir6Ks5afism62poxqBM6sDnMEuPmzTq8XN0OEwqKLLdh1jQI3qyE66Nzb3w==\n'
               '  dependencies:\n'
               '    ajv "^6.12.3"\n'
               '    har-schema "^2.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=300,
          lineno=1625,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'has-bigints@^1.0.1, has-bigints@^1.0.2:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/has-bigints/-/has-bigints-1.0.2.tgz"\n'
               '  integrity '
               'sha512-tSvCKtBr9lkF0Ex0aQiP9N+OpV4zi2r/Nee5VkRDbaqv35RLYMzbwQfFSZZH0kR+Rd6302UJZ2p/bJCEoR3VoQ==\n'
               '\n'
               'has-flag@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/has-flag/-/has-flag-4.0.0.tgz"\n'
               '  integrity '
               'sha512-EykJT/Q1KjTWctppgIAgfSO0tKVuZUjhgMr17kqTumMl6Afv3EISleU7qZUzoXDFTAHTDC4NOoG/ZxU3EvlMPQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=301,
          lineno=1635,
          tokens=135,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'has-property-descriptors@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/has-property-descriptors/-/has-property-descriptors-1.0.0.tgz"\n'
               '  integrity '
               'sha512-62DVLZGoiEBDHQyqG4w9xCuZ7eJEwNmJRWw2VY84Oedb7WFcA27fiEVe8oUQx9hAUJ4ekurquucTGwsyO1XGdQ==\n'
               '  dependencies:\n'
               '    get-intrinsic "^1.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=302,
          lineno=1642,
          tokens=245,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'has-proto@^1.0.1:\n'
               '  version "1.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/has-proto/-/has-proto-1.0.1.tgz"\n'
               '  integrity '
               'sha512-7qE+iP+O+bgF9clE5+UoBFzE65mlBiVj3tKCrlNQ0Ogwm0BjpT/gK4SlLYDMybDh5I3TCTKnPPa0oMG7JDYrhg==\n'
               '\n'
               'has-symbols@^1.0.2, has-symbols@^1.0.3:\n'
               '  version "1.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/has-symbols/-/has-symbols-1.0.3.tgz"\n'
               '  integrity '
               'sha512-l3LCuF6MgDNwTDKkdYGEihYjt5pRPbEg46rtlmnSPlUbgmB8LOIrKJbYYFBSbnPaJexMKtiPO8hmeRjRz2Td+A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=303,
          lineno=1652,
          tokens=133,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'has-tostringtag@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/has-tostringtag/-/has-tostringtag-1.0.0.tgz"\n'
               '  integrity '
               'sha512-kFjcSNhnlGV1kyoGk7OXKSawH5JOb/LzUc5w9B02hOTO0dfFRjbHQKvg1d6cf3HbeUmtU9VbbV3qzZ2Teh97WQ==\n'
               '  dependencies:\n'
               '    has-symbols "^1.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=304,
          lineno=1659,
          tokens=230,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'has@^1.0.3:\n'
               '  version "1.0.3"\n'
               '  resolved "https://registry.npmjs.org/has/-/has-1.0.3.tgz"\n'
               '  integrity '
               'sha512-f2dvO0VU6Oej7RkWJGrehjbzMAjFp5/VKPp5tTpWIV4JHHZK1/BxbFRtf/siA2SWTe09caDmVtYYzWEIbBS4zw==\n'
               '  dependencies:\n'
               '    function-bind "^1.1.1"\n'
               '\n'
               'highlight.js@^10.7.1:\n'
               '  version "10.7.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/highlight.js/-/highlight.js-10.7.3.tgz"\n'
               '  integrity '
               'sha512-tzcUFauisWKNHaRkN4Wjl/ZA07gENAjFl3J/c480dprkGTg5EQstgaNFqBfUqCq54kZRIEcreTsAgF/m2quD7A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=305,
          lineno=1671,
          tokens=168,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'http-errors@^1.8.1:\n'
               '  version "1.8.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/http-errors/-/http-errors-1.8.1.tgz"\n'
               '  integrity '
               'sha512-Kpk9Sm7NmI+RHhnj6OIWDI1d6fIoFAtFt9RLaTMRlg/8w49juAStsrBgp0Dp4OdxdVbRIeKhtCUvoi/RuAhO4g==\n'
               '  dependencies:\n'
               '    depd "~1.1.2"\n'
               '    inherits "2.0.4"\n'
               '    setprototypeof "1.2.0"\n'
               '    statuses ">= 1.5.0 < 2"\n'
               '    toidentifier "1.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=306,
          lineno=1682,
          tokens=152,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'http-signature@~1.2.0:\n'
               '  version "1.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/http-signature/-/http-signature-1.2.0.tgz"\n'
               '  integrity '
               'sha512-CAbnr6Rz4CYQkLYUtSNXxQPUH2gK8f3iWexVlsnMeD+GjlsQ0Xsy1cOX+mN3dtxYomRy21CiOzU8Uhw6OwncEQ==\n'
               '  dependencies:\n'
               '    assert-plus "^1.0.0"\n'
               '    jsprim "^1.2.2"\n'
               '    sshpk "^1.7.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=307,
          lineno=1691,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'human-signals@^2.1.0:\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/human-signals/-/human-signals-2.1.0.tgz"\n'
               '  integrity '
               'sha512-B4FFZ6q/T2jhhksgkbEW3HBvWIfDW85snkQgawt07S7J5QXTk6BkNV+0yAeZrM5QpMAdYlocGoljn0sJ/WQkFw==\n'
               '\n'
               'human-signals@^4.3.0:\n'
               '  version "4.3.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/human-signals/-/human-signals-4.3.1.tgz"\n'
               '  integrity '
               'sha512-nZXjEF2nbo7lIw3mgYjItAfgQXog3OjJogSbKa2CQIIvSGWcKgeJnQlNXip6NglNzYH45nSRiEVimMvYL8DDqQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=308,
          lineno=1701,
          tokens=137,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'iconv-lite@^0.6.2:\n'
               '  version "0.6.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/iconv-lite/-/iconv-lite-0.6.3.tgz"\n'
               '  integrity '
               'sha512-4fCk79wshMdzMp2rH06qWrJE4iolqLhCUH+OiuIgU++RB0+94NlDL81atO7GX55uUKueo0txHNtvEyI6D7WdMw==\n'
               '  dependencies:\n'
               '    safer-buffer ">= 2.1.2 < 3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=309,
          lineno=1708,
          tokens=235,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'ieee754@^1.2.1:\n'
               '  version "1.2.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/ieee754/-/ieee754-1.2.1.tgz"\n'
               '  integrity '
               'sha512-dcyqhDvX1C46lXZcVqCpK+FtMRQVdIMN6/Df5js2zouUsqG7I6sFxitIC+7KYK29KdXOLHdu9zL4sFnoVQnqaA==\n'
               '\n'
               'ignore@^5.2.0, ignore@^5.2.4:\n'
               '  version "5.2.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/ignore/-/ignore-5.2.4.tgz"\n'
               '  integrity '
               'sha512-MAb38BcSbH0eHNBxn7ql2NH/kX33OkB3lZ1BNdh7ENeRChHTYsTvWrMubiIAMNS2llXEEgZ1MUOBtXChP3kaFQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=310,
          lineno=1718,
          tokens=150,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'import-fresh@^3.0.0, import-fresh@^3.2.1:\n'
               '  version "3.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/import-fresh/-/import-fresh-3.3.0.tgz"\n'
               '  integrity '
               'sha512-veYYhQa+D1QBKznvhUHxb8faxlrwUnxseDAbAp457E0wLNio2bOSKnjYDhMj+YiAq61xrMGhQk9iXVk5FzgQMw==\n'
               '  dependencies:\n'
               '    parent-module "^1.0.0"\n'
               '    resolve-from "^4.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=311,
          lineno=1726,
          tokens=244,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'imurmurhash@^0.1.4:\n'
               '  version "0.1.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz"\n'
               '  integrity '
               'sha512-JmXMZ6wuvDmLiHEml9ykzqO6lwFbof0GG4IkcGaENdCRDDmMVnny7s5HsIgHCbaq0w2MyPhDqkhTUgS2LU2PHA==\n'
               '\n'
               'inflight@^1.0.4:\n'
               '  version "1.0.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/inflight/-/inflight-1.0.6.tgz"\n'
               '  integrity '
               'sha512-k92I/b08q4wvFscXCLvqfsHCrjrF7yiXsQuIVvVE7N82W3+aqpzuUdBbfhWcy/FZR3/4IgflMgKLOsvPDrGCJA==\n'
               '  dependencies:\n'
               '    once "^1.3.0"\n'
               '    wrappy "1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=312,
          lineno=1739,
          tokens=120,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'inherits@^2.0.1, inherits@2, inherits@2.0.4:\n'
               '  version "2.0.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/inherits/-/inherits-2.0.4.tgz"\n'
               '  integrity '
               'sha512-k/vGaX4/Yla3WzyMCvTQOXYeIHvqOKtnqBduzTHpzpQZzAskKMhZ2K+EnBiSM9zGSoIFeMpXKxa4dYeZIQqewQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=313,
          lineno=1744,
          tokens=154,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'internal-slot@^1.0.3, internal-slot@^1.0.5:\n'
               '  version "1.0.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/internal-slot/-/internal-slot-1.0.5.tgz"\n'
               '  integrity '
               'sha512-Y+R5hJrzs52QCG2laLn4udYVnxsfny9CpOhNhUvk/SSSVyF6T27FzRbF0sroPidSu3X8oEAkOn2K804mjpt6UQ==\n'
               '  dependencies:\n'
               '    get-intrinsic "^1.2.0"\n'
               '    has "^1.0.3"\n'
               '    side-channel "^1.0.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=314,
          lineno=1753,
          tokens=228,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'ioredis@^5.0.4, ioredis@^5.3.2:\n'
               '  version "5.3.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/ioredis/-/ioredis-5.3.2.tgz"\n'
               '  integrity '
               'sha512-1DKMMzlIHM02eBBVOFQ1+AolGjs6+xEcM4PDL7NqOS6szq7H9jSaEkIUH6/a5Hl241LzW6JLSiAbNvTQjUupUA==\n'
               '  dependencies:\n'
               '    "@ioredis/commands" "^1.1.1"\n'
               '    cluster-key-slot "^1.1.0"\n'
               '    debug "^4.3.4"\n'
               '    denque "^2.1.0"\n'
               '    lodash.defaults "^4.2.0"\n'
               '    lodash.isarguments "^3.1.0"\n'
               '    redis-errors "^1.2.0"\n'
               '    redis-parser "^3.0.0"\n'
               '    standard-as-callback "^2.1.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=315,
          lineno=1768,
          tokens=160,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-array-buffer@^3.0.1, is-array-buffer@^3.0.2:\n'
               '  version "3.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-array-buffer/-/is-array-buffer-3.0.2.tgz"\n'
               '  integrity '
               'sha512-y+FyyR/w8vfIRq4eQcM1EYgSTnmHXPqaF+IgzgraytCFq5Xh8lllDVmAZolPJiZttZLeFSINPYMaEJ7/vWUa1w==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    get-intrinsic "^1.2.0"\n'
               '    is-typed-array "^1.1.10"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=316,
          lineno=1777,
          tokens=246,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-base64@^1.1.0:\n'
               '  version "1.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-base64/-/is-base64-1.1.0.tgz"\n'
               '  integrity '
               'sha512-Nlhg7Z2dVC4/PTvIFkgVVNvPHSO2eR/Yd0XzhGiXCXEvWnptXlXa/clQ8aePPiMuxEGcWfzWbGw2Fe3d+Y3v1g==\n'
               '\n'
               'is-bigint@^1.0.1:\n'
               '  version "1.0.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-bigint/-/is-bigint-1.0.4.tgz"\n'
               '  integrity '
               'sha512-zB9CruMamjym81i2JZ3UMn54PKGsQzsJeo6xvN3HJJ4CAsQNB6iRutp2To77OfCNuoxspsIhzaPoO1zyCEhFOg==\n'
               '  dependencies:\n'
               '    has-bigints "^1.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=317,
          lineno=1789,
          tokens=124,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-binary-path@~2.1.0:\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz"\n'
               '  integrity '
               'sha512-ZMERYes6pDydyuGidse7OsHxtbI7WVeUEozgR/g7rd0xUimYNlvZRE/K2MgZTjWy725IfelLeVcEM97mmtRGXw==\n'
               '  dependencies:\n'
               '    binary-extensions "^2.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=318,
          lineno=1796,
          tokens=144,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-boolean-object@^1.1.0:\n'
               '  version "1.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-boolean-object/-/is-boolean-object-1.1.2.tgz"\n'
               '  integrity '
               'sha512-gDYaKHJmnj4aWxyj6YHyXVpdQawtVLHU5cb+eztPGczf6cjuTdwve5ZIEfgXqH4e57An1D1AKf8CZ3kYrQRqYA==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    has-tostringtag "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=319,
          lineno=1804,
          tokens=140,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-callable@^1.1.3, is-callable@^1.1.4, is-callable@^1.2.7:\n'
               '  version "1.2.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-callable/-/is-callable-1.2.7.tgz"\n'
               '  integrity '
               'sha512-1BC0BVFhS/p0qtw6enp8e+8OD0UrK0oFLztSjNzhcKA3WDuJxxAPXzPuPtKkjEY9UUoEWlX/8fgKeu2S8i9JTA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=320,
          lineno=1809,
          tokens=138,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-core-module@^2.11.0, is-core-module@^2.9.0:\n'
               '  version "2.12.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-core-module/-/is-core-module-2.12.1.tgz"\n'
               '  integrity '
               'sha512-Q4ZuBAe2FUsKtyQJoQHlvP8OvBERxO3jEmy1I7hcRXcJBGGHFh/aJBswbXuS9sgrDH2QUO8ilkwNPHvHMd8clg==\n'
               '  dependencies:\n'
               '    has "^1.0.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=321,
          lineno=1816,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-date-object@^1.0.1:\n'
               '  version "1.0.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-date-object/-/is-date-object-1.0.5.tgz"\n'
               '  integrity '
               'sha512-9YQaSxsAiSwcvS33MBk3wTCVnWK+HhF8VZR2jRxehM16QcVOdHqPn4VPHmRK4lSr38n9JriurInLcP90xsYNfQ==\n'
               '  dependencies:\n'
               '    has-tostringtag "^1.0.0"\n'
               '\n'
               'is-docker@^2.0.0:\n'
               '  version "2.2.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-docker/-/is-docker-2.2.1.tgz"\n'
               '  integrity '
               'sha512-F+i2BKsFrH66iaUFc0woD8sLy8getkwTwtOBjvs56Cx4CgJDeKQeqfz8wAYiSb8JOprWhHH5p77PbmYCvvUuXQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=322,
          lineno=1828,
          tokens=235,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-docker@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-docker/-/is-docker-3.0.0.tgz"\n'
               '  integrity '
               'sha512-eljcgEDlEns/7AXFosB5K/2nCM4P7FQPkGc/DWLy5rmFEWvZayGrik1d9/QIY5nJ4f9YsVvBkA6kJpHn9rISdQ==\n'
               '\n'
               'is-extglob@^2.1.1:\n'
               '  version "2.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz"\n'
               '  integrity '
               'sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=323,
          lineno=1838,
          tokens=118,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-fullwidth-code-point@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz"\n'
               '  integrity '
               'sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=324,
          lineno=1843,
          tokens=161,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-glob@^4.0.0, is-glob@^4.0.1, is-glob@^4.0.3, '
               'is-glob@~4.0.1:\n'
               '  version "4.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz"\n'
               '  integrity '
               'sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==\n'
               '  dependencies:\n'
               '    is-extglob "^2.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=325,
          lineno=1850,
          tokens=244,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-inside-container@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-inside-container/-/is-inside-container-1.0.0.tgz"\n'
               '  integrity '
               'sha512-KIYLCCJghfHZxqjYBE7rEy0OBuTd5xCHS7tHVgvCLkx7StIoaxwNW3hCALgEUjFfeRk+MG/Qxmp/vtETEF3tRA==\n'
               '  dependencies:\n'
               '    is-docker "^3.0.0"\n'
               '\n'
               'is-negative-zero@^2.0.2:\n'
               '  version "2.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-negative-zero/-/is-negative-zero-2.0.2.tgz"\n'
               '  integrity '
               'sha512-dqJvarLawXsFbNDeJW7zAz8ItJ9cd28YufuuFzh0G8pNHjJMnY08Dv7sYX2uF5UpQOwieAeOExEYAWWfu7ZZUA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=326,
          lineno=1862,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-number-object@^1.0.4:\n'
               '  version "1.0.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-number-object/-/is-number-object-1.0.7.tgz"\n'
               '  integrity '
               'sha512-k1U0IRzLMo7ZlYIfzRu23Oh6MiIFasgpb9X76eqfFZAqwH44UI4KTBvBYIZ1dSL9ZzChTB9ShHfLkR4pdW5krQ==\n'
               '  dependencies:\n'
               '    has-tostringtag "^1.0.0"\n'
               '\n'
               'is-number@^7.0.0:\n'
               '  version "7.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz"\n'
               '  integrity '
               'sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=327,
          lineno=1874,
          tokens=119,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-path-inside@^3.0.3:\n'
               '  version "3.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-path-inside/-/is-path-inside-3.0.3.tgz"\n'
               '  integrity '
               'sha512-Fd4gABb+ycGAmKou8eMftCupSir5lRxqf4aD/vd0cD2qc4HL07OjCeuHMr8Ro4CoMaeCKDB0/ECBOVWjTwUvPQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=328,
          lineno=1879,
          tokens=136,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-regex@^1.1.4:\n'
               '  version "1.1.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-regex/-/is-regex-1.1.4.tgz"\n'
               '  integrity '
               'sha512-kvRdxDsxZjhzUX07ZnLydzS1TU/TJlTUHHY4YLL87e37oUA49DfkLqgy+VjFocowy29cKvcSiu+kIv728jTTVg==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    has-tostringtag "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=329,
          lineno=1887,
          tokens=241,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-shared-array-buffer@^1.0.2:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-shared-array-buffer/-/is-shared-array-buffer-1.0.2.tgz"\n'
               '  integrity '
               'sha512-sqN2UDu1/0y6uvXyStCOzyhAjCSlHceFoMKJW8W9EU9cvic/QdsZ0kEU93HEy3IUEFZIiH/3w+AH/UQbPHNdhA==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '\n'
               'is-stream@^2.0.0:\n'
               '  version "2.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-stream/-/is-stream-2.0.1.tgz"\n'
               '  integrity '
               'sha512-hFoiJiTl63nn+kstHGBtewWSKnQLpyb155KHheA1l39uvtO9nWIop1p3udqPcUd/xbF1VLMO4n7OI6p7RbngDg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=330,
          lineno=1899,
          tokens=245,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-stream@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-stream/-/is-stream-3.0.0.tgz"\n'
               '  integrity '
               'sha512-LnQR4bZ9IADDRSkvpqMGvt/tEJWclzklNgSw48V5EAaAeDd6qGvN8ei6k5p0tvxSR171VmGyHuTiAOfxAbr8kA==\n'
               '\n'
               'is-string@^1.0.5, is-string@^1.0.7:\n'
               '  version "1.0.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-string/-/is-string-1.0.7.tgz"\n'
               '  integrity '
               'sha512-tE2UXzivje6ofPW7l23cjDOMa09gb7xlAqG6jG5ej6uPV32TlWP3NKPigtaGeHNu9fohccRYvIiZMfOOnOYUtg==\n'
               '  dependencies:\n'
               '    has-tostringtag "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=331,
          lineno=1911,
          tokens=131,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-symbol@^1.0.2, is-symbol@^1.0.3:\n'
               '  version "1.0.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-symbol/-/is-symbol-1.0.4.tgz"\n'
               '  integrity '
               'sha512-C/CPBqKWnvdcxqIARxyOh4v1UUEOCHpgDa0WYgpKDFMszcrPcffg5uhwSgPCLD2WWxmq6isisz87tzT01tuGhg==\n'
               '  dependencies:\n'
               '    has-symbols "^1.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=332,
          lineno=1918,
          tokens=196,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-typed-array@^1.1.10, is-typed-array@^1.1.9:\n'
               '  version "1.1.10"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-typed-array/-/is-typed-array-1.1.10.tgz"\n'
               '  integrity '
               'sha512-PJqgEHiWZvMpaFZ3uTc8kHPM4+4ADTlDniuQL7cU/UDA0Ql7F70yGfHph3cLNe+c9toaigv+DFzTJKhc2CtO6A==\n'
               '  dependencies:\n'
               '    available-typed-arrays "^1.0.5"\n'
               '    call-bind "^1.0.2"\n'
               '    for-each "^0.3.3"\n'
               '    gopd "^1.0.1"\n'
               '    has-tostringtag "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=333,
          lineno=1929,
          tokens=248,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-typedarray@~1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-typedarray/-/is-typedarray-1.0.0.tgz"\n'
               '  integrity '
               'sha512-cyA56iCMHAh5CdzjJIa4aohJyeO1YbwLi3Jc35MmRU6poroFjIGZzUzupGiRPOjgHg9TLu43xbpwXk523fMxKA==\n'
               '\n'
               'is-weakref@^1.0.2:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-weakref/-/is-weakref-1.0.2.tgz"\n'
               '  integrity '
               'sha512-qctsuLZmIQ0+vSSMfoVvyFe2+GSEvnmZ2ezTup1SBse9+twCCeial6EEi3Nc2KFcf6+qz2FBPnjXsk8xhKSaPQ==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=334,
          lineno=1941,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'is-wsl@^2.2.0:\n'
               '  version "2.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/is-wsl/-/is-wsl-2.2.0.tgz"\n'
               '  integrity '
               'sha512-fKzAra0rGJUUBwGBgNkHZuToZcn+TtXHpeCgmkMJMMYx1sQDYaCSyjJBSCa2nH1DGm7s3n1oBnohoVTBaN7Lww==\n'
               '  dependencies:\n'
               '    is-docker "^2.0.0"\n'
               '\n'
               'isexe@^2.0.0:\n'
               '  version "2.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz"\n'
               '  integrity '
               'sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=335,
          lineno=1953,
          tokens=144,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'isomorphic-fetch@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/isomorphic-fetch/-/isomorphic-fetch-3.0.0.tgz"\n'
               '  integrity '
               'sha512-qvUtwJ3j6qwsF3jLxkZ72qCgjMysPzDfeV240JHiGZsANBYd+EEuu35v7dfrJ9Up0Ak07D7GGSkGhCHTqg/5wA==\n'
               '  dependencies:\n'
               '    node-fetch "^2.6.1"\n'
               '    whatwg-fetch "^3.4.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=336,
          lineno=1961,
          tokens=231,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'isstream@~0.1.2, isstream@0.1.x:\n'
               '  version "0.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/isstream/-/isstream-0.1.2.tgz"\n'
               '  integrity '
               'sha512-Yljz7ffyPbrLpLngrMtZ7NduUgVvi6wG9RJ9IUcyCd59YQ911PBJphODUcbOVbqYfxe1wuYf/LJ8PauMRwsM/g==\n'
               '\n'
               'jiti@^1.18.2:\n'
               '  version "1.19.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/jiti/-/jiti-1.19.1.tgz"\n'
               '  integrity '
               'sha512-oVhqoRDaBXf7sjkll95LHVS6Myyyb1zaunVwk4Z0+WPSW4gjS0pl01zYKHScTuyEhQsFxV5L4DR5r+YqSyqyyg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=337,
          lineno=1971,
          tokens=186,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'joi@^17.6.0:\n'
               '  version "17.9.2"\n'
               '  resolved "https://registry.npmjs.org/joi/-/joi-17.9.2.tgz"\n'
               '  integrity '
               'sha512-Itk/r+V4Dx0V3c7RLFdRh12IOjySm2/WGPMubBT92cQvRfYZhPM2W0hZlctjj72iES8jsRCwp7S/cRmWBnJ4nw==\n'
               '  dependencies:\n'
               '    "@hapi/hoek" "^9.0.0"\n'
               '    "@hapi/topo" "^5.0.0"\n'
               '    "@sideway/address" "^4.1.3"\n'
               '    "@sideway/formula" "^3.0.1"\n'
               '    "@sideway/pinpoint" "^2.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=338,
          lineno=1982,
          tokens=136,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'jose@^4.11.4, jose@^4.14.4, jose@^4.9.2:\n'
               '  version "4.14.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/jose/-/jose-4.14.4.tgz"\n'
               '  integrity '
               'sha512-j8GhLiKmUAh+dsFXlX1aJCbt5KMibuKb+d7j1JaOJG6s2UjX1PQlW+OKB/sD4a/5ZYF4RcmYmLSndOoU3Lt/3g==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=339,
          lineno=1987,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'js-sdsl@^4.1.4:\n'
               '  version "4.4.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/js-sdsl/-/js-sdsl-4.4.1.tgz"\n'
               '  integrity '
               'sha512-6Gsx8R0RucyePbWqPssR8DyfuXmLBooYN5cZFZKjHGnQuaf7pEzhtpceagJxVu4LqhYY5EYA7nko3FmeHZ1KbA==\n'
               '\n'
               '"js-tokens@^3.0.0 || ^4.0.0":\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz"\n'
               '  integrity '
               'sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=340,
          lineno=1997,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'js-yaml@^4.1.0:\n'
               '  version "4.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/js-yaml/-/js-yaml-4.1.0.tgz"\n'
               '  integrity '
               'sha512-wpxZs9NoxZaJESJGIZTyDEaYpl0FKSA+FB9aJiyemKhMwkxQg63h4T1KJgUGHpTqPDNRcmmYLugrRjJlBtWvRA==\n'
               '  dependencies:\n'
               '    argparse "^2.0.1"\n'
               '\n'
               'jsbn@~0.1.0:\n'
               '  version "0.1.1"\n'
               '  resolved "https://registry.npmjs.org/jsbn/-/jsbn-0.1.1.tgz"\n'
               '  integrity '
               'sha512-UVU9dibq2JcFWxQPA6KCqj5O42VOmAY3zQUfEKxU0KpTGXwNoCjkX1e13eHNvw/xPynt6pU0rZ1htjWTNTSXsg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=341,
          lineno=2009,
          tokens=225,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'json-schema-traverse@^0.4.1:\n'
               '  version "0.4.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz"\n'
               '  integrity '
               'sha512-xbbCH5dCYU5T8LcEhhuh7HJ88HXuW3qsI3Y0zOZFKfZEHcpWiHU/Jxzk629Brsab/mMiHQti9wMP+845RPe3Vg==\n'
               '\n'
               'json-schema@0.4.0:\n'
               '  version "0.4.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/json-schema/-/json-schema-0.4.0.tgz"\n'
               '  integrity '
               'sha512-es94M3nTIfsEPisRafak+HDLfHXnKBhV3vU5eqPcS3flIWqcxJWgXHXiey3YrpaNsanY5ei1VoYEbOzijuq9BA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=342,
          lineno=2019,
          tokens=133,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'json-stable-stringify-without-jsonify@^1.0.1:\n'
               '  version "1.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/json-stable-stringify-without-jsonify/-/json-stable-stringify-without-jsonify-1.0.1.tgz"\n'
               '  integrity '
               'sha512-Bdboy+l7tA3OGW6FjyFHWkP5LuByj1Tk33Ljyq0axyzdk9//JSi2u3fP1QSmd1KNwq6VOKYGlAu87CisVir6Pw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=343,
          lineno=2024,
          tokens=242,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'json-stringify-safe@~5.0.1:\n'
               '  version "5.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/json-stringify-safe/-/json-stringify-safe-5.0.1.tgz"\n'
               '  integrity '
               'sha512-ZClg6AaYvamvYEE82d3Iyd3vSSIjQ+odgjaTzRuO3s7toCdFKczob2i0zCh7JE8kWn17yvAWhUVxvqGwUalsRA==\n'
               '\n'
               'json5@^1.0.2:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/json5/-/json5-1.0.2.tgz"\n'
               '  integrity '
               'sha512-g1MWMLBiz8FKi1e4w0UyVL3w+iJceWAFBAaBnnGKOpNa5f8TLktkbre1+s6oICydWAm+HRUGTmI+//xv2hvXYA==\n'
               '  dependencies:\n'
               '    minimist "^1.2.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=344,
          lineno=2036,
          tokens=162,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'jsprim@^1.2.2:\n'
               '  version "1.4.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/jsprim/-/jsprim-1.4.2.tgz"\n'
               '  integrity '
               'sha512-P2bSOMAc/ciLz6DzgjVlGJP9+BrJWu5UDGK70C2iweC5QBIeFf0ZXRvGjEj2uYgrY2MkAAhsSWHDWlFtEroZWw==\n'
               '  dependencies:\n'
               '    assert-plus "1.0.0"\n'
               '    extsprintf "1.3.0"\n'
               '    json-schema "0.4.0"\n'
               '    verror "1.10.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=345,
          lineno=2046,
          tokens=182,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"jsx-ast-utils@^2.4.1 || ^3.0.0", jsx-ast-utils@^3.3.3:\n'
               '  version "3.3.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/jsx-ast-utils/-/jsx-ast-utils-3.3.4.tgz"\n'
               '  integrity '
               'sha512-fX2TVdCViod6HwKEtSWGHs57oFhVfCMwieb9PuRDgjDPh5XeqJiHFFFJCHxU5cnTc3Bu/GRL+kPiFmw8XWOfKw==\n'
               '  dependencies:\n'
               '    array-includes "^3.1.6"\n'
               '    array.prototype.flat "^1.3.1"\n'
               '    object.assign "^4.1.4"\n'
               '    object.values "^1.1.6"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=346,
          lineno=2056,
          tokens=249,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'language-subtag-registry@~0.3.2:\n'
               '  version "0.3.22"\n'
               '  resolved '
               '"https://registry.npmjs.org/language-subtag-registry/-/language-subtag-registry-0.3.22.tgz"\n'
               '  integrity '
               'sha512-tN0MCzyWnoz/4nHS6uxdlFWoUZT7ABptwKPQ52Ea7URk6vll88bWBVhodtnlfEuCcKWNGoc+uGbw1cwa9IKh/w==\n'
               '\n'
               'language-tags@=1.0.5:\n'
               '  version "1.0.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/language-tags/-/language-tags-1.0.5.tgz"\n'
               '  integrity '
               'sha512-qJhlO9cGXi6hBGKoxEG/sKZDAHD5Hnu9Hs4WbOY3pCWXDhw0N8x1NenNzm2EnNLkLkk7J2SdxAkDSbb6ftT+UQ==\n'
               '  dependencies:\n'
               '    language-subtag-registry "~0.3.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=347,
          lineno=2068,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'levn@^0.4.1:\n'
               '  version "0.4.1"\n'
               '  resolved "https://registry.npmjs.org/levn/-/levn-0.4.1.tgz"\n'
               '  integrity '
               'sha512-+bT2uH4E5LGE7h/n3evcS/sQlJXCpIp6ym8OWJ5eV6+67Dsql/LaaT7qJBAt2rzfoa/5QBGBhxDix1dMt2kQKQ==\n'
               '  dependencies:\n'
               '    prelude-ls "^1.2.1"\n'
               '    type-check "~0.4.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=348,
          lineno=2076,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'lilconfig@^2.0.5, lilconfig@^2.1.0:\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/lilconfig/-/lilconfig-2.1.0.tgz"\n'
               '  integrity '
               'sha512-utWOt/GHzuUxnLKxB6dk81RoOeoNeHgbrXiuGk4yyF5qlRz+iIVWu56E2fqGHFrXz0QNUhLB/8nKqvRH66JKGQ==\n'
               '\n'
               'lines-and-columns@^1.1.6:\n'
               '  version "1.2.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/lines-and-columns/-/lines-and-columns-1.2.4.tgz"\n'
               '  integrity '
               'sha512-7ylylesZQ/PV29jhEDl3Ufjo6ZX7gCqJr5F7PKrqc93v7fzSymt1BpwEU8nAUXs8qzzvqhbjhK5QZg6Mt/HkBg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=349,
          lineno=2086,
          tokens=242,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'locate-path@^6.0.0:\n'
               '  version "6.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/locate-path/-/locate-path-6.0.0.tgz"\n'
               '  integrity '
               'sha512-iPZK6eYjbxRu3uB4/WZ3EsEIMJFMqAoopl3R+zuq0UjcAm/MO6KCweDgPfP3elTztoKP3KtnVHxTn2NHBSDVUw==\n'
               '  dependencies:\n'
               '    p-locate "^5.0.0"\n'
               '\n'
               'lodash.defaults@^4.2.0:\n'
               '  version "4.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/lodash.defaults/-/lodash.defaults-4.2.0.tgz"\n'
               '  integrity '
               'sha512-qjxPLHd3r5DnsdGacqOMU6pb/avJzdh9tFX2ymgoZE27BmjXrNy/y4LoaiTeAb+O3gL8AfpJGtqfX/ae2leYYQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=350,
          lineno=2098,
          tokens=234,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'lodash.isarguments@^3.1.0:\n'
               '  version "3.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/lodash.isarguments/-/lodash.isarguments-3.1.0.tgz"\n'
               '  integrity '
               'sha512-chi4NHZlZqZD18a0imDHnZPrDeBbTtVN7GXMwuGdRH9qotxAjYs3aVLKc7zNOG9eddR5Ksd8rvFEBc9SsggPpg==\n'
               '\n'
               'lodash.merge@^4.6.2:\n'
               '  version "4.6.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/lodash.merge/-/lodash.merge-4.6.2.tgz"\n'
               '  integrity '
               'sha512-0KpjqXRVvrYyCsX1swR/XTK0va6VQkQM6MNo7PqW77ByjAhoARA8EfrP1N4+KlKj8YS0ZUCtRT/YUuhyYDujIQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=351,
          lineno=2108,
          tokens=112,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'lodash@^4.17.14:\n'
               '  version "4.17.21"\n'
               '  resolved '
               '"https://registry.npmjs.org/lodash/-/lodash-4.17.21.tgz"\n'
               '  integrity '
               'sha512-v2kDEe57lecTulaDIuNTPy3Ry4gLGJ6Z1O3vE1krgXZNrsQ+LFTGHVxVjcXPs17LhbZVGedAJv8XZ1tvj5FvSg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=352,
          lineno=2113,
          tokens=146,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'loose-envify@^1.1.0, loose-envify@^1.4.0:\n'
               '  version "1.4.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz"\n'
               '  integrity '
               'sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q==\n'
               '  dependencies:\n'
               '    js-tokens "^3.0.0 || ^4.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=353,
          lineno=2120,
          tokens=246,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'lru-cache@^6.0.0:\n'
               '  version "6.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/lru-cache/-/lru-cache-6.0.0.tgz"\n'
               '  integrity '
               'sha512-Jo6dJ04CmSjuznwJSS3pUeWmd/H0ffTlkXXgwZi+eq1UCmqQwCh+eLsYOYCwY991i2Fah4h1BEMCx4qThGbsiA==\n'
               '  dependencies:\n'
               '    yallist "^4.0.0"\n'
               '\n'
               'lucide-react@^0.129.0:\n'
               '  version "0.129.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/lucide-react/-/lucide-react-0.129.0.tgz"\n'
               '  integrity '
               'sha512-kGEZ+pOk9FLKsCr4luL4HYqr23lQdVbmN+3cgTj0Ye6s95FED3CX/DNzB3o8/TimgNmKKw+iq+g3mnTbtS7/ew==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=354,
          lineno=2132,
          tokens=239,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'merge-stream@^2.0.0:\n'
               '  version "2.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/merge-stream/-/merge-stream-2.0.0.tgz"\n'
               '  integrity '
               'sha512-abv/qOcuPfk3URPfDzmZU1LKmuw8kT+0nIHvKrKgFrwifol/doWcdA4ZqsWQ8ENrFKkd67Mfpo/LovbIUsbt3w==\n'
               '\n'
               'merge2@^1.3.0, merge2@^1.4.1:\n'
               '  version "1.4.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz"\n'
               '  integrity '
               'sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=355,
          lineno=2142,
          tokens=150,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'micromatch@^4.0.4, micromatch@^4.0.5:\n'
               '  version "4.0.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/micromatch/-/micromatch-4.0.5.tgz"\n'
               '  integrity '
               'sha512-DMy+ERcEW2q8Z2Po+WNXuw3c5YaUSFjAO5GsJqfEl7UjvtIuFKO6ZrKvcItdy98dwFI2N1tg3zNIdKaQT+aNdA==\n'
               '  dependencies:\n'
               '    braces "^3.0.2"\n'
               '    picomatch "^2.3.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=356,
          lineno=2150,
          tokens=115,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'mime-db@1.52.0:\n'
               '  version "1.52.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/mime-db/-/mime-db-1.52.0.tgz"\n'
               '  integrity '
               'sha512-sPU4uV7dYlvtWJxwwxHD0PuihVNiE7TyAbQ5SWxDCB9mUYvOgroQOwYQQOKPJ8CIbE+1ETVlOoK1UC2nU3gYvg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=357,
          lineno=2155,
          tokens=138,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'mime-types@^2.1.12, mime-types@~2.1.19:\n'
               '  version "2.1.35"\n'
               '  resolved '
               '"https://registry.npmjs.org/mime-types/-/mime-types-2.1.35.tgz"\n'
               '  integrity '
               'sha512-ZDY+bPm5zTTF+YpCrAU9nK0UgICYPT0QtT1NZWFv4s++TNkcgVaT0g6+4R2uI4MjQjzysHB1zxuWL50hzaeXiw==\n'
               '  dependencies:\n'
               '    mime-db "1.52.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=358,
          lineno=2162,
          tokens=245,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'mimic-fn@^2.1.0:\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/mimic-fn/-/mimic-fn-2.1.0.tgz"\n'
               '  integrity '
               'sha512-OqbOk5oEQeAZ8WXWydlu9HJjz9WVdEIvamMCcXmuqUYjTknH/sqsWvhQ3vgwKFRR1HpjvNBKQ37nbJgYzGqGcg==\n'
               '\n'
               'mimic-fn@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/mimic-fn/-/mimic-fn-4.0.0.tgz"\n'
               '  integrity '
               'sha512-vqiC06CuhBTUdZH+RYl8sFrL096vA45Ok5ISO6sE/Mr1jRbGH4Csnhi8f3wKVl7x8mO4Au7Ir9D3Oyv1VYMFJw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=359,
          lineno=2172,
          tokens=122,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'mini-svg-data-uri@^1.2.3:\n'
               '  version "1.4.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/mini-svg-data-uri/-/mini-svg-data-uri-1.4.4.tgz"\n'
               '  integrity '
               'sha512-r9deDe9p5FJUPZAk3A59wGH7Ii9YrjjWw0jmw/liSbHl2CHiyXj6FcDXDu2K3TjVAXqiJdaw3xxwlZZr9E6nHg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=360,
          lineno=2177,
          tokens=150,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'minimatch@^3.0.4, minimatch@^3.0.5, minimatch@^3.1.2:\n'
               '  version "3.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz"\n'
               '  integrity '
               'sha512-J7p63hRiAjw1NDEww1W7i37+ByIrOWO5XQQAzZ3VOcL0PNybwpfmV/N05zFAzwQ9USyEcX6t3UO+K5aqBQOIHw==\n'
               '  dependencies:\n'
               '    brace-expansion "^1.1.7"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=361,
          lineno=2184,
          tokens=128,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'minimatch@^5.0.1:\n'
               '  version "5.1.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/minimatch/-/minimatch-5.1.6.tgz"\n'
               '  integrity '
               'sha512-lKwV/1brpG6mBUFHtb7NUmtABCb2WZZmm2wNiOA5hAb8VdCS4B3dtMWyvcoViccwAW/COERjXLt0zP1zXUN26g==\n'
               '  dependencies:\n'
               '    brace-expansion "^2.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=362,
          lineno=2191,
          tokens=234,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'minimist@^1.2.0, minimist@^1.2.6:\n'
               '  version "1.2.8"\n'
               '  resolved '
               '"https://registry.npmjs.org/minimist/-/minimist-1.2.8.tgz"\n'
               '  integrity '
               'sha512-2yyAR8qBkN3YuheJanUpWC5U3bb5osDywNB8RzDVlDwDHbocAJveqqj1u8+SVD7jkWT4yvsHCpWqqWqAxb0zCA==\n'
               '\n'
               'mkdirp@^2.1.3:\n'
               '  version "2.1.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/mkdirp/-/mkdirp-2.1.6.tgz"\n'
               '  integrity '
               'sha512-+hEnITedc8LAtIP9u3HJDFIdcLV2vXP33sqLLIzkv1Db1zO/1OxbvYf0Y1OC/S/Qo5dxHXepofhmxL02PsKe+A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=363,
          lineno=2201,
          tokens=115,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'ms@^2.1.1, ms@2.1.2:\n'
               '  version "2.1.2"\n'
               '  resolved "https://registry.npmjs.org/ms/-/ms-2.1.2.tgz"\n'
               '  integrity '
               'sha512-sGkPx+VjMtmA6MX27oA4FBFELFCZZ4S4XqeGOXCv68tT+jb3vk/RyaKWP0PTKyWtmLSM0b+adUTEvbs1PEaH2w==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=364,
          lineno=2206,
          tokens=160,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'mz@^2.4.0, mz@^2.7.0:\n'
               '  version "2.7.0"\n'
               '  resolved "https://registry.npmjs.org/mz/-/mz-2.7.0.tgz"\n'
               '  integrity '
               'sha512-z81GNO7nnYMEhrGh9LeymoE4+Yr0Wn5McHIZMK5cfQCl+NDX08sCZgUc9/6MHni9IWuFLm1Z3HTCXu2z9fN62Q==\n'
               '  dependencies:\n'
               '    any-promise "^1.0.0"\n'
               '    object-assign "^4.0.1"\n'
               '    thenify-all "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=365,
          lineno=2215,
          tokens=220,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'nanoid@^3.3.4:\n'
               '  version "3.3.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/nanoid/-/nanoid-3.3.6.tgz"\n'
               '  integrity '
               'sha512-BGcqMMJuToF7i1rt+2PWSNVnWIkGCU78jBG3RxO/bZlnZPK2Cmi2QaffxGO/2RvWi9sL+FAiRiXMgsyxQ1DIDA==\n'
               '\n'
               'nanoid@^3.3.6:\n'
               '  version "3.3.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/nanoid/-/nanoid-3.3.6.tgz"\n'
               '  integrity '
               'sha512-BGcqMMJuToF7i1rt+2PWSNVnWIkGCU78jBG3RxO/bZlnZPK2Cmi2QaffxGO/2RvWi9sL+FAiRiXMgsyxQ1DIDA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=366,
          lineno=2225,
          tokens=229,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'nanoid@^4.0.2:\n'
               '  version "4.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/nanoid/-/nanoid-4.0.2.tgz"\n'
               '  integrity '
               'sha512-7ZtY5KTCNheRGfEFxnedV5zFiORN1+Y1N6zvPTnHQd8ENUvfaDBeuJDZb2bN/oXwXxu3qkTXDzy57W5vAmDTBw==\n'
               '\n'
               'natural-compare@^1.4.0:\n'
               '  version "1.4.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/natural-compare/-/natural-compare-1.4.0.tgz"\n'
               '  integrity '
               'sha512-OWND8ei3VtNC9h7V60qff3SVobHr996CTwgxubgyQYEpg290h9J0buyECNNJexkFm5sOajh5G116RYA1c8ZMSw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=367,
          lineno=2235,
          tokens=221,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'next-auth@^4, next-auth@^4.22.1:\n'
               '  version "4.22.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/next-auth/-/next-auth-4.22.1.tgz"\n'
               '  integrity '
               'sha512-NTR3f6W7/AWXKw8GSsgSyQcDW6jkslZLH8AiZa5PQ09w1kR8uHtR9rez/E9gAq/o17+p0JYHE8QjF3RoniiObA==\n'
               '  dependencies:\n'
               '    "@babel/runtime" "^7.20.13"\n'
               '    "@panva/hkdf" "^1.0.2"\n'
               '    cookie "^0.5.0"\n'
               '    jose "^4.11.4"\n'
               '    oauth "^0.9.15"\n'
               '    openid-client "^5.4.0"\n'
               '    preact "^10.6.3"\n'
               '    preact-render-to-string "^5.1.19"\n'
               '    uuid "^8.3.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=368,
          lineno=2250,
          tokens=198,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'next@*, "next@^12.2.5 || ^13", next@>=10, next@13.2.4:\n'
               '  version "13.2.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/next/-/next-13.2.4.tgz"\n'
               '  integrity '
               'sha512-g1I30317cThkEpvzfXujf0O4wtaQHtDCLhlivwlTJ885Ld+eOgcz7r3TGQzeU+cSRoNHtD8tsJgzxVdYojFssw==\n'
               '  dependencies:\n'
               '    "@next/env" "13.2.4"\n'
               '    "@swc/helpers" "0.4.14"\n'
               '    caniuse-lite "^1.0.30001406"\n'
               '    postcss "8.4.14"\n'
               '    styled-jsx "5.1.1"\n'
               '  optionalDependencies:\n'
               '    '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=369,
          lineno=2262,
          tokens=236,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"@next/swc-android-arm-eabi" "13.2.4"\n'
               '    "@next/swc-android-arm64" "13.2.4"\n'
               '    "@next/swc-darwin-arm64" "13.2.4"\n'
               '    "@next/swc-darwin-x64" "13.2.4"\n'
               '    "@next/swc-freebsd-x64" "13.2.4"\n'
               '    "@next/swc-linux-arm-gnueabihf" "13.2.4"\n'
               '    "@next/swc-linux-arm64-gnu" "13.2.4"\n'
               '    "@next/swc-linux-arm64-musl" "13.2.4"\n'
               '    "@next/swc-linux-x64-gnu" "13.2.4"\n'
               '    "@next/swc-linux-x64-musl" "13.2.4"\n'
               '    "@next/swc-win32-arm64-msvc" "13.2.4"\n'
               '    "@next/swc-win32-ia32-msvc" "13.2.4"\n'
               '    "@next/swc-win32-x64-msvc" "13.2.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=370,
          lineno=2275,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'node-fetch@^2.6.1:\n'
               '  version "2.6.12"\n'
               '  resolved '
               '"https://registry.npmjs.org/node-fetch/-/node-fetch-2.6.12.tgz"\n'
               '  integrity '
               'sha512-C/fGU2E8ToujUivIO0H+tpQ6HWo4eEmchoPIoXtxCrVghxdKq+QOHqEZW7tuP3KlV3bC8FRMO5nMCC7Zm1VP6g==\n'
               '  dependencies:\n'
               '    whatwg-url "^5.0.0"\n'
               '\n'
               'node-releases@^2.0.12:\n'
               '  version "2.0.13"\n'
               '  resolved '
               '"https://registry.npmjs.org/node-releases/-/node-releases-2.0.13.tgz"\n'
               '  integrity '
               'sha512-uYr7J37ae/ORWdZeQ1xxMJe3NtdmqMC/JZK+geofDrkLUApKRHPd18/TxtBOJ4A0/+uUIliorNrfYV6s1b02eQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=371,
          lineno=2287,
          tokens=237,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'normalize-path@^3.0.0, normalize-path@~3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz"\n'
               '  integrity '
               'sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA==\n'
               '\n'
               'normalize-range@^0.1.2:\n'
               '  version "0.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/normalize-range/-/normalize-range-0.1.2.tgz"\n'
               '  integrity '
               'sha512-bdok/XvKII3nUpklnV6P2hxtMNrCboOjAcyBuQnWEhO665FwrSNRxU+AqpsyvO6LgGYPspN+lu5CLtw4jPRKNA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=372,
          lineno=2297,
          tokens=126,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'npm-run-path@^4.0.1:\n'
               '  version "4.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/npm-run-path/-/npm-run-path-4.0.1.tgz"\n'
               '  integrity '
               'sha512-S48WzZW777zhNIrn7gxOlISNAqi9ZC/uQFnRdbeIHhZhCA6UqpkOT8T1G7BvfdgP4Er8gF4sUbaS0i7QvIfCWw==\n'
               '  dependencies:\n'
               '    path-key "^3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=373,
          lineno=2304,
          tokens=238,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'npm-run-path@^5.1.0:\n'
               '  version "5.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/npm-run-path/-/npm-run-path-5.1.0.tgz"\n'
               '  integrity '
               'sha512-sJOdmRGrY2sjNTRMbSvluQqg+8X7ZK61yvzBEIDhz4f8z1TZFYABsqjjCBd/0PUNE9M6QDgHJXQkGUEm7Q+l9Q==\n'
               '  dependencies:\n'
               '    path-key "^4.0.0"\n'
               '\n'
               'oauth-sign@~0.9.0:\n'
               '  version "0.9.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/oauth-sign/-/oauth-sign-0.9.0.tgz"\n'
               '  integrity '
               'sha512-fexhUFFPTGV8ybAtSIGbV6gOkSv8UtRbDBnAyLQw4QPKkgNlsH2ByPGtMUqdWkos6YCRmAqViwgZrJc/mRDzZQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=374,
          lineno=2316,
          tokens=241,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'oauth@^0.9.15:\n'
               '  version "0.9.15"\n'
               '  resolved '
               '"https://registry.npmjs.org/oauth/-/oauth-0.9.15.tgz"\n'
               '  integrity '
               'sha512-a5ERWK1kh38ExDEfoO6qUHJb32rd7aYmPHuyCu3Fta/cnICvYmgd2uhuKXvPD+PXB+gCEYYEaQdIRAjCOwAKNA==\n'
               '\n'
               'object-assign@^4.0.1, object-assign@^4.1.1:\n'
               '  version "4.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz"\n'
               '  integrity '
               'sha512-rJgTQnkUnH1sFw8yT6VSU3zD3sWmu6sZhIseY8VX+GRu3P6F7Fu+JNDoXfklElbLJSnc3FUQHVe4cU5hj+BcUg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=375,
          lineno=2326,
          tokens=223,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'object-hash@^2.2.0:\n'
               '  version "2.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/object-hash/-/object-hash-2.2.0.tgz"\n'
               '  integrity '
               'sha512-gScRMn0bS5fH+IuwyIFgnh9zBdo4DV+6GhygmWM9HyNJSgS0hScp1f5vjtm7oIIOiT9trXrShAkLFSc2IqKNgw==\n'
               '\n'
               'object-hash@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/object-hash/-/object-hash-3.0.0.tgz"\n'
               '  integrity '
               'sha512-RSn9F68PjH9HqtltsSnqYC1XXoWe9Bju5+213R98cNGttag9q9yAOTzdbsqvIa7aNm5WffBZFpWYr2aWrklWAw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=376,
          lineno=2336,
          tokens=241,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'object-inspect@^1.12.3, object-inspect@^1.9.0:\n'
               '  version "1.12.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/object-inspect/-/object-inspect-1.12.3.tgz"\n'
               '  integrity '
               'sha512-geUvdk7c+eizMNUDkRpW1wJwgfOiOeHbxBR/hLXK1aT6zmVSO0jsQcs7fj6MGw89jC/cjGfLcNOrtMYtGqm81g==\n'
               '\n'
               'object-keys@^1.1.1:\n'
               '  version "1.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/object-keys/-/object-keys-1.1.1.tgz"\n'
               '  integrity '
               'sha512-NuAESUOUMrlIXOfHKzD6bpPu3tYt3xvjNdRIQ+FeT0lNb4K8WR70CaDxhuNguS2XG+GjkyMwOzsN5ZktImfhLA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=377,
          lineno=2346,
          tokens=154,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'object.assign@^4.1.4:\n'
               '  version "4.1.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/object.assign/-/object.assign-4.1.4.tgz"\n'
               '  integrity '
               'sha512-1mxKf0e58bvyjSCtKYY4sRe9itRk3PJpquJOjeIkz885CczcI4IvJJDLPS72oowuSh+pBxUFROpX+TU++hxhZQ==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    has-symbols "^1.0.3"\n'
               '    object-keys "^1.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=378,
          lineno=2356,
          tokens=148,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'object.entries@^1.1.6:\n'
               '  version "1.1.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/object.entries/-/object.entries-1.1.6.tgz"\n'
               '  integrity '
               'sha512-leTPzo4Zvg3pmbQ3rDK69Rl8GQvIqMWubrkxONG9/ojtFE2rD9fjMKfSI5BxW3osRH1m6VdzmqK8oAY9aT4x5w==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=379,
          lineno=2365,
          tokens=149,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'object.fromentries@^2.0.6:\n'
               '  version "2.0.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/object.fromentries/-/object.fromentries-2.0.6.tgz"\n'
               '  integrity '
               'sha512-VciD13dswC4j1Xt5394WR4MzmAQmlgN72phd/riNp9vtD7tp4QQWJ0R4wvclXcafgcYK8veHRed2W6XeGBvcfg==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=380,
          lineno=2374,
          tokens=142,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'object.hasown@^1.1.2:\n'
               '  version "1.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/object.hasown/-/object.hasown-1.1.2.tgz"\n'
               '  integrity '
               'sha512-B5UIT3J1W+WuWIU55h0mjlwaqxiE5vYENJXIXZ4VFe05pNYrkKuK0U/6aFcb0pKywYJh7IhfoqUfKVmrJJHZHw==\n'
               '  dependencies:\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=381,
          lineno=2382,
          tokens=146,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'object.values@^1.1.6:\n'
               '  version "1.1.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/object.values/-/object.values-1.1.6.tgz"\n'
               '  integrity '
               'sha512-FVVTkD1vENCsAcwNs9k6jea2uHC/X0+JcjG8YA60FN5CMaJmG95wT9jek/xX9nornqGRrBkKtzuAu2wuHpKqvw==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=382,
          lineno=2391,
          tokens=237,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'oidc-token-hash@^5.0.3:\n'
               '  version "5.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/oidc-token-hash/-/oidc-token-hash-5.0.3.tgz"\n'
               '  integrity '
               'sha512-IF4PcGgzAr6XXSff26Sk/+P4KZFJVuHAJZj3wgO3vX2bMdNVp/QXTP3P7CEm9V1IdG8lDLY3HhiqpsE/nOwpPw==\n'
               '\n'
               'once@^1.3.0:\n'
               '  version "1.4.0"\n'
               '  resolved "https://registry.npmjs.org/once/-/once-1.4.0.tgz"\n'
               '  integrity '
               'sha512-lNaJgI+2Q5URQBkccEKHTQOPaXdUxnZZElQTZY0MFUAuaEqe1E+Nyvgdz/aIyNi6Z9MzO5dv1H8n58/GELp3+w==\n'
               '  dependencies:\n'
               '    wrappy "1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=383,
          lineno=2403,
          tokens=130,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'onetime@^5.1.2:\n'
               '  version "5.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/onetime/-/onetime-5.1.2.tgz"\n'
               '  integrity '
               'sha512-kbpaSSGJTWdAY5KPVeMOKXSrPtr8C8C7wodJbcsd51jRnmD+GZu8Y0VoU6Dm5Z4vWr0Ig/1NKuWRKf7j5aaYSg==\n'
               '  dependencies:\n'
               '    mimic-fn "^2.1.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=384,
          lineno=2410,
          tokens=127,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'onetime@^6.0.0:\n'
               '  version "6.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/onetime/-/onetime-6.0.0.tgz"\n'
               '  integrity '
               'sha512-1FlR+gjXK7X+AsAHso35MnyN5KqGwJRi/31ft6x0M194ht7S+rWAvd7PHss9xSKMzE0asv1pyIHaJYq+BbacAQ==\n'
               '  dependencies:\n'
               '    mimic-fn "^4.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=385,
          lineno=2417,
          tokens=160,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'open@^9.1.0:\n'
               '  version "9.1.0"\n'
               '  resolved "https://registry.npmjs.org/open/-/open-9.1.0.tgz"\n'
               '  integrity '
               'sha512-OS+QTnw1/4vrf+9hh1jc1jnYjzSG4ttTBB8UxOwAnInG3Uo4ssetzC1ihqaIHjLJnA5GGlRl6QlZXOTQhRBUvg==\n'
               '  dependencies:\n'
               '    default-browser "^4.0.0"\n'
               '    define-lazy-prop "^3.0.0"\n'
               '    is-inside-container "^1.0.0"\n'
               '    is-wsl "^2.2.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=386,
          lineno=2427,
          tokens=168,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'openid-client@^5.2.1, openid-client@^5.4.0:\n'
               '  version "5.4.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/openid-client/-/openid-client-5.4.3.tgz"\n'
               '  integrity '
               'sha512-sVQOvjsT/sbSfYsQI/9liWQGVZH/Pp3rrtlGEwgk/bbHfrUDZ24DN57lAagIwFtuEu+FM9Ev7r85s8S/yPjimQ==\n'
               '  dependencies:\n'
               '    jose "^4.14.4"\n'
               '    lru-cache "^6.0.0"\n'
               '    object-hash "^2.2.0"\n'
               '    oidc-token-hash "^5.0.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=387,
          lineno=2437,
          tokens=112,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'openssl@^2.0.0:\n'
               '  version "2.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/openssl/-/openssl-2.0.0.tgz"\n'
               '  integrity '
               'sha512-0FgKhQ/e+XCtTTgn3qZO2g3y+Y3FC/LGvt77oObmMR4ZkZvsV1CuG/mMZClZgZqVKr0+tkemP+I3Uub4WXkHYw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=388,
          lineno=2442,
          tokens=186,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'optionator@^0.9.1:\n'
               '  version "0.9.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/optionator/-/optionator-0.9.3.tgz"\n'
               '  integrity '
               'sha512-JjCoypp+jKn1ttEFExxhetCKeJt9zhAgAve5FXHixTvFDW/5aEktX9bufBKLRRMdU7bNtpLfcGu94B3cdEJgjg==\n'
               '  dependencies:\n'
               '    "@aashutoshrathi/word-wrap" "^1.2.3"\n'
               '    deep-is "^0.1.3"\n'
               '    fast-levenshtein "^2.0.6"\n'
               '    levn "^0.4.1"\n'
               '    prelude-ls "^1.2.1"\n'
               '    type-check "^0.4.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=389,
          lineno=2454,
          tokens=127,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'p-limit@^3.0.2:\n'
               '  version "3.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/p-limit/-/p-limit-3.1.0.tgz"\n'
               '  integrity '
               'sha512-TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==\n'
               '  dependencies:\n'
               '    yocto-queue "^0.1.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=390,
          lineno=2461,
          tokens=249,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'p-locate@^5.0.0:\n'
               '  version "5.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/p-locate/-/p-locate-5.0.0.tgz"\n'
               '  integrity '
               'sha512-LaNjtRWUBY++zB5nE/NwcaoMylSPk+S+ZHNB1TzdbMJMny6dynpAGt7X/tl/QYq3TIeE6nxHppbo2LGymrG5Pw==\n'
               '  dependencies:\n'
               '    p-limit "^3.0.2"\n'
               '\n'
               'parent-module@^1.0.0:\n'
               '  version "1.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/parent-module/-/parent-module-1.0.1.tgz"\n'
               '  integrity '
               'sha512-GQ2EWRpQV8/o+Aw8YqtfZZPfNRWZYkbidE9k5rpl/hC3vtHHBfGm2Ifi6qWV+coDGkrUKZAxE3Lot5kcsRlh+g==\n'
               '  dependencies:\n'
               '    callsites "^3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=391,
          lineno=2475,
          tokens=142,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'parse5-htmlparser2-tree-adapter@^6.0.0:\n'
               '  version "6.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/parse5-htmlparser2-tree-adapter/-/parse5-htmlparser2-tree-adapter-6.0.1.tgz"\n'
               '  integrity '
               'sha512-qPuWvbLgvDGilKc5BoicRovlT4MtYT6JfJyBOMDsKoiT+GiuP5qyrPCnR9HcPECIJJmZh5jRndyNThnhhb/vlA==\n'
               '  dependencies:\n'
               '    parse5 "^6.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=392,
          lineno=2482,
          tokens=227,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'parse5@^5.1.1:\n'
               '  version "5.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/parse5/-/parse5-5.1.1.tgz"\n'
               '  integrity '
               'sha512-ugq4DFI0Ptb+WWjAdOK16+u/nHfiIrcE+sh8kZMaM0WllQKLI9rOUq6c2b7cwPkXdzfQESqvoqK6ug7U/Yyzug==\n'
               '\n'
               'parse5@^6.0.1:\n'
               '  version "6.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/parse5/-/parse5-6.0.1.tgz"\n'
               '  integrity '
               'sha512-Ofn/CTFzRGTTxwpNEs9PP93gXShHcTq255nzRYSKe8AkVpZY7e1fpmTfOyoIvjP5HG7Z2ZM7VS9PPhQGW2pOpw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=393,
          lineno=2492,
          tokens=239,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'path-exists@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz"\n'
               '  integrity '
               'sha512-ak9Qy5Q7jYb2Wwcey5Fpvg2KoAc/ZIhLSLOSBmRmygPsGwkVVt0fZa0qrtMz+m6tJTAHfZQ8FnmB4MG4LWy7/w==\n'
               '\n'
               'path-is-absolute@^1.0.0:\n'
               '  version "1.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/path-is-absolute/-/path-is-absolute-1.0.1.tgz"\n'
               '  integrity '
               'sha512-AVbw3UJ2e9bq64vSaS9Am0fje1Pa8pbGqTTsmXfaIiMpnr5DlDhfJOuLj9Sf95ZPVDAUerDfEk88MPmPe7UCQg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=394,
          lineno=2502,
          tokens=236,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'path-key@^3.0.0, path-key@^3.1.0:\n'
               '  version "3.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz"\n'
               '  integrity '
               'sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==\n'
               '\n'
               'path-key@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/path-key/-/path-key-4.0.0.tgz"\n'
               '  integrity '
               'sha512-haREypq7xkM7ErfgIyA0z+Bj4AGKlMSdlQE2jvJo6huWD1EdkKYV+G/T4nq0YEF2vgTT8kqMFKo1uHn950r4SQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=395,
          lineno=2512,
          tokens=224,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'path-parse@^1.0.7:\n'
               '  version "1.0.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz"\n'
               '  integrity '
               'sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw==\n'
               '\n'
               'path-type@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/path-type/-/path-type-4.0.0.tgz"\n'
               '  integrity '
               'sha512-gDKb8aZMDeD/tZWs9P6+q0J9Mwkdl6xMV8TjnGP3qJVJ06bdMgkbBlLU8IdfOsIsFz2BW1rNVT3XuNEl8zPAvw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=396,
          lineno=2522,
          tokens=221,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'performance-now@^2.1.0:\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/performance-now/-/performance-now-2.1.0.tgz"\n'
               '  integrity '
               'sha512-7EAHlyLHI56VEIdK57uwHdHKIaAGbnXPiw0yWbarQZOKaKpvUIgW0jWRVLiatnM+XXlSwsanIBH/hzGMJulMow==\n'
               '\n'
               'picocolors@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/picocolors/-/picocolors-1.0.0.tgz"\n'
               '  integrity '
               'sha512-1fygroTLlHu66zi26VoTDv8yRgm0Fccecssto+MhsZ0D/DGW2sm8E8AjW7NU5VVTRt5GxbeZ5qBuJr+HyLYkjQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=397,
          lineno=2532,
          tokens=139,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'picomatch@^2.0.4, picomatch@^2.2.1, picomatch@^2.3.1:\n'
               '  version "2.3.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz"\n'
               '  integrity '
               'sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=398,
          lineno=2537,
          tokens=229,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'pify@^2.3.0:\n'
               '  version "2.3.0"\n'
               '  resolved "https://registry.npmjs.org/pify/-/pify-2.3.0.tgz"\n'
               '  integrity '
               'sha512-udgsAY+fTnvv7kI7aaxbqwWNb0AHiB0qBO89PZKPkoTmGOgdbrHDKD+0B2X4uTfJ/FT1R09r9gTsjUjNJotuog==\n'
               '\n'
               'pirates@^4.0.1:\n'
               '  version "4.0.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/pirates/-/pirates-4.0.6.tgz"\n'
               '  integrity '
               'sha512-saLsH7WeYYPiD25LDuLRRY/i+6HaPYr6G1OUlN39otzkSTxKnubR9RTxS3/Kk50s1g2JTgFwWQDQyplC5/SHZg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=399,
          lineno=2547,
          tokens=151,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'postcss-import@^15.1.0:\n'
               '  version "15.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/postcss-import/-/postcss-import-15.1.0.tgz"\n'
               '  integrity '
               'sha512-hpr+J05B2FVYUAXHeK1YyI267J/dDDhMU6B6civm8hSY1jYJnBXxzKDKDswzJmtLHryrjhnDjqqp/49t8FALew==\n'
               '  dependencies:\n'
               '    postcss-value-parser "^4.0.0"\n'
               '    read-cache "^1.0.0"\n'
               '    resolve "^1.1.7"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=400,
          lineno=2556,
          tokens=121,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'postcss-js@^4.0.1:\n'
               '  version "4.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/postcss-js/-/postcss-js-4.0.1.tgz"\n'
               '  integrity '
               'sha512-dDLF8pEO191hJMtlHFPRa8xsizHaM82MLfNkUHdUtVEV3tgTp5oj+8qbEqYM57SLfc74KSbw//4SeJma2LRVIw==\n'
               '  dependencies:\n'
               '    camelcase-css "^2.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=401,
          lineno=2563,
          tokens=139,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'postcss-load-config@^4.0.1:\n'
               '  version "4.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/postcss-load-config/-/postcss-load-config-4.0.1.tgz"\n'
               '  integrity '
               'sha512-vEJIc8RdiBRu3oRAI0ymerOn+7rPuMvRXslTvZUKZonDHFIczxztIyJ1urxM1x9JXEikvpWWTUUqal5j/8QgvA==\n'
               '  dependencies:\n'
               '    lilconfig "^2.0.5"\n'
               '    yaml "^2.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=402,
          lineno=2571,
          tokens=138,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'postcss-nested@^6.0.1:\n'
               '  version "6.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/postcss-nested/-/postcss-nested-6.0.1.tgz"\n'
               '  integrity '
               'sha512-mEp4xPMi5bSWiMbsgoPfcP74lsWLHkQbZc3sY+jWYd65CUwXrUaTp0fmNpa01ZcETKlIgUdFN/MpS2xZtqL9dQ==\n'
               '  dependencies:\n'
               '    postcss-selector-parser "^6.0.11"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=403,
          lineno=2578,
          tokens=146,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'postcss-selector-parser@^6.0.11:\n'
               '  version "6.0.13"\n'
               '  resolved '
               '"https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-6.0.13.tgz"\n'
               '  integrity '
               'sha512-EaV1Gl4mUEV4ddhDnv/xtj7sxwrwxdetHdWUGnT4VJQf+4d05v6lHYZr8N573k5Z0BViss7BDhfWtKS3+sfAqQ==\n'
               '  dependencies:\n'
               '    cssesc "^3.0.0"\n'
               '    util-deprecate "^1.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=404,
          lineno=2586,
          tokens=133,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'postcss-value-parser@^4.0.0, postcss-value-parser@^4.2.0:\n'
               '  version "4.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz"\n'
               '  integrity '
               'sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=405,
          lineno=2591,
          tokens=215,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'postcss@^8.0.0, postcss@^8.1.0, postcss@^8.2.14, '
               'postcss@^8.4.21, postcss@^8.4.23, postcss@^8.4.25, '
               'postcss@>=8.0.9:\n'
               '  version "8.4.25"\n'
               '  resolved '
               '"https://registry.npmjs.org/postcss/-/postcss-8.4.25.tgz"\n'
               '  integrity '
               'sha512-7taJ/8t2av0Z+sQEvNzCkpDynl0tX3uJMCODi6nT3PfASC7dYCWV9aQ+uiCf+KBD4SEFcu+GvJdGdwzQ6OSjCw==\n'
               '  dependencies:\n'
               '    nanoid "^3.3.6"\n'
               '    picocolors "^1.0.0"\n'
               '    source-map-js "^1.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=406,
          lineno=2600,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'postcss@8.4.14:\n'
               '  version "8.4.14"\n'
               '  resolved '
               '"https://registry.npmjs.org/postcss/-/postcss-8.4.14.tgz"\n'
               '  integrity '
               'sha512-E398TUmfAYFPBSdzgeieK2Y1+1cpdxJx8yXbK/m57nRhKSmk1GB2tO4lbLBtlkfPQTDKfe4Xqv1ASWPpayPEig==\n'
               '  dependencies:\n'
               '    nanoid "^3.3.4"\n'
               '    picocolors "^1.0.0"\n'
               '    source-map-js "^1.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=407,
          lineno=2609,
          tokens=246,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'preact-render-to-string@^5.1.19:\n'
               '  version "5.2.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/preact-render-to-string/-/preact-render-to-string-5.2.6.tgz"\n'
               '  integrity '
               'sha512-JyhErpYOvBV1hEPwIxc/fHWXPfnEGdRKxc8gFdAZ7XV4tlzyzG847XAyEZqoDnynP88akM4eaHcSOzNcLWFguw==\n'
               '  dependencies:\n'
               '    pretty-format "^3.8.0"\n'
               '\n'
               'preact@^10.6.3, preact@>=10:\n'
               '  version "10.15.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/preact/-/preact-10.15.1.tgz"\n'
               '  integrity '
               'sha512-qs2ansoQEwzNiV5eAcRT1p1EC/dmEzaATVDJNiB3g2sRDWdA7b7MurXdJjB2+/WQktGWZwxvDrnuRFbWuIr64g==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=408,
          lineno=2621,
          tokens=228,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'prelude-ls@^1.2.1:\n'
               '  version "1.2.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/prelude-ls/-/prelude-ls-1.2.1.tgz"\n'
               '  integrity '
               'sha512-vkcDPrRZo1QZLbn5RLGPpg/WmIQ65qoWWhcGKf/b5eplkkarX0m9z8ppCat4mlOqUsWpyNuYgO3VRyrYHSzX5g==\n'
               '\n'
               'pretty-format@^3.8.0:\n'
               '  version "3.8.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/pretty-format/-/pretty-format-3.8.0.tgz"\n'
               '  integrity '
               'sha512-WuxUnVtlWL1OfZFQFuqvnvs6MiAGk9UNsBostyBOB0Is9wb5uRESevA6rnl/rkksXaGX3GzZhPup5d6Vp1nFew==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=409,
          lineno=2631,
          tokens=147,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'prop-types@^15.8.1:\n'
               '  version "15.8.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/prop-types/-/prop-types-15.8.1.tgz"\n'
               '  integrity '
               'sha512-oj87CgZICdulUohogVAR7AjlC0327U4el4L6eAvOqCeudMDVU0NThNaV+b9Df4dXgSP1gXMTnPdhfe/2qDH5cg==\n'
               '  dependencies:\n'
               '    loose-envify "^1.4.0"\n'
               '    object-assign "^4.1.1"\n'
               '    react-is "^16.13.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=410,
          lineno=2640,
          tokens=223,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'proxy-from-env@^1.1.0:\n'
               '  version "1.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/proxy-from-env/-/proxy-from-env-1.1.0.tgz"\n'
               '  integrity '
               'sha512-D+zkORCbA9f1tdWRK0RaCR3GPv50cMxcrz4X8k5LTSUD1Dkw47mKJEZQNunItRTkWwgtaUSo1RVFRIG9ZXiFYg==\n'
               '\n'
               'psl@^1.1.28:\n'
               '  version "1.9.0"\n'
               '  resolved "https://registry.npmjs.org/psl/-/psl-1.9.0.tgz"\n'
               '  integrity '
               'sha512-E/ZsdU4HLs/68gYzgGTkMicWTLPdAftJLfJFlLUAAKZGkStNU72sZjT66SnMDVOfOWY/YAoiD7Jxa9iHvngcag==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=411,
          lineno=2650,
          tokens=128,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'punycode@^2.1.0, punycode@^2.1.1:\n'
               '  version "2.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/punycode/-/punycode-2.3.0.tgz"\n'
               '  integrity '
               'sha512-rRV+zQD8tVFys26lAGR9WUuS4iUAngJScM+ZRSKtvl5tKeZ2t5bvdNFdNHBW9FWR4guGHlgmsZ1G7BSm2wTbuA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=412,
          lineno=2655,
          tokens=135,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'pusher-js@^8.0.2:\n'
               '  version "8.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/pusher-js/-/pusher-js-8.2.0.tgz"\n'
               '  integrity '
               'sha512-t3WhhR7vgAr5ARl0VNiAqXOb7g4hyW7CNA9Q11tnlcn8dX+1bFZhgRP6IqWVzTX9n7fgjcji3UQ3y8FEMc1o7Q==\n'
               '  dependencies:\n'
               '    tweetnacl "^1.0.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=413,
          lineno=2662,
          tokens=184,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'pusher@^5.1.3:\n'
               '  version "5.1.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/pusher/-/pusher-5.1.3.tgz"\n'
               '  integrity '
               'sha512-Bmy5guFxQsbYSFLF3CM7GA2qE1zDJYn51PnNme9QlSjGguvkqUg4nj31PbgiLVDFK2sJvxPfx4JrB2HLgM3kaw==\n'
               '  dependencies:\n'
               '    "@types/node-fetch" "^2.5.7"\n'
               '    abort-controller "^3.0.0"\n'
               '    is-base64 "^1.1.0"\n'
               '    node-fetch "^2.6.1"\n'
               '    tweetnacl "^1.0.0"\n'
               '    tweetnacl-util "^0.15.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=414,
          lineno=2674,
          tokens=237,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'qs@~6.5.2:\n'
               '  version "6.5.3"\n'
               '  resolved "https://registry.npmjs.org/qs/-/qs-6.5.3.tgz"\n'
               '  integrity '
               'sha512-qxXIEh4pCGfHICj1mAJQ2/2XVZkjCDTcEgfoSQxc/fYivUZxTkk7L3bDBJSoNrEzXI17oUO5Dp07ktqE5KzczA==\n'
               '\n'
               'queue-microtask@^1.2.2:\n'
               '  version "1.2.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz"\n'
               '  integrity '
               'sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=415,
          lineno=2684,
          tokens=174,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"react-dom@^16 || ^17 || ^18", "react-dom@^17.0.2 || ^18", '
               'react-dom@^18.2.0, react-dom@>=16, react-dom@18.2.0:\n'
               '  version "18.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/react-dom/-/react-dom-18.2.0.tgz"\n'
               '  integrity '
               'sha512-6IMTriUmvsjHUjNtEDudZfuDQUoWXVxKHhlEGSk81n4YFS+r/Kl99wXiwlVXtPBtJenozv2P+hxDsw9eA7Xo6g==\n'
               '  dependencies:\n'
               '    loose-envify "^1.1.0"\n'
               '    scheduler "^0.23.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=416,
          lineno=2692,
          tokens=124,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'react-hook-form@^7.0.0, react-hook-form@^7.43.9:\n'
               '  version "7.45.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/react-hook-form/-/react-hook-form-7.45.1.tgz"\n'
               '  integrity '
               'sha512-6dWoFJwycbuFfw/iKMcl+RdAOAOHDiF11KWYhNDRN/OkUt+Di5qsZHwA0OwsVnu9y135gkHpTw9DJA+WzCeR9w==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=417,
          lineno=2697,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'react-hot-toast@^2.4.0:\n'
               '  version "2.4.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/react-hot-toast/-/react-hot-toast-2.4.1.tgz"\n'
               '  integrity '
               'sha512-j8z+cQbWIM5LY37pR6uZR6D4LfseplqnuAO4co4u8917hBUvXlEqyP1ZzqVLcqoyUesZZv/ImreoCeHVDpE5pQ==\n'
               '  dependencies:\n'
               '    goober "^2.1.10"\n'
               '\n'
               'react-is@^16.13.1:\n'
               '  version "16.13.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/react-is/-/react-is-16.13.1.tgz"\n'
               '  integrity '
               'sha512-24e6ynE2H+OKt4kqsOvNd8kBpV65zoxbA4BVsEOB3ARVWQki/DHzaUoC5KuON/BiccDaCCTZBuOcfZs70kR8bQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=418,
          lineno=2709,
          tokens=117,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'react-loading-skeleton@^3.2.0:\n'
               '  version "3.3.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/react-loading-skeleton/-/react-loading-skeleton-3.3.1.tgz"\n'
               '  integrity '
               'sha512-NilqqwMh2v9omN7LteiDloEVpFyMIa0VGqF+ukqp0ncVlYu1sKYbYGX9JEl+GtOT9TKsh04zCHAbavnQ2USldA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=419,
          lineno=2714,
          tokens=159,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'react-textarea-autosize@^8.4.1:\n'
               '  version "8.5.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/react-textarea-autosize/-/react-textarea-autosize-8.5.2.tgz"\n'
               '  integrity '
               'sha512-uOkyjkEl0ByEK21eCJMHDGBAAd/BoFQBawYK5XItjAmCTeSbjxghd8qnt7nzsLYzidjnoObu6M26xts0YGKsGg==\n'
               '  dependencies:\n'
               '    "@babel/runtime" "^7.20.13"\n'
               '    use-composed-ref "^1.3.0"\n'
               '    use-latest "^1.2.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=420,
          lineno=2723,
          tokens=147,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"react@^16 || ^17 || ^18", "react@^16.5.1 || ^17.0.0 || '
               '^18.0.0", "react@^16.8.0 || ^17 || ^18", "react@^16.8.0 || '
               '^17.0.0 || ^18.0.0", "react@^17.0.2 || ^18", react@^18.2.0, '
               '"react@>= 16.8.0 || 17.x.x || ^18.0.0-0", react@>=16, '
               'react@>=16.8.0, react@18.2.0:\n'
               '  '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=421,
          lineno=2725,
          tokens=116,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='version "18.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/react/-/react-18.2.0.tgz"\n'
               '  integrity '
               'sha512-/3IjMdb2L9QbBdWiW5e3P2/npwMBaU9mHCSCUzNln0ZCYbcfTsGbTJrU/kGemdH2IWmB2ioZ+zkxtmq6g09fGQ==\n'
               '  dependencies:\n'
               '    loose-envify "^1.1.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=422,
          lineno=2730,
          tokens=249,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'read-cache@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/read-cache/-/read-cache-1.0.0.tgz"\n'
               '  integrity '
               'sha512-Owdv/Ft7IjOgm/i0xvNDZ1LrRANRfew4b2prF3OWMQLxLfu3bS8FVhCsrSCMK4lR56Y9ya+AThoTpDCTxCmpRA==\n'
               '  dependencies:\n'
               '    pify "^2.3.0"\n'
               '\n'
               'readdirp@~3.6.0:\n'
               '  version "3.6.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/readdirp/-/readdirp-3.6.0.tgz"\n'
               '  integrity '
               'sha512-hOS089on8RduqdbhvQ5Z37A0ESjsqz6qnRcffsMU3495FuTdqSm+7bhJ29JvIOsBDEEnan5DPu9t3To9VRlMzA==\n'
               '  dependencies:\n'
               '    picomatch "^2.2.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=423,
          lineno=2744,
          tokens=128,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'redis-errors@^1.0.0, redis-errors@^1.2.0:\n'
               '  version "1.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/redis-errors/-/redis-errors-1.2.0.tgz"\n'
               '  integrity '
               'sha512-1qny3OExCf0UvUV/5wpYKf2YwPcOqXzkwKKSmKHiE6ZMQs5heeE/c8eXK+PNllPvmjgAbfnsbpkGZWy8cBpn9w==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=424,
          lineno=2749,
          tokens=231,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'redis-parser@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/redis-parser/-/redis-parser-3.0.0.tgz"\n'
               '  integrity '
               'sha512-DJnGAeenTdpMEH6uAJRK/uiyEIH9WVsUmoLwzudwGJUwZPp80PDBWPHXSAGNPwNvIXAbe7MSUB1zQFugFml66A==\n'
               '  dependencies:\n'
               '    redis-errors "^1.0.0"\n'
               '\n'
               'reflect-metadata@^0.1.13:\n'
               '  version "0.1.13"\n'
               '  resolved '
               '"https://registry.npmjs.org/reflect-metadata/-/reflect-metadata-0.1.13.tgz"\n'
               '  integrity '
               'sha512-Ts1Y/anZELhSsjMcU605fU9RE4Oi3p5ORujwbIKXfWa+0Zxs510Qrmrce5/Jowq3cHSZSJqBjypxmHarc+vEWg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=425,
          lineno=2761,
          tokens=115,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'regenerator-runtime@^0.13.11:\n'
               '  version "0.13.11"\n'
               '  resolved '
               '"https://registry.npmjs.org/regenerator-runtime/-/regenerator-runtime-0.13.11.tgz"\n'
               '  integrity '
               'sha512-kY1AZVr2Ra+t+piVaJ4gxaFaReZVH40AKNo7UCX6W+dEwBo/2oZJzqfuN1qLq1oL45o56cPaTXELwrTh8Fpggg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=426,
          lineno=2766,
          tokens=158,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'regexp.prototype.flags@^1.4.3:\n'
               '  version "1.5.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/regexp.prototype.flags/-/regexp.prototype.flags-1.5.0.tgz"\n'
               '  integrity '
               'sha512-0SutC3pNudRKgquxGoRGIz946MZVHqbNfPjBdxeOhBrdgDKlRoXmYLQN9xRbrR09ZXWeGAdPuif7egofn6v5LA==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.2.0"\n'
               '    functions-have-names "^1.2.3"\n'
               '\n'
               'request@^2.88.0:\n'
               '  '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=427,
          lineno=2777,
          tokens=103,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='version "2.88.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/request/-/request-2.88.2.tgz"\n'
               '  integrity '
               'sha512-MsvtOrfG9ZcrOwAW+Qi+F6HbD0CWXEh9ou77uOb7FM2WPhwT7smM833PzanhJLsgXjN89Ir6V2PczXNnMpwKhw==\n'
               '  dependencies:\n'
               '    '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=428,
          lineno=2781,
          tokens=202,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='aws-sign2 "~0.7.0"\n'
               '    aws4 "^1.8.0"\n'
               '    caseless "~0.12.0"\n'
               '    combined-stream "~1.0.6"\n'
               '    extend "~3.0.2"\n'
               '    forever-agent "~0.6.1"\n'
               '    form-data "~2.3.2"\n'
               '    har-validator "~5.1.3"\n'
               '    http-signature "~1.2.0"\n'
               '    is-typedarray "~1.0.0"\n'
               '    isstream "~0.1.2"\n'
               '    json-stringify-safe "~5.0.1"\n'
               '    mime-types "~2.1.19"\n'
               '    oauth-sign "~0.9.0"\n'
               '    performance-now "^2.1.0"\n'
               '    qs "~6.5.2"\n'
               '    safe-buffer "^5.1.2"\n'
               '    tough-cookie "~2.5.0"\n'
               '    tunnel-agent "^0.6.0"\n'
               '    uuid "^3.3.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=429,
          lineno=2801,
          tokens=225,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'require-directory@^2.1.1:\n'
               '  version "2.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/require-directory/-/require-directory-2.1.1.tgz"\n'
               '  integrity '
               'sha512-fGxEI7+wsG9xrvdjsrlmL22OMTTiHRwAMroiEeMgq8gzoLC/PQr7RsRDSTLUg/bZAZtF+TVIkHc6/4RIKrui+Q==\n'
               '\n'
               'resolve-from@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/resolve-from/-/resolve-from-4.0.0.tgz"\n'
               '  integrity '
               'sha512-pb/MYmXstAkysRFx8piNI1tGFNQIFA3vkE3Gq4EuA1dF6gHp/+vgZqsCGJapvy8N3Q+4o7FwvquPJcnZ7RYy4g==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=430,
          lineno=2811,
          tokens=123,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'resolve-pkg-maps@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/resolve-pkg-maps/-/resolve-pkg-maps-1.0.0.tgz"\n'
               '  integrity '
               'sha512-seS2Tj26TBVOC2NIc2rOe2y2ZO7efxITtLZcGSOnHHNOQ7CkiUBfw0Iw2ck6xkIhPwLhKNLS8BO+hEpngQlqzw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=431,
          lineno=2816,
          tokens=163,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'resolve@^1.1.7, resolve@^1.22.1, resolve@^1.22.2:\n'
               '  version "1.22.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/resolve/-/resolve-1.22.2.tgz"\n'
               '  integrity '
               'sha512-Sb+mjNHOULsBv818T40qSPeRiuWLyaGMa5ewydRLFimneixmVy2zdivRl+AF6jaYPC8ERxGDmFSiqui6SfPd+g==\n'
               '  dependencies:\n'
               '    is-core-module "^2.11.0"\n'
               '    path-parse "^1.0.7"\n'
               '    supports-preserve-symlinks-flag "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=432,
          lineno=2825,
          tokens=157,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'resolve@^2.0.0-next.4:\n'
               '  version "2.0.0-next.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/resolve/-/resolve-2.0.0-next.4.tgz"\n'
               '  integrity '
               'sha512-iMDbmAWtfU+MHpxt/I5iWI7cY6YVEZUQ3MBgPQ++XD1PELuJHIl82xBmObyP2KyQmkNB2dsqF7seoQQiAn5yDQ==\n'
               '  dependencies:\n'
               '    is-core-module "^2.9.0"\n'
               '    path-parse "^1.0.7"\n'
               '    supports-preserve-symlinks-flag "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=433,
          lineno=2834,
          tokens=244,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'reusify@^1.0.4:\n'
               '  version "1.0.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/reusify/-/reusify-1.0.4.tgz"\n'
               '  integrity '
               'sha512-U9nH88a3fc/ekCF1l0/UP1IosiuIjyTh7hBvXVMHYgVcfGvt897Xguj2UOLDeI5BG2m7/uwyaLVT6fbtCwTyzw==\n'
               '\n'
               'rimraf@^3.0.2:\n'
               '  version "3.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/rimraf/-/rimraf-3.0.2.tgz"\n'
               '  integrity '
               'sha512-JZkJMZkAGFFPP2YqXZXPbMlMBgsxzE8ILs4lMIX/2o0L9UBw9O/Y3o6wFw/i9YLapcUJWwqbi3kdxIPdC62TIA==\n'
               '  dependencies:\n'
               '    glob "^7.1.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=434,
          lineno=2846,
          tokens=129,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'run-applescript@^5.0.0:\n'
               '  version "5.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/run-applescript/-/run-applescript-5.0.0.tgz"\n'
               '  integrity '
               'sha512-XcT5rBksx1QdIhlFOCtgZkB99ZEouFZ1E2Kc2LHqNW13U3/74YGdkQRmThTwxy4QIyookibDKYZOPqX//6BlAg==\n'
               '  dependencies:\n'
               '    execa "^5.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=435,
          lineno=2853,
          tokens=249,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'run-parallel@^1.1.9:\n'
               '  version "1.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz"\n'
               '  integrity '
               'sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==\n'
               '  dependencies:\n'
               '    queue-microtask "^1.2.2"\n'
               '\n'
               'safe-buffer@^5.0.1, safe-buffer@^5.1.2:\n'
               '  version "5.2.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/safe-buffer/-/safe-buffer-5.2.1.tgz"\n'
               '  integrity '
               'sha512-rp3So07KcdmmKbGvgaNxQSJr7bGVSVk5S9Eq1F+ppbRo70+YeaDxkw5Dd8NPN+GD6bjnYm2VuPuCXmpuYvmCXQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=436,
          lineno=2865,
          tokens=153,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'safe-regex-test@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/safe-regex-test/-/safe-regex-test-1.0.0.tgz"\n'
               '  integrity '
               'sha512-JBUUzyOgEwXQY1NuPtvcj/qcBDbDmEvWufhlnXZIm75DEHp+afM1r1ujJpJsV/gSM4t59tpDyPi1sd6ZaPFfsA==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    get-intrinsic "^1.1.3"\n'
               '    is-regex "^1.1.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=437,
          lineno=2874,
          tokens=158,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'safer-buffer@^2.0.2, safer-buffer@^2.1.0, "safer-buffer@>= '
               '2.1.2 < 3.0.0", safer-buffer@~2.1.0:\n'
               '  version "2.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/safer-buffer/-/safer-buffer-2.1.2.tgz"\n'
               '  integrity '
               'sha512-YZo3K82SD7Riyi0E1EQPojLz7kpepnSQI9IyPbHHg1XXXevb5dJI7tpyN2ADxGcQbHG7vcyRHk0cbwqcQriUtg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=438,
          lineno=2879,
          tokens=237,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'scheduler@^0.23.0:\n'
               '  version "0.23.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/scheduler/-/scheduler-0.23.0.tgz"\n'
               '  integrity '
               'sha512-CtuThmgHNg7zIZWAXi3AsyIzA3n4xx7aNyjwC2VJldO2LMVDhFK+63xGqq6CsJH4rTAt6/M+N4GhZiDYPx9eUw==\n'
               '  dependencies:\n'
               '    loose-envify "^1.1.0"\n'
               '\n'
               'semver@^6.3.0:\n'
               '  version "6.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/semver/-/semver-6.3.0.tgz"\n'
               '  integrity '
               'sha512-b39TBaTSfV6yBrapU89p5fKekE2m/NwnDocOVruQFS1/veMgdzuPcnOM34M6CwxW8jH/lxEa5rBoDeUwu5HHTw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=439,
          lineno=2891,
          tokens=242,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'semver@^7.3.7:\n'
               '  version "7.5.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/semver/-/semver-7.5.4.tgz"\n'
               '  integrity '
               'sha512-1bCSESV6Pv+i21Hvpxp3Dx+pSD8lIPt8uVjRrxAUt/nbswYc+tK6Y2btiULjd4+fnq15PX+nqQDC7Oft7WkwcA==\n'
               '  dependencies:\n'
               '    lru-cache "^6.0.0"\n'
               '\n'
               'setprototypeof@1.2.0:\n'
               '  version "1.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/setprototypeof/-/setprototypeof-1.2.0.tgz"\n'
               '  integrity '
               'sha512-E5LDX7Wrp85Kil5bhZv46j8jOeboKq5JMmYM3gVGdGH8xFpPWXUMsNrlODCrkoxMEeNi/XZIwuRvY4XNwYMJpw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=440,
          lineno=2903,
          tokens=137,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'sha.js@^2.4.11:\n'
               '  version "2.4.11"\n'
               '  resolved '
               '"https://registry.npmjs.org/sha.js/-/sha.js-2.4.11.tgz"\n'
               '  integrity '
               'sha512-QMEp5B7cftE7APOjk5Y6xgrbWu+WkLVQwk8JNjZ8nKRciZaByEW6MubieAiToS7+dwvrjGhH8jRXz3MVd0AYqQ==\n'
               '  dependencies:\n'
               '    inherits "^2.0.1"\n'
               '    safe-buffer "^5.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=441,
          lineno=2911,
          tokens=134,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'shebang-command@^2.0.0:\n'
               '  version "2.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz"\n'
               '  integrity '
               'sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==\n'
               '  dependencies:\n'
               '    shebang-regex "^3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=442,
          lineno=2918,
          tokens=118,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'shebang-regex@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz"\n'
               '  integrity '
               'sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=443,
          lineno=2923,
          tokens=148,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'side-channel@^1.0.4:\n'
               '  version "1.0.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/side-channel/-/side-channel-1.0.4.tgz"\n'
               '  integrity '
               'sha512-q5XPytqFEIKHkGdiMIrY10mvLRvnQh42/+GoBlFW3b2LXLE2xxJpZFdm94we0BaoV3RwJyGqg5wS7epxTv0Zvw==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.0"\n'
               '    get-intrinsic "^1.0.2"\n'
               '    object-inspect "^1.9.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=444,
          lineno=2932,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'signal-exit@^3.0.3, signal-exit@^3.0.7:\n'
               '  version "3.0.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/signal-exit/-/signal-exit-3.0.7.tgz"\n'
               '  integrity '
               'sha512-wnD2ZE+l+SPC/uoS0vXeE9L1+0wuaMqKlfz9AMUo38JsyLSBWSFcHR1Rri62LZc12vLr1gb3jl7iwQhgwpAbGQ==\n'
               '\n'
               'slash@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/slash/-/slash-3.0.0.tgz"\n'
               '  integrity '
               'sha512-g9Q1haeby36OSStwb4ntCGGGaKsaVSjQ68fBxoQcutl5fS1vuY18H3wSt3jFyFtrkx+Kz0V1G85A4MyAdDMi2Q==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=445,
          lineno=2942,
          tokens=111,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'slash@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/slash/-/slash-4.0.0.tgz"\n'
               '  integrity '
               'sha512-3dOsAHXXUkQTpOYcoAxLIorMTp4gIQr5IW3iVb7A7lFIp0VHhnynm9izx6TssdrIcVIESAlVjtnO2K8bg+Coew==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=446,
          lineno=2947,
          tokens=167,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'smartsheet@^3.1.2:\n'
               '  version "3.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/smartsheet/-/smartsheet-3.1.2.tgz"\n'
               '  integrity '
               'sha512-/k2QFWNFhebsx3EzLX3cKZiTg2RrKcaPlMf20irndlzZJJ63uHP6fO1+lDRb3jYUoe1aK8NkjyOiHXG4zuwYSQ==\n'
               '  dependencies:\n'
               '    bluebird "^3.5.0"\n'
               '    extend "^3.0.2"\n'
               '    request "^2.88.0"\n'
               '    underscore "^1.8.2"\n'
               '    winston "^2.3.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=447,
          lineno=2958,
          tokens=116,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'source-map-js@^1.0.2:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/source-map-js/-/source-map-js-1.0.2.tgz"\n'
               '  integrity '
               'sha512-R0XvVJ9WusLiqTCEiGCmICCMplcCkIwwR11mOSD9CR5u+IXYdiseeEuXCVAjS54zqwkLcPNnmU4OeJ6tUrWhDw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=448,
          lineno=2963,
          tokens=218,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'sshpk@^1.7.0:\n'
               '  version "1.17.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/sshpk/-/sshpk-1.17.0.tgz"\n'
               '  integrity '
               'sha512-/9HIEs1ZXGhSPE8X6Ccm7Nam1z8KcoCqPdI7ecm1N33EzAetWahvQWVqLZtaZQ+IDKX4IyA2o0gBzqIMkAagHQ==\n'
               '  dependencies:\n'
               '    asn1 "~0.2.3"\n'
               '    assert-plus "^1.0.0"\n'
               '    bcrypt-pbkdf "^1.0.0"\n'
               '    dashdash "^1.12.0"\n'
               '    ecc-jsbn "~0.1.1"\n'
               '    getpass "^0.1.1"\n'
               '    jsbn "~0.1.0"\n'
               '    safer-buffer "^2.0.2"\n'
               '    tweetnacl "~0.14.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=449,
          lineno=2978,
          tokens=231,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'stack-trace@0.0.x:\n'
               '  version "0.0.10"\n'
               '  resolved '
               '"https://registry.npmjs.org/stack-trace/-/stack-trace-0.0.10.tgz"\n'
               '  integrity '
               'sha512-KGzahc7puUKkzyMt+IqAep+TVNbKP+k2Lmwhub39m1AsTSkaDutx56aDCo+HLDzf/D26BIHTJWNiTG1KAJiQCg==\n'
               '\n'
               'standard-as-callback@^2.1.0:\n'
               '  version "2.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/standard-as-callback/-/standard-as-callback-2.1.0.tgz"\n'
               '  integrity '
               'sha512-qoRRSyROncaz1z0mvYqIE4lCd9p2R90i6GxW3uZv5ucSu8tU7B5HXUP1gG8pVZsYNVaXjk8ClXHPttLyxAL48A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=450,
          lineno=2988,
          tokens=115,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"statuses@>= 1.5.0 < 2":\n'
               '  version "1.5.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/statuses/-/statuses-1.5.0.tgz"\n'
               '  integrity '
               'sha512-OpZ3zP+jT1PI7I8nemJX4AKmAX070ZkYPVWV/AaKTJl+tXCTGyVdC1a4SL8RUQYEwk/f34ZX8UTykN68FwrqAA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=451,
          lineno=2993,
          tokens=168,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'string-width@^4.1.0, string-width@^4.2.0, '
               'string-width@^4.2.3:\n'
               '  version "4.2.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz"\n'
               '  integrity '
               'sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==\n'
               '  dependencies:\n'
               '    emoji-regex "^8.0.0"\n'
               '    is-fullwidth-code-point "^3.0.0"\n'
               '    strip-ansi "^6.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=452,
          lineno=3002,
          tokens=207,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'string.prototype.matchall@^4.0.8:\n'
               '  version "4.0.8"\n'
               '  resolved '
               '"https://registry.npmjs.org/string.prototype.matchall/-/string.prototype.matchall-4.0.8.tgz"\n'
               '  integrity '
               'sha512-6zOCOcJ+RJAQshcTvXPHoxoQGONa3e/Lqx90wUA+wEzX78sg5Bo+1tQo4N0pohS0erG9qtCqJDjNCQBjeWVxyg==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'
               '    get-intrinsic "^1.1.3"\n'
               '    has-symbols "^1.0.3"\n'
               '    internal-slot "^1.0.3"\n'
               '    regexp.prototype.flags "^1.4.3"\n'
               '    side-channel "^1.0.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=453,
          lineno=3016,
          tokens=152,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'string.prototype.trim@^1.2.7:\n'
               '  version "1.2.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/string.prototype.trim/-/string.prototype.trim-1.2.7.tgz"\n'
               '  integrity '
               'sha512-p6TmeT1T3411M8Cgg9wBTMRtY2q9+PNy9EV1i2lIXUN/btt763oIfxwN3RR8VU6wHX8j/1CFy0L+YuThm6bgOg==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=454,
          lineno=3025,
          tokens=149,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'string.prototype.trimend@^1.0.6:\n'
               '  version "1.0.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/string.prototype.trimend/-/string.prototype.trimend-1.0.6.tgz"\n'
               '  integrity '
               'sha512-JySq+4mrPf9EsDBEDYMOb/lM7XQLulwg5R/m1r0PXEFqrV0qHvl58sdTilSXtKOflCsK2E8jxf+GKC0T07RWwQ==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=455,
          lineno=3034,
          tokens=152,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'string.prototype.trimstart@^1.0.6:\n'
               '  version "1.0.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/string.prototype.trimstart/-/string.prototype.trimstart-1.0.6.tgz"\n'
               '  integrity '
               'sha512-omqjMDaY92pbn5HOX7f9IccLA+U1tA9GvtU4JrodiXFfYB7jPzzHpRzpglLAjtUV6bB557zwClJezTqnAiYnQA==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    define-properties "^1.1.4"\n'
               '    es-abstract "^1.20.4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=456,
          lineno=3043,
          tokens=140,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'strip-ansi@^6.0.0, strip-ansi@^6.0.1:\n'
               '  version "6.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz"\n'
               '  integrity '
               'sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==\n'
               '  dependencies:\n'
               '    ansi-regex "^5.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=457,
          lineno=3050,
          tokens=236,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'strip-bom@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/strip-bom/-/strip-bom-3.0.0.tgz"\n'
               '  integrity '
               'sha512-vavAMRXOgBVNF6nyEEmL3DBK19iRpDcoIwW+swQ+CbGiu7lju6t+JklA1MHweoWtadgt4ISVUsXLyDq34ddcwA==\n'
               '\n'
               'strip-final-newline@^2.0.0:\n'
               '  version "2.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/strip-final-newline/-/strip-final-newline-2.0.0.tgz"\n'
               '  integrity '
               'sha512-BrpvfNAE3dcvq7ll3xVumzjKjZQ5tI1sEUIKr3Uoks0XUl45St3FlatVqef9prk4jRDzhW6WZg+3bk93y6pLjA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=458,
          lineno=3060,
          tokens=121,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'strip-final-newline@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/strip-final-newline/-/strip-final-newline-3.0.0.tgz"\n'
               '  integrity '
               'sha512-dOESqjYr96iWYylGObzd39EuNTa5VJxyvVAEm5Jnh7KGo75V43Hk1odPQkNDyXNmUR6k+gEiDVXnjB8HJ3crXw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=459,
          lineno=3065,
          tokens=132,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'strip-json-comments@^3.1.0, strip-json-comments@^3.1.1:\n'
               '  version "3.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/strip-json-comments/-/strip-json-comments-3.1.1.tgz"\n'
               '  integrity '
               'sha512-6fPc+R4ihwqP6N/aIv2f1gMH8lOVtWQHoqC4yK6oSDVVocumAsfCqjkXnqiYMhmMwS/mEHLp7Vehlt3ql6lEig==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=460,
          lineno=3070,
          tokens=134,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'styled-jsx@5.1.1:\n'
               '  version "5.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/styled-jsx/-/styled-jsx-5.1.1.tgz"\n'
               '  integrity '
               'sha512-pW7uC1l4mBZ8ugbiZrcIsiIvVx1UmTfw7UkC3Um2tmfUq9Bhk8IiyEIPl6F8agHgjzku6j0xQEZbfA5uSgSaCw==\n'
               '  dependencies:\n'
               '    client-only "0.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=461,
          lineno=3077,
          tokens=194,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'sucrase@^3.32.0:\n'
               '  version "3.32.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/sucrase/-/sucrase-3.32.0.tgz"\n'
               '  integrity '
               'sha512-ydQOU34rpSyj2TGyz4D2p8rbktIOZ8QY9s+DGLvFU1i5pWJE8vkpruCjGCMHsdXwnD7JDcS+noSwM/a7zyNFDQ==\n'
               '  dependencies:\n'
               '    "@jridgewell/gen-mapping" "^0.3.2"\n'
               '    commander "^4.0.0"\n'
               '    glob "7.1.6"\n'
               '    lines-and-columns "^1.1.6"\n'
               '    mz "^2.7.0"\n'
               '    pirates "^4.0.1"\n'
               '    ts-interface-checker "^0.1.9"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=462,
          lineno=3090,
          tokens=126,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'supports-color@^7.1.0:\n'
               '  version "7.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/supports-color/-/supports-color-7.2.0.tgz"\n'
               '  integrity '
               'sha512-qpCAvRl9stuOHveKsn7HncJRvv501qIacKzQlO/+Lwxc9+0q2wLyv4Dfvt80/DPn2pqOBsJdDiogXGR9+OvwRw==\n'
               '  dependencies:\n'
               '    has-flag "^4.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=463,
          lineno=3097,
          tokens=135,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'supports-preserve-symlinks-flag@^1.0.0:\n'
               '  version "1.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz"\n'
               '  integrity '
               'sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=464,
          lineno=3102,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'synckit@^0.8.5:\n'
               '  version "0.8.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/synckit/-/synckit-0.8.5.tgz"\n'
               '  integrity '
               'sha512-L1dapNV6vu2s/4Sputv8xGsCdAVlb5nRDMFU/E27D44l5U6cw1g0dGd45uLc+OXjNMmF4ntiMdCimzcjFKQI8Q==\n'
               '  dependencies:\n'
               '    "@pkgr/utils" "^2.3.1"\n'
               '    tslib "^2.5.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=465,
          lineno=3110,
          tokens=158,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'tailwind-merge@^1.11.0:\n'
               '  version "1.13.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/tailwind-merge/-/tailwind-merge-1.13.2.tgz"\n'
               '  integrity '
               'sha512-R2/nULkdg1VR/EL4RXg4dEohdoxNUJGLMnWIQnPKL+O9Twu7Cn3Rxi4dlXkDzZrEGtR+G+psSXFouWlpTyLhCQ==\n'
               '\n'
               'tailwindcss@^3.3.2, "tailwindcss@>=3.0.0 || >= '
               '3.0.0-alpha.1":\n'
               '  '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=466,
          lineno=3117,
          tokens=107,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='version "3.3.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/tailwindcss/-/tailwindcss-3.3.2.tgz"\n'
               '  integrity '
               'sha512-9jPkMiIBXvPc2KywkraqsUfbfj+dHDb+JPWtSJa9MLFdrPyazI7q6WX2sUrm7R9eVR7qqv3Pas7EvQFzxKnI6w==\n'
               '  dependencies:\n'
               '    '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=467,
          lineno=3121,
          tokens=250,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"@alloc/quick-lru" "^5.2.0"\n'
               '    arg "^5.0.2"\n'
               '    chokidar "^3.5.3"\n'
               '    didyoumean "^1.2.2"\n'
               '    dlv "^1.1.3"\n'
               '    fast-glob "^3.2.12"\n'
               '    glob-parent "^6.0.2"\n'
               '    is-glob "^4.0.3"\n'
               '    jiti "^1.18.2"\n'
               '    lilconfig "^2.1.0"\n'
               '    micromatch "^4.0.5"\n'
               '    normalize-path "^3.0.0"\n'
               '    object-hash "^3.0.0"\n'
               '    picocolors "^1.0.0"\n'
               '    postcss "^8.4.23"\n'
               '    postcss-import "^15.1.0"\n'
               '    postcss-js "^4.0.1"\n'
               '    postcss-load-config "^4.0.1"\n'
               '    postcss-nested "^6.0.1"\n'
               '    postcss-selector-parser "^6.0.11"\n'
               '    postcss-value-parser "^4.2.0"\n'
               '    resolve "^1.22.2"\n'
               '    sucrase "^3.32.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=468,
          lineno=3144,
          tokens=228,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'tapable@^2.2.0:\n'
               '  version "2.2.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/tapable/-/tapable-2.2.1.tgz"\n'
               '  integrity '
               'sha512-GNzQvQTOIP6RyTfE2Qxb8ZVlNmw0n88vp1szwWRimP02mnTsx3Wtn5qRdqY9w2XduFNUgvOwhNnQsjwCp+kqaQ==\n'
               '\n'
               'text-table@^0.2.0:\n'
               '  version "0.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/text-table/-/text-table-0.2.0.tgz"\n'
               '  integrity '
               'sha512-N+8UisAXDGk8PFXP4HAzVR9nbfmVJ3zYLAWiTIoqC5v5isinhr+r5uaO8+7r3BMfuNIufIsA7RdpVgacC2cSpw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=469,
          lineno=3154,
          tokens=137,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'thenify-all@^1.0.0:\n'
               '  version "1.6.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/thenify-all/-/thenify-all-1.6.0.tgz"\n'
               '  integrity '
               'sha512-RNxQH/qI8/t3thXJDwcstUO4zeqo64+Uy/+sNVRBx4Xn2OX+OZ9oP+iJnNFqplFra2ZUVeKCSa2oVWi3T4uVmA==\n'
               '  dependencies:\n'
               '    thenify ">= 3.1.0 < 4"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=470,
          lineno=3161,
          tokens=246,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"thenify@>= 3.1.0 < 4":\n'
               '  version "3.3.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/thenify/-/thenify-3.3.1.tgz"\n'
               '  integrity '
               'sha512-RVZSIV5IG10Hk3enotrhvz0T9em6cyHBLkH/YAZuKqd8hRkKhSfCGIcP2KUY0EPxndzANBmNllzWPwak+bheSw==\n'
               '  dependencies:\n'
               '    any-promise "^1.0.0"\n'
               '\n'
               'titleize@^3.0.0:\n'
               '  version "3.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/titleize/-/titleize-3.0.0.tgz"\n'
               '  integrity '
               'sha512-KxVu8EYHDPBdUYdKZdKtU2aj2XfEx9AfjXxE/Aj0vT06w2icA09Vus1rh6eSu1y01akYg6BjIK/hxyLJINoMLQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=471,
          lineno=3173,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'to-regex-range@^5.0.1:\n'
               '  version "5.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz"\n'
               '  integrity '
               'sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==\n'
               '  dependencies:\n'
               '    is-number "^7.0.0"\n'
               '\n'
               'toidentifier@1.0.1:\n'
               '  version "1.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/toidentifier/-/toidentifier-1.0.1.tgz"\n'
               '  integrity '
               'sha512-o5sSPKEkg/DIQNmH43V0/uerLrpzVedkUh8tGNvaeXpfpuwjKenlSox/2O/BTlZUtEe+JG7s5YhEz608PlAHRA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=472,
          lineno=3185,
          tokens=141,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'tough-cookie@~2.5.0:\n'
               '  version "2.5.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/tough-cookie/-/tough-cookie-2.5.0.tgz"\n'
               '  integrity '
               'sha512-nlLsUzgm1kfLXSXfRZMc1KLAugd4hqJHDTvc2hDIwS3mZAfMEuMbc03SujMF+GEcpaX/qboeycw6iO8JwVv2+g==\n'
               '  dependencies:\n'
               '    psl "^1.1.28"\n'
               '    punycode "^2.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=473,
          lineno=3193,
          tokens=230,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'tr46@~0.0.3:\n'
               '  version "0.0.3"\n'
               '  resolved "https://registry.npmjs.org/tr46/-/tr46-0.0.3.tgz"\n'
               '  integrity '
               'sha512-N3WMsuqV66lT30CrXNbEjx4GEwlow3v6rr4mCcv6prnfwhS01rkgyFdjPNBYd9br7LpXV1+Emh01fHnq2Gdgrw==\n'
               '\n'
               'ts-interface-checker@^0.1.9:\n'
               '  version "0.1.13"\n'
               '  resolved '
               '"https://registry.npmjs.org/ts-interface-checker/-/ts-interface-checker-0.1.13.tgz"\n'
               '  integrity '
               'sha512-Y/arvbn+rrz3JCKl9C4kVNfTfSm2/mEp5FSz5EsZSANGPSlQrpRI5M4PKF+mJnE52jOO90PnPSc3Ur3bTQw0gA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=474,
          lineno=3203,
          tokens=166,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'tsconfig-paths@^3.14.1:\n'
               '  version "3.14.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/tsconfig-paths/-/tsconfig-paths-3.14.2.tgz"\n'
               '  integrity '
               'sha512-o/9iXgCYc5L/JxCHPe3Hvh8Q/2xm5Z+p18PESBU6Ff33695QnCHBEjcytY2q19ua7Mbl/DavtBOLq+oG0RCL+g==\n'
               '  dependencies:\n'
               '    "@types/json5" "^0.0.29"\n'
               '    json5 "^1.0.2"\n'
               '    minimist "^1.2.6"\n'
               '    strip-bom "^3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=475,
          lineno=3213,
          tokens=242,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'tslib@^1.8.1:\n'
               '  version "1.14.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/tslib/-/tslib-1.14.1.tgz"\n'
               '  integrity '
               'sha512-Xni35NKzjgMrwevysHTCArtLDpPvye8zV/0E4EyYn43P7/7qvQwPh9BGkHewbMulVntbigmcT7rdX3BNo9wRJg==\n'
               '\n'
               'tslib@^2.4.0, tslib@^2.5.0, tslib@^2.6.0:\n'
               '  version "2.6.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/tslib/-/tslib-2.6.0.tgz"\n'
               '  integrity '
               'sha512-7At1WUettjcSRHXCyYtTselblcHl9PJFFVKiCAy/bY97+BPZXSQ2wbq0P9s8tK2G7dFQfNnlJnPAiArVBVBsfA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=476,
          lineno=3223,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'tsutils@^3.21.0:\n'
               '  version "3.21.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/tsutils/-/tsutils-3.21.0.tgz"\n'
               '  integrity '
               'sha512-mHKK3iUXL+3UF6xL5k0PEhKRUBKPBCv/+RkEOpjRWxxx27KKRBmmA60A9pgOUvMi8GKhRMPEmjBRPzs2W7O1OA==\n'
               '  dependencies:\n'
               '    tslib "^1.8.1"\n'
               '\n'
               'tunnel-agent@^0.6.0:\n'
               '  version "0.6.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/tunnel-agent/-/tunnel-agent-0.6.0.tgz"\n'
               '  integrity '
               'sha512-McnNiV1l8RYeY8tBgEpuodCC1mLUdbSN+CYBL7kJsJNInOP8UjDDEwdk6Mw60vdLLrr5NHKZhMAOSrR2NZuQ+w==\n'
               '  dependencies:\n'
               '    safe-buffer "^5.0.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=477,
          lineno=3237,
          tokens=233,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'tweetnacl-util@^0.15.0:\n'
               '  version "0.15.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/tweetnacl-util/-/tweetnacl-util-0.15.1.tgz"\n'
               '  integrity '
               'sha512-RKJBIj8lySrShN4w6i/BonWp2Z/uxwC3h4y7xsRrpP59ZboCd0GpEVsOnMDYLMmKBpYhb5TgHzZXy7wTfYFBRw==\n'
               '\n'
               'tweetnacl@^0.14.3:\n'
               '  version "0.14.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz"\n'
               '  integrity '
               'sha512-KXXFFdAbFXY4geFIwoyNK+f5Z1b7swfXABfL7HXCmoIWMKU3dmS26672A4EeQtDzLKy7SXmfBu51JolvEKwtGA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=478,
          lineno=3247,
          tokens=241,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'tweetnacl@^1.0.0, tweetnacl@^1.0.3:\n'
               '  version "1.0.3"\n'
               '  resolved '
               '"https://registry.npmjs.org/tweetnacl/-/tweetnacl-1.0.3.tgz"\n'
               '  integrity '
               'sha512-6rt+RN7aOi1nGMyC4Xa5DdYiukl2UWCbcJft7YhxReBGQD7OAM8Pbxw6YMo4r2diNEA8FEmu32YOn9rhaiE5yw==\n'
               '\n'
               'tweetnacl@~0.14.0:\n'
               '  version "0.14.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/tweetnacl/-/tweetnacl-0.14.5.tgz"\n'
               '  integrity '
               'sha512-KXXFFdAbFXY4geFIwoyNK+f5Z1b7swfXABfL7HXCmoIWMKU3dmS26672A4EeQtDzLKy7SXmfBu51JolvEKwtGA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=479,
          lineno=3257,
          tokens=135,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'type-check@^0.4.0, type-check@~0.4.0:\n'
               '  version "0.4.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/type-check/-/type-check-0.4.0.tgz"\n'
               '  integrity '
               'sha512-XleUoc9uwGXqjWwXaUTZAmzMcFZ5858QA2vvx1Ur5xIcixXIP+8LnFDgRplU30us6teqdlskFfu+ae4K79Ooew==\n'
               '  dependencies:\n'
               '    prelude-ls "^1.2.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=480,
          lineno=3264,
          tokens=119,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'type-fest@^0.20.2:\n'
               '  version "0.20.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/type-fest/-/type-fest-0.20.2.tgz"\n'
               '  integrity '
               'sha512-Ne+eE4r0/iWnpAxD852z3A+N0Bt5RN//NjJwRd2VFHEmrywxf5vsZlh4R6lixl6B+wz/8d+maTSAkN1FIkI3LQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=481,
          lineno=3269,
          tokens=169,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'typed-array-length@^1.0.4:\n'
               '  version "1.0.4"\n'
               '  resolved '
               '"https://registry.npmjs.org/typed-array-length/-/typed-array-length-1.0.4.tgz"\n'
               '  integrity '
               'sha512-KjZypGq+I/H7HI5HlOoGHkWUUGq+Q0TPhQurLbyrVrvnKTBgzLhIJ7j6J/XTQOi0d1RjyZ0wdas8bKs2p0x3Ng==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    for-each "^0.3.3"\n'
               '    is-typed-array "^1.1.9"\n'
               '\n'
               'typeorm@^0.3.17:\n'
               '  '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=482,
          lineno=3280,
          tokens=104,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='version "0.3.17"\n'
               '  resolved '
               '"https://registry.npmjs.org/typeorm/-/typeorm-0.3.17.tgz"\n'
               '  integrity '
               'sha512-UDjUEwIQalO9tWw9O2A4GU+sT3oyoUXheHJy4ft+RFdnRdQctdQ34L9SqE2p7LdwzafHx1maxT+bqXON+Qnmig==\n'
               '  dependencies:\n'
               '    '),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=483,
          lineno=3284,
          tokens=148,
          depth=2,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='"@sqltools/formatter" "^1.2.5"\n'
               '    app-root-path "^3.1.0"\n'
               '    buffer "^6.0.3"\n'
               '    chalk "^4.1.2"\n'
               '    cli-highlight "^2.1.11"\n'
               '    date-fns "^2.29.3"\n'
               '    debug "^4.3.4"\n'
               '    dotenv "^16.0.3"\n'
               '    glob "^8.1.0"\n'
               '    mkdirp "^2.1.3"\n'
               '    reflect-metadata "^0.1.13"\n'
               '    sha.js "^2.4.11"\n'
               '    tslib "^2.5.0"\n'
               '    uuid "^9.0.0"\n'
               '    yargs "^17.6.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=484,
          lineno=3299,
          tokens=223,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               '"typescript@>= 4.5.5 < 5", "typescript@>=2.8.0 || >= 3.2.0-dev '
               '|| >= 3.3.0-dev || >= 3.4.0-dev || >= 3.5.0-dev || >= '
               '3.6.0-dev || >= 3.6.0-beta || >= 3.7.0-dev || >= 3.7.0-beta", '
               'typescript@>=3.3.1, typescript@4.9.5:\n'
               '  version "4.9.5"\n'
               '  resolved '
               '"https://registry.npmjs.org/typescript/-/typescript-4.9.5.tgz"\n'
               '  integrity '
               'sha512-1FXk9E2Hm+QzZQ7z+McJiHL4NW1F2EzMu9Nq9i3zAaGqibafqYwCVU6WyWAuyQRRzOlxou8xZSyXLEN8oKj24g==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=485,
          lineno=3304,
          tokens=165,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'unbox-primitive@^1.0.2:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/unbox-primitive/-/unbox-primitive-1.0.2.tgz"\n'
               '  integrity '
               'sha512-61pPlCD9h51VoreyJ0BReideM3MDKMKnh6+V9L08331ipq6Q8OFXZYiqP6n/tbHx4s5I9uRhcye6BrbkizkBDw==\n'
               '  dependencies:\n'
               '    call-bind "^1.0.2"\n'
               '    has-bigints "^1.0.2"\n'
               '    has-symbols "^1.0.3"\n'
               '    which-boxed-primitive "^1.0.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=486,
          lineno=3314,
          tokens=229,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'underscore@^1.8.2:\n'
               '  version "1.13.6"\n'
               '  resolved '
               '"https://registry.npmjs.org/underscore/-/underscore-1.13.6.tgz"\n'
               '  integrity '
               'sha512-+A5Sja4HP1M08MaXya7p5LvjuM7K6q/2EaC0+iovj/wOcMsTzMvDFbasi/oSapiwOlt252IqsKqPjCl7huKS0A==\n'
               '\n'
               'untildify@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/untildify/-/untildify-4.0.0.tgz"\n'
               '  integrity '
               'sha512-KK8xQ1mkzZeg9inewmFVDNkg3l5LUhoq9kN6iWYB/CC9YMG8HA+c1Q8HwDe6dEX7kErrEVNVBO3fWsVq5iDgtw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=487,
          lineno=3324,
          tokens=149,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'update-browserslist-db@^1.0.11:\n'
               '  version "1.0.11"\n'
               '  resolved '
               '"https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.0.11.tgz"\n'
               '  integrity '
               'sha512-dCwEFf0/oT85M1fHBg4F0jtLwJrutGoHSQXCh7u4o2t1drG+c0a9Flnqww6XUKSfQMPpJBRjU8d4RXB09qtvaA==\n'
               '  dependencies:\n'
               '    escalade "^3.1.1"\n'
               '    picocolors "^1.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=488,
          lineno=3332,
          tokens=243,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'uri-js@^4.2.2:\n'
               '  version "4.4.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz"\n'
               '  integrity '
               'sha512-7rKUyy33Q1yc98pQ1DAmLtwX109F7TIfWlW1Ydo8Wl1ii1SeHieeh0HHfPeL2fMXK6z0s8ecKs9frCuLJvndBg==\n'
               '  dependencies:\n'
               '    punycode "^2.1.0"\n'
               '\n'
               'url-join@^4.0.1:\n'
               '  version "4.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/url-join/-/url-join-4.0.1.tgz"\n'
               '  integrity '
               'sha512-jk1+QP6ZJqyOiuEI9AEWQfju/nB2Pw466kbA0LEZljHwKeMgd9WrAEgEGxjPDD2+TNbbb37rTyhEfrCXfuKXnA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=489,
          lineno=3344,
          tokens=240,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'use-composed-ref@^1.3.0:\n'
               '  version "1.3.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/use-composed-ref/-/use-composed-ref-1.3.0.tgz"\n'
               '  integrity '
               'sha512-GLMG0Jc/jiKov/3Ulid1wbv3r54K9HlMW29IWcDFPEqFkSO2nS0MuefWgMJpeHQ9YJeXDL3ZUF+P3jdXlZX/cQ==\n'
               '\n'
               'use-isomorphic-layout-effect@^1.1.1:\n'
               '  version "1.1.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/use-isomorphic-layout-effect/-/use-isomorphic-layout-effect-1.1.2.tgz"\n'
               '  integrity '
               'sha512-49L8yCO3iGT/ZF9QttjwLF/ZD9Iwto5LnH5LmEdk/6cFmXddqi2ulF0edxTwjj+7mqvpVVGQWvbXZdn32wRSHA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=490,
          lineno=3354,
          tokens=133,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'use-latest@^1.2.1:\n'
               '  version "1.2.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/use-latest/-/use-latest-1.2.1.tgz"\n'
               '  integrity '
               'sha512-xA+AVm/Wlg3e2P/JiItTziwS7FK92LWrDB0p+hgXloIMuVCeJJ8v6f0eeHyPZaJrM+usM1FkFfbNCrJGs8A/zw==\n'
               '  dependencies:\n'
               '    use-isomorphic-layout-effect "^1.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=491,
          lineno=3361,
          tokens=228,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'util-deprecate@^1.0.2:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz"\n'
               '  integrity '
               'sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==\n'
               '\n'
               'uuid@^3.3.2:\n'
               '  version "3.4.0"\n'
               '  resolved "https://registry.npmjs.org/uuid/-/uuid-3.4.0.tgz"\n'
               '  integrity '
               'sha512-HjSDRw6gZE5JMggctHBcjVak08+KEVhSIiDzFnT9S9aegmp85S/bReBVTb4QTFaRNptJ9kuYaNhnbNEOkbKb/A==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=492,
          lineno=3371,
          tokens=223,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'uuid@^8.3.2:\n'
               '  version "8.3.2"\n'
               '  resolved "https://registry.npmjs.org/uuid/-/uuid-8.3.2.tgz"\n'
               '  integrity '
               'sha512-+NYs2QeMWy+GWFOEm9xnn6HCDp0l7QBD7ml8zLUmJ+93Q5NF0NocErnwkTkXVFNiX3/fpC6afS8Dhb/gz7R7eg==\n'
               '\n'
               'uuid@^9.0.0:\n'
               '  version "9.0.0"\n'
               '  resolved "https://registry.npmjs.org/uuid/-/uuid-9.0.0.tgz"\n'
               '  integrity '
               'sha512-MXcSTerfPa4uqyzStbRoTgt5XIe3x5+42+q1sDuy3R5MDk66URdLMOZe5aPX/SQd+kuYAh0FdP/pO28IkQyTeg==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=493,
          lineno=3381,
          tokens=142,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'verror@1.10.0:\n'
               '  version "1.10.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/verror/-/verror-1.10.0.tgz"\n'
               '  integrity '
               'sha512-ZZKSmDAEFOijERBLkmYfJ+vmk3w+7hOLYDNkRCuRuMJGEmqYNCNLyBBFwWKVMhfwaEF3WOd0Zlw86U/WC/+nYw==\n'
               '  dependencies:\n'
               '    assert-plus "^1.0.0"\n'
               '    core-util-is "1.0.2"\n'
               '    extsprintf "^1.2.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=494,
          lineno=3390,
          tokens=231,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'webidl-conversions@^3.0.0:\n'
               '  version "3.0.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/webidl-conversions/-/webidl-conversions-3.0.1.tgz"\n'
               '  integrity '
               'sha512-2JAn3z8AR6rjK8Sm8orRC0h/bcl/DqL7tRPdGZ4I1CjdF+EaMLmYxBHyXuKL849eucPFhvBoxMsflfOb8kxaeQ==\n'
               '\n'
               'whatwg-fetch@^3.4.1:\n'
               '  version "3.6.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/whatwg-fetch/-/whatwg-fetch-3.6.2.tgz"\n'
               '  integrity '
               'sha512-bJlen0FcuU/0EMLrdbJ7zOnW6ITZLrZMIarMUVmdKtsGvZna8vxKYaexICWPfZ8qwf9fzNq+UEIZrnSaApt6RA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=495,
          lineno=3400,
          tokens=140,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'whatwg-url@^5.0.0:\n'
               '  version "5.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/whatwg-url/-/whatwg-url-5.0.0.tgz"\n'
               '  integrity '
               'sha512-saE57nupxk6v3HY35+jzBwYa0rKSy0XR8JSxZPwgLr7ys0IBzhGviA1/TUGJLmSVqs8pb9AnvICXEuOHLprYTw==\n'
               '  dependencies:\n'
               '    tr46 "~0.0.3"\n'
               '    webidl-conversions "^3.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=496,
          lineno=3408,
          tokens=177,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'which-boxed-primitive@^1.0.2:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/which-boxed-primitive/-/which-boxed-primitive-1.0.2.tgz"\n'
               '  integrity '
               'sha512-bwZdv0AKLpplFY2KZRX6TvyuN7ojjr7lwkg6ml0roIy9YeuSr7JS372qlNW18UQYzgYK9ziGcerWqZOmEn9VNg==\n'
               '  dependencies:\n'
               '    is-bigint "^1.0.1"\n'
               '    is-boolean-object "^1.1.0"\n'
               '    is-number-object "^1.0.4"\n'
               '    is-string "^1.0.5"\n'
               '    is-symbol "^1.0.3"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=497,
          lineno=3419,
          tokens=189,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'which-typed-array@^1.1.9:\n'
               '  version "1.1.9"\n'
               '  resolved '
               '"https://registry.npmjs.org/which-typed-array/-/which-typed-array-1.1.9.tgz"\n'
               '  integrity '
               'sha512-w9c4xkx6mPidwp7180ckYWfMmvxpjlZuIudNtDf4N/tTAUB8VJbX25qZoAsrtGuYNnGw3pa0AXgbGKRB8/EceA==\n'
               '  dependencies:\n'
               '    available-typed-arrays "^1.0.5"\n'
               '    call-bind "^1.0.2"\n'
               '    for-each "^0.3.3"\n'
               '    gopd "^1.0.1"\n'
               '    has-tostringtag "^1.0.0"\n'
               '    is-typed-array "^1.1.10"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=498,
          lineno=3431,
          tokens=120,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'which@^2.0.1:\n'
               '  version "2.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/which/-/which-2.0.2.tgz"\n'
               '  integrity '
               'sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==\n'
               '  dependencies:\n'
               '    isexe "^2.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=499,
          lineno=3438,
          tokens=168,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'winston@^2.3.1:\n'
               '  version "2.4.7"\n'
               '  resolved '
               '"https://registry.npmjs.org/winston/-/winston-2.4.7.tgz"\n'
               '  integrity '
               'sha512-vLB4BqzCKDnnZH9PHGoS2ycawueX4HLqENXQitvFHczhgW2vFpSOn31LZtVr1KU8YTw7DS4tM+cqyovxo8taVg==\n'
               '  dependencies:\n'
               '    async "^2.6.4"\n'
               '    colors "1.0.x"\n'
               '    cycle "1.0.x"\n'
               '    eyes "0.1.x"\n'
               '    isstream "0.1.x"\n'
               '    stack-trace "0.0.x"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=500,
          lineno=3450,
          tokens=151,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'wrap-ansi@^7.0.0:\n'
               '  version "7.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz"\n'
               '  integrity '
               'sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==\n'
               '  dependencies:\n'
               '    ansi-styles "^4.0.0"\n'
               '    string-width "^4.1.0"\n'
               '    strip-ansi "^6.0.0"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=501,
          lineno=3459,
          tokens=225,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'wrappy@1:\n'
               '  version "1.0.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/wrappy/-/wrappy-1.0.2.tgz"\n'
               '  integrity '
               'sha512-l4Sp/DRseor9wL6EvV2+TuQn63dMkPjZ/sp9XkghTEbV9KlPS1xUsZ3u7/IQO4wxtcFB4bgpQPRcR3QCvezPcQ==\n'
               '\n'
               'y18n@^5.0.5:\n'
               '  version "5.0.8"\n'
               '  resolved "https://registry.npmjs.org/y18n/-/y18n-5.0.8.tgz"\n'
               '  integrity '
               'sha512-0pfFzegeDWJHJIAmTLRP2DwHjdF5s7jo9tuztdQxAhINCdvS+3nGINqPd00AphqJR/0LhANUS6/+7SCb98YOfA==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=502,
          lineno=3469,
          tokens=224,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'yallist@^4.0.0:\n'
               '  version "4.0.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/yallist/-/yallist-4.0.0.tgz"\n'
               '  integrity '
               'sha512-3wdGidZyq5PB084XLES5TpOSRA3wjXAlIWMhum2kRcv/41Sn2emQ0dycQW4uZXLejwKvg6EsvbdlVL+FYEct7A==\n'
               '\n'
               'yaml@^2.1.1:\n'
               '  version "2.3.1"\n'
               '  resolved "https://registry.npmjs.org/yaml/-/yaml-2.3.1.tgz"\n'
               '  integrity '
               'sha512-2eHWfjaoXgTBC2jNM1LRef62VQa0umtvRiDSk6HSzW7RvS5YtkabJrwYLLEKWBc8a5U2PTSCs+dJjUTJdlHsWQ==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=503,
          lineno=3479,
          tokens=229,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'yargs-parser@^20.2.2:\n'
               '  version "20.2.9"\n'
               '  resolved '
               '"https://registry.npmjs.org/yargs-parser/-/yargs-parser-20.2.9.tgz"\n'
               '  integrity '
               'sha512-y11nGElTIV+CT3Zv9t7VKl+Q3hTQoT9a1Qzezhhl6Rp21gJ/IVTW7Z3y9EWXhuUBC2Shnf+DX0antecpAwSP8w==\n'
               '\n'
               'yargs-parser@^21.1.1:\n'
               '  version "21.1.1"\n'
               '  resolved '
               '"https://registry.npmjs.org/yargs-parser/-/yargs-parser-21.1.1.tgz"\n'
               '  integrity '
               'sha512-tVpsJW7DdjecAiFpbIB1e3qxIQsE6NoPc5/eTdrbbIC4h0LVsWhnoa3g+m2HclBIujHzsxZ4VJVA+GUuc2/LBw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=504,
          lineno=3489,
          tokens=193,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'yargs@^16.0.0:\n'
               '  version "16.2.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/yargs/-/yargs-16.2.0.tgz"\n'
               '  integrity '
               'sha512-D1mvvtDG0L5ft/jGWkLpG1+m0eQxOfaBvTNELraWj22wSVUMWxZUvYgJYcKh6jGGIkJFhH4IZPQhR4TKpc8mBw==\n'
               '  dependencies:\n'
               '    cliui "^7.0.2"\n'
               '    escalade "^3.1.1"\n'
               '    get-caller-file "^2.0.5"\n'
               '    require-directory "^2.1.1"\n'
               '    string-width "^4.2.0"\n'
               '    y18n "^5.0.5"\n'
               '    yargs-parser "^20.2.2"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=505,
          lineno=3502,
          tokens=187,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'yargs@^17.6.2:\n'
               '  version "17.7.2"\n'
               '  resolved '
               '"https://registry.npmjs.org/yargs/-/yargs-17.7.2.tgz"\n'
               '  integrity '
               'sha512-7dSzzRQ++CKnNI/krKnYRV7JKKPUXMEh61soaHKg9mrWEhzFWhFnxPxGl+69cD1Ou63C13NUPCnmIcrvqCuM6w==\n'
               '  dependencies:\n'
               '    cliui "^8.0.1"\n'
               '    escalade "^3.1.1"\n'
               '    get-caller-file "^2.0.5"\n'
               '    require-directory "^2.1.1"\n'
               '    string-width "^4.2.3"\n'
               '    y18n "^5.0.5"\n'
               '    yargs-parser "^21.1.1"\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=506,
          lineno=3515,
          tokens=235,
          depth=1,
          parent_id=None,
          category='documentation',
          summary=False,
          name='',
          body='\n'
               'yocto-queue@^0.1.0:\n'
               '  version "0.1.0"\n'
               '  resolved '
               '"https://registry.npmjs.org/yocto-queue/-/yocto-queue-0.1.0.tgz"\n'
               '  integrity '
               'sha512-rVksvsnNCdJ/ohGc6xgPwyN8eheCxsiLM8mxuE/t/mOVqJewPuO1miLpTHQiRgTKCLexL4MeAFVagts7HmNZ2Q==\n'
               '\n'
               'zod@^3.21.4:\n'
               '  version "3.21.4"\n'
               '  resolved "https://registry.npmjs.org/zod/-/zod-3.21.4.tgz"\n'
               '  integrity '
               'sha512-m46AKbrzKVzOzs/DZgVnG5H55N1sv1M8qZU3A8RIKbs3mrACDNeIOeilDymVb2HdmP8uwshOCF4uJ8uM9rCqJw==\n'),
 Fragment(document_cs='8c005c18e4f4eb07f7cb25464985dd401eea88bc880a26fce2e74c3780197e40',
          id=507,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='93aba7bd58f1549fef34a17963cea65fa40ee7ebd0ed5342416e76c98004305a',
          id=508,
          lineno=1,
          tokens=0,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body=''),
 Fragment(document_cs='93c9b7c1c4a20930f61173fa77086d5e1cd11dcca05d6179d1db13f97b2e18fd',
          id=509,
          lineno=1,
          tokens=49,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { cn } from '@/lib/utils'import { cva, VariantProps } "
               "from 'class-variance-authority'import { Loader2 } from "
               "'lucide-react'import { ButtonHTMLAttributes, FC } from 'react'"),
 Fragment(document_cs='93c9b7c1c4a20930f61173fa77086d5e1cd11dcca05d6179d1db13f97b2e18fd',
          id=510,
          lineno=27,
          tokens=28,
          depth=2,
          parent_id=None,
          category='interface',
          summary=False,
          name='ButtonProps',
          body='interface ButtonProps\n'
               '  extends ButtonHTMLAttributes<HTMLButtonElement>,\n'
               '    VariantProps<typeof buttonVariants> {\n'
               '  isLoading?: boolean\n'
               '}'),
 Fragment(document_cs='93c9b7c1c4a20930f61173fa77086d5e1cd11dcca05d6179d1db13f97b2e18fd',
          id=511,
          lineno=59,
          tokens=20,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='PersonInterface',
          body='interface PersonInterface {\n'
               '  age: number\n'
               '  name: string\n'
               '  job?: boolean\n'
               '}'),
 Fragment(document_cs='93c9b7c1c4a20930f61173fa77086d5e1cd11dcca05d6179d1db13f97b2e18fd',
          id=512,
          lineno=6,
          tokens=176,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='buttonVariants',
          body='buttonVariants = cva(\n'
               "  'active:scale-95 inline-flex items-center justify-center "
               'rounded-md text-sm font-medium transition-color '
               'focus:outline-none focus:ring-2 focus:ring-slate-400 '
               'focus:ring-offset-2 disabled:opacity-50 '
               "disabled:pointer-events-none',\n"
               '  {\n'
               '    variants: {\n'
               '      variant: {\n'
               "        default: 'bg-slate-900 text-white "
               "hover:bg-slate-800',\n"
               "        ghost: 'bg-transparent hover:text-slate-900 "
               "hover:bg-slate-200',\n"
               '      },\n'
               '      size: {\n'
               "        default: 'h-10 py-2 px-4',\n"
               "        sm: 'h-9 px-2',\n"
               "        lg: 'h-11 px-8',\n"
               '      },\n'
               '    },\n'
               '    defaultVariants: {\n'
               "      variant: 'default',\n"
               "      size: 'default',\n"
               '    },\n'
               '  }\n'
               ')'),
 Fragment(document_cs='93c9b7c1c4a20930f61173fa77086d5e1cd11dcca05d6179d1db13f97b2e18fd',
          id=513,
          lineno=33,
          tokens=97,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='Button',
          body='Button: FC<ButtonProps> = ({\n'
               '  className,\n'
               '  children,\n'
               '  variant,\n'
               '  isLoading,\n'
               '  size,\n'
               '  ...props\n'
               '}) => {\n'
               '  return (\n'
               '    <button\n'
               '      className={cn(buttonVariants({ variant, size, className '
               '}))}\n'
               '      disabled={isLoading}\n'
               '      {...props}>\n'
               "      {isLoading ? <Loader2 className='mr-2 h-4 w-4 "
               "animate-spin' /> : null}\n"
               '      {children}\n'
               '    </button>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='93c9b7c1c4a20930f61173fa77086d5e1cd11dcca05d6179d1db13f97b2e18fd',
          id=514,
          lineno=65,
          tokens=19,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='Person',
          body="Person: PersonInterface = {\n  age: 14,\n  name: 'John'\n}"),
 Fragment(document_cs='93c9b7c1c4a20930f61173fa77086d5e1cd11dcca05d6179d1db13f97b2e18fd',
          id=515,
          lineno=1,
          tokens=40,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: ButtonProps PersonInterface\n'
               '  Variables: Button Person buttonVariants\n'
               '  Usages: ButtonHTMLAttributes FC HTMLButtonElement Loader2 '
               'VariantProps button className cva disabled isLoading props\n'),
 Fragment(document_cs='9db4c982c1acfa5852385bae4c63c905b8a26d025af05ab903280a67aa572b66',
          id=516,
          lineno=1,
          tokens=60,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import FriendRequests from '@/components/FriendRequests'import "
               "{ fetchRedis } from '@/helpers/redis'import { authOptions } "
               "from '@/lib/auth'import { getServerSession } from "
               "'next-auth'import { notFound } from 'next/navigation'import { "
               "FC } from 'react'"),
 Fragment(document_cs='9db4c982c1acfa5852385bae4c63c905b8a26d025af05ab903280a67aa572b66',
          id=517,
          lineno=8,
          tokens=231,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='page',
          body='page = async () => {\n'
               '  const session = await getServerSession(authOptions)\n'
               '  if (!session) notFound()\n'
               '\n'
               '  // ids of people who sent current logged in user a friend '
               'requests\n'
               '  const incomingSenderIds = (await fetchRedis(\n'
               "    'smembers',\n"
               '    `user:${session.user.id}:incoming_friend_requests`\n'
               '  )) as string[]\n'
               '\n'
               '  const incomingFriendRequests = await Promise.all(\n'
               '    incomingSenderIds.map(async (senderId) => {\n'
               "      const sender = (await fetchRedis('get', "
               '`user:${senderId}`)) as string\n'
               '      const senderParsed = JSON.parse(sender) as User\n'
               '      \n'
               '      return {\n'
               '        senderId,\n'
               '        senderEmail: senderParsed.email,\n'
               '      }\n'
               '    })\n'
               '  )\n'
               '\n'
               '  return (\n'
               "    <main className='pt-8'>\n"
               "      <h1 className='font-bold text-5xl mb-8'>Add a "
               'friend</h1>\n'
               "      <div className='flex flex-col gap-4'>\n"
               '        <FriendRequests\n'
               '          incomingFriendRequests={incomingFriendRequests}\n'
               '          sessionId={session.user.id}\n'
               '        />\n'
               '      </div>\n'
               '    </main>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='9db4c982c1acfa5852385bae4c63c905b8a26d025af05ab903280a67aa572b66',
          id=518,
          lineno=9,
          tokens=9,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='session',
          body='session = await getServerSession(authOptions)'),
 Fragment(document_cs='9db4c982c1acfa5852385bae4c63c905b8a26d025af05ab903280a67aa572b66',
          id=519,
          lineno=13,
          tokens=31,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='incomingSenderIds',
          body='incomingSenderIds = (await fetchRedis(\n'
               "    'smembers',\n"
               '    `user:${session.user.id}:incoming_friend_requests`\n'
               '  )) as string[]'),
 Fragment(document_cs='9db4c982c1acfa5852385bae4c63c905b8a26d025af05ab903280a67aa572b66',
          id=520,
          lineno=18,
          tokens=74,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='incomingFriendRequests',
          body='incomingFriendRequests = await Promise.all(\n'
               '    incomingSenderIds.map(async (senderId) => {\n'
               "      const sender = (await fetchRedis('get', "
               '`user:${senderId}`)) as string\n'
               '      const senderParsed = JSON.parse(sender) as User\n'
               '      \n'
               '      return {\n'
               '        senderId,\n'
               '        senderEmail: senderParsed.email,\n'
               '      }\n'
               '    })\n'
               '  )'),
 Fragment(document_cs='9db4c982c1acfa5852385bae4c63c905b8a26d025af05ab903280a67aa572b66',
          id=521,
          lineno=20,
          tokens=18,
          depth=14,
          parent_id=None,
          category='variable',
          summary=False,
          name='sender',
          body="sender = (await fetchRedis('get', `user:${senderId}`)) as "
               'string'),
 Fragment(document_cs='9db4c982c1acfa5852385bae4c63c905b8a26d025af05ab903280a67aa572b66',
          id=522,
          lineno=21,
          tokens=9,
          depth=14,
          parent_id=None,
          category='variable',
          summary=False,
          name='senderParsed',
          body='senderParsed = JSON.parse(sender) as User'),
 Fragment(document_cs='9db4c982c1acfa5852385bae4c63c905b8a26d025af05ab903280a67aa572b66',
          id=523,
          lineno=1,
          tokens=43,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: incomingFriendRequests incomingSenderIds page '
               'sender senderParsed session\n'
               '  Usages: Add FC FriendRequests JSON Promise User authOptions '
               'className div fetchRedis friend getServerSession main notFound '
               'senderId sessionId\n'),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=524,
          lineno=1,
          tokens=157,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { Icon, Icons } from '@/components/Icons'import "
               "SignOutButton from '@/components/SignOutButton'import { "
               "authOptions } from '@/lib/auth'import { getServerSession } "
               "from 'next-auth'import Image from 'next/image'import Link from "
               "'next/link'import { notFound } from 'next/navigation'import { "
               "FC, ReactNode } from 'react'import FriendRequestSidebarOptions "
               "from '@/components/FriendRequestSidebarOptions'import { "
               "fetchRedis } from '@/helpers/redis'import { getFriendsByUserId "
               "} from '@/helpers/get-friends-by-user-id'import "
               "SidebarChatList from '@/components/SidebarChatList'import "
               "MobileChatLayout from '@/components/MobileChatLayout'import { "
               "SidebarOption } from '@/types/typings'"),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=525,
          lineno=17,
          tokens=28,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='LayoutProps',
          body='interface LayoutProps {\n'
               '  children: ReactNode\n'
               '  session: any\n'
               '  friends: any\n'
               '  unseenRequestCount: number\n'
               '}'),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=526,
          lineno=25,
          tokens=22,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='metadata',
          body='metadata = {\n'
               "  title: 'Macro Integrations Portal | Dashboard',\n"
               "  description: 'Your dashboard',\n"
               '}'),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=527,
          lineno=30,
          tokens=40,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='sidebarOptions',
          body='sidebarOptions: SidebarOption[] = [\n'
               '  {\n'
               '    id: 1,\n'
               "    name: 'Add friend',\n"
               "    href: '/dashboard/add',\n"
               "    Icon: 'UserPlus',\n"
               '  },\n'
               ']'),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=528,
          lineno=39,
          tokens=249,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='Layout',
          body='Layout = async ({ children }: LayoutProps) => {\n'
               '  const session = await getServerSession(authOptions)\n'
               '  if (!session) notFound()\n'
               '\n'
               '  const friends = await getFriendsByUserId(session.user.id)\n'
               "  console.log('friends', friends)\n"
               '\n'
               '  const unseenRequestCount = (\n'
               '    (await fetchRedis(\n'
               "      'smembers',\n"
               '      `user:${session.user.id}:incoming_friend_requests`\n'
               '    )) as User[]\n'
               '  ).length\n'
               '\n'
               '  return (\n'
               "    <div className='w-full flex h-screen'>\n"
               "      <div className='md:hidden'>\n"
               '        <MobileChatLayout\n'
               '          friends={friends}\n'
               '          session={session}\n'
               '          sidebarOptions={sidebarOptions}\n'
               '          unseenRequestCount={unseenRequestCount}\n'
               '        />\n'
               '      </div>\n'
               '\n'
               "      <div className='hidden md:flex h-full w-full max-w-xs "
               'grow flex-col gap-y-5 overflow-y-auto border-r border-gray-200 '
               "bg-white px-6'>\n"
               "        <Link href='/dashboard' className='flex h-16 shrink-0 "
               "items-center'>\n"
               "          <Icons.Logo className='h-8 w-auto text-indigo-600' "
               '/>\n'
               '        </Link>\n'
               '\n'
               '        {friends.length > 0 ? (\n'
               "          <div className='text-xs font-semib"),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=529,
          lineno=40,
          tokens=9,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='session',
          body='session = await getServerSession(authOptions)'),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=530,
          lineno=43,
          tokens=11,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='friends',
          body='friends = await getFriendsByUserId(session.user.id)'),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=531,
          lineno=46,
          tokens=37,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='unseenRequestCount',
          body='unseenRequestCount = (\n'
               '    (await fetchRedis(\n'
               "      'smembers',\n"
               '      `user:${session.user.id}:incoming_friend_requests`\n'
               '    )) as User[]\n'
               '  ).length'),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=532,
          lineno=70,
          tokens=203,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='Layout',
          body="old leading-6 text-gray-400'>\n"
               '            Your chats\n'
               '          </div>\n'
               '        ) : null}\n'
               '\n'
               "        <nav className='flex flex-1 flex-col'>\n"
               "          <ul role='list' className='flex flex-1 flex-col "
               "gap-y-7'>\n"
               '            <li>\n'
               '              <SidebarChatList sessionId={session.user.id} '
               'friends={friends} />\n'
               '            </li>\n'
               '            <li>\n'
               "              <div className='text-xs font-semibold leading-6 "
               "text-gray-400'>\n"
               '                Overview\n'
               '              </div>\n'
               '\n'
               "              <ul role='list' className='-mx-2 mt-2 "
               "space-y-1'>\n"
               '                {sidebarOptions.map((option) => {\n'
               '                  const Icon = Icons[option.Icon]\n'
               '                  return (\n'
               '                    <li key={option.id}>\n'
               '                      <Link\n'
               '                        href={option.href}\n'
               "                        className='text-gray-700 "
               'hover:text-indigo-600 hover:bg-gray-50 group flex gap-3 '
               "rounded-md p-2 text-sm leading-6 font-semibold'>\n"
               '                        '),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=533,
          lineno=87,
          tokens=7,
          depth=29,
          parent_id=None,
          category='variable',
          summary=False,
          name='Icon',
          body='Icon = Icons[option.Icon]'),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=534,
          lineno=93,
          tokens=191,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='Layout',
          body="<span className='text-gray-400 border-gray-200 "
               'group-hover:border-indigo-600 group-hover:text-indigo-600 flex '
               'h-6 w-6 shrink-0 items-center justify-center rounded-lg border '
               "text-[0.625rem] font-medium bg-white'>\n"
               "                          <Icon className='h-4 w-4' />\n"
               '                        </span>\n'
               '\n'
               '                        <span '
               "className='truncate'>{option.name}</span>\n"
               '                      </Link>\n'
               '                    </li>\n'
               '                  )\n'
               '                })}\n'
               '\n'
               '                <li>\n'
               '                  <FriendRequestSidebarOptions\n'
               '                    sessionId={session.user.id}\n'
               '                    '
               'initialUnseenRequestCount={unseenRequestCount}\n'
               '                  />\n'
               '                </li>\n'
               '              </ul>\n'
               '            </li>\n'
               '\n'
               "            <li className='-mx-6 mt-auto flex items-center'>\n"
               "              <div className='flex flex-1 items-center gap-x-4 "
               "px-6 py-3 text-sm font-semibold leading-6 text-gray-900'>\n"
               '                <div class'),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=535,
          lineno=114,
          tokens=193,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='Layout',
          body="Name='relative h-8 w-8 bg-gray-50'>\n"
               '                  <Image\n'
               '                    fill\n'
               "                    referrerPolicy='no-referrer'\n"
               "                    className='rounded-full'\n"
               "                    src={session.user.image || ''}\n"
               "                    alt='Your profile picture'\n"
               '                  />\n'
               '                </div>\n'
               '\n'
               "                <span className='sr-only'>Your profile</span>\n"
               "                <div className='flex flex-col'>\n"
               '                  <span '
               "aria-hidden='true'>{session.user.name}</span>\n"
               "                  <span className='text-xs text-zinc-400' "
               "aria-hidden='true'>\n"
               '                    {session.user.email}\n'
               '                  </span>\n'
               '                </div>\n'
               '              </div>\n'
               '\n'
               "              <SignOutButton className='h-full aspect-square' "
               '/>\n'
               '            </li>\n'
               '          </ul>\n'
               '        </nav>\n'
               '      </div>\n'
               '\n'
               "      <aside className='max-h-screen container py-16 md:py-12 "
               "w-full'>\n"
               '        {children}\n'
               '      </aside>\n'
               '    </div>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='a3c34199b1dfd10b3da2e4542c45b109f4ee50cb933b173605f38d41816d7a5d',
          id=536,
          lineno=1,
          tokens=90,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: LayoutProps\n'
               '  Variables: Icon Layout friends metadata session '
               'sidebarOptions unseenRequestCount\n'
               '  Usages: FC FriendRequestSidebarOptions Icons Image Link Logo '
               'MobileChatLayout Overview ReactNode SidebarChatList '
               'SidebarOption SignOutButton User Your alt aria aside '
               'authOptions chats className console div fetchRedis fill '
               'getFriendsByUserId getServerSession hidden href image '
               'initialUnseenRequestCount nav notFound option profile '
               'referrerPolicy role sessionId span src user\n'),
 Fragment(document_cs='a3ec3f9e8c52ad0df3514ca2f778f0dce17c003dfb47d9be77ae559026f40b67',
          id=537,
          lineno=1,
          tokens=90,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { fetchRedis } from '@/helpers/redis'import { "
               "authOptions } from '@/lib/auth'import { db } from "
               "'@/lib/db'import { pusherServer } from '@/lib/pusher'import { "
               "toPusherKey } from '@/lib/utils'import { addFriendValidator } "
               "from '@/lib/validations/add-friend'import { getServerSession } "
               "from 'next-auth'import { z } from 'zod'"),
 Fragment(document_cs='a3ec3f9e8c52ad0df3514ca2f778f0dce17c003dfb47d9be77ae559026f40b67',
          id=538,
          lineno=11,
          tokens=207,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='POST',
          body='async function POST(req: Request) {\n'
               '  try {\n'
               '    const body = await req.json()\n'
               '\n'
               '    const { email: emailToAdd } = '
               'addFriendValidator.parse(body.email)\n'
               '\n'
               '    const idToAdd = (await fetchRedis(\n'
               "      'get',\n"
               '      `user:email:${emailToAdd}`\n'
               '    )) as string\n'
               '\n'
               '    if (!idToAdd) {\n'
               "      return new Response('This person does not exist.', { "
               'status: 400 })\n'
               '    }\n'
               '\n'
               '    const session = await getServerSession(authOptions)\n'
               '\n'
               '    if (!session) {\n'
               "      return new Response('Unauthorized', { status: 401 })\n"
               '    }\n'
               '\n'
               '    if (idToAdd === session.user.id) {\n'
               "      return new Response('You cannot add yourself as a "
               "friend', {\n"
               '        status: 400,\n'
               '      })\n'
               '    }\n'
               '\n'
               '    // check if user is already added\n'
               '    const isAlreadyAdded = (await fetchRedis(\n'
               "      'sismember',\n"
               '      `user:${idToAdd}:incoming_friend_requests`,\n'
               '      session.user.id\n'
               '    )) as 0 | 1\n'),
 Fragment(document_cs='a3ec3f9e8c52ad0df3514ca2f778f0dce17c003dfb47d9be77ae559026f40b67',
          id=539,
          lineno=44,
          tokens=240,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='POST',
          body='\n'
               '    if (isAlreadyAdded) {\n'
               "      return new Response('Already added this user', { status: "
               '400 })\n'
               '    }\n'
               '\n'
               '    // check if user is already added\n'
               '    const isAlreadyFriends = (await fetchRedis(\n'
               "      'sismember',\n"
               '      `user:${session.user.id}:friends`,\n'
               '      idToAdd\n'
               '    )) as 0 | 1\n'
               '\n'
               '    if (isAlreadyFriends) {\n'
               "      return new Response('Already friends with this user', { "
               'status: 400 })\n'
               '    }\n'
               '\n'
               '    // valid request, send friend request\n'
               '\n'
               '    await pusherServer.trigger(\n'
               '      '
               'toPusherKey(`user:${idToAdd}:incoming_friend_requests`),\n'
               "      'incoming_friend_requests',\n"
               '      {\n'
               '        senderId: session.user.id,\n'
               '        senderEmail: session.user.email,\n'
               '      }\n'
               '    )\n'
               '\n'
               '    await db.sadd(`user:${idToAdd}:incoming_friend_requests`, '
               'session.user.id)\n'
               '\n'
               "    return new Response('OK')\n"
               '  } catch (error) {\n'
               '    if (error instanceof z.ZodError) {\n'
               "      return new Response('Invalid request payload', { status: "
               '422 })\n'
               '    }\n'
               '\n'
               "    return new Response('Invalid request', { status: 400 })\n"
               '  }\n'
               '}'),
 Fragment(document_cs='a3ec3f9e8c52ad0df3514ca2f778f0dce17c003dfb47d9be77ae559026f40b67',
          id=540,
          lineno=13,
          tokens=6,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='body',
          body='body = await req.json()'),
 Fragment(document_cs='a3ec3f9e8c52ad0df3514ca2f778f0dce17c003dfb47d9be77ae559026f40b67',
          id=541,
          lineno=17,
          tokens=25,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='idToAdd',
          body='idToAdd = (await fetchRedis(\n'
               "      'get',\n"
               '      `user:email:${emailToAdd}`\n'
               '    )) as string'),
 Fragment(document_cs='a3ec3f9e8c52ad0df3514ca2f778f0dce17c003dfb47d9be77ae559026f40b67',
          id=542,
          lineno=26,
          tokens=9,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='session',
          body='session = await getServerSession(authOptions)'),
 Fragment(document_cs='a3ec3f9e8c52ad0df3514ca2f778f0dce17c003dfb47d9be77ae559026f40b67',
          id=543,
          lineno=39,
          tokens=39,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='isAlreadyAdded',
          body='isAlreadyAdded = (await fetchRedis(\n'
               "      'sismember',\n"
               '      `user:${idToAdd}:incoming_friend_requests`,\n'
               '      session.user.id\n'
               '    )) as 0 | 1'),
 Fragment(document_cs='a3ec3f9e8c52ad0df3514ca2f778f0dce17c003dfb47d9be77ae559026f40b67',
          id=544,
          lineno=50,
          tokens=37,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='isAlreadyFriends',
          body='isAlreadyFriends = (await fetchRedis(\n'
               "      'sismember',\n"
               '      `user:${session.user.id}:friends`,\n'
               '      idToAdd\n'
               '    )) as 0 | 1'),
 Fragment(document_cs='a3ec3f9e8c52ad0df3514ca2f778f0dce17c003dfb47d9be77ae559026f40b67',
          id=545,
          lineno=1,
          tokens=47,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: POST\n'
               '  Variables: body idToAdd isAlreadyAdded isAlreadyFriends '
               'session\n'
               '  Usages: Request Response addFriendValidator authOptions '
               'emailToAdd error fetchRedis getServerSession pusherServer req '
               'toPusherKey\n'),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=546,
          lineno=1,
          tokens=74,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { fetchRedis } from '@/helpers/redis'import { "
               "authOptions } from '@/lib/auth'import { db } from "
               "'@/lib/db'import { pusherServer } from '@/lib/pusher'import { "
               "toPusherKey } from '@/lib/utils'import { getServerSession } "
               "from 'next-auth'import { z } from 'zod'"),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=547,
          lineno=10,
          tokens=172,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='POST',
          body='async function POST(req: Request) {\n'
               '  try {\n'
               '    const body = await req.json()\n'
               '\n'
               '    const { id: idToAdd } = z.object({ id: z.string() '
               '}).parse(body)\n'
               '\n'
               '    const session = await getServerSession(authOptions)\n'
               '\n'
               '    if (!session) {\n'
               "      return new Response('Unauthorized', { status: 401 })\n"
               '    }\n'
               '\n'
               '    // verify both users are not already friends\n'
               '    const isAlreadyFriends = await fetchRedis(\n'
               "      'sismember',\n"
               '      `user:${session.user.id}:friends`,\n'
               '      idToAdd\n'
               '    )\n'
               '\n'
               '    if (isAlreadyFriends) {\n'
               "      return new Response('Already friends', { status: 400 })\n"
               '    }\n'
               '\n'
               '    const hasFriendRequest = await fetchRedis(\n'
               "      'sismember',\n"
               '      `user:${session.user.id}:incoming_friend_requests`,\n'
               '      idToAdd\n'
               '    )\n'),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=548,
          lineno=38,
          tokens=243,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='POST',
          body='\n'
               '    if (!hasFriendRequest) {\n'
               "      return new Response('No friend request', { status: 400 "
               '})\n'
               '    }\n'
               '\n'
               '    const [userRaw, friendRaw] = (await Promise.all([\n'
               "      fetchRedis('get', `user:${session.user.id}`),\n"
               "      fetchRedis('get', `user:${idToAdd}`),\n"
               '    ])) as [string, string]\n'
               '\n'
               '    const user = JSON.parse(userRaw) as User\n'
               '    const friend = JSON.parse(friendRaw) as User\n'
               '\n'
               '    // notify added user\n'
               '\n'
               '    await Promise.all([\n'
               '      pusherServer.trigger(\n'
               '        toPusherKey(`user:${idToAdd}:friends`),\n'
               "        'new_friend',\n"
               '        user\n'
               '      ),\n'
               '      pusherServer.trigger(\n'
               '        toPusherKey(`user:${session.user.id}:friends`),\n'
               "        'new_friend',\n"
               '        friend\n'
               '      ),\n'
               '      db.sadd(`user:${session.user.id}:friends`, idToAdd),\n'
               '      db.sadd(`user:${idToAdd}:friends`, session.user.id),\n'
               '      '
               'db.srem(`user:${session.user.id}:incoming_friend_requests`, '
               'idToAdd),\n'
               '    ])\n'
               '\n'
               "    return new Response('OK')\n"
               '  } catch (error) {\n'
               '    console.log(error)\n'),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=549,
          lineno=72,
          tokens=46,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='POST',
          body='\n'
               '    if (error instanceof z.ZodError) {\n'
               "      return new Response('Invalid request payload', { status: "
               '422 })\n'
               '    }\n'
               '\n'
               "    return new Response('Invalid request', { status: 400 })\n"
               '  }\n'
               '}'),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=550,
          lineno=12,
          tokens=6,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='body',
          body='body = await req.json()'),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=551,
          lineno=16,
          tokens=9,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='session',
          body='session = await getServerSession(authOptions)'),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=552,
          lineno=23,
          tokens=30,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='isAlreadyFriends',
          body='isAlreadyFriends = await fetchRedis(\n'
               "      'sismember',\n"
               '      `user:${session.user.id}:friends`,\n'
               '      idToAdd\n'
               '    )'),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=553,
          lineno=33,
          tokens=32,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='hasFriendRequest',
          body='hasFriendRequest = await fetchRedis(\n'
               "      'sismember',\n"
               '      `user:${session.user.id}:incoming_friend_requests`,\n'
               '      idToAdd\n'
               '    )'),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=554,
          lineno=48,
          tokens=9,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='user',
          body='user = JSON.parse(userRaw) as User'),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=555,
          lineno=49,
          tokens=10,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='friend',
          body='friend = JSON.parse(friendRaw) as User'),
 Fragment(document_cs='a40415b349634f71042024532f48d5451e999e6c67a83e4495e5d2dbbd7236d5',
          id=556,
          lineno=1,
          tokens=52,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: POST\n'
               '  Variables: body friend hasFriendRequest isAlreadyFriends '
               'session user\n'
               '  Usages: JSON Promise Request Response User authOptions '
               'console error fetchRedis friendRaw getServerSession idToAdd '
               'pusherServer req toPusherKey userRaw\n'),
 Fragment(document_cs='a5f1467407b0b93d38d6c6f2e15aa132d7aad1527a09e8e074bfbbecae77c020',
          id=557,
          lineno=3,
          tokens=69,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { pusherClient } from '@/lib/pusher'import { cn, "
               "toPusherKey } from '@/lib/utils'import { Message } from "
               "'@/lib/validations/message'import { format } from "
               "'date-fns'import Image from 'next/image'import { FC, "
               "useEffect, useRef, useState } from 'react'"),
 Fragment(document_cs='a5f1467407b0b93d38d6c6f2e15aa132d7aad1527a09e8e074bfbbecae77c020',
          id=558,
          lineno=11,
          tokens=38,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='MessagesProps',
          body='interface MessagesProps {\n'
               '  initialMessages: Message[]\n'
               '  sessionId: string\n'
               '  chatId: string\n'
               '  sessionImg: string | null | undefined\n'
               '  chatPartner: User\n'
               '}'),
 Fragment(document_cs='a5f1467407b0b93d38d6c6f2e15aa132d7aad1527a09e8e074bfbbecae77c020',
          id=559,
          lineno=33,
          tokens=25,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='messageHandler',
          body='messageHandler = (message: Message) => {\n'
               '      setMessages((prev) => [message, ...prev])\n'
               '    }'),
 Fragment(document_cs='a5f1467407b0b93d38d6c6f2e15aa132d7aad1527a09e8e074bfbbecae77c020',
          id=560,
          lineno=47,
          tokens=12,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='scrollDownRef',
          body='scrollDownRef = useRef<HTMLDivElement | null>(null)'),
 Fragment(document_cs='a5f1467407b0b93d38d6c6f2e15aa132d7aad1527a09e8e074bfbbecae77c020',
          id=561,
          lineno=49,
          tokens=21,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='formatTimestamp',
          body='formatTimestamp = (timestamp: number) => {\n'
               "    return format(timestamp, 'HH:mm')\n"
               '  }'),
 Fragment(document_cs='a5f1467407b0b93d38d6c6f2e15aa132d7aad1527a09e8e074bfbbecae77c020',
          id=562,
          lineno=60,
          tokens=8,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='isCurrentUser',
          body='isCurrentUser = message.senderId === sessionId'),
 Fragment(document_cs='a5f1467407b0b93d38d6c6f2e15aa132d7aad1527a09e8e074bfbbecae77c020',
          id=563,
          lineno=62,
          tokens=22,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='hasNextMessageFromSameUser',
          body='hasNextMessageFromSameUser =\n'
               '          messages[index - 1]?.senderId === '
               'messages[index].senderId'),
 Fragment(document_cs='a5f1467407b0b93d38d6c6f2e15aa132d7aad1527a09e8e074bfbbecae77c020',
          id=564,
          lineno=1,
          tokens=75,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: MessagesProps\n'
               '  Variables: formatTimestamp hasNextMessageFromSameUser '
               'isCurrentUser messageHandler scrollDownRef\n'
               '  Usages: FC HTMLDivElement Image Message Messages User alt '
               'chatId chatPartner className div fill format image index '
               'initialMessages key message messages prev pusherClient ref '
               'referrerPolicy sessionId sessionImg setMessages span src '
               'timestamp toPusherKey useEffect useRef useState\n'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=565,
          lineno=11,
          tokens=12,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { Smartsheet } from 'smartsheet';"),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=566,
          lineno=27,
          tokens=130,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='getRowsBySite',
          body='async function getRowsBySite(siteNumber: string): '
               'Promise<Row[]> {\n'
               '  try {\n'
               '    const sheet = await smartsheet.sheets.getSheet({ id: '
               'sheetId });\n'
               '    const rows = [];\n'
               '    for (const row of sheet.rows) {\n'
               "      const siteCell = getCellByColumnId(row, columnIds['Site "
               "#']);\n"
               '      if (siteCell.value !== null && parseInt(siteCell.value) '
               '=== parseInt(siteNumber)) {\n'
               '        rows.push(row);\n'
               '      }\n'
               '    }\n'
               '    return rows;\n'
               '  } catch (error) {\n'
               '    console.error(`Error getting rows by site: ${error}`);\n'
               '    throw error;\n'
               '  }\n'
               '}'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=567,
          lineno=44,
          tokens=62,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='getCellByColumnId',
          body='function getCellByColumnId(row: Row, columnId: string): Cell '
               '{\n'
               '  const cell = row.cells.find(cell => cell.columnId === '
               'parseInt(columnId));\n'
               '  if (!cell) {\n'
               '    throw new Error(`No cell found with column ID '
               '${columnId}`);\n'
               '  }\n'
               '  return cell;\n'
               '}'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=568,
          lineno=53,
          tokens=105,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='checkIn',
          body='async function checkIn(row: Row): Promise<void> {\n'
               '  try {\n'
               '    const newCell: Cell = {\n'
               "      columnId: parseInt(columnIds['Checked_In']),\n"
               '      value: true,\n'
               '    };\n'
               '    const newRow: Row = {\n'
               '      id: row.id,\n'
               '      cells: [newCell],\n'
               '    };\n'
               '    await smartsheet.sheets.updateRows(sheetId, [newRow]);\n'
               '  } catch (error) {\n'
               '    console.error(`Error checking in user: ${error}`);\n'
               '    throw error;\n'
               '  }\n'
               '}'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=569,
          lineno=72,
          tokens=105,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='checkOut',
          body='async function checkOut(row: Row): Promise<void> {\n'
               '  try {\n'
               '    const newCell: Cell = {\n'
               "      columnId: parseInt(columnIds['Checked_In']),\n"
               '      value: false,\n'
               '    };\n'
               '    const newRow: Row = {\n'
               '      id: row.id,\n'
               '      cells: [newCell],\n'
               '    };\n'
               '    await smartsheet.sheets.updateRows(sheetId, [newRow]);\n'
               '  } catch (error) {\n'
               '    console.error(`Error checking out user: ${error}`);\n'
               '    throw error;\n'
               '  }\n'
               '}'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=570,
          lineno=13,
          tokens=23,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='smartsheet',
          body='smartsheet = Smartsheet.createClient({\n'
               '  accessToken: process.env.SMARTSHEET_ACCESS_TOKEN,\n'
               '})'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=571,
          lineno=17,
          tokens=12,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='sheetId',
          body='sheetId = process.env.SMARTSHEET_SHEET_ID'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=572,
          lineno=19,
          tokens=67,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='columnIds',
          body='columnIds = {\n'
               "  'Site #': process.env.SMARTSHEET_COLUMN_ID_SITE!,\n"
               "  'Customer': process.env.SMARTSHEET_COLUMN_ID_CUSTOMER!,\n"
               "  'Checked_In': process.env.SMARTSHEET_COLUMN_ID_CHECKED_IN!,\n"
               "  'Project Manager': "
               'process.env.SMARTSHEET_COLUMN_ID_PROJECT_MANAGER!,\n'
               '}'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=573,
          lineno=29,
          tokens=16,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='sheet',
          body='sheet = await smartsheet.sheets.getSheet({ id: sheetId })'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=574,
          lineno=30,
          tokens=3,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='rows',
          body='rows = []'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=575,
          lineno=32,
          tokens=16,
          depth=7,
          parent_id=None,
          category='variable',
          summary=False,
          name='siteCell',
          body="siteCell = getCellByColumnId(row, columnIds['Site #'])"),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=576,
          lineno=45,
          tokens=15,
          depth=3,
          parent_id=None,
          category='variable',
          summary=False,
          name='cell',
          body='cell = row.cells.find(cell => cell.columnId === '
               'parseInt(columnId))'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=577,
          lineno=55,
          tokens=24,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='newCell',
          body='newCell: Cell = {\n'
               "      columnId: parseInt(columnIds['Checked_In']),\n"
               '      value: true,\n'
               '    }'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=578,
          lineno=59,
          tokens=21,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='newRow',
          body='newRow: Row = {\n'
               '      id: row.id,\n'
               '      cells: [newCell],\n'
               '    }'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=579,
          lineno=74,
          tokens=24,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='newCell',
          body='newCell: Cell = {\n'
               "      columnId: parseInt(columnIds['Checked_In']),\n"
               '      value: false,\n'
               '    }'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=580,
          lineno=78,
          tokens=21,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='newRow',
          body='newRow: Row = {\n'
               '      id: row.id,\n'
               '      cells: [newCell],\n'
               '    }'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=581,
          lineno=92,
          tokens=36,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='smartsheetHelper',
          body='smartsheetHelper = {\n'
               '  getRowsBySite,\n'
               '  getCellByColumnId,\n'
               '  checkIn,\n'
               '  checkOut,\n'
               '  columnIds,\n'
               '  sheetId,\n'
               '}'),
 Fragment(document_cs='a90fc8f0e0f01c9d82abbff5246080aaa5fdb1b41584bf7e03dca99277546595',
          id=582,
          lineno=1,
          tokens=61,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: checkIn checkOut getCellByColumnId getRowsBySite\n'
               '  Variables: cell columnIds newCell newRow rows sheet sheetId '
               'siteCell smartsheet smartsheetHelper\n'
               '  Usages: Cell Error Promise Row Smartsheet columnId console '
               'error parseInt process row siteNumber\n'),
 Fragment(document_cs='aa96f337977a95ec29d954d2085fe7b26ffb9741f944507f4efb14b7ebd5f24f',
          id=583,
          lineno=1,
          tokens=28,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { FC } from 'react'import Skeleton from "
               "'react-loading-skeleton'import "
               "'react-loading-skeleton/dist/skeleton.css'"),
 Fragment(document_cs='aa96f337977a95ec29d954d2085fe7b26ffb9741f944507f4efb14b7ebd5f24f',
          id=584,
          lineno=5,
          tokens=4,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='loadingProps',
          body='interface loadingProps {}'),
 Fragment(document_cs='aa96f337977a95ec29d954d2085fe7b26ffb9741f944507f4efb14b7ebd5f24f',
          id=585,
          lineno=7,
          tokens=90,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='loading',
          body='loading: FC<loadingProps> = ({}) => {\n'
               '  return (\n'
               "    <div className='w-full flex flex-col gap-3'>\n"
               "      <Skeleton className='mb-4' height={60} width={500} />\n"
               '      <Skeleton height={50} width={350} />\n'
               '      <Skeleton height={50} width={350} />\n'
               '      <Skeleton height={50} width={350} />\n'
               '    </div>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='aa96f337977a95ec29d954d2085fe7b26ffb9741f944507f4efb14b7ebd5f24f',
          id=586,
          lineno=1,
          tokens=22,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: loadingProps\n'
               '  Variables: loading\n'
               '  Usages: FC Skeleton className div height width\n'),
 Fragment(document_cs='aad4bd06d9a865db04e1f9ad3b675444f802389fb33a60b2330e568d8578e548',
          id=587,
          lineno=1,
          tokens=39,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { authOptions } from '@/lib/auth'import { db } from "
               "'@/lib/db'import { getServerSession } from 'next-auth'import { "
               "z } from 'zod'"),
 Fragment(document_cs='aad4bd06d9a865db04e1f9ad3b675444f802389fb33a60b2330e568d8578e548',
          id=588,
          lineno=6,
          tokens=159,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='POST',
          body='async function POST(req: Request) {\n'
               '  try {\n'
               '    const body = await req.json()\n'
               '    const session = await getServerSession(authOptions)\n'
               '\n'
               '    if (!session) {\n'
               "      return new Response('Unauthorized', { status: 401 })\n"
               '    }\n'
               '\n'
               '    const { id: idToDeny } = z.object({ id: z.string() '
               '}).parse(body)\n'
               '\n'
               '    await '
               'db.srem(`user:${session.user.id}:incoming_friend_requests`, '
               'idToDeny)\n'
               '\n'
               "    return new Response('OK')\n"
               '  } catch (error) {\n'
               '    console.log(error)\n'
               '\n'
               '    if (error instanceof z.ZodError) {\n'
               "      return new Response('Invalid request payload', { status: "
               '422 })\n'
               '    }\n'
               '\n'
               "    return new Response('Invalid request', { status: 400 })\n"
               '  }\n'
               '}'),
 Fragment(document_cs='aad4bd06d9a865db04e1f9ad3b675444f802389fb33a60b2330e568d8578e548',
          id=589,
          lineno=8,
          tokens=6,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='body',
          body='body = await req.json()'),
 Fragment(document_cs='aad4bd06d9a865db04e1f9ad3b675444f802389fb33a60b2330e568d8578e548',
          id=590,
          lineno=9,
          tokens=9,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='session',
          body='session = await getServerSession(authOptions)'),
 Fragment(document_cs='aad4bd06d9a865db04e1f9ad3b675444f802389fb33a60b2330e568d8578e548',
          id=591,
          lineno=1,
          tokens=30,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: POST\n'
               '  Variables: body session\n'
               '  Usages: Request Response authOptions console error '
               'getServerSession idToDeny req\n'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=592,
          lineno=1,
          tokens=90,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { fetchRedis } from '@/helpers/redis'import { "
               "authOptions } from '@/lib/auth'import { db } from "
               "'@/lib/db'import { pusherServer } from '@/lib/pusher'import { "
               "toPusherKey } from '@/lib/utils'import { Message, "
               "messageValidator } from '@/lib/validations/message'import { "
               "nanoid } from 'nanoid'import { getServerSession } from "
               "'next-auth'"),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=593,
          lineno=11,
          tokens=170,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='POST',
          body='async function POST(req: Request) {\n'
               '  try {\n'
               '    const { text, chatId }: { text: string; chatId: string } = '
               'await req.json()\n'
               '    const session = await getServerSession(authOptions)\n'
               '\n'
               "    if (!session) return new Response('Unauthorized', { "
               'status: 401 })\n'
               '\n'
               "    const [userId1, userId2] = chatId.split('--')\n"
               '\n'
               '    if (session.user.id !== userId1 && session.user.id !== '
               'userId2) {\n'
               "      return new Response('Unauthorized', { status: 401 })\n"
               '    }\n'
               '\n'
               '    const friendId = session.user.id === userId1 ? userId2 : '
               'userId1\n'
               '\n'
               '    const friendList = (await fetchRedis(\n'
               "      'smembers',\n"
               '      `user:${session.user.id}:friends`\n'
               '    )) as string[]\n'
               '    const isFriend = friendList.includes(friendId)\n'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=594,
          lineno=31,
          tokens=237,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='POST',
          body='\n'
               '    if (!isFriend) {\n'
               "      return new Response('Unauthorized', { status: 401 })\n"
               '    }\n'
               '\n'
               '    const rawSender = (await fetchRedis(\n'
               "      'get',\n"
               '      `user:${session.user.id}`\n'
               '    )) as string\n'
               '    const sender = JSON.parse(rawSender) as User\n'
               '\n'
               '    const timestamp = Date.now()\n'
               '\n'
               '    const messageData: Message = {\n'
               '      id: nanoid(),\n'
               '      senderId: session.user.id,\n'
               '      text,\n'
               '      timestamp,\n'
               '    }\n'
               '\n'
               '    const message = messageValidator.parse(messageData)\n'
               '\n'
               '    // notify all connected chat room clients\n'
               '    await pusherServer.trigger(toPusherKey(`chat:${chatId}`), '
               "'incoming-message', message)\n"
               '\n'
               '    await '
               'pusherServer.trigger(toPusherKey(`user:${friendId}:chats`), '
               "'new_message', {\n"
               '      ...message,\n'
               '      senderImg: sender.image,\n'
               '      senderName: sender.name\n'
               '    })\n'
               '\n'
               '    // all valid, send the message\n'
               '    await db.zadd(`chat:${chatId}:messages`, {\n'
               '      score: timestamp,\n'
               '      member: JSON.stringify(message),\n'
               '    })\n'
               '\n'
               "    return new Response('OK')\n"
               '  } catch (error) {\n'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=595,
          lineno=70,
          tokens=41,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='POST',
          body='    if (error instanceof Error) {\n'
               '      return new Response(error.message, { status: 500 })\n'
               '    }\n'
               '\n'
               "    return new Response('Internal Server Error', { status: 500 "
               '})\n'
               '  }\n'
               '}'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=596,
          lineno=14,
          tokens=9,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='session',
          body='session = await getServerSession(authOptions)'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=597,
          lineno=24,
          tokens=15,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='friendId',
          body='friendId = session.user.id === userId1 ? userId2 : userId1'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=598,
          lineno=26,
          tokens=28,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='friendList',
          body='friendList = (await fetchRedis(\n'
               "      'smembers',\n"
               '      `user:${session.user.id}:friends`\n'
               '    )) as string[]'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=599,
          lineno=30,
          tokens=10,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='isFriend',
          body='isFriend = friendList.includes(friendId)'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=600,
          lineno=36,
          tokens=24,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='rawSender',
          body='rawSender = (await fetchRedis(\n'
               "      'get',\n"
               '      `user:${session.user.id}`\n'
               '    )) as string'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=601,
          lineno=40,
          tokens=9,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='sender',
          body='sender = JSON.parse(rawSender) as User'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=602,
          lineno=42,
          tokens=5,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='timestamp',
          body='timestamp = Date.now()'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=603,
          lineno=44,
          tokens=28,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='messageData',
          body='messageData: Message = {\n'
               '      id: nanoid(),\n'
               '      senderId: session.user.id,\n'
               '      text,\n'
               '      timestamp,\n'
               '    }'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=604,
          lineno=51,
          tokens=8,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='message',
          body='message = messageValidator.parse(messageData)'),
 Fragment(document_cs='ab0cb7c767f9f90f80c0e813b949ba24eff1bbd3feebdd754474e171c012341a',
          id=605,
          lineno=1,
          tokens=61,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: POST\n'
               '  Variables: friendId friendList isFriend message messageData '
               'rawSender sender session timestamp\n'
               '  Usages: Date Error JSON Message Request Response User '
               'authOptions chatId error fetchRedis getServerSession '
               'messageValidator nanoid pusherServer req toPusherKey userId1 '
               'userId2\n'),
 Fragment(document_cs='b0904fdb380273e835ae4fb856af6109d539dc47f9298af988de75dc61486ab9',
          id=606,
          lineno=1,
          tokens=33,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { getToken } from 'next-auth/jwt'import { withAuth } "
               "from 'next-auth/middleware'import { NextResponse } from "
               "'next/server'"),
 Fragment(document_cs='b0904fdb380273e835ae4fb856af6109d539dc47f9298af988de75dc61486ab9',
          id=607,
          lineno=6,
          tokens=160,
          depth=4,
          parent_id=None,
          category='function',
          summary=False,
          name='middleware',
          body='async function middleware(req) {\n'
               '    const pathname = req.nextUrl.pathname\n'
               '\n'
               '    // Manage route protection\n'
               '    const isAuth = await getToken({ req })\n'
               "    const isLoginPage = pathname.startsWith('/login')\n"
               '\n'
               "    const sensitiveRoutes = ['/dashboard']\n"
               '    const isAccessingSensitiveRoute = '
               'sensitiveRoutes.some((route) =>\n'
               '      pathname.startsWith(route)\n'
               '    )\n'
               '\n'
               '    if (isLoginPage) {\n'
               '      if (isAuth) {\n'
               "        return NextResponse.redirect(new URL('/dashboard', "
               'req.url))\n'
               '      }\n'
               '\n'
               '      return NextResponse.next()\n'
               '    }\n'
               '\n'
               '    if (!isAuth && isAccessingSensitiveRoute) {\n'
               "      return NextResponse.redirect(new URL('/login', "
               'req.url))\n'
               '    }\n'
               '\n'
               "    if (pathname === '/') {\n"
               "      return NextResponse.redirect(new URL('/dashboard', "
               'req.url))\n'
               '    }\n'
               '  }'),
 Fragment(document_cs='b0904fdb380273e835ae4fb856af6109d539dc47f9298af988de75dc61486ab9',
          id=608,
          lineno=7,
          tokens=6,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='pathname',
          body='pathname = req.nextUrl.pathname'),
 Fragment(document_cs='b0904fdb380273e835ae4fb856af6109d539dc47f9298af988de75dc61486ab9',
          id=609,
          lineno=10,
          tokens=8,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='isAuth',
          body='isAuth = await getToken({ req })'),
 Fragment(document_cs='b0904fdb380273e835ae4fb856af6109d539dc47f9298af988de75dc61486ab9',
          id=610,
          lineno=11,
          tokens=8,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='isLoginPage',
          body="isLoginPage = pathname.startsWith('/login')"),
 Fragment(document_cs='b0904fdb380273e835ae4fb856af6109d539dc47f9298af988de75dc61486ab9',
          id=611,
          lineno=13,
          tokens=7,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='sensitiveRoutes',
          body="sensitiveRoutes = ['/dashboard']"),
 Fragment(document_cs='b0904fdb380273e835ae4fb856af6109d539dc47f9298af988de75dc61486ab9',
          id=612,
          lineno=14,
          tokens=20,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='isAccessingSensitiveRoute',
          body='isAccessingSensitiveRoute = sensitiveRoutes.some((route) =>\n'
               '      pathname.startsWith(route)\n'
               '    )'),
 Fragment(document_cs='b0904fdb380273e835ae4fb856af6109d539dc47f9298af988de75dc61486ab9',
          id=613,
          lineno=43,
          tokens=19,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='config',
          body='config = {\n'
               "  matchter: ['/', '/login', '/dashboard/:path*'],\n"
               '}'),
 Fragment(document_cs='b0904fdb380273e835ae4fb856af6109d539dc47f9298af988de75dc61486ab9',
          id=614,
          lineno=1,
          tokens=35,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: middleware\n'
               '  Variables: config isAccessingSensitiveRoute isAuth '
               'isLoginPage pathname sensitiveRoutes\n'
               '  Usages: NextResponse URL getToken req route withAuth\n'),
 Fragment(document_cs='be360189fd8f683eff8766c5e6dcecb4e9048cee03090a124c2230e1995394f9',
          id=615,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body='import AddFriendButton from '
               "'@/components/AddFriendButton'import { FC } from 'react'"),
 Fragment(document_cs='be360189fd8f683eff8766c5e6dcecb4e9048cee03090a124c2230e1995394f9',
          id=616,
          lineno=4,
          tokens=55,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='page',
          body='page: FC = () => {\n'
               '  return (\n'
               "    <main className='pt-8'>\n"
               "      <h1 className='font-bold text-5xl mb-8'>Add a "
               'friend</h1>\n'
               '      <AddFriendButton />\n'
               '    </main>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='be360189fd8f683eff8766c5e6dcecb4e9048cee03090a124c2230e1995394f9',
          id=617,
          lineno=1,
          tokens=18,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: page\n'
               '  Usages: Add AddFriendButton FC className friend main\n'),
 Fragment(document_cs='c36d2a2decb57474f6418892c0e006c9ef5548ea9f900f0751e2e6c9b5be99b2',
          id=618,
          lineno=1,
          tokens=28,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { FC } from 'react'import Skeleton from "
               "'react-loading-skeleton'import "
               "'react-loading-skeleton/dist/skeleton.css'"),
 Fragment(document_cs='c36d2a2decb57474f6418892c0e006c9ef5548ea9f900f0751e2e6c9b5be99b2',
          id=619,
          lineno=5,
          tokens=4,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='loadingProps',
          body='interface loadingProps {}'),
 Fragment(document_cs='c36d2a2decb57474f6418892c0e006c9ef5548ea9f900f0751e2e6c9b5be99b2',
          id=620,
          lineno=7,
          tokens=78,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='loading',
          body='loading: FC<loadingProps> = ({}) => {\n'
               '  return (\n'
               "    <div className='w-full flex flex-col gap-3'>\n"
               "      <Skeleton className='mb-4' height={60} width={500} />\n"
               '      <Skeleton height={20} width={150} />\n'
               '      <Skeleton height={50} width={400} />\n'
               '    </div>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='c36d2a2decb57474f6418892c0e006c9ef5548ea9f900f0751e2e6c9b5be99b2',
          id=621,
          lineno=1,
          tokens=22,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: loadingProps\n'
               '  Variables: loading\n'
               '  Usages: FC Skeleton className div height width\n'),
 Fragment(document_cs='c4a48700a2e6751c8a262dfed3edd16cec14193113eeeda6c4f62caee13ac815',
          id=622,
          lineno=1,
          tokens=60,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body='import Auth0Provider from "next-auth/providers/auth0";import { '
               "NextAuthOptions } from 'next-auth'import { UpstashRedisAdapter "
               "} from '@next-auth/upstash-redis-adapter'import { db } from "
               "'./db';import { fetchRedis } from '../helpers/redis';"),
 Fragment(document_cs='c4a48700a2e6751c8a262dfed3edd16cec14193113eeeda6c4f62caee13ac815',
          id=623,
          lineno=20,
          tokens=219,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='authOptions',
          body='authOptions: NextAuthOptions = {\n'
               '  adapter: UpstashRedisAdapter(db),\n'
               '  session: {\n'
               "    strategy: 'jwt',\n"
               '  },\n'
               '\n'
               '  pages: {\n'
               "    signIn: '/login',\n"
               '  },\n'
               '  providers: [\n'
               '    Auth0Provider({\n'
               "      clientId: process.env.AUTH0_CLIENT_ID || '',\n"
               "      clientSecret: process.env.AUTH0_CLIENT_SECRET || '',\n"
               '      issuer: process.env.AUTH0_ISSUER\n'
               '    }),\n'
               '  ],\n'
               '  callbacks: {\n'
               '    async jwt({ token, user }) {\n'
               "      const dbUserResult = (await fetchRedis('get', "
               '`user:${token.id}`)) as\n'
               '        | string\n'
               '        | null\n'
               '\n'
               '      if (!dbUserResult) {\n'
               '        if (user) {\n'
               '          token.id = user!.id\n'
               '        }\n'
               '\n'
               '        return token\n'
               '      }\n'
               '\n'
               '      const dbUser = JSON.parse(dbUserResult) as User\n'
               '\n'
               '      return {\n'
               '        id: dbUser.id,\n'
               '        name: dbUser.name,\n'
               '        email: dbUser.email,\n'
               '        picture: dbUser.image,\n'
               '      }\n'
               '    },\n'
               '    async session({ session, token }) {\n'),
 Fragment(document_cs='c4a48700a2e6751c8a262dfed3edd16cec14193113eeeda6c4f62caee13ac815',
          id=624,
          lineno=38,
          tokens=27,
          depth=9,
          parent_id=None,
          category='variable',
          summary=False,
          name='dbUserResult',
          body="dbUserResult = (await fetchRedis('get', `user:${token.id}`)) "
               'as\n'
               '        | string\n'
               '        | null'),
 Fragment(document_cs='c4a48700a2e6751c8a262dfed3edd16cec14193113eeeda6c4f62caee13ac815',
          id=625,
          lineno=50,
          tokens=11,
          depth=9,
          parent_id=None,
          category='variable',
          summary=False,
          name='dbUser',
          body='dbUser = JSON.parse(dbUserResult) as User'),
 Fragment(document_cs='c4a48700a2e6751c8a262dfed3edd16cec14193113eeeda6c4f62caee13ac815',
          id=626,
          lineno=60,
          tokens=58,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='authOptions',
          body='      if (token) {\n'
               '        session.user.id = token.id\n'
               '        session.user.name = token.name\n'
               '        session.user.email = token.email\n'
               '        session.user.image = token.picture\n'
               '      }\n'
               '\n'
               '      return session\n'
               '    },\n'
               '    // remove the redirect callback from here\n'
               '  },\n'
               '}'),
 Fragment(document_cs='c4a48700a2e6751c8a262dfed3edd16cec14193113eeeda6c4f62caee13ac815',
          id=627,
          lineno=1,
          tokens=35,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: authOptions dbUser dbUserResult\n'
               '  Usages: Auth0Provider JSON NextAuthOptions Profile '
               'UpstashRedisAdapter User fetchRedis process session token '
               'user\n'),
 Fragment(document_cs='c5e5c7404936db6038bec2b6f01e122018bde47f88ca524a91371dba7886f0fe',
          id=628,
          lineno=1,
          tokens=25,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { ClassValue, clsx } from 'clsx'import { twMerge } from "
               "'tailwind-merge'"),
 Fragment(document_cs='c5e5c7404936db6038bec2b6f01e122018bde47f88ca524a91371dba7886f0fe',
          id=629,
          lineno=4,
          tokens=18,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='cn',
          body='function cn(...inputs: ClassValue[]) {\n'
               '  return twMerge(clsx(inputs))\n'
               '}'),
 Fragment(document_cs='c5e5c7404936db6038bec2b6f01e122018bde47f88ca524a91371dba7886f0fe',
          id=630,
          lineno=8,
          tokens=21,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='toPusherKey',
          body='function toPusherKey(key: string) {\n'
               "  return key.replace(/:/g, '__')\n"
               '}'),
 Fragment(document_cs='c5e5c7404936db6038bec2b6f01e122018bde47f88ca524a91371dba7886f0fe',
          id=631,
          lineno=12,
          tokens=46,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='chatHrefConstructor',
          body='function chatHrefConstructor(id1: string, id2: string) {\n'
               '  const sortedIds = [id1, id2].sort()\n'
               '  return `${sortedIds[0]}--${sortedIds[1]}`\n'
               '}'),
 Fragment(document_cs='c5e5c7404936db6038bec2b6f01e122018bde47f88ca524a91371dba7886f0fe',
          id=632,
          lineno=13,
          tokens=12,
          depth=4,
          parent_id=None,
          category='variable',
          summary=False,
          name='sortedIds',
          body='sortedIds = [id1, id2].sort()'),
 Fragment(document_cs='c5e5c7404936db6038bec2b6f01e122018bde47f88ca524a91371dba7886f0fe',
          id=633,
          lineno=1,
          tokens=35,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Functions: chatHrefConstructor cn toPusherKey\n'
               '  Variables: sortedIds\n'
               '  Usages: ClassValue clsx id1 id2 inputs key twMerge\n'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=634,
          lineno=2,
          tokens=62,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { NextApiRequest, NextApiResponse } from 'next';import "
               "smartsheetHelper from '../../helpers/smartsheetHelper';import "
               "chatHelper from '../../helpers/chatHelper';import { getSession "
               "} from 'next-auth/react';import { Session } from "
               "'next-auth';import Pusher from 'pusher';"),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=635,
          lineno=24,
          tokens=98,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='handleCheckIn',
          body='async function handleCheckIn(req: NextApiRequest, res: '
               'NextApiResponse) {\n'
               '  try {\n'
               '    const session = await getSession({ req }) as '
               'ExtendedSession;\n'
               '    const siteNumber = req.body.siteNumber;\n'
               '    const rows = await '
               'smartsheetHelper.getRowsBySite(siteNumber);\n'
               '\n'
               '    if (rows.length > 1) {\n'
               '      const customers = rows.map(row => '
               'smartsheetHelper.getCellByColumnId(row, '
               "smartsheetHelper.columnIds['Customer']).value);\n"),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=636,
          lineno=32,
          tokens=166,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='handleCheckIn',
          body='      if (session) {\n'
               "        session.state = 'awaiting_customer_selection';\n"
               '        session.siteNumber = siteNumber;\n'
               '      }\n'
               '      res.json({\n'
               '        response: `There are multiple customers associated '
               'with Site # ${siteNumber}. Please select a customer:`,\n'
               '        multipleCustomers: customers\n'
               '      });\n'
               '    } else if (rows.length === 1) {\n'
               '      const siteCell = '
               'smartsheetHelper.getCellByColumnId(rows[0], '
               "smartsheetHelper.columnIds['Site #']);\n"
               '      const customer = '
               'smartsheetHelper.getCellByColumnId(rows[0], '
               "smartsheetHelper.columnIds['Customer']).value;\n"
               '      await smartsheetHelper.checkIn(rows[0]);\n'
               "      session.state = 'checked_in';\n"
               '      session.siteNumber = siteNumber;\n'
               '      session.customer = customer;\n'
               '\n'
               '      // Send a chat '),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=637,
          lineno=48,
          tokens=170,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='handleCheckIn',
          body='support message\n'
               '      const projectManagerEmail = '
               'smartsheetHelper.getCellByColumnId(rows[0], '
               "smartsheetHelper.columnIds['Project Manager']).value;\n"
               '      const message = `A technician has Checked In using Macro '
               'Integrations AI Assistant at Site # ${session.siteNumber} for '
               "${session.customer} at ${new Date().toLocaleString('en-US', { "
               "timeZone: 'America/New_York' })}.`;\n"
               '      await sendChatSupport(projectManagerEmail, message);\n'
               '\n'
               '      res.send(`Successfully checked in to Site # '
               '${parseInt(siteCell.value)}.`);\n'
               '    } else {\n'
               '      res.send(`No site found with number ${siteNumber}.`);\n'
               '    }\n'
               '  } catch (error) {\n'
               '    console.error(`Error handling check in: ${error}`);\n'
               "    res.status(500).send('An error occurred while checking "
               "in.');\n"
               '  }\n'
               '}'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=638,
          lineno=63,
          tokens=181,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='sendChatSupport',
          body='async function sendChatSupport(email: string, message: string) '
               '{\n'
               '  try {\n'
               '    // Find the Project Manager user in your application\n'
               '    const projectManagerUser = await findUserByEmail(email);\n'
               '\n'
               '    if (projectManagerUser) {\n'
               '      // Send a chat support message to the Project Manager\n'
               '      const chatMessage = {\n'
               "        senderId: 'MI-AI',  // The ID of the MI-AI bot/user\n"
               '        recipientId: projectManagerUser.id,\n'
               '        text: message,\n'
               '        timestamp: new Date().toISOString(),\n'
               '      };\n'
               '\n'
               '      // Save the chat message in Redis\n'
               '      const response = await '
               'fetch(`${process.env.UPSTASH_REDIS_REST_URL}/lpush/chat:${projectManagerUser.id}`, '
               '{\n'
               "        method: 'POST',\n"
               '        headers: {\n'
               "          'Content-Type': 'application/json'\n"
               '        },\n'
               '        body: JSON.stringify({ value: chatMessage })\n'
               '      });\n'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=639,
          lineno=85,
          tokens=88,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='sendChatSupport',
          body='\n'
               '      if (!response.ok) {\n'
               "        throw new Error('Failed to save chat message in "
               "Redis');\n"
               '      }\n'
               '\n'
               '      // Trigger a Pusher event to update the chat in real '
               'time\n'
               '      '
               'chatHelper.pusher.trigger(`chat-${projectManagerUser.id}`, '
               "'new-message', chatMessage);\n"
               '    }\n'
               '  } catch (error) {\n'
               '    console.error(`Error sending chat support message: '
               '${error}`);\n'
               '    throw error;\n'
               '  }\n'
               '}'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=640,
          lineno=99,
          tokens=221,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='findUserByEmail',
          body='async function findUserByEmail(email: string) {\n'
               '  // Get all user keys\n'
               '  const response = await '
               'fetch(`${process.env.UPSTASH_REDIS_REST_URL}/keys/user:*`, {\n'
               "    method: 'GET',\n"
               '    headers: {\n'
               "      'Content-Type': 'application/json'\n"
               '    }\n'
               '  });\n'
               '\n'
               '  if (!response.ok) {\n'
               "    throw new Error('Failed to get user keys from Redis');\n"
               '  }\n'
               '\n'
               '  const userKeys = await response.json();\n'
               '\n'
               '  // Iterate over the user keys and find the user with the '
               'matching email\n'
               '  for (const userKey of userKeys) {\n'
               '    const userResponse = await '
               'fetch(`${process.env.UPSTASH_REDIS_REST_URL}/get/${userKey}`, '
               '{\n'
               "      method: 'GET',\n"
               '      headers: {\n'
               "        'Content-Type': 'application/json'\n"
               '      }\n'
               '    });\n'
               '\n'
               '    if (!userResponse.ok) {\n'
               "      throw new Error('Failed to get user from Redis');\n"
               '    }\n'
               '\n'
               '    const user = await userResponse.json();\n'
               '    if (user.email === email) {\n'
               '      return user;\n'
               '    }\n'
               '  }  \n'
               '\n'
               '  return null;\n'
               '}'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=641,
          lineno=18,
          tokens=23,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='ExtendedSession',
          body='interface ExtendedSession extends Session {\n'
               '  state?: string;\n'
               '  siteNumber?: string;\n'
               '  customer?: string;\n'
               '}'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=642,
          lineno=9,
          tokens=59,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='pusher',
          body='pusher = new Pusher({\n'
               '     appId: process.env.PUSHER_APP_ID!,\n'
               '     key: process.env.PUSHER_APP_KEY!,\n'
               '     secret: process.env.PUSHER_APP_SECRET!,\n'
               '     cluster: process.env.PUSHER_APP_CLUSTER!,\n'
               '     useTLS: true,\n'
               '   })'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=643,
          lineno=26,
          tokens=10,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='session',
          body='session = await getSession({ req }) as ExtendedSession'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=644,
          lineno=27,
          tokens=7,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='siteNumber',
          body='siteNumber = req.body.siteNumber'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=645,
          lineno=28,
          tokens=14,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='rows',
          body='rows = await smartsheetHelper.getRowsBySite(siteNumber)'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=646,
          lineno=31,
          tokens=27,
          depth=8,
          parent_id=None,
          category='variable',
          summary=False,
          name='customers',
          body='customers = rows.map(row => '
               'smartsheetHelper.getCellByColumnId(row, '
               "smartsheetHelper.columnIds['Customer']).value)"),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=647,
          lineno=41,
          tokens=25,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='siteCell',
          body='siteCell = smartsheetHelper.getCellByColumnId(rows[0], '
               "smartsheetHelper.columnIds['Site #'])"),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=648,
          lineno=42,
          tokens=24,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='customer',
          body='customer = smartsheetHelper.getCellByColumnId(rows[0], '
               "smartsheetHelper.columnIds['Customer']).value"),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=649,
          lineno=49,
          tokens=27,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='projectManagerEmail',
          body='projectManagerEmail = '
               'smartsheetHelper.getCellByColumnId(rows[0], '
               "smartsheetHelper.columnIds['Project Manager']).value"),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=650,
          lineno=50,
          tokens=50,
          depth=10,
          parent_id=None,
          category='variable',
          summary=False,
          name='message',
          body='message = `A technician has Checked In using Macro '
               'Integrations AI Assistant at Site # ${session.siteNumber} for '
               "${session.customer} at ${new Date().toLocaleString('en-US', { "
               "timeZone: 'America/New_York' })}.`"),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=651,
          lineno=66,
          tokens=10,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='projectManagerUser',
          body='projectManagerUser = await findUserByEmail(email)'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=652,
          lineno=70,
          tokens=49,
          depth=7,
          parent_id=None,
          category='variable',
          summary=False,
          name='chatMessage',
          body='chatMessage = {\n'
               "        senderId: 'MI-AI',  // The ID of the MI-AI bot/user\n"
               '        recipientId: projectManagerUser.id,\n'
               '        text: message,\n'
               '        timestamp: new Date().toISOString(),\n'
               '      }'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=653,
          lineno=78,
          tokens=59,
          depth=7,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body='response = await '
               'fetch(`${process.env.UPSTASH_REDIS_REST_URL}/lpush/chat:${projectManagerUser.id}`, '
               '{\n'
               "        method: 'POST',\n"
               '        headers: {\n'
               "          'Content-Type': 'application/json'\n"
               '        },\n'
               '        body: JSON.stringify({ value: chatMessage })\n'
               '      })'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=654,
          lineno=101,
          tokens=43,
          depth=3,
          parent_id=None,
          category='variable',
          summary=False,
          name='response',
          body='response = await '
               'fetch(`${process.env.UPSTASH_REDIS_REST_URL}/keys/user:*`, {\n'
               "    method: 'GET',\n"
               '    headers: {\n'
               "      'Content-Type': 'application/json'\n"
               '    }\n'
               '  })'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=655,
          lineno=112,
          tokens=7,
          depth=3,
          parent_id=None,
          category='variable',
          summary=False,
          name='userKeys',
          body='userKeys = await response.json()'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=656,
          lineno=116,
          tokens=45,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='userResponse',
          body='userResponse = await '
               'fetch(`${process.env.UPSTASH_REDIS_REST_URL}/get/${userKey}`, '
               '{\n'
               "      method: 'GET',\n"
               '      headers: {\n'
               "        'Content-Type': 'application/json'\n"
               '      }\n'
               '    })'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=657,
          lineno=127,
          tokens=7,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='user',
          body='user = await userResponse.json()'),
 Fragment(document_cs='ca6f656679213811076b558c080bfddc38fc5497e27dce8a1dd53eb8df975cf5',
          id=658,
          lineno=1,
          tokens=82,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: ExtendedSession\n'
               '  Functions: findUserByEmail handleCheckIn sendChatSupport\n'
               '  Variables: chatMessage customer customers message '
               'projectManagerEmail projectManagerUser pusher response rows '
               'session siteCell siteNumber user userKeys userResponse\n'
               '  Usages: Date Error JSON NextApiRequest NextApiResponse '
               'Pusher Session chatHelper console email error fetch getSession '
               'parseInt process req res row smartsheetHelper userKey\n'),
 Fragment(document_cs='daaeddf39311b8395dd09cb46fac5c7bf5e77e77921adb886579f1b81d27ec39',
          id=659,
          lineno=3,
          tokens=50,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import axios from 'axios'import { FC, useRef, useState } from "
               "'react'import { toast } from 'react-hot-toast'import "
               "TextareaAutosize from 'react-textarea-autosize'import Button "
               "from './ui/Button'"),
 Fragment(document_cs='daaeddf39311b8395dd09cb46fac5c7bf5e77e77921adb886579f1b81d27ec39',
          id=660,
          lineno=9,
          tokens=18,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='ChatInputProps',
          body='interface ChatInputProps {\n'
               '  chatPartner: User\n'
               '  chatId: string\n'
               '}'),
 Fragment(document_cs='daaeddf39311b8395dd09cb46fac5c7bf5e77e77921adb886579f1b81d27ec39',
          id=661,
          lineno=15,
          tokens=12,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='textareaRef',
          body='textareaRef = useRef<HTMLTextAreaElement | null>(null)'),
 Fragment(document_cs='daaeddf39311b8395dd09cb46fac5c7bf5e77e77921adb886579f1b81d27ec39',
          id=662,
          lineno=19,
          tokens=78,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='sendMessage',
          body='sendMessage = async () => {\n'
               '    if(!input) return\n'
               '    setIsLoading(true)\n'
               '\n'
               '    try {\n'
               "      await axios.post('/api/message/send', { text: input, "
               'chatId })\n'
               "      setInput('')\n"
               '      textareaRef.current?.focus()\n'
               '    } catch {\n'
               "      toast.error('Something went wrong. Please try again "
               "later.')\n"
               '    } finally {\n'
               '      setIsLoading(false)\n'
               '    }\n'
               '  }'),
 Fragment(document_cs='daaeddf39311b8395dd09cb46fac5c7bf5e77e77921adb886579f1b81d27ec39',
          id=663,
          lineno=1,
          tokens=55,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: ChatInputProps\n'
               '  Variables: sendMessage textareaRef\n'
               '  Usages: Button ChatInput FC HTMLTextAreaElement Post '
               'TextareaAutosize User aria axios chatPartner className default '
               'div hidden input isLoading onChange onClick onKeyDown '
               'placeholder ref rows setInput setIsLoading toast useRef '
               'useState\n'),
 Fragment(document_cs='dd5172c6a0e7df3515a32a947af18c170758a23e49ecead9244ba43f2294562e',
          id=664,
          lineno=3,
          tokens=75,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { pusherClient } from '@/lib/pusher'import { "
               "chatHrefConstructor, toPusherKey } from '@/lib/utils'import { "
               "usePathname, useRouter } from 'next/navigation'import { FC, "
               "useEffect, useState } from 'react'import { toast } from "
               "'react-hot-toast'import UnseenChatToast from "
               "'./UnseenChatToast'"),
 Fragment(document_cs='dd5172c6a0e7df3515a32a947af18c170758a23e49ecead9244ba43f2294562e',
          id=665,
          lineno=10,
          tokens=17,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='SidebarChatListProps',
          body='interface SidebarChatListProps {\n'
               '  friends: User[]\n'
               '  sessionId: string\n'
               '}'),
 Fragment(document_cs='dd5172c6a0e7df3515a32a947af18c170758a23e49ecead9244ba43f2294562e',
          id=666,
          lineno=15,
          tokens=19,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='ExtendedMessage',
          body='interface ExtendedMessage extends Message {\n'
               '  senderImg: string\n'
               '  senderName: string\n'
               '}'),
 Fragment(document_cs='dd5172c6a0e7df3515a32a947af18c170758a23e49ecead9244ba43f2294562e',
          id=667,
          lineno=21,
          tokens=4,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='router',
          body='router = useRouter()'),
 Fragment(document_cs='dd5172c6a0e7df3515a32a947af18c170758a23e49ecead9244ba43f2294562e',
          id=668,
          lineno=22,
          tokens=6,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='pathname',
          body='pathname = usePathname()'),
 Fragment(document_cs='dd5172c6a0e7df3515a32a947af18c170758a23e49ecead9244ba43f2294562e',
          id=669,
          lineno=30,
          tokens=39,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='newFriendHandler',
          body='newFriendHandler = (newFriend: User) => {\n'
               '      console.log("received new user", newFriend)\n'
               '      setActiveChats((prev) => [...prev, newFriend])\n'
               '    }'),
 Fragment(document_cs='dd5172c6a0e7df3515a32a947af18c170758a23e49ecead9244ba43f2294562e',
          id=670,
          lineno=36,
          tokens=23,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='shouldNotify',
          body='shouldNotify =\n'
               '        pathname !==\n'
               '        `/dashboard/chat/${chatHrefConstructor(sessionId, '
               'message.senderId)}`'),
 Fragment(document_cs='dd5172c6a0e7df3515a32a947af18c170758a23e49ecead9244ba43f2294562e',
          id=671,
          lineno=80,
          tokens=28,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='unseenMessagesCount',
          body='unseenMessagesCount = unseenMessages.filter((unseenMsg) => {\n'
               '          return unseenMsg.senderId === friend.id\n'
               '        }).length'),
 Fragment(document_cs='dd5172c6a0e7df3515a32a947af18c170758a23e49ecead9244ba43f2294562e',
          id=672,
          lineno=1,
          tokens=97,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: ExtendedMessage SidebarChatListProps\n'
               '  Variables: newFriendHandler pathname router shouldNotify '
               'unseenMessagesCount\n'
               '  Usages: FC Message SidebarChatList UnseenChatToast User '
               'activeChats chatHandler chatHrefConstructor className console '
               'default div friend friends href key message msg name newFriend '
               'prev pusherClient return role senderId senderImg senderMessage '
               'senderName sessionId setActiveChats setUnseenMessages '
               'toPusherKey toast unseenMessages unseenMsg useEffect '
               'usePathname useRouter useState\n'),
 Fragment(document_cs='dfdf41beed0ae4945454412d7787a6aefd7c986dca10b3e3f72361219c9b477f',
          id=673,
          lineno=3,
          tokens=78,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body='import { addFriendValidator } from '
               "'@/lib/validations/add-friend'import axios, { AxiosError } "
               "from 'axios'import { FC, useState } from 'react'import Button "
               "from './ui/Button'import { z } from 'zod'import { useForm } "
               "from 'react-hook-form'import { zodResolver } from "
               "'@hookform/resolvers/zod'"),
 Fragment(document_cs='dfdf41beed0ae4945454412d7787a6aefd7c986dca10b3e3f72361219c9b477f',
          id=674,
          lineno=11,
          tokens=6,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='AddFriendButtonProps',
          body='interface AddFriendButtonProps {}'),
 Fragment(document_cs='dfdf41beed0ae4945454412d7787a6aefd7c986dca10b3e3f72361219c9b477f',
          id=675,
          lineno=27,
          tokens=130,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='addFriend',
          body='addFriend = async (email: string) => {\n'
               '    try {\n'
               '      const validatedEmail = addFriendValidator.parse({ email '
               '})\n'
               '\n'
               "      await axios.post('/api/friends/add', {\n"
               '        email: validatedEmail,\n'
               '      })\n'
               '\n'
               '      setShowSuccessState(true)\n'
               '    } catch (error) {\n'
               '      if (error instanceof z.ZodError) {\n'
               "        setError('email', { message: error.message })\n"
               '        return\n'
               '      }\n'
               '\n'
               '      if (error instanceof AxiosError) {\n'
               "        setError('email', { message: error.response?.data })\n"
               '        return\n'
               '      }\n'
               '\n'
               "      setError('email', { message: 'Something went wrong.' })\n"
               '    }\n'
               '  }'),
 Fragment(document_cs='dfdf41beed0ae4945454412d7787a6aefd7c986dca10b3e3f72361219c9b477f',
          id=676,
          lineno=29,
          tokens=10,
          depth=7,
          parent_id=None,
          category='variable',
          summary=False,
          name='validatedEmail',
          body='validatedEmail = addFriendValidator.parse({ email })'),
 Fragment(document_cs='dfdf41beed0ae4945454412d7787a6aefd7c986dca10b3e3f72361219c9b477f',
          id=677,
          lineno=51,
          tokens=18,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='onSubmit',
          body='onSubmit = (data: FormData) => {\n'
               '    addFriend(data.email)\n'
               '  }'),
 Fragment(document_cs='dfdf41beed0ae4945454412d7787a6aefd7c986dca10b3e3f72361219c9b477f',
          id=678,
          lineno=1,
          tokens=66,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: AddFriendButtonProps\n'
               '  Variables: addFriend onSubmit validatedEmail\n'
               '  Usages: Add AddFriendButton AxiosError Button E FC FormData '
               'Friend Mail addFriendValidator axios className data default '
               'div email error form friend htmlFor infer input label '
               'placeholder register request sent setError setShowSuccessState '
               'showSuccessState useForm useState zodResolver\n'),
 Fragment(document_cs='e34088d8510089d4d3f6a51daa57d3bba8917171d20d1a98ad391ced123112e4',
          id=679,
          lineno=1,
          tokens=17,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { FC } from 'react'import Skeleton from "
               '"react-loading-skeleton"'),
 Fragment(document_cs='e34088d8510089d4d3f6a51daa57d3bba8917171d20d1a98ad391ced123112e4',
          id=680,
          lineno=4,
          tokens=4,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='loadingProps',
          body='interface loadingProps {}'),
 Fragment(document_cs='e34088d8510089d4d3f6a51daa57d3bba8917171d20d1a98ad391ced123112e4',
          id=681,
          lineno=6,
          tokens=231,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='loading',
          body='loading: FC<loadingProps> = ({}) => {\n'
               '  return (\n'
               "<div className='flex flex-col h-full items-center'>\n"
               "      <Skeleton className='mb-4' height={40} width={400} />\n"
               '      {/* chat messages */}\n'
               "      <div className='flex-1 max-h-full overflow-y-scroll "
               "w-full'>\n"
               "        <div className='flex flex-col flex-auto h-full p-6'>\n"
               "          <div className='flex flex-col flex-auto "
               "flex-shrink-0 rounded-2xl bg-gray-50 h-full p-4'>\n"
               "            <div className='flex flex-col h-full "
               "overflow-x-auto mb-4'>\n"
               "              <div className='flex flex-col h-full'>\n"
               "                <div className='grid grid-cols-12 gap-y-2'>\n"
               "                  <div className='col-start-6 col-end-13 p-3 "
               "rounded-lg'>\n"
               "                    <div className='flex items-center "
               "justify-start flex-row-reverse'>\n"
               "                      <div className='relative h-10 w-10'>\n"
               '                        <Skeleton width={40} height={40} '
               'borderRadius={999} />\n'
               '                      </div>\n'
               "                      <div className='relative mr-3 "),
 Fragment(document_cs='e34088d8510089d4d3f6a51daa57d3bba8917171d20d1a98ad391ced123112e4',
          id=682,
          lineno=22,
          tokens=207,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='loading',
          body='text-sm bg-indigo-100 text-black py-2 px-4 border '
               "border-gray-100 rounded-xl'>\n"
               "                        <Skeleton className='ml-2' width={150} "
               'height={20} />\n'
               '                      </div>\n'
               '                    </div>\n'
               '                  </div>\n'
               "                  <div className='col-start-6 col-end-13 p-3 "
               "rounded-lg'>\n"
               "                    <div className='flex items-center "
               "justify-start flex-row-reverse'>\n"
               "                      <div className='relative h-10 w-10'>\n"
               '                        <Skeleton width={40} height={40} '
               'borderRadius={999} />\n'
               '                      </div>\n'
               "                      <div className='relative mr-3 text-sm "
               'bg-indigo-100 text-black py-2 px-4 border border-gray-100 '
               "rounded-xl'>\n"
               "                        <Skeleton className='ml-2' width={150} "
               'height={20} />\n'
               '                      </div>\n'
               '                    </div>\n'
               '                  </div>\n'
               '\n'
               '                  {/* my messages */}\n'
               "                  <div className='col-start-1 col-end-8 p-3 "
               "rounded-lg'>\n"
               '              '),
 Fragment(document_cs='e34088d8510089d4d3f6a51daa57d3bba8917171d20d1a98ad391ced123112e4',
          id=683,
          lineno=40,
          tokens=205,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='loading',
          body="      <div className='flex flex-row items-center'>\n"
               "                      <div className='relative h-10 w-10'>\n"
               '                        <Skeleton width={40} height={40} '
               'borderRadius={999} />\n'
               '                      </div>\n'
               "                      <div className='relative ml-3 text-sm "
               "bg-white py-2 px-4 border border-gray-100 rounded-xl'>\n"
               "                        <Skeleton className='ml-2' width={150} "
               'height={20} />\n'
               '                      </div>\n'
               '                    </div>\n'
               '                  </div>\n'
               "                  <div className='col-start-6 col-end-13 p-3 "
               "rounded-lg'>\n"
               "                    <div className='flex items-center "
               "justify-start flex-row-reverse'>\n"
               "                      <div className='relative h-10 w-10'>\n"
               '                        <Skeleton width={40} height={40} '
               'borderRadius={999} />\n'
               '                      </div>\n'
               "                      <div className='relative mr-3 text-sm "
               'bg-indigo-100 text-black py-2 px-4 border border-gray-100 '
               "rounded-xl'>\n"
               '                        <Skelet'),
 Fragment(document_cs='e34088d8510089d4d3f6a51daa57d3bba8917171d20d1a98ad391ced123112e4',
          id=684,
          lineno=55,
          tokens=215,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='loading',
          body="on className='ml-2' width={150} height={20} />\n"
               '                      </div>\n'
               '                    </div>\n'
               '                  </div>\n'
               "                  <div className='col-start-1 col-end-8 p-3 "
               "rounded-lg'>\n"
               "                    <div className='flex flex-row "
               "items-center'>\n"
               "                      <div className='relative h-10 w-10'>\n"
               '                        <Skeleton width={40} height={40} '
               'borderRadius={999} />\n'
               '                      </div>\n'
               "                      <div className='relative ml-3 text-sm "
               "bg-white py-2 px-4 border border-gray-100 rounded-xl'>\n"
               "                        <Skeleton className='ml-2' width={150} "
               'height={20} />\n'
               '                      </div>\n'
               '                    </div>\n'
               '                  </div>\n'
               '                </div>\n'
               '              </div>\n'
               '            </div>\n'
               '          </div>\n'
               '        </div>\n'
               '      </div>\n'
               '\n'
               '      {/* chat input */}\n'
               '\n'
               '      {/* <ChatInput\n'
               '        chatPartner={chatPartner}\n'
               '        img={session.user.image}\n'
               '        chatId={chatId}\n'
               '      /> */}\n'
               '    </div>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='e34088d8510089d4d3f6a51daa57d3bba8917171d20d1a98ad391ced123112e4',
          id=685,
          lineno=1,
          tokens=22,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: loadingProps\n'
               '  Variables: loading\n'
               '  Usages: FC Skeleton className div height width\n'),
 Fragment(document_cs='e4ec11c537dbed34611021092e3630f1dfa27b2fab94a45535eb8e8846c9aa65',
          id=686,
          lineno=3,
          tokens=22,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { FC, ReactNode } from 'react'import { Toaster } from "
               "'react-hot-toast'"),
 Fragment(document_cs='e4ec11c537dbed34611021092e3630f1dfa27b2fab94a45535eb8e8846c9aa65',
          id=687,
          lineno=6,
          tokens=11,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='ProvidersProps',
          body='interface ProvidersProps {\n  children: ReactNode\n}'),
 Fragment(document_cs='e4ec11c537dbed34611021092e3630f1dfa27b2fab94a45535eb8e8846c9aa65',
          id=688,
          lineno=10,
          tokens=42,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='Providers',
          body='Providers: FC<ProvidersProps> = ({ children }) => {\n'
               '  return (\n'
               '    <>\n'
               "      <Toaster position='top-center' reverseOrder={false} />\n"
               '      {children}\n'
               '    </>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='e4ec11c537dbed34611021092e3630f1dfa27b2fab94a45535eb8e8846c9aa65',
          id=689,
          lineno=1,
          tokens=24,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: ProvidersProps\n'
               '  Variables: Providers\n'
               '  Usages: FC ReactNode Toaster position reverseOrder\n'),
 Fragment(document_cs='e4f3730c420fd4f9cd7c50731356b85ead5d4b8d38e6b8942793c04b3895bb1c',
          id=690,
          lineno=1,
          tokens=9,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { fetchRedis } from './redis'"),
 Fragment(document_cs='e4f3730c420fd4f9cd7c50731356b85ead5d4b8d38e6b8942793c04b3895bb1c',
          id=691,
          lineno=3,
          tokens=133,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='getFriendsByUserId',
          body='getFriendsByUserId = async (userId: string) => {\n'
               '  // retrieve friends for current user\n'
               '  console.log("userid", userId)\n'
               '  const friendIds = (await fetchRedis(\n'
               "    'smembers',\n"
               '    `user:${userId}:friends`\n'
               '  )) as string[]\n'
               '  console.log("friend ids", friendIds)\n'
               '\n'
               '  const friends = await Promise.all(\n'
               '    friendIds.map(async (friendId) => {\n'
               "      const friend = await fetchRedis('get', "
               '`user:${friendId}`) as string\n'
               '      const parsedFriend = JSON.parse(friend) as User\n'
               '      return parsedFriend\n'
               '    })\n'
               '  )\n'
               '\n'
               '  return friends\n'
               '}'),
 Fragment(document_cs='e4f3730c420fd4f9cd7c50731356b85ead5d4b8d38e6b8942793c04b3895bb1c',
          id=692,
          lineno=6,
          tokens=26,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='friendIds',
          body='friendIds = (await fetchRedis(\n'
               "    'smembers',\n"
               '    `user:${userId}:friends`\n'
               '  )) as string[]'),
 Fragment(document_cs='e4f3730c420fd4f9cd7c50731356b85ead5d4b8d38e6b8942793c04b3895bb1c',
          id=693,
          lineno=12,
          tokens=59,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='friends',
          body='friends = await Promise.all(\n'
               '    friendIds.map(async (friendId) => {\n'
               "      const friend = await fetchRedis('get', "
               '`user:${friendId}`) as string\n'
               '      const parsedFriend = JSON.parse(friend) as User\n'
               '      return parsedFriend\n'
               '    })\n'
               '  )'),
 Fragment(document_cs='e4f3730c420fd4f9cd7c50731356b85ead5d4b8d38e6b8942793c04b3895bb1c',
          id=694,
          lineno=14,
          tokens=17,
          depth=15,
          parent_id=None,
          category='variable',
          summary=False,
          name='friend',
          body="friend = await fetchRedis('get', `user:${friendId}`) as string"),
 Fragment(document_cs='e4f3730c420fd4f9cd7c50731356b85ead5d4b8d38e6b8942793c04b3895bb1c',
          id=695,
          lineno=15,
          tokens=10,
          depth=15,
          parent_id=None,
          category='variable',
          summary=False,
          name='parsedFriend',
          body='parsedFriend = JSON.parse(friend) as User'),
 Fragment(document_cs='e4f3730c420fd4f9cd7c50731356b85ead5d4b8d38e6b8942793c04b3895bb1c',
          id=696,
          lineno=1,
          tokens=28,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: friend friendIds friends getFriendsByUserId '
               'parsedFriend\n'
               '  Usages: JSON Promise User console fetchRedis friendId '
               'userId\n'),
 Fragment(document_cs='e6704173d2a0679fe9888cd94550777700bb4c50c80c1576d541d7b4c654eeab',
          id=697,
          lineno=1,
          tokens=19,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import PusherServer from 'pusher'import PusherClient from "
               "'pusher-js'"),
 Fragment(document_cs='e6704173d2a0679fe9888cd94550777700bb4c50c80c1576d541d7b4c654eeab',
          id=698,
          lineno=4,
          tokens=60,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='pusherServer',
          body='pusherServer = new PusherServer({\n'
               '  appId: process.env.PUSHER_APP_ID!,\n'
               '  key: process.env.PUSHER_APP_KEY!,\n'
               '  secret: process.env.PUSHER_APP_SECRET!,\n'
               '  cluster: process.env.PUSHER_APP_CLUSTER!,\n'
               '  useTLS: true,\n'
               '})'),
 Fragment(document_cs='e6704173d2a0679fe9888cd94550777700bb4c50c80c1576d541d7b4c654eeab',
          id=699,
          lineno=12,
          tokens=33,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='pusherClient',
          body='pusherClient = new PusherClient(\n'
               '  process.env.NEXT_PUBLIC_PUSHER_APP_KEY!,\n'
               '  {\n'
               "    cluster: 'mt1',\n"
               '  }\n'
               ')'),
 Fragment(document_cs='e6704173d2a0679fe9888cd94550777700bb4c50c80c1576d541d7b4c654eeab',
          id=700,
          lineno=1,
          tokens=22,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: pusherClient pusherServer\n'
               '  Usages: PusherClient PusherServer process\n'),
 Fragment(document_cs='ec5e157fccbaceea7f48a5bac136498566b004171130e656b731a7e19e3f3788',
          id=701,
          lineno=3,
          tokens=67,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { pusherClient } from '@/lib/pusher'import { "
               "toPusherKey } from '@/lib/utils'import axios from "
               "'axios'import { Check, UserPlus, X } from 'lucide-react'import "
               "{ useRouter } from 'next/navigation'import { FC, useEffect, "
               "useState } from 'react'"),
 Fragment(document_cs='ec5e157fccbaceea7f48a5bac136498566b004171130e656b731a7e19e3f3788',
          id=702,
          lineno=11,
          tokens=20,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='FriendRequestsProps',
          body='interface FriendRequestsProps {\n'
               '  incomingFriendRequests: IncomingFriendRequest[]\n'
               '  sessionId: string\n'
               '}'),
 Fragment(document_cs='ec5e157fccbaceea7f48a5bac136498566b004171130e656b731a7e19e3f3788',
          id=703,
          lineno=20,
          tokens=4,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='router',
          body='router = useRouter()'),
 Fragment(document_cs='ec5e157fccbaceea7f48a5bac136498566b004171130e656b731a7e19e3f3788',
          id=704,
          lineno=31,
          tokens=49,
          depth=6,
          parent_id=None,
          category='variable',
          summary=False,
          name='friendRequestHandler',
          body='friendRequestHandler = ({\n'
               '      senderId,\n'
               '      senderEmail,\n'
               '    }: IncomingFriendRequest) => {\n'
               '      console.log("function got called")\n'
               '      setFriendRequests((prev) => [...prev, { senderId, '
               'senderEmail }])\n'
               '    }'),
 Fragment(document_cs='ec5e157fccbaceea7f48a5bac136498566b004171130e656b731a7e19e3f3788',
          id=705,
          lineno=49,
          tokens=59,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='acceptFriend',
          body='acceptFriend = async (senderId: string) => {\n'
               "    await axios.post('/api/friends/accept', { id: senderId })\n"
               '\n'
               '    setFriendRequests((prev) =>\n'
               '      prev.filter((request) => request.senderId !== senderId)\n'
               '    )\n'
               '\n'
               '    router.refresh()\n'
               '  }'),
 Fragment(document_cs='ec5e157fccbaceea7f48a5bac136498566b004171130e656b731a7e19e3f3788',
          id=706,
          lineno=59,
          tokens=59,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='denyFriend',
          body='denyFriend = async (senderId: string) => {\n'
               "    await axios.post('/api/friends/deny', { id: senderId })\n"
               '\n'
               '    setFriendRequests((prev) =>\n'
               '      prev.filter((request) => request.senderId !== senderId)\n'
               '    )\n'
               '\n'
               '    router.refresh()\n'
               '  }'),
 Fragment(document_cs='ec5e157fccbaceea7f48a5bac136498566b004171130e656b731a7e19e3f3788',
          id=707,
          lineno=1,
          tokens=71,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: FriendRequestsProps\n'
               '  Variables: acceptFriend denyFriend friendRequestHandler '
               'router\n'
               '  Usages: Check FC FriendRequests IncomingFriendRequest '
               'Nothing UserPlus X aria axios button className console default '
               'div friendRequests here incomingFriendRequests key label '
               'length onClick prev pusherClient request senderId sessionId '
               'setFriendRequests show toPusherKey useEffect useRouter '
               'useState\n'),
 Fragment(document_cs='f1fb401769ae7dd67d29d1d80b3f0df2cbcf454f524c49bc4044353bba33f2db',
          id=708,
          lineno=1,
          tokens=9,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import { z } from 'zod'"),
 Fragment(document_cs='f1fb401769ae7dd67d29d1d80b3f0df2cbcf454f524c49bc4044353bba33f2db',
          id=709,
          lineno=3,
          tokens=32,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='messageValidator',
          body='messageValidator = z.object({\n'
               '  id: z.string(),\n'
               '  senderId: z.string(),\n'
               '  text: z.string(),\n'
               '  timestamp: z.number(),\n'
               '})'),
 Fragment(document_cs='f1fb401769ae7dd67d29d1d80b3f0df2cbcf454f524c49bc4044353bba33f2db',
          id=710,
          lineno=10,
          tokens=9,
          depth=2,
          parent_id=None,
          category='variable',
          summary=False,
          name='messageArrayValidator',
          body='messageArrayValidator = z.array(messageValidator)'),
 Fragment(document_cs='f1fb401769ae7dd67d29d1d80b3f0df2cbcf454f524c49bc4044353bba33f2db',
          id=711,
          lineno=1,
          tokens=16,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: messageArrayValidator messageValidator\n'
               '  Usages: Message infer\n'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=712,
          lineno=1,
          tokens=81,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import ChatInput from '@/components/ChatInput'import Messages "
               "from '@/components/Messages'import { fetchRedis } from "
               "'@/helpers/redis'import { authOptions } from "
               "'@/lib/auth'import { messageArrayValidator } from "
               "'@/lib/validations/message'import { getServerSession } from "
               "'next-auth'import Image from 'next/image'import { notFound } "
               "from 'next/navigation'"),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=713,
          lineno=11,
          tokens=144,
          depth=2,
          parent_id=None,
          category='function',
          summary=False,
          name='generateMetadata',
          body='async function generateMetadata({\n'
               '  params,\n'
               '}: {\n'
               '  params: { chatId: string }\n'
               '}) {\n'
               '  const session = await getServerSession(authOptions)\n'
               '  if (!session) notFound()\n'
               "  const [userId1, userId2] = params.chatId.split('--')\n"
               '  const { user } = session\n'
               '\n'
               '  const chatPartnerId = user.id === userId1 ? userId2 : '
               'userId1\n'
               '  const chatPartnerRaw = (await fetchRedis(\n'
               "    'get',\n"
               '    `user:${chatPartnerId}`\n'
               '  )) as string\n'
               '  const chatPartner = JSON.parse(chatPartnerRaw) as User\n'
               '\n'
               '  return { title: `Macro Integrations Portal | '
               '${chatPartner.name} chat` }\n'
               '}'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=714,
          lineno=37,
          tokens=108,
          depth=1,
          parent_id=None,
          category='function',
          summary=False,
          name='getChatMessages',
          body='async function getChatMessages(chatId: string) {\n'
               '  try {\n'
               '    const results: string[] = await fetchRedis(\n'
               "      'zrange',\n"
               '      `chat:${chatId}:messages`,\n'
               '      0,\n'
               '      -1\n'
               '    )\n'
               '\n'
               '    const dbMessages = results.map((message) => '
               'JSON.parse(message) as Message)\n'
               '\n'
               '    const reversedDbMessages = dbMessages.reverse()\n'
               '\n'
               '    const messages = '
               'messageArrayValidator.parse(reversedDbMessages)\n'
               '\n'
               '    return messages\n'
               '  } catch (error) {\n'
               '    notFound()\n'
               '  }\n'
               '}'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=715,
          lineno=31,
          tokens=17,
          depth=1,
          parent_id=None,
          category='interface',
          summary=False,
          name='PageProps',
          body='interface PageProps {\n  params: {\n    chatId: string\n  }\n}'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=716,
          lineno=16,
          tokens=9,
          depth=4,
          parent_id=None,
          category='variable',
          summary=False,
          name='session',
          body='session = await getServerSession(authOptions)'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=717,
          lineno=21,
          tokens=15,
          depth=4,
          parent_id=None,
          category='variable',
          summary=False,
          name='chatPartnerId',
          body='chatPartnerId = user.id === userId1 ? userId2 : userId1'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=718,
          lineno=22,
          tokens=25,
          depth=4,
          parent_id=None,
          category='variable',
          summary=False,
          name='chatPartnerRaw',
          body='chatPartnerRaw = (await fetchRedis(\n'
               "    'get',\n"
               '    `user:${chatPartnerId}`\n'
               '  )) as string'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=719,
          lineno=26,
          tokens=11,
          depth=4,
          parent_id=None,
          category='variable',
          summary=False,
          name='chatPartner',
          body='chatPartner = JSON.parse(chatPartnerRaw) as User'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=720,
          lineno=39,
          tokens=33,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='results',
          body='results: string[] = await fetchRedis(\n'
               "      'zrange',\n"
               '      `chat:${chatId}:messages`,\n'
               '      0,\n'
               '      -1\n'
               '    )'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=721,
          lineno=46,
          tokens=16,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='dbMessages',
          body='dbMessages = results.map((message) => JSON.parse(message) as '
               'Message)'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=722,
          lineno=48,
          tokens=9,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='reversedDbMessages',
          body='reversedDbMessages = dbMessages.reverse()'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=723,
          lineno=50,
          tokens=11,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='messages',
          body='messages = messageArrayValidator.parse(reversedDbMessages)'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=724,
          lineno=58,
          tokens=62,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='page',
          body='page = async ({ params }: PageProps) => {\n'
               '  const { chatId } = params\n'
               '  const session = await getServerSession(authOptions)\n'
               '  if (!session) notFound()\n'
               '\n'
               '  const { user } = session\n'
               '\n'
               "  const [userId1, userId2] = chatId.split('--')\n"),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=725,
          lineno=60,
          tokens=9,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='session',
          body='session = await getServerSession(authOptions)'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=726,
          lineno=66,
          tokens=215,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='page',
          body='\n'
               '  if (user.id !== userId1 && user.id !== userId2) {\n'
               '    notFound()\n'
               '  }\n'
               '\n'
               '  const chatPartnerId = user.id === userId1 ? userId2 : '
               'userId1\n'
               '  // new\n'
               '\n'
               '  const chatPartnerRaw = (await fetchRedis(\n'
               "    'get',\n"
               '    `user:${chatPartnerId}`\n'
               '  )) as string\n'
               '  const chatPartner = JSON.parse(chatPartnerRaw) as User\n'
               '  const initialMessages = await getChatMessages(chatId)\n'
               '\n'
               '  return (\n'
               "    <div className='flex-1 justify-between flex flex-col "
               "h-full max-h-[calc(100vh-6rem)]'>\n"
               "      <div className='flex sm:items-center justify-between "
               "py-3 border-b-2 border-gray-200'>\n"
               "        <div className='relative flex items-center "
               "space-x-4'>\n"
               "          <div className='relative'>\n"
               "            <div className='relative w-8 sm:w-12 h-8 "
               "sm:h-12'>\n"
               '              <Image\n'
               '                fill\n'
               "                referrerPolicy='no-referrer'\n"
               '                src={chat'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=727,
          lineno=71,
          tokens=15,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='chatPartnerId',
          body='chatPartnerId = user.id === userId1 ? userId2 : userId1'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=728,
          lineno=74,
          tokens=25,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='chatPartnerRaw',
          body='chatPartnerRaw = (await fetchRedis(\n'
               "    'get',\n"
               '    `user:${chatPartnerId}`\n'
               '  )) as string'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=729,
          lineno=78,
          tokens=11,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='chatPartner',
          body='chatPartner = JSON.parse(chatPartnerRaw) as User'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=730,
          lineno=79,
          tokens=10,
          depth=5,
          parent_id=None,
          category='variable',
          summary=False,
          name='initialMessages',
          body='initialMessages = await getChatMessages(chatId)'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=731,
          lineno=90,
          tokens=177,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='page',
          body='Partner.image}\n'
               '                alt={`${chatPartner.name} profile picture`}\n'
               "                className='rounded-full'\n"
               '              />\n'
               '            </div>\n'
               '          </div>\n'
               '\n'
               "          <div className='flex flex-col leading-tight'>\n"
               "            <div className='text-xl flex items-center'>\n"
               "              <span className='text-gray-700 mr-3 "
               "font-semibold'>\n"
               '                {chatPartner.name}\n'
               '              </span>\n'
               '            </div>\n'
               '\n'
               "            <span className='text-sm "
               "text-gray-600'>{chatPartner.email}</span>\n"
               '          </div>\n'
               '        </div>\n'
               '      </div>\n'
               '\n'
               '      <Messages\n'
               '        chatId={chatId}\n'
               '        chatPartner={chatPartner}\n'
               '        sessionImg={session.user.image}\n'
               '        sessionId={session.user.id}\n'
               '        initialMessages={initialMessages}\n'
               '      />\n'
               '      <ChatInput chatId={chatId} chatPartner={chatPartner} />\n'
               '    </div>\n'
               '  )\n'
               '}'),
 Fragment(document_cs='f4a2540dbf76350d51544384ee2baa758c49666b103231d491de8637100c84bf',
          id=732,
          lineno=1,
          tokens=83,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: PageProps\n'
               '  Functions: generateMetadata getChatMessages\n'
               '  Variables: chatPartner chatPartnerId chatPartnerRaw '
               'dbMessages initialMessages messages page results '
               'reversedDbMessages session\n'
               '  Usages: ChatInput Image JSON Message Messages User alt '
               'authOptions chatId className div error fetchRedis fill '
               'getServerSession image message messageArrayValidator name '
               'notFound params referrerPolicy span src user userId1 userId2\n'),
 Fragment(document_cs='f8144960482cd8bc87d590c203c000cd5e837b1732f51cf109f2aada600d5980',
          id=733,
          lineno=1,
          tokens=8,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import Pusher from 'pusher';"),
 Fragment(document_cs='f8144960482cd8bc87d590c203c000cd5e837b1732f51cf109f2aada600d5980',
          id=734,
          lineno=3,
          tokens=59,
          depth=1,
          parent_id=None,
          category='variable',
          summary=False,
          name='pusher',
          body='pusher = new Pusher({\n'
               '     appId: process.env.PUSHER_APP_ID!,\n'
               '     key: process.env.PUSHER_APP_KEY!,\n'
               '     secret: process.env.PUSHER_APP_SECRET!,\n'
               '     cluster: process.env.PUSHER_APP_CLUSTER!,\n'
               '     useTLS: true,\n'
               '   })'),
 Fragment(document_cs='f8144960482cd8bc87d590c203c000cd5e837b1732f51cf109f2aada600d5980',
          id=735,
          lineno=1,
          tokens=14,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: pusher\n  Usages: Pusher process\n'),
 Fragment(document_cs='fa650b380adfabb151a0b352f7135e107e6352345f899060f1c5c231228f94bf',
          id=736,
          lineno=1,
          tokens=6,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Usages: module\n'),
 Fragment(document_cs='facc7446cade5ba4fc50529e7343e63c1c625bcbace0b20fa1de1c40a2c1ed0e',
          id=737,
          lineno=1,
          tokens=24,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import type { Session, User } from 'next-auth'import type { "
               "JWT } from 'next-auth/jwt'"),
 Fragment(document_cs='facc7446cade5ba4fc50529e7343e63c1c625bcbace0b20fa1de1c40a2c1ed0e',
          id=738,
          lineno=7,
          tokens=10,
          depth=4,
          parent_id=None,
          category='interface',
          summary=False,
          name='JWT',
          body='interface JWT {\n    id: UserId\n  }'),
 Fragment(document_cs='facc7446cade5ba4fc50529e7343e63c1c625bcbace0b20fa1de1c40a2c1ed0e',
          id=739,
          lineno=13,
          tokens=18,
          depth=4,
          parent_id=None,
          category='interface',
          summary=False,
          name='Session',
          body='interface Session {\n'
               '    user: User & {\n'
               '      id: UserId\n'
               '    }\n'
               '  }'),
 Fragment(document_cs='facc7446cade5ba4fc50529e7343e63c1c625bcbace0b20fa1de1c40a2c1ed0e',
          id=740,
          lineno=1,
          tokens=13,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Interfaces: JWT Session\n  Usages: User UserId\n'),
 Fragment(document_cs='fb04dc3a588737c3fbe9e37f8b9c26403d6835ce35b9ad3551f95fe5580b1e3b',
          id=741,
          lineno=1,
          tokens=60,
          depth=0,
          parent_id=None,
          category='dependency',
          summary=False,
          name='',
          body="import NextAuth from 'next-auth';import CredentialsProvider "
               "from 'next-auth/providers/credentials';import Providers from "
               "'next-auth/providers';import { authOptions } from "
               "'@/lib/auth';import { fetchRedis } from "
               "'@/helpers/redis';import Auth0Provider from "
               '"next-auth/providers/auth0";'),
 Fragment(document_cs='fb04dc3a588737c3fbe9e37f8b9c26403d6835ce35b9ad3551f95fe5580b1e3b',
          id=742,
          lineno=34,
          tokens=22,
          depth=9,
          parent_id=None,
          category='variable',
          summary=False,
          name='dbUserResult',
          body="dbUserResult = (await fetchRedis('get', `user:${token.id}`)) "
               'as string | null'),
 Fragment(document_cs='fb04dc3a588737c3fbe9e37f8b9c26403d6835ce35b9ad3551f95fe5580b1e3b',
          id=743,
          lineno=44,
          tokens=11,
          depth=9,
          parent_id=None,
          category='variable',
          summary=False,
          name='dbUser',
          body='dbUser = JSON.parse(dbUserResult) as User'),
 Fragment(document_cs='fb04dc3a588737c3fbe9e37f8b9c26403d6835ce35b9ad3551f95fe5580b1e3b',
          id=744,
          lineno=1,
          tokens=35,
          depth=0,
          parent_id=None,
          category='summary',
          summary=True,
          name='',
          body='  Variables: dbUser dbUserResult\n'
               '  Usages: Auth0Provider CredentialsProvider Error JSON '
               'NextAuth Providers User authOptions console credentials '
               'fetchRedis process session token user\n')]