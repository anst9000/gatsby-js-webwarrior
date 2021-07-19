class Project:
  def __init__(self, path, date, title, stack, content, language, code):
    self.path = path
    self.date = date
    self.title = title
    self.stack = stack
    self.content = content
    self.language = language
    self.code = code
    self.slug = self.createSlug()

  def __str__(self):
    if self.language is not None:
      return f'''---
path: {self.path}
date: {self.date}
title: {self.title}
stack: {self.stack}
---

{self.content}

```{self.language}
{self.code}


'''
    else:
      return f'''---
path: {self.path}
date: {self.date}
title: {self.title}
stack: {self.stack}
---

{self.content}
'''

  def createSlug(self):
    return self.title.toLowerCase().replace(" ", "-")

