# The Asciidoc SRD5

My rendition of the 5E System Reference Document.

Fully cross-referenced with auto-generated content, extensible, and with multiple output formats including:

* Static HTML
* A bookmarked PDF
* An EPUB

Written as Asciidoc documents for easier editing and extension.
Transformed using DocBook and XSLT for power and programmability.

Forked and derived from the most excellent work of <https://github.com/gguillotte/mdsrd5>

## Reading and Downloading

You can read the books online at: <http://rwdalpe.github.io/srd5/srd/>

You can also download PDFs and EPUBs from the [releases page][2]. PDFs marked
`_basic` are no-frills PDFs useful for people who maybe don't want any images 
and other special design. They're suitable for quick reference and are printer
friendly. Aside from being free of images, the content should be the same as the normal
PDFs.

## Building Your Own Copy

1. Clone the repository
2. Run `git submodule init`
3. Run `git submodule update`
4. Run `./build-deps` or `build-deps.bat` if you're on windows
5. Build the project with gradle `gradle clean buildAll`

## Important Documents

LEGAL: covers legal details for the project

INSTALL: details how to build the project and other technical notes

CONTRIBUTING: instructions and guidelines for contributing to the 
project

## Technical Details

The asciidoc is transformed into DocBook XML with [some extensions][2] I wrote to support RPG elements. 
That transformation is done using [asciidoctor][3].
Then the XML files are piped through the DocBook XSLT 1 and 2 stylesheets (with some extensions by me) to produce the final output.
The build does some final business with moving assets around and packaging.

[1]: https://github.com/rwdalpe/srd5/releases
[2]: https://github.com/rwdalpe/docbook-5.0-extension_rwdalpe-rpg
[3]: http://asciidoctor.org/