---
title: Padel every way
stack: mern
slug: padel-every-way
date: 2021-07-19
thumb: ../images/thumbs/rabbit.png
featuredImg: ../images/featured/rabbit-banner.png
---

# alsdkf

**l alskdf** ökjaös dflskdj fl

## alsdkfj a

_a sdlfj_

````Python
def printToFile(project):
  newFile = f"{projectPath}/{project.slug}.md"
  thumb = f"../images/thumbs/{project.thumb}"
  featured = f"../images/featured/{project.featured}"

  with open(newFile, 'w', encoding='utf8') as f:
    f.write('---\n')
    f.write('title: ' + project.title + '\n')
    f.write('stack: ' + project.stack + '\n')
    f.write('slug: ' + project.slug + '\n')
    f.write('date: ' + project.date + '\n')
    f.write('thumb: ' + thumb + '\n')
    f.write('featuredImg: ' + featured + '\n')
    f.write('---\n\n')
    f.write(project.content + '\n')

    if project.language is not None:
      f.write('\n```' + project.language + '\n')
      f.write(project.code)
      f.write('\n```')


````
