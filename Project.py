class Project:
  def __init__(self, date, title, stack, content, thumb, featured, language = None, code = None):
    self.date = date
    self.title = title
    self.stack = stack
    self.content = content
    self.thumb = thumb
    self.featured = featured
    self.language = language
    self.code = code
    self.slug = self.createSlug()

  def __str__(self):
    if self.language is not None:
      return f'''---
title: {self.title}
stack: {self.stack}
slug: {self.slug}
date: {self.date}
thumb: {self.thumb}
featuredImg: {self.featured}
---

{self.content}

```{self.language}
{self.code}
'''
    else:
      return f'''---
title: {self.title}
stack: {self.stack}
slug: {self.slug}
date: {self.date}
thumb: {self.thumb}
featuredImg: {self.featured}
---

{self.content}
'''

  def createSlug(self):
    return self.title.lower().replace(" ", "-")
