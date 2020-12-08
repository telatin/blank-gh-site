---
title: Nannochloropsis genome portal end of life
tags:
  - bioinformatics
---

During my PhD (2012), I made the *Nannochloropsis gaditana* genome portal,
and also secured the *nannochloropsis.org* domain for it.

![Nannochloropsis portal icons]({{ site.baseurl }}{% link images/2013-10-22-nannochloropsis.png %})

<!--more-->
After 8 years, I realised that most of the resources it was hosting
where no longer being maintained by the original department,
and most of the features of the site were no longer needed.

Retrospectively, it has been amazing to maintain a genomic website for 8 years,
see its usage statistics with thousands downloads from the US, latin America,
Europe, and Asia.

From my side it was an interesting ride into **PHP**, a language that I don't
love but don't dislike too much, and **Ajax**, that made it's appearance in my
automatic primer picker.

## Automatic primer picker

This is a small screencast I made **7 years** ago.

<iframe src="https://player.vimeo.com/video/69833362" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

The idea was to allow to design
primers to close gaps between contigs, so it was offering to assist in the selection
using the known information from mate paired reads.


## Blast with GBrowse integration

Managing the whole server allowed for interesting integrations, for example the
genomic preview of BLAST results, to see if the query sequence was aligned near
or withing known (annotated) genes:

<iframe src="https://player.vimeo.com/video/56845429" width="640" height="480" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
<p><a href="https://vimeo.com/56845429">Blast interface demo</a> from <a href="https://vimeo.com/telatin">Andrea Telatin</a> on <a href="https://vimeo.com">Vimeo</a>.</p>
