<h3 align="center">
    <a href="https://assetstore.unity.com/packages/tools/video/vlc-for-unity-windows-133979"><img src="/images/Social_Media_Image_1200x630.png"/></a>
</h3>

# VLC for Unity

[![Join the chat at https://discord.gg/3h3K3JF](https://img.shields.io/discord/716939396464508958?label=discord)](https://discord.gg/3h3K3JF)

This repository contains the native Unity plugin that bridges [LibVLCSharp](https://code.videolan.org/videolan/LibVLCSharp) with LibVLC for performance oriented video rendering in Unity3D applications and games. Available on the [Unity Store](https://assetstore.unity.com/packages/tools/video/vlc-for-unity-windows-133979).

- [VLC for Unity](#VLC-for-Unity)
  - [LibVLC Features](#libVLC-Features)
  - [Supported platforms](#supported-platforms)
  - [Installation](#installation)
  - [Getting started](#getting-started)
  - [Documentation](#documentation)
  - [Support](#support)
    - [StackOverflow](#stackoverflow)
  - [Sample scenes](#sample-scenes)
  - [Roadmap](#roadmap)
    - [Future platforms support](#future-platforms-support)
    - [Future graphics APIs](#future-graphics-APIs)
    - [Other improvements](#other-improvements)
  - [Release Notes](#release-Notes)
  - [Building](#building)
  - [Code of Conduct](#code-of-Conduct)
  - [Commercial Services](#commercial-services)
  - [License](#license)

## LibVLC Features

Given that this plugin is using [LibVLCSharp](https://code.videolan.org/videolan/LibVLCSharp) (which uses LibVLC), it exposes more or less the [same feature set](https://code.videolan.org/videolan/LibVLCSharp#features) and same codecs support than VLC, such as:

- Play every media file formats, every codec and every streaming protocols
- Run on every platform, from desktop (Windows, Linux, Mac) to mobile (Android, iOS) and TVs
- Hardware and efficient decoding on every platform, up to 8K
- Network browsing for distant filesystems (SMB, FTP, SFTP, NFS...) and servers (UPnP, DLNA)
- Playback of Audio CD, DVD and Bluray with menu navigation
- Support for HDR, including tonemapping for SDR streams
- Audio passthrough with SPDIF and HDMI, including for Audio HD codecs, like DD+, TrueHD or DTS-HD
- Support for video and audio filters
- Support for 360 video and 3D audio playback, including Ambisonics
- Able to cast and stream to distant renderers, like Chromecast and UPnP renderers.

And more.

## Supported platforms

- Windows Classic
  - Minimum OS version: Windows 7.
  - ABI supported: x64.
  - Graphics API: Direct3D 11
- Windows Modern (UWP)
  - Minimum OS version: Windows 10.
  - ABI supported: x64, ARM64.
  - Graphics API: Direct3D 11
- Android:
  - Minimum OS version: Android 4.2 (API 17).
  - ABIs supposed: armeabi-v7a, arm64-v8a, x86, x86_64.
  - Graphics API: OpenGL ES 2/3

## Installation

The recommended way to install the VLC for Unity plugin is through the [Unity Store](https://assetstore.unity.com/publishers/39987). This also ensures you get commercial support with your build.

| Platform          |  Unity Store Asset                              |
| ----------------- | ----------------------------------------------- |
| Windows           | [![VLCUnityBadge]][VLCUnityWindows]             |
| UWP               | [![VLCUnityBadge]][VLCUnityUWP]                 |
| Android           | [![VLCUnityBadge]][VLCUnityAndroid]             |

[VLCUnityWindows]: https://assetstore.unity.com/packages/tools/video/vlc-for-unity-windows-133979
[VLCUnityUWP]: https://assetstore.unity.com/packages/tools/video/vlc-for-unity-uwp-246153
[VLCUnityAndroid]: https://assetstore.unity.com/packages/tools/video/vlc-for-unity-android-213786

[VLCUnityBadge]: https://img.shields.io/badge/Made%20with-Unity-57b9d3.svg?style=flat&logo=unity

#### [Download the Free Trial Version](https://videolabs.io/#unity).

## Getting started

There is a quick `documentation.txt` file [included in the package](./Assets/VLCUnity/documentation.txt). It gives some context and high level overview of how things work and how to get started.

Since this Unity plugin largely shares the same API than LibVLCSharp, most LibVLCSharp [samples](https://code.videolan.org/mfkl/libvlcsharp-samples) and [documentation](https://code.videolan.org/videolan/LibVLCSharp/tree/3.x/docs) apply, do check those out!

## Documentation

See the [LibVLCSharp documentation](https://code.videolan.org/videolan/LibVLCSharp/tree/master/docs).

It includes [best practices](https://code.videolan.org/videolan/LibVLCSharp/blob/master/docs/best_practices.md), [Q&A guide](https://code.videolan.org/videolan/LibVLCSharp/blob/master/docs/how_do_I_do_X.md), [libvlc specific information](https://code.videolan.org/videolan/LibVLCSharp/blob/master/docs/libvlc_documentation.md) and [tutorials](https://code.videolan.org/videolan/LibVLCSharp/blob/master/docs/tutorials.md).

## Support

Support is done on a volunteer base, professional support is only available for [paying customers](https://assetstore.unity.com/packages/tools/video/vlc-for-unity-windows-133979).

### StackOverflow

We regularly monitor the [![stackoverflow-libvlcsharp](https://img.shields.io/stackexchange/stackoverflow/t/libvlcsharp.svg?label=libvlcsharp&style=flat)](https://stackoverflow.com/questions/tagged/libvlcsharp) and [![stackoverflow-vlc-unity](https://img.shields.io/stackexchange/stackoverflow/t/vlc-unity.svg?label=vlc-unity&style=flat)](https://stackoverflow.com/questions/tagged/vlc-unity) tags on StackOverflow.

