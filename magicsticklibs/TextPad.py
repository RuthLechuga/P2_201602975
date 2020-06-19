#!/usr/bin/python
##
##
##    Developed by:   Suraj Singh
##                    surajsinghbisht054@gmail.com
##					  github.com/surajsinghbisht054
## 					  http://bitforestinfo.blogspot.com
##
##    Permission is hereby granted, free of charge, to any person obtaining
##    a copy of this software and associated documentation files (the
##    "Software"), to deal with the Software without restriction, including
##    without limitation the rights to use, copy, modify, merge, publish,
##    distribute, sublicense, and/or sell copies of the Software, and to
##    permit persons to whom the Software is furnished to do so, subject to
##    the following conditions:
##
##    + Redistributions of source code must retain the above copyright
##      notice, this list of conditions and the following disclaimers.
##
##    + Redistributions in binary form must reproduce the above copyright
##      notice, this list of conditions and the following disclaimers in the
##      documentation and/or other materials provided with the distribution.
##
##    + Neither the names of Suraj Singh
##                    surajsinghbisht054@gmail.com
##					  github.com/surajsinghbisht054
## 					  http://bitforestinfo.blogspot.com nor
##      the names of its contributors may be used to endorse or promote
##      products derived from this Software without specific prior written
##      permission.
##
##    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
##    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
##    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
##    IN NO EVENT SHALL THE CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR
##    ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
##    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
##    THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH THE SOFTWARE.
##
##
## ################################################
## ###### Please Don't Remove Author Name #########
## ############# Thanks ###########################
## ################################################
##
##
__author__='''
    Suraj Singh
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.com/
'''
if __name__=='__main__':
	from Graphics import Tkinter
	from ConfigSettings import Connect
else:
	from .Graphics import Tkinter
	from .ConfigSettings import Connect

class TextPad(Tkinter.Text):
	def __init__(self, *args, **kwargs):
		Tkinter.Text.__init__(self, *args, **kwargs)
		self.storeobj = {"Root": self.master}
		self.Connect_External_Module_Features()
		self._pack()
		return

	def Connect_External_Module_Features(self):
		Connect(self)
		return

	def _pack(self):
		self.pack(expand = False, fill = "x", side="top")
		return
	
	def get_text(self):
		return self.get("1.0",'end')
	
	def delete_text(self):
		self.delete('1.0', Tkinter.END)

	def insert_text(self,data):
		self.insert('1.0',data)
	
	def change_color(self,color):
		self.config(bg=color)
	
	def resaltar(self,start):
		self.tag_add("debug", float(start), float(start+1))
		self.tag_config("debug", background="yellow", foreground="blue")
	
	def deleteResaltar(self):
		self.tag_delete("debug")

if __name__ == '__main__':
	root = Tkinter.Tk(className = " Test TextPad")
	TextPad(root)
	root.mainloop()
