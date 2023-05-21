# AskYourCode ChatGPT plugin

Ask your source code directly. The intelligent rubber ducky!

This plugin provides access to the source code and documentation of a software project provided by the user.

## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin's API backend, enter the following command:

```bash
python plugin/plugin_server.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a question like "What is on my todo list" and then try adding something to it as well! 

## How to use the plugin

1. Install the **AskYourCode** plugin on ChatGPT's Web UI.
2. Enable the **AskYourCode** plugin.
3. Compress the source code of your project as a `zip` or `tar.gz` archive. 
4. **Share the archive file** on the Internet in a way that the plugin can access it directly without authentication. The URL should be cryptic, so nobody can find it easily.
5. Open a new chat.
6. Enter: **AskYourCode YOUR-URL-HERE**
7. The plugin's backend server will download your archive, extract the source code, split it into small fragments and store into a vector database.
8. The plugin will report back with a GUID, that's the unique identifier of your project. You can refer to this project later without having to upload it again.
9. 

## Limits

### ChatGPT account

You must be logged in on CharGPT to use this plugin.

### Usage limits

#### Free usage

- Up to 100kB decompressed source code archive. Please subscribe to work on bigger projects.
- Up to 3 project uploads per hour.
- Up to 30 requests per hour.
- Up to 8 hours of project retention time after last use.

#### Subscribers

- Up to 10MB decompressed source code archive. Please split your project or remove unnecessary files.
- Up to 30 project uploads per hour.
- Up to 600 requests per hour (pretty much unlimited).
- Up to 30 days of project retention time after last use.

Paid accounts are not available yet. Please leave your email address
to express your interest in a paid subscription. Once we have enough
signups it will happen.

TODO: Way to sign interest

Planned price: $10/month

### Supported file types

Only files of know types are stored in the vector database and made accessible to ChatGPT. 
The rest of files are ignored, but still count towards the project size limit.

- Source code files of all supported languages (see below)
- Text (.txt) and Markdown (.md) documents

Planned:
- Binary documentation (.doc, .doct, .odt, .pdf, .rtf)
- Textual data (.csv, .tsv)
- Spreadsheets (.xls, .xlsx, .ods) 

### Supported programming languages

Source code files of the supported programming languages are split into logical fragments 
and made accessible to ChatGPT with proper metadata, so the LLM can reason about your code.

Programming languages with support planned are recognized and fragmented the same way as
text documents. They don't get proper metadata, but the LLM can still access those source files.

Supported:
- Text
- Markdown
- Python
- Shell
- C#
- C
- C++
- Rust
- Zig
- Java
- JavaScript
- SQL
- CSS
- HTML

TODO: Way to request more languages and doc formats.

## Security

Only your ChatGPT user can access your projects, even if others would know its unique identifier.

- All fragments are encrypted on transit (HTTPS) and storage in the vector database. 
- Metadata in the vector database is not encrypted.

## Deleting projects

- To delete a project: **AskYourCode delete project YOUR-PROJECT-ID-HERE**
- To delete all projects: **AskYourCode delete all my projects**

## Assumptions

- All textual source files are UTF-8 encoded. 

## Best practices

TODO

## Roadmap

- Paid subscription with increased limits, required for sustainable service
- Agent to upload source directly form the user's machine (no need to upload an archive)

## Citations

- [Instructor-XL](https://huggingface.co/hkunlp/instructor-xl)

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
