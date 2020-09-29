
# groff
- `groff -ms file.ms -T pdf > file.pdf` - to compile
- syntax of file.ms
```
.TL
This is title
.AU
Vladimir
.AI
My university
.NH
This is a section. This will be bold and have order number (works in all .NH)
.PP
Paragraph starts indented
This sentence will be in the same row.
This sentence will be in the same row.
This sentence will be in the same row.

this sentense will be in next row, but not indented (because is now marked as paragraph)

.NH 1
this is same as .NH
.NH 2
This is a subsection
.PP
Here's the weird thing
This is how i make words
.B "bold words"
to be bold
.RS
.PP
This p will be indented
.RE
.SH
This is an unnumbered heading
```
