"""
https://chat.openai.com/share/22b71474-0242-469d-a471-03150095b8ea

When I start my Python Web service I often get this error: `OSError: [Errno 98] Address already in use`
I'm pretty sure no other instance is running on that port, but the previous one was killed just a fraction of a second before starting the new one.
The Web framework used is Quart, which makes it difficult to set a socket option. Especially when the service is running via hypercorn in production.
How can I get rid of the occasional errors on startup?

How can I monkey-patch the socket opening in the library used by Quart and hypercorn to set the `SO_REUSEADDR` socket option regardless?

"""
import sys

if sys.platform == 'linux':

    import asyncio
    import socket


    class ReuseAddrServer(asyncio.Server):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for sock in self.sockets:
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    class ReuseAddrEventLoop(asyncio.SelectorEventLoop):
        async def create_server(self, *args, **kwargs):
            server = await super().create_server(*args, **kwargs)
            return ReuseAddrServer(*server.args, **server.kwargs)


    class ReuseAddrEventLoopPolicy(asyncio.DefaultEventLoopPolicy):
        _loop_factory = ReuseAddrEventLoop


    # Apply the custom event loop policy
    def patch_reuse_addr(patched=[]):
        if patched:
            return

        asyncio.set_event_loop_policy(ReuseAddrEventLoopPolicy())
        patched.append(True)

    # Then start your server as normal...
else:
    def patch_reuse_addr():
        pass
