from tkinter import *
import os, sys
from datetime import date
import textwrap
from Project import Project

fields = ('Title', 'Stack', 'Content', 'Thumbnail', 'Image', 'Language', 'Code')


def fixText(text):
  returnText = ''
  lines = text.split('\n')
  print(lines)
  for line in lines:
    print(line)
    if len(line) > 60:
      returnText = returnText + textwrap.fill(line, 60) + '\n'
    else:
      returnText = returnText + line + '\n'

  return returnText


def printFields(entries):
  attr_list = []
  date = dateToday
  attr_list.append(date)

  for field in fields:
    attribute = ''
    if field == 'Content' or field == 'Code':
      attribute = entries[field].get("1.0","end-1c")
      attribute = fixText(attribute)

    else:
      attribute = entries[field].get()

    attr_list.append(attribute)

  index = 1
  for item in attr_list:
    print(index, item)
    index += 1
  newProject = Project(attr_list[0], attr_list[1], attr_list[2], attr_list[3], attr_list[4], attr_list[5], attr_list[6], attr_list[7])
  print(newProject)
  printToFile(newProject)

  root.destroy()


def makeform(root, fields):
  heading = Label(text="Enter Project info", width="300", height="2", font=("Calibri", 20)).pack()

  entries = {}
  for field in fields:
    row = Frame(root)
    lab = Label(row, width=10, text=field + ": ", anchor='w')
    lab.config(font=("Consolas", 14))
    if field == 'Content' or field == 'Code':
      print('This is ' + field)
      ent = Text(row, height=5, width=10, wrap=WORD)
    else:
      ent = Entry(row)

    ent.config(font=("Source Code Pro", 12))
    row.pack(side = TOP, fill = X, padx = 25 , pady = 5)
    lab.pack(side = LEFT)
    ent.pack(side = RIGHT, expand = YES, fill = X)
    entries[field] = ent
  return entries

def dirCount():
  count1 = 1
  for root, dirs, files in os.walk(projectPath):
    count1 += len(dirs)

  return str(count1).zfill(3)


def getDate():
  today = date.today()
  return today.strftime("%Y-%m-%d")

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


if __name__ == '__main__':
  root = Tk()
  root.geometry("800x600")
  ents = makeform(root, fields)
  root.bind('<Return>', (lambda event, e = ents: fetch(e)))

  b1 = Button(root, text = 'Submit', command=(lambda e = ents: printFields(e)), bg='#00ff00', fg='#333333', font=('helvetica', 9, 'bold'))
  b1.config(font=("Consolas", 14))
  b1.pack(side = RIGHT, padx = 50, pady = 5)

  currentPath = os.getcwd()
  projectPath = "./src/projects/"
  dateToday = getDate()

  # numberOfDirectories = dirCount()
  # printToFile(newBlog)
  # print(newBlog)

  root.mainloop()